# RAGTruth baseline — hhem-2.1-open (modal-T4)

- **scorer:** hhem-2.1-open (modal-T4)
- **split:** train
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 1500 (of 1500; 0 errors)
- **base rate (hallucinated):** 0.461
- **wall time:** 1391.0s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.7949 |
| auprc | 0.7418 |
| f1_best | 0.7359 |
| precision_best | 0.6339 |
| recall_best | 0.8770 |
| threshold_best | 0.5669 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 500 | 0.724 | 0.5940 | 0.8399 |
| QA | 500 | 0.322 | 0.8404 | 0.6667 |
| Summary | 500 | 0.336 | 0.7549 | 0.6115 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 217 | 0.175 | 0.7048 | 0.4746 |
| gpt-4-0613 | 252 | 0.143 | 0.7822 | 0.4565 |
| llama-2-13b-chat | 253 | 0.573 | 0.7055 | 0.7580 |
| llama-2-70b-chat | 248 | 0.480 | 0.8769 | 0.8340 |
| llama-2-7b-chat | 266 | 0.639 | 0.7039 | 0.8021 |
| mistral-7B-instruct | 264 | 0.693 | 0.8616 | 0.8763 |
