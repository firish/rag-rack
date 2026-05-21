# RAGTruth baseline — llm-judge::claude-haiku-4-5-20251001

- **scorer:** llm-judge::claude-haiku-4-5-20251001
- **split:** train
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 300 (of 300; 0 errors)
- **base rate (hallucinated):** 0.450
- **wall time:** 397.3s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.7293 |
| auprc | 0.6036 |
| f1_best | 0.7333 |
| precision_best | 0.6205 |
| recall_best | 0.8963 |
| threshold_best | 0.9500 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 100 | 0.700 | 0.7136 | 0.8707 |
| QA | 100 | 0.310 | 0.6620 | 0.5625 |
| Summary | 100 | 0.340 | 0.7611 | 0.6897 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 44 | 0.159 | 0.5521 | 0.3125 |
| gpt-4-0613 | 56 | 0.161 | 0.6998 | 0.4000 |
| llama-2-13b-chat | 55 | 0.582 | 0.6515 | 0.7848 |
| llama-2-70b-chat | 51 | 0.490 | 0.7815 | 0.8136 |
| llama-2-7b-chat | 42 | 0.619 | 0.6442 | 0.8136 |
| mistral-7B-instruct | 52 | 0.692 | 0.7049 | 0.8462 |
