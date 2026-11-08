"""Optional cross-encoder reranker (RERANK_ENABLED=true), BAAI/bge-reranker-v2-m3 by default."""
from __future__ import annotations

from functools import lru_cache

from rag.config import settings


@lru_cache(maxsize=1)
def _model():
    import torch
    from sentence_transformers import CrossEncoder

    device = settings.embed_device if settings.embed_device != "mps" or torch.backends.mps.is_available() else "cpu"
    return CrossEncoder(settings.rerank_model, device=device, max_length=1024)


def rerank_scores(query: str, texts: list[str]) -> list[float]:
    """Relevance of each text to the query; higher is better."""
    if not texts:
        return []
    return [float(s) for s in _model().predict([(query, t) for t in texts])]
