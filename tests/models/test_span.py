"""Smoke tests for Span and BBox — the foundational span-preservation primitives.

Span uses document-level char offsets, so spans naturally cross page boundaries.
Multi-page bboxes are tested via PageBBox.
"""
import pytest

from verifiable_rag.models.span import BBox, PageBBox, Span


DOC = "doc-001"


@pytest.mark.smoke
def test_span_basic() -> None:
    s = Span(doc_id=DOC, char_start=10, char_end=50)
    assert s.length() == 40


@pytest.mark.smoke
def test_span_rejects_inverted() -> None:
    with pytest.raises(ValueError):
        Span(doc_id=DOC, char_start=50, char_end=10)


@pytest.mark.smoke
def test_span_rejects_negative_start() -> None:
    with pytest.raises(ValueError):
        Span(doc_id=DOC, char_start=-1, char_end=10)


@pytest.mark.smoke
def test_span_overlaps() -> None:
    a = Span(doc_id=DOC, char_start=0, char_end=20)
    b = Span(doc_id=DOC, char_start=10, char_end=30)
    c = Span(doc_id=DOC, char_start=20, char_end=40)
    assert a.overlaps(b)
    assert not a.overlaps(c)  # touching but not overlapping


@pytest.mark.smoke
def test_span_overlaps_cross_doc() -> None:
    a = Span(doc_id="doc-a", char_start=0, char_end=20)
    b = Span(doc_id="doc-b", char_start=10, char_end=30)
    assert not a.overlaps(b)


@pytest.mark.smoke
def test_span_contains() -> None:
    outer = Span(doc_id=DOC, char_start=0, char_end=100)
    inner = Span(doc_id=DOC, char_start=10, char_end=50)
    assert outer.contains(inner)
    assert not inner.contains(outer)


@pytest.mark.smoke
def test_span_merge() -> None:
    spans = [
        Span(doc_id=DOC, char_start=0, char_end=30),
        Span(doc_id=DOC, char_start=40, char_end=80),
        Span(doc_id=DOC, char_start=5, char_end=15),
    ]
    merged = Span.merge(spans)
    assert merged.doc_id == DOC
    assert merged.char_start == 0
    assert merged.char_end == 80


@pytest.mark.smoke
def test_span_merge_empty_raises() -> None:
    with pytest.raises(ValueError):
        Span.merge([])


@pytest.mark.smoke
def test_span_merge_cross_doc_raises() -> None:
    with pytest.raises(ValueError):
        Span.merge([
            Span(doc_id="doc-a", char_start=0, char_end=10),
            Span(doc_id="doc-b", char_start=0, char_end=10),
        ])


@pytest.mark.smoke
def test_span_merge_combines_bboxes_across_pages() -> None:
    """A sentence whose tail wraps onto the next page — both bboxes preserved."""
    pb_top = PageBBox(page=2, bbox=BBox(x0=0, y0=700, x1=400, y1=720))
    pb_bot = PageBBox(page=3, bbox=BBox(x0=0, y0=10, x1=400, y1=30))
    head = Span(doc_id=DOC, char_start=1000, char_end=1050, bboxes=(pb_top,))
    tail = Span(doc_id=DOC, char_start=1050, char_end=1100, bboxes=(pb_bot,))
    merged = Span.merge([head, tail])
    assert merged.char_start == 1000
    assert merged.char_end == 1100
    assert merged.pages == (2, 3)
    assert len(merged.bboxes) == 2


@pytest.mark.smoke
def test_span_merge_dedupes_identical_bboxes() -> None:
    pb = PageBBox(page=1, bbox=BBox(x0=0, y0=0, x1=10, y1=10))
    a = Span(doc_id=DOC, char_start=0, char_end=10, bboxes=(pb,))
    b = Span(doc_id=DOC, char_start=10, char_end=20, bboxes=(pb,))
    merged = Span.merge([a, b])
    assert len(merged.bboxes) == 1


@pytest.mark.smoke
def test_span_bboxes_must_be_sorted_by_page() -> None:
    pb_a = PageBBox(page=3, bbox=BBox(x0=0, y0=0, x1=10, y1=10))
    pb_b = PageBBox(page=2, bbox=BBox(x0=0, y0=0, x1=10, y1=10))
    with pytest.raises(ValueError):
        Span(doc_id=DOC, char_start=0, char_end=10, bboxes=(pb_a, pb_b))


@pytest.mark.smoke
def test_span_pages_property_empty_when_no_bboxes() -> None:
    s = Span(doc_id=DOC, char_start=0, char_end=10)
    assert s.pages == ()


@pytest.mark.smoke
def test_pagebbox_rejects_negative_page() -> None:
    with pytest.raises(ValueError):
        PageBBox(page=-1, bbox=BBox(x0=0, y0=0, x1=10, y1=10))


@pytest.mark.smoke
def test_bbox_area() -> None:
    bbox = BBox(x0=0, y0=0, x1=10, y1=20)
    assert bbox.area() == 200.0


@pytest.mark.smoke
def test_span_with_bboxes_roundtrip() -> None:
    pb = PageBBox(page=3, bbox=BBox(x0=10.0, y0=20.0, x1=200.0, y1=40.0))
    s = Span(doc_id=DOC, char_start=100, char_end=150, bboxes=(pb,))
    assert s.pages == (3,)
    assert s.bboxes[0].bbox.area() > 0
