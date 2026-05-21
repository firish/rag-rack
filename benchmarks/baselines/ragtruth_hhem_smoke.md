# RAGTruth baseline — hhem-2.1-open

- **scorer:** hhem-2.1-open
- **split:** test
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 20 (of 20; 0 errors)
- **base rate (hallucinated):** 0.250
- **wall time:** 192.1s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.6800 |
| auprc | 0.3925 |
| f1_best | 0.6154 |
| precision_best | 0.5000 |
| recall_best | 0.8000 |
| threshold_best | 0.2107 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Summary | 20 | 0.250 | 0.6800 | 0.6154 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 4 | 0.000 | nan | nan |
| gpt-4-0613 | 4 | 0.000 | nan | nan |
| llama-2-13b-chat | 3 | 1.000 | nan | nan |
| llama-2-70b-chat | 3 | 0.333 | 0.0000 | 0.5000 |
| llama-2-7b-chat | 3 | 0.000 | nan | nan |
| mistral-7B-instruct | 3 | 0.333 | 0.5000 | 0.6667 |
