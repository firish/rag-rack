"""Eval runner — orchestrates benchmark execution and produces an EvalReport.

The runner:
  1. Walks the benchmark to collect every unique document path.
  2. Ingests each document into the pipeline EXACTLY ONCE (sharing the
     index across all questions).
  3. Runs ``pipeline.ask(question)`` for each EvalQuestion.
  4. Wraps the answer into an EvalRecord (catching pipeline errors so one
     bad question doesn't tank the whole run).
  5. Scores all records and returns a populated EvalReport.

Errors are recorded on the EvalRecord rather than raised — this lets a long
benchmark survive a single LLM timeout or rate-limit blip.
"""

from __future__ import annotations

import time

from verifiable_rag.eval import Benchmark, EvalQuestion, EvalRecord, EvalReport
from verifiable_rag.eval.metrics import score_records
from verifiable_rag.pipeline import Pipeline


def run_benchmark(
    pipeline: Pipeline,
    benchmark: Benchmark,
    pipeline_label: str = "baseline",
    max_questions: int | None = None,
    progress: bool = True,
    delay_between_questions: float = 0.0,
) -> EvalReport:
    """Run *benchmark* through *pipeline* and return a scored EvalReport.

    Args:
        pipeline: configured Pipeline (already wired with parser, chunker,
            embedder, indexer, generator).
        benchmark: any object satisfying the Benchmark protocol.
        pipeline_label: free-text label baked into the report (e.g. model name
            + chunker config) so reports are self-describing.
        max_questions: cap for fast smoke runs; None = run all questions.
        progress: print "[i/N] question" before each ask().
    """
    questions = list(benchmark.questions())
    if max_questions is not None:
        questions = questions[:max_questions]

    # ---- 1) Ingest every unique document once ----------------------------
    seen_paths: set[str] = set()
    for q in questions:
        for path in q.document_paths:
            key = str(path.resolve())
            if key in seen_paths:
                continue
            seen_paths.add(key)
            if progress:
                print(f"[ingest] {path}")
            pipeline.ingest(path)

    # ---- 2) Ask each question, collect records ---------------------------
    records: list[EvalRecord] = []
    gold_by_id: dict[str, tuple[frozenset[str], bool]] = {}

    total = len(questions)
    for i, q in enumerate(questions, start=1):
        gold_by_id[q.id] = (q.gold_sentence_ids, q.should_refuse)
        if progress:
            print(f"[ask {i}/{total}] {q.id}: {q.question}")
        records.append(_ask_one(pipeline, q))
        if delay_between_questions and i < total:
            time.sleep(delay_between_questions)

    # ---- 3) Score and return ---------------------------------------------
    report = EvalReport(
        benchmark_name=benchmark.name,
        pipeline_label=pipeline_label,
        records=records,
    )
    report.metrics = score_records(records, gold_by_id)
    return report


def _ask_one(pipeline: Pipeline, question: EvalQuestion) -> EvalRecord:
    """Wrap pipeline.ask() so a single failure becomes an error record."""
    try:
        answer = pipeline.ask(question.question)
    except Exception as exc:  # noqa: BLE001 — eval must survive one bad question
        return EvalRecord(
            question_id=question.id,
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="",
            faithfulness_score=0.0,
            error=f"{type(exc).__name__}: {exc}",
        )

    cited: set[str] = set()
    for cs in answer.sentences:
        cited.update(cs.supporting_sentence_ids)

    # An empty answer is functionally a refusal regardless of strictness:
    # the system produced nothing the user can act on. The Pipeline's
    # was_refused flag only fires above the faithfulness threshold, which
    # in loose mode is 0 — so we OR in the empty-answer case here.
    refused = answer.was_refused or not answer.sentences

    return EvalRecord(
        question_id=question.id,
        was_refused=refused,
        cited_sentence_ids=frozenset(cited),
        answer_text=answer.text,
        faithfulness_score=answer.faithfulness_score,
    )
