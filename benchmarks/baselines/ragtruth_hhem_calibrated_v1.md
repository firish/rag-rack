# RAGTruth calibrated baseline — HHEM

- **verifiers:** HHEM
- **n_train (intersection):** 1500
- **n_test (intersection):** 2700
- **frozen threshold (from train):** 0.4331
- **train F1 at threshold (in-sample on train):** 0.7359

## Test set metrics — calibrated

Threshold frozen from train; metrics below are on the held-out test split.

| metric | value |
|---|---|
| auroc (threshold-free) | 0.8132 |
| auprc (threshold-free) | 0.6801 |
| **calibrated F1** | **0.6632** |
| calibrated precision | 0.5302 |
| calibrated recall | 0.8855 |
| in-sample best F1 (diagnostic only) | 0.6759 |
| in-sample best threshold (diagnostic) | 0.7666 |

## Per task (test-side, calibrated)

| task | n | auroc | calibrated F1 | precision | recall |
|---|---|---|---|---|---|
| Data2txt | 900 | 0.5659 | 0.7762 | 0.6467 | 0.9706 |
| QA | 900 | 0.8742 | 0.5257 | 0.3781 | 0.8625 |
| Summary | 900 | 0.7594 | 0.4954 | 0.3959 | 0.6618 |

## Per model (test-side, calibrated)

| model | n | auroc | calibrated F1 |
|---|---|---|---|
| gpt-3.5-turbo-0613 | 450 | 0.8252 | 0.3684 |
| gpt-4-0613 | 450 | 0.8420 | 0.3379 |
| llama-2-13b-chat | 450 | 0.8152 | 0.6964 |
| llama-2-70b-chat | 450 | 0.8060 | 0.6916 |
| llama-2-7b-chat | 450 | 0.7656 | 0.7171 |
| mistral-7B-instruct | 450 | 0.8627 | 0.8106 |
