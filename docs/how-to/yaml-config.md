# Use YAML pipeline configs

For production deployments where the pipeline config should live in source control (and you want to change it without touching Python), describe it in YAML.

## Minimal YAML

The smallest config that still produces a working pipeline:

```yaml title="pipeline.yaml"
parser:
  type: pymupdf
chunker:
  type: parent_child
embedder:
  type: bge
indexer:
  dense:
    type: lancedb
  sparse:
    type: bm25
generator:
  type: prompted
  config:
    model: anthropic/claude-haiku-4-5
```

Load it:

```python
from verifiable_rag import Pipeline
pipeline = Pipeline.from_yaml("pipeline.yaml")
pipeline.ingest("paper.pdf")
answer = pipeline.ask("What did the authors find?")
```

## The recommended production config

Mirror of the `hybrid_balanced` preset, with all the knobs visible:

```yaml title="pipeline.yaml" hl_lines="20 27 33-37 41-44"
parser:
  type: docling
  fallback: pymupdf      # CompositeParser — try Docling first, fall back to PyMuPDF
  cache: true            # CachingParser — content-hashed JSON cache

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
  type: constrained          # ⭐ schema-forced cites, ReClaim-style
  config:
    model: anthropic/claude-haiku-4-5

verifier:
  type: dual_nli              # ⭐ HHEM + MiniCheck ensemble
  config:
    scorer_a: hhem
    scorer_b: minicheck
    aggregation: min
    threshold: 0.0562         # RAGTruth-train calibrated; recalibrate for your domain

pipeline:
  strictness: balanced        # loose | balanced | strict | paranoid
  top_k_retrieve: 100
  top_k_rerank: 10
```

[Full reference at `examples/pipeline.yaml`](https://github.com/firish/rag-rack/blob/main/examples/pipeline.yaml)

## Contextual Retrieval (opt-in)

To enable Anthropic's Contextual Retrieval recipe — generate per-chunk preambles via an LLM before embedding:

```yaml hl_lines="6-9"
chunker:
  type: parent_child
  config:
    max_child_tokens: 400
    min_child_tokens: 100
  contextual:
    enabled: true
    granularity: section     # cheapest tier; paragraph and chunk also supported
    model: claude-haiku-4-5-20251001
```

??? note "Cost & efficacy"
    Contextual Retrieval costs ~$0.10–0.20 per doc at section granularity (one LLM call per section), and more at finer granularities. On our LitQA2 ablation it was a null result — already-strong hybrid retrieval saturates without needing CR. Measure on your domain before scaling up. See [Contextual Retrieval how-to](contextual-retrieval.md).

## Discoverability — what types are available?

Every component type the YAML loader understands is listed by the registry at runtime:

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

This is the source of truth; if you can name it in YAML, it shows up here.

## Adding a custom component

Use the `@register` decorator to plug a new factory into the registry:

```python
# my_pipeline_extras.py
from verifiable_rag.config import register

@register("embedder", "my_custom_embedder")
def _factory(api_endpoint: str = "https://embed.example.com", **kw):
    from my_internal_lib import CustomEmbedder
    return CustomEmbedder(api_endpoint=api_endpoint, **kw)
```

Make sure the file is imported somewhere before you call `Pipeline.from_yaml(...)`:

```python
import my_pipeline_extras  # populates the registry
from verifiable_rag import Pipeline

pipeline = Pipeline.from_yaml("pipeline.yaml")  # can now use my_custom_embedder
```

Then in YAML:

```yaml
embedder:
  type: my_custom_embedder
  config:
    api_endpoint: https://embed.acme-corp.internal
```

The factory function takes `**config` from the YAML directly — any kwargs you accept are exposed as YAML keys under `config:`.

## Patterns we've found useful

### Environment-specific configs

Keep one YAML per environment (`dev.yaml`, `staging.yaml`, `prod.yaml`) and switch via env var:

```python
import os
from verifiable_rag import Pipeline

env = os.environ.get("APP_ENV", "dev")
pipeline = Pipeline.from_yaml(f"pipelines/{env}.yaml")
```

### Pipeline versioning

Tag the YAML file (or commit) when you ship a config change so you can roll back. We use a simple `version:` key at the top of the file that gets logged to observability:

```yaml
# Logged but ignored by the loader — useful for traceability
version: "v3-2026-05-28"

parser:
  # ...
```

### Validating configs in CI

Build the pipeline in a smoke test that doesn't ingest anything — just confirms the wiring:

```python
def test_prod_yaml_loads():
    from verifiable_rag import Pipeline
    pipeline = Pipeline.from_yaml("pipelines/prod.yaml")
    assert pipeline.strictness == "balanced"
    assert pipeline.verifier is not None
```

Catches typos before they hit production.

## When YAML isn't the right move

YAML is great when the config is **declarative and durable**. For these cases, prefer direct Python:

- **You're sharing components across pipelines** (one embedder serving multiple). Build them in code and pass instances.
- **You need conditional wiring** based on env vars or other runtime state. Python is cleaner than templating YAML.
- **You're prototyping.** A preset call (`hybrid_balanced()`) is 80% shorter than the equivalent YAML.

Use the level that matches your durability requirement. See [Configuration](../concepts/configuration.md) for the full hierarchy.
