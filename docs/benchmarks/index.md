# Published benchmark results

Every claim the library makes is backed by a numbered, reproducible benchmark report. The reports under [`benchmarks/`](https://github.com/firish/rag-rack/tree/main/benchmarks) include the headline numbers, per-task and per-model breakdowns, dual-judge cross-validation (where applicable), honest caveats, and one-command reproducibility instructions.

## RAGTruth — hallucination detection

The headline result that drives the library's design. Dual NLI ensemble matches a frontier LLM judge at 1/250× the cost.

| Verifier | n_test | AUROC | Calibrated F1 | Per-call cost |
|---|---|---|---|---|
| HHEM single | 2700 | 0.813 | 0.663 | ~$0.0002 |
| MiniCheck single | 2700 | 0.836 | 0.696 | ~$0.0002 |
| **Dual NLI (HHEM + MC, min)** | 2700 | **0.844** | **0.706** | ~$0.0004 |
| Sonnet 4.6 judge | 300 | 0.846 | 0.707 | ~$0.05 |
| Triple (HHEM + MC + Sonnet) | 300 | 0.861 | 0.734 | ~$0.05 |

**Headline:** the open-source Dual NLI ensemble matches Sonnet 4.6 LLM-judge on AUROC and calibrated F1 — at roughly 1/250th the per-call cost.

[📄 Full report](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_ragtruth.md) · [📝 Blog post](https://github.com/firish/rag-rack/blob/main/blog/03_verified_rag.md)

## ALCE — citation quality

Princeton's citation-quality benchmark. Constrained decoding (ReClaim-style schema-forced output) beats prompted-only citations by 4–7 F1 points under dual-LLM-judge cross-validation.

| Sub-benchmark | Prompted (rec / prec / F1) | Constrained (rec / prec / F1) |
|---|---|---|
| ASQA (Sonnet-judge) | 0.882 / 0.882 / 0.882 | **0.953 / 0.885 / 0.918** |
| QAMPARI (Sonnet-judge) | 0.904 / 0.901 / 0.902 | **0.952 / 0.906 / 0.929** |

**Headline:** schema-forced output is more *judge-robust* — the Haiku→Sonnet score gap is dramatically smaller under constrained (1.6pp ASQA recall) than under prompted (5.2pp). Both judges agree more often when the model is forced to be specific.

Library defaults to `ConstrainedCitedGenerator` based on this result.

[📄 Full report](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_alce.md) · [📝 Blog post](https://github.com/firish/rag-rack/blob/main/blog/02_constrained_citations.md)

## LitQA2 — biomedical scientific Q&A

FutureHouse's 199-question scientific Q&A benchmark. Our 3×2 ablation (3 generators × 2 retrieval configs) finds the bottleneck isn't where you'd expect.

| Generator | MC accuracy | Citation F1 | Localization |
|---|---|---|---|
| Prompted | 0.897 | 0.463 | 0.241 |
| **Constrained** | **0.966** | 0.466 | 0.207 |
| SAFE | 0.966 | 0.475 | 0.207 |

**Headline:** constrained decoding is the lever (+6.9pp MC on pilot slice, +0.5pp full corpus). **Contextual retrieval is a null result** — adding section-level CR moved no metric in either generator config. The localization metric is benchmark-imposed at ~0.21, not generator-imposed (SAFE, designed for localization, doesn't lift it).

[📄 Full report](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_litqa2.md) · [📝 Blog post](https://github.com/firish/rag-rack/blob/main/blog/04_litqa2_ablation.md)

---

## Methodology notes shared across reports

All three benchmark reports follow the same discipline:

1. **Train/test split** — thresholds and aggregation choices are fit on a held-out train slice, then *frozen* and applied to test. In-sample best metrics are reported only as a diagnostic.
2. **Reproducibility** — every report ends with a "Reproducibility" section containing the exact CLI command(s) to recreate the headline number from a fresh checkout.
3. **Dual-judge cross-validation** (where LLM judges are used) — the same outputs are scored by two independent models to spot judge-generosity artifacts.
4. **Honest caveats** — each report lists what *isn't* validated, what would strengthen the result, and what we deferred to backlog.

We welcome methodology critiques. Eval rigor is the whole moat; the only way to find the holes is to invite people to look for them.
