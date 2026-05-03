"""Smoke tests for the Document model — span round-trips and page lookups."""
from pathlib import Path

import pytest

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import Span


DOC_ID = "test-doc-roundtrip"


def _make_sentence(idx: int) -> Sentence:
    start = idx * 50
    return Sentence(
        id=f"{DOC_ID}::s{idx}",
        text=f"Sentence {idx} contains some verifiable content.",
        span=Span(doc_id=DOC_ID, char_start=start, char_end=start + 49),
    )


@pytest.mark.smoke
def test_sentence_rejects_empty_text() -> None:
    with pytest.raises(ValueError):
        Sentence(
            id=f"{DOC_ID}::s0",
            text="   ",
            span=Span(doc_id=DOC_ID, char_start=0, char_end=1),
        )


@pytest.mark.smoke
def test_sentence_id_must_contain_doc_id() -> None:
    with pytest.raises(ValueError):
        Sentence(
            id="wrong-doc::s0",
            text="Hello.",
            span=Span(doc_id=DOC_ID, char_start=0, char_end=6),
        )


@pytest.mark.smoke
def test_document_sentences_roundtrip(simple_document: Document) -> None:
    """All sentences accessible via Document.sentences must have valid spans."""
    sentences = simple_document.sentences
    assert len(sentences) == 3
    for s in sentences:
        assert s.span.doc_id == simple_document.doc_id
        assert s.span.char_end > s.span.char_start


@pytest.mark.smoke
def test_document_sentence_by_id(simple_document: Document) -> None:
    target = simple_document.sentences[1]
    found = simple_document.sentence_by_id(target.id)
    assert found is target


@pytest.mark.smoke
def test_document_sentence_by_id_missing(simple_document: Document) -> None:
    with pytest.raises(KeyError):
        simple_document.sentence_by_id("nonexistent::s999")


@pytest.mark.smoke
def test_paragraph_rejects_empty_sentences() -> None:
    with pytest.raises(ValueError):
        Paragraph(
            id=f"{DOC_ID}::para0",
            sentences=[],
            span=Span(doc_id=DOC_ID, char_start=0, char_end=10),
        )


@pytest.mark.smoke
def test_document_paragraphs_property(simple_document: Document) -> None:
    paras = simple_document.paragraphs
    assert len(paras) == 1
    assert paras[0].text  # not empty


@pytest.mark.smoke
def test_span_preserved_through_document_hierarchy() -> None:
    """Round-trip: build Document, retrieve Sentence, check span integrity."""
    s0 = _make_sentence(0)
    s1 = _make_sentence(1)
    para = Paragraph(
        id=f"{DOC_ID}::para0",
        sentences=[s0, s1],
        span=Span(doc_id=DOC_ID, char_start=0, char_end=99),
    )
    sec = Section(
        id=f"{DOC_ID}::sec0",
        title=None,
        paragraphs=[para],
        span=Span(doc_id=DOC_ID, char_start=0, char_end=99),
    )
    doc = Document(
        doc_id=DOC_ID,
        source_path=Path("dummy.pdf"),
        sections=[sec],
        page_breaks=[0],
    )

    for sentence in doc.sentences:
        assert sentence.span.doc_id == doc.doc_id, (
            f"Sentence {sentence.id!r} span.doc_id {sentence.span.doc_id!r} "
            f"!= doc.doc_id {doc.doc_id!r}"
        )


# ---------- page_breaks / page_for_offset ----------------------------------

@pytest.mark.smoke
def test_document_page_for_offset() -> None:
    """A 3-page document with page breaks at offsets 0, 1000, 2500."""
    doc = Document(
        doc_id="multi-page-doc",
        source_path=Path("test.pdf"),
        sections=[],
        page_breaks=[0, 1000, 2500],
    )
    assert doc.num_pages == 3
    assert doc.page_for_offset(0) == 0
    assert doc.page_for_offset(500) == 0
    assert doc.page_for_offset(999) == 0
    assert doc.page_for_offset(1000) == 1
    assert doc.page_for_offset(2499) == 1
    assert doc.page_for_offset(2500) == 2
    assert doc.page_for_offset(5000) == 2  # past last break — still last page


@pytest.mark.smoke
def test_document_pages_for_span_single_page() -> None:
    doc = Document(
        doc_id="single-page-doc",
        source_path=Path("test.pdf"),
        sections=[],
        page_breaks=[0, 1000],
    )
    s = Span(doc_id="single-page-doc", char_start=200, char_end=400)
    first, last = doc.pages_for_span(s)
    assert first == 0
    assert last == 0


@pytest.mark.smoke
def test_document_pages_for_span_cross_page() -> None:
    """A sentence whose span crosses a page boundary returns (n, n+1)."""
    doc = Document(
        doc_id="cross-page-doc",
        source_path=Path("test.pdf"),
        sections=[],
        page_breaks=[0, 1000],
    )
    cross = Span(doc_id="cross-page-doc", char_start=950, char_end=1050)
    first, last = doc.pages_for_span(cross)
    assert first == 0
    assert last == 1


@pytest.mark.smoke
def test_document_pages_for_span_ending_on_break_does_not_leak() -> None:
    """Span ending exactly at a page break belongs to the previous page only."""
    doc = Document(
        doc_id="d",
        source_path=Path("t.pdf"),
        sections=[],
        page_breaks=[0, 1000],
    )
    s = Span(doc_id="d", char_start=500, char_end=1000)  # char_end is exclusive
    first, last = doc.pages_for_span(s)
    assert first == 0
    assert last == 0


@pytest.mark.smoke
def test_document_pages_for_span_wrong_doc_raises() -> None:
    doc = Document(
        doc_id="doc-a",
        source_path=Path("t.pdf"),
        sections=[],
        page_breaks=[0],
    )
    foreign = Span(doc_id="doc-b", char_start=0, char_end=10)
    with pytest.raises(ValueError):
        doc.pages_for_span(foreign)


@pytest.mark.smoke
def test_document_page_for_offset_no_breaks_raises() -> None:
    doc = Document(
        doc_id="no-pages",
        source_path=Path("test.pdf"),
        sections=[],
        page_breaks=[],
    )
    with pytest.raises(ValueError):
        doc.page_for_offset(0)


@pytest.mark.smoke
def test_document_page_breaks_must_start_at_zero() -> None:
    with pytest.raises(ValueError):
        Document(
            doc_id="bad",
            source_path=Path("test.pdf"),
            sections=[],
            page_breaks=[10, 20, 30],
        )


@pytest.mark.smoke
def test_document_page_breaks_must_be_sorted() -> None:
    with pytest.raises(ValueError):
        Document(
            doc_id="bad",
            source_path=Path("test.pdf"),
            sections=[],
            page_breaks=[0, 30, 20],
        )
