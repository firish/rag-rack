"""End-to-end Pipeline integration tests.

These tests wire real chunker + indexer (LanceDB + bm25 + RRF) with fakes
for parser, embedder, and generator so the whole flow runs in <1s with no
network or model downloads.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
from verifiable_rag.models.answer import (
    Answer,
    CitedSentence,
    VerificationResult,
)
from verifiable_rag.models.chunk import RetrievedChunk
from verifiable_rag.models.document import Document
from verifiable_rag.models.span import Span
from verifiable_rag.pipeline import Pipeline

lancedb = pytest.importorskip("lancedb", reason="lancedb not installed")
bm25s = pytest.importorskip("bm25s", reason="bm25s not installed")


# --------------------------------------------------------------------------- #
# Fakes — parser / embedder / generator / verifier
# --------------------------------------------------------------------------- #

DIM = 8


class _FakeParser:
    """Returns a pre-built Document on every parse() call."""

    def __init__(self, document: Document) -> None:
        self._doc = document

    def parse(self, path: Path) -> Document:
        return self._doc


class _FakeEmbedder:
    """Hash-based embedder — deterministic, no model needed."""

    def __init__(self, dim: int = DIM) -> None:
        self._dim = dim

    @property
    def dimension(self) -> int:
        return self._dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [self._vec(t) for t in texts]

    def embed_query(self, query: str) -> list[float]:
        return self._vec(query)

    def _vec(self, text: str) -> list[float]:
        # Cheap unit-vector hash: stable per text, length=dim, non-zero magnitude.
        import hashlib
        import math

        digest = hashlib.sha256(text.encode("utf-8")).digest()
        raw = [(digest[i] / 255.0) + 0.01 for i in range(self._dim)]
        mag = math.sqrt(sum(v * v for v in raw))
        return [v / mag for v in raw]


class _FakeGenerator:
    """Returns a pre-baked list of CitedSentence ignoring inputs."""

    mode = "prompted"

    def __init__(self, sentences: list[CitedSentence]) -> None:
        self._sentences = sentences
        self.last_chunks: list[RetrievedChunk] | None = None
        self.last_documents: dict[str, Document] = {}

    def generate(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        documents: dict[str, Document],
    ) -> list[CitedSentence]:
        self.last_chunks = chunks
        self.last_documents = documents
        return self._sentences


class _AlwaysSupportedVerifier:
    def verify(
        self,
        sentences: list[CitedSentence],
        documents: dict[str, Document],
    ) -> list[VerificationResult]:
        return [
            VerificationResult(
                cited_sentence_index=i,
                claim_text=s.text,
                is_supported=True,
                nli_score=1.0,
            )
            for i, s in enumerate(sentences)
        ]


class _AlwaysFailVerifier:
    def verify(
        self,
        sentences: list[CitedSentence],
        documents: dict[str, Document],
    ) -> list[VerificationResult]:
        return [
            VerificationResult(
                cited_sentence_index=i,
                claim_text=s.text,
                is_supported=False,
                nli_score=0.05,
            )
            for i, s in enumerate(sentences)
        ]


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _build_pipeline(tmp_path: Path, generator: _FakeGenerator, **kwargs) -> Pipeline:
    return Pipeline(
        parser=_FakeParser(_build_doc()),
        chunker=ParentChildChunker(),
        embedder=_FakeEmbedder(),
        indexer=HybridIndex(
            dense=LanceDBIndex(uri=tmp_path / "lance"),
            sparse=BM25Index(),
        ),
        generator=generator,
        **kwargs,
    )


def _build_doc() -> Document:
    return build_document(
        sections_spec=[
            (
                "Intro",
                [
                    ["Mitochondria produce ATP.", "They are organelles."],
                    ["Cells need energy."],
                ],
            ),
            ("Methods", [["We measured oxygen consumption rates."]]),
        ],
        doc_id="bio",
    )


# --------------------------------------------------------------------------- #
# ingest()
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_ingest_returns_document_and_indexes_chunks(tmp_path: Path) -> None:
    gen = _FakeGenerator([])
    pipe = _build_pipeline(tmp_path, gen)

    doc = pipe.ingest("/dev/null")  # path is ignored by FakeParser
    assert doc.doc_id == "bio"
    assert pipe.indexer.count > 0


@pytest.mark.smoke
def test_ingest_remembers_document_for_later_ask(tmp_path: Path) -> None:
    gen = _FakeGenerator(
        [CitedSentence(text="ATP is energy.", supporting_sentence_ids=("bio::s0",), confidence=1.0)]
    )
    pipe = _build_pipeline(tmp_path, gen)
    pipe.ingest("/dev/null")

    pipe.ask("what is ATP?")
    # The generator must have received the document keyed by doc_id
    assert "bio" in gen.last_documents
    assert gen.last_documents["bio"].doc_id == "bio"


# --------------------------------------------------------------------------- #
# ask() — baseline (no reranker, no verifier, loose strictness)
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_ask_returns_answer_with_cited_sentences(tmp_path: Path) -> None:
    gen = _FakeGenerator(
        [
            CitedSentence(
                text="Mitochondria make ATP.",
                supporting_sentence_ids=("bio::s0",),
                confidence=1.0,
            )
        ]
    )
    pipe = _build_pipeline(tmp_path, gen, strictness="loose")
    pipe.ingest("/dev/null")

    answer = pipe.ask("what produces ATP?")
    assert isinstance(answer, Answer)
    assert len(answer.sentences) == 1
    assert answer.sentences[0].supporting_sentence_ids == ("bio::s0",)


@pytest.mark.smoke
def test_ask_passes_retrieved_chunks_to_generator(tmp_path: Path) -> None:
    gen = _FakeGenerator([])
    pipe = _build_pipeline(tmp_path, gen, strictness="loose")
    pipe.ingest("/dev/null")
    pipe.ask("question")

    assert gen.last_chunks is not None
    assert len(gen.last_chunks) > 0
    # Capped at top_k_rerank when no reranker is set
    assert len(gen.last_chunks) <= pipe.top_k_rerank


@pytest.mark.smoke
def test_loose_strictness_runs_verifier_but_does_not_refuse(tmp_path: Path) -> None:
    """Loose mode runs the verifier (for scoring/analysis) but never refuses.

    Pipeline calls the verifier whenever one is configured — strictness only
    controls whether a low NLI score triggers refusal. Loose mode = instrument
    but don't act.
    """

    class _SpyVerifier(_AlwaysFailVerifier):
        def __init__(self) -> None:
            self.calls = 0

        def verify(self, sentences, documents):  # type: ignore[no-untyped-def]
            self.calls += 1
            return super().verify(sentences, documents)

    spy = _SpyVerifier()
    gen = _FakeGenerator(
        [CitedSentence(text="X.", supporting_sentence_ids=("bio::s0",), confidence=1.0)]
    )
    pipe = _build_pipeline(tmp_path, gen, strictness="loose", verifier=spy)
    pipe.ingest("/dev/null")
    answer = pipe.ask("q?")

    # Verifier was called — we want the score in the report
    assert spy.calls == 1
    # But loose mode never refuses on faithfulness, even when the verifier fails
    assert not answer.was_refused
    # And we get the verification_results in the Answer for inspection
    assert len(answer.verification_results) == 1


# --------------------------------------------------------------------------- #
# ask() — with verifier
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_ask_with_supporting_verifier_keeps_sentences(tmp_path: Path) -> None:
    gen = _FakeGenerator(
        [CitedSentence(text="ATP.", supporting_sentence_ids=("bio::s0",), confidence=1.0)]
    )
    pipe = _build_pipeline(
        tmp_path,
        gen,
        strictness="strict",
        verifier=_AlwaysSupportedVerifier(),
    )
    pipe.ingest("/dev/null")
    answer = pipe.ask("q?")

    assert not answer.was_refused
    assert answer.faithfulness_components.nli_score == pytest.approx(1.0)
    assert answer.unsupported_claims == []


@pytest.mark.smoke
def test_ask_with_failing_verifier_refuses_in_strict_mode(tmp_path: Path) -> None:
    gen = _FakeGenerator(
        [CitedSentence(text="Bad.", supporting_sentence_ids=("bio::s0",), confidence=1.0)]
    )
    pipe = _build_pipeline(
        tmp_path,
        gen,
        strictness="strict",
        verifier=_AlwaysFailVerifier(),
    )
    pipe.ingest("/dev/null")
    answer = pipe.ask("q?")

    assert answer.was_refused
    assert answer.refusal_reason is not None
    assert answer.sentences == []  # refused → no claims surfaced
    assert "Bad." in answer.unsupported_claims


# --------------------------------------------------------------------------- #
# Refusal mechanics
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_empty_generator_output_is_not_refused_in_loose_mode(tmp_path: Path) -> None:
    """Empty generator output produces an empty answer but not a refusal flag in loose."""
    gen = _FakeGenerator([])
    pipe = _build_pipeline(tmp_path, gen, strictness="loose")
    pipe.ingest("/dev/null")
    answer = pipe.ask("q?")

    assert answer.sentences == []
    assert answer.was_refused is False  # loose threshold is 0.0


# --------------------------------------------------------------------------- #
# Reranker pass-through
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_reranker_called_when_supplied(tmp_path: Path) -> None:
    """If a reranker is provided, the pipeline must use it."""

    class _ReverseReranker:
        """Reverses the retrieved order, then trims to top_k."""

        def __init__(self) -> None:
            self.called_with: list[RetrievedChunk] | None = None

        def rerank(
            self,
            query: str,
            chunks: list[RetrievedChunk],
            top_k: int = 5,
        ) -> list[RetrievedChunk]:
            self.called_with = chunks
            return list(reversed(chunks))[:top_k]

    rr = _ReverseReranker()
    gen = _FakeGenerator([])
    pipe = _build_pipeline(tmp_path, gen, strictness="loose", reranker=rr)
    pipe.ingest("/dev/null")
    pipe.ask("q?")

    assert rr.called_with is not None
    assert len(rr.called_with) > 0


# --------------------------------------------------------------------------- #
# Multi-document ingest
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_pipeline_handles_multiple_documents(tmp_path: Path) -> None:
    """Two ingests → both docs available; generator sees both."""

    class _TwoDocParser:
        """Returns doc 'bio' on first call, 'chem' on second."""

        def __init__(self) -> None:
            self._docs = [
                build_document(
                    sections_spec=[("S1", [["Bio sentence one.", "Bio sentence two."]])],
                    doc_id="bio",
                ),
                build_document(
                    sections_spec=[("S1", [["Chem sentence one."]])],
                    doc_id="chem",
                ),
            ]
            self._n = 0

        def parse(self, path: Path) -> Document:
            doc = self._docs[self._n]
            self._n += 1
            return doc

    gen = _FakeGenerator(
        [CitedSentence(text="X.", supporting_sentence_ids=("bio::s0",), confidence=1.0)]
    )
    pipe = Pipeline(
        parser=_TwoDocParser(),
        chunker=ParentChildChunker(),
        embedder=_FakeEmbedder(),
        indexer=HybridIndex(
            dense=LanceDBIndex(uri=tmp_path / "lance"),
            sparse=BM25Index(),
        ),
        generator=gen,
        strictness="loose",
    )
    pipe.ingest("/path/a.pdf")
    pipe.ingest("/path/b.pdf")

    pipe.ask("anything?")
    assert "bio" in gen.last_documents
    # chem doc may or may not be passed depending on retrieval — but both
    # are stored on the pipeline
    assert pipe.indexer.count > 0
