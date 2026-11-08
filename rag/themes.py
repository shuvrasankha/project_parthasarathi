"""Controlled theme vocabulary (data/themes.yaml): map free-text themes to canonical ones."""
from __future__ import annotations

from functools import lru_cache

import yaml

from rag.config import settings


@lru_cache(maxsize=1)
def vocabulary() -> dict[str, str]:
    """lowercase term -> canonical theme (each canonical theme maps to itself)."""
    data = yaml.safe_load((settings.data_dir / "themes.yaml").read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for canon, syns in data.items():
        for term in [canon, *syns]:
            out.setdefault(term.lower().strip(), canon)
    return out


def canonical(theme: str) -> str:
    """Canonical theme, or the cleaned input if it is not in the vocabulary."""
    t = theme.lower().strip()
    return vocabulary().get(t, t)


def canonical_list(themes: list[str]) -> list[str]:
    return list(dict.fromkeys(canonical(t) for t in themes))


def names() -> list[str]:
    return list(dict.fromkeys(vocabulary().values()))
