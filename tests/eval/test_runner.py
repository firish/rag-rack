"""Tests for run_benchmark using a fake pipeline (no LLM, no docling).

Validates the orchestration loop: ingests are deduped, ask() is called per
question, errors are caught into EvalRecords, and metrics are computed.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import pytest

from verifiable_rag.eval import EvalQuestion
from verifiable_rag.eval.runners import run_benchmark
from verifiable_rag.models.answer import (
    Answer,
    CitedSentence,
    FaithfulnessComponents,
)

# --------------------------------------------------------------------------- #
# Fake pipeline + benchmark
# --------------------------------------------------------------------------- #


class _FakeDoc:
    """Minimal Document stand-in carrying parser_name + path for tests."""

    def __init__(self, parser_name: str | None, path: Path | None = None) -> None:
        self.parser_name = parser_name
        self.path = path


class _FakePipeline:
    """Minimal stand-in for Pipeline — records calls, returns canned Answers."""

    def __init__(self, answers_by_question: dict[str, Answer]) -> None:
        self._answers = answers_by_question
        self.ingested_paths: list[Path] = []
        self.prepared_paths: list[Path] = []
        self.asked: list[str] = []

    def ingest(self, path) -> None:  # type: ignore[no-untyped-def]
        document, chunks, embeddings = self.prepare_ingest(path)
        self.commit_ingest(document, chunks, embeddings)

    def prepare_ingest(self, path):  # type: ignore[no-untyped-def]
        self.prepared_paths.append(Path(path))
        # The runner reads document.parser_name from prepared[0]; return a
        # minimal stand-in that carries that attribute plus the path so
        # commit_ingest can still record what landed.
        return (_FakeDoc(path=Path(path), parser_name=None), [], [])

    def commit_ingest(self, document, chunks, embeddings) -> None:  # type: ignore[no-untyped-def]
        # commit is the equivalent of "successfully ingested" — tests check
        # this list because it reflects what actually landed in the index.
        self.ingested_paths.append(document.path)

    def ask(self, query: str) -> Answer:
        self.asked.append(query)
        return self._answers[query]


class _FakeBench:
    name = "fake"

    def __init__(self, questions: list[EvalQuestion]) -> None:
        self._qs = questions

    def questions(self) -> Iterator[EvalQuestion]:
        yield from self._qs


def _answer(text: str, supporting: tuple[str, ...] = (), refused: bool = False) -> Answer:
    sentences = (
        []
        if refused
        else [CitedSentence(text=text, supporting_sentence_ids=supporting, confidence=1.0)]
    )
    return Answer(
        query="ignored",
        sentences=sentences,
        faithfulness_score=0.0 if refused else 0.9,
        faithfulness_components=FaithfulnessComponents(retrieval_score=0.5, nli_score=1.0),
        unsupported_claims=[],
        retrieved_chunks=[],
        verification_results=[],
        was_refused=refused,
        refusal_reason="fake-refusal" if refused else None,
    )


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_dedupes_document_ingest(tmp_path: Path) -> None:
    """Two questions sharing a document should ingest it once."""
    p = tmp_path / "doc.pdf"
    p.write_bytes(b"")  # exists for resolve()

    qs = [
        EvalQuestion(
            id="q1", question="A?", document_paths=(p,), gold_sentence_ids=frozenset({"x"})
        ),
        EvalQuestion(
            id="q2", question="B?", document_paths=(p,), gold_sentence_ids=frozenset({"y"})
        ),
    ]
    pipe = _FakePipeline({"A?": _answer("A.", ("x",)), "B?": _answer("B.", ("y",))})

    run_benchmark(pipe, _FakeBench(qs), progress=False)
    assert len(pipe.ingested_paths) == 1
    assert pipe.asked == ["A?", "B?"]


@pytest.mark.smoke
def test_records_capture_citations_and_refusal() -> None:
    qs = [
        EvalQuestion(id="q1", question="A?", document_paths=(), gold_sentence_ids=frozenset({"x"})),
        EvalQuestion(
            id="q2",
            question="B?",
            document_paths=(),
            gold_sentence_ids=frozenset(),
            should_refuse=True,
        ),
    ]
    pipe = _FakePipeline({"A?": _answer("A.", ("x",)), "B?": _answer("", refused=True)})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    rec_by_id = {r.question_id: r for r in report.records}

    assert rec_by_id["q1"].cited_sentence_ids == frozenset({"x"})
    assert rec_by_id["q1"].was_refused is False
    assert rec_by_id["q2"].cited_sentence_ids == frozenset()
    assert rec_by_id["q2"].was_refused is True


@pytest.mark.smoke
def test_ingest_exception_does_not_kill_the_run(tmp_path: Path) -> None:
    """A bad PDF (or any ingest error) should not abort the whole benchmark."""

    class _BadIngestPipeline(_FakePipeline):
        def prepare_ingest(self, path):  # type: ignore[no-untyped-def]
            if "bad" in str(path):
                raise ValueError(f"DoclingParser produced no content from {path}")
            return super().prepare_ingest(path)

    good_pdf = tmp_path / "good.pdf"
    bad_pdf = tmp_path / "bad.pdf"
    good_pdf.write_bytes(b"")
    bad_pdf.write_bytes(b"")

    qs = [
        EvalQuestion(
            id="q_good", question="A?", document_paths=(good_pdf,),
            gold_sentence_ids=frozenset({"x"}),
        ),
        EvalQuestion(
            id="q_bad", question="B?", document_paths=(bad_pdf,),
            gold_sentence_ids=frozenset({"y"}),
        ),
    ]
    pipe = _BadIngestPipeline(
        {"A?": _answer("A.", ("x",)), "B?": _answer("", refused=True)}
    )

    # The run should COMPLETE despite the bad PDF. The good question lands in
    # records; the bad question is discarded (no source PDF survived ingest).
    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    assert [r.question_id for r in report.records] == ["q_good"]
    assert report.discarded_question_ids == ["q_bad"]
    assert pipe.ingested_paths == [good_pdf]  # only the good one ingested


@pytest.mark.smoke
def test_pipeline_exception_becomes_error_record() -> None:
    """One bad question must not break the run."""

    class _BoomPipeline(_FakePipeline):
        def ask(self, query: str) -> Answer:
            if query == "B?":
                raise RuntimeError("kaboom")
            return super().ask(query)

    qs = [
        EvalQuestion(id="q1", question="A?", document_paths=(), gold_sentence_ids=frozenset({"x"})),
        EvalQuestion(id="q2", question="B?", document_paths=(), gold_sentence_ids=frozenset({"y"})),
    ]
    pipe = _BoomPipeline({"A?": _answer("A.", ("x",))})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    rec_by_id = {r.question_id: r for r in report.records}

    assert rec_by_id["q1"].error is None
    assert rec_by_id["q2"].error is not None
    assert "kaboom" in rec_by_id["q2"].error
    # The error count is reflected in the metrics
    assert report.metrics["n_errors"] == 1.0


@pytest.mark.smoke
def test_max_questions_caps_run() -> None:
    qs = [
        EvalQuestion(
            id=f"q{i}", question=f"Q{i}?", document_paths=(), gold_sentence_ids=frozenset({"x"})
        )
        for i in range(5)
    ]
    pipe = _FakePipeline({f"Q{i}?": _answer(f"A{i}.", ("x",)) for i in range(5)})

    report = run_benchmark(pipe, _FakeBench(qs), max_questions=2, progress=False)
    assert len(report.records) == 2
    assert pipe.asked == ["Q0?", "Q1?"]


@pytest.mark.smoke
def test_parallel_ingest_commits_serially(tmp_path: Path) -> None:
    """ingest_workers>1 may prepare in parallel, but commits stay serial.

    Asserts every prepared path also got committed exactly once — i.e. the
    commit_lock kept the index consistent under concurrency.
    """
    paths = []
    for i in range(8):
        p = tmp_path / f"doc{i}.pdf"
        p.write_bytes(b"")
        paths.append(p)

    qs = [
        EvalQuestion(
            id=f"q{i}", question=f"Q{i}?", document_paths=(paths[i],),
            gold_sentence_ids=frozenset({"x"}),
        )
        for i in range(8)
    ]
    pipe = _FakePipeline({f"Q{i}?": _answer(f"A{i}.", ("x",)) for i in range(8)})

    run_benchmark(pipe, _FakeBench(qs), progress=False, ingest_workers=4)

    assert sorted(p.name for p in pipe.prepared_paths) == [f"doc{i}.pdf" for i in range(8)]
    assert sorted(p.name for p in pipe.ingested_paths) == [f"doc{i}.pdf" for i in range(8)]


@pytest.mark.smoke
def test_questions_with_all_pdfs_failed_are_discarded(tmp_path: Path) -> None:
    """If every source PDF of a question fails to parse, drop it from records.

    The question must not appear in records and must not contribute to metrics;
    its id ends up in report.discarded_question_ids and n_discarded.
    """
    good_pdf = tmp_path / "good.pdf"
    bad_pdf = tmp_path / "bad.pdf"
    good_pdf.write_bytes(b"")
    bad_pdf.write_bytes(b"")

    class _SelectiveFailPipeline(_FakePipeline):
        def prepare_ingest(self, path):  # type: ignore[no-untyped-def]
            if "bad" in str(path):
                raise ValueError("DoclingParser produced no content")
            return super().prepare_ingest(path)

    qs = [
        EvalQuestion(
            id="q_good", question="A?", document_paths=(good_pdf,),
            gold_sentence_ids=frozenset({"x"}),
        ),
        EvalQuestion(
            id="q_bad", question="B?", document_paths=(bad_pdf,),
            gold_sentence_ids=frozenset({"y"}),
        ),
    ]
    pipe = _SelectiveFailPipeline({"A?": _answer("A.", ("x",))})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False)

    assert [r.question_id for r in report.records] == ["q_good"]
    assert report.discarded_question_ids == ["q_bad"]
    assert report.metrics["n_discarded"] == 1.0
    # Pipeline.ask was never called for q_bad
    assert "B?" not in pipe.asked


@pytest.mark.smoke
def test_partial_pdf_failure_keeps_question(tmp_path: Path) -> None:
    """Question with multiple source PDFs survives if ANY of them parses."""
    good_pdf = tmp_path / "good.pdf"
    bad_pdf = tmp_path / "bad.pdf"
    good_pdf.write_bytes(b"")
    bad_pdf.write_bytes(b"")

    class _SelectiveFailPipeline(_FakePipeline):
        def prepare_ingest(self, path):  # type: ignore[no-untyped-def]
            if "bad" in str(path):
                raise ValueError("broken")
            return super().prepare_ingest(path)

    qs = [
        EvalQuestion(
            id="q_mixed",
            question="A?",
            document_paths=(good_pdf, bad_pdf),
            gold_sentence_ids=frozenset({"x"}),
        ),
    ]
    pipe = _SelectiveFailPipeline({"A?": _answer("A.", ("x",))})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    assert [r.question_id for r in report.records] == ["q_mixed"]
    assert report.discarded_question_ids == []


@pytest.mark.smoke
def test_parallel_preserves_order_and_count() -> None:
    """With max_workers>1, records still come back in question order."""
    qs = [
        EvalQuestion(
            id=f"q{i}", question=f"Q{i}?", document_paths=(), gold_sentence_ids=frozenset({"x"})
        )
        for i in range(8)
    ]
    pipe = _FakePipeline({f"Q{i}?": _answer(f"A{i}.", ("x",)) for i in range(8)})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False, max_workers=4)

    assert len(report.records) == 8
    assert [r.question_id for r in report.records] == [f"q{i}" for i in range(8)]
    # Every Q? was asked (order doesn't matter, since threads can interleave)
    assert sorted(pipe.asked) == [f"Q{i}?" for i in range(8)]


@pytest.mark.smoke
def test_parallel_tolerates_per_question_error() -> None:
    """Parallel mode still wraps exceptions into error records."""

    class _FlakyPipeline(_FakePipeline):
        def ask(self, query: str) -> Answer:
            if query == "Q3?":
                raise RuntimeError("flaky")
            return super().ask(query)

    qs = [
        EvalQuestion(
            id=f"q{i}", question=f"Q{i}?", document_paths=(), gold_sentence_ids=frozenset({"x"})
        )
        for i in range(5)
    ]
    pipe = _FlakyPipeline({f"Q{i}?": _answer(f"A{i}.", ("x",)) for i in range(5) if i != 3})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False, max_workers=3)
    rec_by_id = {r.question_id: r for r in report.records}

    assert len(report.records) == 5
    assert rec_by_id["q3"].error is not None
    assert "flaky" in rec_by_id["q3"].error
    assert all(rec_by_id[f"q{i}"].error is None for i in (0, 1, 2, 4))


@pytest.mark.smoke
def test_report_carries_parser_provenance_per_question(tmp_path: Path) -> None:
    """Runner populates parsers_by_question_id from each Document.parser_name."""
    doc_a = tmp_path / "a.pdf"
    doc_b = tmp_path / "b.pdf"
    doc_a.write_bytes(b"")
    doc_b.write_bytes(b"")

    class _TaggingPipeline(_FakePipeline):
        def prepare_ingest(self, path):  # type: ignore[no-untyped-def]
            super().prepare_ingest(path)
            parser = "docling" if path.name == "a.pdf" else "pymupdf"
            return (_FakeDoc(parser_name=parser), [], [])

        def commit_ingest(self, document, chunks, embeddings) -> None:  # type: ignore[no-untyped-def]
            # path-equivalent for the test bookkeeping
            self.ingested_paths.append(Path(f"committed::{document.parser_name}"))

    qs = [
        EvalQuestion(
            id="q_a", question="A?", document_paths=(doc_a,),
            gold_sentence_ids=frozenset({"x"}),
        ),
        EvalQuestion(
            id="q_b", question="B?", document_paths=(doc_b,),
            gold_sentence_ids=frozenset({"y"}),
        ),
    ]
    pipe = _TaggingPipeline({"A?": _answer("A.", ("x",)), "B?": _answer("B.", ("y",))})

    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    assert report.parsers_by_question_id == {"q_a": ["docling"], "q_b": ["pymupdf"]}


@pytest.mark.smoke
def test_parser_name_defaults_to_unknown_when_doc_does_not_set_it(tmp_path: Path) -> None:
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"")

    class _UntaggedPipeline(_FakePipeline):
        def prepare_ingest(self, path):  # type: ignore[no-untyped-def]
            super().prepare_ingest(path)
            return (_FakeDoc(parser_name=None), [], [])

        def commit_ingest(self, document, chunks, embeddings) -> None:  # type: ignore[no-untyped-def]
            self.ingested_paths.append(Path("committed"))

    qs = [EvalQuestion(
        id="q", question="Q?", document_paths=(pdf,), gold_sentence_ids=frozenset({"x"}),
    )]
    pipe = _UntaggedPipeline({"Q?": _answer("A.", ("x",))})
    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    assert report.parsers_by_question_id == {"q": ["unknown"]}


@pytest.mark.smoke
def test_metrics_populated_after_run() -> None:
    qs = [
        EvalQuestion(id="q1", question="A?", document_paths=(), gold_sentence_ids=frozenset({"x"})),
    ]
    pipe = _FakePipeline({"A?": _answer("A.", ("x",))})
    report = run_benchmark(pipe, _FakeBench(qs), progress=False)

    assert "citation_f1" in report.metrics
    assert "abstention_f1" in report.metrics
    assert report.metrics["citation_f1"] == 1.0
