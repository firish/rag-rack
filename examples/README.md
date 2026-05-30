# Examples

Runnable demos that exercise the headline `verifiable-rag` features.
All examples default to the bundled sample document
([`data/sample.pdf`](data/sample.pdf), a ~3-page authored overview of
penicillin); pass a `--pdf` argument to use your own.

| Example | Shows | Required env vars |
|---|---|---|
| [`01_minimal.py`](01_minimal.py) | 10-line top-level `verifiable_rag.ask()` quickstart | `ANTHROPIC_API_KEY` |
| [`02_audit_html.py`](02_audit_html.py) | Generate the HTML audit report and open it in a browser | `ANTHROPIC_API_KEY` |
| [`03_audit_trail.py`](03_audit_trail.py) | Programmatic access — `unsupported_sentences`, `audit_trail()`, JSON-ready dump | `ANTHROPIC_API_KEY` |
| [`04_multi_question.py`](04_multi_question.py) | Build a Pipeline once, ask many questions over the same docs | `ANTHROPIC_API_KEY` |
| [`05_yaml_config.py`](05_yaml_config.py) | Load a Pipeline from `pipeline.yaml` + discover types via `registered_types()` | `ANTHROPIC_API_KEY`, `COHERE_API_KEY` |
| [`inspect_parser.py`](inspect_parser.py) | Diagnostic — parse a PDF with Docling and print structural stats | — |

## First-run cost

Examples 02–04 use the `local_verified` preset which includes
**HHEM-2.1-open** (~600 MB) as the NLI verifier. The model is downloaded
from HuggingFace on first call and cached forever after in
`~/.cache/huggingface/hub/`. Subsequent runs reuse the cache and skip
the download.

The bundled sample document is pre-parsed
([`data/sample.parsed.json`](data/sample.parsed.json)) so the parsing
step is effectively free. Embedding + indexing ~30 chunks takes a few
seconds on CPU, ~1 second on Apple Metal (MPS) or CUDA.

## Sample document

The bundled `data/sample.pdf` is a ~3-page summary of penicillin
(discovery, mechanism, resistance, clinical use) authored for this
project — no third-party copyright applies. The raw text is at
[`data/sample.txt`](data/sample.txt) if you want to inspect or modify it.

Good demo questions:

- "Who discovered penicillin and when?"
- "What is the mechanism of action of penicillin?"
- "How does bacterial resistance to penicillin develop?"
- "What classes of antibiotics share the beta-lactam ring?"
