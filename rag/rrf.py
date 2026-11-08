"""Reciprocal Rank Fusion: merge ranked id lists without comparing their raw scores."""
from __future__ import annotations


def rrf(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    """score(id) = sum over lists of 1 / (k + rank), rank starting at 1. Ties keep first-seen order."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, id_ in enumerate(ranking, start=1):
            scores[id_] = scores.get(id_, 0.0) + 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda kv: -kv[1])
