"""NLIVerifier tests — uses scripted NLIScorer stubs, no real models."""

from __future__ import annotations

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.document import Document
from verifiable_rag.verifiers import NLIScorer, NLIVerifier, Verifier


# --------------------------------------------------------------------------- #
# Scripted scorers
# --------------------------------------------------------------------------- #


class _ConstScorer:
    def __init__(self, score: float) -> None:
        self._score = score

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        return [self._score] * len(pairs)


class _ScriptedScorer:
    """Returns scores by hypothesis-text lookup."""

    def __init__(self, scores: dict[str, float], default: float = 0.5) -> None:
        self._scores = scores
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
    v = NLIVerifier(_ConstScorer(0.7))
    assert isinstance(v, Verifier)


@pytest.mark.smoke
def test_satisfies_nli_scorer_protocol_passthrough() -> None:
    """NLIVerifier itself implements NLIScorer — score_pairs delegates."""
    v = NLIVerifier(_ConstScorer(0.7))
    assert isinstance(v, NLIScorer)
    assert v.score_pairs([("p", "h")]) == [0.7]


@pytest.mark.smoke
def test_invalid_threshold_raises() -> None:
    with pytest.raises(ValueError, match="threshold"):
        NLIVerifier(_ConstScorer(0.5), threshold=1.5)
    with pytest.raises(ValueError, match="threshold"):
        NLIVerifier(_ConstScorer(0.5), threshold=-0.1)


# --------------------------------------------------------------------------- #
# verify() — edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_empty_sentences_returns_empty_no_scorer_calls() -> None:
    scorer = _ScriptedScorer({})
    v = NLIVerifier(scorer)
    assert v.verify([], {}) == []
    assert scorer.calls == []


@pytest.mark.smoke
def test_no_citations_yields_zero_score() -> None:
    doc = _make_doc()
    cs = CitedSentence(text="A claim.", supporting_sentence_ids=(), confidence=0.0)
    scorer = _ScriptedScorer({})
    v = NLIVerifier(scorer)
    results = v.verify([cs], {doc.doc_id: doc})
    assert len(results) == 1
    assert results[0].nli_score == 0.0
    assert results[0].is_supported is False
    assert scorer.calls == []  # never called for empty-cite sentence


@pytest.mark.smoke
def test_unknown_cited_id_yields_zero_score() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Made-up.",
        supporting_sentence_ids=("bio::sNOPE",),
        confidence=1.0,
    )
    scorer = _ScriptedScorer({})
    v = NLIVerifier(scorer)
    results = v.verify([cs], {doc.doc_id: doc})
    assert results[0].nli_score == 0.0
    assert results[0].is_supported is False


# --------------------------------------------------------------------------- #
# verify() — scoring + threshold
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_threshold_application_above_supports() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0",),
        confidence=1.0,
    )
    scorer = _ScriptedScorer({"Hagrid is a wizard.": 0.85})
    v = NLIVerifier(scorer, threshold=0.5)
    results = v.verify([cs], {doc.doc_id: doc})
    assert results[0].nli_score == pytest.approx(0.85)
    assert results[0].is_supported is True


@pytest.mark.smoke
def test_threshold_application_below_unsupports() -> None:
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0",),
        confidence=1.0,
    )
    scorer = _ScriptedScorer({"Hagrid is a wizard.": 0.3})
    v = NLIVerifier(scorer, threshold=0.5)
    results = v.verify([cs], {doc.doc_id: doc})
    assert results[0].nli_score == pytest.approx(0.3)
    assert results[0].is_supported is False


@pytest.mark.smoke
def test_one_call_per_verify_batch() -> None:
    """All pairs go through the underlying scorer in a single batched call."""
    doc = _make_doc()
    sentences = [
        CitedSentence(text="s1", supporting_sentence_ids=("bio::s0",), confidence=1.0),
        CitedSentence(text="s2", supporting_sentence_ids=("bio::s1",), confidence=1.0),
        CitedSentence(text="s3", supporting_sentence_ids=("bio::s2",), confidence=1.0),
    ]
    scorer = _ScriptedScorer({}, default=0.7)
    v = NLIVerifier(scorer)
    v.verify(sentences, {doc.doc_id: doc})
    assert len(scorer.calls) == 1
    assert len(scorer.calls[0]) == 3


@pytest.mark.smoke
def test_preserves_order_with_mixed_empty_premises() -> None:
    doc = _make_doc()
    sentences = [
        CitedSentence(text="cited", supporting_sentence_ids=("bio::s0",), confidence=1.0),
        CitedSentence(text="empty", supporting_sentence_ids=(), confidence=0.5),
        CitedSentence(text="cited2", supporting_sentence_ids=("bio::s2",), confidence=1.0),
    ]
    scorer = _ScriptedScorer({"cited": 0.9, "cited2": 0.8})
    v = NLIVerifier(scorer, threshold=0.5)
    results = v.verify(sentences, {doc.doc_id: doc})

    assert len(results) == 3
    assert results[0].claim_text == "cited"
    assert results[0].nli_score == pytest.approx(0.9)
    assert results[1].claim_text == "empty"
    assert results[1].nli_score == 0.0
    assert results[2].claim_text == "cited2"
    assert results[2].nli_score == pytest.approx(0.8)
