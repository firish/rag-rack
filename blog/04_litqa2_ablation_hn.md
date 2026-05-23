# HN submission — Blog post #4 (LitQA2 ablation)

## Recommended title (pick one)

- **A LitQA2 ablation: contextual retrieval doesn't help, constrained decoding does**
- **Five SOTA RAG techniques on LitQA2 — what moved the needle and what didn't**
- **Where the localization ceiling actually is: a 3×2 generator/retrieval ablation on LitQA2**

First is the cleanest "I ran a benchmark" framing. Second hooks the SOTA-curious crowd. Third is for the audience who'd recognize the metric.

## Body (~210 words)

I ran a 3×2 ablation on LitQA2 (FutureHouse's 199-question biomedical scientific Q&A benchmark) to find where the headroom past my 0.870 baseline actually is. Three generators (prompted / constrained / SAFE) × two retrieval configs (no contextual / section-level Contextual Retrieval). Results on a 29-question stratified slice:

- **Contextual Retrieval is a null result.** Bit-identical metrics across both generator backbones — MC, citation_precision, citation_recall, coverage, localization, all unchanged. The hybrid retriever (BM25 + Cohere embed + Cohere rerank) was already saturating; LLM-written context preambles disappeared in the noise.
- **Constrained decoding lifts MC by 6.9 pp on this slice** (0.897 → 0.966; the full-corpus delta is +0.5 pp per the published v9→v11 comparison). Schema-forced output commits the model on borderline cases instead of letting it bail with "insufficient information."
- **SAFE matches constrained on MC and beats it on citation_f1**, but doesn't move localization (0.207 either way). SAFE was *designed* to lift localization. The most likely interpretation: LitQA2's sentence-level scoring rewards single-cite output even when multi-cite is more informative. **The localization ceiling is benchmark-imposed, not generator-imposed.**

Caveats: 29-question pilot, not 199. Direction transfers; absolute numbers don't. Cohere-rerank in the loop. All scoring with Claude Haiku 4.5 as the generator.

Full write-up: [link to blog/04_litqa2_ablation.md]
Benchmark report: [link to benchmarks/PUBLISHED_litqa2.md]
Library (MIT, pre-alpha): [link to github.com/firish/rag-rack]

## Pre-submission checklist

- [ ] Push current branch + blog post to a public URL
- [ ] Replace the three `[link ...]` placeholders with real URLs
- [ ] Time submission for Tuesday or Wednesday morning PT
- [ ] Don't use `Show HN:` — this is a benchmark write-up, not a product launch
- [ ] Be ready for 2 hours of comment-tending; that's when it lives or dies

## Likely top HN comments to pre-empt

1. **"29 questions is a tiny sample."** Acknowledged in the post — it's a *pilot* designed to answer "is there meaningful direction?" not "what's the precise number?" The 2×2 retrieval ablation was bit-identical between cells, which is a stronger null signal than a noisy 0.005 delta would be. Full-corpus CR run is on the backlog if reviewers want it (~$15, ~3 hours).

2. **"You're attacking a strawman — published Contextual Retrieval results were on a different stack."** True; Anthropic's published CR results were against a baseline that wasn't already running Cohere rerank. The finding here is *conditional*: "CR's marginal value disappears when your retrieval stack is already saturating on this benchmark." That's a meaningful operational claim even if not a universal one.

3. **"Why didn't you try chunk-level CR (Anthropic's original recipe) instead of section-level?"** Cost. Chunk-level CR on full LitQA2 would have been ~$300 vs ~$15 for section-level. Given the bit-identical null on section-level, scaling up to per-chunk for a marginal effect isn't EV-positive — but I'd be open to running it if multiple people request.

4. **"Your localization ceiling claim is a hypothesis, not a measurement."** Fair — the claim is *interpreted* from three generators all hitting the same number, not *measured* against a known-perfect baseline. Stronger evidence would be a synthetic dataset with sentence-precise gold to show metric saturation. Backlog.

5. **"SAFE on a benchmark not designed for SAFE isn't a real test."** Agreed — SAFE's natural home is RAGTruth or FaithBench (atomic-claim-level gold). The LitQA2 result is "even the SOTA atomic-claim recipe can't move LitQA2's localization metric," which is interesting *as* a benchmark-limits finding, not a generator-architecture finding.

## X / Twitter thread version (5 tweets)

1/ Ran a 3×2 ablation on LitQA2 (199-question biomedical Q&A) to find where the headroom past my 0.870 baseline is. Three generators (prompted/constrained/SAFE) × two retrieval configs (no CR / section-level Contextual Retrieval).

Some surprises.

2/ Contextual Retrieval is a *null result* on this benchmark. Bit-identical metrics across both generator backbones — MC, citation precision, citation recall, coverage, localization. All unchanged.

If your hybrid retriever (BM25 + dense + rerank) is saturating, CR adds nothing.

3/ Constrained decoding (ReClaim-style schema-forced output) lifts MC by 6.9 pp on the pilot slice (full-corpus delta is +0.5 pp).

Schema commits the model on borderline cases instead of letting it bail with "insufficient information."

4/ SAFE matches constrained on MC, edges it on citation_f1 — but doesn't move localization (0.21 either way).

SAFE was *designed* for localization. If it doesn't help on this metric, the ceiling is benchmark-imposed (sentence-level gold rewards single-cite output), not generator-imposed.

5/ Three takeaways:

- Ship constrained generators as default
- Don't ship Contextual Retrieval for saturated hybrid retrieval
- LitQA2 isn't the right benchmark for localization claims — measure on RAGTruth/FaithBench instead

Full write-up + library: [link]

Methodology holes welcome.
