"""PyMuPDFParser: PDF → span-tracked Document, lenient Docling fallback.

PyMuPDF (a.k.a. ``pymupdf`` / ``fitz``) is far more permissive than Docling
for layout-quirky PDFs — multi-column papers, footnotes, sidebars — that
trigger Docling's internal assertions. We use it as the second link in a
``CompositeParser`` chain so those PDFs still produce a usable Document
instead of being dropped from the eval.

What you get vs DoclingParser
-----------------------------
* Every Sentence still carries (doc_id, char_start, char_end, bboxes) — the
  citation invariant in CLAUDE.md §6 is preserved.
* Section hierarchy is flat: one Section per document (title=None). PyMuPDF
  doesn't surface heading semantics; reconstructing them heuristically is
  out of scope for the fallback path.
* Block ordering follows PyMuPDF's reading order. Multi-column layouts can
  interleave — bboxes remain correct but the prose flow may not match the
  rendered reading order.

External deps (lazy)
--------------------
``pymupdf`` is an optional extra; the import happens inside ``parse()``.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import BBox, PageBBox, Span
from verifiable_rag.parsers._cache import file_content_hash
from verifiable_rag.parsers._sentence_splitter import SentenceSplitter

_BLOCK_SEPARATOR = "\n\n"


def _make_doc_id(path: Path) -> str:
    h = file_content_hash(path)
    stem = "".join(c if c.isalnum() else "_" for c in path.stem[:20])
    return f"{stem}-{h[:8]}"


@dataclass(frozen=True)
class _RawBlock:
    """One PyMuPDF text block, normalised to (text, page, bbox)."""

    text: str
    page: int  # 0-indexed
    bbox: tuple[float, float, float, float]  # (x0, y0, x1, y1) in PDF space


def _extract_blocks(pdf_doc: Any) -> list[_RawBlock]:
    """Walk pages in order, return one _RawBlock per non-empty text block.

    Uses ``page.get_text("dict")`` so we get per-block bboxes; image blocks
    (type==1) are skipped.
    """
    blocks: list[_RawBlock] = []
    for page_idx in range(pdf_doc.page_count):
        page = pdf_doc.load_page(page_idx)
        page_dict = page.get_text("dict")
        for block in page_dict.get("blocks", []):
            if block.get("type", 0) != 0:
                continue
            line_texts: list[str] = []
            for line in block.get("lines", []):
                span_texts = [s.get("text", "") for s in line.get("spans", [])]
                line_texts.append("".join(span_texts))
            text = "\n".join(line_texts).strip()
            if not text:
                continue
            bbox = block.get("bbox")
            if bbox is None or len(bbox) != 4:
                continue
            blocks.append(
                _RawBlock(
                    text=text,
                    page=page_idx,
                    bbox=(float(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3])),
                )
            )
    return blocks


def _assign_char_offsets(
    blocks: list[_RawBlock],
) -> tuple[str, list[int], list[int], list[int]]:
    """Concatenate block texts; return (full_text, page_breaks, block_starts, block_ends).

    page_breaks invariants match DoclingParser: starts at 0, sorted ascending,
    length == max page index + 1.
    """
    parts: list[str] = []
    block_starts: list[int] = []
    block_ends: list[int] = []
    page_starts: dict[int, int] = {}
    cursor = 0

    for block in blocks:
        page_starts.setdefault(block.page, cursor)
        block_start = cursor
        block_end = cursor + len(block.text)
        parts.append(block.text)
        parts.append(_BLOCK_SEPARATOR)
        cursor = block_end + len(_BLOCK_SEPARATOR)
        block_starts.append(block_start)
        block_ends.append(block_end)

    full_text = "".join(parts)

    if not page_starts:
        return full_text, [0], block_starts, block_ends

    # Page 0 must start at offset 0 — if the first block was on a higher page,
    # we still need page 0 to exist.
    page_starts.setdefault(0, 0)
    max_page = max(page_starts)
    page_breaks: list[int] = []
    last = 0
    for p in range(max_page + 1):
        if p in page_starts:
            last = page_starts[p]
        page_breaks.append(last)
    return full_text, page_breaks, block_starts, block_ends


class PyMuPDFParser:
    """PyMuPDF-backed parser, used as a Docling fallback.

    Stateless across calls; the wtpsplit splitter is reused.
    """

    def __init__(self, sentence_splitter: SentenceSplitter | None = None) -> None:
        self._splitter = sentence_splitter or SentenceSplitter()

    def parse(self, path: Path) -> Document:
        if not path.exists():
            raise FileNotFoundError(f"No file at {path}")
        try:
            import pymupdf
        except ImportError as exc:
            raise ImportError(
                "pymupdf is required for PyMuPDFParser. "
                "Install with: pip install 'verifiable-rag[pymupdf]'"
            ) from exc

        pdf_doc: Any = pymupdf.open(str(path))  # type: ignore[no-untyped-call]
        try:
            return self._build_document(pdf_doc, path)
        finally:
            pdf_doc.close()

    def _build_document(self, pdf_doc: Any, path: Path) -> Document:
        doc_id = _make_doc_id(path)
        raw_blocks = _extract_blocks(pdf_doc)
        if not raw_blocks:
            raise ValueError(
                f"PyMuPDFParser produced no content from {path}. "
                "The file may be empty, image-only, or have no extractable text."
            )

        full_text, page_breaks, block_starts, _block_ends = _assign_char_offsets(raw_blocks)

        paragraphs: list[Paragraph] = []
        para_idx = 0
        sent_idx_global = 0
        for block, b_start in zip(raw_blocks, block_starts, strict=True):
            sent_spans = self._splitter.split_with_offsets(block.text)
            if not sent_spans:
                continue
            block_pbbox = PageBBox(
                page=block.page,
                bbox=BBox(x0=block.bbox[0], y0=block.bbox[1], x1=block.bbox[2], y1=block.bbox[3]),
            )
            sentences: list[Sentence] = []
            for ss in sent_spans:
                sentences.append(
                    Sentence(
                        id=f"{doc_id}::s{sent_idx_global}",
                        text=ss.text,
                        span=Span(
                            doc_id=doc_id,
                            char_start=b_start + ss.start,
                            char_end=b_start + ss.end,
                            bboxes=(block_pbbox,),
                        ),
                    )
                )
                sent_idx_global += 1

            para_span = Span(
                doc_id=doc_id,
                char_start=sentences[0].span.char_start,
                char_end=sentences[-1].span.char_end,
                bboxes=(block_pbbox,),
            )
            paragraphs.append(
                Paragraph(
                    id=f"{doc_id}::para{para_idx}",
                    sentences=sentences,
                    span=para_span,
                )
            )
            para_idx += 1

        if not paragraphs:
            raise ValueError(
                f"PyMuPDFParser extracted blocks but produced no sentences from {path}. "
                "Sentence segmentation may have failed."
            )

        section = Section(
            id=f"{doc_id}::sec0",
            title=None,
            paragraphs=paragraphs,
            span=Span(
                doc_id=doc_id,
                char_start=paragraphs[0].span.char_start,
                char_end=paragraphs[-1].span.char_end,
            ),
        )
        return Document(
            doc_id=doc_id,
            source_path=path,
            sections=[section],
            page_breaks=page_breaks,
            full_text=full_text,
            parser_name="pymupdf",
        )
