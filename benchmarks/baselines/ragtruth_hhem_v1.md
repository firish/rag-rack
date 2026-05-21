# RAGTruth baseline — hhem-2.1-open (modal-T4)

- **scorer:** hhem-2.1-open (modal-T4)
- **split:** test
- **aggregation:** min
- **task filter:** all
- **model filter:** all
- **examples scored:** 2700 (of 2700; 0 errors)
- **base rate (hallucinated):** 0.349
- **wall time:** 2545.8s

## Aggregate metrics

| metric | value |
|---|---|
| auroc | 0.8132 |
| auprc | 0.6801 |
| f1_best | 0.6759 |
| precision_best | 0.5831 |
| recall_best | 0.8038 |
| threshold_best | 0.7666 |

## Per task

| task | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| Data2txt | 900 | 0.643 | 0.5659 | 0.7858 |
| QA | 900 | 0.178 | 0.8742 | 0.6541 |
| Summary | 900 | 0.227 | 0.7594 | 0.5044 |

## Per model

| model | n | base_rate | auroc | f1_best |
|---|---|---|---|---|
| gpt-3.5-turbo-0613 | 450 | 0.102 | 0.8252 | 0.4247 |
| gpt-4-0613 | 450 | 0.093 | 0.8420 | 0.4737 |
| llama-2-13b-chat | 450 | 0.460 | 0.8152 | 0.7468 |
| llama-2-70b-chat | 450 | 0.380 | 0.8060 | 0.7039 |
| llama-2-7b-chat | 450 | 0.502 | 0.7656 | 0.7308 |
| mistral-7B-instruct | 450 | 0.558 | 0.8627 | 0.8187 |
