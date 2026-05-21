# RAGTruth baseline — llm-judge::claude-sonnet-4-6

- **scorer:** llm-judge::claude-sonnet-4-6
- **split:** train
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 300 (of 300; 0 errors)
- **base rate (hallucinated):** 0.450
- **wall time:** 1120.8s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.8268 |
| auprc | 0.7405 |
| f1_best | 0.7461 |
| precision_best | 0.6467 |
| recall_best | 0.8815 |
| threshold_best | 0.8500 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 100 | 0.700 | 0.8198 | 0.8904 |
| QA | 100 | 0.310 | 0.8050 | 0.6769 |
| Summary | 100 | 0.340 | 0.8137 | 0.7073 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 44 | 0.159 | 0.7394 | 0.4545 |
| gpt-4-0613 | 56 | 0.161 | 0.7352 | 0.4000 |
| llama-2-13b-chat | 55 | 0.582 | 0.7527 | 0.8000 |
| llama-2-70b-chat | 51 | 0.490 | 0.8208 | 0.8000 |
| llama-2-7b-chat | 42 | 0.619 | 0.6827 | 0.8000 |
| mistral-7B-instruct | 52 | 0.692 | 0.8967 | 0.8824 |
