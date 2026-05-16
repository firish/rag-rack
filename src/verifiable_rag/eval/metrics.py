"""Sentence-level evaluation metrics.

Tier 1 metrics — set-based (no char-span alignment yet):

* ``citation_set_metrics`` — precision/recall/F1 of predicted vs. gold
  sentence ID sets, per question.
* ``abstention_metrics`` — precision/recall/F1 of refusal decisions across a
  whole benchmark.
* ``aggregate_citation_metrics`` — macro-average citation P/R/F1 over many
  questions.

These are the bare minimum needed to baseline the pipeline. Span tightness
and per-claim attribution come in Tier 2.
"""

from __future__ import annotations

from dataclasses import dataclass

from verifiable_rag.eval import EvalRecord


@dataclass(frozen=True)
class CitationMetrics:
    """Citation quality for one or many questions."""

    precision: float  # of predicted IDs, fraction in the gold set
    recall: float  # of gold IDs, fraction in the predicted set
    f1: float
    span_tightness: float = 0.0  # 0.0 = not measured (Tier 2)


@dataclass(frozen=True)
class AbstentionMetrics:
    """Calibration of the abstention layer."""

    precision: float  # of refusals, fraction that were truly unsupported
    recall: float  # of unsupported questions, fraction that were refused
    f1: float


# --------------------------------------------------------------------------- #
# Per-question primitives
# --------------------------------------------------------------------------- #


def citation_set_metrics(
    predicted_ids: frozenset[str],
    gold_ids: frozenset[str],
) -> CitationMetrics:
    """Precision/recall/F1 over sets of sentence IDs for one question.

    Edge cases:
      * gold_ids empty → precision=1.0 if predicted_ids empty else 0.0; recall=1.0
      * predicted_ids empty + gold_ids non-empty → precision=1.0 (vacuous), recall=0.0
    """
    tp = len(predicted_ids & gold_ids)
    precision = tp / len(predicted_ids) if predicted_ids else 1.0
    recall = tp / len(gold_ids) if gold_ids else 1.0
    f1 = _harmonic_mean(precision, recall)
    return CitationMetrics(precision=precision, recall=recall, f1=f1)


# --------------------------------------------------------------------------- #
# Aggregate metrics
# --------------------------------------------------------------------------- #


def aggregate_citation_metrics(
    pairs: list[tuple[frozenset[str], frozenset[str]]],
) -> CitationMetrics:
    """Macro-average citation precision/recall/F1 across many questions.

    *pairs* is a list of (predicted_ids, gold_ids) tuples. Questions where
    BOTH sets are empty are excluded from the average — they carry no signal.
    """
    scored = [
        citation_set_metrics(pred, gold)
        for pred, gold in pairs
        if pred or gold  # skip vacuous (refused-and-should-refuse) cases
    ]
    if not scored:
        return CitationMetrics(precision=1.0, recall=1.0, f1=1.0)

    n = len(scored)
    avg_p = sum(m.precision for m in scored) / n
    avg_r = sum(m.recall for m in scored) / n
    avg_f = sum(m.f1 for m in scored) / n
    return CitationMetrics(precision=avg_p, recall=avg_r, f1=avg_f)


def abstention_metrics(
    refused: list[bool],
    should_refuse: list[bool],
) -> AbstentionMetrics:
    """Precision/recall/F1 over refusal decisions.

    Positive class = "refused". Treats *refused* and *should_refuse* as
    aligned binary vectors of the same length.
    """
    if len(refused) != len(should_refuse):
        raise ValueError(f"length mismatch: {len(refused)} refused vs. {len(should_refuse)} gold")

    tp = sum(1 for r, g in zip(refused, should_refuse, strict=True) if r and g)
    fp = sum(1 for r, g in zip(refused, should_refuse, strict=True) if r and not g)
    fn = sum(1 for r, g in zip(refused, should_refuse, strict=True) if not r and g)

    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = _harmonic_mean(precision, recall)
    return AbstentionMetrics(precision=precision, recall=recall, f1=f1)


def localization_accuracy(
    pairs: list[tuple[frozenset[str], frozenset[str]]],
) -> float:
    """Fraction of questions where the predicted set is exactly the gold set.

    Strictest possible per-question metric. Useful as a sanity check but
    expect it to be low for the prompted baseline.
    """
    if not pairs:
        return 0.0
    correct = sum(1 for pred, gold in pairs if pred == gold)
    return correct / len(pairs)


def coverage(
    pairs: list[tuple[frozenset[str], frozenset[str]]],
) -> float:
    """Fraction of questions where at least one cited ID is in the gold set.

    Looser than localization_accuracy — captures partial wins. Excludes
    refused-and-should-refuse cases (both sets empty).
    """
    informative = [(p, g) for p, g in pairs if p or g]
    if not informative:
        return 1.0
    hits = sum(1 for pred, gold in informative if pred & gold)
    return hits / len(informative)


# --------------------------------------------------------------------------- #
# End-to-end report scoring
# --------------------------------------------------------------------------- #


def score_records(
    records: list[EvalRecord],
    gold_by_id: dict[str, tuple[frozenset[str], bool]],
) -> dict[str, float]:
    """Compute every Tier 1 metric over a benchmark run.

    *gold_by_id* maps question_id -> (gold_sentence_ids, should_refuse).
    Returns a flat dict of metric_name -> float, ready for markdown rendering.
    """
    pairs: list[tuple[frozenset[str], frozenset[str]]] = []
    refused: list[bool] = []
    should_refuse: list[bool] = []
    errors = 0

    for record in records:
        if record.error is not None:
            errors += 1
            continue
        gold_ids, gold_should_refuse = gold_by_id[record.question_id]
        pairs.append((record.cited_sentence_ids, gold_ids))
        refused.append(record.was_refused)
        should_refuse.append(gold_should_refuse)

    citation = aggregate_citation_metrics(pairs)
    abstention = abstention_metrics(refused, should_refuse)

    return {
        "n_questions": float(len(records)),
        "n_errors": float(errors),
        "citation_precision": citation.precision,
        "citation_recall": citation.recall,
        "citation_f1": citation.f1,
        "coverage": coverage(pairs),
        "localization_accuracy": localization_accuracy(pairs),
        "abstention_precision": abstention.precision,
        "abstention_recall": abstention.recall,
        "abstention_f1": abstention.f1,
    }


# --------------------------------------------------------------------------- #
# Multi-choice scoring (LitQA2-style benchmarks)
# --------------------------------------------------------------------------- #


def multi_choice_selected(
    answer_text: str,
    ideal: str,
    distractors: list[str],
) -> str | None:
    """Pick the multi-choice option the LLM chose from its freeform answer.

    Word-boundary regex match for each option (case-insensitive) so short
    options don't false-match inside other words (e.g. ``"y"`` inside
    ``"answer"``).

    Returns:
        * the ideal/distractor string that matches exactly one option
        * ``None`` if zero or multiple options match (ambiguous / refusal)

    Same general approach PaperQA2 uses for LitQA2 scoring.
    """
    import re as _re

    if not answer_text:
        return None
    lowered = answer_text.lower()
    options = [ideal] + list(distractors)
    matches: list[str] = []
    for opt in options:
        if not opt:
            continue
        pattern = r"\b" + _re.escape(opt.lower()) + r"\b"
        if _re.search(pattern, lowered):
            matches.append(opt)
    if len(matches) == 1:
        return matches[0]
    return None


def multi_choice_accuracy(
    records: list[EvalRecord],
    gold_by_id: dict[str, tuple[str, list[str]]],
) -> dict[str, float]:
    """Score a benchmark with multi-choice gold answers.

    *gold_by_id* maps ``question_id -> (ideal, distractors)``.

    Returns:
        ``{"mc_correct": float, "mc_wrong": float, "mc_unanswered": float,
        "mc_accuracy_over_answered": float, "mc_accuracy_over_all": float,
        "n_questions": float, "n_errors": float}``

    Two accuracy numbers because LitQA2 reports both:
        * "over answered" = correct / (correct + wrong)
        * "over all" = correct / total
    """
    correct = wrong = unanswered = errors = 0
    for r in records:
        if r.error is not None:
            errors += 1
            continue
        if r.question_id not in gold_by_id:
            continue
        ideal, distractors = gold_by_id[r.question_id]
        selected = multi_choice_selected(r.answer_text, ideal, distractors)
        if selected is None:
            unanswered += 1
        elif selected.lower() == ideal.lower():
            correct += 1
        else:
            wrong += 1

    answered = correct + wrong
    total = correct + wrong + unanswered
    return {
        "mc_correct": float(correct),
        "mc_wrong": float(wrong),
        "mc_unanswered": float(unanswered),
        "mc_accuracy_over_answered": correct / answered if answered else 0.0,
        "mc_accuracy_over_all": correct / total if total else 0.0,
        "n_questions": float(len(records)),
        "n_errors": float(errors),
    }


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _harmonic_mean(a: float, b: float) -> float:
    return 2 * a * b / (a + b) if (a + b) else 0.0
