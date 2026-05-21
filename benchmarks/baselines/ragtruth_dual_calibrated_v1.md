# RAGTruth calibrated baseline — HHEM + MiniCheck

- **verifiers:** HHEM, MiniCheck
- **aggregation:** min
- **n_train (intersection):** 1500
- **n_test (intersection):** 2700
- **frozen threshold (from train):** 0.0562
- **train F1 at threshold (in-sample on train):** 0.7437

## Test set metrics — calibrated

Threshold frozen from train; metrics below are on the held-out test split.

| metric | value |
|---|---|
| auroc (threshold-free) | 0.8435 |
| auprc (threshold-free) | 0.7290 |
| **calibrated F1** | **0.7065** |
| calibrated precision | 0.6389 |
| calibrated recall | 0.7900 |
| in-sample best F1 (diagnostic only) | 0.7095 |
| in-sample best threshold (diagnostic) | 0.9409 |

## Per task (test-side, calibrated)

| task | n | auroc | calibrated F1 | precision | recall |
|---|---|---|---|---|---|
| Data2txt | 900 | 0.6858 | 0.7839 | 0.6708 | 0.9430 |
| QA | 900 | 0.8655 | 0.5833 | 0.5000 | 0.7000 |
| Summary | 900 | 0.7923 | 0.5241 | 0.6797 | 0.4265 |

## Per model (test-side, calibrated)

| model | n | auroc | calibrated F1 |
|---|---|---|---|
| gpt-3.5-turbo-0613 | 450 | 0.8051 | 0.3716 |
| gpt-4-0613 | 450 | 0.8113 | 0.3684 |
| llama-2-13b-chat | 450 | 0.8940 | 0.8141 |
| llama-2-70b-chat | 450 | 0.8444 | 0.7268 |
| llama-2-7b-chat | 450 | 0.7983 | 0.7527 |
| mistral-7B-instruct | 450 | 0.8607 | 0.8134 |
