"""DualNLIVerifier tests — uses scripted scorers, no real models."""

from __future__ import annotations

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.document import Document
from verifiable_rag.verifiers import DualNLIVerifier, NLIScorer, Verifier


# --------------------------------------------------------------------------- #
# Scripted scorers
# --------------------------------------------------------------------------- #


class _ConstScorer:
    def __init__(self, score: float) -> None:
        self._score = score

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        return [self._score] * len(pairs)


class _ScriptedScorer:
    """Returns scores by exact hypothesis-text lookup."""

    def __init__(self, by_hypothesis: dict[str, float], default: float = 0.5) -> None:
        self._scores = by_hypothesis
        self._default = default
        self.calls: list[list[tuple[str, str]]] = []

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        self.calls.append(list(pairs))
        return [self._scores.get(h, self._default) for _, h in pairs]


def _make_doc() -> Document:
    return build_document(
        sections_spec=[
            ("Intro", [["Hagrid is a wizard.", "He keeps the keys at Hogwarts."]]),
            ("Methods", [["Harry has a lightning-bolt scar."]]),
        ],
        doc_id="bio",
    )


# --------------------------------------------------------------------------- #
# Protocol + construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_satisfies_verifier_protocol() -> None:
    v = DualNLIVerifier(_ConstScorer(0.5), _ConstScorer(0.5))
    assert isinstance(v, Verifier)


@pytest.mark.smoke
def test_satisfies_nli_scorer_protocol() -> None:
    """Dual itself exposes score_pairs (pass-through to ensemble)."""
    v = DualNLIVerifier(_ConstScorer(0.5), _ConstScorer(0.5))
    assert isinstance(v, NLIScorer)


@pytest.mark.smoke
def test_invalid_threshold_raises() -> None:
    with pytest.raises(ValueError, match="threshold"):
        DualNLIVerifier(_ConstScorer(0.5), _ConstScorer(0.5), threshold=1.5)
    with pytest.raises(ValueError, match="threshold"):
        DualNLIVerifier(_ConstScorer(0.5), _ConstScorer(0.5), threshold=-0.1)


@pytest.mark.smoke
def test_invalid_aggregation_raises() -> None:
    with pytest.raises(ValueError, match="aggregation"):
        DualNLIVerifier(_ConstScorer(0.5), _ConstScorer(0.5), aggregation="median")


# --------------------------------------------------------------------------- #
# verify() — edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_empty_sentences_returns_empty() -> None:
    a, b = _ScriptedScorer({}), _ScriptedScorer({})
    v = DualNLIVerifier(a, b)
    assert v.verify([], {}) == []
    assert a.calls == [] and b.calls == []


@pytest.mark.smoke
def test_no_citations_yields_zero_score() -> None:
    doc = _make_doc()
    cs = CitedSentence(text="A claim.", supporting_sentence_ids=(), confidence=0.0)
    a, b = _ScriptedScorer({}), _ScriptedScorer({})
    v = DualNLIVerifier(a, b)
    results = v.verify([cs], {doc.doc_id: doc})
    assert len(results) == 1
    assert results[0].nli_score == 0.0
    assert results[0].is_supported is False
    # Neither scorer was called — no work to do.
    assert a.calls == [] and b.calls == []


@pytest.mark.smoke
def test_unknown_cited_id_yields_zero_score() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Made-up.",
        supporting_sentence_ids=("bio::sNOPE",),
        confidence=1.0,
    )
    a, b = _ScriptedScorer({}), _ScriptedScorer({})
    v = DualNLIVerifier(a, b)
    results = v.verify([cs], {doc.doc_id: doc})
    assert results[0].nli_score == 0.0
    assert results[0].is_supported is False


# --------------------------------------------------------------------------- #
# verify() — scoring, aggregation, threshold
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_min_aggregation_picks_lower_scorer() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0",),
        confidence=1.0,
    )
    a = _ScriptedScorer({"Hagrid is a wizard.": 0.9})
    b = _ScriptedScorer({"Hagrid is a wizard.": 0.3})
    v = DualNLIVerifier(a, b, aggregation="min", threshold=0.5)
    results = v.verify([cs], {doc.doc_id: doc})
    # min(0.9, 0.3) = 0.3 < 0.5 → unsupported
    assert results[0].nli_score == pytest.approx(0.3)
    assert results[0].is_supported is False


@pytest.mark.smoke
def test_mean_aggregation_smooths() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0",),
        confidence=1.0,
    )
    a = _ScriptedScorer({"Hagrid is a wizard.": 0.9})
    b = _ScriptedScorer({"Hagrid is a wizard.": 0.3})
    v = DualNLIVerifier(a, b, aggregation="mean", threshold=0.5)
    results = v.verify([cs], {doc.doc_id: doc})
    assert results[0].nli_score == pytest.approx(0.6)  # (0.9 + 0.3) / 2
    assert results[0].is_supported is True  # 0.6 ≥ 0.5


@pytest.mark.smoke
def test_threshold_application_supported() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0",),
        confidence=1.0,
    )
    a = _ConstScorer(0.8)
    b = _ConstScorer(0.7)
    # min(0.8, 0.7) = 0.7 — well above default 0.0562
    v = DualNLIVerifier(a, b)
    results = v.verify([cs], {doc.doc_id: doc})
    assert results[0].is_supported is True


@pytest.mark.smoke
def test_one_call_per_scorer_per_verify_batch() -> None:
    """The ensemble batches all pairs into one score_pairs() call per scorer.

    Important for cost — a 4-sentence batch should mean 1 GPU call per scorer
    (not 4).
    """
    doc = _make_doc()
    sentences = [
        CitedSentence(text="s1", supporting_sentence_ids=("bio::s0",), confidence=1.0),
        CitedSentence(text="s2", supporting_sentence_ids=("bio::s1",), confidence=1.0),
        CitedSentence(text="s3", supporting_sentence_ids=("bio::s2",), confidence=1.0),
    ]
    a = _ScriptedScorer({}, default=0.7)
    b = _ScriptedScorer({}, default=0.6)
    v = DualNLIVerifier(a, b)
    v.verify(sentences, {doc.doc_id: doc})
    assert len(a.calls) == 1
    assert len(b.calls) == 1
    assert len(a.calls[0]) == 3
    assert len(b.calls[0]) == 3


@pytest.mark.smoke
def test_preserves_order_with_mixed_empty_premises() -> None:
    """Sentences with no citations interleave with cited ones — order preserved."""
    doc = _make_doc()
    sentences = [
        CitedSentence(text="cited", supporting_sentence_ids=("bio::s0",), confidence=1.0),
        CitedSentence(text="empty", supporting_sentence_ids=(), confidence=0.5),
        CitedSentence(text="cited2", supporting_sentence_ids=("bio::s2",), confidence=1.0),
    ]
    a = _ScriptedScorer({"cited": 0.9, "cited2": 0.8})
    b = _ScriptedScorer({"cited": 0.7, "cited2": 0.6})
    v = DualNLIVerifier(a, b, aggregation="min")
    results = v.verify(sentences, {doc.doc_id: doc})

    assert len(results) == 3
    assert results[0].claim_text == "cited"
    assert results[0].nli_score == pytest.approx(0.7)
    assert results[1].claim_text == "empty"
    assert results[1].nli_score == 0.0
    assert results[2].claim_text == "cited2"
    assert results[2].nli_score == pytest.approx(0.6)


@pytest.mark.smoke
def test_score_pairs_passthrough() -> None:
    """DualNLIVerifier itself implements NLIScorer — pass-through to ensemble."""
    a = _ScriptedScorer({"h1": 0.9, "h2": 0.4})
    b = _ScriptedScorer({"h1": 0.3, "h2": 0.8})
    v = DualNLIVerifier(a, b, aggregation="min")
    out = v.score_pairs([("p1", "h1"), ("p2", "h2")])
    assert out == [pytest.approx(0.3), pytest.approx(0.4)]
