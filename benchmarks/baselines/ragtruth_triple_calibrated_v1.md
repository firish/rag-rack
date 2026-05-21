# RAGTruth calibrated baseline — HHEM + MiniCheck + Sonnet

- **verifiers:** HHEM, MiniCheck, Sonnet
- **aggregation:** min
- **n_train (intersection):** 300
- **n_test (intersection):** 300
- **frozen threshold (from train):** 0.0500
- **train F1 at threshold (in-sample on train):** 0.7682

## Test set metrics — calibrated

Threshold frozen from train; metrics below are on the held-out test split.

| metric | value |
|---|---|
| auroc (threshold-free) | 0.8610 |
| auprc (threshold-free) | 0.6667 |
| **calibrated F1** | **0.7342** |
| calibrated precision | 0.6444 |
| calibrated recall | 0.8529 |
| in-sample best F1 (diagnostic only) | 0.7436 |
| in-sample best threshold (diagnostic) | 0.9521 |

## Per task (test-side, calibrated)

| task | n | auroc | calibrated F1 | precision | recall |
|---|---|---|---|---|---|
| Data2txt | 100 | 0.7246 | 0.8312 | 0.7356 | 0.9552 |
| QA | 100 | 0.8301 | 0.4186 | 0.3103 | 0.6429 |
| Summary | 100 | 0.8813 | 0.7000 | 0.7368 | 0.6667 |

## Per model (test-side, calibrated)

| model | n | auroc | calibrated F1 |
|---|---|---|---|
| gpt-3.5-turbo-0613 | 36 | 0.8555 | 0.4615 |
| gpt-4-0613 | 45 | 0.8963 | 0.3750 |
| llama-2-13b-chat | 60 | 0.9031 | 0.8163 |
| llama-2-70b-chat | 45 | 0.8459 | 0.7179 |
| llama-2-7b-chat | 63 | 0.7922 | 0.7619 |
| mistral-7B-instruct | 51 | 0.8605 | 0.8070 |
