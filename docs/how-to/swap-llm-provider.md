# Swap LLM provider

The library uses [LiteLLM](https://docs.litellm.ai/) to route generator calls, which means you can use any provider LiteLLM supports — Anthropic (default), OpenAI, Google Gemini, Groq, Together, local Ollama, vLLM endpoints, and dozens more.

## Switching the generator model

The default is Claude Haiku 4.5. Override via the `generator_model` kwarg on any preset:

```python
import verifiable_rag

answer = verifiable_rag.ask(
    "What did the authors find?",
    docs="paper.pdf",
    preset="hybrid_balanced",
    generator_model="openai/gpt-4o-mini",
)
```

Or when building a Pipeline directly:

```python
from verifiable_rag import Pipeline
from verifiable_rag.generators import ConstrainedCitedGenerator

pipeline = Pipeline(
    ...,
    generator=ConstrainedCitedGenerator(model="openai/gpt-4o-mini"),
)
```

## Setting the API key

LiteLLM looks for provider-specific env vars:

| Provider | Env var |
|---|---|
| Anthropic | `ANTHROPIC_API_KEY` |
| OpenAI | `OPENAI_API_KEY` |
| Google Gemini | `GEMINI_API_KEY` |
| Groq | `GROQ_API_KEY` |
| Together | `TOGETHER_API_KEY` |
| Cohere | `COHERE_API_KEY` (also used by the embedder/reranker) |

For the full list, see [LiteLLM provider docs](https://docs.litellm.ai/docs/providers).

## Recommended models per use case

### Best citation quality (constrained generator)

`ConstrainedCitedGenerator` requires structured-output support. These all work:

- `anthropic/claude-haiku-4-5` ⭐ (default — best cost/quality)
- `anthropic/claude-sonnet-4-6` (stronger, more expensive — used by `hybrid_paranoid` preset)
- `openai/gpt-4o-mini`
- `openai/gpt-4o`
- `gemini/gemini-1.5-flash`
- `gemini/gemini-1.5-pro`

### Best cost (prompted generator)

`PromptedCitedGenerator` works with any LiteLLM model, including ones without structured output. Useful for:

- `groq/llama-3.3-70b-versatile` (very fast, free tier available)
- `ollama/llama3.1` (local, free, no API key needed)
- `together/Qwen/Qwen2-72B-Instruct` (open weights, hosted)

```python
from verifiable_rag.generators import PromptedCitedGenerator

pipeline = Pipeline(
    ...,
    generator=PromptedCitedGenerator(model="groq/llama-3.3-70b-versatile"),
)
```

### Local-only (no API keys)

Use Ollama or a local vLLM endpoint with LiteLLM's `api_base` override:

```python
PromptedCitedGenerator(
    model="ollama/llama3.1",
    api_base="http://localhost:11434",
)
```

Then start Ollama:

```bash
ollama pull llama3.1
ollama serve
```

See [Local-only setup](local-only-setup.md) for the full air-gapped recipe.

## Switching the verifier's LLM judge

If you're using `LLMJudgeVerifier` instead of (or in addition to) the NLI verifiers:

```python
from verifiable_rag.verifiers import LLMJudgeVerifier

verifier = LLMJudgeVerifier(
    model="anthropic/claude-sonnet-4-6",  # default
    max_workers=8,
    temperature=0.0,
)
```

Same provider list applies. For most use cases, the dual NLI verifier is the better choice — see [Verification](../concepts/verification.md).

## Switching the Contextual Retrieval LLM

`LLMContextualizer` (used inside `ContextualChunker`) also runs on LiteLLM:

```python
from verifiable_rag.chunkers import LLMContextualizer

contextualizer = LLMContextualizer(
    model="claude-haiku-4-5-20251001",  # default — cheapest with prompt caching
)
```

For local Contextual Retrieval, swap to Ollama. Quality is noticeably lower per-preamble but the per-doc cost drops to zero.

## Model pinning vs. version aliasing

LiteLLM accepts both:

| Form | Behavior |
|---|---|
| `anthropic/claude-haiku-4-5` | Alias — Anthropic picks the latest 4.5 patch |
| `anthropic/claude-haiku-4-5-20251001` | Pinned — exact model version |

For **production**, always pin. Silent model updates have shifted benchmark scores before, and the library's calibrated thresholds (HHEM 0.3, Dual NLI 0.0562) assume the same model that was calibrated against.

For **prototyping**, the alias is fine — you want the latest improvements.

## Rate-limiting & retries

LiteLLM honors provider `Retry-After` headers and uses exponential backoff on transient errors. Each generator accepts a `num_retries` kwarg:

```python
PromptedCitedGenerator(model="anthropic/claude-haiku-4-5", num_retries=5)
```

For `LLMJudgeVerifier` running large batches under sustained load, drop `max_workers` to 2–4 to avoid bursty `overloaded_error` responses.

## When the swap silently doesn't work

Common failures and how to spot them:

- **Empty answers from `ConstrainedCitedGenerator`** — your chosen model doesn't support structured output. Switch to `PromptedCitedGenerator` or pick a supported model.
- **Garbage citations from `PromptedCitedGenerator`** — the model doesn't follow the in-prompt format reliably. Use a stronger model or switch to `ConstrainedCitedGenerator` if the model supports it.
- **Hallucinated cite IDs** — a known failure mode for `PromptedCitedGenerator` on smaller models. `ConstrainedCitedGenerator` makes this structurally impossible (cite IDs are drawn from an enum at decode time).
- **API errors propagate up** — by design. The Pipeline catches per-question errors in the eval runner, but in production code wrap `pipeline.ask()` in your own try/except.

For the trade-offs between generator types, see [Citation flow](../concepts/citation-flow.md).
