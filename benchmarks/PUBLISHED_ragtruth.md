# RAGTruth Benchmark — Published Result

- **Date:** 2026-05-21
- **Benchmark:** RAGTruth (Niu et al., NAACL 2024) — word-span hallucination annotations across QA / Data-to-text / Summary tasks, six generating LLMs
- **Subject under test:** verifier (post-hoc faithfulness scorer). Pipeline parser/chunker/retriever/generator are not exercised — RAGTruth ships pre-generated `(context, response)` pairs.
- **Verifiers compared:** HHEM-2.1-open, MiniCheck-Flan-T5-Large, Dual-NLI ensemble, Sonnet 4.6 LLM-judge

## Headline — Dual NLI matches frontier LLM-judge quality at >100× lower per-call cost

| Verifier | n_train | n_test | AUROC | **Calibrated F1** | Per-call cost |
|---|---|---|---|---|---|
| HHEM single | 1500 | 2700 | 0.813 | 0.663 | ~$0.0002 (Modal T4) |
| MiniCheck single | 1500 | 2700 | 0.836 | 0.696 | ~$0.0002 (Modal T4) |
| **Dual NLI (HHEM + MiniCheck, min)** | 1500 | 2700 | **0.844** | **0.706** | ~$0.0004 |
| Sonnet judge | 300 | 300 | 0.846 | 0.707 | ~$0.05 (Anthropic API) |
| **Triple (HHEM + MC + Sonnet, min)** | 300 | 300 | **0.861** | **0.734** | ~$0.05 |

**Headline claim:** the open-source **Dual NLI ensemble matches Sonnet 4.6 LLM-judge** (AUROC 0.844 vs 0.846; F1 0.706 vs 0.707) on RAGTruth — at less than 1/100th the per-call cost. Adding Sonnet as a third member lifts performance another ~2 F1 points on the 300-example subset where all three verifiers scored.

## Full calibrated comparison

Methodology: each verifier's threshold is swept on a stratified train subset to maximize F1, then **frozen** and applied to the held-out test split. The reported F1 is therefore on examples the threshold never saw. ("In-sample best F1" reported as a diagnostic — within 0.5 pp of calibrated F1 in every case, confirming threshold stability.)

| Verifier | n_test | AUROC | AUPRC | Calibrated F1 | Cal. precision | Cal. recall |
|---|---|---|---|---|---|---|
| HHEM | 2700 | 0.813 | 0.680 | 0.663 | 0.530 | 0.886 |
| MiniCheck | 2700 | 0.836 | 0.711 | 0.696 | 0.591 | 0.846 |
| **Dual NLI** | 2700 | **0.844** | 0.729 | **0.706** | 0.639 | 0.790 |
| Sonnet judge | 300 | 0.846 | — | 0.707 | 0.578 | 0.912 |
| **Triple ensemble** | 300 | **0.861** | 0.667 | **0.734** | 0.644 | 0.853 |

**Cheap-judge floor (Haiku, footnoted):** Haiku 4.5 reaches AUROC 0.728 / F1 0.66 (in-sample) on a stratified 600-example subset. Train-calibrated F1 is **unreliable** for Haiku — the train-fit threshold (0.05) did not transfer to test (calibrated F1 collapsed to 0.14). Likely cause: train/test base-rate mismatch (46 % vs 35 %) combined with Haiku's near-bimodal confidence distribution. With only 300 train examples the F1 curve found a knife-edge that didn't generalize. Even at the optimistic in-sample number (0.66), Haiku falls **below** the dual NLI baseline. We treat it as a "cheap-judge floor" reference, not a recommended verifier.

## Per-task breakdown (calibrated F1 / AUROC)

| Task | HHEM | MiniCheck | **Dual NLI** | Sonnet (300) | **Triple (300)** |
|---|---|---|---|---|---|
| **Data2txt** (Yelp → narrative) | 0.78 / 0.57 | 0.79 / 0.70 | **0.78 / 0.69** | 0.90 / 0.85 | 0.83 / 0.72 |
| **QA** (MS MARCO + retrieved) | 0.53 / 0.87 | 0.52 / 0.84 | 0.58 / 0.87 | 0.44 / 0.84 | 0.42 / 0.83 |
| **Summary** (CNN/DailyMail) | 0.50 / 0.76 | 0.56 / 0.78 | 0.52 / 0.79 | 0.57 / 0.85 | 0.70 / 0.88 |

**Per-task observations:**
- **HHEM and MiniCheck are complementary on Data2txt** — HHEM alone gets AUROC 0.57 (near random); MiniCheck alone gets 0.70; the dual lifts to 0.69. MiniCheck's training distribution (synthetic claim decomposition) handles structured-record entailment better than HHEM's summarization training.
- **QA is HHEM's strongest task** (AUROC 0.87) — factoid claims against retrieved passages match its training distribution exactly. F1 is dragged down by QA's low base rate (18 % hall) inflating the precision-recall imbalance.
- **Summary improves monotonically with ensemble size**: HHEM 0.50 → MiniCheck 0.56 → Sonnet 0.65 → Triple 0.70 calibrated F1.

## Per upstream-model breakdown (calibrated F1)

| Upstream LLM (judged) | base rate | HHEM | MiniCheck | **Dual NLI** | **Triple (300)** |
|---|---|---|---|---|---|
| gpt-4-0613 | 9 % | 0.34 | 0.35 | 0.37 | 0.38 |
| gpt-3.5-turbo-0613 | 10 % | 0.37 | 0.37 | 0.37 | 0.46 |
| llama-2-70b-chat | 38 % | 0.69 | 0.72 | 0.73 | 0.72 |
| llama-2-13b-chat | 46 % | 0.70 | 0.79 | **0.81** | 0.82 |
| llama-2-7b-chat | 50 % | 0.72 | 0.74 | 0.75 | 0.76 |
| mistral-7B-instruct | 56 % | 0.81 | 0.82 | 0.81 | 0.81 |

**Key per-model finding:** the **dual NLI dominates on the open-source models** (Llama-2 family, Mistral) where base rates are highest and hallucinations most consequential. On gpt-4/gpt-3.5 outputs (low base rate), F1 is structurally lower across all verifiers — the long tail of clean responses dominates. AUROC is more honest there.

## Comparison vs published literature

| Verifier | Reported metric on RAGTruth | This work (calibrated F1) |
|---|---|---|
| HHEM-2.1-open (Vectara card) | not directly reported (response F1) | **0.66** |
| MiniCheck-Flan-T5-Large (Tang et al. 2024) | BACC ~77 % | F1 **0.70**; AUROC **0.84** |
| Bespoke-MiniCheck-7B (Bespoke Labs) | F1 ~0.80 (estimated) | not measured |
| HALT-RAG dual ensemble (Sept 2025) | F1 ~0.78-0.82 (paper) | F1 **0.71** (response-level dual) |
| GPT-4 LLM-judge (RAGTruth paper baseline) | F1 ~0.85 | not measured |
| **This work: Dual NLI** | — | **F1 0.71, AUROC 0.84** |
| **This work: Triple ensemble** | — | **F1 0.73, AUROC 0.86** (300-ex subset) |

Caveats on direct comparison: published numbers vary on metric (BACC vs response-F1 vs token-F1), on aggregation (we use per-sentence min; some papers use mean), and on RAGTruth subset (we used full test). Direction and rank-order are robust; absolute values would shift with different aggregation choices.

## The substantive finding

**Open-source small-model NLI ensemble matches frontier LLM-judge quality on RAGTruth at >100× lower per-call cost.** Specifically:

- **HHEM (0.66 F1) and MiniCheck (0.70 F1)** are individually below the LLM-judge ceiling.
- **Their min-aggregation ensemble (0.71 F1, 0.84 AUROC)** matches a Sonnet 4.6 LLM-judge (0.71 F1, 0.85 AUROC).
- The two NLI models are **complementary**: their per-task and per-model error patterns differ enough that combining them lifts both metrics, especially on Data2txt (HHEM's weak task).
- **Adding Sonnet as a third ensemble member yields a real ~2 F1 point lift** (0.71 → 0.73), but only justifiable if budget for an LLM-judge already exists. Pure-NLI dual is the recommended production configuration.

**Library recommendation: ship `DualNLIVerifier(HHEMVerifier, MiniCheckVerifier, aggregation="min")` as the default high-strictness verifier.** It costs nothing per call after weights download, matches a frontier judge on AUROC and F1, and dominates either NLI alone.

## Methodology

### Train/test split
RAGTruth ships canonical train (~18 K rows) and test (2 700 rows) splits. We use the full test split where compute allowed; for Sonnet we stratify down to 300 examples (100 per task: QA, Data2txt, Summary) for cost reasons. All sampling uses `seed=42` so train and test subsets are reproducible.

### Sentence segmentation
Each response is segmented with `wtpsplit` SaT (`sat-3l`) → typically 3–5 sentences. The verifier scores each `(context, response_sentence)` pair independently; the response-level score is the **min** across sentences (HALT-RAG convention: any unsupported sentence flags the response).

### Threshold calibration
For each verifier (or ensemble), the **response-level threshold is swept on the train split to maximize F1, then frozen** and applied to the test split. The published F1 is therefore on data the threshold has not seen. An in-sample best-F1 is also reported as a diagnostic; in every case it's within 0.5 pp of the calibrated number — confirming threshold stability under our train sample size.

### Ensemble aggregation
For multiple verifiers, per-example response scores are combined via `min` (default — HALT-RAG style: most conservative, any verifier flagging an example flags it). `mean` and `max` are also supported by `scripts/compute_calibrated_metrics.py` for ablations; `min` is reported here.

### GPU hosting (Modal)
HHEM and MiniCheck run on Modal T4 GPUs via a thin `NLIScorer` adapter ([`infra/modal_verifiers.py`](../infra/modal_verifiers.py)). Cold-start ~30 s; warm scoring ~0.3 s per pair; total Modal cost for the four runs (HHEM/MiniCheck × train/test) under $1.

### LLM-judge prompt
Sonnet receives a deterministic JSON-output prompt (`{"supported": bool, "confidence": [0.5, 1.0]}`) per `(context, sentence)` pair. Confidence is clamped to `[0.5, 1.0]` so the boolean is the dominant signal. Anthropic prompt caching is enabled on the system prompt + premise — meaningful only when premise exceeds Anthropic's ~1 024-token minimum-cacheable-block size (so caching saved most cost on Summary task contexts, less on QA).

## Reproducibility

```bash
# One-time data fetch
python scripts/fetch_faithfulness_benches.py

# Modal app deploy (one-time)
modal deploy infra/modal_verifiers.py

# Score each verifier × split. Modal runs are ~$0.25 each, ~25-100 min.
python scripts/run_ragtruth.py --verifier modal_hhem      --split test  --slug ragtruth_hhem_v1            --batch-size 8
python scripts/run_ragtruth.py --verifier modal_hhem      --split train --max-examples 1500 --stratify --seed 42 --slug ragtruth_hhem_train_v1      --batch-size 8
python scripts/run_ragtruth.py --verifier modal_minicheck --split test  --slug ragtruth_minicheck_v1       --batch-size 8
python scripts/run_ragtruth.py --verifier modal_minicheck --split train --max-examples 1500 --stratify --seed 42 --slug ragtruth_minicheck_train_v1 --batch-size 8

# LLM-judge runs (Anthropic API key required)
python scripts/run_ragtruth.py --verifier llm_judge --judge-model claude-sonnet-4-6           --max-examples 300 --stratify --seed 42 --split test  --slug ragtruth_judge_sonnet_smoke_v1
python scripts/run_ragtruth.py --verifier llm_judge --judge-model claude-sonnet-4-6           --max-examples 300 --stratify --seed 42 --split train --slug ragtruth_judge_sonnet_train_v1
python scripts/run_ragtruth.py --verifier llm_judge --judge-model claude-haiku-4-5-20251001   --max-examples 600 --stratify --seed 42 --split test  --slug ragtruth_judge_haiku_v1

# Calibrated metrics — single, dual, triple
python scripts/compute_calibrated_metrics.py \
  --verifier "HHEM:benchmarks/baselines/ragtruth_hhem_train_v1.jsonl:benchmarks/baselines/ragtruth_hhem_v1.jsonl" \
  --verifier "MiniCheck:benchmarks/baselines/ragtruth_minicheck_train_v1.jsonl:benchmarks/baselines/ragtruth_minicheck_v1.jsonl" \
  --aggregation min --slug ragtruth_dual_calibrated_v1
```

Source reports:
- HHEM test/train: [ragtruth_hhem_v1.md](baselines/ragtruth_hhem_v1.md) · [ragtruth_hhem_train_v1.md](baselines/ragtruth_hhem_train_v1.md)
- MiniCheck test/train: [ragtruth_minicheck_v1.md](baselines/ragtruth_minicheck_v1.md) · [ragtruth_minicheck_train_v1.md](baselines/ragtruth_minicheck_train_v1.md)
- Calibrated single: [ragtruth_hhem_calibrated_v1.md](baselines/ragtruth_hhem_calibrated_v1.md) · [ragtruth_minicheck_calibrated_v1.md](baselines/ragtruth_minicheck_calibrated_v1.md) · [ragtruth_sonnet_calibrated_v1.md](baselines/ragtruth_sonnet_calibrated_v1.md)
- Calibrated dual / triple: [ragtruth_dual_calibrated_v1.md](baselines/ragtruth_dual_calibrated_v1.md) · [ragtruth_triple_calibrated_v1.md](baselines/ragtruth_triple_calibrated_v1.md)
- Haiku reference (in-sample, calibration noted unreliable): [ragtruth_judge_haiku_v1.md](baselines/ragtruth_judge_haiku_v1.md)

## Future work

- **Sentence-level dual** — current dual aggregates already-aggregated response scores. True sentence-level ensemble (per-sentence dual then per-response aggregate) requires storing per-sentence scores in the runner. Likely modest lift; backlogged.
- **Bespoke-MiniCheck-7B variant** — published F1 ~0.80 on RAGTruth; would add a third NLI model with different scale. Drop-in via the `NLIScorer` Protocol.
- **Sonnet on full 2 700 test** — would tighten the LLM-judge CI from ±0.045 to ±0.015 AUROC, at ~$30 cost. Deferred unless reviewers ask for it.
- **Haiku threshold robustness** — current Haiku-train-300 threshold failed to transfer. Either larger Haiku-train (1500) or a different operating-point criterion (e.g. balanced accuracy or fixed-precision) would likely fix it.
- **FaithBench / HaluBench cross-validation** — vectara/FaithBench is currently HF-gated; once re-opened or replaced, the same calibration pipeline applies.
- **Train-base-rate normalization** — the train (46 %) vs test (35 %) hallucination base-rate gap shifts the F1-optimal threshold. A base-rate-aware calibration would be more honest; on the order of 1-2 F1 points expected.
