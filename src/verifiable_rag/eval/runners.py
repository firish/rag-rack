"""Eval runner — orchestrates benchmark execution and produces an EvalReport.

The runner:
  1. Walks the benchmark to collect every unique document path.
  2. Ingests each document into the pipeline EXACTLY ONCE (sharing the
     index across all questions).
  3. Runs ``pipeline.ask(question)`` for each EvalQuestion. With
     ``max_workers > 1``, asks run concurrently via a ThreadPoolExecutor;
     the LLM call dominates wall time and releases the GIL while waiting
     on the network, so threads scale linearly until the model's rate
     limit kicks in.
  4. Wraps the answer into an EvalRecord (catching pipeline errors so one
     bad question doesn't tank the whole run).
  5. Scores all records and returns a populated EvalReport.

Errors are recorded on the EvalRecord rather than raised — this lets a long
benchmark survive a single LLM timeout or rate-limit blip.
"""

from __future__ import annotations

import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from verifiable_rag.eval import Benchmark, EvalQuestion, EvalRecord, EvalReport
from verifiable_rag.eval.metrics import score_records
from verifiable_rag.pipeline import Pipeline


def run_benchmark(
    pipeline: Pipeline,
    benchmark: Benchmark,
    pipeline_label: str = "baseline",
    max_questions: int | None = None,
    progress: bool = True,
    delay_between_questions: float = 0.0,
    max_workers: int = 1,
    ingest_workers: int = 1,
) -> EvalReport:
    """Run *benchmark* through *pipeline* and return a scored EvalReport.

    Args:
        pipeline: configured Pipeline (already wired with parser, chunker,
            embedder, indexer, generator).
        benchmark: any object satisfying the Benchmark protocol.
        pipeline_label: free-text label baked into the report (e.g. model name
            + chunker config) so reports are self-describing.
        max_questions: cap for fast smoke runs; None = run all questions.
        progress: print "[i/N] question" before each ask().
        delay_between_questions: seconds to sleep after each question. Only
            applied when running sequentially (max_workers == 1) — under
            concurrency the sleep doesn't pace the LLM in any useful way.
        max_workers: parallelism for ask(). 1 = sequential (default).
        ingest_workers: parallelism for the prepare phase of ingest
            (parse + chunk + embed). The commit phase (index write) is
            always serialised behind a lock for correctness.
    """
    questions = list(benchmark.questions())
    if max_questions is not None:
        questions = questions[:max_questions]

    # ---- 1) Ingest every unique document once ----------------------------
    # Tolerate per-PDF failures (corrupt files, image-only scans, etc.) so
    # one bad paper doesn't tank the whole benchmark run. We record which
    # paths failed and use that set in (2) to discard questions whose
    # sources didn't make it into the index.
    unique_paths: list[Path] = []
    seen_paths: set[str] = set()
    for q in questions:
        for path in q.document_paths:
            key = str(path.resolve())
            if key in seen_paths:
                continue
            seen_paths.add(key)
            unique_paths.append(path)

    failed_path_keys, parser_by_path = _ingest_paths(
        pipeline, unique_paths, ingest_workers, progress
    )

    # ---- 2) Drop questions whose every document failed to ingest ---------
    # If even one source PDF parsed, we keep the question — the retriever
    # can still find evidence in the surviving documents. We also build the
    # parsers_by_question_id map so the report carries native parser
    # provenance per question.
    asked_questions: list[EvalQuestion] = []
    discarded_ids: list[str] = []
    parsers_by_question_id: dict[str, list[str]] = {}
    for q in questions:
        if not q.document_paths:
            asked_questions.append(q)
            parsers_by_question_id[q.id] = []
            continue
        all_failed = all(
            str(p.resolve()) in failed_path_keys for p in q.document_paths
        )
        if all_failed:
            discarded_ids.append(q.id)
            if progress:
                print(f"[discard] {q.id}: all source PDFs failed to parse")
        else:
            asked_questions.append(q)
            parsers_by_question_id[q.id] = [
                parser_by_path.get(str(p.resolve()), "unknown")
                for p in q.document_paths
                if str(p.resolve()) not in failed_path_keys
            ]

    # ---- 3) Ask each surviving question, collect records ----------------
    gold_by_id: dict[str, tuple[frozenset[str], bool]] = {
        q.id: (q.gold_sentence_ids, q.should_refuse) for q in asked_questions
    }

    total = len(asked_questions)
    if max_workers > 1 and total > 1:
        records = _ask_parallel(pipeline, asked_questions, max_workers, progress)
    else:
        records = _ask_sequential(
            pipeline, asked_questions, progress, delay_between_questions
        )

    # ---- 4) Score and return --------------------------------------------
    report = EvalReport(
        benchmark_name=benchmark.name,
        pipeline_label=pipeline_label,
        records=records,
        discarded_question_ids=discarded_ids,
        parsers_by_question_id=parsers_by_question_id,
    )
    report.metrics = score_records(records, gold_by_id)
    report.metrics["n_discarded"] = float(len(discarded_ids))
    return report


def _ingest_paths(
    pipeline: Pipeline,
    paths: list[Path],
    workers: int,
    progress: bool,
) -> tuple[set[str], dict[str, str]]:
    """Ingest a list of unique paths.

    Returns ``(failed_keys, parser_by_path)`` where:
      * ``failed_keys`` is ``{str(path.resolve()) for every failed path}``
      * ``parser_by_path`` maps resolved path → ``Document.parser_name`` (or
        ``"unknown"`` if the parser didn't set it) for every *successful*
        ingest.
    """
    failed_keys: set[str] = set()
    parser_by_path: dict[str, str] = {}
    total = len(paths)
    if total == 0:
        return failed_keys, parser_by_path

    commit_lock = threading.Lock()
    counter = {"done": 0, "failed": 0}

    def _record_failure(path: Path, exc: BaseException) -> None:
        failed_keys.add(str(path.resolve()))
        counter["failed"] += 1
        counter["done"] += 1
        print(
            f"[ingest-FAIL {counter['done']}/{total}] {path}: "
            f"{type(exc).__name__}: {exc}",
            flush=True,
        )

    def _one(path: Path) -> None:
        try:
            prepared = pipeline.prepare_ingest(path)
        except Exception as exc:  # noqa: BLE001
            with commit_lock:
                _record_failure(path, exc)
            return
        document = prepared[0]  # (document, chunks, embeddings)
        with commit_lock:
            try:
                pipeline.commit_ingest(*prepared)
            except Exception as exc:  # noqa: BLE001
                _record_failure(path, exc)
                return
            parser_by_path[str(path.resolve())] = document.parser_name or "unknown"
            counter["done"] += 1
            if progress:
                print(f"[ingest {counter['done']}/{total}] {path}", flush=True)

    if workers > 1 and total > 1:
        if progress:
            print(
                f"[parallel-ingest] {total} docs with {workers} workers",
                flush=True,
            )
        with ThreadPoolExecutor(max_workers=workers) as pool:
            list(pool.map(_one, paths))
    else:
        for p in paths:
            _one(p)
    return failed_keys, parser_by_path


def _ask_sequential(
    pipeline: Pipeline,
    questions: list[EvalQuestion],
    progress: bool,
    delay_between_questions: float,
) -> list[EvalRecord]:
    records: list[EvalRecord] = []
    total = len(questions)
    for i, q in enumerate(questions, start=1):
        if progress:
            print(f"[ask {i}/{total}] {q.id}: {q.question}", flush=True)
        records.append(_ask_one(pipeline, q))
        if delay_between_questions and i < total:
            time.sleep(delay_between_questions)
    return records


def _ask_parallel(
    pipeline: Pipeline,
    questions: list[EvalQuestion],
    max_workers: int,
    progress: bool,
) -> list[EvalRecord]:
    """Run asks concurrently while preserving question order in the output.

    The Pipeline's per-ask state (retrieval → rerank → generate → verify) is
    read-only against the shared index and documents dict, so threads are
    safe. The LLM call is the long pole and releases the GIL; embed/rerank/
    verify steps are torch CPU ops that share the GIL but are tiny relative
    to the network round-trip.
    """
    total = len(questions)
    results: list[EvalRecord | None] = [None] * total
    print_lock = threading.Lock()
    counter = {"done": 0}

    def _run(idx: int, q: EvalQuestion) -> None:
        rec = _ask_one(pipeline, q)
        if progress:
            with print_lock:
                counter["done"] += 1
                print(f"[ask {counter['done']}/{total}] {q.id}: done", flush=True)
        results[idx] = rec

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        if progress:
            print(
                f"[parallel] running {total} questions with {max_workers} workers",
                flush=True,
            )
        list(pool.map(lambda iq: _run(iq[0], iq[1]), enumerate(questions)))

    # All slots are filled because _ask_one catches exceptions internally.
    return [r for r in results if r is not None]


def _ask_one(pipeline: Pipeline, question: EvalQuestion) -> EvalRecord:
    """Wrap pipeline.ask() so a single failure becomes an error record."""
    try:
        answer = pipeline.ask(question.question)
    except Exception as exc:  # noqa: BLE001 — eval must survive one bad question
        return EvalRecord(
            question_id=question.id,
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="",
            faithfulness_score=0.0,
            error=f"{type(exc).__name__}: {exc}",
        )

    cited: set[str] = set()
    for cs in answer.sentences:
        cited.update(cs.supporting_sentence_ids)

    # Preserve the per-sentence cite breakdown so downstream scorers can
    # attribute citations correctly. Sort cites within each sentence for
    # determinism (so cached judgments stay stable across re-runs).
    per_sentence = tuple(
        (cs.text, tuple(sorted(cs.supporting_sentence_ids)))
        for cs in answer.sentences
    )

    # An empty answer is functionally a refusal regardless of strictness:
    # the system produced nothing the user can act on. The Pipeline's
    # was_refused flag only fires above the faithfulness threshold, which
    # in loose mode is 0 — so we OR in the empty-answer case here.
    refused = answer.was_refused or not answer.sentences

    return EvalRecord(
        question_id=question.id,
        was_refused=refused,
        cited_sentence_ids=frozenset(cited),
        answer_text=answer.text,
        faithfulness_score=answer.faithfulness_score,
        cited_sentences=per_sentence,
    )


# --------------------------------------------------------------------------- #
# ALCE runner — bypasses the shared-corpus model
# --------------------------------------------------------------------------- #


def run_alce_benchmark(
    pipeline: Pipeline,
    benchmark,  # type: ignore[no-untyped-def] — ALCEBench, not declared here to avoid circular import
    pipeline_label: str = "alce-baseline",
    max_questions: int | None = None,
    progress: bool = True,
    delay_between_questions: float = 0.0,
    max_workers: int = 1,
) -> EvalReport:
    """Run an ALCE-style benchmark where each question carries its own passages.

    Bypasses ingestion entirely — the bench provides ``passages_for(qid)`` and
    we synthesize per-question ``Document`` + ``RetrievedChunk`` objects on the
    fly. Reranker (if configured) still ranks the question's passages; the
    generator and verifier are unchanged.
    """
    from verifiable_rag.eval.datasets.alce import _passage_sentence_id, passage_doc_id
    from verifiable_rag.models.chunk import Chunk, RetrievedChunk
    from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
    from verifiable_rag.models.span import Span

    def _build_synthetic(qid: str, passages: list) -> tuple[Document, list[RetrievedChunk]]:
        doc_id = passage_doc_id(qid)
        char_offset = 0
        sections: list[Section] = []
        retrieved: list[RetrievedChunk] = []
        full_text_parts: list[str] = []
        for i, p in enumerate(passages):
            text = (p.get("text") or "").strip()
            if not text:
                continue
            start = char_offset
            end = start + len(text)
            span = Span(doc_id=doc_id, char_start=start, char_end=end)
            sentence_id = _passage_sentence_id(qid, i)
            sentence = Sentence(id=sentence_id, text=text, span=span)
            paragraph = Paragraph(
                id=f"{doc_id}::para{i}", sentences=[sentence], span=span,
            )
            section = Section(
                id=f"{doc_id}::sec{i}",
                title=p.get("title"),
                paragraphs=[paragraph],
                span=span,
            )
            sections.append(section)
            full_text_parts.append(text)
            chunk = Chunk(
                chunk_id=f"{doc_id}::chunk{i}",
                text=text,
                doc_id=doc_id,
                sentence_ids=(sentence_id,),
                span=span,
                metadata={
                    "passage_index": i,
                    "passage_id": str(p.get("id", "")),
                    "passage_title": p.get("title"),
                },
            )
            # Use ALCE's pre-computed score where present; fall back to a
            # descending series so first-position passages are preferred.
            score = float(p.get("score") if p.get("score") is not None else 1.0 - i * 0.001)
            retrieved.append(
                RetrievedChunk(chunk=chunk, score=score, retrieval_method="alce_provided")
            )
            # +2 gap between passages keeps each sentence's span distinct.
            char_offset = end + 2

        document = Document(
            doc_id=doc_id,
            source_path=Path(f"alce/{qid}"),  # synthetic — not a real file
            sections=sections,
            full_text="\n\n".join(full_text_parts),
            metadata={"alce_qid": qid},
            parser_name="alce_synthetic",
        )
        return document, retrieved

    def _ask_one_alce(q: EvalQuestion) -> EvalRecord:
        """Run the full ALCE per-question pipeline; catch exceptions as errors."""
        passages = benchmark.passages_for(q.id)
        document, retrieved = _build_synthetic(q.id, passages)
        documents = {document.doc_id: document}
        try:
            if pipeline.reranker is not None:
                reranked = pipeline.reranker.rerank(
                    q.question, retrieved, top_k=pipeline.top_k_rerank
                )
            else:
                reranked = retrieved[: pipeline.top_k_rerank]

            cited_sentences = pipeline.generator.generate(q.question, reranked, documents)

            verification_results: list = []
            if pipeline.verifier is not None:
                verification_results = pipeline.verifier.verify(cited_sentences, documents)

            answer = pipeline._build_answer(  # noqa: SLF001 — internal but stable
                q.question, cited_sentences, verification_results, reranked
            )

            cited: set[str] = set()
            for cs in answer.sentences:
                cited.update(cs.supporting_sentence_ids)
            per_sentence = tuple(
                (cs.text, tuple(sorted(cs.supporting_sentence_ids)))
                for cs in answer.sentences
            )
            refused = answer.was_refused or not answer.sentences

            return EvalRecord(
                question_id=q.id,
                was_refused=refused,
                cited_sentence_ids=frozenset(cited),
                answer_text=answer.text,
                faithfulness_score=answer.faithfulness_score,
                cited_sentences=per_sentence,
            )
        except Exception as exc:  # noqa: BLE001
            return EvalRecord(
                question_id=q.id,
                was_refused=False,
                cited_sentence_ids=frozenset(),
                answer_text="",
                faithfulness_score=0.0,
                error=f"{type(exc).__name__}: {exc}",
            )

    questions = list(benchmark.questions())
    if max_questions is not None:
        questions = questions[:max_questions]

    records: list[EvalRecord] = [None] * len(questions)  # type: ignore[list-item]
    total = len(questions)
    print_lock = threading.Lock()
    counter = {"done": 0}

    if max_workers > 1 and total > 1:
        if progress:
            print(f"[alce-parallel] {total} questions with {max_workers} workers", flush=True)

        def _run(idx: int, q: EvalQuestion) -> None:
            rec = _ask_one_alce(q)
            with print_lock:
                counter["done"] += 1
                if progress:
                    err = f" ERROR: {rec.error}" if rec.error else ""
                    print(f"[alce-ask {counter['done']}/{total}] {q.id}{err}", flush=True)
            records[idx] = rec

        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            list(pool.map(lambda iq: _run(iq[0], iq[1]), enumerate(questions)))
    else:
        for i, q in enumerate(questions, start=1):
            if progress:
                print(f"[alce-ask {i}/{total}] {q.id}: {q.question[:80]}", flush=True)
            records[i - 1] = _ask_one_alce(q)
            if delay_between_questions and i < total:
                time.sleep(delay_between_questions)

    records = [r for r in records if r is not None]  # type: ignore[assignment]

    gold_by_id = {
        q.id: (q.gold_sentence_ids, q.should_refuse) for q in questions
    }
    report = EvalReport(
        benchmark_name=benchmark.name,
        pipeline_label=pipeline_label,
        records=records,
        discarded_question_ids=[],
        parsers_by_question_id={q.id: ["alce_synthetic"] for q in questions},
    )
    report.metrics = score_records(records, gold_by_id)
    return report
