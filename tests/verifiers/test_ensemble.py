"""EnsembleScorer tests — uses tiny scripted NLIScorers, no real models."""

from __future__ import annotations

import pytest

from verifiable_rag.verifiers import EnsembleScorer, NLIScorer


class _ConstScorer:
    """Returns the same score for every pair. Implements NLIScorer."""

    def __init__(self, score: float) -> None:
        self._score = score

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        return [self._score] * len(pairs)


class _IndexedScorer:
    """Returns a fixed per-pair list. Implements NLIScorer."""

    def __init__(self, scores: list[float]) -> None:
        self._scores = scores

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        if len(pairs) != len(self._scores):
            raise AssertionError(
                f"test scorer expected {len(self._scores)} pairs, got {len(pairs)}"
            )
        return list(self._scores)


@pytest.mark.smoke
def test_satisfies_nli_scorer_protocol() -> None:
    e = EnsembleScorer([_ConstScorer(0.5), _ConstScorer(0.5)])
    assert isinstance(e, NLIScorer)


@pytest.mark.smoke
def test_empty_input_returns_empty() -> None:
    e = EnsembleScorer([_ConstScorer(0.5), _ConstScorer(0.9)])
    assert e.score_pairs([]) == []


@pytest.mark.smoke
def test_min_aggregation() -> None:
    e = EnsembleScorer(
        [_IndexedScorer([0.9, 0.1]), _IndexedScorer([0.5, 0.8])],
        aggregation="min",
    )
    assert e.score_pairs([("p", "h"), ("p", "h")]) == [pytest.approx(0.5), pytest.approx(0.1)]


@pytest.mark.smoke
def test_mean_aggregation() -> None:
    e = EnsembleScorer(
        [_IndexedScorer([0.8, 0.2]), _IndexedScorer([0.4, 0.6])],
        aggregation="mean",
    )
    out = e.score_pairs([("p", "h"), ("p", "h")])
    assert out[0] == pytest.approx(0.6)
    assert out[1] == pytest.approx(0.4)


@pytest.mark.smoke
def test_max_aggregation() -> None:
    e = EnsembleScorer(
        [_IndexedScorer([0.3, 0.7]), _IndexedScorer([0.6, 0.2])],
        aggregation="max",
    )
    assert e.score_pairs([("p", "h"), ("p", "h")]) == [pytest.approx(0.6), pytest.approx(0.7)]


@pytest.mark.smoke
def test_three_scorers_min_aggregation() -> None:
    """Triple ensemble (e.g. HHEM + MiniCheck + Sonnet)."""
    e = EnsembleScorer(
        [_ConstScorer(0.9), _ConstScorer(0.6), _ConstScorer(0.3)],
        aggregation="min",
    )
    assert e.score_pairs([("p", "h")]) == [pytest.approx(0.3)]


@pytest.mark.smoke
def test_rejects_single_scorer() -> None:
    with pytest.raises(ValueError, match="≥2 scorers"):
        EnsembleScorer([_ConstScorer(0.5)])


@pytest.mark.smoke
def test_rejects_unknown_aggregation() -> None:
    with pytest.raises(ValueError, match="aggregation must be"):
        EnsembleScorer([_ConstScorer(0.5), _ConstScorer(0.5)], aggregation="median")


@pytest.mark.smoke
def test_length_mismatch_raises() -> None:
    """If an underlying scorer returns the wrong-length list, surface clearly."""

    class _BadScorer:
        def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
            return [0.5]  # always 1 — wrong if called with >1 pair

    e = EnsembleScorer([_BadScorer(), _ConstScorer(0.5)])
    with pytest.raises(RuntimeError, match="length mismatch"):
        e.score_pairs([("p1", "h1"), ("p2", "h2")])
