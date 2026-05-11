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


class _FakePipeline:
    """Minimal stand-in for Pipeline — records calls, returns canned Answers."""

    def __init__(self, answers_by_question: dict[str, Answer]) -> None:
        self._answers = answers_by_question
        self.ingested_paths: list[Path] = []
        self.asked: list[str] = []

    def ingest(self, path) -> None:  # type: ignore[no-untyped-def]
        self.ingested_paths.append(Path(path))

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
    pipe = _FakePipeline(
        {"A?": _answer("A.", ("x",)), "B?": _answer("B.", ("y",))}
    )

    run_benchmark(pipe, _FakeBench(qs), progress=False)
    assert len(pipe.ingested_paths) == 1
    assert pipe.asked == ["A?", "B?"]


@pytest.mark.smoke
def test_records_capture_citations_and_refusal() -> None:
    qs = [
        EvalQuestion(
            id="q1", question="A?", document_paths=(), gold_sentence_ids=frozenset({"x"})
        ),
        EvalQuestion(
            id="q2", question="B?", document_paths=(), gold_sentence_ids=frozenset(), should_refuse=True
        ),
    ]
    pipe = _FakePipeline(
        {"A?": _answer("A.", ("x",)), "B?": _answer("", refused=True)}
    )

    report = run_benchmark(pipe, _FakeBench(qs), progress=False)
    rec_by_id = {r.question_id: r for r in report.records}

    assert rec_by_id["q1"].cited_sentence_ids == frozenset({"x"})
    assert rec_by_id["q1"].was_refused is False
    assert rec_by_id["q2"].cited_sentence_ids == frozenset()
    assert rec_by_id["q2"].was_refused is True


@pytest.mark.smoke
def test_pipeline_exception_becomes_error_record() -> None:
    """One bad question must not break the run."""

    class _BoomPipeline(_FakePipeline):
        def ask(self, query: str) -> Answer:
            if query == "B?":
                raise RuntimeError("kaboom")
            return super().ask(query)

    qs = [
        EvalQuestion(
            id="q1", question="A?", document_paths=(), gold_sentence_ids=frozenset({"x"})
        ),
        EvalQuestion(
            id="q2", question="B?", document_paths=(), gold_sentence_ids=frozenset({"y"})
        ),
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
def test_metrics_populated_after_run() -> None:
    qs = [
        EvalQuestion(
            id="q1", question="A?", document_paths=(), gold_sentence_ids=frozenset({"x"})
        ),
    ]
    pipe = _FakePipeline({"A?": _answer("A.", ("x",))})
    report = run_benchmark(pipe, _FakeBench(qs), progress=False)

    assert "citation_f1" in report.metrics
    assert "abstention_f1" in report.metrics
    assert report.metrics["citation_f1"] == 1.0
