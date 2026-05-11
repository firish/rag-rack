"""ParentChildChunker: paragraph-level child chunks with section-pointer metadata.

Given a parsed Document, produces chunks that:
  * carry every contained sentence_id (so downstream retrieval still produces
    sentence-precise citations — citation granularity is decoupled from chunk
    granularity, CLAUDE.md §6),
  * fall within a token range bounded by ``[min_child_tokens, max_child_tokens]``
    where possible.

Parent context is NOT stored on chunks.  Each chunk carries
``metadata["section_id"]`` (and the new ``paragraph_ids`` tuple) so the generator
can call ``ParentExpander`` to compute the LLM context at retrieval time.

Sizing
------
- ``max_child_tokens`` (default 400): ceiling. Paragraphs above this are split
  greedily at sentence boundaries; an oversized single sentence is emitted alone.
- ``min_child_tokens`` (default 0): floor. When > 0, consecutive small paragraphs
  *within the same section* are merged until the chunk reaches the floor or
  adding the next group would exceed the ceiling. ``0`` preserves the legacy
  one-chunk-per-paragraph behavior.
- Sections are hard boundaries — chunks never span sections.

Token counting
--------------
A ``token_count`` callable is injected (default: ``len(text) // 4``, the
standard English approximation).  Plug in tiktoken or a model-specific
tokenizer when you need exact budgets.
"""

from __future__ import annotations

from collections.abc import Callable

from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import Span


def _default_token_count(text: str) -> int:
    """1 token ≈ 4 chars (English).  Coarse but stable."""
    return max(1, len(text) // 4)


# Internal: a (paragraph, sentences) pair representing one candidate chunk
# slot before cross-paragraph merging.
_GroupedSlot = tuple[Paragraph, tuple[Sentence, ...]]

# A merged slot — may include sentences from multiple paragraphs.
_MergedSlot = tuple[tuple[Paragraph, ...], tuple[Sentence, ...]]


class ParentChildChunker:
    """Paragraph-level chunker that preserves sentence_ids and section pointers.

    Output chunks satisfy:
      - ``chunk.sentence_ids`` lists every Sentence inside the chunk in order.
      - ``chunk.span`` is the bounding span over those sentences (bboxes merged).
      - ``chunk.metadata`` includes ``section_id``, ``section_title``,
        ``paragraph_id`` (first paragraph touched, for backward compat),
        ``paragraph_ids`` (tuple of all paragraph IDs touched),
        ``paragraph_part``, ``paragraph_part_count``,
        ``page_first``, ``page_last``.
    """

    def __init__(
        self,
        max_child_tokens: int = 400,
        min_child_tokens: int = 0,
        token_count: Callable[[str], int] = _default_token_count,
    ) -> None:
        if max_child_tokens <= 0:
            raise ValueError(f"max_child_tokens must be > 0, got {max_child_tokens}")
        if min_child_tokens < 0:
            raise ValueError(f"min_child_tokens must be >= 0, got {min_child_tokens}")
        if min_child_tokens > max_child_tokens:
            raise ValueError(
                f"min_child_tokens ({min_child_tokens}) cannot exceed "
                f"max_child_tokens ({max_child_tokens})"
            )
        self._max = max_child_tokens
        self._min = min_child_tokens
        self._tok = token_count

    def chunk(self, document: Document) -> list[Chunk]:
        chunks: list[Chunk] = []
        chunk_idx = 0
        for section in document.sections:
            # 1) Existing per-paragraph grouping (splits oversized paragraphs).
            section_groups: list[_GroupedSlot] = []
            for paragraph in section.paragraphs:
                for sents in self._group_sentences(paragraph):
                    section_groups.append((paragraph, sents))

            # 2) Cross-paragraph merging (no-op when min_child_tokens == 0).
            merged = self._merge_under_floor(section_groups)

            # 3) Build a chunk per merged slot.
            for paragraphs, sentences in merged:
                chunks.append(
                    self._build_chunk(
                        chunk_idx=chunk_idx,
                        section=section,
                        paragraphs=paragraphs,
                        sentences=sentences,
                        document=document,
                    )
                )
                chunk_idx += 1
        return chunks

    # --------------------------------------------------------------------- #
    # Internals
    # --------------------------------------------------------------------- #

    def _group_sentences(self, paragraph: Paragraph) -> list[tuple[Sentence, ...]]:
        """Pack paragraph sentences into groups <= max_child_tokens.

        Greedy: start a new group when adding the next sentence would push
        the current group over the cap.  A single sentence above the cap is
        emitted alone — sentences are atomic.
        """
        if self._tok(paragraph.text) <= self._max:
            return [tuple(paragraph.sentences)]

        groups: list[tuple[Sentence, ...]] = []
        current: list[Sentence] = []
        current_tokens = 0

        for sent in paragraph.sentences:
            sent_tokens = self._tok(sent.text)
            if current and current_tokens + sent_tokens > self._max:
                groups.append(tuple(current))
                current = [sent]
                current_tokens = sent_tokens
            else:
                current.append(sent)
                current_tokens += sent_tokens

        if current:
            groups.append(tuple(current))
        return groups

    def _merge_under_floor(self, groups: list[_GroupedSlot]) -> list[_MergedSlot]:
        """Merge consecutive groups within a section until the floor is met.

        Algorithm:
          * Walk groups left-to-right, accumulating into a pending buffer.
          * Flush pending when adding the next group would exceed ``max``.
          * Otherwise keep accumulating — the buffer naturally grows toward
            the ceiling. When ``min == 0`` this is a no-op identity transform.
          * Trailing pending is always flushed (even if under floor — better
            than dropping data).
        """
        if self._min <= 0 or not groups:
            return [((para,), sents) for para, sents in groups]

        out: list[_MergedSlot] = []
        pending_paragraphs: list[Paragraph] = []
        pending_seen_para_ids: set[str] = set()
        pending_sentences: list[Sentence] = []
        pending_tokens = 0

        def flush() -> None:
            nonlocal pending_tokens
            if pending_sentences:
                out.append((tuple(pending_paragraphs), tuple(pending_sentences)))
            pending_paragraphs.clear()
            pending_seen_para_ids.clear()
            pending_sentences.clear()
            pending_tokens = 0

        for paragraph, sents in groups:
            sent_tokens = sum(self._tok(s.text) for s in sents)

            # If adding this group would overflow the ceiling, flush first.
            if pending_sentences and pending_tokens + sent_tokens > self._max:
                flush()

            if paragraph.id not in pending_seen_para_ids:
                pending_paragraphs.append(paragraph)
                pending_seen_para_ids.add(paragraph.id)
            pending_sentences.extend(sents)
            pending_tokens += sent_tokens

        flush()
        return out

    def _build_chunk(
        self,
        *,
        chunk_idx: int,
        section: Section,
        paragraphs: tuple[Paragraph, ...],
        sentences: tuple[Sentence, ...],
        document: Document,
    ) -> Chunk:
        text = " ".join(s.text for s in sentences)
        # Bounding span: char range covers the first/last sentence; bboxes
        # are union-ed across all contained sentences via Span.merge.
        span = Span.merge([s.span for s in sentences])
        page_first, page_last = document.pages_for_span(span)

        # paragraph_part / paragraph_part_count are only meaningful when this
        # chunk is a strict subset of one paragraph.  Compute them only in
        # that case; multi-paragraph chunks get the trivial (0, 1).
        if len(paragraphs) == 1:
            sole_paragraph = paragraphs[0]
            full_groups = self._group_sentences(sole_paragraph)
            paragraph_part_count = len(full_groups)
            try:
                paragraph_part = full_groups.index(sentences)
            except ValueError:
                # Sentences weren't a single original group (e.g. a merged
                # subset that happened to fall under one paragraph). Treat
                # as a single-part chunk.
                paragraph_part = 0
                paragraph_part_count = 1
        else:
            paragraph_part = 0
            paragraph_part_count = 1

        return Chunk(
            chunk_id=f"{document.doc_id}::ch{chunk_idx}",
            text=text,
            doc_id=document.doc_id,
            sentence_ids=tuple(s.id for s in sentences),
            span=span,
            metadata={
                "section_id": section.id,
                "section_title": section.title,
                "paragraph_id": paragraphs[0].id,
                "paragraph_ids": tuple(p.id for p in paragraphs),
                "paragraph_part": paragraph_part,
                "paragraph_part_count": paragraph_part_count,
                "page_first": page_first,
                "page_last": page_last,
            },
        )
