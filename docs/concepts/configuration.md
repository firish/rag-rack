# Configuration

Three levels of customization, in order of how often you'll use them.

## 1. Presets (most users)

Five named factory functions cover ~95% of use cases. Pick the one closest to what you need and pass kwargs to tweak:

| Preset | Components | Required keys |
|---|---|---|
| `local_minimal` | BGE + PyMuPDF + Haiku, no verifier | `ANTHROPIC_API_KEY` |
| `local_verified` | + BGE rerank + HHEM NLI | `ANTHROPIC_API_KEY` |
| `hybrid_balanced` ⭐ | Docling + Cohere + Dual NLI + constrained Haiku | `ANTHROPIC_API_KEY` + `COHERE_API_KEY` |
| `hybrid_strict` | Same as balanced, refuse below faithfulness 0.7 | same |
| `hybrid_paranoid` | Sonnet generator, refuse below 0.9 | same |

```python
from verifiable_rag import hybrid_balanced

pipeline = hybrid_balanced(
    generator_model="anthropic/claude-haiku-4-5",  # default
    index_dir="./my_index",                         # override the default cache path
)
pipeline.ingest("paper.pdf")
answer = pipeline.ask("...")
```

For the top-level one-liner:

```python
import verifiable_rag

answer = verifiable_rag.ask(
    "...",
    docs="paper.pdf",
    preset="hybrid_strict",          # name of any preset
    generator_model="claude-sonnet-4-6",  # forwarded to the preset factory
)
```

## 2. `build_pipeline()` (mix and match)

When none of the presets quite fits, `build_pipeline()` lets you pick axes independently:

```python
from verifiable_rag import build_pipeline

pipeline = build_pipeline(
    retrieval="local",          # "local" | "hybrid"
    verifier="dual_nli",        # "none" | "hhem" | "minicheck" | "dual_nli"
    generator="constrained",    # "prompted" | "constrained"
    strictness="strict",        # "loose" | "balanced" | "strict" | "paranoid"
    generator_model="anthropic/claude-haiku-4-5",
    top_k_retrieve=80,
    top_k_rerank=8,
)
```

This is still a factory function — it returns a `Pipeline` with sensible defaults for the unselected components.

## 3. YAML config (custom, durable)

For production pipelines where the config should live in source control (and you don't want it in Python), describe the full pipeline in YAML:

```yaml title="pipeline.yaml"
parser:
  type: docling
  fallback: pymupdf
  cache: true

chunker:
  type: parent_child
  config:
    max_child_tokens: 400
    min_child_tokens: 100

embedder:
  type: cohere

indexer:
  dense:
    type: lancedb
    uri: .verifiable_rag_cache/indexes/my_pipeline
  sparse:
    type: bm25

reranker:
  type: cohere

generator:
  type: constrained
  config:
    model: anthropic/claude-haiku-4-5

verifier:
  type: dual_nli
  config:
    scorer_a: hhem
    scorer_b: minicheck
    aggregation: min
    threshold: 0.0562

pipeline:
  strictness: balanced
  top_k_retrieve: 100
  top_k_rerank: 10
```

Then:

```python
from verifiable_rag import Pipeline

pipeline = Pipeline.from_yaml("pipeline.yaml")
```

See [examples/pipeline.yaml](https://github.com/firish/rag-rack/blob/main/examples/pipeline.yaml) for a fully annotated reference and [YAML config how-to](../how-to/yaml-config.md) for patterns.

## Component discoverability

The YAML loader uses a registry. To see every component type the loader understands at runtime:

```python
from verifiable_rag.config import registered_types

for component, types in registered_types().items():
    print(f"{component}: {types}")
```

```text
parser: ['docling', 'pymupdf']
chunker: ['parent_child']
embedder: ['bge', 'cohere', 'voyage']
dense_indexer: ['lancedb']
sparse_indexer: ['bm25']
reranker: ['bge', 'cohere']
generator: ['constrained', 'prompted', 'safe']
verifier: ['dual_nli', 'hhem']
scorer: ['hhem', 'llm_judge', 'minicheck']
```

Every entry in the registry maps to a factory function. Add your own with the `@register` decorator:

```python
from verifiable_rag.config import register

@register("embedder", "my_custom_embedder")
def _factory(**config):
    return MyCustomEmbedder(**config)
```

Now your component is reachable from YAML:

```yaml
embedder:
  type: my_custom_embedder
  config:
    api_key: ...
```

This is the extension hook for company-internal components, niche providers, or experimental modules you don't want to upstream.

## 4. Direct `Pipeline()` construction (rare)

Sometimes you want full control — passing component instances you've already configured elsewhere, mixing in custom wrappers, sharing an embedder across pipelines, etc:

```python
from verifiable_rag import Pipeline
from verifiable_rag.parsers import DoclingParser
from verifiable_rag.chunkers import ParentChildChunker, ContextualChunker, LLMContextualizer
from verifiable_rag.embedders import CohereEmbedder
# ...

shared_embedder = CohereEmbedder()
contextualizer = LLMContextualizer(model="claude-haiku-4-5-20251001")

pipeline = Pipeline(
    parser=DoclingParser(),
    chunker=ContextualChunker(
        base=ParentChildChunker(max_child_tokens=400),
        contextualizer=contextualizer,
        granularity="section",
    ),
    embedder=shared_embedder,
    # ...
)
```

This is the escape hatch — you can do *anything* the protocol-based interface allows. But you give up the preset defaults and have to wire every component yourself.

## When to use which

| Need | Use |
|---|---|
| Quickest path to a working pipeline | A preset |
| Mix two preset axes (e.g. local retrieval + Cohere reranker) | `build_pipeline()` |
| Reproducible, version-controlled config | YAML |
| Custom components, niche providers, experimental wrappers | Direct `Pipeline()` |

The four options compose. You can register a custom component via the YAML registry and then call it from a `build_pipeline()` factory by wrapping `Pipeline()` directly. Pick the level that matches your durability vs. flexibility tradeoff.
