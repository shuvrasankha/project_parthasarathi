from eval.run_eval import overlap, theme_match
from rag.themes import canonical, canonical_list


def test_synonyms_map_to_canonical():
    assert canonical("Jealousy") == "envy"
    assert canonical("sibling rivalry") == "rivalry"
    assert canonical("something new") == "something new"
    assert canonical_list(["jealousy", "envy", "rage"]) == ["envy", "anger"]


def test_eval_theme_match_uses_vocabulary():
    assert theme_match("envy", "jealousy")
    assert theme_match("fear", "fear of failure")  # substring still counts
    assert not theme_match("grief", "anger")
    assert overlap(["envy", "family"], ["jealousy"]) == 0.5
