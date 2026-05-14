#!/usr/bin/env bash
# v6 sweep — new prompt + HHEM threshold sweep
# Runs 5 evals sequentially:
#   1. baseline-new-prompt: no verifier (isolates the prompt-tuning effect)
#   2-5. HHEM verifier at thresholds 0.10, 0.15, 0.20, 0.30 (with new prompt)
#
# Each clears the LanceDB cache before running so chunks don't duplicate.
# Output: benchmarks/baselines/v6_*.md plus a combined log at /tmp/v6_sweep.log

set -u  # don't fail on errors — we want all 5 runs even if one breaks

cd "$(dirname "$0")/.."
set -a
source .env
set +a
source .venv/bin/activate

LOG=/tmp/v6_sweep.log
echo "=== v6 sweep started $(date) ===" | tee "$LOG"

run_eval () {
    local out_name="$1"
    local extra_flags="$2"
    echo
    echo "=== $(date) | $out_name ===" | tee -a "$LOG"
    rm -rf .verifiable_rag_cache/indexes/eval_lance
    python -m verifiable_rag.eval \
        --benchmark harry_potter_micro \
        --model "gemini/gemma-4-31b-it" \
        --delay 4.0 \
        --min-tokens 100 \
        --top-k-retrieve 80 \
        --top-k-rerank 8 \
        --out "benchmarks/baselines/${out_name}.md" \
        ${extra_flags} 2>&1 | tee -a "$LOG"
    echo "--- $out_name done at $(date) ---" | tee -a "$LOG"
}

# 1. New-prompt baseline (no verifier) — measures prompt-tuning effect alone
run_eval "v6_prompt_no_verifier" ""

# 2-5. Sweep HHEM threshold with new prompt
run_eval "v6_prompt_hhem_010" "--verifier hhem --strictness balanced --verifier-threshold 0.10"
run_eval "v6_prompt_hhem_015" "--verifier hhem --strictness balanced --verifier-threshold 0.15"
run_eval "v6_prompt_hhem_020" "--verifier hhem --strictness balanced --verifier-threshold 0.20"
run_eval "v6_prompt_hhem_030" "--verifier hhem --strictness balanced --verifier-threshold 0.30"

echo
echo "=== v6 sweep COMPLETE at $(date) ===" | tee -a "$LOG"
ls -la benchmarks/baselines/v6_*.md 2>&1 | tee -a "$LOG"
