#!/usr/bin/env bash
# Runs the full LitQA2 pipeline overnight/AFK:
#   Stage 1: reindex with alignment (rapidfuzz over parsed sentences)
#   Stage 2: LitQA2 eval on 192-paper subset, lock as v7 baseline
#   Stage 3: write a "DONE" marker so the monitor knows we finished
#
# Designed to run unattended via:
#     nohup bash scripts/run_litqa2_pipeline.sh > /tmp/litqa2_pipeline.log 2>&1 &

set -u  # don't bail on errors — we want the eval to run even if alignment hits issues
cd "$(dirname "$0")/.."
set -a
source .env
set +a
source .venv/bin/activate

LOG=/tmp/litqa2_pipeline.log
DONE_MARKER=/tmp/litqa2_pipeline.done

echo "=== START $(date) ===" | tee -a "$LOG"

# Stage 1 — reindex with key-passage → sentence_id alignment
echo "" | tee -a "$LOG"
echo "=== Stage 1: reindex with alignment $(date) ===" | tee -a "$LOG"
python scripts/litqa2_pdfs.py reindex 2>&1 | tail -25 | tee -a "$LOG"
echo "Stage 1 done $(date)" | tee -a "$LOG"

# Stage 2 — LitQA2 eval (clear lance index for clean run)
echo "" | tee -a "$LOG"
echo "=== Stage 2: LitQA2 eval $(date) ===" | tee -a "$LOG"
rm -rf .verifiable_rag_cache/indexes/eval_lance
python -m verifiable_rag.eval \
    --benchmark litqa2 \
    --model "gemini/gemma-4-31b-it" \
    --delay 4.0 \
    --min-tokens 100 \
    --top-k-retrieve 80 \
    --top-k-rerank 8 \
    --out benchmarks/baselines/v7_litqa2_baseline.md 2>&1 | tail -30 | tee -a "$LOG"
echo "Stage 2 done $(date)" | tee -a "$LOG"

# Stage 3 — drop a marker so the watcher knows everything finished
echo "$(date)" > "$DONE_MARKER"
echo "" | tee -a "$LOG"
echo "=== ALL DONE $(date) ===" | tee -a "$LOG"
ls -la benchmarks/baselines/v7_litqa2_baseline.md 2>&1 | tee -a "$LOG"
