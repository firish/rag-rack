"""JSON (de)serialization for Document and friends.

Versioned via _SERDE_VERSION.  Bump the version whenever the on-disk shape
changes — old caches with a mismatched version are treated as cache misses.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import BBox, PageBBox, Span

# Bump this whenever the wire format or any model dataclass changes shape.
_SERDE_VERSION = 1


def document_to_dict(doc: Document) -> dict[str, Any]:
    return {
        "_serde_version": _SERDE_VERSION,
        "doc_id": doc.doc_id,
        "source_path": str(doc.source_path),
        "page_breaks": list(doc.page_breaks),
        "full_text": doc.full_text,
        "metadata": doc.metadata,
        "sections": [_section_to_dict(s) for s in doc.sections],
        "parser_name": doc.parser_name,
    }


def document_from_dict(d: dict[str, Any]) -> Document:
    version = d.get("_serde_version")
    if version != _SERDE_VERSION:
        raise ValueError(
            f"Cache version mismatch: expected {_SERDE_VERSION}, got {version!r}"
        )
    return Document(
        doc_id=d["doc_id"],
        source_path=Path(d["source_path"]),
        sections=[_section_from_dict(s) for s in d["sections"]],
        page_breaks=list(d.get("page_breaks", [])),
        full_text=d.get("full_text"),
        metadata=dict(d.get("metadata", {})),
        # Optional field — caches written before this existed return None,
        # which is the right "unknown provenance" sentinel.
        parser_name=d.get("parser_name"),
    )


def save_document(doc: Document, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = document_to_dict(doc)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))


def load_document(path: Path) -> Document:
    with path.open("r", encoding="utf-8") as f:
        return document_from_dict(json.load(f))


# --------------------------------------------------------------------------- #
# Internal helpers
# --------------------------------------------------------------------------- #

def _bbox_to_dict(bbox: BBox) -> dict[str, float]:
    return {"x0": bbox.x0, "y0": bbox.y0, "x1": bbox.x1, "y1": bbox.y1}


def _bbox_from_dict(d: dict[str, Any]) -> BBox:
    return BBox(x0=d["x0"], y0=d["y0"], x1=d["x1"], y1=d["y1"])


def _pagebbox_to_dict(pb: PageBBox) -> dict[str, Any]:
    return {"page": pb.page, "bbox": _bbox_to_dict(pb.bbox)}


def _pagebbox_from_dict(d: dict[str, Any]) -> PageBBox:
    return PageBBox(page=d["page"], bbox=_bbox_from_dict(d["bbox"]))


def _span_to_dict(span: Span) -> dict[str, Any]:
    return {
        "doc_id": span.doc_id,
        "char_start": span.char_start,
        "char_end": span.char_end,
        "bboxes": [_pagebbox_to_dict(pb) for pb in span.bboxes],
    }


def _span_from_dict(d: dict[str, Any]) -> Span:
    return Span(
        doc_id=d["doc_id"],
        char_start=d["char_start"],
        char_end=d["char_end"],
        bboxes=tuple(_pagebbox_from_dict(pb) for pb in d.get("bboxes", [])),
    )


def _sentence_to_dict(s: Sentence) -> dict[str, Any]:
    return {"id": s.id, "text": s.text, "span": _span_to_dict(s.span)}


def _sentence_from_dict(d: dict[str, Any]) -> Sentence:
    return Sentence(id=d["id"], text=d["text"], span=_span_from_dict(d["span"]))


def _paragraph_to_dict(p: Paragraph) -> dict[str, Any]:
    return {
        "id": p.id,
        "span": _span_to_dict(p.span),
        "sentences": [_sentence_to_dict(s) for s in p.sentences],
    }


def _paragraph_from_dict(d: dict[str, Any]) -> Paragraph:
    return Paragraph(
        id=d["id"],
        span=_span_from_dict(d["span"]),
        sentences=[_sentence_from_dict(s) for s in d["sentences"]],
    )


def _section_to_dict(s: Section) -> dict[str, Any]:
    return {
        "id": s.id,
        "title": s.title,
        "span": _span_to_dict(s.span),
        "paragraphs": [_paragraph_to_dict(p) for p in s.paragraphs],
    }


def _section_from_dict(d: dict[str, Any]) -> Section:
    return Section(
        id=d["id"],
        title=d.get("title"),
        span=_span_from_dict(d["span"]),
        paragraphs=[_paragraph_from_dict(p) for p in d["paragraphs"]],
    )
