# Blog

Long-form posts on the architectural and empirical decisions behind `verifiable-rag`. Each post ties to a published benchmark report under [`benchmarks/`](../benchmarks/index.md); the blog tells the story, the report has the raw numbers.

**Reading order if you're new:** the feature roundup ([What's in the box and what's coming next](05_what_we_have_and_whats_next.md)) is the most comprehensive single overview. The benchmark posts can be read in any order, but the chronological narrative is **ALCE → RAGTruth → LitQA2**.

---

## 05 — What's in the box, and what's coming next

[Read →](05_what_we_have_and_whats_next.md){ .md-button .md-button--primary }

A complete tour of every component shipped in the library today — corpus acquisition, parsing, chunking (including Contextual Retrieval), embedding, indexing, reranking, three citation modes, the dual NLI verifier, the strictness slider, audit trail — plus eight planned SOTA features the next few releases will land (HyDE, late chunking, sentence-level dual NLI, streaming citations, LAQuer, ColBERTv2, cross-document disagreement detection, visual citation highlighting in PDF viewers).

If you want one post that captures what verifiable-rag is and where it's going, this is it.

---

## 04 — Five levers, one ceiling: a LitQA2 ablation

[Read →](04_litqa2_ablation.md){ .md-button }

I ran a 3×2 ablation on FutureHouse's biomedical Q&A benchmark — three generators (prompted, constrained, SAFE) × two retrieval configurations (with/without Contextual Retrieval). The result:

- **Contextual Retrieval is a null on a saturated hybrid retrieval stack.** Bit-identical metrics on every cell.
- **Constrained decoding is the lever** (+6.9pp MC on the pilot slice, +0.5pp on the full corpus).
- **SAFE doesn't move localization** even though it was designed for it — the ceiling is benchmark-imposed (sentence-level scoring rewards single-cite output), not generator-imposed.

The honest takeaway: measure where your bottleneck actually is before reaching for SOTA techniques.

---

## 03 — Verified RAG: every sentence checked

[Read →](03_verified_rag.md){ .md-button }

The result that drives the library's design. On RAGTruth (the canonical 2,700-example RAG hallucination corpus), a dual NLI ensemble of two small open-source models (HHEM-2.1-open + MiniCheck-Flan-T5-Large) matches a Claude Sonnet 4.6 LLM-judge — **AUROC 0.844 vs 0.846 — at roughly 1/250th the per-call cost.**

The interesting story underneath the headline: the two NLI models have *complementary blind spots*. HHEM is strong on QA-style entailment; MiniCheck is strong on data-to-text. Ensembling them at the min-aggregation produces a verifier that's robust across the task distributions you'll see in practice.

---

## 02 — Sentence-grounded citations beat prompted citations on ALCE

[Read →](02_constrained_citations.md){ .md-button }

Constrained-decoding citations (ReClaim-style schema-forced output) beat prompted-only citations by 4–7 F1 points on Princeton's ALCE benchmark, under both Haiku 4.5 and Sonnet 4.6 as judges.

The methodologically interesting part: **the Haiku→Sonnet score gap is much smaller under constrained outputs**. Two independent judges agree more when the model is forced (by schema) to produce specific, multi-cite output. If you're using LLM-as-judge in production faithfulness pipelines, *judge-stability* of your generator architecture matters more than absolute numbers from any single judge.

The library defaults to `ConstrainedCitedGenerator` because of this result.

---

## Methodology notes that apply to all posts

- **Reproducibility** — every published number maps to a CLI command in the matching benchmark report.
- **Dual-judge cross-validation** (where LLM judges are used) — same outputs are scored by two different Claude models to spot generosity bias.
- **Train/test discipline** — thresholds and aggregation choices are fit on a held-out train slice, frozen, applied to test. In-sample best metrics are reported only as a diagnostic.
- **Honest caveats** — each post lists what *isn't* validated, what would strengthen the result, and what was deferred to backlog.

Methodology critiques welcome. Eval rigor is the whole moat; the only way to find the holes is to invite people to look for them. File an issue on [GitHub](https://github.com/firish/rag-rack/issues) if you find one.
