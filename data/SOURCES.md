# Data sources

Raw downloads live in `data/raw/` (gitignored). Cleaned outputs live in `data/clean/`.

## Bhagavad Gita: Sanskrit
- **URL:** https://raw.githubusercontent.com/gita/gita/main/data/verse.json
- **Retrieved:** 2026-11-07
- **License:** the repository is under the Unlicense. The Sanskrit text itself is ancient and in the public domain.
- **Used:** only the Devanagari `text` field (701 verses; chapter 13 has 35, counting 13.1 "Arjuna said: prakṛtiṁ puruṣaṁ…").
- **Not used:** `transliteration` and `word_meanings`. Their romanisation scheme and glosses match a modern copyrighted site, so we don't ingest them. `translation.json` and `commentary.json` are never downloaded.
- **Transliteration:** IAST, generated locally from the Devanagari with `indic-transliteration`.

## Bhagavad Gita: English (Annie Besant, 4th ed., 1922)
- **URL:** https://en.wikisource.org/wiki/Bhagavad-Gita_(Besant_4th), fetched per discourse through the MediaWiki API (`action=parse&prop=text`, pages `Bhagavad-Gita (Besant 4th)/Discourse 1..18`)
- **Retrieved:** 2026-11-07
- **License:** Wikisource tags it `{{translation-license|original={{PD-old}}|translation={{PD/US|1933}}}}`. Besant died in 1933, so the translation is public domain in the US and in life+60 and life+70 countries.
- **Why Besant over Telang:** "The Bhagavad Gita (Telang translation)" redirects to *The Glories of the Bhagavad Gita*, the Padma Purana's Gita Mahatmya, which is a different text. The real Telang Gita (Sacred Books of the East, Vol. 8, 1882) is marked incomplete on Wikisource, has no verse numbers, and has footnotes mixed into the prose. Besant prints each verse's Sanskrit (ending `॥ N ॥`) followed by its English, so all 701 verses align with verse.json.
- **Not used:** Besant's footnotes and chapter colophons.

## Mahabharata: English (Kisari Mohan Ganguli, 1883–1896)
- **URLs:** Project Gutenberg ebooks 15474, 15475, 15476, 15477 (Plain Text UTF-8), fetched from `https://www.gutenberg.org/cache/epub/<n>/pg<n>.txt`
  - 15474: Books 1–3 · 15475: Books 4–7 · 15476: Books 8–12 · 15477: Books 13–18
- **Retrieved:** 2026-11-07
- **License:** public domain in the US (translation published 1883–1896; Ganguli died 1908). Gutenberg's own header, footer and license text are stripped and not stored.
- **Used:** the text of every section in all 18 parvas (2,107 sections), chunked for embedding.
- **Not used:**
  - each book's title and credits front matter
  - the per-book `FOOTNOTES` blocks and their `[n]` markers
  - "End of … parva" lines
  - the sacred-texts.com transcriber's (J. B. Hare's) additions: `[...--JBH]` notes, his added "Bhagavad Gita Chapter N" headings in Bhishma 25–42, `[End of the Bhagavad Gita]` and `[sic]`
- **Source numbering gaps:** Adi 177, Sabha 67, Drona 54–55, Drona 189 and Santi 364 have no heading in the files. For Santi the transcriber notes the section is absent from the source edition. Text stays under the preceding section; nothing is filled in.
- **Tagging:** Bhishma sections 25–42 are Ganguli's translation of the Bhagavad Gita and carry `contains_gita: true`.
