#!/usr/bin/env bash
# Print a comparison table across baseline runs.
# Usage: ./scripts/compare_baselines.sh [run1.md run2.md ...]
# Defaults to comparing v3 (locked) against the v6 sweep outputs.

cd "$(dirname "$0")/.."

if [ "$#" -eq 0 ]; then
    set -- \
        benchmarks/baselines/v3_phase2_baseline.md \
        benchmarks/baselines/v6_prompt_no_verifier.md \
        benchmarks/baselines/v6_prompt_hhem_010.md \
        benchmarks/baselines/v6_prompt_hhem_015.md \
        benchmarks/baselines/v6_prompt_hhem_020.md \
        benchmarks/baselines/v6_prompt_hhem_030.md
fi

METRICS="citation_precision citation_recall citation_f1 coverage localization_accuracy abstention_precision abstention_recall abstention_f1"

# Header
printf "%-25s" "metric"
for f in "$@"; do
    if [ -e "$f" ]; then
        # Short name = filename without prefix/suffix
        name=$(basename "$f" .md | sed 's/^v[0-9]*_phase[0-9]*_//;s/^v[0-9]*_//')
        printf " | %-22s" "$name"
    else
        printf " | %-22s" "$(basename "$f" .md) (missing)"
    fi
done
printf "\n"

# Underline
printf "%-25s" "-------------------------"
for f in "$@"; do
    printf " | %-22s" "----------------------"
done
printf "\n"

# Rows
for metric in $METRICS; do
    printf "%-25s" "$metric"
    for f in "$@"; do
        if [ -e "$f" ]; then
            val=$(grep -E "\`$metric\` \|" "$f" | head -1 | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')
            printf " | %-22s" "${val:-—}"
        else
            printf " | %-22s" "—"
        fi
    done
    printf "\n"
done

# Errors row (special)
printf "%-25s" "errors"
for f in "$@"; do
    if [ -e "$f" ]; then
        err=$(grep -E "^\*\*Errors:\*\*" "$f" | head -1 | awk '{print $3}')
        printf " | %-22s" "${err:-0}"
    else
        printf " | %-22s" "—"
    fi
done
printf "\n"
