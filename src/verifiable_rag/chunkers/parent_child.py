"""ParentChildChunker: paragraph-level child chunks with section-pointer metadata.

Given a parsed Document, produces one Chunk per paragraph (splitting at sentence
boundaries when a paragraph exceeds ``max_child_tokens``).  Every chunk carries
the sentence_ids of the sentences it contains, so retrieved chunks always map
back to sentence-precise citations downstream — citation granularity is decoupled
from chunk granularity (CLAUDE.md §6).

Parent context is NOT stored on chunks.  Each chunk carries
``metadata["section_id"]`` and ``metadata["paragraph_id"]`` pointers; the
generator calls ``ParentExpander`` to compute the LLM context at retrieval time.
This avoids duplicating large section text into every child.

Sizing
------
- max_child_tokens (default 400): paragraphs above this are split greedily at
  sentence boundaries.
- A single sentence above the cap is emitted as its own oversize chunk;
  sentences are atomic and never split.

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


class ParentChildChunker:
    """Paragraph-level chunker that preserves sentence_ids and section pointers.

    Output chunks satisfy:
      - ``chunk.sentence_ids`` lists every Sentence inside the chunk in order.
      - ``chunk.span`` is the bounding span over those sentences (bboxes merged).
      - ``chunk.metadata`` includes ``section_id``, ``paragraph_id``,
        ``paragraph_part``, ``paragraph_part_count``, ``section_title``,
        ``page_first``, ``page_last``.
    """

    def __init__(
        self,
        max_child_tokens: int = 400,
        token_count: Callable[[str], int] = _default_token_count,
    ) -> None:
        if max_child_tokens <= 0:
            raise ValueError(f"max_child_tokens must be > 0, got {max_child_tokens}")
        self._max = max_child_tokens
        self._tok = token_count

    def chunk(self, document: Document) -> list[Chunk]:
        chunks: list[Chunk] = []
        chunk_idx = 0
        for section in document.sections:
            for paragraph in section.paragraphs:
                groups = self._group_sentences(paragraph)
                for grp_idx, sents in enumerate(groups):
                    chunks.append(
                        self._build_chunk(
                            chunk_idx=chunk_idx,
                            section=section,
                            paragraph=paragraph,
                            sentences=sents,
                            paragraph_part=grp_idx,
                            paragraph_part_count=len(groups),
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

    def _build_chunk(
        self,
        *,
        chunk_idx: int,
        section: Section,
        paragraph: Paragraph,
        sentences: tuple[Sentence, ...],
        paragraph_part: int,
        paragraph_part_count: int,
        document: Document,
    ) -> Chunk:
        text = " ".join(s.text for s in sentences)
        # Bounding span: char range covers the first/last sentence; bboxes
        # are union-ed across all contained sentences via Span.merge.
        span = Span.merge([s.span for s in sentences])
        page_first, page_last = document.pages_for_span(span)

        return Chunk(
            chunk_id=f"{document.doc_id}::ch{chunk_idx}",
            text=text,
            doc_id=document.doc_id,
            sentence_ids=tuple(s.id for s in sentences),
            span=span,
            metadata={
                "section_id": section.id,
                "section_title": section.title,
                "paragraph_id": paragraph.id,
                "paragraph_part": paragraph_part,
                "paragraph_part_count": paragraph_part_count,
                "page_first": page_first,
                "page_last": page_last,
            },
        )
