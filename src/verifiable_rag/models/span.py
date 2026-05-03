from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BBox:  # Bounding Box
    """Page-coordinate bounding box (PDF user-space units)."""

    x0: float
    y0: float
    x1: float
    y1: float

    def area(self) -> float:
        return max(0.0, self.x1 - self.x0) * max(0.0, self.y1 - self.y0)


@dataclass(frozen=True)
class PageBBox:
    """A bounding box on a specific page.

    Spans crossing page boundaries carry one PageBBox per page they touch
    (e.g. a sentence whose tail wraps onto the next page has two).
    """

    page: int  # 0-indexed
    bbox: BBox

    def __post_init__(self) -> None:
        if self.page < 0:
            raise ValueError(f"page must be >= 0, got {self.page}")


@dataclass(frozen=True)
class Span:
    """Exact source location of a piece of text.

    Offsets are character positions into the *full document text*, so spans
    naturally support text that crosses page boundaries.  Use
    Document.page_for_offset()/pages_for_span() to recover page numbers when
    bboxes are not populated.

    Invariant: every object in the pipeline that wraps text from a source
    document must carry a Span.  Losing a Span is a bug.
    """

    doc_id: str
    char_start: int  # offset into Document.full_text
    char_end: int    # exclusive
    bboxes: tuple[PageBBox, ...] = ()  # sorted ascending by page; empty if unknown

    def __post_init__(self) -> None:
        if self.char_start < 0:
            raise ValueError(f"char_start must be >= 0, got {self.char_start}")
        if self.char_end < self.char_start:
            raise ValueError(
                f"char_end ({self.char_end}) must be >= char_start ({self.char_start})"
            )
        pages = [pb.page for pb in self.bboxes]
        if pages != sorted(pages):
            raise ValueError(f"bboxes must be sorted by page, got {pages}")

    def length(self) -> int:
        return self.char_end - self.char_start

    @property
    def pages(self) -> tuple[int, ...]:
        """Page numbers this span touches, derived from bboxes.  Empty if unknown."""
        return tuple(pb.page for pb in self.bboxes)

    def overlaps(self, other: Span) -> bool:
        if self.doc_id != other.doc_id:
            return False
        return self.char_start < other.char_end and other.char_start < self.char_end

    def contains(self, other: Span) -> bool:
        if self.doc_id != other.doc_id:
            return False
        return self.char_start <= other.char_start and other.char_end <= self.char_end

    @classmethod
    def merge(cls, spans: list[Span]) -> Span:
        """Return a bounding Span covering all spans in the list.

        bboxes from input spans are union-ed and re-sorted by (page, y0, x0).
        Duplicate (page, bbox) pairs are dropped.
        """
        if not spans:
            raise ValueError("Cannot merge empty span list")
        doc_ids = {s.doc_id for s in spans}
        if len(doc_ids) > 1:
            raise ValueError(f"Cannot merge spans from different documents: {doc_ids}")

        seen: set[tuple[int, BBox]] = set()
        all_bboxes: list[PageBBox] = []
        for s in spans:
            for pb in s.bboxes:
                key = (pb.page, pb.bbox)
                if key not in seen:
                    seen.add(key)
                    all_bboxes.append(pb)
        all_bboxes.sort(key=lambda pb: (pb.page, pb.bbox.y0, pb.bbox.x0))

        return cls(
            doc_id=spans[0].doc_id,
            char_start=min(s.char_start for s in spans),
            char_end=max(s.char_end for s in spans),
            bboxes=tuple(all_bboxes),
        )
