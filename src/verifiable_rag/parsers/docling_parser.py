"""DoclingParser: PDF → span-tracked Document.

Produces a Document where every Sentence carries (doc_id, char_start, char_end,
bboxes) such that ``doc.full_text[s.span.char_start:s.span.char_end] == s.text``
holds for every sentence.  This is the foundational invariant — see CLAUDE.md §6.

Cross-page handling
-------------------
Docling exposes provenance as a list of (page_no, bbox) entries — one per page
the item touches.  We preserve all of them on the *block* (paragraph) span.
For sentences inside a single-page block we copy the block's PageBBox down.
For sentences inside a cross-page block we leave bboxes empty: the char offsets
are still correct (which is what citation tracking needs), but precise per-
sentence bounding boxes require splitting the wtpsplit output across pages,
which is a Phase-5 rendering concern.

External deps (lazy)
--------------------
Both ``docling`` and ``wtpsplit`` are optional extras.  Importing this module
does NOT import them; the imports happen inside ``parse()`` and the splitter's
``_load()``.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import BBox, PageBBox, Span
from verifiable_rag.parsers._cache import file_content_hash
from verifiable_rag.parsers._sentence_splitter import SentenceSplitter

# Separator written between blocks when assembling full_text.  Affects offsets
# but never overlaps with any block's reported span.
_BLOCK_SEPARATOR = "\n\n"


# --------------------------------------------------------------------------- #
# Internal block representation — decoupled from docling's own types so the
# downstream model-building logic is testable without docling installed.
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class _BBoxData:
    """Single page-bbox extracted from one provenance entry.  page_no is 1-indexed."""

    page_no: int
    l: float  # noqa: E741 — docling field name
    t: float
    r: float
    b: float


@dataclass(frozen=True)
class _RawBlock:
    """A docling content block flattened to (text, per-page bboxes, label)."""

    text: str
    bbox_list: tuple[_BBoxData, ...]  # sorted by page_no ascending
    label: str  # "paragraph" | "section_header"


# --------------------------------------------------------------------------- #
# Pure helpers — testable without docling
# --------------------------------------------------------------------------- #

def _make_doc_id(path: Path) -> str:
    """Stable, human-readable doc_id derived from the file's content."""
    h = file_content_hash(path)
    stem = "".join(c if c.isalnum() else "_" for c in path.stem[:20])
    return f"{stem}-{h[:8]}"


def _compute_page_breaks(page_starts: dict[int, int]) -> list[int]:
    """Convert {1-indexed page_no: char_offset} → 0-indexed page_breaks list.

    Invariants on output:
      - page_breaks[0] == 0
      - page_breaks is sorted non-decreasing
      - len(page_breaks) == max page_no observed (or 1 if none observed)
    """
    if not page_starts:
        return [0]

    starts = dict(page_starts)
    if 1 not in starts:
        starts[1] = 0

    max_page_no = max(starts)
    breaks: list[int] = []
    last_offset = 0
    for page_no in range(1, max_page_no + 1):
        if page_no in starts:
            last_offset = starts[page_no]
        breaks.append(last_offset)
    return breaks


def _assign_char_offsets(
    blocks: list[_RawBlock],
) -> tuple[str, list[int], list[int], list[int]]:
    """Concatenate block texts into full_text and record per-block offsets.

    Returns (full_text, page_breaks, block_starts, block_ends) where the
    block_*[i] offsets refer to positions in full_text *excluding* the trailing
    separator inserted between blocks.
    """
    parts: list[str] = []
    block_starts: list[int] = []
    block_ends: list[int] = []
    page_starts: dict[int, int] = {}
    cursor = 0

    for block in blocks:
        # Primary page = lowest-numbered page this block touches
        primary_page_no = block.bbox_list[0].page_no
        page_starts.setdefault(primary_page_no, cursor)

        # Cross-page blocks: also record the start offset for the OTHER pages.
        # The "start" of a cross-page block is the same offset for all pages it
        # contributes to — which is wrong for the secondary pages strictly, but
        # there's no way to know the exact split point inside the block text.
        # We only record secondary pages if no earlier block has set them.
        for bb in block.bbox_list[1:]:
            page_starts.setdefault(bb.page_no, cursor)

        block_start = cursor
        block_end = cursor + len(block.text)
        parts.append(block.text)
        parts.append(_BLOCK_SEPARATOR)
        cursor = block_end + len(_BLOCK_SEPARATOR)

        block_starts.append(block_start)
        block_ends.append(block_end)

    full_text = "".join(parts)
    page_breaks = _compute_page_breaks(page_starts)
    return full_text, page_breaks, block_starts, block_ends


def _block_pagebboxes(block: _RawBlock) -> tuple[PageBBox, ...]:
    """Convert a block's bbox_list into our PageBBox tuple (0-indexed pages)."""
    return tuple(
        PageBBox(
            page=bb.page_no - 1,
            bbox=BBox(x0=bb.l, y0=bb.t, x1=bb.r, y1=bb.b),
        )
        for bb in block.bbox_list  # already sorted ascending by page_no
    )


def _build_sections(
    blocks: list[_RawBlock],
    block_starts: list[int],
    block_ends: list[int],
    doc_id: str,
    splitter: SentenceSplitter,
) -> list[Section]:
    """Group blocks into Section/Paragraph/Sentence objects with doc-level spans."""
    sections: list[Section] = []
    current_title: str | None = None
    current_paras: list[Paragraph] = []
    current_section_start: int | None = None
    sec_idx = 0
    para_idx = 0
    global_sent_idx = 0

    def _flush_section(end_offset: int) -> None:
        nonlocal sec_idx, current_title, current_paras, current_section_start
        if not current_paras:
            return
        start = current_section_start if current_section_start is not None else 0
        # Use the actual paragraph end — more accurate than block boundary
        actual_end = max(end_offset, current_paras[-1].span.char_end)
        sections.append(
            Section(
                id=f"{doc_id}::sec{sec_idx}",
                title=current_title,
                paragraphs=current_paras,
                span=Span(doc_id=doc_id, char_start=start, char_end=actual_end),
            )
        )
        sec_idx += 1
        current_paras = []

    for block, b_start, _b_end in zip(blocks, block_starts, block_ends, strict=True):
        if block.label == "section_header":
            _flush_section(end_offset=b_start)
            current_title = block.text.strip() or None
            current_section_start = b_start
            continue

        # paragraph block
        sent_spans = splitter.split_with_offsets(block.text)
        if not sent_spans:
            continue

        if current_section_start is None:
            current_section_start = b_start

        block_bboxes = _block_pagebboxes(block)
        # If a block touches multiple pages we cannot precisely localise each
        # sentence inside it, so leave per-sentence bboxes empty.  Char offsets
        # remain correct, which is what the citation layer relies on.
        sentence_bboxes: tuple[PageBBox, ...] = (
            block_bboxes if len(block_bboxes) == 1 else ()
        )

        sentences: list[Sentence] = []
        for ss in sent_spans:
            doc_start = b_start + ss.start
            doc_end = b_start + ss.end
            sentences.append(
                Sentence(
                    id=f"{doc_id}::s{global_sent_idx}",
                    text=ss.text,
                    span=Span(
                        doc_id=doc_id,
                        char_start=doc_start,
                        char_end=doc_end,
                        bboxes=sentence_bboxes,
                    ),
                )
            )
            global_sent_idx += 1

        para_span = Span(
            doc_id=doc_id,
            char_start=sentences[0].span.char_start,
            char_end=sentences[-1].span.char_end,
            bboxes=block_bboxes,
        )
        current_paras.append(
            Paragraph(
                id=f"{doc_id}::para{para_idx}",
                sentences=sentences,
                span=para_span,
            )
        )
        para_idx += 1

    # Flush trailing section
    _flush_section(end_offset=block_ends[-1] if block_ends else 0)
    return sections


# --------------------------------------------------------------------------- #
# Docling-side extraction — isolates docling's API surface to a single function
# --------------------------------------------------------------------------- #

def _extract_raw_blocks(dl_doc: Any) -> list[_RawBlock]:
    """Walk a DoclingDocument in reading order, emit one _RawBlock per text item.

    Skips tables, pictures, and items without provenance.  Cross-page items
    contribute multiple bboxes (one per provenance entry).
    """
    try:
        from docling_core.types.doc import (
            SectionHeaderItem,
            TextItem,
        )
    except ImportError as exc:
        raise ImportError(
            "docling_core is required for DoclingParser. "
            "Install it with: pip install 'verifiable-rag[docling]'"
        ) from exc

    blocks: list[_RawBlock] = []
    for item, _level in dl_doc.iterate_items():
        if isinstance(item, SectionHeaderItem):
            label = "section_header"
        elif isinstance(item, TextItem):
            label = "paragraph"
        else:
            # Tables, pictures, lists with rich structure — skip for v0.5.
            continue

        text = getattr(item, "text", None)
        if not text or not text.strip():
            continue
        prov_entries = getattr(item, "prov", None) or []
        if not prov_entries:
            continue

        bbox_list: list[_BBoxData] = []
        for prov in prov_entries:
            bbox = getattr(prov, "bbox", None)
            page_no = getattr(prov, "page_no", None)
            if bbox is None or page_no is None:
                continue
            try:
                bbox_list.append(
                    _BBoxData(
                        page_no=int(page_no),
                        l=float(bbox.l),
                        t=float(bbox.t),
                        r=float(bbox.r),
                        b=float(bbox.b),
                    )
                )
            except (AttributeError, TypeError, ValueError):
                # Unexpected bbox shape — skip this provenance entry
                continue

        if not bbox_list:
            continue
        bbox_list.sort(key=lambda x: x.page_no)
        blocks.append(_RawBlock(text=text, bbox_list=tuple(bbox_list), label=label))

    return blocks


# --------------------------------------------------------------------------- #
# Public parser
# --------------------------------------------------------------------------- #

class DoclingParser:
    """Parses PDFs (and other docling-supported formats) into a Document.

    The parser is stateless across calls; expensive resources (the docling
    DocumentConverter, the wtpsplit model) are constructed lazily and reused.
    """

    def __init__(
        self,
        sentence_splitter: SentenceSplitter | None = None,
    ) -> None:
        self._splitter = sentence_splitter or SentenceSplitter()
        self._converter: Any = None

    def _get_converter(self) -> Any:
        if self._converter is None:
            try:
                from docling.document_converter import DocumentConverter
            except ImportError as exc:
                raise ImportError(
                    "docling is required for DoclingParser. "
                    "Install it with: pip install 'verifiable-rag[docling]'"
                ) from exc
            self._converter = DocumentConverter()
        return self._converter

    def parse(self, path: Path) -> Document:
        if not path.exists():
            raise FileNotFoundError(f"No file at {path}")

        converter = self._get_converter()
        result = converter.convert(str(path))
        dl_doc = result.document

        return self._build_document(dl_doc, path)

    def _build_document(self, dl_doc: Any, path: Path) -> Document:
        doc_id = _make_doc_id(path)
        raw_blocks = _extract_raw_blocks(dl_doc)
        if not raw_blocks:
            raise ValueError(
                f"DoclingParser produced no content from {path}. "
                "The file may be empty, image-only, or parsed without text."
            )

        full_text, page_breaks, block_starts, block_ends = _assign_char_offsets(
            raw_blocks
        )
        sections = _build_sections(
            raw_blocks, block_starts, block_ends, doc_id, self._splitter
        )

        if not sections:
            raise ValueError(
                f"DoclingParser extracted blocks but produced no sentences from {path}. "
                "Sentence segmentation may have failed."
            )

        return Document(
            doc_id=doc_id,
            source_path=path,
            sections=sections,
            page_breaks=page_breaks,
            full_text=full_text,
        )
