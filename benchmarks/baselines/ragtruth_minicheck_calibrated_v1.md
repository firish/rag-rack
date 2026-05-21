# RAGTruth calibrated baseline — MiniCheck

- **verifiers:** MiniCheck
- **n_train (intersection):** 1500
- **n_test (intersection):** 2700
- **frozen threshold (from train):** 0.1111
- **train F1 at threshold (in-sample on train):** 0.7329

## Test set metrics — calibrated

Threshold frozen from train; metrics below are on the held-out test split.

| metric | value |
|---|---|
| auroc (threshold-free) | 0.8355 |
| auprc (threshold-free) | 0.7107 |
| **calibrated F1** | **0.6963** |
| calibrated precision | 0.5915 |
| calibrated recall | 0.8462 |
| in-sample best F1 (diagnostic only) | 0.7001 |
| in-sample best threshold (diagnostic) | 0.9147 |

## Per task (test-side, calibrated)

| task | n | auroc | calibrated F1 | precision | recall |
|---|---|---|---|---|---|
| Data2txt | 900 | 0.7023 | 0.7900 | 0.6628 | 0.9775 |
| QA | 900 | 0.8386 | 0.5241 | 0.3943 | 0.7812 |
| Summary | 900 | 0.7770 | 0.5602 | 0.6011 | 0.5245 |

## Per model (test-side, calibrated)

| model | n | auroc | calibrated F1 |
|---|---|---|---|
| gpt-3.5-turbo-0613 | 450 | 0.8036 | 0.3744 |
| gpt-4-0613 | 450 | 0.7970 | 0.3474 |
| llama-2-13b-chat | 450 | 0.8881 | 0.7880 |
| llama-2-70b-chat | 450 | 0.8366 | 0.7237 |
| llama-2-7b-chat | 450 | 0.7858 | 0.7390 |
| mistral-7B-instruct | 450 | 0.8466 | 0.8247 |
