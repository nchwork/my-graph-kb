"""
Updates Obsidian Canvas (.canvas), Bookmarks, Graph View config, and Workspace
to organize Docker in Action cleanly by Parts 1-3 and Chapters 01-13.
"""

from __future__ import annotations

import json
from pathlib import Path

from build_chapter_summaries import CHAPTERS, ROADMAP_STEM, SUMMARY_STEM, CANVAS_FILE

VAULT_DIR = Path(r"C:\Users\hiepnc1\Documents\Obsidian Vault")
BOOK_FOLDER = "Docker-in-Action-2ed"
SUMMARIES_DIR = VAULT_DIR / BOOK_FOLDER
BACKUP_DIR = Path(r"D:\hiepnc\obsidian_brain") / BOOK_FOLDER
OBSIDIAN_CONF = VAULT_DIR / ".obsidian"


def build_bookmarks() -> None:
    items = [
        {
            "type": "file",
            "path": f"{BOOK_FOLDER}/{ROADMAP_STEM}.md",
            "title": "📚 Mục lục & Lộ trình Đọc (13 Chương)",
        },
        {
            "type": "file",
            "path": f"{BOOK_FOLDER}/{CANVAS_FILE}",
            "title": "🗺️ Bản đồ 3 Phần (Canvas)",
        },
        {
            "type": "file",
            "path": f"{BOOK_FOLDER}/{SUMMARY_STEM}.md",
            "title": "📖 Tóm tắt Toàn Sách (Docker in Action)",
        },
    ]
    for ch in CHAPTERS:
        items.append(
            {
                "type": "file",
                "path": f"{BOOK_FOLDER}/{ch['stem']}.md",
                "title": ch["stem"],
            }
        )

    with open(OBSIDIAN_CONF / "bookmarks.json", "w", encoding="utf-8") as f:
        json.dump({"items": items}, f, indent=2, ensure_ascii=False)
    print("✓ Updated bookmarks.json with Roadmap, Canvas, Summary, and 13 Chapters")


def build_canvas() -> None:
    canvas_nodes = [
        {
            "id": "header_title",
            "x": -100,
            "y": -380,
            "width": 1460,
            "height": 180,
            "type": "text",
            "text": (
                "# 📚 DOCKER IN ACTION (2ND EDITION) — LỘ TRÌNH 3 PHẦN, 13 CHƯƠNG\n\n"
                "> [!tip] **Hướng dẫn sử dụng:**\n"
                "> Đọc theo thứ tự từ **Phần 1 (Trái)** ➔ **Phần 2 (Giữa)** ➔ **Phần 3 (Phải)**, từ Chương 01 đến Chương 13.\n"
                "> Mỗi thẻ là bản tóm tắt song ngữ đầy đủ từng mục trong chương!"
            ),
            "color": "5",
        }
    ]

    parts = [
        {
            "part": 1,
            "title": "Phần 1: Cô lập Tiến trình & Điện toán Độc lập Môi trường (Ch. 01 – 06)",
            "color": "4",
        },
        {
            "part": 2,
            "title": "Phần 2: Đóng gói Phần mềm để Phân phối (Ch. 07 – 10)",
            "color": "2",
        },
        {
            "part": 3,
            "title": "Phần 3: Trừu tượng hóa Cấp cao & Điều phối (Ch. 11 – 13)",
            "color": "6",
        },
    ]

    canvas_edges = []
    start_x = -200
    card_w = 380
    card_h = 165
    gap_y = 35
    group_pad = 40
    col_step = card_w + (group_pad * 2) + 120

    prev_chapter_node_id = None
    prev_chapter_part = None

    for p_idx, p_info in enumerate(parts):
        part_chapters = [c for c in CHAPTERS if c["part"] == p_info["part"]]
        gx = start_x + p_idx * col_step
        gy = -120
        g_height = len(part_chapters) * (card_h + gap_y) + 90
        group_id = f"part_{p_info['part']}"

        canvas_nodes.append(
            {
                "id": group_id,
                "x": gx,
                "y": gy,
                "width": card_w + (group_pad * 2),
                "height": g_height,
                "type": "group",
                "label": p_info["title"],
                "color": p_info["color"],
            }
        )

        for c_idx, ch in enumerate(part_chapters):
            node_id = f"ch_{ch['num']:02d}"
            ny = gy + 70 + c_idx * (card_h + gap_y)
            canvas_nodes.append(
                {
                    "id": node_id,
                    "x": gx + group_pad,
                    "y": ny,
                    "width": card_w,
                    "height": card_h,
                    "type": "file",
                    "file": f"{BOOK_FOLDER}/{ch['stem']}.md",
                }
            )
            if prev_chapter_node_id is not None:
                same_part = prev_chapter_part == p_info["part"]
                canvas_edges.append(
                    {
                        "id": f"edge_{prev_chapter_node_id}_{node_id}",
                        "fromNode": prev_chapter_node_id,
                        "fromSide": "bottom" if same_part else "right",
                        "toNode": node_id,
                        "toSide": "top" if same_part else "left",
                    }
                )
            prev_chapter_node_id = node_id
            prev_chapter_part = p_info["part"]

        if p_idx > 0:
            canvas_edges.append(
                {
                    "id": f"edge_part_{p_idx}_{p_idx + 1}",
                    "fromNode": f"part_{p_idx}",
                    "fromSide": "right",
                    "toNode": f"part_{p_idx + 1}",
                    "toSide": "left",
                    "label": f"Sang Phần {p_idx + 1}",
                }
            )

    canvas_data = {"nodes": canvas_nodes, "edges": canvas_edges}
    for folder in (SUMMARIES_DIR, BACKUP_DIR):
        folder.mkdir(parents=True, exist_ok=True)
        out_path = folder / CANVAS_FILE
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(canvas_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Created Canvas: {out_path}")


def build_graph_config() -> None:
    graph_cfg = {
        "collapse-filter": False,
        "search": "",
        "showTags": False,
        "showAttachments": False,
        "hideUnresolved": True,
        "showOrphans": True,
        "collapse-color-groups": False,
        "colorGroups": [
            {"query": "tag:#roadmap", "color": {"a": 1, "rgb": 2201331}},   # Blue
            {"query": "tag:#part-1", "color": {"a": 1, "rgb": 1096065}},    # Green
            {"query": "tag:#part-2", "color": {"a": 1, "rgb": 16096779}},   # Amber/Orange
            {"query": "tag:#part-3", "color": {"a": 1, "rgb": 10835197}},   # Purple
            {"query": "tag:#summary", "color": {"a": 1, "rgb": 15485081}},  # Magenta
        ],
        "collapse-display": True,
        "showArrow": True,
        "textFadeMultiplier": 0,
        "nodeSizeMultiplier": 1.15,
        "lineSizeMultiplier": 1,
        "collapse-forces": True,
        "centerStrength": 0.518713248970312,
        "repelStrength": 10,
        "linkStrength": 1,
        "linkDistance": 250,
        "scale": 0.7132754626224403,
        "close": False,
    }
    with open(OBSIDIAN_CONF / "graph.json", "w", encoding="utf-8") as f:
        json.dump(graph_cfg, f, indent=2, ensure_ascii=False)
    print("✓ Updated graph.json with Part 1-3 color groups")


def update_workspace() -> None:
    workspace_file = OBSIDIAN_CONF / "workspace.json"
    if not workspace_file.exists():
        return
    with open(workspace_file, "r", encoding="utf-8") as f:
        ws = json.load(f)

    roadmap_rel = f"{BOOK_FOLDER}/{ROADMAP_STEM}.md"
    canvas_rel = f"{BOOK_FOLDER}/{CANVAS_FILE}"

    ws["main"] = {
        "id": "a9ea851e34b3091c",
        "type": "split",
        "children": [
            {
                "id": "973c78e0f96d821c",
                "type": "tabs",
                "currentTab": 0,
                "children": [
                    {
                        "id": "graph_view_leaf",
                        "type": "leaf",
                        "state": {
                            "type": "graph",
                            "state": {},
                            "icon": "lucide-git-fork",
                            "title": "Graph view",
                        },
                    },
                    {
                        "id": "roadmap_view_leaf",
                        "type": "leaf",
                        "state": {
                            "type": "markdown",
                            "state": {
                                "file": roadmap_rel,
                                "mode": "preview",
                                "source": False,
                            },
                            "icon": "lucide-file",
                            "title": ROADMAP_STEM,
                        },
                    },
                    {
                        "id": "canvas_view_leaf",
                        "type": "leaf",
                        "state": {
                            "type": "canvas",
                            "state": {
                                "file": canvas_rel,
                            },
                            "icon": "lucide-layout-dashboard",
                            "title": "Docker Learning Path",
                        },
                    },
                ],
            }
        ],
        "direction": "vertical",
    }
    ws["active"] = "graph_view_leaf"

    ws["lastOpenFiles"] = [
        roadmap_rel,
        canvas_rel,
        f"{BOOK_FOLDER}/{CHAPTERS[0]['stem']}.md",
        f"{BOOK_FOLDER}/{SUMMARY_STEM}.md",
    ]

    with open(workspace_file, "w", encoding="utf-8") as f:
        json.dump(ws, f, indent=2, ensure_ascii=False)
    print("✓ Updated workspace.json with Graph view (active), Roadmap, and Canvas tabs")


def main() -> None:
    build_bookmarks()
    build_canvas()
    build_graph_config()
    update_workspace()


if __name__ == "__main__":
    main()
