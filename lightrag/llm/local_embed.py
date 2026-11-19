"""
Local Offline Embedding Provider for LightRAG using FastEmbed (ONNX Runtime).
Runs 100% locally on CPU without external API calls or quota limits.
"""

from __future__ import annotations

import os
import asyncio
from typing import Any
import numpy as np
from fastembed import TextEmbedding
from lightrag.utils import logger, wrap_embedding_func_with_attrs

_CACHED_MODELS: dict[str, TextEmbedding] = {}


def _get_local_model(model_name: str = "BAAI/bge-small-en-v1.5") -> TextEmbedding:
    """Get or lazily load the local ONNX embedding model."""
    if model_name not in _CACHED_MODELS:
        logger.info(f"Loading local offline embedding model: {model_name}")
        _CACHED_MODELS[model_name] = TextEmbedding(model_name=model_name)
    return _CACHED_MODELS[model_name]


@wrap_embedding_func_with_attrs(
    embedding_dim=384,
    max_token_size=512,
    model_name="BAAI/bge-small-en-v1.5",
    supports_asymmetric=False,
)
async def local_embed(
    texts: list[str],
    model: str = "BAAI/bge-small-en-v1.5",
    **kwargs: Any,
) -> np.ndarray:
    """
    Generate embeddings locally on CPU using FastEmbed.
    Runs asynchronously in a threadpool executor to avoid blocking the event loop.
    """
    embed_model = _get_local_model(model)
    loop = asyncio.get_running_loop()
    embeddings = await loop.run_in_executor(
        None,
        lambda: np.array(list(embed_model.embed(texts)), dtype=np.float32),
    )
    return embeddings


__all__ = ["local_embed"]
