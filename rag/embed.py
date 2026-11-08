"""Embedding behind a tiny interface so a hosted API can replace BGE-M3 via EMBED_PROVIDER."""
from __future__ import annotations

from functools import lru_cache
from typing import Protocol

from rag.config import settings


class Embedder(Protocol):
    dim: int

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one L2-normalised vector per text."""
        ...


class BGEM3Embedder:
    """BAAI/bge-m3 dense vectors via sentence-transformers. fp16 on MPS to fit 8 GB RAM."""

    dim = 1024

    def __init__(self, model_name: str, device: str, batch_size: int) -> None:
        import torch
        from sentence_transformers import SentenceTransformer

        if device == "mps" and not torch.backends.mps.is_available():
            device = "cpu"
        self.model = SentenceTransformer(model_name, device=device)
        if device != "cpu":
            self.model.half()
        self.batch_size = batch_size

    def embed(self, texts: list[str]) -> list[list[float]]:
        vecs = self.model.encode(
            texts, batch_size=self.batch_size, normalize_embeddings=True, show_progress_bar=len(texts) > 50
        )
        return [v.astype("float32").tolist() for v in vecs]


@lru_cache(maxsize=1)
def get_embedder() -> Embedder:
    """Build the embedder named by EMBED_PROVIDER (loaded once per process)."""
    if settings.embed_provider == "bge-m3":
        return BGEM3Embedder(settings.embed_model, settings.embed_device, settings.embed_batch_size)
    # Add hosted providers here (openai/cohere/voyage); they must return 1024-dim vectors or the column must change.
    raise ValueError(f"Unknown EMBED_PROVIDER: {settings.embed_provider!r}")
