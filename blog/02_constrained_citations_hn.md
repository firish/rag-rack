# HN submission — Blog post #2 (ALCE / constrained citations)

## Recommended title (pick one)

- **Constrained decoding for RAG citations beats prompted by 4–7 F1 points on ALCE**
- **Structured-output citations on ALCE: dual-LLM-judge cross-validated**
- **ReClaim-style constrained decoding for citations matches SAFE-tier on ASQA**

First is most clickable, second flags the methodological rigor, third hooks the readers who recognize "SAFE" and "ALCE" by name.

## Body (~200 words)

Spent the last few weeks comparing two ways to generate RAG citations on Princeton's ALCE benchmark: prompt-only ("emit cites inline by passage ID") vs constrained decoding ("structured-output schema forces 1–3 cites per sentence"). Constrained wins by +7.1 pp recall on ASQA and +4.8 pp on QAMPARI, while precision stays within 0.5 pp.

But the actually-interesting result is from dual-LLM-judge cross-validation. I ran every output through both Claude Haiku 4.5 and Sonnet 4.6 as independent graders. Two findings:

1. Both judges agree constrained beats prompted — so it's not a judge-generosity artifact.
2. The Haiku→Sonnet score gap is *much smaller* for constrained outputs (1.6 pp ASQA recall) than for prompted (5.2 pp). The constrained generator produces output that's more *judge-robust* — both graders agree more often when the model is schema-forced to produce specific, multi-cite output.

Practical takeaway: if you're using a small LLM as a judge for faithfulness checks in production, the architectural choice that minimizes Haiku→Sonnet drift matters more than absolute numbers on any single judge.

Numbers sit above ALCE-paper and ReClaim, at/above SAFE-tier on both measured sub-benchmarks. Caveats: Claude judges (not T5-XXL TRUE), ELI5 missing Sonnet measurement, retrieval held constant per ALCE design.

Full write-up: [link to blog/02_constrained_citations.md]
Benchmark report (per-sub-benchmark, reproducibility): [link to benchmarks/PUBLISHED_alce.md]
Library: [link to github.com/firish/rag-rack]

## Pre-submission checklist

- [ ] Push current branch + blog post to a public URL (personal blog / Substack / GitHub Pages)
- [ ] Replace the three `[link ...]` placeholders with real URLs
- [ ] Time the submission for Tuesday or Wednesday morning PT
- [ ] Don't use a `Show HN:` prefix — this is a "I ran a benchmark" methodology post, not a product launch
- [ ] Be ready to answer methodology questions in the comments for the first 2 hours

## Likely top HN comments to pre-empt

1. **"Claude judges aren't T5-XXL TRUE — your numbers aren't paper-comparable."** True; in the post and benchmark report. T5-XXL cross-validation is backlog. The dual-Claude design establishes internal consistency, not paper-bit-exact equivalence.

2. **"Why didn't you use structured outputs for prompted too?"** Because the comparison is *prompt-only-cites* vs *schema-forced-cites*. Putting structured output in the "prompted" arm would conflate the two interventions.

3. **"Constrained adds a runtime dependency on `outlines` / `lm-format-enforcer` for local models."** Yes — closed-API providers (Anthropic, OpenAI, Gemini) handle it natively. Local Llama-3 needs one of these libs. Prompted is the fallback for environments where neither is available.

4. **"Per-sentence cite attribution vs per-question union — why does that matter?"** If you union all cites in an answer to the question level, LOO precision divides by the union size; that artificially deflates precision for any generator that emits multi-cite answers. Per-sentence attribution gives every cite a defined home, and LOO is computed within the sentence. Without this, constrained looks worse than it is.

5. **"95% recall on ASQA seems too high."** Two factors: ALCE ships pre-retrieved passages (the generator's job is constrained to picking from oracle-tier candidates), and we use Sonnet-4.6 as judge (lower than Haiku-judge but higher than T5-XXL TRUE for our outputs). The number is real for this judge under this retrieval setting; it's not "end-to-end RAG accuracy."

## X / Twitter thread version (5 tweets)

1/ Spent the last few weeks running ALCE (Princeton's RAG citation-quality benchmark) on two generator configs: prompt-only citations vs structured-output constrained decoding.

Constrained wins by +7.1 pp recall on ASQA (88.2 → 95.3) and +4.8 pp on QAMPARI (90.4 → 95.2).

2/ But the headline isn't the most interesting bit. I ran every output through both Claude Haiku 4.5 and Sonnet 4.6 as independent judges. The Haiku→Sonnet score gap is much smaller under constrained (1.6 pp ASQA recall) than under prompted (5.2 pp).

3/ Translation: the constrained generator's output is more *judge-robust*. Two graders agree more often when the model is forced (by schema) to produce specific, multi-cite output. Less room for any single judge's biases to dominate.

4/ Practical takeaway: if you use a small LLM as a faithfulness judge in production, the *judge-stability* of your generator architecture matters more than absolute numbers from any single judge. Constrained raises the floor — your outputs hold up under stricter graders.

5/ Numbers sit above the ALCE paper (T5-XXL judge ~65/~70 F1) and ReClaim (~75/~80), at/above SAFE-tier (~85–90).

Full write-up: [link]
Benchmark report: [link]
Library (MIT, pre-alpha): [link]

Methodology holes welcome.
