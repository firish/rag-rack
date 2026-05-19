"""ALCE — Princeton's citation-quality benchmark (EMNLP 2023).

Three sub-benchmarks share the canonical ``princeton-nlp/ALCE-data`` archive:
  * ASQA      (factoid Q&A with answer ambiguity)
  * QAMPARI   (multi-hop factoid Q&A — answers are sets)
  * ELI5      (long-form Q&A — long answers, BM25 + reranker retrieval)

For each example, ALCE ships **pre-retrieved supporting passages** so the
benchmark scores generator+citation quality with retrieval held constant.
That's exactly the design we want for the first run: a clean test of "given
the right context, does our generator pick the right cites?", with no
confound from our hybrid retriever.

Architectural note
------------------
ALCE's "passages-per-question" model is incompatible with the standard
runner's "ingest a shared corpus once, query against it" model, so the
ALCE benchmark has its own runner in ``verifiable_rag.eval.runners``.
This adapter therefore yields ``EvalQuestion`` instances with
``document_paths=()`` and exposes a separate :meth:`passages_for`
accessor that the custom runner consumes.

Synthetic doc/sentence model
----------------------------
Each ALCE passage is mapped to one Sentence inside one Section inside
the question's synthetic ``Document``. Sentence IDs follow the format
``f"alce::{qid}::p{i}"`` where *i* is the passage's 0-indexed position.
That makes citation metrics work unchanged on top of ``cited_sentence_ids``.

Gold extraction
---------------
ASQA includes ``qa_pairs`` (sub-questions with short_answers) and per-passage
``answers_found`` lists. A passage counts as gold-supporting iff *any* of
its ``answers_found`` entries is 1. QAMPARI / ELI5 use slightly different
gold formats; this adapter focuses on the **oracle** ASQA file for the
first iteration and will grow QAMPARI / ELI5 support as we run them.

Files supported
---------------
Only the ``*_reranked_oracle.json`` files are wired up initially — they
have ~5 passages per question (already filtered to plausible supporters)
which keeps eval cost low for the first round. Top-100 variants are a
trivial extension once we want a harder test.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from verifiable_rag.eval import EvalQuestion

logger = logging.getLogger(__name__)


_ALCE_CACHE = Path(".verifiable_rag_cache/alce/ALCE-data")

# Each entry: (eval_file_under_ALCE-data/, gold_strategy, id_field)
# - gold_strategy: enum controlling how gold passage IDs are derived from the
#   example's annotations. Only ASQA's oracle file has per-passage flags
#   (`answers_found`); the other files have no per-passage gold so the proxy
#   metric is vacuous and the LLM-judge is the canonical scorer.
# - id_field: name of the example field that holds the question ID.
#   ``None`` means the file has no ID field and we synthesise one from the
#   row index (ELI5).
_SUBBENCHES: dict[str, tuple[str, str, str | None]] = {
    # ASQA — sample_id field, oracle has answers_found flags
    "alce_asqa_oracle": ("asqa_eval_gtr_top100_reranked_oracle.json", "asqa_oracle", "sample_id"),
    "alce_asqa_gtr": ("asqa_eval_gtr_top100.json", "asqa_oracle", "sample_id"),
    "alce_asqa_dpr": ("asqa_eval_dpr_top100.json", "asqa_oracle", "sample_id"),
    # QAMPARI — multi-hop factoid with entity-set answers; ID field is `id`.
    # No per-passage gold flags → proxy metric vacuous; use LLM-judge.
    "alce_qampari_gtr": ("qampari_eval_gtr_top100.json", "vacuous", "id"),
    "alce_qampari_dpr": ("qampari_eval_dpr_top100.json", "vacuous", "id"),
    # ELI5 — long-form Q&A from Sphere/CommonCrawl via BM25.
    # No ID field at all; synthesise from row index. Each example has a
    # ``claims`` field with pre-decomposed atomic claims — interesting for
    # future SAFE-style scoring but not used here.
    "alce_eli5_bm25": ("eli5_eval_bm25_top100.json", "vacuous", None),
}


def _gold_passage_indices_asqa(example: dict[str, Any]) -> set[int]:
    """ASQA: a passage is gold if any ``answers_found`` flag is set.

    Falls back to an empty set when the file lacks ``answers_found``
    (the non-oracle variants do; metrics will be vacuous for those).
    """
    gold: set[int] = set()
    for i, doc in enumerate(example.get("docs") or []):
        flags = doc.get("answers_found")
        if flags and any(int(f) > 0 for f in flags):
            gold.add(i)
    return gold


def _gold_passage_indices(example: dict[str, Any], strategy: str) -> set[int]:
    if strategy == "asqa_oracle":
        return _gold_passage_indices_asqa(example)
    if strategy == "vacuous":
        # No per-passage gold — proxy metrics will be vacuous. The LLM-judge
        # is the canonical scorer for these sub-benchmarks.
        return set()
    raise ValueError(f"Unknown ALCE gold strategy {strategy!r}")


def _extract_qid(example: dict[str, Any], id_field: str | None, row_index: int) -> str:
    """Extract the question ID from an ALCE example. Synthesises from row
    index when the file has no ID field (ELI5).
    """
    if id_field is None:
        return f"row_{row_index:04d}"
    return str(example[id_field])


class ALCEBench:
    """ALCE benchmark adapter.

    Parameters
    ----------
    subbench:
        One of :data:`_SUBBENCHES` keys (e.g. ``"alce_asqa_oracle"``).
    cache_root:
        Where the extracted ``ALCE-data/`` tree lives. Defaults to the
        path produced by ``scripts/fetch_alce.py``.
    max_questions:
        Optional cap (smoke runs).
    """

    def __init__(
        self,
        subbench: str = "alce_asqa_oracle",
        cache_root: Path = _ALCE_CACHE,
        max_questions: int | None = None,
    ) -> None:
        if subbench not in _SUBBENCHES:
            raise ValueError(
                f"Unknown ALCE sub-benchmark {subbench!r}; choose one of "
                f"{sorted(_SUBBENCHES)}"
            )
        filename, gold_strategy, id_field = _SUBBENCHES[subbench]
        self.name = subbench
        self._gold_strategy = gold_strategy
        self._id_field = id_field
        self._path = Path(cache_root) / filename
        self._max_questions = max_questions

        if not self._path.exists():
            raise FileNotFoundError(
                f"ALCE data not found at {self._path}. "
                f"Run `python scripts/fetch_alce.py` first."
            )

        # Lazy load — but cheap enough to load eagerly for these file sizes
        self._examples: list[dict[str, Any]] = json.loads(self._path.read_text())
        if self._max_questions is not None:
            self._examples = self._examples[: self._max_questions]

        # Pre-compute qids in row order so passages_for() and questions() agree.
        self._qids: list[str] = [
            _extract_qid(ex, id_field, i) for i, ex in enumerate(self._examples)
        ]
        # Index by qid so the custom runner can look up passages
        self._by_qid: dict[str, dict[str, Any]] = dict(zip(self._qids, self._examples, strict=True))

    # ------------------------------------------------------------------ #
    # Benchmark Protocol
    # ------------------------------------------------------------------ #

    def questions(self) -> Iterator[EvalQuestion]:
        for qid, ex in zip(self._qids, self._examples, strict=True):
            gold_idxs = _gold_passage_indices(ex, self._gold_strategy)
            gold_ids = frozenset(_passage_sentence_id(qid, i) for i in gold_idxs)
            # ALCE answers are always answerable from the attached passages —
            # there's no "should refuse" notion. Refusal would be a model error.
            yield EvalQuestion(
                id=qid,
                question=str(ex["question"]).strip(),
                document_paths=(),  # passages are pre-attached, no filesystem ingest
                gold_sentence_ids=gold_ids,
                should_refuse=False,
                gold_answer_text=str(ex.get("answer") or "").strip() or None,
            )

    # ------------------------------------------------------------------ #
    # ALCE-specific: per-question passage access (used by run_alce)
    # ------------------------------------------------------------------ #

    def passages_for(self, qid: str) -> list[dict[str, Any]]:
        """Return the raw passage dicts for a question."""
        return list(self._by_qid[qid].get("docs") or [])

    def example_for(self, qid: str) -> dict[str, Any]:
        """Return the full raw example (qa_pairs, annotations, etc.)."""
        return self._by_qid[qid]


# --------------------------------------------------------------------- #
# Helpers — passage → sentence ID + synthetic Document construction
# --------------------------------------------------------------------- #


def _passage_sentence_id(qid: str, passage_idx: int) -> str:
    """Canonical sentence ID for an ALCE passage. Must embed doc_id."""
    return f"alce::{qid}::p{passage_idx}"


def passage_doc_id(qid: str) -> str:
    return f"alce::{qid}"


def supported_subbenches() -> tuple[str, ...]:
    return tuple(_SUBBENCHES.keys())
