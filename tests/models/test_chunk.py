"""Smoke tests for Chunk — ensures sentence_ids are preserved across chunks."""
import pytest

from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import Span

DOC_ID = "chunk-test-doc"


def _span(start: int, end: int) -> Span:
    return Span(doc_id=DOC_ID, char_start=start, char_end=end)


@pytest.mark.smoke
def test_chunk_requires_sentence_ids() -> None:
    with pytest.raises(ValueError):
        Chunk(
            chunk_id="c0",
            text="Some text.",
            doc_id=DOC_ID,
            sentence_ids=(),
            span=_span(0, 10),
        )


@pytest.mark.smoke
def test_chunk_span_doc_id_must_match() -> None:
    with pytest.raises(ValueError):
        Chunk(
            chunk_id="c0",
            text="Some text.",
            doc_id=DOC_ID,
            sentence_ids=(f"{DOC_ID}::s0",),
            span=Span(doc_id="different-doc", char_start=0, char_end=10),
        )


@pytest.mark.smoke
def test_chunk_sentence_ids_preserved() -> None:
    ids = (f"{DOC_ID}::s0", f"{DOC_ID}::s1")
    chunk = Chunk(
        chunk_id="c0",
        text="Sentence 0. Sentence 1.",
        doc_id=DOC_ID,
        sentence_ids=ids,
        span=_span(0, 23),
    )
    assert chunk.sentence_ids == ids


@pytest.mark.smoke
def test_chunk_can_span_pages() -> None:
    """A chunk's bounding span may cross page boundaries — that's the whole point."""
    chunk = Chunk(
        chunk_id="c0",
        text="Long chunk crossing pages.",
        doc_id=DOC_ID,
        sentence_ids=(f"{DOC_ID}::s0", f"{DOC_ID}::s1"),
        span=_span(900, 1200),  # spans a page break at e.g. offset 1000
    )
    assert chunk.span.char_start == 900
    assert chunk.span.char_end == 1200


@pytest.mark.smoke
def test_retrieved_chunk_wraps_chunk() -> None:
    chunk = Chunk(
        chunk_id="c0",
        text="Text.",
        doc_id=DOC_ID,
        sentence_ids=(f"{DOC_ID}::s0",),
        span=_span(0, 5),
    )
    rc = RetrievedChunk(chunk=chunk, score=0.87, retrieval_method="hybrid")
    assert rc.chunk is chunk
    assert rc.score == pytest.approx(0.87)
