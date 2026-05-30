# Calibrate the verifier threshold on your domain

The default thresholds (`HHEMVerifier` 0.3, `DualNLIVerifier` 0.0562) were fit on the RAGTruth train split. They are **not guaranteed to be optimal for your domain**. This guide walks through how to re-fit on your own labeled data.

## When you should recalibrate

| Signal | What it means |
|---|---|
| `unsupported_claims` is empty even on obvious nonsense | Threshold is too low — verifier accepts everything |
| Every answer is refused | Threshold is too high — verifier rejects everything |
| Refusal pattern doesn't match user feedback ("model refused something I'd trust") | Domain mismatch — recalibrate |
| You're scoring on a benchmark different from RAGTruth | Recalibrate for the new distribution |

If the published thresholds are working acceptably on a small test set, leave them. Calibration is for when they're not.

## What you need

A small labeled dataset where each example has:

1. The **context** (source passage)
2. The **response** (model output to verify)
3. A **gold label**: `is_hallucinated: bool`

50–500 labeled examples is usually enough. Stratify by your dominant subtypes (task, domain, response length).

## Step 1: Score the train split

The library's RAGTruth runner accepts any `(NLIScorer, dataset)` pair. The "dataset" is just a collection of `(context, response, is_hallucinated)` examples — you can plug your own in:

```python
from verifiable_rag.eval.ragtruth_runner import run_ragtruth
from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier, MiniCheckVerifier

# Your benchmark — must expose .examples() yielding objects with:
#   id, task_type, model, query, context, response, is_hallucinated
my_train_bench = MyDomainBench(split="train")

scorer = DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier())

report = run_ragtruth(
    scorer,
    my_train_bench,
    scorer_label="dual-nli-my-domain",
    aggregation="min",
)
# Writes records to a JSONL file the calibration script consumes
```

[Reference RAGTruthBench loader →](https://github.com/firish/rag-rack/blob/main/src/verifiable_rag/eval/datasets/ragtruth.py)

## Step 2: Fit the threshold

The `scripts/compute_calibrated_metrics.py` script sweeps a threshold on the train scores, picks the one maximizing F1, then freezes it and reports on test:

```bash
python scripts/compute_calibrated_metrics.py \
    --verifier "DualNLI:my_train_scores.jsonl:my_test_scores.jsonl" \
    --aggregation min \
    --slug dual_calibrated_my_domain
```

The output is a markdown report with:

- The frozen threshold
- The in-sample train F1 (where the threshold was fit)
- The held-out test F1, precision, recall, AUROC (the publishable numbers)
- Per-task / per-model breakdowns

## Step 3: Use the new threshold

Take the frozen threshold from the report and plug it into your verifier:

```python
from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier, MiniCheckVerifier

verifier = DualNLIVerifier(
    HHEMVerifier(),
    MiniCheckVerifier(),
    aggregation="min",
    threshold=0.087,  # ← your calibrated value
)
```

## Common pitfalls

??? warning "Base rate mismatch"
    If your train hallucination base rate is meaningfully different from test (e.g. 60% vs 30%), the F1-optimal threshold can transfer poorly. Two fixes: (1) balance the train data so base rates match, or (2) optimize a different metric — balanced accuracy or fixed-precision at a target — instead of F1.

??? warning "Tiny train sets"
    With <100 train examples, the F1-optimal threshold can be a noisy knife-edge that doesn't generalize. Either collect more data, or use a coarser metric like AUROC and pick the threshold at a fixed operating point (e.g. precision = 0.8).

??? warning "Bimodal score distributions"
    LLM-judge scorers often produce near-binary outputs (0.0 or 1.0). When that happens, the optimal threshold is unstable — any value between 0.0 and 1.0 gives the same F1. For these cases, use `aggregation="mean"` (smoother) or report at a fixed precision.

??? warning "Held-out is small"
    The published RAGTruth threshold is fit on 1500 train and tested on 2700. If your test set has fewer than ~300 positives, treat the calibrated number as exploratory, not publishable. Either grow your eval set or be honest about the CI in your report.

## What the published baseline looks like

The library ships a worked example: [`benchmarks/PUBLISHED_ragtruth.md`](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md) walks through the same calibration flow on RAGTruth, producing:

- Frozen threshold: 0.0562 (Dual NLI, min aggregation)
- Calibrated F1: 0.706 on the 2700-example test split
- AUROC: 0.844 (threshold-independent)

The threshold is calibrated on a 1500-example stratified train slice. The same script (`compute_calibrated_metrics.py`) generates this report — your domain-specific report will have the same shape.

## Going further

- **Sentence-level vs. response-level aggregation:** the library does response-level by default (one score per response). For finer-grained calibration, store per-sentence scores from the runner and aggregate offline. See [`scripts/compute_dual_metrics.py`](https://github.com/firish/rag-rack/blob/main/scripts/compute_dual_metrics.py) for an example of multi-scorer aggregation.
- **Strictness-mode-specific thresholds:** you can calibrate different thresholds for `balanced` (target ~0.5 F1) vs. `strict` (target ~0.8 precision). Wire them with multiple `DualNLIVerifier` instances, one per strictness level.
- **Cross-domain validation:** before deploying a recalibrated threshold, check it doesn't regress on the original RAGTruth test set. If it does, you've overfit to your domain and need to widen your train data.
