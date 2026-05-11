"""Evaluation harness for verifiable-rag.

Metrics here operate at sentence/span-level, not chunk-level, to match the
library's core thesis. Wrap RAGAS/DeepEval for chunk-level baselines later.

Tier 1 scope (current):
  * Set-based citation precision/recall (does the predicted citation set
    overlap the gold set?)
  * Abstention precision/recall (did we refuse on questions we should have?)
  * Per-question records + aggregate report

Tier 2 will add: span tightness (char-level alignment), per-claim attribution,
and additional benchmarks (LitQA2, RAGTruth, HaluBench).
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, runtime_checkable


@dataclass(frozen=True)
class EvalQuestion:
    """One question in an evaluation benchmark.

    The pipeline ingests *document_paths* (in order) before being asked
    *question*. Predictions are then scored against *gold_sentence_ids*
    and *should_refuse*.
    """

    id: str
    question: str
    document_paths: tuple[Path, ...]
    gold_sentence_ids: frozenset[str]  # sentences that genuinely support the answer
    should_refuse: bool = False  # True for unanswerable questions
    gold_answer_text: str | None = None  # optional human-readable reference

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("EvalQuestion.id must be non-empty")
        if not self.question.strip():
            raise ValueError(f"EvalQuestion {self.id!r} has empty question text")
        if self.should_refuse and self.gold_sentence_ids:
            raise ValueError(
                f"EvalQuestion {self.id!r}: should_refuse=True is "
                f"incompatible with non-empty gold_sentence_ids"
            )


@runtime_checkable
class Benchmark(Protocol):
    """A collection of EvalQuestions sharing some context (e.g. one source PDF)."""

    name: str

    def questions(self) -> Iterator[EvalQuestion]: ...


@dataclass(frozen=True)
class EvalRecord:
    """The pipeline's output for one EvalQuestion, ready to be scored."""

    question_id: str
    was_refused: bool
    cited_sentence_ids: frozenset[str]  # union across all CitedSentences in the answer
    answer_text: str
    faithfulness_score: float
    error: str | None = None  # set if the pipeline raised


@dataclass
class EvalReport:
    """Aggregate result of running a benchmark."""

    benchmark_name: str
    pipeline_label: str
    records: list[EvalRecord] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)


__all__ = [
    "Benchmark",
    "EvalQuestion",
    "EvalRecord",
    "EvalReport",
]
