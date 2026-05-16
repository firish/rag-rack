from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from verifiable_rag.chunkers import Chunker
from verifiable_rag.embedders import Embedder
from verifiable_rag.generators import Generator
from verifiable_rag.indexers import HybridIndex
from verifiable_rag.models.answer import (
    Answer,
    CitedSentence,
    FaithfulnessComponents,
    Strictness,
    VerificationResult,
)
from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.document import Document
from verifiable_rag.parsers import Parser
from verifiable_rag.rerankers import Reranker
from verifiable_rag.verifiers import Verifier

# Thresholds below which we refuse regardless of strictness
_STRICTNESS_THRESHOLDS: dict[str, float] = {
    "loose": 0.0,  # never refuse on faithfulness
    "balanced": 0.5,
    "strict": 0.7,
    "paranoid": 0.9,
}


@dataclass
class Pipeline:
    """Orchestrates the full verifiable RAG pipeline.

    Swap any component by passing a different implementation of the
    corresponding Protocol.  All components are required; there are no
    silent no-ops.
    """

    parser: Parser
    chunker: Chunker
    embedder: Embedder
    indexer: HybridIndex
    generator: Generator
    reranker: Reranker | None = None
    verifier: Verifier | None = None
    strictness: Strictness = "balanced"
    top_k_retrieve: int = 20
    top_k_rerank: int = 5

    _documents: dict[str, Document] = field(default_factory=dict, init=False, repr=False)

    def ingest(self, path: str | Path) -> Document:
        """Parse, chunk, embed, and index a document.

        Returns the parsed Document so callers can inspect sentence IDs.
        """
        document, chunks, embeddings = self.prepare_ingest(path)
        self.commit_ingest(document, chunks, embeddings)
        return document

    def prepare_ingest(
        self, path: str | Path
    ) -> tuple[Document, list[Any], list[list[float]]]:
        """Parse, chunk, and embed *path* without touching the shared index.

        Split out from ``ingest()`` so the slow work (parse + embed) can run
        concurrently across threads while ``commit_ingest()`` is serialised
        behind a lock to keep the index consistent.
        """
        p = Path(path)
        document = self.parser.parse(p)
        chunks = self.chunker.chunk(document)
        embeddings = self.embedder.embed([c.text for c in chunks])
        return document, chunks, embeddings

    def commit_ingest(
        self,
        document: Document,
        chunks: list[Any],
        embeddings: list[list[float]],
    ) -> None:
        """Atomically write a prepared ingest to the shared index + doc map."""
        self.indexer.add(chunks, embeddings)
        self._documents[document.doc_id] = document

    def ask(self, query: str) -> Answer:
        """Run the full pipeline for *query* and return a verified Answer."""
        query_embedding = self.embedder.embed_query(query)
        retrieved = self.indexer.search(query, query_embedding, k=self.top_k_retrieve)

        if self.reranker is not None:
            reranked = self.reranker.rerank(query, retrieved, top_k=self.top_k_rerank)
        else:
            reranked = retrieved[: self.top_k_rerank]

        doc_ids = {r.chunk.doc_id for r in reranked}
        documents = {did: self._documents[did] for did in doc_ids if did in self._documents}

        cited_sentences = self.generator.generate(query, reranked, documents)

        # Run the verifier whenever one is configured — strictness only controls
        # whether we REFUSE on a low score, not whether we score at all. This
        # lets loose mode emit NLI scores for analysis without filtering.
        if self.verifier is None:
            verification_results: list[VerificationResult] = []
        else:
            verification_results = self.verifier.verify(cited_sentences, documents)

        return self._build_answer(query, cited_sentences, verification_results, reranked)

    def _build_answer(
        self,
        query: str,
        cited_sentences: list[CitedSentence],
        verification_results: list[VerificationResult],
        retrieved: list[RetrievedChunk],
    ) -> Answer:
        """Build the final Answer, applying surgical correction when a verifier ran.

        Filtering strategy:
        * No verifier results (or loose strictness): every generated CitedSentence
          surfaces. ``was_refused`` reflects only the hard retrieval-score path
          (used when there's no NLI signal to act on).
        * Verifier ran AND strictness != loose: **surgical correction**.  Drop
          individual sentences whose ``VerificationResult.is_supported`` is
          False; keep the rest.  If every sentence is dropped, that counts as
          a refusal.  This is strictly more useful than hard refusal — one
          weakly-supported sentence no longer kills a 4-sentence answer.

        Strictness still controls the *threshold* the verifier uses (via its
        own ``is_supported`` flag, which we trust); strictness in Pipeline
        decides whether we ACT on those flags at all.
        """
        threshold = _STRICTNESS_THRESHOLDS[self.strictness]

        unsupported: list[str] = []
        nli_scores: list[float] = []
        is_supported_by_idx: dict[int, bool] = {}

        for vr in verification_results:
            nli_scores.append(vr.nli_score)
            is_supported_by_idx[vr.cited_sentence_index] = vr.is_supported
            if not vr.is_supported:
                unsupported.append(vr.claim_text)

        avg_nli = sum(nli_scores) / len(nli_scores) if nli_scores else 1.0
        avg_retrieval = sum(r.score for r in retrieved) / len(retrieved) if retrieved else 0.0
        faithfulness_score = avg_nli if nli_scores else avg_retrieval

        # ----- Surgical correction vs hard refusal -----
        if verification_results and self.strictness != "loose":
            # Per-sentence filtering using the verifier's is_supported flag.
            # Sentences without a matching VerificationResult are kept by
            # default (shouldn't happen in practice — Verifier returns one
            # result per input).
            kept = [
                cs
                for i, cs in enumerate(cited_sentences)
                if is_supported_by_idx.get(i, True)
            ]
            # An answer that *had* content but lost it all to filtering is a
            # refusal; an answer that started empty is not.
            was_refused = bool(cited_sentences) and not kept
            final_sentences = kept
            refusal_reason = (
                f"surgical correction filtered all {len(cited_sentences)} "
                f"sentences (strictness={self.strictness})"
                if was_refused
                else None
            )
        else:
            # No verifier — fall back to retrieval-score threshold for refusal.
            was_refused = faithfulness_score < threshold and self.strictness != "loose"
            final_sentences = cited_sentences if not was_refused else []
            refusal_reason = (
                f"faithfulness_score {faithfulness_score:.2f} below "
                f"{self.strictness} threshold {threshold}"
                if was_refused
                else None
            )

        return Answer(
            query=query,
            sentences=final_sentences,
            faithfulness_score=faithfulness_score,
            faithfulness_components=FaithfulnessComponents(
                retrieval_score=avg_retrieval,
                nli_score=avg_nli,
            ),
            unsupported_claims=unsupported,
            retrieved_chunks=retrieved,
            verification_results=verification_results,
            strictness=self.strictness,
            was_refused=was_refused,
            refusal_reason=refusal_reason,
        )
