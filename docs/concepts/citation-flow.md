# Citation flow

How a citation gets from "LLM emitted some text" to "user clicks a link and sees the supporting source span."

## Three citation modes

The library ships three generators that produce sentence-level citations:

| Generator | What it does | When to use |
|---|---|---|
| `PromptedCitedGenerator` | LLM is told via prompt to cite by sentence ID. Works with any model. | Local models without structured output (Llama, Mistral via Ollama) |
| `ConstrainedCitedGenerator` ⭐ | Schema-forced JSON output with cite IDs from an enum. Works with Anthropic, OpenAI, Gemini. | **Default — published baseline.** Higher recall, no invented IDs. |
| `SAFECitedGenerator` | Atomic-claim decomposition + per-claim cites. ReClaim/SAFE-style. | Domains with rich multi-claim sentences (legal, scientific narrative) |

The library defaults to `ConstrainedCitedGenerator` because it's the configuration that achieves the published 0.875 mc_accuracy on LitQA2 and the +4–7 F1 lift on ALCE.

## What the generator emits

Every generator produces a `list[CitedSentence]`:

```python
@dataclass(frozen=True)
class CitedSentence:
    text: str
    supporting_sentence_ids: tuple[str, ...]
    confidence: float  # [0, 1] — generator-side, before verification
```

For example, given the query *"What is the mechanism of action of penicillin?"*, the generator might emit:

```python
[
    CitedSentence(
        text="Penicillin binds covalently to penicillin-binding proteins.",
        supporting_sentence_ids=("paper::s12", "paper::s13"),
        confidence=0.94,
    ),
    CitedSentence(
        text="This prevents the cross-linking step in bacterial cell wall synthesis.",
        supporting_sentence_ids=("paper::s14",),
        confidence=0.91,
    ),
]
```

Each `supporting_sentence_ids` entry is a **stable** ID pointing at a specific `Sentence` in the parsed `Document`. The ID format encodes the source doc — typically `"<doc_id>::s<sentence_index>"`.

## What the verifier does

For each `CitedSentence`, the verifier:

1. Looks up the supporting sentences from the `Document` (via `document.sentence_by_id(sid)`)
2. Concatenates their text into a "premise"
3. Runs the (premise, generated sentence) pair through the NLI scorer
4. Produces a `VerificationResult`:

```python
@dataclass(frozen=True)
class VerificationResult:
    cited_sentence_index: int
    claim_text: str
    is_supported: bool   # NLI score ≥ threshold
    nli_score: float     # [0, 1] entailment probability
```

The verifier checks the **specific cited sentences**, not the full chunk the generator saw. This deliberately catches the failure mode where the LLM cites `paper::s12` but the actual support is `paper::s14` in the same chunk.

## How citations become anchor links

The HTML audit report walks every `CitedSentence` and emits its citations as anchor links into the passage list:

```html
<span class='sentence supported'>
  Penicillin binds covalently to penicillin-binding proteins.
  <a class='cite' href='#chunk-paper::c3'>[paper::s12]</a>
  <a class='cite' href='#chunk-paper::c3'>[paper::s13]</a>
</span>
```

The anchor target (`#chunk-paper::c3`) corresponds to the retrieved chunk that *contains* the cited sentence. Click the cite, the page scrolls to the passage card showing the full source text, the chunk ID, the retrieval method, and the retrieval score.

See [Render audit HTML](../how-to/render-audit-html.md) for the full report walkthrough.

## Sentence ID conventions

| Source | ID format | Example |
|---|---|---|
| `DoclingParser`, `PyMuPDFParser` | `"<content_hash_prefix>::s<idx>"` | `"3f7c14...::s17"` |
| Test fixtures (via `build_document`) | `"<doc_id>::s<idx>"` | `"paper::s17"` |
| ALCE synthetic passages | `"alce::<qid>::p<i>"` | `"alce::asqa_42::p3"` |

Whatever the convention, the contract is that `document.sentence_by_id(sid)` returns the source `Sentence` and `sentence.span` returns the `(char_start, char_end)` that the parser observed.

## What if the LLM invents an ID?

Two protections:

1. **`ConstrainedCitedGenerator`** uses a JSON schema with `cite_ids: array[enum]` where the enum is the *actual* sentence IDs in the retrieved chunks. Invented IDs are rejected at decode time — the LLM can't produce them.
2. **The verifier** silently treats invented IDs as empty premises (the `Document` doesn't contain them), so the NLI score is 0 and the sentence is flagged unsupported.

The combination means: invented cites in the generator output produce sentences flagged as unsupported in the audit trail. They never silently pass through.

## Citation precision vs. recall

The published ALCE result quantifies this:

| Generator | Precision | Recall | F1 |
|---|---|---|---|
| Prompted | 0.83 | 0.47 | 0.46 |
| Constrained | 0.67 | 0.48 | 0.47 |
| SAFE | 0.65 | 0.50 | 0.48 |

**Prompted is more conservative** — it cites less, but is right when it does. **Constrained casts a wider net** — recall goes up, precision drops, F1 ends up roughly flat. For benchmarks like ALCE that score `citation_f1`, the choice is a wash; for benchmarks like LitQA2 that score `mc_accuracy`, constrained's "wider net" produces a meaningful lift because the LLM has more chances to land on the right answer option.

See the [ALCE benchmark report](https://github.com/firish/rag-rack/blob/main/benchmarks/PUBLISHED_alce.md) for the dual-judge cross-validation that establishes this isn't a Haiku-judge artifact.

## Programmatic access

The full audit trail is on the `Answer` object:

```python
answer = pipeline.ask("What is the mechanism of penicillin?")

answer.sentences                    # list[CitedSentence]
answer.verification_results         # list[VerificationResult]
answer.cited_sentence_ids           # frozenset of every source ID cited
answer.supported_sentences          # CitedSentences that passed verification
answer.unsupported_sentences        # CitedSentences flagged unsupported

# Look up the source span for a cited sentence:
for cs in answer.sentences:
    for sid in cs.supporting_sentence_ids:
        sentence = answer.retrieved_chunks[0].chunk  # or lookup via document
        # ... do something with the span
```

For a self-contained HTML view of all of this, use `answer.to_html()` — see [Render audit HTML](../how-to/render-audit-html.md).
