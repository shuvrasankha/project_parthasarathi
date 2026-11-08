from rag.llm import parse_json
from rag.situations import candidate_sections, quote_in, validate

TEXT = "Vaisampayana said, 'Then Pritha, approaching Karna, spoke unto him these words, O king.'"


def test_quote_in_ignores_case_and_punctuation():
    assert quote_in("then pritha approaching karna spoke unto him", TEXT)
    assert not quote_in("then pritha approaching arjuna spoke unto him", TEXT)  # changed word
    assert not quote_in("Pritha approaching", TEXT)  # too short to count as evidence
    assert not quote_in("then pritha approaching karna spoke unto hi", TEXT)  # partial word


def test_candidate_sections_ranks_by_distinct_terms_and_keeps_guesses():
    secs = {("udyoga", 1): "Karna", ("udyoga", 2): "Karna Pritha Pritha", ("udyoga", 3): "nothing",
            ("vana", 4): "Karna Pritha", ("udyoga", 9): "unrelated"}
    assert candidate_sections(secs, "udyoga", ["Karna", "Pritha"], guessed=[9, 77]) == [2, 1, 9]


def test_validate_rejects_bad_entries():
    good = {"id": "a", "title": "t", "parva": "Udyoga", "dilemma": "d", "themes": ["x"],
            "sections": [2], "related_verses": ["2.47"], "reviewed": False}
    keys = {("udyoga", 2)}
    assert validate([good], {"2.47"}, keys) == []
    bad = {**good, "related_verses": ["19.1"], "sections": [], "reviewed": "no"}
    errs = validate([good, {**good}, bad], {"2.47"}, keys)
    assert any("duplicate id" in e for e in errs)
    assert any("unknown verse 19.1" in e for e in errs)
    assert any("needs_check" in e for e in errs)
    assert any("reviewed" in e for e in errs)


def test_parse_json_strips_think_and_fences():
    assert parse_json('<think>{"no": 1}</think>\n```json\n{"a": [1, 2]}\n```') == {"a": [1, 2]}


def test_free_models_guard():
    import pytest

    from rag.llm import free_models

    assert free_models(" a/b:free, c/d:free ") == ["a/b:free", "c/d:free"]
    with pytest.raises(ValueError):
        free_models("a/b:free,c/d")  # a paid model slipped in


def test_duplicate_of_matches_same_parva_overlapping_sections():
    from rag.situations import duplicate_of

    old = [{"id": "a", "parva": "Udyoga", "sections": [144, 145]}, {"id": "b", "parva": "Adi", "sections": [1]}]
    assert duplicate_of({"parva": "Udyoga", "sections": [145, 146]}, old) == "a"
    assert duplicate_of({"parva": "Sabha", "sections": [144]}, old) is None
    assert duplicate_of({"parva": "Udyoga", "sections": []}, old) is None
