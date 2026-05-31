"""HTML report rendering for an :class:`Answer` — the audit-trail view.

Produces a self-contained HTML page (inline CSS, no JS, no external deps)
showing:

1. The query and the final answer
2. Per-sentence verification badges (supported / unsupported / NLI score)
3. The faithfulness score with its components
4. The reranked passages the generator saw, with retrieval scores
5. Citations rendered as inline anchor links to the supporting passages

The purpose is to make verifiable-rag actually *verifiable* by the human
who's reading the answer — every claim's audit path is one click away.

Usage::

    answer = pipeline.ask("What did the authors find?")
    Path("report.html").write_text(answer.to_html())

Or via the top-level ``ask`` helper::

    verifiable_rag.ask(
        "What did the authors find?",
        docs="paper.pdf",
        output_html="report.html",
    )
"""

from __future__ import annotations

import html
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from verifiable_rag.models.answer import Answer


_CSS = """
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
       max-width: 980px; margin: 2em auto; padding: 0 1.5em; color: #1a1a1a;
       line-height: 1.5; }
header { border-bottom: 1px solid #eaeaea; padding-bottom: 1em; margin-bottom: 1.5em; }
h1 { font-size: 1.4em; margin: 0; }
h2 { font-size: 1.1em; margin-top: 2em; color: #444; border-bottom: 1px solid #eee;
     padding-bottom: 0.3em; }
.meta { color: #666; font-size: 0.9em; }
.query { background: #f8f8f8; padding: 1em; border-left: 3px solid #888;
         border-radius: 0 4px 4px 0; }
.answer { background: #fafffa; padding: 1em; border-radius: 4px;
          border: 1px solid #cce5cc; }
.sentence { display: inline; }
.sentence.unsupported { background: #fff0f0; border-bottom: 1px dashed #cc6666; }
.sentence.supported { background: transparent; }
.cite-list { display: inline; white-space: nowrap; }
.cite { font-size: 0.78em; color: #1565c0; text-decoration: none;
        vertical-align: super; margin: 0 1px; }
.cite:hover { text-decoration: underline; }
.refused { background: #fff3e0; border-left: 4px solid #f57c00; padding: 1em;
           margin: 1em 0; }
table.verify { border-collapse: collapse; width: 100%; margin-top: 0.5em; font-size: 0.92em; }
table.verify th, table.verify td { padding: 0.5em 0.75em; text-align: left;
                                    border-bottom: 1px solid #eee; vertical-align: top; }
table.verify th { background: #f6f6f6; font-weight: 600; }
.score { font-family: "SF Mono", Menlo, monospace; font-size: 0.92em; color: #333; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 12px;
         font-size: 0.78em; font-weight: 600; }
.badge.ok { background: #d4edda; color: #155724; }
.badge.bad { background: #f8d7da; color: #721c24; }
.chunk { border: 1px solid #e0e0e0; padding: 1em; margin: 0.5em 0;
         border-radius: 4px; }
.chunk-header { color: #555; font-size: 0.88em; margin-bottom: 0.5em;
                font-family: "SF Mono", Menlo, monospace; }
.chunk-text { color: #222; white-space: pre-wrap; }
.faithfulness { display: flex; gap: 1em; flex-wrap: wrap; margin: 1em 0; }
.fcard { background: #f4f8ff; padding: 0.8em 1.2em; border-radius: 6px;
         border: 1px solid #cfdcf3; min-width: 140px; }
.fcard .label { color: #666; font-size: 0.85em; }
.fcard .value { font-size: 1.3em; font-weight: 600; color: #1a3a6e; }
footer { color: #888; font-size: 0.85em; text-align: center; margin-top: 2em;
         padding-top: 1em; border-top: 1px solid #eee; }
"""


def to_html(answer: "Answer", title: str = "verifiable-rag report") -> str:
    """Render *answer* as a self-contained HTML page string.

    Pure-Python, no Jinja or external template dep. Returns the full HTML
    document; caller writes to a file or serves it as needed.
    """
    parts: list[str] = []
    parts.append(
        "<!DOCTYPE html>\n<html lang='en'>\n<head>\n"
        f"<meta charset='utf-8'><title>{html.escape(title)}</title>\n"
        f"<style>{_CSS}</style>\n</head>\n<body>\n"
    )
    parts.append(f"<header><h1>{html.escape(title)}</h1>")
    verifier_ran = bool(answer.verification_results)
    faithfulness_label = (
        f"faithfulness={answer.faithfulness_score:.3f}"
        if verifier_ran
        else "no verifier configured"
    )
    parts.append(
        f"<div class='meta'>strictness={html.escape(str(answer.strictness))} · "
        f"refused={'yes' if answer.was_refused else 'no'} · "
        f"{faithfulness_label}</div></header>\n"
    )

    # Query
    parts.append("<h2>Query</h2>")
    parts.append(f"<div class='query'>{html.escape(answer.query)}</div>")

    # Refusal banner (when applicable)
    if answer.was_refused:
        parts.append(
            f"<div class='refused'><strong>Refused.</strong> "
            f"{html.escape(answer.refusal_reason or 'no reason given')}</div>"
        )

    # Answer with inline citations + verification color coding
    parts.append("<h2>Answer</h2>")
    parts.append(_render_answer_body(answer))

    # Faithfulness card row — only meaningful when a verifier ran. Skip the
    # section entirely when no verifier was configured to avoid surfacing
    # an uninterpretable 1.0 default + a raw retrieval scalar.
    if verifier_ran:
        parts.append("<h2>Faithfulness</h2>")
        parts.append(_render_faithfulness(answer))

    # Per-sentence verification table
    if answer.verification_results:
        parts.append("<h2>Per-sentence verification</h2>")
        parts.append(_render_verification_table(answer))

    # Reranked passages the generator saw
    if answer.retrieved_chunks:
        parts.append(
            f"<h2>Reranked passages ({len(answer.retrieved_chunks)})</h2>"
        )
        parts.append(_render_passages(answer))

    parts.append(
        "<footer>Generated by "
        "<a href='https://github.com/firish/rag-rack'>verifiable-rag</a></footer>"
    )
    parts.append("</body></html>")
    return "".join(parts)


# --------------------------------------------------------------------------- #
# Section renderers
# --------------------------------------------------------------------------- #


def _render_answer_body(answer: "Answer") -> str:
    """Render the answer text with per-sentence verification color + cite links."""
    if not answer.sentences:
        return "<div class='answer'><em>(no answer produced)</em></div>"

    is_supported_by_idx = {
        vr.cited_sentence_index: vr.is_supported for vr in answer.verification_results
    }

    out: list[str] = ["<div class='answer'>"]
    for i, sent in enumerate(answer.sentences):
        supported = is_supported_by_idx.get(i, True)
        cls = "sentence supported" if supported else "sentence unsupported"
        out.append(f"<span class='{cls}'>{html.escape(sent.text)}")
        if sent.supporting_sentence_ids:
            out.append("<span class='cite-list'>")
            for cid in sent.supporting_sentence_ids:
                anchor = _chunk_anchor_for_sentence_id(cid, answer)
                if anchor:
                    out.append(
                        f"<a class='cite' href='#{html.escape(anchor)}'>"
                        f"[{html.escape(cid)}]</a>"
                    )
                else:
                    out.append(f"<span class='cite'>[{html.escape(cid)}]</span>")
            out.append("</span>")
        out.append("</span> ")
    out.append("</div>")
    return "".join(out)


def _render_faithfulness(answer: "Answer") -> str:
    fc = answer.faithfulness_components
    out = ["<div class='faithfulness'>"]
    out.append(
        f"<div class='fcard'><div class='label'>overall</div>"
        f"<div class='value'>{answer.faithfulness_score:.3f}</div></div>"
    )
    out.append(
        f"<div class='fcard'><div class='label'>retrieval</div>"
        f"<div class='value'>{fc.retrieval_score:.3f}</div></div>"
    )
    out.append(
        f"<div class='fcard'><div class='label'>NLI</div>"
        f"<div class='value'>{fc.nli_score:.3f}</div></div>"
    )
    if fc.generation_logprob is not None:
        out.append(
            f"<div class='fcard'><div class='label'>gen logprob</div>"
            f"<div class='value'>{fc.generation_logprob:.3f}</div></div>"
        )
    out.append("</div>")
    return "".join(out)


def _render_verification_table(answer: "Answer") -> str:
    rows = []
    rows.append(
        "<table class='verify'><thead><tr><th>#</th><th>Sentence</th>"
        "<th>Supported?</th><th>NLI score</th></tr></thead><tbody>"
    )
    for vr in answer.verification_results:
        badge_cls = "badge ok" if vr.is_supported else "badge bad"
        badge_text = "supported" if vr.is_supported else "unsupported"
        rows.append(
            f"<tr><td>{vr.cited_sentence_index}</td>"
            f"<td>{html.escape(vr.claim_text)}</td>"
            f"<td><span class='{badge_cls}'>{badge_text}</span></td>"
            f"<td class='score'>{vr.nli_score:.3f}</td></tr>"
        )
    rows.append("</tbody></table>")
    return "".join(rows)


def _render_passages(answer: "Answer") -> str:
    parts: list[str] = []
    for i, rc in enumerate(answer.retrieved_chunks):
        anchor = f"chunk-{rc.chunk.chunk_id}"
        parts.append(f"<div class='chunk' id='{html.escape(anchor)}'>")
        parts.append(
            f"<div class='chunk-header'>"
            f"#{i + 1} · <strong>{html.escape(rc.chunk.chunk_id)}</strong> · "
            f"{html.escape(rc.retrieval_method)} score={rc.score:.3f}</div>"
        )
        parts.append(
            f"<div class='chunk-text'>{html.escape(rc.chunk.text)}</div>"
        )
        parts.append("</div>")
    return "".join(parts)


def _chunk_anchor_for_sentence_id(sentence_id: str, answer: "Answer") -> str | None:
    """Return the chunk anchor that contains *sentence_id*, or None."""
    for rc in answer.retrieved_chunks:
        if sentence_id in rc.chunk.sentence_ids:
            return f"chunk-{rc.chunk.chunk_id}"
    return None


__all__ = ["to_html"]
