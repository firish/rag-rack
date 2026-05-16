# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose`
- **Run at:** 2026-05-16 03:18:17
- **Questions:** 9
- **Errors:** 1

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.875 |
| `citation_recall` | 0.428 |
| `citation_f1` | 0.337 |
| `coverage` | 0.500 |
| `localization_accuracy` | 0.250 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |
| `mc_correct` | 1.000 |
| `mc_wrong` | 1.000 |
| `mc_unanswered` | 6.000 |
| `mc_accuracy_over_answered` | 0.500 |
| `mc_accuracy_over_all` | 0.125 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✓ | ✗ | 0 | 0 | 1 | 0.12 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 1 | 1 | 5 | 0.38 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✓ | ✗ | 0 | 0 | 3 | 0.12 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✓ | ✗ | 0 | 0 | 14 | 0.79 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.49 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 2 | 2 | 9 | 0.95 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 0 | 0 | 12 | 0.00 ⚠️ RateLimitError: litellm.RateLimitError: AnthropicException - {"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your organization's rate limit of 50,000 input tokens per minute (org: ac37d026-8a94-437f-87a7-e20cfa6cefa5, model: claude-haiku-4-5-20251001). For details, refer to: https://docs.claude.com/en/api/rate-limits. You can see the response headers for current usage. Please reduce the prompt length or the maximum tokens requested, or try again later. You may also contact sales at https://claude.com/contact-sales to discuss your options for a rate limit increase."},"request_id":"req_011Cb65QGSoG8amLeK1MRLH3"} |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> Based on the provided sources, Acinetobacter lwoffii has been evolved in the lab to be resistant to ciprofloxacin. The sources indicate that "A. lwoffii seemed to be capable of evolving drug-resistance mutations to ciprofloxacin but not meropenem." Additionally, "clinical resistance was seen only for ciprofloxacin" in A. lwoffii.

Cited: 6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
_Refused._

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions.

Cited: aca6b37101ab6098-3101659e::s135

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
> Based on the experiments with B16-F10 melanoma cells expressing ovalbumin in mice, the number of tumor-infiltrating leukocytes is highest in the evening. "The overall number of TILs was highly dependent on the time of day of tumor harvest, with total leukocyte numbers peaking in the evening (ZT13)." This finding was confirmed by immunofluorescence staining: "higher T cell numbers in the evening (ZT13) compared with the morning (ZT1)"

Cited: 40349a281d8b56ff-7979b34d::s110, 40349a281d8b56ff-7979b34d::s112

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
**Error:** RateLimitError: litellm.RateLimitError: AnthropicException - {"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your organization's rate limit of 50,000 input tokens per minute (org: ac37d026-8a94-437f-87a7-e20cfa6cefa5, model: claude-haiku-4-5-20251001). For details, refer to: https://docs.claude.com/en/api/rate-limits. You can see the response headers for current usage. Please reduce the prompt length or the maximum tokens requested, or try again later. You may also contact sales at https://claude.com/contact-sales to discuss your options for a rate limit increase."},"request_id":"req_011Cb65QGSoG8amLeK1MRLH3"}
