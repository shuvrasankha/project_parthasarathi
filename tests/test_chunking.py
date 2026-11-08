from rag.chunking import chunk_section, split_sentences

words = lambda s: len(s.split())  # noqa: E731  # word count stands in for tokens


def test_short_section_is_one_chunk():
    assert chunk_section("One para.\n\nTwo para.", words, max_single=10) == ["One para.\n\nTwo para."]


def test_long_section_splits_on_paragraphs_with_sentence_overlap():
    paras = [f"Para {i} first sentence here. Para {i} second sentence here." for i in range(6)]  # 8 words each
    chunks = chunk_section("\n\n".join(paras), words, max_single=20, target=20, overlap=5)
    assert len(chunks) > 1
    for prev, nxt in zip(chunks, chunks[1:]):
        last_sentence = split_sentences(prev)[-1]
        assert nxt.startswith(last_sentence)  # overlap is the previous chunk's last whole sentence
    # every original sentence survives intact somewhere
    joined = " ".join(chunks)
    assert all(s in joined for p in paras for s in split_sentences(p))


def test_oversized_paragraph_falls_back_to_sentences_never_mid_sentence():
    para = " ".join(f"Sentence number {i} is right here." for i in range(10))  # 6 words each
    chunks = chunk_section(para, words, max_single=20, target=20, overlap=6)
    for c in chunks:
        assert c.endswith(".") and c[0].isupper()
        assert words(c) <= 20 + 6


def test_split_sentences_keeps_quotes_and_abbreviations():
    s = split_sentences("Karna said, 'I am Radha's son.' Then he left. He wept, i.e. silently.")
    assert s == ["Karna said, 'I am Radha's son.'", "Then he left.", "He wept, i.e. silently."]
