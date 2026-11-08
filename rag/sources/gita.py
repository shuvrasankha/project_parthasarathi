"""Bhagavad Gita: Sanskrit from gita/gita verse.json, English from Besant (1922) on Wikisource.

Only the Devanagari `text` field of verse.json is used. Transliteration is generated locally (IAST)
so no third-party romanisation or gloss is ingested. Besant verses are aligned on the Sanskrit
`॥ N ॥` markers, which are reliable; the English `(N)` markers have OCR errors.
"""
from __future__ import annotations

import html
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from indic_transliteration import sanscript

from rag.sources.fetch import fetch

VERSE_JSON_URL = "https://raw.githubusercontent.com/gita/gita/main/data/verse.json"
WIKISOURCE_API = "https://en.wikisource.org/w/api.php"
BESANT_PAGE = "Bhagavad-Gita (Besant 4th)/Discourse {n}"
TRANSLATOR = "Annie Besant (1922, 4th ed.)"

_DEV_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
_MARKER = re.compile(r"॥\s*([०-९]+)\s*॥\s*$")
_DEVANAGARI = re.compile(r"[ऀ-ॿ]")
_LATIN = re.compile(r"[A-Za-z]")


@dataclass
class GitaVerse:
    id: str
    chapter: int
    verse: int
    sanskrit: str
    transliteration: str
    translation: str
    translator: str = TRANSLATOR
    meaning_simple: str = ""
    themes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


# ---------- download ----------

def download(raw_dir: Path) -> None:
    """Fetch verse.json and the 18 Besant discourse pages (MediaWiki action=parse)."""
    fetch(VERSE_JSON_URL, raw_dir / "gita" / "verse.json", valid=lambda b: b.lstrip().startswith(b"["))
    for n in range(1, 19):
        fetch(
            WIKISOURCE_API,
            raw_dir / "wikisource" / f"besant_d{n}.parse.json",
            params={"action": "parse", "page": BESANT_PAGE.format(n=n), "prop": "text", "format": "json"},
            valid=lambda b: b.lstrip().startswith(b"{") and b'"parse"' in b[:200],
        )


# ---------- Sanskrit (verse.json) ----------

def clean_sanskrit(text: str) -> str:
    """Drop the trailing `।।2.47।।` number and blank lines; keep speaker lines like `सञ्जय उवाच`."""
    text = re.sub(r"[।|]{1,2}\s*\d+\.\d+\s*[।|]{0,2}", "॥", text)
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return "\n".join(lines)


def to_iast(devanagari: str) -> str:
    return sanscript.transliterate(devanagari, sanscript.DEVANAGARI, sanscript.IAST)


def load_sanskrit(verse_json: Path) -> dict[tuple[int, int], str]:
    """Return {(chapter, verse): cleaned Devanagari} using ONLY the `text` field."""
    data = json.loads(verse_json.read_text(encoding="utf-8"))
    return {(v["chapter_number"], v["verse_number"]): clean_sanskrit(v["text"]) for v in data}


# ---------- English (Besant HTML) ----------

def html_to_lines(page_html: str) -> list[str]:
    """Strip styles, footnote markers, the footnote list and tags; return non-empty text lines."""
    h = re.sub(r"<style.*?</style>", "", page_html, flags=re.S)
    h = re.sub(r'<sup[^>]*class="reference"[^>]*>.*?</sup>', "", h, flags=re.S)
    h = re.sub(r'<ol class="references">.*?</ol>', "", h, flags=re.S)
    h = re.sub(r"<br\s*/?>", "\n", h)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", h)).replace("​", "").replace("‌", "").replace("\xa0", " ")
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def _is_devanagari(line: str) -> bool:
    return len(_DEVANAGARI.findall(line)) > len(_LATIN.findall(line))


def clean_english(text: str) -> str:
    text = re.sub(r"\[\d+\]", "", text)  # any footnote markers left as plain text
    # English colophon follows the last verse when the Sanskrit colophon has no ॥N॥ marker.
    text = re.split(r"\bThus in the glorious Upanishads?\b", text)[0]
    text = re.sub(r"\(?\s*\d+(?:\s*[-–,]\s*\d+)*\s*\)?\s*$", "", text.strip())  # trailing (47), OCR-broken (23
    text = re.sub(r"\s+([,;:.!?])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_besant(page_html: str) -> dict[int, str]:
    """Map verse number -> English for one discourse.

    Lines are grouped into alternating Devanagari / English blocks. A Devanagari block ending in
    `॥ N ॥` is verse N; the English block that follows is its translation. The chapter colophon
    (the Devanagari block naming the `अध्यायः`) ends the chapter. Raises on duplicate verse numbers.
    """
    verses: dict[int, str] = {}
    current: int | None = None
    sk_block: list[str] = []
    for line in html_to_lines(page_html):
        if _is_devanagari(line):
            sk_block.append(line)
            m = _MARKER.search(line)
            if m:
                # Colophon "इति ... नाम ...ऽध्यायः ॥N॥". Not just "इति": verses 13.19, 15.20, 18.63 start with it too.
                if "ध्यायः" in " ".join(sk_block):
                    break
                current = int(m.group(1).translate(_DEV_DIGITS))
                if current in verses:
                    raise ValueError(f"duplicate verse marker {current}")
                verses[current] = ""
                sk_block = []
            continue
        sk_block = []
        if current is not None and not line.startswith("↑"):
            verses[current] = f"{verses[current]} {line}".strip()
    return {n: clean_english(t) for n, t in verses.items()}


def load_besant(raw_dir: Path) -> dict[tuple[int, int], str]:
    out: dict[tuple[int, int], str] = {}
    for n in range(1, 19):
        page = json.loads((raw_dir / "wikisource" / f"besant_d{n}.parse.json").read_text(encoding="utf-8"))
        for v, text in parse_besant(page["parse"]["text"]["*"]).items():
            out[(n, v)] = text
    return out


# ---------- merge + validate ----------

@dataclass
class GitaReport:
    records: list[GitaVerse]
    source_count: int
    only_sanskrit: list[str]
    only_english: list[str]
    empty_translation: list[str]
    suspicious_length: list[str]

    @property
    def ok(self) -> bool:
        chapters = {r.chapter for r in self.records}
        return (
            chapters == set(range(1, 19))
            and len(self.records) == self.source_count
            and not (self.only_sanskrit or self.only_english or self.empty_translation)
        )

    def render(self) -> str:
        per_ch = {c: sum(r.chapter == c for r in self.records) for c in range(1, 19)}
        lines = [
            "Gita validation report",
            f"  chapters present: {len(set(per_ch) & {r.chapter for r in self.records})}/18",
            f"  verses per chapter: {per_ch}",
            f"  merged verses: {len(self.records)}  (verse.json has {self.source_count})",
            f"  in Sanskrit only (no Besant English): {self.only_sanskrit or 'none'}",
            f"  in Besant only (no Sanskrit): {self.only_english or 'none'}",
            f"  empty translations: {self.empty_translation or 'none'}",
            f"  suspicious length (<25 or >1200 chars, check by eye): {self.suspicious_length or 'none'}",
            f"  RESULT: {'OK' if self.ok else 'FAILED'}",
        ]
        return "\n".join(lines)


def build(raw_dir: Path) -> GitaReport:
    sanskrit = load_sanskrit(raw_dir / "gita" / "verse.json")
    english = load_besant(raw_dir)
    keys = sorted(set(sanskrit) & set(english))
    records = [
        GitaVerse(
            id=f"{c}.{v}", chapter=c, verse=v,
            sanskrit=sanskrit[(c, v)], transliteration=to_iast(sanskrit[(c, v)]), translation=english[(c, v)],
        )
        for c, v in keys
    ]
    fmt = lambda ks: [f"{c}.{v}" for c, v in sorted(ks)]  # noqa: E731
    return GitaReport(
        records=records,
        source_count=len(sanskrit),
        only_sanskrit=fmt(set(sanskrit) - set(english)),
        only_english=fmt(set(english) - set(sanskrit)),
        empty_translation=[r.id for r in records if not r.translation],
        suspicious_length=[r.id for r in records if r.translation and not 25 <= len(r.translation) <= 1200],
    )


def embed_text(v: dict) -> str:
    """What gets embedded: translation + meaning_simple (when present)."""
    return "\n".join(x for x in (v["translation"], v.get("meaning_simple", "")) if x)
