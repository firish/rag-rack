"""LitQA2 — FutureHouse's scientific-literature multi-choice benchmark.

LitQA2 (part of LAB-Bench) is 199 multiple-choice questions about findings
in published papers, designed to require **full-text** access (not just
abstracts). Originally designed for PaperQA2 / agentic retrieval systems,
it's the canonical external benchmark for our use case.

Source: https://huggingface.co/datasets/futurehouse/lab-bench (LitQA2 split).

Pipeline shape
--------------
Each question maps to one source paper (DOI). We ingest the paper's PDF
into the pipeline's corpus, then ask the question. Multiple questions may
share the same DOI (rare); the runner dedupes by absolute path.

Gold annotations
----------------
LitQA2 ships with a ``key-passage`` field — the actual sentences from the
source paper that contain the answer. ``scripts/fetch_litqa2.py`` runs
fuzzy text alignment (rapidfuzz) between that gold passage and our
parsed sentences, storing the matching ``sentence_ids`` in the index
under ``key_passage_sentence_ids``. This benchmark adapter surfaces those
IDs as ``gold_sentence_ids`` so our citation precision/recall metrics
become "did you cite a sentence inside the gold passage?" — a real
signal, not vacuous.

If the index has no ``key_passage_sentence_ids`` for a question (older
indexes pre-dating the alignment step, or alignment failed), we fall back
to ``frozenset()`` and the citation metric on that question is vacuous.

For multi-choice accuracy (the canonical LitQA2 metric, comparable to
PaperQA2's reported numbers), we use a separate :func:`multi_choice_accuracy`
metric that substring-matches the LLM's answer text against the
``ideal``/``distractors`` options.

PDF availability
----------------
Not all LitQA2 papers are fetchable through legitimate channels (~60-70%
on our end). The benchmark adapter reads the index file produced by
``scripts/fetch_litqa2.py`` and **skips questions whose PDF wasn't
fetched** with a logged warning. Pass ``allow_missing=True`` to include
them anyway (they'll error out at ingest time).
"""

from __future__ import annotations

import json
import logging
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from huggingface_hub import hf_hub_download

from verifiable_rag.eval import EvalQuestion

logger = logging.getLogger(__name__)

_HF_REPO = "futurehouse/lab-bench"
_HF_FILE = "LitQA2/train-00000-of-00001.parquet"

# Default index location written by scripts/fetch_litqa2.py
_DEFAULT_INDEX = Path(".verifiable_rag_cache/litqa2_pdfs/_index.json")

# When the LLM's choice should be treated as a refusal (matches the LitQA2
# convention for "Insufficient information to answer").
_INSUFFICIENT_PREFIXES = ("insufficient", "not enough", "cannot determine")


class LitQA2Bench:
    """LitQA2 (199 scientific-paper multi-choice questions) as a Benchmark.

    Parameters
    ----------
    index_path:
        JSON index produced by ``scripts/fetch_litqa2.py`` mapping
        question_id → fetched PDF path. Defaults to the standard cache
        location.
    allow_missing:
        If True, yield questions even when the PDF wasn't fetched. The
        runner will then surface the ingest error per question. Default
        False — skips with a warning.
    max_questions:
        Optional cap (for fast smoke runs).
    """

    name: str = "litqa2"

    def __init__(
        self,
        index_path: Path = _DEFAULT_INDEX,
        allow_missing: bool = False,
        max_questions: int | None = None,
    ) -> None:
        self._index_path = Path(index_path)
        self._allow_missing = allow_missing
        self._max_questions = max_questions

        if not self._index_path.exists():
            raise FileNotFoundError(
                f"LitQA2 PDF index not found at {self._index_path}. "
                f"Run `python scripts/fetch_litqa2.py` first to fetch papers."
            )

    def questions(self) -> Iterator[EvalQuestion]:
        index = json.loads(self._index_path.read_text())

        # Load the original LitQA2 parquet (cached by HF)
        parquet_path = hf_hub_download(
            repo_id=_HF_REPO,
            filename=_HF_FILE,
            repo_type="dataset",
        )
        import pandas as pd  # type: ignore[import-untyped]

        df = pd.read_parquet(parquet_path)

        skipped = 0
        emitted = 0
        for _, row in df.iterrows():
            qid = str(row["id"])
            entry = index.get(qid, {})
            pdf_path = entry.get("path")

            if not pdf_path:
                if self._allow_missing:
                    pdf_path = ""  # runner will hit FileNotFoundError on ingest
                else:
                    skipped += 1
                    continue
            elif not Path(str(pdf_path)).exists():
                # Index claims a PDF path but the file is gone — same as missing
                skipped += 1
                continue

            ideal = str(row["ideal"]).strip()
            should_refuse = self._is_refusal_answer(ideal)

            distractors_raw = row["distractors"]
            distractors_clean = (
                [str(d).strip() for d in distractors_raw]
                if distractors_raw is not None
                else []
            )
            # Embed MC options in the question text so the LLM can select the
            # best-matching option rather than trying to produce a verbatim
            # match (which causes over-refusal on near-matches like 12,309 vs
            # 12,300). This mirrors PaperQA2's approach for LitQA2.
            # Sort alphabetically for a deterministic, position-bias-free order.
            options = sorted(
                distractors_clean + [ideal, "Insufficient information to answer"],
                key=str.lower,
            )
            options_block = "\n".join(f"  - {opt}" for opt in options)
            formatted_question = (
                f"{str(row['question']).strip()}\n\n"
                f"Select the best answer from these options:\n{options_block}"
            )

            # If the index has key_passage_sentence_ids for this question
            # (computed by scripts/fetch_litqa2.py via rapidfuzz alignment),
            # surface them as gold. Otherwise we fall back to empty —
            # citation metrics will be vacuous for that question.
            kp_ids = entry.get("key_passage_sentence_ids") or []
            yield EvalQuestion(
                id=qid,
                question=formatted_question,
                document_paths=(Path(str(pdf_path)),) if pdf_path else (),
                gold_sentence_ids=frozenset(str(s) for s in kp_ids)
                if not should_refuse
                else frozenset(),
                should_refuse=should_refuse,
                gold_answer_text=ideal,
            )
            emitted += 1
            if self._max_questions is not None and emitted >= self._max_questions:
                break

        if skipped:
            logger.warning(
                "LitQA2: skipped %d questions whose PDFs weren't fetched "
                "(set allow_missing=True to include them)",
                skipped,
            )

    @staticmethod
    def _is_refusal_answer(ideal: str) -> bool:
        """Detect LitQA2's 'Insufficient information' style answers.

        Also matches the literal string ``"null"`` — a handful of LitQA2
        rows have ``ideal='null'`` for genuinely unanswerable questions
        (e.g. PLSCR5/GARIN3 questions where the paper doesn't cover the
        requested entity). Treating them as ``should_refuse=True`` keeps
        abstention metrics honest.
        """
        lowered = ideal.lower().strip()
        if lowered == "null":
            return True
        return any(lowered.startswith(p) for p in _INSUFFICIENT_PREFIXES)


# --------------------------------------------------------------------------- #
# LitQA2-specific gold reader (used by the runner / metrics)
# --------------------------------------------------------------------------- #


def load_litqa2_meta(index_path: Path = _DEFAULT_INDEX) -> dict[str, dict[str, Any]]:
    """Load the multi-choice metadata (ideal + distractors) for LitQA2.

    Returns a dict ``{question_id -> {"ideal": str, "distractors": [str, ...],
    "key_passage": str}}`` so the multi-choice metric can score outputs
    without re-loading the parquet.
    """
    parquet_path = hf_hub_download(
        repo_id=_HF_REPO,
        filename=_HF_FILE,
        repo_type="dataset",
    )
    import pandas as pd

    df = pd.read_parquet(parquet_path)
    out: dict[str, dict[str, Any]] = {}
    for _, row in df.iterrows():
        distractors_raw = row["distractors"]
        # ``row["distractors"]`` comes back from parquet as a numpy array, which
        # makes ``arr or []`` raise "truth value ambiguous". Iterate over the
        # raw value (numpy arrays are iterable); None becomes an empty list.
        distractors_iter = distractors_raw if distractors_raw is not None else []
        out[str(row["id"])] = {
            "ideal": str(row["ideal"]).strip(),
            "distractors": [str(d).strip() for d in distractors_iter],
            "key_passage": str(row.get("key-passage", "") or ""),
        }
    return out
