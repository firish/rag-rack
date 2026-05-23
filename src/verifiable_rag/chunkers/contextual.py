"""Contextual Retrieval (Anthropic 2024) — chunker wrapper that adds an
LLM-generated context preamble to each chunk before embedding.

For each chunk produced by a base chunker, ``LLMContextualizer`` sends
the *full document* plus the *chunk text* to a chat LLM and asks for a
short (50-100 token) preamble describing what the chunk is about within
the larger document. The preamble is stored in
``chunk.metadata["contextual_preamble"]``; the original ``chunk.text``
and ``chunk.span`` are unchanged (span preservation invariant).

The pipeline's embed step then concatenates the preamble before the
chunk text when present:

    embed_text = f"{preamble}\\n\\n{chunk.text}" if preamble else chunk.text

This is purely an embedding-time transformation — citations, span lookup,
and reranking all continue to use the original ``chunk.text``.

Reference: https://www.anthropic.com/news/contextual-retrieval

Cost
----
One LLM call per chunk, with the document portion cacheable. Within a
single document's batch of chunks, Anthropic prompt caching reduces the
document portion's cost by ~90 % after the first call. For a 30-chunk
paper with Haiku + caching: ~$0.10 per document.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Literal

from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.document import Document

Granularity = Literal["section", "paragraph", "chunk"]
_GRANULARITIES = frozenset({"section", "paragraph", "chunk"})

logger = logging.getLogger(__name__)


_DEFAULT_SYSTEM = (
    "You add brief, retrieval-focused context to passages from a document.\n"
    "\n"
    "Given a document and a passage extracted from it, write a 50-100 token "
    "preamble that (1) names what topic the passage covers, (2) locates it "
    "within the document's broader argument, and (3) uses terms a search "
    "query might plausibly use.\n"
    "\n"
    "Reply with ONLY the preamble text — no preface, no quotes, no "
    "explanation, no bullet points. Just the preamble."
)

_USER_TEMPLATE = (
    "<document>\n{document_text}\n</document>\n"
    "\n"
    "<passage>\n{chunk_text}\n</passage>\n"
    "\n"
    "Write the 50-100 token retrieval preamble for this passage."
)


class LLMContextualizer:
    """Generate a per-chunk contextual preamble via a chat LLM.

    Parameters
    ----------
    model:
        LiteLLM model identifier. Default ``"claude-haiku-4-5-20251001"``
        — cheap, fast, and prompt-cacheable for the long document portion.
    temperature:
        Sampling temperature. Default ``0.0`` for deterministic preambles
        (matters if you cache embeddings across re-ingests).
    max_tokens:
        Cap on preamble length. Default ``160`` leaves headroom for the
        50-100 token target.
    max_workers:
        Threadpool concurrency for contextualizing many chunks of one
        document in parallel. Anthropic Tier 2 → 8 is safe.
    num_retries:
        LiteLLM built-in retries for transient errors.
    system_prompt, user_template:
        Override the default prompts. ``user_template`` must contain
        ``{document_text}`` and ``{chunk_text}`` placeholders.
    """

    def __init__(
        self,
        model: str = "claude-haiku-4-5-20251001",
        temperature: float = 0.0,
        max_tokens: int = 160,
        max_workers: int = 8,
        num_retries: int = 2,
        system_prompt: str = _DEFAULT_SYSTEM,
        user_template: str = _USER_TEMPLATE,
    ) -> None:
        if "{document_text}" not in user_template or "{chunk_text}" not in user_template:
            raise ValueError(
                "user_template must contain both {document_text} and {chunk_text}"
            )
        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._max_workers = max_workers
        self._num_retries = num_retries
        self._system_prompt = system_prompt
        self._user_template = user_template

    def generate_batch(
        self,
        document_text: str,
        chunk_texts: list[str],
    ) -> list[str | None]:
        """Return one preamble per chunk_text, in order. ``None`` on failure.

        All calls share the same ``document_text``, so Anthropic prompt
        caching applies — the first call writes the cache, subsequent
        calls read it at ~10 % cost.
        """
        if not chunk_texts:
            return []

        if self._max_workers > 1 and len(chunk_texts) > 1:
            with ThreadPoolExecutor(max_workers=self._max_workers) as pool:
                return list(
                    pool.map(
                        lambda ct: self._generate_one(document_text, ct),
                        chunk_texts,
                    )
                )
        return [self._generate_one(document_text, ct) for ct in chunk_texts]

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _generate_one(self, document_text: str, chunk_text: str) -> str | None:
        user_msg = self._user_template.format(
            document_text=document_text, chunk_text=chunk_text
        )
        try:
            return self._call_llm(user_msg)
        except Exception as exc:  # noqa: BLE001 — one bad call shouldn't tank ingest
            logger.warning(
                "LLMContextualizer call failed: %s: %s", type(exc).__name__, exc
            )
            return None

    def _call_llm(self, user_msg: str) -> str:
        try:
            import litellm
        except ImportError as exc:
            raise ImportError(
                "litellm is required for LLMContextualizer. "
                "Install with: pip install 'verifiable-rag[litellm]'"
            ) from exc
        # Cache breakpoints: system prompt + the document portion of the user
        # message. Within one document's batch, the document is identical
        # across all calls → cache hit on chunks 2+ in the batch.
        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": self._system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": _split_document_block(user_msg),
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "type": "text",
                        "text": _split_chunk_block(user_msg),
                    },
                ],
            },
        ]
        response = litellm.completion(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
            num_retries=self._num_retries,
        )
        return str(response.choices[0].message.content or "").strip()


def _split_document_block(user_msg: str) -> str:
    """Return the prefix of user_msg up through the closing </document> tag.

    This is what gets cached. The portion *after* </document> (the chunk
    text + the instruction) is the uncached suffix.
    """
    marker = "</document>"
    idx = user_msg.find(marker)
    if idx == -1:
        # Custom template without our marker — cache the whole user message.
        return user_msg
    return user_msg[: idx + len(marker)]


def _split_chunk_block(user_msg: str) -> str:
    marker = "</document>"
    idx = user_msg.find(marker)
    if idx == -1:
        return ""
    return user_msg[idx + len(marker) :].lstrip("\n")


# --------------------------------------------------------------------------- #
# ContextualChunker — the Chunker-protocol-conformant wrapper
# --------------------------------------------------------------------------- #


class ContextualChunker:
    """Wrap a base :class:`Chunker` and add contextual preambles to chunks.

    Chunks sharing the same *group key* (section, paragraph, or
    individual chunk — controlled by ``granularity``) receive the same
    preamble. One LLM call per unique group, not per chunk — the same
    preamble is mapped onto every child chunk under it.

    Parameters
    ----------
    base:
        Any object satisfying the :class:`Chunker` protocol. Typically
        :class:`ParentChildChunker`.
    contextualizer:
        Object exposing ``generate_batch(document_text, passage_texts)``.
        Defaults to :class:`LLMContextualizer` with Haiku 4.5.
    granularity:
        Choose how many LLM calls per document — cost vs specificity tradeoff:

        - ``"section"`` (default): one preamble per Section, shared across
          every chunk under it. Typically 10-20 calls per academic paper.
          Right for structured docs (papers, books, technical docs).
        - ``"paragraph"``: one preamble per Paragraph. Typically 30-100 calls.
          Right for mixed-topic docs or very long sections.
        - ``"chunk"``: one preamble per child Chunk (Anthropic's original
          recipe). Typically 100-500 calls. Max specificity, max cost.

        Requires the base chunker to set ``metadata["section_id"]`` or
        ``metadata["paragraph_id"]`` accordingly. :class:`ParentChildChunker`
        sets both.
    group_by:
        Power-user override — a callable mapping a Chunk to a group key.
        When set, supersedes ``granularity``. Chunks returning the same
        key share a preamble; chunks where the callable returns ``None``
        get no preamble. Use this for non-standard document structures
        (chat logs, code, custom topic clusters).
    keep_on_failure:
        If True (default), chunks whose contextualization failed are kept
        with no preamble (they embed as their original text). If False,
        the failed chunks are dropped from the returned list.
        Default True — partial degradation beats total ingest failure.
    """

    def __init__(
        self,
        base,  # type: ignore[no-untyped-def] — Chunker (Protocol from sibling module)
        contextualizer: LLMContextualizer | None = None,
        granularity: Granularity = "section",
        group_by: Callable[[Chunk], str | None] | None = None,
        keep_on_failure: bool = True,
    ) -> None:
        if granularity not in _GRANULARITIES:
            raise ValueError(
                f"granularity must be one of {sorted(_GRANULARITIES)}, got "
                f"{granularity!r}"
            )
        self._base = base
        self._contextualizer = contextualizer or LLMContextualizer()
        self._granularity = granularity
        self._group_by = group_by
        self._keep_on_failure = keep_on_failure

    def chunk(self, document: Document) -> list[Chunk]:
        chunks = self._base.chunk(document)
        if not chunks:
            return []

        # 1) Group chunks by key (preserves first-seen order)
        groups: dict[str, list[Chunk]] = {}
        skipped: list[Chunk] = []  # chunks with no group key (group_by returned None)
        for c in chunks:
            key = self._key_for(c)
            if key is None:
                skipped.append(c)
                continue
            groups.setdefault(key, []).append(c)

        # 2) Decide the "passage" text for each group — what we ask the
        # LLM to contextualize. Section / paragraph look it up from the
        # document; chunk + custom group_by use the first chunk's text.
        group_keys = list(groups.keys())
        passage_texts = self._passage_texts(group_keys, groups, document)

        # 3) ONE LLM call per unique group key
        preambles = self._contextualizer.generate_batch(
            document.full_text, passage_texts
        )
        preamble_by_key = dict(zip(group_keys, preambles, strict=True))

        # 4) Map preamble back to every chunk in each group, preserve order
        chunk_order = {c.chunk_id: i for i, c in enumerate(chunks)}
        out: list[Chunk] = []
        for key, group_chunks in groups.items():
            preamble = preamble_by_key[key]
            for c in group_chunks:
                new_chunk = self._attach_preamble(c, preamble)
                if new_chunk is not None:
                    out.append(new_chunk)
        # Chunks with no group key (only possible via group_by) pass through.
        for c in skipped:
            out.append(c)
        # Restore original chunk order so downstream consumers see no reordering.
        out.sort(key=lambda c: chunk_order[c.chunk_id])
        return out

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _key_for(self, chunk: Chunk) -> str | None:
        """Return the group key for *chunk*, or None to skip."""
        if self._group_by is not None:
            key = self._group_by(chunk)
            return None if key is None else str(key)
        if self._granularity == "section":
            key = chunk.metadata.get("section_id")
            if key is None:
                raise ValueError(
                    f"ContextualChunker(granularity='section') requires chunks "
                    f"to carry metadata['section_id']. Chunk {chunk.chunk_id!r} "
                    f"is missing this key. Use ParentChildChunker (which sets "
                    f"it) or pass a custom group_by callable."
                )
            return str(key)
        if self._granularity == "paragraph":
            key = chunk.metadata.get("paragraph_id")
            if key is None:
                raise ValueError(
                    f"ContextualChunker(granularity='paragraph') requires chunks "
                    f"to carry metadata['paragraph_id']. Chunk {chunk.chunk_id!r} "
                    f"is missing this key. Use ParentChildChunker (which sets "
                    f"it) or pass a custom group_by callable."
                )
            return str(key)
        # granularity == "chunk"
        return chunk.chunk_id

    def _passage_texts(
        self,
        group_keys: list[str],
        groups: dict[str, list[Chunk]],
        document: Document,
    ) -> list[str]:
        """Return one passage-text per group key, in the same order."""
        if self._group_by is not None or self._granularity == "chunk":
            # No document lookup — the passage IS the chunk text (or, for
            # multi-chunk groups under a custom group_by, the first chunk's
            # text as a representative).
            return [groups[k][0].text for k in group_keys]
        if self._granularity == "section":
            section_by_id = {sec.id: sec for sec in document.sections}
            missing = [k for k in group_keys if k not in section_by_id]
            if missing:
                raise KeyError(
                    f"section_id(s) {missing!r} referenced by chunks but not "
                    f"present in document {document.doc_id!r}"
                )
            return [section_by_id[k].text for k in group_keys]
        # granularity == "paragraph"
        para_by_id: dict[str, Any] = {}
        for sec in document.sections:
            for p in sec.paragraphs:
                para_by_id[p.id] = p
        missing = [k for k in group_keys if k not in para_by_id]
        if missing:
            raise KeyError(
                f"paragraph_id(s) {missing!r} referenced by chunks but not "
                f"present in document {document.doc_id!r}"
            )
        return [para_by_id[k].text for k in group_keys]

    def _attach_preamble(self, chunk: Chunk, preamble: str | None) -> Chunk | None:
        """Return a new Chunk with preamble in metadata, or None to drop."""
        if preamble is None:
            if not self._keep_on_failure:
                return None  # type: ignore[return-value]
            return chunk
        new_meta = {**chunk.metadata, "contextual_preamble": preamble.strip()}
        return Chunk(
            chunk_id=chunk.chunk_id,
            text=chunk.text,
            doc_id=chunk.doc_id,
            sentence_ids=chunk.sentence_ids,
            span=chunk.span,
            metadata=new_meta,
        )


def embedding_text(chunk: Chunk) -> str:
    """Return the text to embed for *chunk*.

    Uses ``metadata["contextual_preamble"]`` if present (Contextual
    Retrieval recipe: preamble + blank line + original text), otherwise
    falls back to the chunk's original text. Centralized here so any
    Pipeline / Indexer / Embedder call site can use the same convention.
    """
    preamble = chunk.metadata.get("contextual_preamble")
    if preamble:
        return f"{preamble}\n\n{chunk.text}"
    return chunk.text


__all__ = [
    "ContextualChunker",
    "LLMContextualizer",
    "embedding_text",
]
