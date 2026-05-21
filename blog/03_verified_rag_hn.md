# HN submission — Blog post #3

## Recommended title (pick one)

- **Open-source NLI ensemble matches Sonnet 4.6 on RAGTruth at 1/250th the cost**
- **Two small NLI models match a frontier LLM judge at hallucination detection**
- **Dual NLI verifier on RAGTruth: AUROC 0.844, calibrated F1 0.706**

The first is most clickable; the second is most HN-tone (claim-stating, no marketing words); the third is what a strict reviewer would want.

## Body (~180 words)

Spent the last week benchmarking faithfulness verifiers on RAGTruth (the canonical 2,700-example RAG hallucination corpus, NAACL 2024) for an open-source library I'm building.

The surprise: a min-aggregation ensemble of HHEM-2.1-open (600M params) and MiniCheck-Flan-T5-Large (770M) hits AUROC 0.844 / calibrated F1 0.706 — statistically indistinguishable from Claude Sonnet 4.6 as a per-claim judge (0.846 / 0.707 on a stratified 300-example subset). Per-call cost ratio is ~250×.

The real story isn't the headline number, it's complementarity. HHEM is great at QA-style entailment (AUROC 0.87) but barely above random on Yelp→narrative data-to-text (0.57). MiniCheck fills exactly that gap (0.70). Neither alone is competitive with the LLM judge; together they keep up.

All thresholds fit on train, applied to held-out test (no in-sample reporting). Honest caveats: Sonnet ran on 300 not 2,700, Haiku-as-judge didn't calibrate well on small train, and FaithBench is currently HF-gated so I can't cross-validate. Eval rigor is the whole moat — methodology holes welcome.

Full write-up: [link to blog/03_verified_rag.md]
Benchmark report (per-task, per-upstream-model, reproducibility): [link to benchmarks/PUBLISHED_ragtruth.md]
Library: [link to github.com/firish/rag-rack]

## Pre-submission checklist

- [ ] Push current branch + blog post to a public URL (your personal blog / Substack / repo's GitHub Pages)
- [ ] Replace the three `[link ...]` placeholders with real URLs
- [ ] Time the submission for Tuesday or Wednesday morning PT (best HN volume + dwell time)
- [ ] Don't use a `Show HN:` prefix — that's for finished products. This is a "I ran a benchmark" technical post.
- [ ] Be ready to answer methodology questions in the comments for the first 2 hours — that's when the post is on the front page or not.

## Likely top HN comments to pre-empt

1. **"Why min aggregation and not mean?"** — Because HALT-RAG (Sept 2025) showed min was strongest on RAGTruth, and my own ablation (in the linked benchmark report) confirms min beats mean by ~0.005 AUROC. Mention this in a reply not the post.
2. **"Sonnet on 300 vs ensemble on 2700 isn't fair."** — Acknowledge: yes, CI is wider on the Sonnet number (±0.045 vs ±0.015). The directional claim ("dual matches Sonnet") is robust; the precise gap is not. Re-running Sonnet on full 2700 is ~$30, deferred unless a reviewer pushes back.
3. **"Why not Bespoke-MiniCheck-7B or Patronus Lynx?"** — Both real candidates, ~10× larger, plausibly stronger. On the roadmap; they'd add another tier to the ensemble. The headline claim ("two small NLI models match a frontier judge") only needs the 600M+770M tier to land.
4. **"This is just HALT-RAG."** — Partially true; the dual-NLI architecture is theirs. My contribution is the open-source library, the publicly reproducible RAGTruth calibration, and the per-task complementarity story (HHEM↔MiniCheck specifically, with cost numbers).

## X / Twitter thread version (5 tweets)

1/ Spent a week benchmarking hallucination verifiers on RAGTruth. The surprise: a 600M + 770M NLI ensemble (HHEM-2.1-open + MiniCheck-Flan-T5-Large, min aggregation) matches Claude Sonnet 4.6 on AUROC and calibrated F1.

At 1/250th the per-call cost.

2/ Headline numbers (train-calibrated, test-only F1, no in-sample peeking):

- Dual NLI: AUROC 0.844, F1 0.706 (n=2700)
- Sonnet judge: AUROC 0.846, F1 0.707 (n=300, stratified)
- Triple (NLI + Sonnet): AUROC 0.861, F1 0.734 (n=300)

3/ The interesting bit is complementarity. HHEM alone is great at QA entailment (AUROC 0.87) but barely above random on Yelp→narrative data-to-text (0.57). MiniCheck fills exactly that gap (0.70). Two models with different blind spots.

4/ This means: don't default to LLM-as-judge for production faithfulness verification. A frozen pair of small NLI models gives you the same quality and no per-call cost after the one-time weight download. Save the LLM judge for offline eval.

5/ Full write-up (per-task, per-upstream-model breakdowns, code, caveats):
[link]

Library (MIT, pre-alpha):
[link to github.com/firish/rag-rack]

Eval rigor is the whole moat — methodology holes welcome.
