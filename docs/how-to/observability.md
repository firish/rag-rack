# Integrate with your observability stack

Every `Answer` ships a JSON-serializable audit trail ready for emission to your metrics / logging / tracing pipeline.

## The audit dump

`Answer.audit_trail()` returns a flat dict with primitives only:

```python
{
  "query": "What is the mechanism of action of penicillin?",
  "strictness": "balanced",
  "was_refused": false,
  "refusal_reason": null,
  "faithfulness_score": 0.91,
  "faithfulness_components": {
    "retrieval_score": 0.84,
    "nli_score": 0.92,
    "generation_logprob": null
  },
  "n_sentences": 3,
  "n_supported": 3,
  "n_unsupported": 0,
  "n_verified": 3,
  "min_nli_score": 0.89,
  "mean_nli_score": 0.92,
  "unsupported_claims": [],
  "cited_sentence_ids": ["paper::s12", "paper::s14"],
  "n_retrieved_chunks": 10
}
```

`json.dumps(answer.audit_trail())` works directly — no custom encoder needed.

## Pattern 1: structured logs

```python
import logging
import json

log = logging.getLogger("verifiable_rag")

answer = pipeline.ask(query)
log.info("answer", extra={"audit": answer.audit_trail()})
```

With a JSON log formatter (e.g. `python-json-logger`), each line is a structured record you can query in Splunk, Datadog Logs, etc.

## Pattern 2: metrics emit

```python
from prometheus_client import Counter, Histogram, Summary

faithfulness_score = Histogram(
    "vrag_faithfulness_score",
    "Per-query faithfulness score",
    buckets=[0.0, 0.5, 0.7, 0.9, 1.0],
)
refusal_counter = Counter("vrag_refusals_total", "Refusals")
unsupported_summary = Summary("vrag_unsupported_count", "Unsupported sentences per answer")

answer = pipeline.ask(query)
audit = answer.audit_trail()

faithfulness_score.observe(audit["faithfulness_score"])
unsupported_summary.observe(audit["n_unsupported"])
if audit["was_refused"]:
    refusal_counter.inc()
```

## Pattern 3: OpenTelemetry tracing

Attach the audit dump as span attributes:

```python
from opentelemetry import trace

tracer = trace.get_tracer("verifiable_rag")

with tracer.start_as_current_span("verifiable_rag.ask") as span:
    answer = pipeline.ask(query)
    audit = answer.audit_trail()
    span.set_attributes({
        f"vrag.{k}": v if isinstance(v, (str, int, float, bool)) else json.dumps(v)
        for k, v in audit.items()
    })
```

The audit dict is shallow-ish; complex values (lists, nested dicts) get JSON-stringified to fit OpenTelemetry's attribute constraints.

## Pattern 4: alerting on faithfulness regressions

The audit_trail values are stable — same query, same docs, same threshold should produce the same `faithfulness_score`. So you can alert on regressions:

```python
# At deploy time, record per-query baseline scores
baseline = {
    "What did the authors find?": 0.92,
    "What methodology did they use?": 0.88,
    # ...
}

# In CI / canary
for query, expected in baseline.items():
    audit = pipeline.ask(query).audit_trail()
    actual = audit["faithfulness_score"]
    assert actual >= expected - 0.05, f"regression: {query} dropped from {expected} to {actual}"
```

Pin the LLM model version (`generator_model="anthropic/claude-haiku-4-5-20251001"` not `"anthropic/claude-haiku-4-5"`) so model updates don't silently shift scores.

## Per-sentence detail when you need it

`audit_trail()` is a summary. For per-sentence detail, walk the underlying lists:

```python
answer = pipeline.ask(query)
for i, sentence in enumerate(answer.sentences):
    vr = answer.verification_for(i)
    log.info(
        "sentence",
        extra={
            "sentence_idx": i,
            "text": sentence.text,
            "cite_ids": list(sentence.supporting_sentence_ids),
            "nli_score": vr.nli_score if vr else None,
            "is_supported": vr.is_supported if vr else None,
        }
    )
```

This produces N log records per query (one per sentence). Useful for debugging specific failures; too noisy for production at scale.

## Pattern 5: capture the HTML for replay

For high-stakes use cases (legal, medical), persist the full HTML report alongside the answer:

```python
from pathlib import Path
import hashlib
import time

answer = pipeline.ask(query)

# Stable filename per-query so re-runs can be diffed
qid = hashlib.sha256(query.encode()).hexdigest()[:12]
report_path = Path(f"reports/{int(time.time())}_{qid}.html")
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(answer.to_html(title=query[:80]))

# Persist the audit dump as the index entry
audit = answer.audit_trail()
audit["report_path"] = str(report_path)
log.info("answer", extra={"audit": audit})
```

The HTML report is self-contained — opens in any browser, no server needed. Six months from now you can pull up the exact decision path for a flagged answer.

## What to alert on

| Signal | Alert when... | Why |
|---|---|---|
| `faithfulness_score` regressions | drops > 5pp on baseline queries | Pipeline degradation (bad model swap, retrieval issue) |
| `was_refused` rate | rises by >20% week-over-week | Either the threshold is too aggressive or the input distribution shifted |
| `n_unsupported / n_sentences` average | rises | Generator is hallucinating more — investigate the generator model or prompt |
| `min_nli_score` distribution | bimodal collapse | Verifier is producing degenerate scores (often a model loading bug) |

These give you visibility before user-facing problems show up.
