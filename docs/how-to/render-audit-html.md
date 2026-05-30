# Render the HTML audit report

The headline differentiator — a self-contained HTML page showing every query's full audit trail.

## The simplest path

```python
import verifiable_rag
from verifiable_rag.demo import sample_paper_path

verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
    output_html="audit.html",
)
```

Open `audit.html` in any browser. That's it.

## What's in the report

The HTML page shows, top to bottom:

1. **Header** with strictness, refusal status, and overall faithfulness score
2. **Query** in a callout box
3. **Refusal banner** (only when the answer was refused)
4. **Answer body** with each sentence color-coded by verification:
   - **Default background:** supported (verifier passed)
   - **Red-tinted with dashed underline:** unsupported (verifier flagged)
   - Citations rendered as superscript `[chunk-id]` links — clicking jumps to the source passage card
5. **Faithfulness card row** — overall score plus the retrieval / NLI / generation components
6. **Per-sentence verification table** — every sentence with its NLI score and supported/unsupported badge
7. **Reranked passages** — every chunk the generator actually saw, anchored so citations link in

It's a single HTML file with inline CSS, no JavaScript, no external dependencies. Open it on any device with a browser.

## From a pre-built Pipeline

The `output_html=` kwarg also works on `Answer.to_html()`:

```python
from pathlib import Path
from verifiable_rag import hybrid_balanced

pipeline = hybrid_balanced()
pipeline.ingest("paper.pdf")
answer = pipeline.ask("What did the authors find?")

Path("audit.html").write_text(answer.to_html())
```

Custom title:

```python
Path("audit.html").write_text(
    answer.to_html(title="Audit — Q3 2026 review")
)
```

## Serve the report in a web app

The HTML is just a string. Drop it into any web framework:

=== "Flask"

    ```python
    from flask import Flask, Response, request

    app = Flask(__name__)
    pipeline = hybrid_balanced()
    pipeline.ingest("corpus/paper.pdf")

    @app.get("/ask")
    def ask():
        q = request.args["q"]
        answer = pipeline.ask(q)
        return Response(answer.to_html(title=q), mimetype="text/html")
    ```

=== "FastAPI"

    ```python
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse

    app = FastAPI()
    pipeline = hybrid_balanced()
    pipeline.ingest("corpus/paper.pdf")

    @app.get("/ask", response_class=HTMLResponse)
    def ask(q: str):
        return pipeline.ask(q).to_html(title=q)
    ```

## Use it as your debugging surface

The audit report is also the fastest way to **debug** a failing pipeline. When the answer looks wrong:

1. Generate the HTML report
2. Look at the **reranked passages section** — did the right passage make it through retrieval?
3. Check the **per-sentence verification table** — which sentences got flagged?
4. Look at the **citation links** — do they point at the right source spans?

Three failure modes show up immediately:

| What you see in the report | Likely cause |
|---|---|
| Right passage missing from "Reranked passages" | Retrieval issue — tune `top_k_retrieve`, swap embedder, add Contextual Retrieval |
| Right passage present, but generator cited a different one | Generator confused by similar chunks — switch to `ConstrainedCitedGenerator` |
| All sentences flagged unsupported | Threshold too high, or NLI model isn't trained on your domain — see [Calibrate threshold](calibrate-threshold.md) |

## Programmatic access to the same data

The HTML view is one surface. The same data is on the `Answer` object for code that needs it programmatically:

```python
answer.sentences                # list[CitedSentence]
answer.verification_results     # list[VerificationResult]
answer.retrieved_chunks         # the reranked passages (same as in the HTML)
answer.unsupported_sentences    # filtered: only the flagged ones
answer.cited_sentence_ids       # frozenset of all sentence IDs cited
answer.audit_trail()            # JSON-serializable dict for logging / metrics
```

See [Observability](observability.md) for production logging patterns.

## Customizing the report

The HTML report is rendered by [`verifiable_rag.report.to_html`](../api/report.md), which is a pure function. For substantial customization, copy it into your project and modify — there are no plugins or callbacks.

Common tweaks:

- **Custom CSS** — edit the `_CSS` constant in `report.py`
- **Hide sections** — wrap the section-rendering call in a feature flag
- **Add your branding** — modify the `<header>` block in `to_html()`
- **Multi-language** — replace the labels in the section renderers (they're plain strings)

If you do something interesting, open a PR — we'd like to hear the use case.
