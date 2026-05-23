# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose | gen=constrained`
- **Run at:** 2026-05-21 23:52:30
- **Questions:** 29
- **Errors:** 19

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.700 |
| `citation_recall` | 0.338 |
| `citation_f1` | 0.363 |
| `coverage` | 0.800 |
| `localization_accuracy` | 0.100 |
| `abstention_precision` | 1.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 1.000 |
| `mc_correct` | 10.000 |
| `mc_wrong` | 0.000 |
| `mc_unanswered` | 0.000 |
| `mc_accuracy_over_answered` | 1.000 |
| `mc_accuracy_over_all` | 1.000 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 0 | 0 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA4siun4BR6GTmxRtNu"} |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA5uHSzB5VfYKVS352N"} |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 0 | 0 | 5 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA6uuBZwiA6X9QW4Uik"} |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 1 | 3 | 0.24 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA8hFyathHVMLFQybcu"} |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✗ | ✗ | 0 | 0 | 14 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA9nJs4j1oJ6n2fEayK"} |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAAmhBJihSsiiQSXckb"} |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 0 | 0 | 9 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHABnMtemmYZBfc5xXaq"} |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.28 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 0 | 0 | 12 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHADjDw2Ugf5gyjtytrg"} |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 2 | 2 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAFcjK7MGGhvyxEZB2c"} |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAGktjJsBZ1faTjyizf"} |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 2 | 3 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 0 | 0 | 6 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAKpQ9qN4nWpzjBZYY5"} |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHALvxZztTeNw8cs1UBB"} |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHANEH9Un16GZc9huUwM"} |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 0 | 5 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAPTG2Q5mR7WW94JSKX"} |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHARRXQKSoiQXK6U1cLR"} |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 3 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHATJ3kXggPgNHAv1ef7"} |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAUL73ybgf2QnntwWbi"} |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.30 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAXVTx9RL7ktjjPuJWP"} |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAYjmxHjYz1vYWtggXC"} |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 3 | 1 | 0.95 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA4siun4BR6GTmxRtNu"}

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA5uHSzB5VfYKVS352N"}

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA6uuBZwiA6X9QW4Uik"}

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> **12,300**
> Our method detected 4,850 SWO-specific ILs, 12,309 mandarin-specific ILs, and 4,900 pummelo-specific ILs in them. [c322ce6575cc1c3a-d56b589a::s181]

Cited: c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA8hFyathHVMLFQybcu"}

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHA9nJs4j1oJ6n2fEayK"}

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAAmhBJihSsiiQSXckb"}

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHABnMtemmYZBfc5xXaq"}

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> **cell–matrix interactions**
> Myotendinous junction myonuclei exhibited enrichment in genes associated with cell-matrix interactions (COL22A1, ADGBR4), whereas NMJ myonuclei showed enrichment in genes linked to synaptic transmission responses (PHLDB2, CHRNE). [f7c3d31ee5706405-5f6af1d3::s122]

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHADjDw2Ugf5gyjtytrg"}

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> **Saponaria vaccaria**
> β-Amyrin synthases (BASs) of various plant origins (Artemisia annua, Arabidopsis thaliana, Glycyrrhiza glabra and Saponaria vaccaria) were integrated into JWY601 to quantify the production of β-amyrin from squalene by gas chromatography-mass spectrometry (GC-MS). [e35c8530af941f04-9a7975aa::s99]
> Among these candidates, the BAS homologue from S. vaccaria (SvBAS) yielded the highest titre of β-amyrin, the production of which was further confirmed by efficient consumption of squalene compared to the parent strain. [e35c8530af941f04-9a7975aa::s100]

Cited: e35c8530af941f04-9a7975aa::s100, e35c8530af941f04-9a7975aa::s99

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAFcjK7MGGhvyxEZB2c"}

### `dd29920d-cb70-440f-961c-3e1103776c4f`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAGktjJsBZ1faTjyizf"}

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> **7.7x**
> In six MMR-proficient cell types, including induced pluripotent stem cells (iPSCs) and primary T cells, these PE4 (PE2+MLH1dn) and PE5 (PE3+MLH1dn) systems enhanced editing efficiency over PE2 and PE3 by an average of 7.7-fold and 2.0-fold, respectively, and increased edit/indel ratios (outcome purity) by 3.4fold. [fa808d37a77e6019-79d6e54c::s96]

Cited: fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> **residues 344–360**
> A domain in Apollo (amino acids 344-360) promotes Apollo's interaction with DNA-PK and is required for Apollo function at telomeres. [cea2facf97f5150c-660a07bf::s61]
> A version of Apollo with a deletion of amino acids 344-360 (Apollo/Delta1 PK), removing the residues most similar to those of the Artemis DNA-PK interaction motif, had a reduced interaction with DNA-PKcs in 293T cells. [cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s407]

Cited: cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s407, cea2facf97f5150c-660a07bf::s61

### `487539f9-2f17-4009-aa4a-c41322445f11`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAKpQ9qN4nWpzjBZYY5"}

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHALvxZztTeNw8cs1UBB"}

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHANEH9Un16GZc9huUwM"}

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAPTG2Q5mR7WW94JSKX"}

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> **coding strand**
> In all 17 CRISPRi screens, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands. [b0c70be4f4a933d3-7fb87fac::s328]

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHARRXQKSoiQXK6U1cLR"}

### `d2860d38-dfb9-4b80-905f-812c32573915`
> **S. epidermis**
> Engineered S. epidermidis strains stimulate T cells specific for non-native epitopes under physiologic conditions of colonization. [8e4b7872a7579d54-cb6467cd::s93]
> The engineered strains of S. epidermidis could stimulate antigen-specific T cells in vitro and prime T cells in vivo. [8e4b7872a7579d54-cb6467cd::s89]
> OT-I- or OT-II-expressing S. epidermidis could prime OVA-specific CD8+ or CD4+ T cells, respectively, without any barrier breach or skin inflammation. [8e4b7872a7579d54-cb6467cd::s92]

Cited: 8e4b7872a7579d54-cb6467cd::s89, 8e4b7872a7579d54-cb6467cd::s92, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHATJ3kXggPgNHAv1ef7"}

### `5a2128ad-3127-4595-b810-db128d1a2335`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAUL73ybgf2QnntwWbi"}

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> **gp02**
> Whereas regulation of the three host genes all involved sequestration of the target ribosome-binding site, regulation of gp02 occurs in the coding sequence, indicating that target regulation might be accompanied by ribonuclease recruitment. [d1ef96583ec64586-195f7c93::s219]

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> **1300 anstrom^2**
> Formation of the DarR dimer by interaction of the two monomers results in the burial of ~1300 Å 2 of surface from solvent. [405dcaff86bce126-c6c89512::s68]

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAXVTx9RL7ktjjPuJWP"}

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
**Error:** InternalServerError: litellm.InternalServerError: AnthropicError - {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHAYjmxHjYz1vYWtggXC"}

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> **Yes**
> We performed a base-editing screen against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs. [6acd5496cc0d3cfd-49391314::s129]
> Multiple sgRNAs were enriched in the CD33 low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2. [6acd5496cc0d3cfd-49391314::s131]
> We performed another systematic mutagenesis screen of CD33 splice sites, as was done with ABE8e, but with evoFERNY protein instead. [6acd5496cc0d3cfd-49391314::s249]

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131, 6acd5496cc0d3cfd-49391314::s249
