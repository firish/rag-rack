# Installation

## Python version

`verifiable-rag` requires **Python 3.11 or newer** (3.11, 3.12, 3.13). The library is pure-Python; the heavy dependencies (torch, transformers, etc.) are opt-in extras.

## Install everything

For the recommended `hybrid_balanced` preset and the audit HTML report:

```bash
pip install "verifiable-rag[all]"
```

The `[all]` extra resolves to all of the following optional extras combined.

## Lighter installs

The core wheel is intentionally tiny — every heavy dependency is opt-in. Pick the extras that match what you're going to use:

```bash
# Just the core data model & helpers — no parsing, no embedding, no LLMs
pip install verifiable-rag

# Parsing
pip install "verifiable-rag[docling]"   # Docling — best PDF quality, slow, OCR-capable
pip install "verifiable-rag[pymupdf]"   # PyMuPDF — fast, text-only, no OCR

# Sentence segmentation
pip install "verifiable-rag[wtpsplit]"  # wtpsplit SaT — used by the default segmenter

# Embedding
pip install "verifiable-rag[bge]"       # BGE-small via sentence-transformers (local, free)
pip install "verifiable-rag[cohere]"    # Cohere embed-english-v3 (hosted)
pip install "verifiable-rag[voyage]"    # Voyage embeddings (hosted)

# Indexing
pip install "verifiable-rag[lancedb]"   # LanceDB dense store
pip install "verifiable-rag[bm25]"      # BM25 sparse store via bm25s

# LLM generators / judges
pip install "verifiable-rag[litellm]"   # LiteLLM — routes Anthropic, OpenAI, Gemini, Groq, Ollama, ...

# Verifiers
pip install "verifiable-rag[hhem]"      # HHEM-2.1-open NLI verifier (~600 MB at runtime)
pip install "verifiable-rag[minicheck]" # MiniCheck-Flan-T5-Large (~770 MB at runtime)

# YAML pipeline config
pip install "verifiable-rag[yaml]"      # Pipeline.from_yaml()

# Modal-hosted GPU verifiers (advanced)
pip install "verifiable-rag[modal]"
```

## API keys

The default `hybrid_balanced` preset needs two:

| Service | Used for | Env var | Get one |
|---|---|---|---|
| Anthropic | Generator (Claude Haiku 4.5) | `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/) |
| Cohere | Embedding + reranking | `COHERE_API_KEY` | [dashboard.cohere.com](https://dashboard.cohere.com/) |

For zero-API-key retrieval, use the `local_minimal` preset (BGE + PyMuPDF, generator still needs Anthropic) or swap in a fully-local LLM via Ollama. See [Local-only setup](../how-to/local-only-setup.md).

## First-run model downloads

Verifier model weights are **not bundled** in the wheel — they're downloaded lazily from HuggingFace Hub on first use, then cached forever in `~/.cache/huggingface/hub/`.

| Verifier | Model | Size |
|---|---|---|
| `HHEMVerifier` | `vectara/hallucination_evaluation_model` | ~600 MB |
| `MiniCheckVerifier` | `lytang/MiniCheck-Flan-T5-Large` | ~770 MB |
| `LLMJudgeVerifier` | (hosted API, no local model) | 0 |

Standard `transformers` progress bar is shown during download.

## Editable / development install

```bash
git clone https://github.com/firish/rag-rack.git
cd rag-rack
python -m venv .venv && source .venv/bin/activate
pip install -e ".[all,dev]"
```

The `[dev]` extra adds pytest, mypy, ruff, and pre-commit.

Run the smoke tests:

```bash
pytest -m smoke
```

## Verify the install

```bash
python -c "import verifiable_rag; print(verifiable_rag.__version__)"
```

A 5-second sanity check that the bundled demo helpers work:

```bash
python -c "from verifiable_rag.demo import load_sample_document; \
           d = load_sample_document(); \
           print(f'{len(d.sections)} sections, {sum(len(p.sentences) for s in d.sections for p in s.paragraphs)} sentences')"
```

Expected output: `1 sections, 84 sentences`.

## Troubleshooting

??? bug "ImportError: No module named 'sentence_transformers' / 'cohere' / 'transformers'"
    You haven't installed the extra that pulls in the missing dependency. Re-install with the right extra (see table above), or just use `pip install "verifiable-rag[all]"`.

??? bug "AuthenticationError from LiteLLM"
    The generator model isn't getting the right API key. Confirm with `echo $ANTHROPIC_API_KEY` (or whichever provider). If it's set but still failing, check the provider's dashboard for rate-limit or billing issues.

??? bug "First call hangs for a long time"
    The verifier models are downloading from HuggingFace (~1.4 GB combined for the dual NLI default). This is one-time; subsequent runs use the cache. Set `HF_HUB_VERBOSITY=info` to see the progress bar.

??? bug "Out of memory on Apple Silicon MPS"
    Long premises can blow up MPS memory on the verifier's attention layer. Either drop the batch size at the call site or set `PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0` (read the [PyTorch MPS note](https://docs.pytorch.org/docs/stable/notes/cuda.html) first; this can cause system instability).
