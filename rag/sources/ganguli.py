"""Mahabharata, K. M. Ganguli translation (1883-1896), Project Gutenberg ebooks 15474-15477.

Structure seen in the files: `BOOK N` starts each parva. Books 1-7 and 12-15 head sections with
`SECTION <roman>`; books 8-11 and 16-18 use a bare Arabic number on its own line. Each Roman book ends
with a `FOOTNOTES` block. Editor notes look like `[... --JBH]`.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from rag.chunking import TokenCounter, chunk_section
from rag.sources.fetch import fetch

log = logging.getLogger(__name__)

EBOOKS = (15474, 15475, 15476, 15477)
URL = "https://www.gutenberg.org/cache/epub/{n}/pg{n}.txt"
PARVAS = (
    "adi", "sabha", "vana", "virata", "udyoga", "bhishma", "drona", "karna", "shalya",
    "sauptika", "stri", "santi", "anusasana", "aswamedha", "asramavasika", "mausala",
    "mahaprasthanika", "svargarohanika",
)
BARE_NUMBER_BOOKS = {8, 9, 10, 11, 16, 17, 18}
GITA_SECTIONS = ("bhishma", range(25, 43))  # Ganguli's Bhagavad Gita: Bhishma Parva sections 25-42

_HARE = r"-+\s*(?:JBH|John Bruno Hare)"
_BOOK = re.compile(r"^BOOK (\d+)$")
_ROMAN = re.compile(r"^SECTION ([IVXLCDM]+)(?:-([IVXLCDM]+))?$")
_BARE = re.compile(r"^(\d+)$")
_END_LINE = re.compile(r"^(?:The End of .*parva|END OF [A-Z ]+PARVA|The Eighteen parvas of the Mahabharata are thus complete\.?)$", re.I)


def roman_to_int(s: str) -> int:
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for a, b in zip(s, s[1:] + " "):
        total += -vals[a] if b != " " and vals[a] < vals[b] else vals[a]
    return total


@dataclass
class Section:
    parva: str
    parva_number: int
    section: int
    sections_covered: list[int]
    text: str

    @property
    def contains_gita(self) -> bool:
        return self.parva == GITA_SECTIONS[0] and self.section in GITA_SECTIONS[1]


def download(raw_dir: Path) -> list[Path]:
    return [
        fetch(URL.format(n=n), raw_dir / "gutenberg" / f"pg{n}.txt", valid=lambda b: b"*** START OF" in b[:20000], delay=3)
        for n in EBOOKS
    ]


def strip_gutenberg(text: str) -> list[str]:
    """Lines strictly between the `*** START OF` and `*** END OF` markers."""
    lines = text.splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("*** START OF"))
    end = next(i for i, ln in enumerate(lines) if ln.startswith("*** END OF"))
    return lines[start + 1 : end]


def clean_text(raw: str) -> str:
    """Remove footnote markers and transcriber notes; one paragraph per blank-line block."""
    # Transcriber (J. B. Hare, sacred-texts.com) additions, not Ganguli: notes, Gita chapter headings, [sic].
    t = re.sub(rf"\(?\[[^\[\]]*?{_HARE}[^\[\]]*?\]\)?", "", raw, flags=re.S)
    t = re.sub(rf"\([^()]*?{_HARE}[^()]*?\)", "", t, flags=re.S)
    t = re.sub(r"\[\(Bhagavad Gita,? Chapter [IVXL]+\)\]|\[End of the Bhagavad Gita\]|\s?\[sic\]", "", t)
    t = re.sub(r"\[\d+\]", "", t)
    paragraphs = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", t)]
    return "\n\n".join(p for p in paragraphs if p)


def parse_volume(text: str) -> list[Section]:
    """Split one ebook into sections. Front matter, FOOTNOTES blocks and end-of-parva lines are dropped."""
    sections: list[Section] = []
    book: int | None = None
    current: tuple[int, list[int]] | None = None
    buf: list[str] = []
    in_notes = False

    def flush() -> None:
        if book is not None and current is not None:
            sections.append(Section(PARVAS[book - 1], book, current[0], current[1], clean_text("\n".join(buf))))

    for line in strip_gutenberg(text):
        s = line.strip()
        if m := _BOOK.match(s):
            flush()
            book, current, buf, in_notes = int(m.group(1)), None, [], False
            continue
        if book is None or in_notes:
            continue
        if s == "FOOTNOTES":
            flush()
            current, buf, in_notes = None, [], True  # everything until the next BOOK is notes
            continue
        if m := _ROMAN.match(s):
            if book not in BARE_NUMBER_BOOKS:
                flush()
                a = roman_to_int(m.group(1))
                b = roman_to_int(m.group(2)) if m.group(2) else a
                current, buf = (a, list(range(a, b + 1))), []
                continue
        elif (m := _BARE.match(s)) and book in BARE_NUMBER_BOOKS:
            flush()
            n = int(m.group(1))
            current, buf = (n, [n]), []
            continue
        if current is not None and not _END_LINE.match(s):
            buf.append(line)
    flush()
    return sections


@dataclass
class MBReport:
    sections: list[Section]
    chunks: list[dict]
    gaps: dict[str, list[int]] = field(default_factory=dict)
    duplicates: dict[str, list[int]] = field(default_factory=dict)
    short: list[str] = field(default_factory=list)
    leftovers: list[str] = field(default_factory=list)
    oversized_chunks: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        present = {s.parva for s in self.sections}
        return present == set(PARVAS) and not self.duplicates and not self.leftovers and not any(
            not s.text for s in self.sections
        )

    def render(self) -> str:
        per = {p: sum(s.parva == p for s in self.sections) for p in PARVAS}
        out = ["Mahabharata (Ganguli) validation report", f"  parvas present: {sum(v > 0 for v in per.values())}/18"]
        out += [f"    {i:>2}. {p:<16} sections={per[p]:>4}  gaps={self.gaps.get(p) or '-'}" for i, p in enumerate(PARVAS, 1)]
        out += [
            f"  total sections: {len(self.sections)}   total chunks: {len(self.chunks)}",
            f"  Gita-tagged chunks (bhishma 25-42): {sum(c['contains_gita'] for c in self.chunks)}",
            f"  duplicate section numbers: {self.duplicates or 'none'}",
            f"  empty or short sections (<80 words): {self.short or 'none'}",
            f"  leftover markup ([n], transcriber notes, FOOTNOTES, SECTION lines): {self.leftovers or 'none'}",
            f"  chunks over 700 tokens (one unsplittable sentence): {len(self.oversized_chunks)} {self.oversized_chunks[:10]}",
            "  numbering gaps are in the source; text is kept under the preceding section, nothing is filled in",
            f"  RESULT: {'OK' if self.ok else 'FAILED'}",
        ]
        return "\n".join(out)


def build(raw_dir: Path, count: TokenCounter) -> MBReport:
    sections = [s for n in EBOOKS for s in parse_volume((raw_dir / "gutenberg" / f"pg{n}.txt").read_text(encoding="utf-8"))]
    chunks: list[dict] = []
    oversized: list[str] = []
    for s in sections:
        for i, text in enumerate(chunk_section(s.text, count), start=1):
            cid = f"{s.parva}-{s.section}-{i}"
            chunks.append({
                "id": cid, "parva": s.parva, "parva_number": s.parva_number, "section": s.section,
                "sections_covered": s.sections_covered, "chunk_index": i, "contains_gita": s.contains_gita, "text": text,
            })
            if count(text) > 700:
                oversized.append(cid)

    report = MBReport(sections=sections, chunks=chunks, oversized_chunks=oversized)
    for p in PARVAS:
        nums = [n for s in sections if s.parva == p for n in s.sections_covered]
        if nums:
            report.gaps[p] = sorted(set(range(1, max(nums) + 1)) - set(nums))
            if dups := sorted({n for n in nums if nums.count(n) > 1}):
                report.duplicates[p] = dups
    report.gaps = {p: g for p, g in report.gaps.items() if g}
    report.short = [f"{s.parva}-{s.section} ({len(s.text.split())}w)" for s in sections if len(s.text.split()) < 80]
    bad = re.compile(r"\[\d+\]|JBH|Hare\b|sacred-texts|FOOTNOTES|Bhagavad Gita,? Chapter|\[sic\]|^SECTION [IVXLCDM]+$", re.M)
    report.leftovers = [f"{s.parva}-{s.section}" for s in sections if bad.search(s.text)]
    return report
