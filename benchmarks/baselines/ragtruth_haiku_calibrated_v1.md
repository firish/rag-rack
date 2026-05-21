# RAGTruth calibrated baseline — Haiku

- **verifiers:** Haiku
- **n_train (intersection):** 300
- **n_test (intersection):** 600
- **frozen threshold (from train):** 0.0500
- **train F1 at threshold (in-sample on train):** 0.7333

## Test set metrics — calibrated

Threshold frozen from train; metrics below are on the held-out test split.

| metric | value |
|---|---|
| auroc (threshold-free) | 0.7282 |
| auprc (threshold-free) | 0.4936 |
| **calibrated F1** | **0.1382** |
| calibrated precision | 0.4146 |
| calibrated recall | 0.0829 |
| in-sample best F1 (diagnostic only) | 0.6598 |
| in-sample best threshold (diagnostic) | 0.8500 |

## Per task (test-side, calibrated)

| task | n | auroc | calibrated F1 | precision | recall |
|---|---|---|---|---|---|
| Data2txt | 200 | 0.7665 | 0.1268 | 0.8182 | 0.0687 |
| QA | 200 | 0.6990 | 0.0645 | 0.2000 | 0.0385 |
| Summary | 200 | 0.7558 | 0.1918 | 0.2800 | 0.1458 |

## Per model (test-side, calibrated)

| model | n | auroc | calibrated F1 |
|---|---|---|---|
| gpt-3.5-turbo-0613 | 87 | 0.7533 | 0.0000 |
| gpt-4-0613 | 111 | 0.7096 | 0.4000 |
| llama-2-13b-chat | 96 | 0.5125 | 0.2069 |
| llama-2-70b-chat | 81 | 0.7140 | 0.0571 |
| llama-2-7b-chat | 135 | 0.5991 | 0.1918 |
| mistral-7B-instruct | 90 | 0.7513 | 0.0000 |
