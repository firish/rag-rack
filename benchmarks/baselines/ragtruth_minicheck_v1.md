# RAGTruth baseline — minicheck-flan-t5-large (modal-T4)

- **scorer:** minicheck-flan-t5-large (modal-T4)
- **split:** test
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 2700 (of 2700; 0 errors)
- **base rate (hallucinated):** 0.349
- **wall time:** 6140.9s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.8355 |
| auprc | 0.7107 |
| f1_best | 0.7001 |
| precision_best | 0.6182 |
| recall_best | 0.8070 |
| threshold_best | 0.9147 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 900 | 0.643 | 0.7023 | 0.7972 |
| QA | 900 | 0.178 | 0.8386 | 0.5542 |
| Summary | 900 | 0.227 | 0.7770 | 0.5632 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 450 | 0.102 | 0.8036 | 0.3883 |
| gpt-4-0613 | 450 | 0.093 | 0.7970 | 0.3616 |
| llama-2-13b-chat | 450 | 0.460 | 0.8881 | 0.8290 |
| llama-2-70b-chat | 450 | 0.380 | 0.8366 | 0.7366 |
| llama-2-7b-chat | 450 | 0.502 | 0.7858 | 0.7442 |
| mistral-7B-instruct | 450 | 0.558 | 0.8466 | 0.8280 |
