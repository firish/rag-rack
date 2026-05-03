"""Smoke tests for Answer and CitedSentence."""
import pytest

from verifiable_rag.models.answer import (
    Answer,
    CitedSentence,
    FaithfulnessComponents,
    VerificationResult,
)


@pytest.mark.smoke
def test_cited_sentence_confidence_bounds() -> None:
    with pytest.raises(ValueError):
        CitedSentence(text="Hello.", supporting_sentence_ids=(), confidence=1.5)
    with pytest.raises(ValueError):
        CitedSentence(text="Hello.", supporting_sentence_ids=(), confidence=-0.1)


@pytest.mark.smoke
def test_cited_sentence_no_citations() -> None:
    s = CitedSentence(text="Ungrounded claim.", supporting_sentence_ids=(), confidence=0.0)
    assert len(s.supporting_sentence_ids) == 0


@pytest.mark.smoke
def test_answer_faithfulness_bounds() -> None:
    components = FaithfulnessComponents(retrieval_score=0.8, nli_score=0.9)
    with pytest.raises(ValueError):
        Answer(
            query="q",
            sentences=[],
            faithfulness_score=1.5,  # invalid
            faithfulness_components=components,
            unsupported_claims=[],
            retrieved_chunks=[],
            verification_results=[],
        )


@pytest.mark.smoke
def test_answer_refused_requires_reason() -> None:
    components = FaithfulnessComponents(retrieval_score=0.2, nli_score=0.1)
    with pytest.raises(ValueError):
        Answer(
            query="q",
            sentences=[],
            faithfulness_score=0.1,
            faithfulness_components=components,
            unsupported_claims=["bad claim"],
            retrieved_chunks=[],
            verification_results=[],
            was_refused=True,
            refusal_reason=None,  # missing — should raise
        )


@pytest.mark.smoke
def test_answer_text_joins_sentences() -> None:
    components = FaithfulnessComponents(retrieval_score=0.9, nli_score=0.95)
    sentences = [
        CitedSentence(text="First.", supporting_sentence_ids=("doc::p0::s0",), confidence=0.9),
        CitedSentence(text="Second.", supporting_sentence_ids=("doc::p0::s1",), confidence=0.85),
    ]
    answer = Answer(
        query="What?",
        sentences=sentences,
        faithfulness_score=0.92,
        faithfulness_components=components,
        unsupported_claims=[],
        retrieved_chunks=[],
        verification_results=[],
    )
    assert answer.text == "First. Second."
    assert answer.is_fully_supported


@pytest.mark.smoke
def test_imports() -> None:
    """All public names from verifiable_rag must be importable."""
    import verifiable_rag as vr
    assert hasattr(vr, "Pipeline")
    assert hasattr(vr, "Document")
    assert hasattr(vr, "Span")
    assert hasattr(vr, "Answer")
    assert hasattr(vr, "__version__")
