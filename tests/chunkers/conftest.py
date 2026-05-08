"""Chunker-test helpers.

The most important thing here is ``assert_chunk_invariants`` — every chunker
test calls this to enforce:
  - Every sentence in the document appears in exactly one chunk.
  - Every chunk's span bounds its sentences and is doc-id-consistent.
  - Sentence IDs round-trip cleanly between document and chunks.

If any of these fail, retrieval may surface chunks whose citations don't map
back to the source — which silently corrupts the verifiable-RAG contract.
"""

from __future__ import annotations

from pathlib import Path

from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import BBox, PageBBox, Span


def assert_chunk_invariants(document: Document, chunks: list[Chunk]) -> None:
    """Enforce every cross-cutting guarantee chunkers must satisfy."""
    doc_sent_ids = [s.id for s in document.sentences]

    # ---- coverage: every sentence appears in exactly one chunk -----------
    seen: list[str] = []
    for ch in chunks:
        seen.extend(ch.sentence_ids)
    assert seen == doc_sent_ids, (
        "Chunk coverage mismatch:\n"
        f"  doc has {len(doc_sent_ids)} sentence(s) in order\n"
        f"  chunks list {len(seen)} sentence_id(s) in order\n"
        f"  doc_ids[:10] = {doc_sent_ids[:10]}\n"
        f"  chunk_ids[:10] = {seen[:10]}"
    )

    # ---- per-chunk structural invariants ---------------------------------
    sent_lookup = {s.id: s for s in document.sentences}
    for ch in chunks:
        assert ch.doc_id == document.doc_id, (
            f"Chunk {ch.chunk_id!r} doc_id {ch.doc_id!r} != document {document.doc_id!r}"
        )
        assert ch.span.doc_id == document.doc_id, (
            f"Chunk {ch.chunk_id!r} span.doc_id mismatch: {ch.span.doc_id!r}"
        )
        assert ch.sentence_ids, f"Chunk {ch.chunk_id!r} has no sentence_ids"

        chunk_sents = [sent_lookup[sid] for sid in ch.sentence_ids]
        # Bounding span covers contained sentences
        assert ch.span.char_start <= min(s.span.char_start for s in chunk_sents), (
            f"Chunk {ch.chunk_id!r} span starts after its first sentence"
        )
        assert ch.span.char_end >= max(s.span.char_end for s in chunk_sents), (
            f"Chunk {ch.chunk_id!r} span ends before its last sentence"
        )
        # Required parent-pointer metadata
        assert "section_id" in ch.metadata, f"Chunk {ch.chunk_id!r} missing 'section_id' metadata"
        assert "paragraph_id" in ch.metadata, (
            f"Chunk {ch.chunk_id!r} missing 'paragraph_id' metadata"
        )
        # Page lookup is consistent
        first, last = document.pages_for_span(ch.span)
        assert ch.metadata["page_first"] == first, (
            f"Chunk {ch.chunk_id!r} metadata page_first mismatch"
        )
        assert ch.metadata["page_last"] == last, (
            f"Chunk {ch.chunk_id!r} metadata page_last mismatch"
        )


# --------------------------------------------------------------------------- #
# Synthetic Document builder — avoids needing docling for chunker tests.
# --------------------------------------------------------------------------- #


def build_document(
    sections_spec: list[tuple[str | None, list[list[str]]]],
    *,
    doc_id: str = "doctest",
    page_breaks: list[int] | None = None,
) -> Document:
    """Build a Document from a structural spec.

    sections_spec: list of (section_title, list_of_paragraphs) where each
    paragraph is a list of sentence strings.

    Char offsets are assigned by walking the spec, joining sentences with " "
    inside a paragraph and "\\n\\n" between paragraphs/sections.  Bboxes are
    fabricated as a single PageBBox per paragraph on page 0.
    """
    sections: list[Section] = []
    cursor = 0
    full_parts: list[str] = []
    sent_idx = 0
    para_idx = 0

    for sec_idx, (title, paras) in enumerate(sections_spec):
        sec_start = cursor
        paragraphs: list[Paragraph] = []
        for sentences_text in paras:
            para_sents: list[Sentence] = []
            para_start = cursor
            for j, st in enumerate(sentences_text):
                start = cursor
                end = start + len(st)
                full_parts.append(st)
                bb = PageBBox(page=0, bbox=BBox(0.0, float(j), 100.0, float(j) + 10.0))
                sent = Sentence(
                    id=f"{doc_id}::s{sent_idx}",
                    text=st,
                    span=Span(
                        doc_id=doc_id,
                        char_start=start,
                        char_end=end,
                        bboxes=(bb,),
                    ),
                )
                para_sents.append(sent)
                sent_idx += 1
                cursor = end
                # join with " " between sentences in the same paragraph
                if j < len(sentences_text) - 1:
                    full_parts.append(" ")
                    cursor += 1
            para_span = Span(
                doc_id=doc_id,
                char_start=para_start,
                char_end=cursor,
                bboxes=tuple(s.span.bboxes[0] for s in para_sents),
            )
            paragraphs.append(
                Paragraph(
                    id=f"{doc_id}::para{para_idx}",
                    sentences=para_sents,
                    span=para_span,
                )
            )
            para_idx += 1
            # paragraph separator
            full_parts.append("\n\n")
            cursor += 2
        sec_span = Span(
            doc_id=doc_id,
            char_start=sec_start,
            char_end=cursor,
        )
        sections.append(
            Section(
                id=f"{doc_id}::sec{sec_idx}",
                title=title,
                paragraphs=paragraphs,
                span=sec_span,
            )
        )

    return Document(
        doc_id=doc_id,
        source_path=Path(f"/synthetic/{doc_id}.txt"),
        sections=sections,
        page_breaks=page_breaks or [0],
        full_text="".join(full_parts),
    )
