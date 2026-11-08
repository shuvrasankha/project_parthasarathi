import pytest

from rag.rrf import rrf


def test_rrf_scores_and_order():
    out = rrf([["a", "b", "c"], ["b", "d"]], k=60)
    assert [i for i, _ in out] == ["b", "a", "d", "c"]
    assert dict(out)["b"] == pytest.approx(1 / 62 + 1 / 61)
    assert dict(out)["a"] == pytest.approx(1 / 61)


def test_rrf_ties_keep_first_seen_order_and_empty_lists():
    assert [i for i, _ in rrf([["x"], ["y"]])] == ["x", "y"]
    assert rrf([[], []]) == []


def test_item_in_both_lists_beats_top_of_one():
    # 10th in both lists (2/70) outranks 1st in only one (1/61)
    a = [f"a{i}" for i in range(9)] + ["both"]
    b = [f"b{i}" for i in range(9)] + ["both"]
    assert rrf([a, b])[0][0] == "both"
