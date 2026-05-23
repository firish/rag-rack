# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose | gen=constrained`
- **Run at:** 2026-05-20 23:47:17
- **Questions:** 29

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.672 |
| `citation_recall` | 0.484 |
| `citation_f1` | 0.466 |
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
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 1 | 3 | 0.24 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✗ | ✗ | 2 | 4 | 14 | 0.72 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.68 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 2 | 3 | 9 | 0.92 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.26 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 3 | 3 | 12 | 0.87 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 2 | 2 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.63 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 2 | 3 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 4 | 13 | 6 | 0.96 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 3 | 1 | 0.89 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 4 | 3 | 0.98 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 14 | 5 | 0.99 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✗ | ✗ | 0 | 8 | 2 | 0.99 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 3 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 1 | 2 | 0.70 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 2 | 2 | 4 | 0.85 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.30 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 2 | 2 | 4 | 0.99 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 3 | 3 | 0.42 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 0 | 3 | 1 | 0.95 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> **ciproflaxin**
> A. lwoffii evolved resistance to ciprofloxacin in laboratory experiments, as demonstrated by the fact that clinical resistance was seen only for ciprofloxacin. [6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383]
> In the one instance where A. lwoffii evolved resistance, to ciprofloxacin, drug target mutations were also observed. [6795e9ad5fae6fe1-b687cf6e::s370]
> A. lwoffii seemed to be capable of evolving drug-resistance mutations to ciprofloxacin but not meropenem. [6795e9ad5fae6fe1-b687cf6e::s267]

Cited: 6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s370, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
> **2.7 fold**
> Furthermore, total contacts made to GIs showed that whereas the active OR gene significantly increased its contacts to GIs by 2.7-fold, both inactive OR genes and other GIs significantly decreased their GI contacts. [a8d467f77e70f70d-553b632a::s175]

Cited: a8d467f77e70f70d-553b632a::s175

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> **61% of gene loci**
> The majority of gene disruption phenotypes (61% of total gene phenotypes) were detected by 4 cell divisions. [aca6b37101ab6098-3101659e::s135]

Cited: aca6b37101ab6098-3101659e::s135

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> **12,300**
> Our method detected 4,850 SWO-specific ILs, 12,309 mandarin-specific ILs, and 4,900 pummelo-specific ILs in them. [c322ce6575cc1c3a-d56b589a::s181]

Cited: c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> **80%**
> H3.3 K36R mutants complete development and eclose at a frequency of ~80%, which is nearly identical to that of H3.3 Ctrl animals. [116c0e949dd415fc-61f4295b::s281]

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
> **10%**
> The acute heat stress assay was performed with animals exposed to 35°C for 6 hours, and survival was assessed after 14 hours of recovery at 20°C. [1c5f1e074ba072b8-31d0ed90::s437, 1c5f1e074ba072b8-31d0ed90::s438]
> Only 10% of adr mutant animals die after the same 35°C stress, which includes adr-1(-), adr-2(-), and adr-1(-);adr-2(-) animals. [1c5f1e074ba072b8-31d0ed90::s79, 1c5f1e074ba072b8-31d0ed90::s80]

Cited: 1c5f1e074ba072b8-31d0ed90::s437, 1c5f1e074ba072b8-31d0ed90::s438, 1c5f1e074ba072b8-31d0ed90::s79, 1c5f1e074ba072b8-31d0ed90::s80

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> **Asn326**
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6, attaching to Asn326. [d79480166f4ab0e3-4297b383::s79]

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> **evening**
> The overall number of TILs was highly dependent on the time of day of tumor harvest, with total leukocyte numbers peaking in the evening (ZT13). [40349a281d8b56ff-7979b34d::s110]
> We confirmed these data by immunofluorescence staining of tumor sections, showing higher T cell numbers in the evening (ZT13) compared with the morning (ZT1). [40349a281d8b56ff-7979b34d::s112]
> Leukocyte trafficking to the tumor was strongly time-of-day dependent, with more cells reaching the tumor in the evening, in line with the infiltration block data. [40349a281d8b56ff-7979b34d::s132]

Cited: 40349a281d8b56ff-7979b34d::s110, 40349a281d8b56ff-7979b34d::s112, 40349a281d8b56ff-7979b34d::s132

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> **cell–matrix interactions**
> Myotendinous junction myonuclei exhibited enrichment in genes associated with cell-matrix interactions (COL22A1, ADGBR4), whereas NMJ myonuclei showed enrichment in genes linked to synaptic transmission responses (PHLDB2, CHRNE). [f7c3d31ee5706405-5f6af1d3::s122]

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> **5.3%**
> Results showed that the percentage of AR-negative patients was significantly lower in MBC than in FBC samples (5.3% vs. 17.4% in MBC and FBC samples, respectively) [476ba9a9e8ea9c14-b5e5878b::s495, 476ba9a9e8ea9c14-b5e5878b::s496, 476ba9a9e8ea9c14-b5e5878b::s497]

Cited: 476ba9a9e8ea9c14-b5e5878b::s495, 476ba9a9e8ea9c14-b5e5878b::s496, 476ba9a9e8ea9c14-b5e5878b::s497

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> **Saponaria vaccaria**
> β-Amyrin synthases (BASs) of various plant origins (Artemisia annua, Arabidopsis thaliana, Glycyrrhiza glabra and Saponaria vaccaria) were integrated into JWY601 to quantify the production of β-amyrin from squalene by gas chromatography-mass spectrometry (GC-MS). [e35c8530af941f04-9a7975aa::s99]
> Among these candidates, the BAS homologue from S. vaccaria (SvBAS) yielded the highest titre of β-amyrin, the production of which was further confirmed by efficient consumption of squalene compared to the parent strain. [e35c8530af941f04-9a7975aa::s100]

Cited: e35c8530af941f04-9a7975aa::s100, e35c8530af941f04-9a7975aa::s99

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> **5x**
> From P6 to P15, TC synapse density increases 5-fold in wild-type mice. [c0b69d2af9f2e018-845b5d60::s271]

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> **100**
> Cells with the synthetic IL-2 circuit autonomously identified the target tumor (CD19 + /right) and locally expanded by a factor of ~100 within this tumor. [34f4e70030aa5d35-a24b74ef::s130]

Cited: 34f4e70030aa5d35-a24b74ef::s130

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
> **aa 31-40**
> The N-terminus of COSA-1 mediates the interaction with MSH-5 and ZHP-3. [4c0f27bd833d0295-e8c8a393::s612, 4c0f27bd833d0295-e8c8a393::s613]
> COSA-1 has a long N-terminus containing an intrinsically disordered region (IDR) spanning residue 1–50. [4c0f27bd833d0295-e8c8a393::s625, 4c0f27bd833d0295-e8c8a393::s626, 4c0f27bd833d0295-e8c8a393::s627, 4c0f27bd833d0295-e8c8a393::s628]
> Truncated COSA-1 1–10, COSA-1 1–20, and COSA-1 1–30 could interact with MSH-5 and ZHP-3, while COSA-1 1-40 showed dramatically decreased interactions with these two proteins. [4c0f27bd833d0295-e8c8a393::s638, 4c0f27bd833d0295-e8c8a393::s639, 4c0f27bd833d0295-e8c8a393::s640, 4c0f27bd833d0295-e8c8a393::s641]
> The N-terminal 53 amino acids of COSA-1 play a vital role in the interactions with MSH-5 and ZHP-3. [4c0f27bd833d0295-e8c8a393::s645, 4c0f27bd833d0295-e8c8a393::s646, 4c0f27bd833d0295-e8c8a393::s647]

Cited: 4c0f27bd833d0295-e8c8a393::s612, 4c0f27bd833d0295-e8c8a393::s613, 4c0f27bd833d0295-e8c8a393::s625, 4c0f27bd833d0295-e8c8a393::s626, 4c0f27bd833d0295-e8c8a393::s627, 4c0f27bd833d0295-e8c8a393::s628, 4c0f27bd833d0295-e8c8a393::s638, 4c0f27bd833d0295-e8c8a393::s639, 4c0f27bd833d0295-e8c8a393::s640, 4c0f27bd833d0295-e8c8a393::s641, 4c0f27bd833d0295-e8c8a393::s645, 4c0f27bd833d0295-e8c8a393::s646, 4c0f27bd833d0295-e8c8a393::s647

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> **Depletion of photosynthetic machinery**
> MTF1 is the chloroplast's MTF and is required for translation of nearly all chloroplast-encoded proteins, and its mutant shows a severe photosynthetic phenotype. [9afb8ab3b1d5ff95-b03dfb72::s237]
> Loss of MTF1 expression resulted in the depletion of the entire photosynthetic apparatus and most of the chloroplast-expressed proteins. [9afb8ab3b1d5ff95-b03dfb72::s238]
> Disruption of the poorly characterized genes PMR1 and MTF1 led to the depletion of the entire photosynthetic apparatus. [9afb8ab3b1d5ff95-b03dfb72::s180]

Cited: 9afb8ab3b1d5ff95-b03dfb72::s180, 9afb8ab3b1d5ff95-b03dfb72::s237, 9afb8ab3b1d5ff95-b03dfb72::s238

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
> **Yes**
> A striking difference between PBS- and verteporfin-treated wounds was the emergence of regenerated HF in the latter within 30 days; control wounds formed bare areas. [7dead537a45e92bd-e35471f4::s253]
> By POD 30, verteporfin-treated wounds regrew levels of HF and glands comparable with those in unwounded skin and had less-dense, more randomly oriented ECM fibers. [7dead537a45e92bd-e35471f4::s89]
> Blocking mechanotransduction (verteporfin, YAP inhibitor) prevents conversion and yields regeneration, defined by the restoration of dermal appendages (hair follicles). [7dead537a45e92bd-e35471f4::s72, 7dead537a45e92bd-e35471f4::s73]

Cited: 7dead537a45e92bd-e35471f4::s253, 7dead537a45e92bd-e35471f4::s72, 7dead537a45e92bd-e35471f4::s73, 7dead537a45e92bd-e35471f4::s89

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> **Yes**
> Metabolic glycan labeling can reduce the membrane mobility of DCs, which activates DCs and improves the antigen presentation and subsequent T cell priming property of DCs. [6f59dd139145c891-36c60054::s16, 6f59dd139145c891-36c60054::s17, 6f59dd139145c891-36c60054::s18]
> Metabolic glycan labeling itself can enhance the antitumor efficacy of DC vaccines. [6f59dd139145c891-36c60054::s19, 6f59dd139145c891-36c60054::s20]
> The metabolic glycan labeling process itself is able to reduce the mobility of proteins on DC membrane and upregulate the activation markers of DCs, leading to the improved ability of DCs to process and present peptide and protein antigens and subsequently prime antigen-specific CD8+ T cells. [6f59dd139145c891-36c60054::s108, 6f59dd139145c891-36c60054::s109, 6f59dd139145c891-36c60054::s110, 6f59dd139145c891-36c60054::s111, 6f59dd139145c891-36c60054::s112]
> By simply adding azido-sugars to the culture medium of DCs during the expansion of antigen-presenting DCs, the CTL response and antitumor efficacy of DC vaccines are significantly improved. [6f59dd139145c891-36c60054::s114, 6f59dd139145c891-36c60054::s115, 6f59dd139145c891-36c60054::s116, 6f59dd139145c891-36c60054::s117]

Cited: 6f59dd139145c891-36c60054::s108, 6f59dd139145c891-36c60054::s109, 6f59dd139145c891-36c60054::s110, 6f59dd139145c891-36c60054::s111, 6f59dd139145c891-36c60054::s112, 6f59dd139145c891-36c60054::s114, 6f59dd139145c891-36c60054::s115, 6f59dd139145c891-36c60054::s116, 6f59dd139145c891-36c60054::s117, 6f59dd139145c891-36c60054::s16, 6f59dd139145c891-36c60054::s17, 6f59dd139145c891-36c60054::s18, 6f59dd139145c891-36c60054::s19, 6f59dd139145c891-36c60054::s20

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> **coding strand**
> In all 17 CRISPRi screens, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands. [b0c70be4f4a933d3-7fb87fac::s328]

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
> **Insufficient information to answer**
> The sources discuss the binding properties of TDRD1's Tudor domains to methylated arginine peptides from other proteins (MILI, MIWI, MVH), but do not describe any dimethylarginine modifications on TDRD1 itself. [aa268cf616154b07-7384f4cb::s1160, aa268cf616154b07-7384f4cb::s1161, aa268cf616154b07-7384f4cb::s1162, aa268cf616154b07-7384f4cb::s1163]
> The study focuses on TDRD1's recognition of symmetrical dimethylarginine (sDMA) modifications on other piRNA pathway proteins, not on modifications of TDRD1 itself. [aa268cf616154b07-7384f4cb::s312, aa268cf616154b07-7384f4cb::s313, aa268cf616154b07-7384f4cb::s328, aa268cf616154b07-7384f4cb::s329]

Cited: aa268cf616154b07-7384f4cb::s1160, aa268cf616154b07-7384f4cb::s1161, aa268cf616154b07-7384f4cb::s1162, aa268cf616154b07-7384f4cb::s1163, aa268cf616154b07-7384f4cb::s312, aa268cf616154b07-7384f4cb::s313, aa268cf616154b07-7384f4cb::s328, aa268cf616154b07-7384f4cb::s329

### `d2860d38-dfb9-4b80-905f-812c32573915`
> **S. epidermis**
> Engineered S. epidermidis strains stimulate T cells specific for non-native epitopes under physiologic conditions of colonization. [8e4b7872a7579d54-cb6467cd::s93]
> OT-I- or OT-II-expressing S. epidermidis could prime OVA-specific CD8+ or CD4+ T cells, respectively, without any barrier breach or skin inflammation. [8e4b7872a7579d54-cb6467cd::s92]
> The engineered strains of S. epidermidis could stimulate antigen-specific T cells in vitro and in vivo. [8e4b7872a7579d54-cb6467cd::s89]

Cited: 8e4b7872a7579d54-cb6467cd::s89, 8e4b7872a7579d54-cb6467cd::s92, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> **Enlarged granular cells**
> The α PrePro and Ost1ssα Pro sequences resulted in enlarged granular cells, expanded ER membranes, and relocalization of HsMOR-GFP to puncta. [33d9e243f2ee99de-02bbb79f::s173]

Cited: 33d9e243f2ee99de-02bbb79f::s173

### `5a2128ad-3127-4595-b810-db128d1a2335`
> **TM3**
> The homology models were weak in the extracellular TM2-TM3 loop region and did not predict partial unwinding of TM3 at the extracellular end, an unusual feature of Hc ChRs. [f2e1fb5c9886efad-202dbbbb::s114]
> In contrast, models were particularly good for helices TM1, TM6, and TM7. [f2e1fb5c9886efad-202dbbbb::s113]

Cited: f2e1fb5c9886efad-202dbbbb::s113, f2e1fb5c9886efad-202dbbbb::s114

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> **gp02**
> Whereas regulation of the three host genes all involved sequestration of the target ribosome-binding site, regulation of gp02 occurs in the coding sequence, indicating that target regulation might be accompanied by ribonuclease recruitment. [d1ef96583ec64586-195f7c93::s219]

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> **1300 anstrom^2**
> Formation of the DarR dimer by interaction of the two monomers results in the burial of ~1300 Å 2 of surface from solvent. [405dcaff86bce126-c6c89512::s68]

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
> **increases**
> To assess the role of ECL3 in A3AR, we engineered chimeric receptors by grafting ECL3 from A3AR onto the backbones of other adenosine receptors. [23f9c4bad2271b89-675be55a::s146]
> The three ECL3-chimeric receptors gained the ability to bind CF101 and CF102 with increased efficacy or potency. [23f9c4bad2271b89-675be55a::s148]

Cited: 23f9c4bad2271b89-675be55a::s146, 23f9c4bad2271b89-675be55a::s148

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> **Yes**
> Having demonstrated robust tagmentation over large ranges of cDNA, Tn5 and reaction volumes, we realized an opportunity to exclude several time-consuming and expensive experimental steps, including excessive cDNA preamplification, concentration measurements, bioanalyzer QC traces and cDNA amount normalization. [70758b216a7dc837-240c67f2::s36]
> Instead, cDNA products after preamplification at fewer cycles could directly be tagmented without the abovementioned steps - this strategy we termed Smart-seq3xpress. [70758b216a7dc837-240c67f2::s37]
> To explore this potential, we first generated libraries with low-volume RT (300 nL lysis volume) from HEK293FT cells and using a range of PCR preamplification cycles (10 to 20), that strikingly, revealed very similar gene detection without any need for additional enzymatic reaction clean-ups. [70758b216a7dc837-240c67f2::s38]

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s38

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> **Yes**
> We performed a base-editing screen against all canonical splice donor or acceptor sites present in CD33 to identify single base edits that reduced or eliminated CD33 expression in HSPCs. [6acd5496cc0d3cfd-49391314::s129]
> Multiple sgRNAs were enriched in the CD33 low population, with strong enrichment for sgRNAs targeting splice donor sites of exons 1 and 2. [6acd5496cc0d3cfd-49391314::s131]
> We performed another systematic mutagenesis screen of CD33 splice sites, as was done with ABE8e, but with evoFERNY protein instead. [6acd5496cc0d3cfd-49391314::s249]

Cited: 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s131, 6acd5496cc0d3cfd-49391314::s249
