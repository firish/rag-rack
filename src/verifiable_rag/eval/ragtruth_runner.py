"""RAGTruth runner — scores a verifier (any :class:`NLIScorer`) on
:class:`RAGTruthBench` and produces a :class:`RAGTruthReport`.

The shape is intentionally different from :func:`run_benchmark` /
:func:`run_alce_benchmark`: RAGTruth examples are *pre-generated*, so
parser/chunker/retriever/reranker/generator never run. Only the verifier
is exercised. The runner:

1. For each example, segments the response into sentences.
2. Scores every ``(context, response_sentence)`` pair with the scorer.
3. Aggregates per-sentence scores into a response-level score
   (``min`` by default — HALT-RAG's recommendation: any unsupported
   sentence makes the response unsupported).
4. Computes binary-classification metrics against the gold
   ``is_hallucinated`` label, plus per-task / per-model breakdowns.

The scorer is anything satisfying :class:`NLIScorer`. Today that's
:class:`HHEMVerifier`; later it will be MiniCheck, DualNLI, LLM-judge.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Protocol

from verifiable_rag.eval.datasets.ragtruth import RAGTruthBench, RAGTruthExample
from verifiable_rag.verifiers import NLIScorer

logger = logging.getLogger(__name__)

_AGGREGATIONS = frozenset({"min", "mean"})


class _Splitter(Protocol):
    def split_with_offsets(self, text: str) -> list:  # SentenceSpan
        ...


@dataclass(frozen=True)
class RAGTruthRecord:
    """One scored RAGTruth example."""

    example_id: str
    task_type: str
    model: str
    is_hallucinated: bool  # gold
    response_score: float  # aggregated per-sentence NLI score, [0, 1] (higher = more supported)
    n_sentences: int
    error: str | None = None


@dataclass
class RAGTruthReport:
    benchmark_name: str
    scorer_label: str
    aggregation: str  # "min" | "mean"
    records: list[RAGTruthRecord] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    by_task: dict[str, dict[str, float]] = field(default_factory=dict)
    by_model: dict[str, dict[str, float]] = field(default_factory=dict)


# --------------------------------------------------------------------------- #
# Public entry point
# --------------------------------------------------------------------------- #


def run_ragtruth(
    scorer: NLIScorer,
    benchmark: RAGTruthBench,
    *,
    scorer_label: str = "hhem",
    aggregation: str = "min",
    sentence_splitter: _Splitter | None = None,
    progress: bool = True,
    batch_size: int = 32,
) -> RAGTruthReport:
    """Score *benchmark* with *scorer*, return a populated report.

    Args:
        scorer: any object satisfying :class:`NLIScorer`.
        benchmark: a :class:`RAGTruthBench` (filter by task/model/split
            before passing in).
        scorer_label: free-text label baked into the report.
        aggregation: how to collapse per-sentence scores into a
            response-level score. ``"min"`` (default) flags the response
            if any sentence is unsupported — matches HALT-RAG. ``"mean"``
            averages, smoothing over single bad sentences.
        sentence_splitter: object exposing ``split_with_offsets(text)``.
            Defaults to :class:`SentenceSplitter` (wtpsplit-backed).
        progress: print per-example progress.
        batch_size: how many ``(premise, hypothesis)`` pairs to send to
            ``scorer.score_pairs`` at once. Bigger = faster on GPU,
            limited by model memory.
    """
    if aggregation not in _AGGREGATIONS:
        raise ValueError(
            f"aggregation must be one of {sorted(_AGGREGATIONS)}, got {aggregation!r}"
        )

    splitter = sentence_splitter or _default_splitter()
    examples = list(benchmark.examples())
    total = len(examples)

    records: list[RAGTruthRecord] = []
    pending_pairs: list[tuple[str, str]] = []
    pending_lookup: list[tuple[int, int]] = []  # (example_idx, sentence_idx)
    per_example_n_sentences: list[int] = [0] * total

    # Pass 1: segment, collect pairs (batched per example boundary not required,
    # but we flush at batch_size so a 2700-row run doesn't OOM the scorer).
    per_example_scores: list[list[float]] = [[] for _ in range(total)]
    per_example_error: list[str | None] = [None] * total

    for ex_idx, ex in enumerate(examples):
        if progress and ex_idx % 100 == 0:
            print(f"[ragtruth-segment {ex_idx}/{total}]", flush=True)
        if not ex.response.strip() or not ex.context.strip():
            per_example_error[ex_idx] = "empty_response_or_context"
            continue
        try:
            sentences = splitter.split_with_offsets(ex.response)
        except Exception as exc:  # noqa: BLE001 — one bad segment shouldn't kill the run
            per_example_error[ex_idx] = f"segment: {type(exc).__name__}: {exc}"
            continue
        if not sentences:
            per_example_error[ex_idx] = "no_sentences_after_split"
            continue
        per_example_n_sentences[ex_idx] = len(sentences)
        for s_idx, sent in enumerate(sentences):
            pending_pairs.append((ex.context, sent.text))
            pending_lookup.append((ex_idx, s_idx))
            per_example_scores[ex_idx].append(0.0)  # placeholder, filled below

            if len(pending_pairs) >= batch_size:
                _flush_batch(
                    scorer, pending_pairs, pending_lookup, per_example_scores
                )

    if pending_pairs:
        _flush_batch(scorer, pending_pairs, pending_lookup, per_example_scores)

    # Pass 2: aggregate, build records.
    for ex_idx, ex in enumerate(examples):
        if progress and ex_idx % 500 == 0 and ex_idx > 0:
            print(f"[ragtruth-aggregate {ex_idx}/{total}]", flush=True)
        scores = per_example_scores[ex_idx]
        err = per_example_error[ex_idx]
        if err is not None or not scores:
            records.append(
                RAGTruthRecord(
                    example_id=ex.id,
                    task_type=ex.task_type,
                    model=ex.model,
                    is_hallucinated=ex.is_hallucinated,
                    response_score=0.0,
                    n_sentences=per_example_n_sentences[ex_idx],
                    error=err or "no_scores",
                )
            )
            continue
        agg = min(scores) if aggregation == "min" else sum(scores) / len(scores)
        records.append(
            RAGTruthRecord(
                example_id=ex.id,
                task_type=ex.task_type,
                model=ex.model,
                is_hallucinated=ex.is_hallucinated,
                response_score=float(agg),
                n_sentences=len(scores),
            )
        )

    report = RAGTruthReport(
        benchmark_name=benchmark.name,
        scorer_label=scorer_label,
        aggregation=aggregation,
        records=records,
    )
    report.metrics = compute_metrics(records)
    report.by_task = {
        task: compute_metrics([r for r in records if r.task_type == task])
        for task in sorted({r.task_type for r in records})
    }
    report.by_model = {
        model: compute_metrics([r for r in records if r.model == model])
        for model in sorted({r.model for r in records})
    }
    return report


# --------------------------------------------------------------------------- #
# Metrics
# --------------------------------------------------------------------------- #


def compute_metrics(records: list[RAGTruthRecord]) -> dict[str, float]:
    """Binary-classification metrics treating ``is_hallucinated`` as positive.

    The verifier outputs a *support* score (high = supported). To frame
    this as hallucination detection we set ``y_score = 1 - response_score``
    so high y_score = "model thinks this is hallucinated."

    Returns:
        n: total examples (including errored)
        n_scored: examples that produced a score
        n_hallucinated: gold-positive count
        base_rate: n_hallucinated / n_scored
        auroc: ROC AUC (1.0 = perfect, 0.5 = random)
        auprc: average precision for the positive (hallucinated) class
        f1_best, precision_best, recall_best, threshold_best:
            best-F1 operating point on this exact split (in-sample —
            for real calibration, fit threshold on train and report
            test numbers separately)
    """
    scored = [r for r in records if r.error is None]
    out: dict[str, float] = {
        "n": float(len(records)),
        "n_scored": float(len(scored)),
        "n_errors": float(len(records) - len(scored)),
    }
    if not scored:
        return out

    y_true = [1 if r.is_hallucinated else 0 for r in scored]
    y_score = [1.0 - r.response_score for r in scored]  # positive = hallucinated
    n_pos = sum(y_true)
    out["n_hallucinated"] = float(n_pos)
    out["base_rate"] = n_pos / len(scored)

    # AUROC + AUPRC require both classes present.
    if 0 < n_pos < len(scored):
        from sklearn.metrics import (
            average_precision_score,
            precision_recall_curve,
            roc_auc_score,
        )

        out["auroc"] = float(roc_auc_score(y_true, y_score))
        out["auprc"] = float(average_precision_score(y_true, y_score))

        precision, recall, thresholds = precision_recall_curve(y_true, y_score)
        f1 = [
            2 * p * r / (p + r) if (p + r) > 0 else 0.0
            for p, r in zip(precision, recall, strict=True)
        ]
        # precision_recall_curve returns len(thresholds) = len(precision) - 1
        # (the last point is recall=0, precision=1 with no threshold). Score
        # only the threshold-aligned entries.
        best_idx = max(range(len(thresholds)), key=lambda i: f1[i]) if thresholds.size else 0
        out["f1_best"] = float(f1[best_idx])
        out["precision_best"] = float(precision[best_idx])
        out["recall_best"] = float(recall[best_idx])
        out["threshold_best"] = float(thresholds[best_idx]) if thresholds.size else 0.0

    return out


# --------------------------------------------------------------------------- #
# Internals
# --------------------------------------------------------------------------- #


def _flush_batch(
    scorer: NLIScorer,
    pending_pairs: list[tuple[str, str]],
    pending_lookup: list[tuple[int, int]],
    per_example_scores: list[list[float]],
) -> None:
    scores = scorer.score_pairs(pending_pairs)
    for (ex_idx, s_idx), score in zip(pending_lookup, scores, strict=True):
        per_example_scores[ex_idx][s_idx] = float(score)
    pending_pairs.clear()
    pending_lookup.clear()


def _default_splitter() -> _Splitter:
    """Lazy-import the default sentence splitter so tests don't pay for
    wtpsplit unless they actually run an end-to-end smoke."""
    from verifiable_rag.parsers._sentence_splitter import SentenceSplitter

    return SentenceSplitter()


__all__ = [
    "RAGTruthRecord",
    "RAGTruthReport",
    "compute_metrics",
    "run_ragtruth",
]
