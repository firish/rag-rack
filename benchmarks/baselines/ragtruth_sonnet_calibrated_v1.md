# RAGTruth calibrated baseline — Sonnet

- **verifiers:** Sonnet
- **n_train (intersection):** 300
- **n_test (intersection):** 300
- **frozen threshold (from train):** 0.1500
- **train F1 at threshold (in-sample on train):** 0.7461

## Test set metrics — calibrated

Threshold frozen from train; metrics below are on the held-out test split.

| metric | value |
|---|---|
| auroc (threshold-free) | 0.8456 |
| auprc (threshold-free) | 0.6325 |
| **calibrated F1** | **0.7072** |
| calibrated precision | 0.5776 |
| calibrated recall | 0.9118 |
| in-sample best F1 (diagnostic only) | 0.7072 |
| in-sample best threshold (diagnostic) | 0.9000 |

## Per task (test-side, calibrated)

| task | n | auroc | calibrated F1 | precision | recall |
|---|---|---|---|---|---|
| Data2txt | 100 | 0.8523 | 0.8955 | 0.8955 | 0.8955 |
| QA | 100 | 0.8443 | 0.4407 | 0.2889 | 0.9286 |
| Summary | 100 | 0.8484 | 0.5714 | 0.4082 | 0.9524 |

## Per model (test-side, calibrated)

| model | n | auroc | calibrated F1 |
|---|---|---|---|
| gpt-3.5-turbo-0613 | 36 | 0.9688 | 0.7500 |
| gpt-4-0613 | 45 | 0.8476 | 0.4000 |
| llama-2-13b-chat | 60 | 0.7721 | 0.5882 |
| llama-2-70b-chat | 45 | 0.7500 | 0.6829 |
| llama-2-7b-chat | 63 | 0.7989 | 0.7123 |
| mistral-7B-instruct | 51 | 0.8542 | 0.8889 |
