"""HTML report rendering tests."""

from __future__ import annotations

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.models.answer import (
    Answer,
    CitedSentence,
    FaithfulnessComponents,
    VerificationResult,
)
from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import Span
from verifiable_rag.report import to_html


def _make_answer(
    *,
    was_refused: bool = False,
    refusal_reason: str | None = None,
    has_verification: bool = True,
    has_chunks: bool = True,
) -> Answer:
    doc = build_document(
        sections_spec=[("Intro", [["Cats are mammals.", "They purr."]])],
        doc_id="paper",
    )
    sent0 = doc.sentence_by_id("paper::s0")
    sent1 = doc.sentence_by_id("paper::s1")

    sentences = [
        CitedSentence(
            text="Cats are mammals.",
            supporting_sentence_ids=("paper::s0",),
            confidence=0.9,
        ),
        CitedSentence(
            text="They allegedly speak French.",
            supporting_sentence_ids=("paper::s1",),
            confidence=0.4,
        ),
    ]
    verification = []
    if has_verification:
        verification = [
            VerificationResult(
                cited_sentence_index=0,
                claim_text="Cats are mammals.",
                is_supported=True,
                nli_score=0.92,
            ),
            VerificationResult(
                cited_sentence_index=1,
                claim_text="They allegedly speak French.",
                is_supported=False,
                nli_score=0.04,
            ),
        ]
    retrieved_chunks: list[RetrievedChunk] = []
    if has_chunks:
        chunk = Chunk(
            chunk_id="paper::c0",
            text="Cats are mammals. They purr.",
            doc_id=doc.doc_id,
            sentence_ids=("paper::s0", "paper::s1"),
            span=Span(doc_id=doc.doc_id, char_start=0, char_end=28),
            metadata={"section_id": "sec_0"},
        )
        retrieved_chunks = [
            RetrievedChunk(chunk=chunk, score=0.81, retrieval_method="hybrid")
        ]

    return Answer(
        query="What can you tell me about cats?",
        sentences=sentences,
        faithfulness_score=0.66,
        faithfulness_components=FaithfulnessComponents(
            retrieval_score=0.81, nli_score=0.48
        ),
        unsupported_claims=(
            ["They allegedly speak French."] if has_verification else []
        ),
        retrieved_chunks=retrieved_chunks,
        verification_results=verification,
        strictness="balanced",
        was_refused=was_refused,
        refusal_reason=refusal_reason,
    )


# --------------------------------------------------------------------------- #
# Basic output shape
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_to_html_returns_full_document() -> None:
    answer = _make_answer()
    out = to_html(answer)
    assert out.startswith("<!DOCTYPE html>")
    assert "</html>" in out
    assert "verifiable-rag report" in out


@pytest.mark.smoke
def test_html_includes_query_text() -> None:
    answer = _make_answer()
    out = to_html(answer)
    assert "What can you tell me about cats?" in out


@pytest.mark.smoke
def test_html_includes_answer_sentences() -> None:
    answer = _make_answer()
    out = to_html(answer)
    assert "Cats are mammals." in out
    assert "They allegedly speak French." in out


@pytest.mark.smoke
def test_html_includes_faithfulness_score() -> None:
    answer = _make_answer()
    out = to_html(answer)
    # the overall score
    assert "0.660" in out
    # the components
    assert "0.810" in out  # retrieval_score
    assert "0.480" in out  # nli_score


# --------------------------------------------------------------------------- #
# Color coding + citation flow
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_supported_sentences_get_supported_class() -> None:
    answer = _make_answer()
    out = to_html(answer)
    # The first sentence is supported; the second isn't.
    # The 'unsupported' class should appear at least once.
    assert "sentence unsupported" in out
    assert "sentence supported" in out


@pytest.mark.smoke
def test_citations_become_anchor_links_to_chunks() -> None:
    answer = _make_answer()
    out = to_html(answer)
    # The chunk anchor matches the chunk_id; the cite href points to it.
    assert "id='chunk-paper::c0'" in out or 'id="chunk-paper::c0"' in out
    assert "href='#chunk-paper::c0'" in out or 'href="#chunk-paper::c0"' in out


@pytest.mark.smoke
def test_citation_without_matching_chunk_renders_as_plain_text() -> None:
    """If the cited sentence_id doesn't belong to any retrieved chunk, fall back
    to a non-link span so we don't emit a broken anchor."""
    answer = _make_answer(has_chunks=False)
    out = to_html(answer)
    # cite label still present
    assert "paper::s0" in out
    # but no href to a non-existent anchor
    assert "href='#chunk-" not in out
    assert 'href="#chunk-' not in out


# --------------------------------------------------------------------------- #
# Refusal handling
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_refusal_banner_shows_reason() -> None:
    answer = _make_answer(
        was_refused=True, refusal_reason="faithfulness below threshold (0.21 < 0.5)"
    )
    out = to_html(answer)
    assert "Refused" in out
    assert "faithfulness below threshold" in out


@pytest.mark.smoke
def test_no_refusal_banner_when_not_refused() -> None:
    answer = _make_answer(was_refused=False)
    out = to_html(answer)
    assert "Refused" not in out


# --------------------------------------------------------------------------- #
# Optional sections
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_skips_verification_section_when_no_results() -> None:
    answer = _make_answer(has_verification=False)
    out = to_html(answer)
    assert "Per-sentence verification" not in out


@pytest.mark.smoke
def test_skips_passages_section_when_no_chunks() -> None:
    answer = _make_answer(has_chunks=False)
    out = to_html(answer)
    assert "Reranked passages" not in out


# --------------------------------------------------------------------------- #
# Escaping — no XSS via answer text
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_html_escapes_query_special_chars() -> None:
    """A query containing HTML/script must not produce live markup."""
    answer = _make_answer()
    # Mutate query to contain a dangerous string
    object.__setattr__(answer, "query", "<script>alert(1)</script>")
    out = to_html(answer)
    assert "<script>alert(1)</script>" not in out
    assert "&lt;script&gt;" in out


@pytest.mark.smoke
def test_answer_to_html_method_works() -> None:
    """Answer.to_html() delegates to report.to_html() — sanity check."""
    answer = _make_answer()
    out = answer.to_html()
    assert out.startswith("<!DOCTYPE html>")
    assert "Cats are mammals." in out


@pytest.mark.smoke
def test_answer_to_html_title_override() -> None:
    answer = _make_answer()
    out = answer.to_html(title="My Custom Title")
    assert "My Custom Title" in out
