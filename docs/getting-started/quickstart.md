# Quickstart

The fastest path from `pip install` to a verified, cited answer.

## 1. Install

```bash
pip install "verifiable-rag[all]"
```

The `[all]` extra brings in everything (parser, embedder, index, reranker, verifiers). For lighter installs see the [installation guide](installation.md).

## 2. Set an API key

The default generator is Claude Haiku 4.5. You need an Anthropic API key:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

To switch to OpenAI, Gemini, Groq, Ollama, etc., see [Swap LLM provider](../how-to/swap-llm-provider.md).

## 3. Ask a question

The library ships with a small public-domain demo document (a 3-page overview of penicillin) so you can verify everything works without finding a PDF yourself:

```python
import verifiable_rag
from verifiable_rag.demo import sample_paper_path

answer = verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
)
print(answer.text)
```

That's it. The `ask()` helper:

1. Builds the default `hybrid_balanced` pipeline (Cohere retrieval + Dual NLI + constrained Haiku generator)
2. Parses, chunks, embeds, and indexes the document
3. Runs the query through retrieval → reranking → generation → verification
4. Returns an `Answer` object

??? note "First-run model downloads"
    On the first call, the verifier downloads HHEM-2.1-open (~600 MB) and MiniCheck-Flan-T5-Large (~770 MB) from HuggingFace, cached to `~/.cache/huggingface/hub/`. Subsequent calls reuse the cache and skip the download.

## 4. Use your own document

Swap the demo path for your own PDF:

```python
answer = verifiable_rag.ask(
    "What did the authors find?",
    docs="path/to/your_paper.pdf",
)
```

Or a list of documents:

```python
answer = verifiable_rag.ask(
    "Compare the two methods.",
    docs=["paper_a.pdf", "paper_b.pdf"],
)
```

## 5. See the audit trail

The headline feature. Get a self-contained HTML page showing the answer with per-sentence verification color coding, faithfulness scores, and every reranked passage the generator saw:

```python
verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
    output_html="audit.html",
)
```

Open `audit.html` in any browser. Citations are anchored links into the passage list; unsupported sentences get a red dashed underline; faithfulness scores show at a glance.

For the programmatic version of the same data:

```python
answer = verifiable_rag.ask("...", docs=...)

for sentence in answer.unsupported_sentences:
    print(f"⚠ unsupported: {sentence.text}")

# Structured dump for logging / metrics emit:
import json
print(json.dumps(answer.audit_trail(), indent=2))
```

## 6. Pick a preset

The default `hybrid_balanced` preset uses Cohere for embedding and reranking (requires `COHERE_API_KEY`). For zero-API-key retrieval:

```python
answer = verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
    preset="local_minimal",  # BGE embed, no reranker, no verifier
)
```

For stricter refusal behavior:

```python
answer = verifiable_rag.ask(
    "What did the authors prove?",
    docs="paper.pdf",
    preset="hybrid_strict",  # refuses below faithfulness 0.7
)
if answer.was_refused:
    print(f"Refused: {answer.refusal_reason}")
```

See the [configuration concept page](../concepts/configuration.md) for the full preset list with cost-vs-quality tradeoffs.

## 7. Multi-question pattern

`verifiable_rag.ask()` is single-shot — it ingests on every call. For multiple questions over the same corpus, build a Pipeline directly so you only pay the ingest cost once:

```python
from verifiable_rag import hybrid_balanced

pipeline = hybrid_balanced()
pipeline.ingest("paper.pdf")

a1 = pipeline.ask("What did the authors find?")
a2 = pipeline.ask("What methodology did they use?")
a3 = pipeline.ask("What are the limitations?")
```

[Runnable example →](https://github.com/firish/rag-rack/blob/main/examples/04_multi_question.py)

## Next steps

- **Understand what's happening:** [Architecture](../concepts/architecture.md), [Citation flow](../concepts/citation-flow.md), [Verification](../concepts/verification.md)
- **Tune the verifier on your domain:** [Calibrate threshold](../how-to/calibrate-threshold.md)
- **Build a custom pipeline:** [YAML config](../how-to/yaml-config.md), [Configuration](../concepts/configuration.md)
- **Integrate with your stack:** [Observability](../how-to/observability.md), [Local-only setup](../how-to/local-only-setup.md)
