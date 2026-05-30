# Use Contextual Retrieval (and when not to)

[Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) is Anthropic's 2024 recipe for improving retrieval quality: for each chunk, generate an LLM-written 50–100-token preamble describing what the chunk is about within the document, and prepend that preamble before embedding. The embedding model then has document-level context, which Anthropic reports cuts retrieval failures by ~67%.

The library ships this as an opt-in chunker wrapper. **Whether it helps you depends entirely on whether retrieval is your bottleneck.**

## The honest finding from our LitQA2 ablation

We ran Contextual Retrieval on LitQA2 (a 199-question biomedical scientific Q&A benchmark) at section-level granularity. **The result was a null — bit-identical metrics across both generator backbones.**

```
        | prompted | prompted + CR | constrained | constrained + CR
--------|----------|---------------|-------------|------------------
mc_acc  | 0.897    | 0.897         | 0.966       | 0.966
cit_f1  | 0.463    | 0.466         | 0.466       | 0.466
loc_acc | 0.241    | 0.241         | 0.207       | 0.207
```

Across every metric, CR moved nothing. Because the underlying hybrid retrieval stack (Cohere embed + BM25 + Cohere rerank) was already saturating, the document-level context preambles disappeared in the noise.

[Full LitQA2 ablation result →](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_litqa2.md)

## When Contextual Retrieval probably WILL help

- **Single-method retrieval** — you have dense embeddings only, no BM25, no reranker. The preamble adds context that the dense embeddings otherwise miss.
- **Heterogeneous corpora** — a mix of biology papers, legal docs, and code documentation. The preamble disambiguates which domain a chunk is from.
- **Ambiguous queries** — "What did they find?" without enough context for retrieval to match the right paper. The preamble lets the embedder know "this chunk is about cancer immunotherapy."
- **Short, content-poor chunks** — headers, dates, single sentences. The preamble adds enough surrounding context for them to embed meaningfully.

## When it probably WON'T help

- **You're already running hybrid retrieval + rerank.** LitQA2-style result — the gains overlap with what rerank already does.
- **Your queries are well-specified.** "What is the binding mechanism of penicillin-binding protein 2a?" leaves little ambiguity for the preamble to resolve.
- **Your chunks are already rich in content.** A 400-token academic paper paragraph usually has its own context.
- **You're cost-sensitive.** CR at chunk granularity is the most expensive option — for LitQA2's 185 papers, the full corpus would cost ~$300 with Haiku. Even section granularity is ~$15.

## How to enable it

Use the `ContextualChunker` to wrap any base chunker:

```python
from verifiable_rag import Pipeline
from verifiable_rag.chunkers import (
    ContextualChunker, LLMContextualizer, ParentChildChunker,
)
# ... other components

pipeline = Pipeline(
    parser=...,
    chunker=ContextualChunker(
        base=ParentChildChunker(max_child_tokens=400),
        contextualizer=LLMContextualizer(
            model="claude-haiku-4-5-20251001",
            max_workers=3,           # be conservative under sustained load
            num_retries=5,            # absorb Anthropic 529 overload bursts
        ),
        granularity="section",        # cheapest tier — see below
    ),
    embedder=...,
    # ...
)
```

Or via YAML:

```yaml
chunker:
  type: parent_child
  config:
    max_child_tokens: 400
  contextual:
    enabled: true
    granularity: section
    model: claude-haiku-4-5-20251001
```

## Granularity tiers — cost vs. specificity

The library exposes three granularities:

| Granularity | Calls per paper | Cost per paper (Haiku + caching) | When to use |
|---|---|---|---|
| `section` ⭐ | ~10–20 | $0.05–0.20 | **Default** — structured docs (papers, books, technical docs) |
| `paragraph` | ~30–100 | $0.15–0.60 | Mixed-topic docs, long sections |
| `chunk` | ~100–500 | $0.50–3.00 | Power-user — Anthropic's original recipe; max specificity |

`section` shares one preamble across every child chunk in the section — for academic papers where sections are coherent thematic units, this is the right tradeoff. `paragraph` is the middle ground; `chunk` is the original Anthropic recipe.

??? note "Custom grouping"
    The `group_by` parameter lets you provide an arbitrary callable that maps a chunk to a group key. Useful for documents with custom structure (chat logs grouped by speaker, code grouped by function, transcripts grouped by topic cluster). See the [ContextualChunker API reference](../api/chunkers.md).

## Run the LitQA2-style ablation on your data

Before paying for full-corpus CR, validate it helps on a small slice:

```bash
# Baseline: no CR
python -m verifiable_rag.eval \
    --benchmark litqa2 \
    --max-questions 30 \
    --model anthropic/claude-haiku-4-5 \
    --embedder cohere --reranker cohere \
    --top-k-retrieve 100 --top-k-rerank 10 \
    --index-dir .verifiable_rag_cache/indexes/pilot_baseline \
    --contextual none \
    --out report_baseline.md

# With CR at section granularity
python -m verifiable_rag.eval \
    --benchmark litqa2 \
    --max-questions 30 \
    --model anthropic/claude-haiku-4-5 \
    --embedder cohere --reranker cohere \
    --top-k-retrieve 100 --top-k-rerank 10 \
    --index-dir .verifiable_rag_cache/indexes/pilot_contextual_section \
    --contextual section \
    --out report_contextual.md
```

Compare the metrics. If the delta is below your noise floor (typically ±0.3pp on a 30-example slice), CR isn't doing anything useful for your stack — stop here. If it shows ≥0.5pp lift, scale up to your full corpus.

## API stability dodging

Anthropic's `overloaded_error` 529s hit during sustained contextualization runs. The library defaults to conservative settings inside the eval pipeline (`max_workers=3`, `num_retries=5`), which empirically survives even bursty overload events. If you're using `LLMContextualizer` directly outside the eval flow, mirror these defaults:

```python
LLMContextualizer(
    model="claude-haiku-4-5-20251001",
    max_workers=3,
    num_retries=5,
)
```
