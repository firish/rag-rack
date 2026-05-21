# RAGTruth baseline — llm-judge::claude-sonnet-4-6

- **scorer:** llm-judge::claude-sonnet-4-6
- **split:** test
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 300 (of 300; 0 errors)
- **base rate (hallucinated):** 0.340
- **wall time:** 634.7s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.8456 |
| auprc | 0.6325 |
| f1_best | 0.7072 |
| precision_best | 0.5776 |
| recall_best | 0.9118 |
| threshold_best | 0.9000 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 100 | 0.670 | 0.8523 | 0.9028 |
| QA | 100 | 0.140 | 0.8443 | 0.5000 |
| Summary | 100 | 0.210 | 0.8484 | 0.6538 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 36 | 0.111 | 0.9688 | 0.8000 |
| gpt-4-0613 | 45 | 0.089 | 0.8476 | 0.5000 |
| llama-2-13b-chat | 60 | 0.367 | 0.7721 | 0.6531 |
| llama-2-70b-chat | 45 | 0.356 | 0.7500 | 0.6829 |
| llama-2-7b-chat | 63 | 0.429 | 0.7989 | 0.7333 |
| mistral-7B-instruct | 51 | 0.569 | 0.8542 | 0.8889 |
