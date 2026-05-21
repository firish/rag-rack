# RAGTruth baseline — minicheck-flan-t5-large (modal-T4)

- **scorer:** minicheck-flan-t5-large (modal-T4)
- **split:** train
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 1500 (of 1500; 0 errors)
- **base rate (hallucinated):** 0.461
- **wall time:** 3957.8s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.8187 |
| auprc | 0.7926 |
| f1_best | 0.7329 |
| precision_best | 0.6651 |
| recall_best | 0.8162 |
| threshold_best | 0.8889 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 500 | 0.724 | 0.7426 | 0.8487 |
| QA | 500 | 0.322 | 0.8145 | 0.6707 |
| Summary | 500 | 0.336 | 0.7561 | 0.6137 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 217 | 0.175 | 0.6575 | 0.3716 |
| gpt-4-0613 | 252 | 0.143 | 0.7290 | 0.4242 |
| llama-2-13b-chat | 253 | 0.573 | 0.8141 | 0.7986 |
| llama-2-70b-chat | 248 | 0.480 | 0.9126 | 0.8504 |
| llama-2-7b-chat | 266 | 0.639 | 0.7514 | 0.8040 |
| mistral-7B-instruct | 264 | 0.693 | 0.8602 | 0.8564 |
