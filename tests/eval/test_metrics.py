"""Tests for the Tier 1 eval metrics."""

from __future__ import annotations

import pytest

from verifiable_rag.eval import EvalRecord
from verifiable_rag.eval.metrics import (
    abstention_metrics,
    aggregate_citation_metrics,
    citation_set_metrics,
    coverage,
    localization_accuracy,
    score_records,
)


# --------------------------------------------------------------------------- #
# citation_set_metrics
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_perfect_citation() -> None:
    m = citation_set_metrics(frozenset({"a", "b"}), frozenset({"a", "b"}))
    assert m.precision == 1.0
    assert m.recall == 1.0
    assert m.f1 == 1.0


@pytest.mark.smoke
def test_partial_overlap() -> None:
    m = citation_set_metrics(frozenset({"a", "b", "c"}), frozenset({"a", "b", "d"}))
    # tp=2, predicted=3 → precision=2/3
    # tp=2, gold=3      → recall=2/3
    assert m.precision == pytest.approx(2 / 3)
    assert m.recall == pytest.approx(2 / 3)
    assert m.f1 == pytest.approx(2 / 3)


@pytest.mark.smoke
def test_no_overlap() -> None:
    m = citation_set_metrics(frozenset({"a"}), frozenset({"b"}))
    assert m.precision == 0.0
    assert m.recall == 0.0
    assert m.f1 == 0.0


@pytest.mark.smoke
def test_empty_predictions_with_gold() -> None:
    """Vacuous precision (no false positives), zero recall."""
    m = citation_set_metrics(frozenset(), frozenset({"a"}))
    assert m.precision == 1.0
    assert m.recall == 0.0
    assert m.f1 == 0.0


@pytest.mark.smoke
def test_empty_both() -> None:
    """Both empty — vacuously perfect."""
    m = citation_set_metrics(frozenset(), frozenset())
    assert m.precision == 1.0
    assert m.recall == 1.0
    assert m.f1 == 1.0


# --------------------------------------------------------------------------- #
# aggregate_citation_metrics
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_aggregate_macro_averages() -> None:
    pairs = [
        (frozenset({"a"}), frozenset({"a"})),  # perfect
        (frozenset({"x"}), frozenset({"y"})),  # zero
    ]
    m = aggregate_citation_metrics(pairs)
    assert m.precision == 0.5
    assert m.recall == 0.5


@pytest.mark.smoke
def test_aggregate_skips_doubly_empty_pairs() -> None:
    """Refused-and-should-refuse cases shouldn't pollute the average."""
    pairs = [
        (frozenset({"a"}), frozenset({"a"})),
        (frozenset(), frozenset()),  # skipped
    ]
    m = aggregate_citation_metrics(pairs)
    assert m.precision == 1.0
    assert m.recall == 1.0


@pytest.mark.smoke
def test_aggregate_all_doubly_empty_returns_perfect() -> None:
    """If everything is refused-and-should-refuse, the metric is vacuous."""
    pairs = [(frozenset(), frozenset()), (frozenset(), frozenset())]
    m = aggregate_citation_metrics(pairs)
    assert m.precision == 1.0
    assert m.recall == 1.0


# --------------------------------------------------------------------------- #
# abstention_metrics
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_abstention_perfect() -> None:
    m = abstention_metrics(refused=[True, True, False, False], should_refuse=[True, True, False, False])
    assert m.precision == 1.0
    assert m.recall == 1.0
    assert m.f1 == 1.0


@pytest.mark.smoke
def test_abstention_over_refusal() -> None:
    """Refusing answerable questions hurts precision."""
    # Refused: T T T F   Should refuse: T F F F
    # tp=1, fp=2, fn=0 → precision=1/3, recall=1/1
    m = abstention_metrics(refused=[True, True, True, False], should_refuse=[True, False, False, False])
    assert m.precision == pytest.approx(1 / 3)
    assert m.recall == 1.0


@pytest.mark.smoke
def test_abstention_under_refusal() -> None:
    """Failing to refuse unsupportable questions hurts recall."""
    # Refused: F F F F   Should refuse: T T F F
    # tp=0, fp=0, fn=2 → precision=1.0 (vacuous), recall=0
    m = abstention_metrics(refused=[False, False, False, False], should_refuse=[True, True, False, False])
    assert m.precision == 1.0
    assert m.recall == 0.0


@pytest.mark.smoke
def test_abstention_length_mismatch_raises() -> None:
    with pytest.raises(ValueError, match="length mismatch"):
        abstention_metrics(refused=[True], should_refuse=[True, False])


# --------------------------------------------------------------------------- #
# localization_accuracy + coverage
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_localization_accuracy_exact_match() -> None:
    pairs = [
        (frozenset({"a"}), frozenset({"a"})),
        (frozenset({"a", "b"}), frozenset({"a", "b"})),
    ]
    assert localization_accuracy(pairs) == 1.0


@pytest.mark.smoke
def test_localization_accuracy_partial() -> None:
    pairs = [
        (frozenset({"a"}), frozenset({"a"})),  # exact
        (frozenset({"a", "b"}), frozenset({"a"})),  # not exact (extra)
    ]
    assert localization_accuracy(pairs) == 0.5


@pytest.mark.smoke
def test_coverage_any_intersection_counts() -> None:
    pairs = [
        (frozenset({"a", "x"}), frozenset({"a"})),  # hit (intersects)
        (frozenset({"y"}), frozenset({"b"})),  # miss
        (frozenset({"c"}), frozenset({"c"})),  # hit
    ]
    assert coverage(pairs) == pytest.approx(2 / 3)


@pytest.mark.smoke
def test_coverage_excludes_doubly_empty() -> None:
    pairs = [
        (frozenset({"a"}), frozenset({"a"})),  # hit
        (frozenset(), frozenset()),  # excluded
    ]
    assert coverage(pairs) == 1.0


# --------------------------------------------------------------------------- #
# score_records — end-to-end smoke
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_score_records_shape() -> None:
    records = [
        EvalRecord(
            question_id="q1",
            was_refused=False,
            cited_sentence_ids=frozenset({"a"}),
            answer_text="...",
            faithfulness_score=0.8,
        ),
        EvalRecord(
            question_id="q2",
            was_refused=True,
            cited_sentence_ids=frozenset(),
            answer_text="",
            faithfulness_score=0.0,
        ),
    ]
    gold = {
        "q1": (frozenset({"a"}), False),
        "q2": (frozenset(), True),
    }
    out = score_records(records, gold)
    assert out["n_questions"] == 2
    assert out["n_errors"] == 0
    assert out["citation_f1"] == 1.0
    assert out["abstention_f1"] == 1.0


@pytest.mark.smoke
def test_score_records_skips_errors() -> None:
    records = [
        EvalRecord(
            question_id="q1",
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="",
            faithfulness_score=0.0,
            error="boom",
        ),
    ]
    out = score_records(records, {"q1": (frozenset({"a"}), False)})
    assert out["n_errors"] == 1
