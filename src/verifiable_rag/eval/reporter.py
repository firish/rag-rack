"""Render an EvalReport as a markdown document.

Three sections:
  1. Summary — pipeline label, benchmark name, aggregate metrics.
  2. Parser-slice — metrics split by which parser handled each question's
     source PDFs. Catches silent quality regressions when fallback parsers
     activate.
  3. Per-question table — id, refused?, citations vs gold, faithfulness.

Markdown is checked into ``benchmarks/`` so we have a versioned trail of
baseline numbers as we tune the pipeline.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from verifiable_rag.eval import EvalRecord, EvalReport
from verifiable_rag.eval.metrics import score_records


def to_markdown(
    report: EvalReport,
    gold_by_id: dict[str, tuple[frozenset[str], bool]],
    *,
    timestamp: datetime | None = None,
) -> str:
    """Render *report* as a markdown string."""
    ts = (timestamp or datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = []
    lines.append(f"# Eval Report: {report.benchmark_name}")
    lines.append("")
    lines.append(f"- **Pipeline:** `{report.pipeline_label}`")
    lines.append(f"- **Run at:** {ts}")
    lines.append(f"- **Questions:** {int(report.metrics.get('n_questions', 0))}")
    if report.metrics.get("n_errors", 0):
        lines.append(f"- **Errors:** {int(report.metrics['n_errors'])}")
    lines.append("")

    lines.append("## Aggregate metrics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    for key in (
        "citation_precision",
        "citation_recall",
        "citation_f1",
        "coverage",
        "localization_accuracy",
        "abstention_precision",
        "abstention_recall",
        "abstention_f1",
        # LitQA2-only multi-choice metrics
        "mc_correct",
        "mc_wrong",
        "mc_unanswered",
        "mc_accuracy_over_answered",
        "mc_accuracy_over_all",
    ):
        if key in report.metrics:
            lines.append(f"| `{key}` | {report.metrics[key]:.3f} |")
    lines.append("")

    # ---- Parser slice (only useful when at least 2 distinct parsers ran) -
    parser_slice = _parser_slice(report, gold_by_id)
    if parser_slice:
        lines.append("## Parser slice")
        lines.append("")
        lines.append(
            "Metrics split by which parser handled the question's source "
            "PDF(s). A question is counted in a bucket if **any** of its "
            "PDFs were produced by that parser."
        )
        lines.append("")
        # Header
        buckets = sorted(parser_slice)
        header = "| Metric | " + " | ".join(buckets) + " |"
        sep = "|---|" + "|".join("---:" for _ in buckets) + "|"
        lines.append(header)
        lines.append(sep)
        for metric_key in (
            "n",
            "citation_precision",
            "citation_recall",
            "citation_f1",
            "coverage",
            "localization_accuracy",
            "abstention_f1",
        ):
            row = [f"`{metric_key}`"]
            for bucket in buckets:
                val = parser_slice[bucket].get(metric_key)
                row.append(f"{val:.3f}" if val is not None else "—")
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    lines.append("## Per-question results")
    lines.append("")
    lines.append("| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |")
    lines.append("|---|---|---|---|---|---|---|")
    for record in report.records:
        gold_ids, should_refuse = gold_by_id.get(record.question_id, (frozenset(), False))
        intersect = len(record.cited_sentence_ids & gold_ids)
        cited = len(record.cited_sentence_ids)
        gold = len(gold_ids)
        err = f" ⚠️ {record.error}" if record.error else ""
        lines.append(
            f"| `{record.question_id}` | "
            f"{'✓' if record.was_refused else '✗'} | "
            f"{'✓' if should_refuse else '✗'} | "
            f"{intersect} | {cited} | {gold} | "
            f"{record.faithfulness_score:.2f}{err} |"
        )
    lines.append("")

    lines.append("## Per-question answers")
    lines.append("")
    for record in report.records:
        lines.append(f"### `{record.question_id}`")
        if record.error:
            lines.append(f"**Error:** {record.error}")
            lines.append("")
            continue
        if record.was_refused:
            lines.append("_Refused._")
        elif record.cited_sentences:
            # Per-sentence rendering — preserves citation attribution. Each
            # CitedSentence becomes one blockquote line with its inline cites
            # appended in square brackets. Sentences with no cites render
            # without the trailing bracket.
            for text, cites in record.cited_sentences:
                clean = text.strip() or "_(empty)_"
                if cites:
                    cite_str = ", ".join(cites)
                    lines.append(f"> {clean} [{cite_str}]")
                else:
                    lines.append(f"> {clean}")
        else:
            # Backwards-compatible single-blob rendering for old runs
            # whose EvalRecord didn't preserve cited_sentences.
            lines.append(f"> {record.answer_text or '_(empty)_'}")
        if record.cited_sentence_ids:
            lines.append("")
            lines.append(f"Cited: {', '.join(sorted(record.cited_sentence_ids))}")
        lines.append("")

    return "\n".join(lines)


def write_markdown(
    report: EvalReport,
    gold_by_id: dict[str, tuple[frozenset[str], bool]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(to_markdown(report, gold_by_id), encoding="utf-8")


def _parser_slice(
    report: EvalReport,
    gold_by_id: dict[str, tuple[frozenset[str], bool]],
) -> dict[str, dict[str, float | None]]:
    """Return per-parser-bucket metrics, or {} if there's nothing to slice.

    Bucketing rule: a question lands in bucket ``<parser_name>`` if that
    parser handled at least one of its source PDFs. A question with mixed
    parsers (e.g. docling + pymupdf) appears in both buckets.
    """
    if not report.parsers_by_question_id:
        return {}
    parsers_used = {
        p for parsers in report.parsers_by_question_id.values() for p in parsers
    }
    # Only useful if more than one parser actually ran.
    if len(parsers_used) < 2:
        return {}

    records_by_id: dict[str, EvalRecord] = {r.question_id: r for r in report.records}
    out: dict[str, dict[str, float | None]] = {}
    for parser in sorted(parsers_used):
        bucket_records = [
            records_by_id[qid]
            for qid, parsers in report.parsers_by_question_id.items()
            if parser in parsers and qid in records_by_id
        ]
        scored = score_records(bucket_records, gold_by_id)
        scored["n"] = float(len(bucket_records))
        out[parser] = dict(scored)
    return out
