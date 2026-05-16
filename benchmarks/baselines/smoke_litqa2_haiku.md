# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | bge-small | hybrid(BM25+lance) | min_tokens=100 | bge-rerank-v2-m3 | retrieve=80/rerank=8 | no-verifier | loose`
- **Run at:** 2026-05-15 23:20:33
- **Questions:** 9

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.889 |
| `citation_recall` | 0.399 |
| `citation_f1` | 0.325 |
| `coverage` | 0.556 |
| `localization_accuracy` | 0.222 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |
| `mc_correct` | 2.000 |
| `mc_wrong` | 0.000 |
| `mc_unanswered` | 7.000 |
| `mc_accuracy_over_answered` | 1.000 |
| `mc_accuracy_over_all` | 0.222 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✓ | ✗ | 0 | 0 | 1 | 0.32 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 2 | 2 | 5 | 0.40 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✓ | ✗ | 0 | 0 | 3 | 0.33 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.70 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✓ | ✗ | 0 | 0 | 14 | 0.75 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.55 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 1 | 1 | 9 | 0.90 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.70 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> Based on the provided sources, Acinetobacter lwoffii evolved resistance in the lab to **ciprofloxacin only**. Specifically, "for A. lwoffii, clinical resistance was seen only for ciprofloxacin." Additionally, "the mutant evolution experiments clearly show that A. lwoffii has a reduced capacity to evolve resistance to antibiotics compared to A. baumannii, where it only evolved resistance to ciprofloxacin."

Cited: 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
_Refused._

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions. However, the question asks specifically about "Cas9-disrupted loci in human neural stem cells" without specifying whether this refers to genes, enhancers, or both. If the question intends to ask about all disrupted loci collectively, the sources do not provide a single combined fraction. The sources separately report that 61% of gene disruption phenotypes were detected by 4 cell divisions, while 30% of enhancer disruption phenotypes were detected at this early time point.

Cited: aca6b37101ab6098-3101659e::s135, aca6b37101ab6098-3101659e::s136

### `27234279-f50c-4cfc-86e2-af68364a8f94`
_Refused._

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> H3.3 K36R mutants complete development and eclose at a frequency of ~80%.

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
_Refused._

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6, attaching to Asn326.

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> The number of tumor-infiltrating leukocytes is highest in the evening. Specifically, total leukocyte numbers peak at zeitgeber time 13 (ZT13), which corresponds to the evening time point.

Cited: 40349a281d8b56ff-7979b34d::s110

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> Based on the single-nuclei RNA sequencing data, myotendinous junction myonuclei are enriched for genes involved in cell-matrix interactions.

Cited: f7c3d31ee5706405-5f6af1d3::s122
