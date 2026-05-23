# Eval Report: litqa2

- **Pipeline:** `anthropic/claude-haiku-4-5 | cohere-embed-v3 | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=10 | no-verifier | loose | gen=prompted`
- **Run at:** 2026-05-20 23:40:19
- **Questions:** 29

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.828 |
| `citation_recall` | 0.475 |
| `citation_f1` | 0.466 |
| `coverage` | 0.759 |
| `localization_accuracy` | 0.241 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |
| `mc_correct` | 26.000 |
| `mc_wrong` | 0.000 |
| `mc_unanswered` | 3.000 |
| `mc_accuracy_over_answered` | 1.000 |
| `mc_accuracy_over_all` | 0.897 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `e3b5a4af-41d9-48db-becf-29a08d0ad28e` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `76184ccf-4bf0-469e-a442-11d04b4ff8b0` | ✗ | ✗ | 1 | 1 | 1 | 0.12 |
| `39129e1c-096f-4414-bf4f-37fadbbe364c` | ✗ | ✗ | 2 | 2 | 5 | 0.55 |
| `27234279-f50c-4cfc-86e2-af68364a8f94` | ✗ | ✗ | 1 | 1 | 3 | 0.24 |
| `517e7cf8-c5d2-4391-9e2a-235b79d93050` | ✗ | ✗ | 1 | 1 | 1 | 0.81 |
| `cb710074-73a8-4407-b0c7-7dc868f1bc76` | ✓ | ✗ | 0 | 0 | 14 | 0.72 |
| `5c4c602c-9624-4eae-ac44-efe4c0dd10e6` | ✗ | ✗ | 1 | 1 | 1 | 0.68 |
| `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369` | ✗ | ✗ | 2 | 2 | 9 | 0.92 |
| `e6b0f9e5-e976-47dc-b839-0b2fca967e9e` | ✗ | ✗ | 1 | 1 | 12 | 0.26 |
| `247eeb85-a552-4b87-b83e-327538fcb8a9` | ✗ | ✗ | 2 | 2 | 12 | 0.87 |
| `a214f5f8-0de8-43cf-82e0-7930003e4a0c` | ✗ | ✗ | 1 | 1 | 7 | 0.35 |
| `a43e5166-d0e8-48f8-a113-648acac7ed59` | ✗ | ✗ | 1 | 1 | 1 | 0.63 |
| `dd29920d-cb70-440f-961c-3e1103776c4f` | ✗ | ✗ | 1 | 1 | 1 | 0.97 |
| `7d805bb8-4c7c-431f-b068-acf5e5459985` | ✗ | ✗ | 0 | 1 | 1 | 1.00 |
| `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd` | ✗ | ✗ | 1 | 2 | 6 | 0.80 |
| `487539f9-2f17-4009-aa4a-c41322445f11` | ✗ | ✗ | 0 | 0 | 6 | 0.96 |
| `5049c648-b1bb-4624-8824-9d93dfb04e51` | ✗ | ✗ | 1 | 1 | 1 | 0.89 |
| `a18883e9-218a-4719-8d2c-cf94d740de1a` | ✗ | ✗ | 0 | 2 | 3 | 0.98 |
| `d7833c0f-2a16-40d2-b6a0-6764aa3003a6` | ✗ | ✗ | 0 | 0 | 5 | 0.99 |
| `1ccdc348-50e1-4941-9151-5e50411a2b41` | ✗ | ✗ | 1 | 1 | 1 | 1.00 |
| `1e5f5199-84f4-4133-ab87-2372fa6ca722` | ✓ | ✗ | 0 | 0 | 2 | 0.99 |
| `d2860d38-dfb9-4b80-905f-812c32573915` | ✗ | ✗ | 1 | 2 | 1 | 0.75 |
| `77a41274-cd9c-48bc-a347-e0746907840d` | ✗ | ✗ | 1 | 1 | 2 | 0.70 |
| `5a2128ad-3127-4595-b810-db128d1a2335` | ✗ | ✗ | 2 | 2 | 4 | 0.85 |
| `d65103ae-c881-4116-a0a7-1b233eb6275a` | ✗ | ✗ | 1 | 1 | 5 | 0.30 |
| `ab5eb050-d134-4445-9307-6faa08be7474` | ✗ | ✗ | 1 | 1 | 7 | 0.15 |
| `82de3e92-abe2-46ac-ad17-23417b9c4da7` | ✗ | ✗ | 1 | 1 | 4 | 0.99 |
| `7cf0fcde-fea8-420c-8531-2f2fe9e38980` | ✗ | ✗ | 2 | 3 | 3 | 0.42 |
| `da5b2a8f-ba08-4692-851f-2e0bf142a02f` | ✗ | ✗ | 1 | 3 | 1 | 0.95 |

## Per-question answers

### `e3b5a4af-41d9-48db-becf-29a08d0ad28e`
> Based on the provided sources, the best answer is: **ciprofloxacin**

Acinetobacter lwoffii evolved resistance in the laboratory to ciprofloxacin. [6795e9ad5fae6fe1-b687cf6e::s267]
> The organism was capable of evolving drug-resistance mutations to ciprofloxacin but not meropenem. [6795e9ad5fae6fe1-b687cf6e::s383]
> Additionally, clinical resistance was seen only for ciprofloxacin when A. lwoffii was tested. [6795e9ad5fae6fe1-b687cf6e::s278]
> In contrast, A. lwoffii did not evolve resistance to meropenem or gentamicin under the experimental conditions tested. [6795e9ad5fae6fe1-b687cf6e::s267]

Cited: 6795e9ad5fae6fe1-b687cf6e::s267, 6795e9ad5fae6fe1-b687cf6e::s278, 6795e9ad5fae6fe1-b687cf6e::s383

### `76184ccf-4bf0-469e-a442-11d04b4ff8b0`
> Active olfactory receptor genes increase their contacts with Greek island regions by **2.7 fold** in mouse olfactory neurons. [a8d467f77e70f70d-553b632a::s175]

Cited: a8d467f77e70f70d-553b632a::s175

### `39129e1c-096f-4414-bf4f-37fadbbe364c`
> The best answer is **61% of gene loci**.

Among Cas9-disrupted loci in human neural stem cells, 61% of gene disruption phenotypes were apparent after 4 cell divisions. [aca6b37101ab6098-3101659e::s135]
> In contrast, only 30% of conserved-region (enhancer) disruption phenotypes were detected at this early time point. [aca6b37101ab6098-3101659e::s136]

Cited: aca6b37101ab6098-3101659e::s135, aca6b37101ab6098-3101659e::s136

### `27234279-f50c-4cfc-86e2-af68364a8f94`
> The mandarin (Citrus reticulata) genome contains approximately 12,309 unique transposable element insertion loci. [c322ce6575cc1c3a-d56b589a::s181]
> **Answer: 12,300**

Cited: c322ce6575cc1c3a-d56b589a::s181

### `517e7cf8-c5d2-4391-9e2a-235b79d93050`
> Drosophila with an H3.3K36R mutation complete development and eclose at a frequency of approximately 80%. [116c0e949dd415fc-61f4295b::s281]
> The best answer is: **80%**

Cited: 116c0e949dd415fc-61f4295b::s281

### `cb710074-73a8-4407-b0c7-7dc868f1bc76`
_Refused._

### `5c4c602c-9624-4eae-ac44-efe4c0dd10e6`
> A large oligosaccharide density was observed in the cryo-EM map of Nav1.6 at amino acid position Asn326. [d79480166f4ab0e3-4297b383::s79]
> **Answer: Asn326**

Cited: d79480166f4ab0e3-4297b383::s79

### `c9bdb9b5-28c1-44da-93b6-b1fc9d8bf369`
> Based on the provided sources, the number of tumor-infiltrating leukocytes is highest in the **evening**.

In experiments with B16-F10-OVA melanoma cells injected into mice, tumors were harvested at four different times of day (morning at ZT1, day at ZT7, evening at ZT13, and night at ZT19). The overall number of tumor-infiltrating leukocytes (TILs) was highly dependent on the time of day of tumor harvest, with total leukocyte numbers peaking in the evening (ZT13). [40349a281d8b56ff-7979b34d::s110]
> This finding was confirmed by immunofluorescence staining of tumor sections, which showed higher T cell numbers in the evening (ZT13) compared with the morning (ZT1). [40349a281d8b56ff-7979b34d::s112]

Cited: 40349a281d8b56ff-7979b34d::s110, 40349a281d8b56ff-7979b34d::s112

### `e6b0f9e5-e976-47dc-b839-0b2fca967e9e`
> Based on the single-nuclei RNA sequencing data provided, myotendinous junction myonuclei are enriched for genes involved in **cell–matrix interactions**.

Myotendinous junction myonuclei exhibited enrichment in genes associated with cell-matrix interactions, including COL22A1 and ADGBR4. [f7c3d31ee5706405-5f6af1d3::s122]

Cited: f7c3d31ee5706405-5f6af1d3::s122

### `247eeb85-a552-4b87-b83e-327538fcb8a9`
> Based on the provided sources, the answer is **5.3%**.

The study retrospectively investigated AR levels evaluated by IHC in a cohort including 113 ER+ MBC samples. [476ba9a9e8ea9c14-b5e5878b::s493]
> Results showed that the percentage of AR-negative patients in MBC samples was 5.3%. [476ba9a9e8ea9c14-b5e5878b::s495]

Cited: 476ba9a9e8ea9c14-b5e5878b::s493, 476ba9a9e8ea9c14-b5e5878b::s495

### `a214f5f8-0de8-43cf-82e0-7930003e4a0c`
> **Saponaria vaccaria**

Beta-amyrin synthase from *Saponaria vaccaria* produces the highest yield of beta-amyrin from squalene among the plant sources tested. [e35c8530af941f04-9a7975aa::s100]
> When beta-amyrin synthases from *Artemisia annua*, *Arabidopsis thaliana*, *Glycyrrhiza glabra*, and *Saponaria vaccaria* were compared, the BAS homologue from *S. vaccaria* yielded the highest titre of β-amyrin. [e35c8530af941f04-9a7975aa::s100]

Cited: e35c8530af941f04-9a7975aa::s100

### `a43e5166-d0e8-48f8-a113-648acac7ed59`
> Between postnatal ages P6 to P15, thalamocortical synapse density in the anterior cingulate cortex increases 5-fold in wild-type mice. [c0b69d2af9f2e018-845b5d60::s271]
> **The best answer is: 5x**

Cited: c0b69d2af9f2e018-845b5d60::s271

### `dd29920d-cb70-440f-961c-3e1103776c4f`
> T cells with an anti-CD19 synNotch → sIL-2 receptor circuit expanded by a factor of approximately 100 within a mouse tumor. [34f4e70030aa5d35-a24b74ef::s130]
> **The best answer is: 100**

Cited: 34f4e70030aa5d35-a24b74ef::s130

### `7d805bb8-4c7c-431f-b068-acf5e5459985`
> MLH1dn expression increases editing efficiency of the PE2 editing system by an average of 7.7-fold. [fa808d37a77e6019-79d6e54c::s96]
> The best answer is: **7.7x**

Cited: fa808d37a77e6019-79d6e54c::s96

### `8d7fa642-ee46-4a13-8ea9-61cc2d4f4ddd`
> A version of Apollo with a deletion of amino acids 344-360 (Apollo/Delta1 PK) has been shown to reduce the interaction between Apollo and DNA-PKcs in HEK293T cells. [cea2facf97f5150c-660a07bf::s360]
> This deletion removes the DNA-PK binding motif that is similar to that of Artemis. [cea2facf97f5150c-660a07bf::s61]
> **The best answer is: residues 344–360**

Cited: cea2facf97f5150c-660a07bf::s360, cea2facf97f5150c-660a07bf::s61

### `487539f9-2f17-4009-aa4a-c41322445f11`
> Based on the provided sources, the best answer is **aa 31-40**.

Here is the supporting evidence:

The N-terminus of COSA-1 mediates interaction with MSH-5 and ZHP-3.
> Researchers tested COSA-1 N-terminal truncations (aa 1-10, 1-20, 1-30, 1-40, and 1-53) using yeast two-hybrid assays.
> The truncated COSA-1 constructs spanning aa 1-10, 1-20, and 1-30 could all interact with MSH-5 and ZHP-3, but COSA-1 1-40 showed dramatically decreased interactions with these two proteins.
> The interaction was further weakened to an undetectable level upon deleting 13 additional amino acids from the N-terminus (creating COSA-1 1-53), suggesting that the N-terminal 53 amino acids play a vital role in interactions with MSH-5 and ZHP-3.
> Since aa 1-30 retained interaction ability but aa 1-40 showed dramatically decreased interaction, the critical region lies within aa 31-40.

### `5049c648-b1bb-4624-8824-9d93dfb04e51`
> Disruption of MTF1 expression in Chlamydomonas results in depletion of the photosynthetic machinery. [9afb8ab3b1d5ff95-b03dfb72::s238]
> Specifically, loss of MTF1 expression caused the disruption of the entire photosynthetic apparatus and most of the chloroplast-expressed proteins. [9afb8ab3b1d5ff95-b03dfb72::s238]
> **The best answer is: Depletion of photosynthetic machinery**

Cited: 9afb8ab3b1d5ff95-b03dfb72::s238

### `a18883e9-218a-4719-8d2c-cf94d740de1a`
> **Yes**

Hair cells (hair follicles) do regenerate in wounds treated with verteporfin in mouse models. By postoperative day 30, verteporfin-treated wounds regrew levels of hair follicles comparable with those in unwounded skin, whereas control PBS-treated wounds formed bare areas without hair follicles. [7dead537a45e92bd-e35471f4::s89]
> A striking difference between PBS- and verteporfin-treated wounds was the emergence of regenerated hair follicles in the latter within 30 days; control wounds formed bare areas. [7dead537a45e92bd-e35471f4::s253]

Cited: 7dead537a45e92bd-e35471f4::s253, 7dead537a45e92bd-e35471f4::s89

### `d7833c0f-2a16-40d2-b6a0-6764aa3003a6`
> **Yes**

Metabolic glycan labeling immobilizes dendritic cell membrane and enhances antitumor efficacy of dendritic cell vaccine.
> More specifically, metabolic glycan labeling reduces the mobility of dendritic cell membrane proteins.
> This reduced membrane mobility activates dendritic cells and improves their antigen presentation and T cell priming properties.
> Metabolic glycan labeling itself enhances the antitumor efficacy of dendritic cell vaccines.
> Additionally, the chemical tags introduced via metabolic glycan labeling enable conjugation of cytokines onto dendritic cells, which further enhances cytotoxic T lymphocyte response and antitumor efficacy.

### `1ccdc348-50e1-4941-9151-5e50411a2b41`
> Targeting sgRNAs to coding strands in gene bodies leads to higher effect sizes on average across multiple CRISPRi screens. [b0c70be4f4a933d3-7fb87fac::s328]
> In all 17 CRISPRi screens examined, the average effect sizes of sgRNAs targeting coding strands within gene bodies were more than twofold higher than those targeting the template strands. [b0c70be4f4a933d3-7fb87fac::s328]
> **Answer: coding strand**

Cited: b0c70be4f4a933d3-7fb87fac::s328

### `1e5f5199-84f4-4133-ab87-2372fa6ca722`
_Refused._

### `d2860d38-dfb9-4b80-905f-812c32573915`
> The best answer is **S. epidermis**.

Engineered strains of S. epidermidis can stimulate T cells specific for non-native epitopes. [8e4b7872a7579d54-cb6467cd::s93]
> The engineered S. epidermidis strains were designed to express non-native antigens and successfully primed antigen-specific T cells in vivo under physiologic conditions of colonization. [8e4b7872a7579d54-cb6467cd::s92]

Cited: 8e4b7872a7579d54-cb6467cd::s92, 8e4b7872a7579d54-cb6467cd::s93

### `77a41274-cd9c-48bc-a347-e0746907840d`
> Expression of human mu-opioid receptor (HsMOR) with an N-terminal yeast αPrePro sequence results in **Enlarged granular cells**.

The α PrePro sequence resulted in enlarged granular cells, expanded ER membranes, and relocalization of HsMOR-GFP to puncta. [33d9e243f2ee99de-02bbb79f::s173]

Cited: 33d9e243f2ee99de-02bbb79f::s173

### `5a2128ad-3127-4595-b810-db128d1a2335`
> Based on the provided sources, the ColabFold homology-based structure prediction for HcKCR1 had poor prediction for **TM3**.

Source [f2e1fb5c9886efad-202dbbbb::s114]
> explicitly states: "However, the homology models were weak in the extracellular TM2-TM3 loop region and did not predict partial unwinding of TM3 at the extracellular end, an unusual feature of Hc ChRs that they share with ChRmine."

In contrast, source [f2e1fb5c9886efad-202dbbbb::s113]
> indicates that "models were particularly good for helices TM1, TM6, and TM7," which were well-predicted.
> The answer is: **TM3**

Cited: f2e1fb5c9886efad-202dbbbb::s113, f2e1fb5c9886efad-202dbbbb::s114

### `d65103ae-c881-4116-a0a7-1b233eb6275a`
> Based on the provided sources, the best answer is **gp02**.

Regulation of gp02 occurs in the coding sequence. [d1ef96583ec64586-195f7c93::s219]
> In contrast, regulation of the three host genes (rpoS, cyaA, and petA) all involved sequestration of the target ribosome-binding site, not the coding sequence. [d1ef96583ec64586-195f7c93::s219]

Cited: d1ef96583ec64586-195f7c93::s219

### `ab5eb050-d134-4445-9307-6faa08be7474`
> Formation of the mycobacterial repressor DarR dimer results in the burial of approximately 1300 Ångström² of surface from the solvent. [405dcaff86bce126-c6c89512::s68]
> The best answer is: **1300 anstrom^2**

Cited: 405dcaff86bce126-c6c89512::s68

### `82de3e92-abe2-46ac-ad17-23417b9c4da7`
> When ECL3 from A3AR was grafted onto A2AAR (and other adenosine receptor backbones), the resulting chimeric receptors gained the ability to bind CF101 with increased efficacy. [23f9c4bad2271b89-675be55a::s148]
> **Answer: increases**

Cited: 23f9c4bad2271b89-675be55a::s148

### `7cf0fcde-fea8-420c-8531-2f2fe9e38980`
> **Yes**

Researchers have assessed doing tagmentation of cDNA directly in the PCR mix without cleaning and quantifying the cDNA first. [70758b216a7dc837-240c67f2::s37]
> They termed this strategy "Smart-seq3xpress," where cDNA products after preamplification at fewer cycles could directly be tagmented without steps including concentration measurements, bioanalyzer QC traces, and cDNA amount normalization. [70758b216a7dc837-240c67f2::s36]
> Libraries were generated without any need for additional enzymatic reaction clean-ups. [70758b216a7dc837-240c67f2::s38]

Cited: 70758b216a7dc837-240c67f2::s36, 70758b216a7dc837-240c67f2::s37, 70758b216a7dc837-240c67f2::s38

### `da5b2a8f-ba08-4692-851f-2e0bf142a02f`
> **Yes**

Researchers performed a base-editing screen against splice sites in CD33. [6acd5496cc0d3cfd-49391314::s129]
> Specifically, they performed a systematic mutagenesis screen of CD33 splice sites using base editor ABE8e. [6acd5496cc0d3cfd-49391314::s123]
> Additionally, they conducted a second systematic mutagenesis screen of CD33 splice sites using evoFERNY protein instead of ABE8e. [6acd5496cc0d3cfd-49391314::s249]

Cited: 6acd5496cc0d3cfd-49391314::s123, 6acd5496cc0d3cfd-49391314::s129, 6acd5496cc0d3cfd-49391314::s249
