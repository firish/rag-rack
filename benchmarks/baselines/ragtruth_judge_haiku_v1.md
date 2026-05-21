# RAGTruth baseline — llm-judge::claude-haiku-4-5-20251001

- **scorer:** llm-judge::claude-haiku-4-5-20251001
- **split:** test
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 600 (of 600; 0 errors)
- **base rate (hallucinated):** 0.342
- **wall time:** 901.2s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.7282 |
| auprc | 0.4936 |
| f1_best | 0.6598 |
| precision_best | 0.5079 |
| recall_best | 0.9415 |
| threshold_best | 0.8500 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 200 | 0.655 | 0.7665 | 0.8714 |
| QA | 200 | 0.130 | 0.6990 | 0.3421 |
| Summary | 200 | 0.240 | 0.7558 | 0.5935 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 87 | 0.138 | 0.7533 | 0.5000 |
| gpt-4-0613 | 111 | 0.108 | 0.7096 | 0.4118 |
| llama-2-13b-chat | 96 | 0.375 | 0.5125 | 0.5854 |
| llama-2-70b-chat | 81 | 0.407 | 0.7140 | 0.7033 |
| llama-2-7b-chat | 135 | 0.444 | 0.5991 | 0.6667 |
| mistral-7B-instruct | 90 | 0.578 | 0.7513 | 0.8333 |
