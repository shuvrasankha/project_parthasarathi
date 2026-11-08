from rag.sources.ganguli import clean_text, parse_volume, roman_to_int

# Shaped like the real files: Gutenberg wrapper, CRLF, front matter, running heads, Roman and bare-number
# books, a combined heading, footnote markers, transcriber notes and a FOOTNOTES block.
EBOOK = "\r\n".join([
    "The Project Gutenberg eBook of The Mahabharata",
    "*** START OF THE PROJECT GUTENBERG EBOOK THE MAHABHARATA ***",
    "Produced by John B. Hare.",
    "BOOK 5",
    "UDYOGA PARVA",
    "Translated into English Prose from the Original Sanskrit Text",
    "THE MAHABHARATA",
    "UDYOGA PARVA",
    "SECTION CXLIV",
    "",
    "Vaisampayana said, 'Kunti went to the river.[1] She saw Karna there.'",
    "",
    "Karna said, 'I am Karna, the son of Radha.' [Some text is obviously",
    "missing here--JBH] He bowed.",
    "",
    " SECTION CXLV",
    "",
    "Kunti said, 'Thou art my son.' [possibly 'is'?--JBH]",
    "",
    "END OF UDYOGA PARVA",
    "",
    "FOOTNOTES",
    "",
    "1. The Ganga.",
    "SECTION IX",
    "BOOK 8",
    "Karna-parva",
    "Scanned and Proofed by Mantra Caitanya.",
    "",
    "1",
    "",
    "Om! Having bowed down unto Narayana.",
    "",
    "2",
    "",
    "Sanjaya said, 'Karna fought.'",
    "",
    "The End of Karna-parva",
    "BOOK 12",
    "SECTION XXXIV-XXXV",
    "",
    "Bhishma said, 'Hear.'",
    "*** END OF THE PROJECT GUTENBERG EBOOK THE MAHABHARATA ***",
    "license text that must be ignored",
])


def test_parse_volume_structure():
    secs = parse_volume(EBOOK)
    assert [(s.parva, s.section, s.sections_covered) for s in secs] == [
        ("udyoga", 144, [144]), ("udyoga", 145, [145]),
        ("karna", 1, [1]), ("karna", 2, [2]),
        ("santi", 34, [34, 35]),
    ]


def test_parse_volume_cleans_notes_and_boilerplate():
    secs = {(s.parva, s.section): s.text for s in parse_volume(EBOOK)}
    assert secs[("udyoga", 144)] == (
        "Vaisampayana said, 'Kunti went to the river. She saw Karna there.'\n\n"
        "Karna said, 'I am Karna, the son of Radha.' He bowed."
    )
    assert secs[("udyoga", 145)] == "Kunti said, 'Thou art my son.'"  # END line and FOOTNOTES dropped
    assert secs[("karna", 2)] == "Sanjaya said, 'Karna fought.'"
    assert "license" not in " ".join(secs.values())


def test_clean_text_removes_hare_gita_headings():
    raw = "[(Bhagavad Gita Chapter I)]\n\n([This is where the Gita starts.--John Bruno Hare])\n\nDhritarashtra said."
    assert clean_text(raw) == "Dhritarashtra said."


def test_roman_to_int():
    assert [roman_to_int(r) for r in ("I", "IV", "XLIV", "CXLIV", "CCCLXV")] == [1, 4, 44, 144, 365]
