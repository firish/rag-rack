"""Compute response-level Dual-NLI metrics by combining two RAGTruth runs.

Read two JSONL output files (one per verifier), match by example_id,
combine their response_scores via min / mean / max aggregations, then
compute the standard RAGTruth metrics for each dual variant.

This avoids a third Modal run — DualNLI is post-hoc combination of two
already-scored runs.

Caveat: each input JSONL stores the *already-aggregated* response_score
(per-sentence min/mean from each run). True sentence-level dual would
require both runs to store per-sentence scores; that's a backlog
enhancement. The response-level dual implemented here is what most
RAGTruth papers report.

Usage
-----
    python scripts/compute_dual_metrics.py \\
        --a benchmarks/baselines/ragtruth_hhem_v1.jsonl \\
        --b benchmarks/baselines/ragtruth_minicheck_v1.jsonl \\
        --slug ragtruth_dual_hhem_minicheck_v1
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from verifiable_rag.eval.ragtruth_runner import RAGTruthRecord, compute_metrics

_AGGREGATIONS = ("min", "mean", "max")
_OUTPUT_DIR = Path("benchmarks/baselines")


def _load_jsonl(path: Path) -> dict[str, dict]:
    records: dict[str, dict] = {}
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            records[str(obj["example_id"])] = obj
    return records


def _combine(
    a: dict[str, dict], b: dict[str, dict], agg: str
) -> list[RAGTruthRecord]:
    """Pair records by example_id and combine response_scores by *agg*."""
    out: list[RAGTruthRecord] = []
    shared = set(a) & set(b)
    for ex_id in sorted(shared):
        ra, rb = a[ex_id], b[ex_id]
        err = ra.get("error") or rb.get("error")
        if err is not None:
            out.append(
                RAGTruthRecord(
                    example_id=ex_id,
                    task_type=str(ra.get("task_type", "")),
                    model=str(ra.get("model", "")),
                    is_hallucinated=bool(ra.get("is_hallucinated", False)),
                    response_score=0.0,
                    n_sentences=int(ra.get("n_sentences", 0)),
                    error=err,
                )
            )
            continue
        sa = float(ra["response_score"])
        sb = float(rb["response_score"])
        if agg == "min":
            combined = min(sa, sb)
        elif agg == "mean":
            combined = (sa + sb) / 2
        elif agg == "max":
            combined = max(sa, sb)
        else:
            raise ValueError(f"unknown agg {agg!r}")
        out.append(
            RAGTruthRecord(
                example_id=ex_id,
                task_type=str(ra["task_type"]),
                model=str(ra["model"]),
                is_hallucinated=bool(ra["is_hallucinated"]),
                response_score=float(combined),
                n_sentences=int(ra.get("n_sentences", 0)),
            )
        )
    return out


def _format_md(
    label_a: str,
    label_b: str,
    n_a: int,
    n_b: int,
    n_shared: int,
    metrics_by_agg: dict[str, dict],
    by_task_by_agg: dict[str, dict],
    by_model_by_agg: dict[str, dict],
) -> str:
    lines = [
        f"# RAGTruth dual baseline — {label_a} + {label_b}",
        "",
        f"- **A:** {label_a} ({n_a} records)",
        f"- **B:** {label_b} ({n_b} records)",
        f"- **shared example_ids:** {n_shared}",
        "- **method:** response-level dual (combining per-run aggregated scores)",
        "",
        "## Aggregate metrics by dual aggregation",
        "",
        "| aggregation | n | auroc | auprc | f1_best | precision_best | recall_best |",
        "|---|---|---|---|---|---|---|",
    ]
    for agg in _AGGREGATIONS:
        m = metrics_by_agg[agg]
        lines.append(
            f"| {agg} | {int(m.get('n_scored', 0))} | "
            f"{m.get('auroc', float('nan')):.4f} | "
            f"{m.get('auprc', float('nan')):.4f} | "
            f"{m.get('f1_best', float('nan')):.4f} | "
            f"{m.get('precision_best', float('nan')):.4f} | "
            f"{m.get('recall_best', float('nan')):.4f} |"
        )

    lines += ["", "## Per task × aggregation (auroc / f1_best)", "",
              "| task | min | mean | max |", "|---|---|---|---|"]
    tasks = sorted({t for agg in _AGGREGATIONS for t in by_task_by_agg[agg]})
    for task in tasks:
        row = [task]
        for agg in _AGGREGATIONS:
            m = by_task_by_agg[agg].get(task, {})
            row.append(f"{m.get('auroc', float('nan')):.3f} / {m.get('f1_best', float('nan')):.3f}")
        lines.append("| " + " | ".join(row) + " |")

    lines += ["", "## Per model × aggregation (auroc / f1_best)", "",
              "| model | min | mean | max |", "|---|---|---|---|"]
    models = sorted({m for agg in _AGGREGATIONS for m in by_model_by_agg[agg]})
    for model in models:
        row = [model]
        for agg in _AGGREGATIONS:
            m = by_model_by_agg[agg].get(model, {})
            row.append(f"{m.get('auroc', float('nan')):.3f} / {m.get('f1_best', float('nan')):.3f}")
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--a", type=Path, required=True, help="first run's .jsonl")
    p.add_argument("--b", type=Path, required=True, help="second run's .jsonl")
    p.add_argument("--label-a", default=None, help="display label for run A")
    p.add_argument("--label-b", default=None, help="display label for run B")
    p.add_argument("--slug", required=True)
    p.add_argument("--output-dir", type=Path, default=_OUTPUT_DIR)
    args = p.parse_args(argv)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.output_dir / f"{args.slug}.md"
    json_path = args.output_dir / f"{args.slug}.json"
    jsonl_dir = args.output_dir / args.slug
    jsonl_dir.mkdir(exist_ok=True)

    a = _load_jsonl(args.a)
    b = _load_jsonl(args.b)
    n_shared = len(set(a) & set(b))
    print(f"[dual] A={args.a.name}: {len(a)} records", flush=True)
    print(f"[dual] B={args.b.name}: {len(b)} records", flush=True)
    print(f"[dual] shared: {n_shared}", flush=True)
    if n_shared == 0:
        print("[dual] ERROR: no overlapping example_ids", file=sys.stderr)
        return 1

    label_a = args.label_a or args.a.stem
    label_b = args.label_b or args.b.stem

    metrics_by_agg: dict[str, dict] = {}
    by_task_by_agg: dict[str, dict] = {}
    by_model_by_agg: dict[str, dict] = {}
    for agg in _AGGREGATIONS:
        recs = _combine(a, b, agg)
        metrics_by_agg[agg] = compute_metrics(recs)
        by_task_by_agg[agg] = {
            t: compute_metrics([r for r in recs if r.task_type == t])
            for t in sorted({r.task_type for r in recs})
        }
        by_model_by_agg[agg] = {
            m: compute_metrics([r for r in recs if r.model == m])
            for m in sorted({r.model for r in recs})
        }
        # Persist raw combined records per agg
        with (jsonl_dir / f"{agg}.jsonl").open("w") as fh:
            for rec in recs:
                fh.write(json.dumps(asdict(rec)) + "\n")

    summary = _format_md(
        label_a, label_b, len(a), len(b), n_shared,
        metrics_by_agg, by_task_by_agg, by_model_by_agg,
    )
    md_path.write_text(summary)
    json_path.write_text(
        json.dumps(
            {
                "label_a": label_a,
                "label_b": label_b,
                "n_a": len(a),
                "n_b": len(b),
                "n_shared": n_shared,
                "metrics_by_aggregation": metrics_by_agg,
                "by_task_by_aggregation": by_task_by_agg,
                "by_model_by_aggregation": by_model_by_agg,
            },
            indent=2,
        )
    )
    print(summary, flush=True)
    print(f"[dual] wrote {md_path}, {json_path}, {jsonl_dir}/", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
