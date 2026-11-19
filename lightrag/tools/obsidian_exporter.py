"""
Obsidian Bilingual Exporter for LightRAG.
Generates structured bilingual (English & Vietnamese) Chapter-by-Chapter Markdown notes
tailored for Obsidian Brain:
- Detects document Parts & Chapters (via TOC/structure) and writes one comprehensive
  bilingual note per chapter (`{doc} - Chương XX - {title}.md`) plus a Roadmap MOC.
- Connects chapters sequentially (Previous | Roadmap | Next) and links them from the
  document's Bilingual Summary note.
- Prunes any unresolved wikilinks so Obsidian Graph View contains zero empty/ghost nodes.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from google import genai

logger = logging.getLogger("lightrag")

DEFAULT_OBSIDIAN_VAULT = r"C:\Users\hiepnc1\Documents\Obsidian Vault"
DEFAULT_LOCAL_BACKUP = r"D:\hiepnc\obsidian_brain"

_WIKILINK_RE = re.compile(r"\[\[([^\[\]]+)\]\]")


def get_obsidian_dirs() -> tuple[Path, Path]:
    """Resolve destination directories from environment or defaults."""
    vault_env = os.getenv("OBSIDIAN_VAULT_DIR", DEFAULT_OBSIDIAN_VAULT)
    local_env = os.getenv("OBSIDIAN_LOCAL_BACKUP_DIR", DEFAULT_LOCAL_BACKUP)

    vault_path = Path(vault_env)
    local_path = Path(local_env)

    vault_path.mkdir(parents=True, exist_ok=True)
    local_path.mkdir(parents=True, exist_ok=True)

    return vault_path, local_path


def sanitize_filename(name: str, keep_spaces: bool = False) -> str:
    """Sanitize title or filename for filesystem safety."""
    name = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    if not keep_spaces:
        name = name.replace(" ", "-")
    return name.strip(".-") or "Document-Summary"


def prune_unresolved_wikilinks(target_dir: Path, vault_root: Path | None = None) -> int:
    """Replace unresolved [[wikilinks]] across Markdown files in target_dir with bold text.

    Ensures Obsidian Graph View contains zero empty/ghost nodes and only displays
    populated main documents, chapter summaries, and roadmap notes.
    """
    if not target_dir.exists():
        return 0

    search_root = vault_root if vault_root and vault_root.exists() else target_dir
    valid_targets: set[str] = {p.stem for p in search_root.rglob("*.md")}
    for canvas_file in search_root.rglob("*.canvas"):
        valid_targets.add(canvas_file.name)
        valid_targets.add(canvas_file.stem)

    md_files = list(target_dir.glob("*.md"))

    pruned_count = 0

    def _replace_match(match: re.Match[str]) -> str:
        nonlocal pruned_count
        inner = match.group(1)
        if "|" in inner:
            target_part, display_part = inner.split("|", 1)
        else:
            target_part, display_part = inner, inner

        page_name = target_part.split("#", 1)[0].strip()
        if page_name in valid_targets:
            return match.group(0)

        pruned_count += 1
        return f"**{display_part.strip()}**"

    for md_path in md_files:
        original = md_path.read_text(encoding="utf-8")
        updated = _WIKILINK_RE.sub(_replace_match, original)
        if updated != original:
            md_path.write_text(updated, encoding="utf-8")

    if pruned_count:
        logger.info("Pruned %d unresolved wikilink(s) in %s", pruned_count, target_dir)
    return pruned_count


async def _generate_text(
    client: genai.Client,
    model_name: str,
    prompt: str,
) -> str:
    """Run Gemini generate_content in default thread executor."""
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(
        None,
        lambda: client.models.generate_content(
            model=model_name,
            contents=prompt,
        ),
    )
    return response.text or ""


def _extract_json_array(raw_text: str) -> list[dict[str, Any]]:
    """Strip optional markdown code fences and parse a JSON list."""
    cleaned = raw_text.strip()
    fence_match = re.search(r"```(?:json)?\s*(\[[\s\S]*?\])\s*```", cleaned)
    if fence_match:
        cleaned = fence_match.group(1)
    else:
        bracket_match = re.search(r"(\[[\s\S]*\])", cleaned)
        if bracket_match:
            cleaned = bracket_match.group(1)
    data = json.loads(cleaned)
    return data if isinstance(data, list) else []


def _slice_chapter_context(
    content: str,
    title_hint: str,
    chapter_idx: int,
    total_chapters: int,
    max_chars: int = 16000,
) -> str:
    """Locate a chapter's body slice, skipping front-matter TOC when searching."""
    if not content:
        return ""
    body_start = min(len(content) // 12, 20000)
    search_space = content[body_start:]
    match_pos = -1
    if title_hint:
        idx = search_space.lower().find(title_hint.lower())
        if idx != -1:
            match_pos = body_start + idx

    if match_pos == -1:
        chunk_len = max(1, (len(content) - body_start) // max(1, total_chapters))
        match_pos = body_start + chapter_idx * chunk_len

    return content[match_pos : match_pos + max_chars]


async def _extract_chapter_outline(
    client: genai.Client,
    model_name: str,
    title: str,
    content_sample: str,
    entities_sample: list[str],
) -> list[dict[str, Any]]:
    """Identify document chapters/parts from TOC and opening text."""
    entities_text = ", ".join(entities_sample[:60]) if entities_sample else title
    prompt = f"""Analyze the opening / Table of Contents of the document titled "{title}" and extract its main Chapters (or primary logical sections if the document has no numbered chapters).

Document opening & TOC text:
{content_sample[:18000]}

Extracted entities context:
{entities_text}

Return STRICTLY a valid JSON array (up to 20 chapters; no text outside JSON) where each item has:
{{
  "chapter_num": 1,
  "part_num": 1,
  "part_label": "Phần 1: Tên phần bằng tiếng Việt (hoặc 'Nội dung chính')",
  "title_vi": "Tên chương ngắn gọn bằng tiếng Việt (English Title)",
  "title_hint": "Exact English heading or short phrase to locate this chapter in text"
}}
"""
    raw = await _generate_text(client, model_name, prompt)
    outline = _extract_json_array(raw)
    return outline[:20]


async def generate_bilingual_summary(
    title: str,
    content_sample: str,
    entities_sample: list[str],
    api_key: str,
    model_name: str = "gemini-3.5-flash-lite",
) -> str:
    """Call Gemini to generate an Obsidian-formatted bilingual overall summary note."""
    client = genai.Client(api_key=api_key)
    entities_text = (
        ", ".join(entities_sample[:60])
        if entities_sample
        else "Core Architecture, Components, Workflows, Best Practices"
    )

    prompt = f"""You are an expert technical author and Knowledge Management Specialist specializing in Obsidian Second Brain PKM.
Create an in-depth, comprehensive, beautifully structured BILINGUAL (Vietnamese & English) Markdown overview note for the document/book titled: "{title}".

Reference Extracted Concepts/Entities (mention naturally in bold/code; do NOT create [[wikilinks]] to individual terms):
{entities_text}

Document Context & Content Excerpt:
{content_sample[:18000]}

---
INSTRUCTIONS & OBSIDIAN FORMAT REQUIREMENTS:
1. Start with YAML Frontmatter:
---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d')}
tags:
  - lightrag
  - summary
  - bilingual
  - obsidian-brain
source: "{title}"
language: bilingual
---

2. Note Structure:
Include TWO complete, rich, standalone sections:
# 🇻🇳 BẢN TÓM TẮT TIẾNG VIỆT
- **Tổng quan & Mục đích cốt lõi**: Nêu rõ tài liệu nói về cái gì, giải quyết bài toán gì.
- **Kiến trúc & Các thành phần trọng tâm**: Phân tích chi tiết từng khối kiến trúc.
- **Tóm lược chi tiết từng chương / phần chính**: Tóm lược theo từng chương.
- **Bảng tra cứu câu lệnh / Khái niệm thực chiến (Cheatsheet)**: Bảng markdown các mục quan trọng kèm mô tả chức năng.
- **Best Practices & Lưu ý khi triển khai thực tế**: Các kinh nghiệm thực tiễn, tối ưu hiệu năng, bảo mật.

# 🇬🇧 COMPREHENSIVE ENGLISH SUMMARY
- **Executive Summary & Core Objectives**: High-level overview of the material.
- **System Architecture & Key Components**: Detailed technical breakdown of the architecture and components.
- **Chapter-by-Chapter Overview**: Concise breakdown across chapters/parts.
- **Essential Reference & Recipes**: Markdown table of crucial commands/patterns and practical tips.
- **Production Best Practices & Pitfalls to Avoid**: Key principles, constraints, and recommendations.

3. Formatting rules:
- Use Obsidian Callouts like `> [!tip]`, `> [!note]`, `> [!warning]`, `> [!info]` where appropriate.
- Do NOT wrap random nouns or concepts in `[[wikilinks]]` — use **bold** or `code` instead so Obsidian Graph View stays clean.
"""
    return await _generate_text(client, model_name, prompt)


async def _generate_single_chapter_note(
    client: genai.Client,
    model_name: str,
    doc_title: str,
    chapter_info: dict[str, Any],
    chapter_context: str,
    summary_stem: str,
    roadmap_stem: str,
    prev_stem: str | None,
    next_stem: str | None,
) -> str:
    """Generate one comprehensive bilingual Obsidian note for a single chapter."""
    ch_num = int(chapter_info.get("chapter_num", 1))
    part_num = int(chapter_info.get("part_num", 1))
    part_label = str(chapter_info.get("part_label", f"Phần {part_num}")).strip()
    title_vi = str(chapter_info.get("title_vi", f"Chương {ch_num:02d}")).strip()

    prompt = f"""You are an expert technical writer summarizing Chapter {ch_num} ("{title_vi}") of "{doc_title}" for an Obsidian Second Brain.

Chapter Context Excerpt:
{chapter_context}

Write a structured BILINGUAL chapter summary with these exact headings (NO YAML frontmatter needed, NO [[wikilinks]] inside body prose — use **bold** or `code` for technical terms):

> [!info] **{part_label}**
> 🇻🇳 **Trọng tâm chương**: (2-3 sentence summary in Vietnamese covering all sections of this chapter)
>
> 🇬🇧 **Executive Summary**: (2-3 sentence summary in English)

---

## 🇻🇳 PHÂN TÍCH CHI TIẾT TỪNG MỤC (TIẾNG VIỆT)
(Provide detailed bulleted subsections matching the chapter sections, explaining mechanics, workflows, and caveats deeply.)

---

## 🛠️ Bảng Câu lệnh / Điểm Trọng tâm Chương
| Mục / Câu lệnh | Chức năng & Ý nghĩa |
| :--- | :--- |
(Include 4-6 practical rows relevant to this chapter)

---

## 🇬🇧 COMPREHENSIVE ENGLISH CHAPTER SUMMARY
(Clear, concise subsection-by-subsection English breakdown)

---

## 💡 Đúc kết & Thực hành Tốt nhất (Key Takeaways)
(2-4 actionable takeaways in Vietnamese)
"""
    body = await _generate_text(client, model_name, prompt)

    prev_link = f"⬅ **[[{prev_stem}]]**" if prev_stem else "⬅ *(Chương đầu tiên)*"
    next_link = f"**[[{next_stem}]]** ➔" if next_stem else "*(Chương cuối cùng)* ➔"

    frontmatter = f"""---
title: "Chương {ch_num:02d}: {title_vi}"
chapter: {ch_num}
part: {part_num}
type: chapter-summary
tags:
  - lightrag
  - chapter
  - part-{part_num}
  - obsidian-brain
source: "[[{summary_stem}]]"
---

# 📖 Chương {ch_num:02d}: {title_vi}

"""
    footer = f"""

---

## 🧭 Điều hướng Chương
{prev_link} &nbsp;|&nbsp; 🧭 **[[{roadmap_stem}]]** &nbsp;|&nbsp; {next_link}

* 📖 Quay về bản tóm tắt tổng thể: **[[{summary_stem}]]**
"""
    return frontmatter + body.strip() + footer


async def generate_chapter_summaries_for_doc(
    title: str,
    content_sample: str,
    entities_sample: list[str],
    summary_stem: str,
    api_key: str,
    model_name: str,
    target_dirs: list[Path],
) -> list[str]:
    """Identify chapters in any document and generate bilingual Chapter Notes + a Roadmap MOC."""
    client = genai.Client(api_key=api_key)
    safe_prefix = sanitize_filename(title)[:40]

    outline = await _extract_chapter_outline(
        client=client,
        model_name=model_name,
        title=title,
        content_sample=content_sample,
        entities_sample=entities_sample,
    )
    if not outline:
        return []

    roadmap_stem = f"{safe_prefix} - 00 - Mục lục & Lộ trình Đọc"
    stems: list[str] = []
    for idx, ch in enumerate(outline, start=1):
        ch_num = int(ch.get("chapter_num", idx))
        ch["chapter_num"] = ch_num
        ch_title = str(ch.get("title_vi", f"Chương {ch_num:02d}")).strip()
        short_title = sanitize_filename(ch_title, keep_spaces=True)[:70]
        stems.append(f"{safe_prefix} - Chương {ch_num:02d} - {short_title}")

    total_ch = len(outline)
    for idx, ch in enumerate(outline):
        prev_stem = stems[idx - 1] if idx > 0 else None
        next_stem = stems[idx + 1] if idx < total_ch - 1 else None
        ctx_slice = _slice_chapter_context(
            content=content_sample,
            title_hint=str(ch.get("title_hint", ch.get("title_vi", ""))),
            chapter_idx=idx,
            total_chapters=total_ch,
        )
        note_text = await _generate_single_chapter_note(
            client=client,
            model_name=model_name,
            doc_title=title,
            chapter_info=ch,
            chapter_context=ctx_slice,
            summary_stem=summary_stem,
            roadmap_stem=roadmap_stem,
            prev_stem=prev_stem,
            next_stem=next_stem,
        )
        fname = f"{stems[idx]}.md"
        for out_dir in target_dirs:
            (out_dir / fname).write_text(note_text, encoding="utf-8")

    # Build Roadmap MOC linking Parts & Chapters in reading order
    mermaid_edges = "\n".join(
        f'    C{i:02d}["[[{stems[i]}]]"] --> C{i + 1:02d}["[[{stems[i + 1]}]]"]'
        for i in range(total_ch - 1)
    )
    if total_ch == 1:
        mermaid_edges = f'    C00["[[{stems[0]}]]"] --> Sum["[[{summary_stem}]]"]'
    else:
        mermaid_edges += f'\n    C{total_ch - 1:02d}["[[{stems[-1]}]]"] --> Sum["[[{summary_stem}]]"]'

    checklist_lines = "\n".join(f"- [ ] **[[{s}]]**" for s in stems)
    roadmap_note = f"""---
title: "{title} - Mục lục & Lộ trình Đọc"
type: roadmap
tags:
  - lightrag
  - roadmap
  - moc
  - obsidian-brain
---

# 📚 Mục lục & Lộ trình Đọc: {title}

> [!tip] **Tóm tắt theo từng Chương**
> Toàn bộ tài liệu **{title}** được chia gọn thành **{total_ch} Chương** có liên kết tuần tự — không sinh các node khái niệm nhỏ lẻ.

## 🗺️ Sơ đồ Lộ trình
```mermaid
flowchart TD
{mermaid_edges}
```

## 📖 Danh sách Chương
{checklist_lines}

## 📌 Tóm tắt Tổng thể
- **[[{summary_stem}]]**
"""
    for out_dir in target_dirs:
        (out_dir / f"{roadmap_stem}.md").write_text(roadmap_note, encoding="utf-8")

    # Add Roadmap + Chapter index banner to the main Bilingual Summary note
    chapter_bullets = "\n".join(f"- **[[{s}]]**" for s in stems)
    banner = (
        f"> [!tip] 🧭 **Xem tóm tắt chi tiết từng chương:** Mở **[[{roadmap_stem}]]**\n\n"
        f"### 📚 Danh sách các Chương\n{chapter_bullets}\n\n"
    )
    for out_dir in target_dirs:
        summary_path = out_dir / f"{summary_stem}.md"
        if summary_path.exists():
            existing_txt = summary_path.read_text(encoding="utf-8")
            if roadmap_stem not in existing_txt:
                existing_txt = existing_txt.replace(
                    "# 🇻🇳 BẢN TÓM TẮT TIẾNG VIỆT\n",
                    f"# 🇻🇳 BẢN TÓM TẮT TIẾNG VIỆT\n\n{banner}",
                    1,
                )
                summary_path.write_text(existing_txt, encoding="utf-8")

    return stems


async def export_document_to_obsidian_async(
    doc_id: str,
    title: str,
    content: str,
    entities: list[str] | None = None,
    generate_chapters: bool = True,
) -> dict[str, Any]:
    """Asynchronous function called by the ingestion pipeline or REST API."""
    load_dotenv(r"D:\hiepnc\.env")
    api_key = os.getenv("LLM_BINDING_API_KEY")
    if not api_key:
        logger.warning("Obsidian export skipped: LLM_BINDING_API_KEY missing.")
        return {"status": "skipped", "reason": "no_api_key"}

    vault_root, local_root = get_obsidian_dirs()
    book_folder = sanitize_filename(title)
    vault_dir = vault_root / book_folder
    local_dir = local_root / book_folder
    vault_dir.mkdir(parents=True, exist_ok=True)
    local_dir.mkdir(parents=True, exist_ok=True)

    summary_stem = f"{book_folder}-Bilingual-Summary"
    filename = f"{summary_stem}.md"

    vault_target = vault_dir / filename
    local_target = local_dir / filename
    model_name = os.getenv("LLM_MODEL", "gemini-3.5-flash-lite")

    try:
        summary_text = await generate_bilingual_summary(
            title=title,
            content_sample=content,
            entities_sample=entities or [],
            api_key=api_key,
            model_name=model_name,
        )

        vault_target.write_text(summary_text, encoding="utf-8")
        local_target.write_text(summary_text, encoding="utf-8")

        chapters_created: list[str] = []
        if generate_chapters:
            try:
                chapters_created = await generate_chapter_summaries_for_doc(
                    title=title,
                    content_sample=content,
                    entities_sample=entities or [],
                    summary_stem=summary_stem,
                    api_key=api_key,
                    model_name=model_name,
                    target_dirs=[vault_dir, local_dir],
                )
            except Exception as e_ch:
                logger.warning("Auto chapter summary generation notice: %s", e_ch)

        # Keep Obsidian Graph View clean: remove any unresolved ghost wikilinks
        prune_unresolved_wikilinks(vault_dir, vault_root=vault_root)
        prune_unresolved_wikilinks(local_dir, vault_root=local_root)

        logger.info(
            "Successfully exported bilingual Obsidian summary (%d chapters): %s",
            len(chapters_created),
            vault_target,
        )
        return {
            "status": "success",
            "doc_id": doc_id,
            "title": title,
            "vault_path": str(vault_target),
            "local_path": str(local_target),
            "filename": filename,
            "chapters_count": len(chapters_created),
        }
    except Exception as e:
        logger.error("Failed to generate Obsidian summary for %s: %s", doc_id, e)
        return {"status": "error", "error": str(e)}


def export_document_by_id(
    doc_id: str,
    rag_dir: str = r"D:\hiepnc\rag_storage",
) -> dict[str, Any]:
    """Synchronous/CLI helper to export a document from local storage."""
    full_docs_file = Path(rag_dir) / "kv_store_full_docs.json"
    cache_file = Path(rag_dir) / "kv_store_llm_response_cache.json"

    if not full_docs_file.exists():
        raise FileNotFoundError(f"Cannot find {full_docs_file}")

    with open(full_docs_file, "r", encoding="utf-8") as f:
        full_docs = json.load(f)

    doc = full_docs.get(doc_id)
    if not doc:
        for k, v in full_docs.items():
            if doc_id in k or doc_id == v.get("file_path"):
                doc = v
                doc_id = k
                break

    if not doc:
        raise ValueError(f"Document with ID or filename '{doc_id}' not found in storage.")

    file_path = doc.get("file_path", doc_id)
    title = Path(file_path).stem
    content = doc.get("content", "")

    entities: list[str] = []
    if cache_file.exists():
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cache_data = json.load(f)
            for v in cache_data.values():
                val_text = v.get("return", "")
                for line in val_text.splitlines():
                    if "entity<|#|>" in line or "entity\t" in line:
                        parts = re.split(r"<\|#\|>|\t", line)
                        if len(parts) >= 2 and parts[1].strip():
                            entities.append(parts[1].strip())
                    elif line.startswith('"entity_name":'):
                        m = re.search(r'"entity_name":\s*"([^"]+)"', line)
                        if m:
                            entities.append(m.group(1))
        except Exception:
            pass

    entities = list(dict.fromkeys(entities))
    return asyncio.run(
        export_document_to_obsidian_async(
            doc_id=doc_id,
            title=title,
            content=content,
            entities=entities,
        )
    )


if __name__ == "__main__":
    import sys

    doc_arg = sys.argv[1] if len(sys.argv) > 1 else "doc-b2c4efe42bcc09ab18ea1f6c3337da7b"
    print(f"Exporting document {doc_arg} to Obsidian Vault...")
    res = export_document_by_id(doc_arg)
    print("Export completed:")
    print("Vault File:", res.get("vault_path"))
    print("Backup File:", res.get("local_path"))
