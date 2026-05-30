"""Answer convenience-property tests — the programmatic audit trail UX."""

from __future__ import annotations

import json

import pytest

from verifiable_rag.models.answer import (
    Answer,
    CitedSentence,
    FaithfulnessComponents,
    VerificationResult,
)
from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import Span


def _make_answer(
    *,
    n_supported: int = 2,
    n_unsupported: int = 1,
    has_verification: bool = True,
    has_retrieved: bool = True,
    was_refused: bool = False,
) -> Answer:
    """Build a synthetic Answer with controllable verification shape."""
    sentences: list[CitedSentence] = []
    for i in range(n_supported):
        sentences.append(
            CitedSentence(
                text=f"Supported claim {i}.",
                supporting_sentence_ids=(f"doc::s{i}",),
                confidence=0.9,
            )
        )
    for i in range(n_unsupported):
        sentences.append(
            CitedSentence(
                text=f"Unsupported claim {i}.",
                supporting_sentence_ids=(f"doc::s{n_supported + i}",),
                confidence=0.5,
            )
        )
    verification: list[VerificationResult] = []
    if has_verification:
        for i in range(n_supported):
            verification.append(
                VerificationResult(
                    cited_sentence_index=i,
                    claim_text=f"Supported claim {i}.",
                    is_supported=True,
                    nli_score=0.85 + 0.01 * i,
                )
            )
        for i in range(n_unsupported):
            verification.append(
                VerificationResult(
                    cited_sentence_index=n_supported + i,
                    claim_text=f"Unsupported claim {i}.",
                    is_supported=False,
                    nli_score=0.1,
                )
            )
    retrieved: list[RetrievedChunk] = []
    if has_retrieved:
        chunk = Chunk(
            chunk_id="doc::c0",
            text="Some chunk text.",
            doc_id="doc",
            sentence_ids=tuple(f"doc::s{i}" for i in range(n_supported + n_unsupported)),
            span=Span(doc_id="doc", char_start=0, char_end=16),
            metadata={},
        )
        retrieved = [RetrievedChunk(chunk=chunk, score=0.8, retrieval_method="hybrid")]
    return Answer(
        query="Q?",
        sentences=sentences,
        faithfulness_score=0.5,
        faithfulness_components=FaithfulnessComponents(
            retrieval_score=0.8, nli_score=0.5
        ),
        unsupported_claims=[s.text for s in sentences[n_supported:]] if has_verification else [],
        retrieved_chunks=retrieved,
        verification_results=verification,
        strictness="balanced",
        was_refused=was_refused,
        refusal_reason="not enough support" if was_refused else None,
    )


# --------------------------------------------------------------------------- #
# verification_for
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_verification_for_returns_matching_result() -> None:
    a = _make_answer(n_supported=1, n_unsupported=1)
    vr = a.verification_for(1)
    assert vr is not None
    assert vr.cited_sentence_index == 1
    assert not vr.is_supported


@pytest.mark.smoke
def test_verification_for_returns_none_when_no_match() -> None:
    a = _make_answer(n_supported=1, n_unsupported=0)
    assert a.verification_for(99) is None


@pytest.mark.smoke
def test_verification_for_returns_none_when_no_verifier() -> None:
    a = _make_answer(has_verification=False)
    assert a.verification_for(0) is None


# --------------------------------------------------------------------------- #
# supported_sentences / unsupported_sentences
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_supported_sentences_filters_by_is_supported() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    assert len(a.supported_sentences) == 2
    assert all("Supported" in s.text for s in a.supported_sentences)


@pytest.mark.smoke
def test_unsupported_sentences_filters_by_is_supported() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    assert len(a.unsupported_sentences) == 1
    assert "Unsupported" in a.unsupported_sentences[0].text


@pytest.mark.smoke
def test_supported_default_when_no_verifier_ran() -> None:
    """Without a verifier, sentences default to supported (lib's null-safety)."""
    a = _make_answer(n_supported=2, n_unsupported=0, has_verification=False)
    assert len(a.supported_sentences) == 2
    assert a.unsupported_sentences == []


@pytest.mark.smoke
def test_unsupported_complement_is_strict() -> None:
    """unsupported_sentences requires an EXPLICIT is_supported=False."""
    a = _make_answer(has_verification=False)
    assert a.unsupported_sentences == []


# --------------------------------------------------------------------------- #
# cited_sentence_ids
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_cited_sentence_ids_unions_across_sentences() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    assert a.cited_sentence_ids == frozenset(
        {"doc::s0", "doc::s1", "doc::s2"}
    )


@pytest.mark.smoke
def test_cited_sentence_ids_dedupes() -> None:
    """Two sentences citing the same source → one entry in the set."""
    sentences = [
        CitedSentence(text="A.", supporting_sentence_ids=("doc::s0",), confidence=1.0),
        CitedSentence(text="B.", supporting_sentence_ids=("doc::s0", "doc::s1"), confidence=1.0),
    ]
    a = Answer(
        query="Q?",
        sentences=sentences,
        faithfulness_score=0.5,
        faithfulness_components=FaithfulnessComponents(retrieval_score=0.5, nli_score=0.5),
        unsupported_claims=[],
        retrieved_chunks=[],
        verification_results=[],
        strictness="balanced",
    )
    assert a.cited_sentence_ids == frozenset({"doc::s0", "doc::s1"})


# --------------------------------------------------------------------------- #
# nli_scores / min_nli_score
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_nli_scores_returns_list_in_verification_order() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    scores = a.nli_scores
    assert len(scores) == 3
    # supported scores were 0.85, 0.86; unsupported was 0.1
    assert scores[0] == pytest.approx(0.85)
    assert scores[2] == pytest.approx(0.1)


@pytest.mark.smoke
def test_min_nli_score_returns_worst_case() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    assert a.min_nli_score == pytest.approx(0.1)


@pytest.mark.smoke
def test_min_nli_score_returns_one_when_no_verifier() -> None:
    """When no verifier ran, there's no evidence of unfaithfulness — min = 1.0."""
    a = _make_answer(has_verification=False)
    assert a.min_nli_score == 1.0


# --------------------------------------------------------------------------- #
# audit_trail
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_audit_trail_returns_dict_with_core_fields() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    audit = a.audit_trail()
    assert audit["query"] == "Q?"
    assert audit["strictness"] == "balanced"
    assert audit["was_refused"] is False
    assert audit["n_sentences"] == 3
    assert audit["n_supported"] == 2
    assert audit["n_unsupported"] == 1
    assert audit["n_verified"] == 3
    assert audit["faithfulness_score"] == 0.5
    assert audit["min_nli_score"] == pytest.approx(0.1)
    assert "Unsupported claim 0." in audit["unsupported_claims"]


@pytest.mark.smoke
def test_audit_trail_is_json_serializable() -> None:
    a = _make_answer(n_supported=2, n_unsupported=1)
    audit = a.audit_trail()
    # round-trip through JSON to confirm no non-serializable values slipped in
    serialized = json.dumps(audit)
    parsed = json.loads(serialized)
    assert parsed["query"] == "Q?"
    assert parsed["min_nli_score"] == pytest.approx(0.1)


@pytest.mark.smoke
def test_audit_trail_includes_refusal_info() -> None:
    a = _make_answer(was_refused=True)
    audit = a.audit_trail()
    assert audit["was_refused"] is True
    assert audit["refusal_reason"] == "not enough support"


@pytest.mark.smoke
def test_audit_trail_mean_nli_is_none_when_no_verifier() -> None:
    a = _make_answer(has_verification=False)
    audit = a.audit_trail()
    assert audit["mean_nli_score"] is None
    assert audit["n_verified"] == 0
