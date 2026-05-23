# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose | gen=safe`
- **Run at:** 2026-05-22 17:41:00
- **Questions:** 29

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.652 |
| `citation_recall` | 0.496 |
| `citation_f1` | 0.475 |
| `coverage` | 0.793 |
| `localization_accuracy` | 0.207 |
| `abstention_precision` | 1.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 1.000 |
| `mc_correct` | 28.000 |
| `mc_wrong` | 0.000 |
| `mc_unanswered` | 1.000 |
| `mc_accuracy_over_answered` | 1.000 |
| `mc_accuracy_over_all` | 0.966 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 1 | 1 | 5 | 0.55 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 2 | 3 | 0.24 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✗ | ✗ | 3 | 3 | 14 | 0.72 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.68 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 3 | 5 | 9 | 0.92 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.26 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 5 | 6 | 12 | 0.87 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 2 | 2 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.63 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 2 | 3 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 4 | 13 | 6 | 0.96 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 3 | 1 | 0.89 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 6 | 3 | 0.98 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 11 | 5 | 0.99 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✗ | ✗ | 0 | 8 | 2 | 0.99 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 2 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 2 | 2 | 0.70 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 2 | 2 | 4 | 0.85 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.30 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 2 | 2 | 4 | 0.99 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 3 | 3 | 0.42 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 5 | 1 | 0.95 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> **ciproflaxin**
> A. lwoffii evolved resistance to ciprofloxacin in laboratory experiments. [6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383]
> A. lwoffii did not evolve resistance to meropenem or gentamicin in the laboratory experiments. [6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s272]
> Clinical resistance in A. lwoffii was seen only for ciprofloxacin among the three antibiotics tested. [6795e9ad5fae6fe1-b687cf6e::s278]

Cited: 6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s272, 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
> **2.7 fold**
> Active olfactory receptor genes increase their contacts with Greek island regions by 2.7-fold in mouse olfactory neurons. [a8d467f77e70f70d-553b632a::s175]

Cited: a8d467f77e70f70d-553b632a::s175

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> **61% of gene loci**
> The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions. [aca6b37101ab6098-3101659e::s135]

Cited: aca6b37101ab6098-3101659e::s135

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> **12,300**
> The method detected 12,309 mandarin-specific insertion loci among the 57 Mandarin accessions surveyed. [c322ce6575cc1c3a-d56b589a::s172, c322ce6575cc1c3a-d56b589a::s181]

Cited: c322ce6575cc1c3a-d56b589a::s172, c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> **80%**
> H3.3 K36R mutants complete development and eclose at a frequency of approximately 80%. [116c0e949dd415fc-61f4295b::s281]

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
> **10%**
> When C. elegans adr mutant animals were exposed to 35°C for 6 hours with survival assessed after 14 hours of recovery at 20°C, only 10% of adr mutant animals died. [1c5f1e074ba072b8-31d0ed90::s78, 1c5f1e074ba072b8-31d0ed90::s79]
> The adr-1(-), adr-2(-), and adr-1(-);adr-2(-) mutant animals were not sensitive to acute heat stress. [1c5f1e074ba072b8-31d0ed90::s80]

Cited: 1c5f1e074ba072b8-31d0ed90::s78, 1c5f1e074ba072b8-31d0ed90::s79, 1c5f1e074ba072b8-31d0ed90::s80

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> **Asn326**
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6, attaching to Asn326. [d79480166f4ab0e3-4297b383::s79]

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> **evening**
> In experiments with B16-F10 melanoma cells expressing ovalbumin injected into mice, the overall number of tumor-infiltrating leukocytes was highly dependent on the time of day of tumor harvest, with total leukocyte numbers peaking in the evening (ZT13). [40349a281d8b56ff-7979b34d::s109, 40349a281d8b56ff-7979b34d::s110]
> Immunofluorescence staining of tumor sections confirmed higher T cell numbers in the evening (ZT13) compared with the morning (ZT1). [40349a281d8b56ff-7979b34d::s112]
> The tumor microenvironment exhibited pro-migratory properties in the evening, demonstrating that leukocyte infiltration into tumors peaks at this time of day. [40349a281d8b56ff-7979b34d::s132, 40349a281d8b56ff-7979b34d::s133]

Cited: 40349a281d8b56ff-7979b34d::s109, 40349a281d8b56ff-7979b34d::s110, 40349a281d8b56ff-7979b34d::s112, 40349a281d8b56ff-7979b34d::s132, 40349a281d8b56ff-7979b34d::s133

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> **cell–matrix interactions**
> Based on single-nuclei RNA sequencing data, myotendinous junction myonuclei are enriched for genes involved in cell-matrix interactions. [f7c3d31ee5706405-5f6af1d3::s122]

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> **5.3%**
> In a retrospective analysis of AR levels evaluated by IHC in a large sample cohort including 113 ER+ MBC and 86 ER+ FBC samples, the percentage of AR-negative patients was significantly lower in MBC than in FBC samples. [476ba9a9e8ea9c14-b5e5878b::s491, 476ba9a9e8ea9c14-b5e5878b::s492, 476ba9a9e8ea9c14-b5e5878b::s493, 476ba9a9e8ea9c14-b5e5878b::s495, 476ba9a9e8ea9c14-b5e5878b::s496]
> Specifically, 5.3% of ER+ MBC patients showed AR-negative status when evaluated by IHC, compared to 17.4% in FBC samples. [476ba9a9e8ea9c14-b5e5878b::s497]

Cited: 476ba9a9e8ea9c14-b5e5878b::s491, 476ba9a9e8ea9c14-b5e5878b::s492, 476ba9a9e8ea9c14-b5e5878b::s493, 476ba9a9e8ea9c14-b5e5878b::s495, 476ba9a9e8ea9c14-b5e5878b::s496, 476ba9a9e8ea9c14-b5e5878b::s497

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> **Saponaria vaccaria**
> Beta-amyrin synthases from Artemisia annua, Arabidopsis thaliana, Glycyrrhiza glabra, and Saponaria vaccaria were integrated into yeast to quantify the production of β-amyrin from squalene. [e35c8530af941f04-9a7975aa::s99]
> Among these candidates, the beta-amyrin synthase from Saponaria vaccaria yielded the highest titre of β-amyrin. [e35c8530af941f04-9a7975aa::s100]

Cited: e35c8530af941f04-9a7975aa::s100, e35c8530af941f04-9a7975aa::s99

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> **5x**
> From P6 to P15, thalamocortical synapse density increases 5-fold in wild-type mice. [c0b69d2af9f2e018-845b5d60::s271]

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> **100**
> T cells with the anti-CD19 synNotch → sIL-2 circuit locally expanded by a factor of approximately 100 within the target tumor in a mouse model. [34f4e70030aa5d35-a24b74ef::s130]

Cited: 34f4e70030aa5d35-a24b74ef::s130

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> **7.7x**
> In six MMR-proficient cell types, including induced pluripotent stem cells (iPSCs) and primary T cells, the PE4 system (PE2+MLH1dn) enhanced editing efficiency over PE2 by an average of 7.7-fold. [fa808d37a77e6019-79d6e54c::s96]

Cited: fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> **residues 344–360**
> A version of Apollo with a deletion of amino acids 344-360 (Apollo/Delta1 PK) was created, removing the DNA-PKcs interacting region. [cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s61]
> This Apollo/Delta1 PK construct, containing residues most similar to those of the Artemis DNA-PK interaction motif, had a reduced interaction with DNA-PKcs in 293T cells. [cea2facf97f5150c-660a07bf::s407]
> A domain in Apollo (amino acids 344-360) promotes Apollo's interaction with DNA-PK and is required for Apollo function at telomeres. [cea2facf97f5150c-660a07bf::s61]

Cited: cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s407, cea2facf97f5150c-660a07bf::s61

### `487539f9-2f17-4009-aa4a-c41322445f11`
> **aa 31-40**
> The N-terminus of COSA-1 mediates the interaction with MSH-5 and ZHP-3. [4c0f27bd833d0295-e8c8a393::s612, 4c0f27bd833d0295-e8c8a393::s613]
> COSA-1 contains an intrinsically disordered region (IDR) spanning residue 1–50. [4c0f27bd833d0295-e8c8a393::s625, 4c0f27bd833d0295-e8c8a393::s626, 4c0f27bd833d0295-e8c8a393::s627, 4c0f27bd833d0295-e8c8a393::s628]
> Truncated COSA-1 1–10, COSA-1 1–20, and COSA-1 1–30 could interact with MSH-5 and ZHP-3, while COSA-1 1-40 showed dramatically decreased interactions with these two proteins. [4c0f27bd833d0295-e8c8a393::s638, 4c0f27bd833d0295-e8c8a393::s639, 4c0f27bd833d0295-e8c8a393::s640, 4c0f27bd833d0295-e8c8a393::s641]
> The N-terminal 53 amino acids of COSA-1 play a vital role in the interactions with MSH-5 and ZHP-3. [4c0f27bd833d0295-e8c8a393::s645, 4c0f27bd833d0295-e8c8a393::s646, 4c0f27bd833d0295-e8c8a393::s647]

Cited: 4c0f27bd833d0295-e8c8a393::s612, 4c0f27bd833d0295-e8c8a393::s613, 4c0f27bd833d0295-e8c8a393::s625, 4c0f27bd833d0295-e8c8a393::s626, 4c0f27bd833d0295-e8c8a393::s627, 4c0f27bd833d0295-e8c8a393::s628, 4c0f27bd833d0295-e8c8a393::s638, 4c0f27bd833d0295-e8c8a393::s639, 4c0f27bd833d0295-e8c8a393::s640, 4c0f27bd833d0295-e8c8a393::s641, 4c0f27bd833d0295-e8c8a393::s645, 4c0f27bd833d0295-e8c8a393::s646, 4c0f27bd833d0295-e8c8a393::s647

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> **Depletion of photosynthetic machinery**
> Disruption of MTF1 expression in Chlamydomonas results in depletion of the entire photosynthetic apparatus. [9afb8ab3b1d5ff95-b03dfb72::s180]
> Loss of MTF1 expression resulted in the depletion of the entire photosynthetic apparatus and most of the chloroplast-expressed proteins. [9afb8ab3b1d5ff95-b03dfb72::s238]
> MTF1 is required for translation of nearly all chloroplast-encoded proteins and its mutant shows a severe photosynthetic phenotype. [9afb8ab3b1d5ff95-b03dfb72::s237]

Cited: 9afb8ab3b1d5ff95-b03dfb72::s180, 9afb8ab3b1d5ff95-b03dfb72::s237, 9afb8ab3b1d5ff95-b03dfb72::s238

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
> **Yes**
> Verteporfin treatment yields wound regeneration in mice, with regenerated hair follicles emerging within 30 days in treated wounds compared to control wounds that formed bare areas. [7dead537a45e92bd-e35471f4::s0, 7dead537a45e92bd-e35471f4::s1, 7dead537a45e92bd-e35471f4::s253]
> By postoperative day 30, verteporfin-treated wounds regrew levels of hair follicles and glands comparable with those in unwounded skin and had less-dense, more randomly oriented extracellular matrix fibers. [7dead537a45e92bd-e35471f4::s89]
> Blocking mechanotransduction with verteporfin, a YAP inhibitor, prevents fibroblast conversion and yields regeneration defined by restoration of dermal appendages including hair follicles. [7dead537a45e92bd-e35471f4::s72, 7dead537a45e92bd-e35471f4::s73]

Cited: 7dead537a45e92bd-e35471f4::s0, 7dead537a45e92bd-e35471f4::s1, 7dead537a45e92bd-e35471f4::s253, 7dead537a45e92bd-e35471f4::s72, 7dead537a45e92bd-e35471f4::s73, 7dead537a45e92bd-e35471f4::s89

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> **Yes**
> Metabolic glycan labeling reduces the membrane mobility of dendritic cells. [6f59dd139145c891-36c60054::s16, 6f59dd139145c891-36c60054::s17]
> This reduction in membrane mobility activates dendritic cells and improves their antigen presentation and T cell priming properties. [6f59dd139145c891-36c60054::s17, 6f59dd139145c891-36c60054::s18]
> Metabolic glycan labeling itself enhances the antitumor efficacy of dendritic cell vaccines. [6f59dd139145c891-36c60054::s19, 6f59dd139145c891-36c60054::s20]
> Dendritic cells treated with azido-sugars exhibit reduced membrane mobility compared to control dendritic cells without treatment. [6f59dd139145c891-36c60054::s748, 6f59dd139145c891-36c60054::s750]
> In vivo, azido-labeled antigen-pulsed dendritic cells result in improved cytotoxic T lymphocyte response and antitumor efficacy compared to unlabeled dendritic cells in both prophylactic and therapeutic settings. [6f59dd139145c891-36c60054::s760, 6f59dd139145c891-36c60054::s761, 6f59dd139145c891-36c60054::s762, 6f59dd139145c891-36c60054::s763]

Cited: 6f59dd139145c891-36c60054::s16, 6f59dd139145c891-36c60054::s17, 6f59dd139145c891-36c60054::s18, 6f59dd139145c891-36c60054::s19, 6f59dd139145c891-36c60054::s20, 6f59dd139145c891-36c60054::s748, 6f59dd139145c891-36c60054::s750, 6f59dd139145c891-36c60054::s760, 6f59dd139145c891-36c60054::s761, 6f59dd139145c891-36c60054::s762, 6f59dd139145c891-36c60054::s763

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> **coding strand**
> In all 17 CRISPRi screens, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands. [b0c70be4f4a933d3-7fb87fac::s328]

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
> **Insufficient information to answer**
> TDRD1 is a multidomain protein with four tandem extended Tudor domains that bind to methylated arginine residues on other proteins in the piRNA pathway. [aa268cf616154b07-7384f4cb::s224, aa268cf616154b07-7384f4cb::s227, aa268cf616154b07-7384f4cb::s25, aa268cf616154b07-7384f4cb::s26]
> The sources describe TDRD1 as a protein that recognizes and binds to symmetrical dimethylarginine (sDMA) modifications on other piRNA pathway proteins like MILI and MIWI, but do not specify whether TDRD1 itself contains dimethylarginine modifications. [aa268cf616154b07-7384f4cb::s1160, aa268cf616154b07-7384f4cb::s1161, aa268cf616154b07-7384f4cb::s1162, aa268cf616154b07-7384f4cb::s1163]

Cited: aa268cf616154b07-7384f4cb::s1160, aa268cf616154b07-7384f4cb::s1161, aa268cf616154b07-7384f4cb::s1162, aa268cf616154b07-7384f4cb::s1163, aa268cf616154b07-7384f4cb::s224, aa268cf616154b07-7384f4cb::s227, aa268cf616154b07-7384f4cb::s25, aa268cf616154b07-7384f4cb::s26

### `d2860d38-dfb9-4b80-905f-812c32573915`
> **S. epidermis**
> Engineered strains of S. epidermidis can stimulate T cells specific for non-native epitopes. [8e4b7872a7579d54-cb6467cd::s93]
> Under physiologic conditions of colonization, engineered S. epidermidis strains express non-native antigens that elicit antigen-specific T cell responses. [8e4b7872a7579d54-cb6467cd::s77, 8e4b7872a7579d54-cb6467cd::s93]

Cited: 8e4b7872a7579d54-cb6467cd::s77, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> **Enlarged granular cells**
> Expression of HsMOR with an N-terminal yeast αPrePro sequence resulted in enlarged granular cells and expanded ER membranes. [33d9e243f2ee99de-02bbb79f::s173]
> Additionally, the αPrePro sequence caused relocalization of HsMOR-GFP to puncta. [33d9e243f2ee99de-02bbb79f::s173]
> These cellular disruptions were associated with yeast-based sequences causing global cellular disruptions, possibly through partial HsMOR-GFP misfolding and premature ER exit. [33d9e243f2ee99de-02bbb79f::s175]

Cited: 33d9e243f2ee99de-02bbb79f::s173, 33d9e243f2ee99de-02bbb79f::s175

### `5a2128ad-3127-4595-b810-db128d1a2335`
> **TM3**
> ColabFold homology models were particularly good for helices TM1, TM6, and TM7. [f2e1fb5c9886efad-202dbbbb::s113]
> However, the homology models were weak in the extracellular TM2-TM3 loop region and did not predict partial unwinding of TM3 at the extracellular end. [f2e1fb5c9886efad-202dbbbb::s114]

Cited: f2e1fb5c9886efad-202dbbbb::s113, f2e1fb5c9886efad-202dbbbb::s114

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> **gp02**
> Regulation of gp02 occurs in the coding sequence, whereas regulation of the three host genes (rpoS, cyaA, and petA) all involved sequestration of the target ribosome-binding site. [d1ef96583ec64586-195f7c93::s219]

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> **1300 anstrom^2**
> Formation of the DarR dimer by interaction of the two monomers results in the burial of approximately 1300 Ångströms squared of surface from solvent. [405dcaff86bce126-c6c89512::s68]

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
> **increases**
> When ECL3 from A3AR was grafted onto the backbones of other adenosine receptors, the resulting chimeric receptors gained the ability to bind CF101 with increased efficacy. [23f9c4bad2271b89-675be55a::s146, 23f9c4bad2271b89-675be55a::s148]

Cited: 23f9c4bad2271b89-675be55a::s146, 23f9c4bad2271b89-675be55a::s148

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> **Yes**
> Researchers demonstrated that cDNA products after preamplification could directly be tagmented without cleaning and quantifying steps, a strategy termed Smart-seq3xpress. [70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37]
> The researchers excluded time-consuming and expensive experimental steps including concentration measurements, bioanalyzer QC traces, and cDNA amount normalization. [70758b216a7dc837-240c67f2::s36]
> Libraries generated with low-volume RT from HEK293FT cells using a range of PCR preamplification cycles revealed very similar gene detection without any need for additional enzymatic reaction clean-ups. [70758b216a7dc837-240c67f2::s38]

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s38

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> **Yes**
> A base-editing screen was performed against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs. [6acd5496cc0d3cfd-49391314::s129]
> Multiple sgRNAs were enriched in the CD33 low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2. [6acd5496cc0d3cfd-49391314::s131]
> A second base-editing screen of CD33 splice sites was performed using evoFERNY protein, which identified the exon 1 donor splice site as the top hit and also identified the exon donor 2 site and splice acceptors in exons 3 and 4. [6acd5496cc0d3cfd-49391314::s249, 6acd5496cc0d3cfd-49391314::s250, 6acd5496cc0d3cfd-49391314::s251]

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131, 6acd5496cc0d3cfd-49391314::s249, 6acd5496cc0d3cfd-49391314::s250, 6acd5496cc0d3cfd-49391314::s251
