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


import re as _re
import unicodedata as _unicodedata

_BOLD_RE = _re.compile(r"\*\*([^*\n]+?)\*\*")
_TRAILING_PUNCT_RE = _re.compile(r"[\.,;:!\?\s]+$")

# Phrasings the LLM commonly wraps around its actual answer when it bolds
# the *whole sentence* instead of just the option, e.g.
# "**The best answer is: K548R**". Stripped greedily, longest first.
_ANSWER_PREFIXES = (
    "the best answer is:",
    "best answer is:",
    "the answer is:",
    "best answer:",
    "answer:",
)

# Fuzzy-match threshold: only accept a bold→option rescue when rapidfuzz's
# normalized similarity is at least this high. 90 is conservative enough to
# avoid false matches between distinct distractors (typical inter-distractor
# similarity is far below 90 in benchmark sets) but tolerant of single-char
# typos in long strings.
_FUZZY_THRESHOLD = 90.0


def _normalize_option(s: str) -> str:
    """Lowercase, strip whitespace, strip trailing punctuation."""
    return _TRAILING_PUNCT_RE.sub("", s.strip().lower())


def _strip_answer_prefix(norm: str) -> str | None:
    """If *norm* starts with a known "Answer:" preamble, return the suffix.

    Returns ``None`` if no preamble matches, so callers can distinguish
    "no rewrite happened" from "rewrite produced an empty string".
    """
    for prefix in _ANSWER_PREFIXES:
        if norm.startswith(prefix):
            return norm[len(prefix):].strip()
    return None


def _nfkd_normalize(s: str) -> str:
    """Unicode-normalize for symbol-equivalence matching.

    Decomposes via NFKD (handles superscripts like ``⁻¹`` → ``-1``, fraction
    forms, ligatures). NFKD does NOT collapse the math minus ``U+2212`` to
    an ASCII hyphen — that's a separate codepoint semantically — so we map
    it (and the multiplication sign) explicitly. The output is then run
    through ``_normalize_option`` for lowercasing + punctuation stripping.
    """
    decomposed = _unicodedata.normalize("NFKD", s)
    decomposed = decomposed.replace("−", "-").replace("×", "x")
    return _normalize_option(decomposed)


def _fuzzy_pick(text: str, options: list[str], threshold: float) -> str | None:
    """Return the unique option whose normalized fuzzy similarity to *text*
    meets *threshold*. ``None`` if zero or >1 options qualify.

    rapidfuzz is an optional dependency; falls back to no-op if missing so
    the metric still works in stripped-down environments.
    """
    try:
        from rapidfuzz import fuzz
    except ImportError:
        return None
    norm_text = _nfkd_normalize(text)
    qualifying: list[tuple[str, float]] = []
    for opt in options:
        if not opt:
            continue
        score = fuzz.ratio(_nfkd_normalize(opt), norm_text)
        if score >= threshold:
            qualifying.append((opt, score))
    if len(qualifying) == 1:
        return qualifying[0][0]
    return None


def _resolve_bold(bold_str: str, options: list[str]) -> str | None:
    """Map a bolded answer to one of *options*, trying progressively looser
    matchers. Returns the matched option string, or ``None``.

    Match order (each falls through to the next on miss):
      1. Direct normalized exact match.
      2. Prefix-strip ("Answer: X" → "X") then exact match.
      3. NFKD Unicode normalization (handles ``⁻¹``, ``×``, U+2212) then 1+2.
      4. Fuzzy match at ``_FUZZY_THRESHOLD`` — guarded by uniqueness so
         distinct distractors can't both qualify.
    """
    norm_to_opt = {_normalize_option(opt): opt for opt in options if opt}
    nfkd_to_opt = {_nfkd_normalize(opt): opt for opt in options if opt}

    norm = _normalize_option(bold_str)
    if norm in norm_to_opt:
        return norm_to_opt[norm]

    stripped = _strip_answer_prefix(norm)
    if stripped is not None and stripped in norm_to_opt:
        return norm_to_opt[stripped]

    nfkd = _nfkd_normalize(bold_str)
    if nfkd in nfkd_to_opt:
        return nfkd_to_opt[nfkd]
    nfkd_stripped = _strip_answer_prefix(nfkd)
    if nfkd_stripped is not None and nfkd_stripped in nfkd_to_opt:
        return nfkd_to_opt[nfkd_stripped]

    # Fuzzy fallback — try the stripped bold first (drops the "Answer:"
    # preamble before comparing), then the raw bold. Either may produce a
    # unique hit; if both produce hits and they agree, fine. If they
    # disagree, treat as ambiguous and return None.
    fuzzy_candidates: list[str] = []
    candidate_strs = [bold_str]
    if stripped is not None:
        candidate_strs.append(stripped)
    elif nfkd_stripped is not None:
        candidate_strs.append(nfkd_stripped)
    for cand in candidate_strs:
        picked = _fuzzy_pick(cand, options, _FUZZY_THRESHOLD)
        if picked is not None and picked not in fuzzy_candidates:
            fuzzy_candidates.append(picked)
    if len(fuzzy_candidates) == 1:
        return fuzzy_candidates[0]
    return None


def _relaxed_match(option: str, text: str) -> bool:
    """Substring match for ``option`` in ``text`` with non-alphanumeric boundaries.

    Tolerates options ending (or starting) in non-word chars such as ``%``,
    ``-``, or pure digits — cases where ``\\b...\\b`` mishandles boundaries
    (``\\b80%\\b`` fails because ``%`` is non-word and so is the char that
    typically follows it). Case-insensitive.
    """
    pat = r"(?<![A-Za-z0-9])" + _re.escape(option) + r"(?![A-Za-z0-9])"
    return bool(_re.search(pat, text, flags=_re.IGNORECASE))


def multi_choice_selected(
    answer_text: str,
    ideal: str,
    distractors: list[str],
) -> str | None:
    """Pick the multi-choice option the LLM chose from its freeform answer.

    Two-tier strategy:

    1. **Bold extraction.** Find ``**X**`` markdown-bold spans and try to map
       each to an option via :func:`_resolve_bold`, which walks: exact match
       → prefix-strip ("Answer: K548R" → "K548R") → Unicode NFKD normalize
       (``⁻¹`` → ``-1``) → guarded fuzzy match. If exactly one bold maps,
       return it. If multiple bolds map to different options (LLM walked
       through reasoning before settling), return the **last** map —
       empirically the LLM's chosen answer.

    2. **Relaxed substring fallback.** If no bolds resolved, fall back to
       case-insensitive substring matching with non-alphanumeric boundaries
       (handles options ending in ``%``, ``-``, digits, etc., which the
       traditional ``\\b`` form mishandles). Returns the unique hit, or
       ``None`` if zero / multiple options match.

    Returns:
        * the ideal/distractor string that matches
        * ``None`` if no signal can be extracted (counts as unanswered)
    """
    if not answer_text:
        return None

    options = [ideal] + list(distractors)

    # --- Tier 1: bold extraction --------------------------------------------
    bold_picks: list[str] = []
    last_bold_pick: str | None = None
    for m in _BOLD_RE.finditer(answer_text):
        opt = _resolve_bold(m.group(1), options)
        if opt is not None:
            last_bold_pick = opt
            if opt not in bold_picks:
                bold_picks.append(opt)
    if len(bold_picks) == 1:
        return bold_picks[0]
    if len(bold_picks) > 1:
        return last_bold_pick

    # --- Tier 2: relaxed substring match ------------------------------------
    hits = [opt for opt in options if opt and _relaxed_match(opt, answer_text)]
    if len(hits) == 1:
        return hits[0]
    return None


_REFUSAL_STYLE_IDEAL_PREFIXES = ("insufficient", "not enough", "cannot determine")


def _is_refusal_style_ideal(ideal: str) -> bool:
    """Return True if *ideal* signals "the right answer is to refuse".

    Mirrors :func:`LitQA2Bench._is_refusal_answer`. Some LitQA2 rows use
    ``"null"`` as the literal ideal for genuinely unanswerable questions;
    others use ``"Insufficient information to answer"``. Both mean the
    same thing for MC scoring: the model is correct iff it refused (or
    explicitly picked the "Insufficient information" option).
    """
    lowered = ideal.lower().strip()
    if lowered == "null":
        return True
    return any(lowered.startswith(p) for p in _REFUSAL_STYLE_IDEAL_PREFIXES)


def _answer_is_refusal(answer_text: str) -> bool:
    """True if the answer is empty OR explicitly refuses with a known phrase.

    The pipeline collapses LLM refusals (matching ``_REFUSAL_PATTERNS``) to
    an empty ``answer.text`` — but post-hoc rescoring from a saved report
    sometimes has the raw "Insufficient information to answer" text intact,
    so we check both forms.
    """
    if not answer_text:
        return True
    lowered = answer_text.lower()
    # Local copy of the phrases (avoid a circular import from the generator
    # package). Keep in sync with prompted._REFUSAL_PATTERNS.
    refusal_phrases = (
        "i cannot answer",
        "i can't answer",
        "i do not have enough information",
        "i don't have enough information",
        "the sources do not contain",
        "the provided sources do not",
        "the sources do not mention",
        "the sources do not discuss",
        "the sources do not address",
        "the sources do not provide",
        "insufficient information to answer",
    )
    return any(p in lowered for p in refusal_phrases)


def multi_choice_accuracy(
    records: list[EvalRecord],
    gold_by_id: dict[str, tuple[str, list[str]]],
) -> dict[str, float]:
    """Score a benchmark with multi-choice gold answers.

    *gold_by_id* maps ``question_id -> (ideal, distractors)``.

    Refusal-style ideals (``"null"``, ``"Insufficient information to
    answer"``, etc.) get special treatment: the question is **correct**
    iff the pipeline refused or the LLM picked the "Insufficient
    information" option, **wrong** if the LLM committed to any actual
    distractor.

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

        # Refusal-style ideal: the right answer is "I can't answer."
        if _is_refusal_style_ideal(ideal):
            if _answer_is_refusal(r.answer_text):
                correct += 1
                continue
            # LLM committed to something — see whether it picked a distractor
            # (wrong) or produced ambiguous prose (unanswered).
            selected = multi_choice_selected(r.answer_text, ideal, distractors)
            if selected is None:
                unanswered += 1
            else:
                wrong += 1
            continue

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
