"""Compute train-calibrated RAGTruth metrics for one or more verifiers.

For each verifier you pass a ``LABEL:TRAIN_JSONL:TEST_JSONL`` triple.
The script:

1. Loads each verifier's train + test records (JSONL).
2. Intersects example_ids across verifiers (so per-example scores are
   directly comparable).
3. Combines per-example response_scores via ``min`` / ``mean`` / ``max``
   for ensembles. Single-verifier runs skip this step.
4. Sweeps a single scalar threshold on the **train** intersection to
   maximize F1 → freezes that threshold.
5. Applies the frozen threshold to the **test** intersection → reports
   the publishable calibrated F1 / precision / recall.

Examples
--------
  # Single calibrated
  python scripts/compute_calibrated_metrics.py \\
    --verifier "HHEM:benchmarks/baselines/ragtruth_hhem_train_v1.jsonl:benchmarks/baselines/ragtruth_hhem_v1.jsonl" \\
    --slug ragtruth_hhem_calibrated_v1

  # Dual NLI (HALT-RAG style, default min aggregation)
  python scripts/compute_calibrated_metrics.py \\
    --verifier "HHEM:.../ragtruth_hhem_train_v1.jsonl:.../ragtruth_hhem_v1.jsonl" \\
    --verifier "MiniCheck:.../ragtruth_minicheck_train_v1.jsonl:.../ragtruth_minicheck_v1.jsonl" \\
    --slug ragtruth_dual_calibrated_v1

  # Triple (NLI + LLM-judge — intersection auto-detected, so the
  # smaller Sonnet 300 subset caps the comparison)
  python scripts/compute_calibrated_metrics.py \\
    --verifier "HHEM:...train.jsonl:...test.jsonl" \\
    --verifier "MiniCheck:...train.jsonl:...test.jsonl" \\
    --verifier "Sonnet:...sonnet_train.jsonl:...sonnet_test.jsonl" \\
    --slug ragtruth_triple_calibrated_v1
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from verifiable_rag.eval.ragtruth_runner import RAGTruthRecord, compute_metrics

_OUTPUT_DIR = Path("benchmarks/baselines")
_AGGREGATIONS = ("min", "mean", "max")


@dataclass
class _VerifierSpec:
    label: str
    train_path: Path
    test_path: Path
    train: dict[str, dict]
    test: dict[str, dict]


def _parse_verifier_spec(s: str) -> _VerifierSpec:
    parts = s.split(":", 2)
    if len(parts) != 3:
        raise ValueError(
            f"--verifier expects 'LABEL:TRAIN_JSONL:TEST_JSONL', got {s!r}"
        )
    label, train, test = parts
    train_path, test_path = Path(train), Path(test)
    if not train_path.exists():
        raise FileNotFoundError(f"train JSONL not found: {train_path}")
    if not test_path.exists():
        raise FileNotFoundError(f"test JSONL not found: {test_path}")
    return _VerifierSpec(
        label=label,
        train_path=train_path,
        test_path=test_path,
        train=_load_jsonl(train_path),
        test=_load_jsonl(test_path),
    )


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
    records_by_verifier: list[dict[str, dict]], aggregation: str
) -> dict[str, dict]:
    """Build per-example combined records by aggregating verifier scores.

    Only keeps example_ids present in *all* verifiers' records and with
    no error in any of them.
    """
    if not records_by_verifier:
        return {}
    shared = set.intersection(*[set(r) for r in records_by_verifier])
    out: dict[str, dict] = {}
    for ex_id in shared:
        verifier_recs = [r[ex_id] for r in records_by_verifier]
        if any(r.get("error") for r in verifier_recs):
            continue
        scores = [float(r["response_score"]) for r in verifier_recs]
        if aggregation == "min":
            combined = min(scores)
        elif aggregation == "mean":
            combined = sum(scores) / len(scores)
        elif aggregation == "max":
            combined = max(scores)
        else:
            raise ValueError(f"unknown aggregation {aggregation!r}")
        first = verifier_recs[0]
        out[ex_id] = {
            "example_id": ex_id,
            "task_type": first["task_type"],
            "model": first["model"],
            "is_hallucinated": first["is_hallucinated"],
            "response_score": float(combined),
            "n_sentences": first.get("n_sentences", 0),
        }
    return out


def _records_from_dict(d: dict[str, dict]) -> list[RAGTruthRecord]:
    return [
        RAGTruthRecord(
            example_id=str(v["example_id"]),
            task_type=str(v["task_type"]),
            model=str(v["model"]),
            is_hallucinated=bool(v["is_hallucinated"]),
            response_score=float(v["response_score"]),
            n_sentences=int(v.get("n_sentences", 0)),
        )
        for v in d.values()
    ]


def _fit_threshold(records: list[RAGTruthRecord]) -> tuple[float, float]:
    """Sweep response_score thresholds on these records, return ``(threshold, f1)``.

    Positive class = ``is_hallucinated``. Score is "supported" (high =
    clean), so we flag hallucination when ``response_score < threshold``.
    """
    from sklearn.metrics import precision_recall_curve

    y_true = [1 if r.is_hallucinated else 0 for r in records]
    y_score = [1.0 - r.response_score for r in records]  # high = hallucinated

    n_pos = sum(y_true)
    if n_pos == 0 or n_pos == len(records):
        return 0.5, 0.0

    precision, recall, thresholds = precision_recall_curve(y_true, y_score)
    f1 = [
        2 * p * r / (p + r) if (p + r) > 0 else 0.0
        for p, r in zip(precision, recall, strict=True)
    ]
    if not thresholds.size:
        return 0.5, 0.0
    best_idx = max(range(len(thresholds)), key=lambda i: f1[i])
    # Convert the y_score threshold back to a response_score threshold.
    return float(1.0 - thresholds[best_idx]), float(f1[best_idx])


def _apply_threshold(records: list[RAGTruthRecord], threshold: float) -> dict:
    """Compute calibrated precision/recall/F1 at *threshold*."""
    if not records:
        return {"n": 0.0, "threshold": float(threshold)}
    y_true = [1 if r.is_hallucinated else 0 for r in records]
    y_pred = [1 if r.response_score < threshold else 0 for r in records]
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )
    return {
        "n": float(len(records)),
        "threshold": float(threshold),
        "calibrated_precision": float(precision),
        "calibrated_recall": float(recall),
        "calibrated_f1": float(f1),
    }


def _full_metrics(records: list[RAGTruthRecord], threshold: float) -> dict:
    base = compute_metrics(records)
    base.update(_apply_threshold(records, threshold))
    return base


def _format_md(s: dict, agg: str, label: str) -> str:
    tm = s["test_metrics"]
    n_verifiers = len(s["verifiers"])
    lines = [
        f"# RAGTruth calibrated baseline — {label}",
        "",
        f"- **verifiers:** {', '.join(v['label'] for v in s['verifiers'])}",
    ]
    if n_verifiers > 1:
        lines.append(f"- **aggregation:** {agg}")
    lines += [
        f"- **n_train (intersection):** {s['n_train']}",
        f"- **n_test (intersection):** {s['n_test']}",
        f"- **frozen threshold (from train):** {s['frozen_threshold']:.4f}",
        f"- **train F1 at threshold (in-sample on train):** {s['train_f1_at_threshold']:.4f}",
        "",
        "## Test set metrics — calibrated",
        "",
        "Threshold frozen from train; metrics below are on the held-out test split.",
        "",
        "| metric | value |",
        "|---|---|",
        f"| auroc (threshold-free) | {tm.get('auroc', float('nan')):.4f} |",
        f"| auprc (threshold-free) | {tm.get('auprc', float('nan')):.4f} |",
        f"| **calibrated F1** | **{tm.get('calibrated_f1', float('nan')):.4f}** |",
        f"| calibrated precision | {tm.get('calibrated_precision', float('nan')):.4f} |",
        f"| calibrated recall | {tm.get('calibrated_recall', float('nan')):.4f} |",
        f"| in-sample best F1 (diagnostic only) | {tm.get('f1_best', float('nan')):.4f} |",
        f"| in-sample best threshold (diagnostic) | {tm.get('threshold_best', float('nan')):.4f} |",
        "",
        "## Per task (test-side, calibrated)",
        "",
        "| task | n | auroc | calibrated F1 | precision | recall |",
        "|---|---|---|---|---|---|",
    ]
    for task, m in s["by_task"].items():
        lines.append(
            f"| {task} | {int(m.get('n_scored', 0))} | "
            f"{m.get('auroc', float('nan')):.4f} | "
            f"{m.get('calibrated_f1', float('nan')):.4f} | "
            f"{m.get('calibrated_precision', float('nan')):.4f} | "
            f"{m.get('calibrated_recall', float('nan')):.4f} |"
        )
    lines += [
        "",
        "## Per model (test-side, calibrated)",
        "",
        "| model | n | auroc | calibrated F1 |",
        "|---|---|---|---|",
    ]
    for model, m in s["by_model"].items():
        lines.append(
            f"| {model} | {int(m.get('n_scored', 0))} | "
            f"{m.get('auroc', float('nan')):.4f} | "
            f"{m.get('calibrated_f1', float('nan')):.4f} |"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--verifier",
        action="append",
        required=True,
        help="LABEL:TRAIN_JSONL:TEST_JSONL — repeat for ensemble (2 or 3 verifiers)",
    )
    p.add_argument("--aggregation", choices=_AGGREGATIONS, default="min")
    p.add_argument("--slug", required=True)
    p.add_argument("--output-dir", type=Path, default=_OUTPUT_DIR)
    args = p.parse_args(argv)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.output_dir / f"{args.slug}.md"
    json_path = args.output_dir / f"{args.slug}.json"

    specs = [_parse_verifier_spec(v) for v in args.verifier]
    print(f"[calib] {len(specs)} verifier(s): {[s.label for s in specs]}", flush=True)
    for s in specs:
        print(f"  {s.label}: train={len(s.train)} test={len(s.test)}", flush=True)

    train_combined = _combine([s.train for s in specs], args.aggregation)
    test_combined = _combine([s.test for s in specs], args.aggregation)
    print(f"[calib] train intersection: {len(train_combined)}", flush=True)
    print(f"[calib] test intersection: {len(test_combined)}", flush=True)
    if not train_combined or not test_combined:
        print("[calib] ERROR: empty intersection", file=sys.stderr)
        return 1

    train_records = _records_from_dict(train_combined)
    test_records = _records_from_dict(test_combined)

    threshold, train_f1 = _fit_threshold(train_records)
    print(
        f"[calib] frozen threshold: {threshold:.4f} (train F1={train_f1:.4f})",
        flush=True,
    )

    test_metrics = _full_metrics(test_records, threshold)
    tasks = sorted({r.task_type for r in test_records})
    models = sorted({r.model for r in test_records})
    by_task = {
        t: _full_metrics(
            [r for r in test_records if r.task_type == t], threshold
        )
        for t in tasks
    }
    by_model = {
        m: _full_metrics(
            [r for r in test_records if r.model == m], threshold
        )
        for m in models
    }

    label = " + ".join(s.label for s in specs)
    summary = {
        "label": label,
        "aggregation": args.aggregation,
        "verifiers": [
            {
                "label": s.label,
                "train_path": str(s.train_path),
                "test_path": str(s.test_path),
            }
            for s in specs
        ],
        "n_train": len(train_combined),
        "n_test": len(test_combined),
        "frozen_threshold": threshold,
        "train_f1_at_threshold": train_f1,
        "test_metrics": test_metrics,
        "by_task": by_task,
        "by_model": by_model,
    }
    json_path.write_text(json.dumps(summary, indent=2))
    md = _format_md(summary, args.aggregation, label)
    md_path.write_text(md)
    print(md, flush=True)
    print(f"[calib] wrote {md_path}, {json_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
