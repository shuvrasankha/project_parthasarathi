"""Section -> chunks. Paragraph boundaries first, sentences only when a paragraph is too big. Never mid-sentence."""
from __future__ import annotations

import re
from collections.abc import Callable
from functools import lru_cache

TokenCounter = Callable[[str], int]

# A sentence ends at . ! ? (plus closing quotes/brackets) when the next one starts with a capital or an opening quote.
_SENTENCE = re.compile(r".+?(?:[.!?]+['\"’”)\]]*(?=\s+['\"‘“(\[]?[A-Z])|$)", re.S)


def split_sentences(paragraph: str) -> list[str]:
    return [s.strip() for s in _SENTENCE.findall(paragraph) if s.strip()]


@lru_cache(maxsize=1)
def bge_token_counter() -> TokenCounter:
    """Token count with the embedding model's own tokenizer (no special tokens)."""
    from transformers import AutoTokenizer

    from rag.config import settings

    tok = AutoTokenizer.from_pretrained(settings.embed_model)
    return lambda text: len(tok.encode(text, add_special_tokens=False))


def chunk_section(
    text: str,
    count: TokenCounter,
    max_single: int = 600,
    target: int = 500,
    overlap: int = 80,
) -> list[str]:
    """Return [text] if it fits in max_single tokens, else ~target-token chunks with ~overlap tokens carried over.

    Paragraphs are separated by blank lines and kept intact when they fit. The overlap is the trailing whole
    sentences of the previous chunk (up to `overlap` tokens). A single sentence longer than `target` becomes
    its own oversized chunk rather than being cut.
    """
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if count("\n\n".join(paragraphs)) <= max_single:
        return ["\n\n".join(paragraphs)] if paragraphs else []

    # Units: (text, tokens, starts_new_paragraph). Oversized paragraphs become sentence units.
    units: list[tuple[str, int, bool]] = []
    for p in paragraphs:
        n = count(p)
        if n <= target:
            units.append((p, n, True))
        else:
            units.extend((s, count(s), i == 0) for i, s in enumerate(split_sentences(p)))

    chunks: list[list[tuple[str, int, bool]]] = []
    cur: list[tuple[str, int, bool]] = []
    cur_tokens = 0
    fresh = 0  # units in `cur` that are not overlap carried from the previous chunk
    for u in units:
        if cur and fresh and cur_tokens + u[1] > target:
            chunks.append(cur)
            cur = _overlap_tail(cur, count, overlap)
            cur_tokens = sum(x[1] for x in cur)
            fresh = 0
        cur.append(u)
        cur_tokens += u[1]
        fresh += 1
    if fresh:
        chunks.append(cur)
    return [_join(c) for c in chunks]


def _overlap_tail(units: list[tuple[str, int, bool]], count: TokenCounter, budget: int) -> list[tuple[str, int, bool]]:
    """Trailing whole sentences of `units` totalling at most `budget` tokens."""
    sentences = [s for text, _, _ in units for s in split_sentences(text)]
    tail: list[str] = []
    used = 0
    for s in reversed(sentences):
        n = count(s)
        if used + n > budget:
            break
        tail.insert(0, s)
        used += n
    return [(" ".join(tail), used, True)] if tail else []


def _join(units: list[tuple[str, int, bool]]) -> str:
    out = ""
    for text, _, new_para in units:
        out += (("\n\n" if new_para else " ") if out else "") + text
    return out
