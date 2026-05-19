# Eval Report: alce_qampari_gtr

- **Pipeline:** `anthropic/claude-haiku-4-5 | bge-small | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=5 | no-verifier | loose | gen=prompted`
- **Run at:** 2026-05-18 21:20:57
- **Questions:** 1000

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.000 |
| `citation_recall` | 1.000 |
| `citation_f1` | 0.000 |
| `coverage` | 0.000 |
| `localization_accuracy` | 0.251 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `799__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.64 |
| `136__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `248__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.35 |
| `366__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `663__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.61 |
| `777__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `386__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `843__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `801__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `8__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `481__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `439__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `772__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `336__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.71 |
| `479__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `573__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.72 |
| `885__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `683__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `356__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.87 |
| `960__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `744__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `671__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `665__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.84 |
| `1334__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `145__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `611__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.16 |
| `806__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `224__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `577__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `12__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `699__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `285__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `891__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `804__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.39 |
| `972__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `642__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `1008__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `930__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `62__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `317__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.65 |
| `902__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `29__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `851__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `719__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `739__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `639__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.71 |
| `607__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `897__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.44 |
| `437__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `758__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.81 |
| `599__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `927__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `834__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `815__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.92 |
| `174__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `487__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `414__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `460__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `859__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `610__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `278__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `743__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `948__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.39 |
| `524__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.56 |
| `353__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `818__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `403__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `387__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `360__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.81 |
| `1012__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1002__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.69 |
| `234__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `555__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `449__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `893__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `633__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `935__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `253__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `951__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `498__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.78 |
| `374__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `721__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `377__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `587__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `741__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `707__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `293__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `773__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.88 |
| `212__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `195__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `283__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `569__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `675__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.74 |
| `1351__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `14__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `461__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.90 |
| `903__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.76 |
| `325__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `58__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `916__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `919__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `723__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `628__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.70 |
| `379__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `654__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.59 |
| `714__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `338__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.53 |
| `1352__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `196__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `289__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.48 |
| `1000__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `965__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `333__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `281__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `539__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.50 |
| `52__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `80__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `310__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `657__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.28 |
| `429__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `508__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.87 |
| `936__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.93 |
| `362__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.84 |
| `784__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.81 |
| `231__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `247__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `644__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.48 |
| `71__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `492__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.63 |
| `562__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `979__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.83 |
| `636__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `39__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `226__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `757__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `618__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.57 |
| `418__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `56__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `767__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `594__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `648__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.32 |
| `4__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `875__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.77 |
| `826__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `868__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `191__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.69 |
| `769__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.76 |
| `855__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `593__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `73__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `846__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `1252__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `494__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.51 |
| `205__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `632__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.41 |
| `865__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `690__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `704__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.60 |
| `456__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `929__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `13__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.68 |
| `713__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `519__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.95 |
| `914__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `749__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `586__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `798__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.16 |
| `162__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `184__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `658__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.88 |
| `288__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `103__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `630__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `819__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `672__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `351__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `655__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `934__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `182__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `428__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.73 |
| `1010__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `9__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `37__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `416__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `835__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.82 |
| `931__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `740__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.45 |
| `623__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.76 |
| `638__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.26 |
| `364__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `958__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `522__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.95 |
| `447__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `24__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `653__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `1254__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `287__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `584__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `33__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `95__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `1353__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `684__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `768__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `693__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `230__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `408__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.64 |
| `252__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `583__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.20 |
| `718__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.70 |
| `484__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `616__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.63 |
| `144__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `592__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `925__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.57 |
| `775__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `110__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `426__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `15__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `120__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.63 |
| `966__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `440__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `413__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.82 |
| `820__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `664__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `118__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.92 |
| `260__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1259__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.20 |
| `358__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.72 |
| `711__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `751__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.95 |
| `354__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.84 |
| `560__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `715__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `643__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `790__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `404__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `148__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `232__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `874__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `670__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `211__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `308__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `280__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `150__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `917__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `933__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.79 |
| `629__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `319__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `755__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `235__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `46__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `698__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.85 |
| `105__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `343__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `756__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.59 |
| `515__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `779__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `572__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `397__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `465__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `949__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.85 |
| `800__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `538__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `375__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `36__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `736__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `491__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `750__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `1256__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `809__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.77 |
| `82__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `689__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.80 |
| `202__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.32 |
| `111__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `516__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `645__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `944__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `6__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `405__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `464__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `198__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `634__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `896__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `161__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `122__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.80 |
| `1354__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.87 |
| `321__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `301__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `119__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `668__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `805__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `284__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `595__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `369__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `852__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.90 |
| `729__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `659__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.31 |
| `208__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `419__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `898__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `963__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `49__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `695__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.87 |
| `637__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `793__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.78 |
| `272__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `1251__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `588__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `422__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `911__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `40__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.82 |
| `341__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `565__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.86 |
| `900__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `251__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `742__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.74 |
| `557__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `177__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `920__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `391__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.44 |
| `1355__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.76 |
| `309__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `335__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.19 |
| `615__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `597__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `945__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `318__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `22__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `766__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.27 |
| `1356__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `600__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `237__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.79 |
| `549__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.24 |
| `109__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `734__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `482__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `696__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `222__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `621__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `459__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.81 |
| `116__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.24 |
| `703__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `394__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `238__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `537__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `502__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `559__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `1357__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `425__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `327__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.69 |
| `181__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `554__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `477__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.10 |
| `307__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.88 |
| `604__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.58 |
| `1006__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.10 |
| `1103__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1253__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `55__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.71 |
| `889__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `17__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.73 |
| `70__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `849__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.26 |
| `513__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.67 |
| `526__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `1358__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `976__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `716__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.24 |
| `552__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `824__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `476__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `535__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `631__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `735__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.73 |
| `240__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `44__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `541__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.05 |
| `332__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `457__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `782__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `561__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `558__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.55 |
| `651__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `964__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `79__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.68 |
| `67__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `367__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `771__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `1007__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.18 |
| `576__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `622__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.70 |
| `407__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `973__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.79 |
| `813__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.68 |
| `867__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `923__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `114__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `857__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `166__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `257__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `620__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `124__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `313__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `504__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `60__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `135__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `323__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.61 |
| `402__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `971__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.77 |
| `292__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `829__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `104__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `781__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `20__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `568__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `879__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.27 |
| `378__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `228__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `692__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `493__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.19 |
| `544__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `1250__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `895__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `957__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.90 |
| `274__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `1011__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.85 |
| `881__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `548__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.52 |
| `1359__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `928__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `660__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `759__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `125__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.97 |
| `134__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `434__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `788__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.26 |
| `564__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.54 |
| `924__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `217__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `506__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `359__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `720__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.86 |
| `589__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `21__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `894__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `244__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `864__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `947__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.76 |
| `939__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `679__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.69 |
| `130__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.57 |
| `269__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.29 |
| `462__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.66 |
| `505__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.61 |
| `123__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `470__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.84 |
| `11__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `398__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `113__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `866__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `147__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `941__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `254__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `495__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `811__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.40 |
| `862__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.09 |
| `904__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.81 |
| `627__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `421__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `880__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `183__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `712__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `550__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.63 |
| `656__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `480__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `662__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.35 |
| `157__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.87 |
| `613__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `760__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.71 |
| `290__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `764__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `233__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `97__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.02 |
| `72__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `647__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `330__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1003__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.90 |
| `486__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.45 |
| `778__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `483__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `950__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `334__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.60 |
| `770__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `830__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `83__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `300__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `273__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `575__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `1257__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.85 |
| `132__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `901__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.43 |
| `940__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `61__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.78 |
| `1360__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `814__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.76 |
| `591__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `159__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `531__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.66 |
| `840__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `872__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.78 |
| `303__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.69 |
| `94__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.11 |
| `3__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `270__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `433__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `63__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `530__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.16 |
| `676__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.83 |
| `932__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.85 |
| `342__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `823__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `543__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `838__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.72 |
| `1014__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `687__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.75 |
| `87__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.76 |
| `910__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `34__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `842__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.78 |
| `489__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.93 |
| `1361__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `614__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `54__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `142__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `209__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `510__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `762__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `188__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `906__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `546__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.74 |
| `207__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `977__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `1009__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `276__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `747__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.38 |
| `796__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `856__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `151__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.88 |
| `392__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `580__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `701__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `168__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `785__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.60 |
| `761__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.17 |
| `340__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `792__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `458__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `888__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.75 |
| `839__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.58 |
| `724__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `363__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.26 |
| `107__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `574__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `501__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `1300__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.86 |
| `390__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `887__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `878__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.52 |
| `752__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `423__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.17 |
| `214__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `304__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `411__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `84__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.78 |
| `153__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.67 |
| `65__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `265__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.39 |
| `215__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `98__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.68 |
| `853__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `112__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `357__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `877__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `709__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `488__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `348__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.77 |
| `912__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `266__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `74__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.59 |
| `890__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.52 |
| `1013__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `581__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `345__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `294__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.92 |
| `1__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `337__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.64 |
| `571__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `942__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `101__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `922__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `585__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `807__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.47 |
| `129__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `795__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `451__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.89 |
| `329__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `43__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `370__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `229__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `673__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `256__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `1005__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `605__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `667__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.39 |
| `832__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `170__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.37 |
| `66__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `523__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.85 |
| `271__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `722__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.09 |
| `227__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `727__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.08 |
| `92__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `496__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.78 |
| `961__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.63 |
| `905__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.53 |
| `204__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `1004__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.23 |
| `612__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.65 |
| `503__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `18__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `533__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `705__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `726__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `302__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.36 |
| `400__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.76 |
| `381__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.61 |
| `137__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `542__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `176__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `431__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `926__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `753__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `438__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `146__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `579__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `1362__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.92 |
| `282__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `678__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.91 |
| `609__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.81 |
| `794__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `567__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `797__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `255__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `424__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.83 |
| `946__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `128__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `324__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `51__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.94 |
| `625__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1258__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `203__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `450__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `967__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.68 |
| `180__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `30__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.49 |
| `825__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `952__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.57 |
| `28__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `978__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `677__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `331__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `210__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `165__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `117__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `854__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `602__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.89 |
| `446__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `666__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `732__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.90 |
| `78__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `968__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.08 |
| `787__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `512__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `845__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `652__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `131__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `399__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `372__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `96__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `75__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `780__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `178__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `90__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `115__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `837__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `314__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `296__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.71 |
| `869__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `848__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `441__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.74 |
| `937__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `173__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.52 |
| `680__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `836__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `509__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.85 |
| `499__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `89__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `528__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.72 |
| `754__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `85__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `355__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `1101__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `706__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.71 |
| `241__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.54 |
| `1363__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.67 |
| `371__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `969__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.82 |
| `858__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `1255__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.43 |
| `681__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `32__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `352__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `786__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `47__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `817__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `646__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.58 |
| `702__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `384__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.58 |
| `158__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `453__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `455__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `871__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `297__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `882__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `406__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.86 |
| `507__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `669__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `844__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `50__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `469__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `139__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.44 |
| `200__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.57 |
| `478__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.28 |
| `943__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `199__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `812__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `179__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `25__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `409__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `497__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.72 |
| `376__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.61 |
| `385__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `626__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `193__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.98 |
| `737__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.61 |
| `746__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `412__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `873__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `261__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `527__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `566__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `312__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `311__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `295__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `954__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `427__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `220__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `468__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `841__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `921__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.91 |
| `803__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `218__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `194__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `1350__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `76__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `236__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `598__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `185__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `53__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `187__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `915__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `42__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `816__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `1364__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.59 |
| `763__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `339__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.74 |
| `828__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `774__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.72 |
| `396__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.17 |
| `955__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.72 |
| `731__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `861__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `532__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `553__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `635__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.80 |
| `907__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `511__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `467__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `789__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `617__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.84 |
| `365__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `821__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.47 |
| `1365__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `7__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `395__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.70 |
| `383__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `201__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `192__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `243__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `167__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `748__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `810__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `91__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.49 |
| `938__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `831__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `463__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `913__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `246__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `149__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.38 |
| `346__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `38__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.69 |
| `190__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `275__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `802__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `102__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `264__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `382__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `221__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `69__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `326__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `959__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `650__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `545__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `471__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.84 |
| `258__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `68__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `262__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `268__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `518__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.87 |
| `2__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `31__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `808__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `827__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.27 |
| `547__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.20 |
| `445__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.69 |
| `619__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `239__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `373__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.23 |
| `443__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `263__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `1366__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `738__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `640__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `466__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `368__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.35 |
| `349__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `863__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `883__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `520__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `833__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `454__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `847__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.30 |
| `160__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `525__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `521__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `909__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `1102__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `783__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `850__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.46 |
| `1001__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `956__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `975__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `596__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `436__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `57__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.64 |
| `389__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `186__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `745__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.71 |
| `822__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `485__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.89 |
| `401__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.84 |
| `717__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.53 |
| `141__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `590__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `953__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.65 |
| `918__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.42 |
| `694__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.83 |
| `601__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `691__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `860__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.58 |
| `490__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.50 |
| `250__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `776__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.04 |
| `316__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.90 |
| `608__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `733__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `970__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `163__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `415__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `442__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `710__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `765__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `361__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.45 |
| `536__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `138__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `641__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `219__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `556__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.64 |
| `126__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `155__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `686__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `886__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.62 |
| `472__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `106__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.93 |
| `299__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `175__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.12 |
| `152__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `0__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `884__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `908__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `64__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.63 |
| `624__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.71 |
| `708__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `143__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.31 |
| `474__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `870__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `45__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.52 |
| `298__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `197__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `417__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.85 |
| `603__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `306__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.81 |
| `35__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `1367__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `225__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.76 |
| `682__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `267__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `876__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `444__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `728__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `432__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `570__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.46 |
| `259__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `974__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `435__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.92 |
| `305__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `320__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `649__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `286__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `171__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `563__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `245__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `534__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.91 |
| `26__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `169__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.11 |
| `674__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `725__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.77 |
| `730__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `430__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `172__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `606__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `700__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `452__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `213__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `410__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `514__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `81__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `475__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.87 |
| `99__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `688__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1368__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `206__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `661__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `540__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `517__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `962__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `473__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `697__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `388__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.58 |
| `133__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `86__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `322__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `27__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `791__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `88__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `899__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `108__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `892__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `500__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `529__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `551__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `578__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `448__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `154__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `582__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `156__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `121__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.80 |
| `140__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `328__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.44 |

## Per-question answers

### `799__wikidata_simple__dev`
> Ryoichi Ikegami drew "Crying Freeman" with writer Kazuo Koike. [alce::799__wikidata_simple__dev::p12]

Cited: alce::799__wikidata_simple__dev::p12

### `136__wikidata_intersection__dev`
> Harmony Korine was both screenwriter and director of several movies. He wrote and directed "Spring Breakers", "Gummo", "Julien Donkey-Boy", and "Mister Lonely". [alce::136__wikidata_intersection__dev::p0]
> He also wrote and directed "Trash Humpers". [alce::136__wikidata_intersection__dev::p3]

Cited: alce::136__wikidata_intersection__dev::p0, alce::136__wikidata_intersection__dev::p3

### `248__wikidata_comp__dev`
_Refused._

### `366__wikidata_comp__dev`
_Refused._

### `663__wikidata_simple__dev`
_Refused._

### `777__wikidata_simple__dev`
> Jewell Loyd was selected in the draft by the Seattle Storm. [alce::777__wikidata_simple__dev::p69]
> She was drafted first overall in the 2015 WNBA Draft. [alce::777__wikidata_simple__dev::p69]

Cited: alce::777__wikidata_simple__dev::p69

### `386__wikidata_comp__dev`
> Toby Howarth, the first area Bishop of Bradford, was educated at Yale University and Wycliffe Hall, Oxford. [alce::386__wikidata_comp__dev::p22]
> He also studied at Birmingham University for his MA. [alce::386__wikidata_comp__dev::p22]

Cited: alce::386__wikidata_comp__dev::p22

### `843__wikidata_simple__dev`
> Scott Z. Burns has written screenplays for "The Bourne Ultimatum" (2007), "The Informant!" (2009), and "Contagion" (2011). [alce::843__wikidata_simple__dev::p0]
> He also wrote the screenplay for "Side Effects". [alce::843__wikidata_simple__dev::p0]

Cited: alce::843__wikidata_simple__dev::p0

### `801__wikidata_simple__dev`
> David G. Hartwell edited numerous pieces of literature. He edited the best-novel Nebula Award-winners "Timescape" by Gregory Benford (1980), "The Claw of the Conciliator" by Gene Wolfe (1981), and "No Enemy But Time" by Michael Bishop (1982). [alce::801__wikidata_simple__dev::p4]
> He also edited the best-novel Hugo Award-winner "Hominids" by Robert J. Sawyer (2002) and the World Fantasy Award-winning novels "The Shadow of the Torturer" by Gene Wolfe (1981) and "The Dragon Waiting" by John M. Ford (1984). [alce::801__wikidata_simple__dev::p4]
> Additionally, he edited numerous anthologies, including two annual anthologies: "Year's Best SF" (started in 1996 and co-edited with Kathryn Cramer since 2002) and "Year's Best Fantasy" (co-edited with Cramer). [alce::801__wikidata_simple__dev::p3]

Cited: alce::801__wikidata_simple__dev::p3, alce::801__wikidata_simple__dev::p4

### `8__wikitables_composition__dev`
> The Electric Tower is the seventh tallest building in Buffalo. [alce::8__wikitables_composition__dev::p7]
> The Liberty Building is the fifth tallest building in Buffalo. [alce::8__wikitables_composition__dev::p17]
> The Key Center North Tower is the eighth tallest building in Buffalo. [alce::8__wikitables_composition__dev::p47]

Cited: alce::8__wikitables_composition__dev::p17, alce::8__wikitables_composition__dev::p47, alce::8__wikitables_composition__dev::p7

### `481__wikitables_simple__dev`
> Several magazines are science fiction magazines based on the provided sources:

Space Science Fiction Magazine was a US science fiction magazine published by Republic Features Syndicate, Inc. [alce::481__wikitables_simple__dev::p2]
> Science Fiction (full title: Science Fiction, Fantasy i Horror) is a Polish speculative fiction monthly magazine. [alce::481__wikitables_simple__dev::p11]
> Vargo Statten Science Fiction Magazine was a British science fiction magazine which published nineteen issues between 1954 and 1956. [alce::481__wikitables_simple__dev::p58]

Cited: alce::481__wikitables_simple__dev::p11, alce::481__wikitables_simple__dev::p2, alce::481__wikitables_simple__dev::p58

### `439__wikidata_intersection__dev`
> Based on the provided sources, I can identify one movie for which Mani Ratnam worked on the script and served as producer:

"Thiruda Thiruda" is the film for which Mani Ratnam wrote the script and served as producer under his production studio, Aalayam Productions, alongside his co-producer Sriram. [alce::439__wikidata_intersection__dev::p6]

Cited: alce::439__wikidata_intersection__dev::p6

### `772__wikidata_simple__dev`
> An example of the marine vessel classification German Type U 31 is U-31 (S181), which is a Type 212A submarine of the German Navy. [alce::772__wikidata_simple__dev::p15]
> U-31 was built by TKMS with construction at the shipyards of Thyssen Nordseewerke of Emden and Howaldtswerke at Kiel, and was launched on 20 March 2002. [alce::772__wikidata_simple__dev::p15]

Cited: alce::772__wikidata_simple__dev::p15

### `336__wikidata_comp__dev`
_Refused._

### `479__wikitables_simple__dev`
> Bog bodies are human cadavers that have been naturally mummified in peat bogs. [alce::479__wikitables_simple__dev::p2]
> They are sometimes known as bog people and have been dated to between 8000 BCE and the Second World War. [alce::479__wikitables_simple__dev::p2]
> The principal locations where bog bodies have been discovered are the Northern European countries of Germany, the Netherlands, the United Kingdom, Ireland, and especially Denmark. [alce::479__wikitables_simple__dev::p7]
> The oldest of these bodies dates to about 8000 BCE, although the majority of specimens in Denmark are from the Pre-Roman Iron Age to Roman Iron Age era (about 500 BC to 400 CE). [alce::479__wikitables_simple__dev::p7]
> As of 2006, more than 700 ancient bodies have been discovered in these sites, although other estimates have placed the number in the thousands. [alce::479__wikitables_simple__dev::p7]
> In 1965, the German scientist Alfred Dieck cataloged more than 1,850 bog bodies, but later scholarship revealed much of Dieck's work was erroneous, and an exact number of discovered bodies is unknown. [alce::479__wikitables_simple__dev::p0]
> Unlike most ancient human remains, bog bodies often retain their skin and internal organs due to the unusual conditions of the surrounding area. [alce::479__wikitables_simple__dev::p2]
> The vast majority of the bog bodies that have been discovered date from the Iron Age, a period of time when peat bogs covered a much larger area of northern Europe. [alce::479__wikitables_simple__dev::p26]
> Notable examples include Lindow Man, discovered in a peat bog at Lindow Moss near Wilmslow in Cheshire, North West England on 1 August 1984. [alce::479__wikitables_simple__dev::p23]

Cited: alce::479__wikitables_simple__dev::p0, alce::479__wikitables_simple__dev::p2, alce::479__wikitables_simple__dev::p23, alce::479__wikitables_simple__dev::p26, alce::479__wikitables_simple__dev::p7

### `573__wikidata_simple__dev`
_Refused._

### `885__wikidata_simple__dev`
> Trey Anastasio is best known as the lead vocalist and guitarist for the rock band Phish, which he co-founded in 1983. [alce::885__wikidata_simple__dev::p1]
> In addition to his work with Phish, he is the leader of the Trey Anastasio Band and was the frontman for the groups Oysterhead and Surrender. [alce::885__wikidata_simple__dev::p1]

Cited: alce::885__wikidata_simple__dev::p1

### `683__wikidata_simple__dev`
_Refused._

### `356__wikidata_intersection__dev`
_Refused._

### `960__wikidata_comp__dev`
> Several First-Circuit Appeals Court Judges attended college at different institutions:

Jeffrey R. Howard attended Plymouth State College (now Plymouth State University), graduating in 1978 with a Bachelor of Arts degree. [alce::960__wikidata_comp__dev::p0]
> William J. Kayatta Jr. earned a Bachelor of Arts degree in 1976 from Amherst College. [alce::960__wikidata_comp__dev::p27]
> Levin H. Campbell received an Artium Baccalaureus degree from Harvard University in 1948. [alce::960__wikidata_comp__dev::p56]
> Bailey Aldrich graduated from Harvard University with an Artium Baccalaureus degree in 1928. [alce::960__wikidata_comp__dev::p30]

Cited: alce::960__wikidata_comp__dev::p0, alce::960__wikidata_comp__dev::p27, alce::960__wikidata_comp__dev::p30, alce::960__wikidata_comp__dev::p56

### `744__wikidata_simple__dev`
> Baojun manufactures automobiles, specifically cars and crossover SUVs. [alce::744__wikidata_simple__dev::p0]
> The company's products include compact sedans such as the Baojun 630, which was the first car produced by Baojun. [alce::744__wikidata_simple__dev::p3]
> Baojun also manufactures subcompact hatchbacks like the Baojun 310. [alce::744__wikidata_simple__dev::p5]
> Additionally, Baojun produces compact crossover SUVs such as the RS-5. [alce::744__wikidata_simple__dev::p1]

Cited: alce::744__wikidata_simple__dev::p0, alce::744__wikidata_simple__dev::p1, alce::744__wikidata_simple__dev::p3, alce::744__wikidata_simple__dev::p5

### `671__wikidata_simple__dev`
> Based on the provided sources, the East Nippon Expressway Company maintains the following expressways:

The Hachinohe Expressway is maintained and tolled by the East Nippon Expressway Company. [alce::671__wikidata_simple__dev::p3]
> The Kamaishi Expressway is partially maintained by the East Nippon Expressway Company, specifically from Hanamaki to Tōwa. [alce::671__wikidata_simple__dev::p12]
> The Hokuriku Expressway is owned and managed by the East Nippon Expressway Company (in conjunction with Central Nippon Expressway Company). [alce::671__wikidata_simple__dev::p31]

Cited: alce::671__wikidata_simple__dev::p12, alce::671__wikidata_simple__dev::p3, alce::671__wikidata_simple__dev::p31

### `665__wikidata_simple__dev`
> German submarine U-74 was a marine vessel in the German Type VIIB classification. [alce::665__wikidata_simple__dev::p24]

Cited: alce::665__wikidata_simple__dev::p24

### `1334__wikidata_simple__dev`
> Several ships were Solstice-class cruise ships. The lead vessel of the class was Celebrity Solstice. [alce::1334__wikidata_simple__dev::p0]
> The second ship of the class was Celebrity Equinox. [alce::1334__wikidata_simple__dev::p0]
> The third ship of the class was Celebrity Eclipse, delivered on April 15, 2010. [alce::1334__wikidata_simple__dev::p0]
> The fourth ship was Celebrity Silhouette, which sailed on her Maiden Voyage on July 23, 2011. [alce::1334__wikidata_simple__dev::p0]
> The fifth ship was Celebrity Reflection, launched in August 2012. [alce::1334__wikidata_simple__dev::p0]

Cited: alce::1334__wikidata_simple__dev::p0

### `145__wikidata_comp__dev`
> I need to identify which TV show had a screenplay written by B. J. Novak, and then find who directed it.

From the sources, B. J. Novak wrote screenplays for multiple episodes of "The Office":

1. "Sexual Harassment" - written by B. J. Novak and directed by Ken Kwapis [alce::145__wikidata_comp__dev::p32]
> 2. "Counseling" - written by B. J. Novak and directed by Jeffrey Blitz [alce::145__wikidata_comp__dev::p2]
> 3. "Local Ad" - written by B. J. Novak and directed by Jason Reitman [alce::145__wikidata_comp__dev::p78]
> Since the question asks "who directed the TV show" (singular) without specifying which episode, and multiple directors worked on different episodes of "The Office," I can provide the directors of the episodes whose screenplays were written by B. J. Novak:

Ken Kwapis directed "Sexual Harassment," an episode of "The Office" whose screenplay was written by B. J. Novak. [alce::145__wikidata_comp__dev::p32]
> Jeffrey Blitz directed "Counseling," an episode of "The Office" whose screenplay was written by B. J. Novak. [alce::145__wikidata_comp__dev::p2]
> Jason Reitman directed "Local Ad," an episode of "The Office" whose screenplay was written by B. J. Novak. [alce::145__wikidata_comp__dev::p78]

Cited: alce::145__wikidata_comp__dev::p2, alce::145__wikidata_comp__dev::p32, alce::145__wikidata_comp__dev::p78

### `611__wikidata_simple__dev`
_Refused._

### `806__wikidata_simple__dev`
> Guy Lowell featured his design work at multiple institutions. He designed Lowell Lecture Hall at Harvard and academic buildings at Phillips Academy Andover, Simmons College, and Brown University. [alce::806__wikidata_simple__dev::p14]
> Additionally, he was hired by museum trustees to create a design for a museum on Huntington Avenue in Boston's Fenway-Kenmore neighborhood, where his neoclassical design was completed in two years and featured a façade of granite and a grand rotunda. [alce::806__wikidata_simple__dev::p22]

Cited: alce::806__wikidata_simple__dev::p14, alce::806__wikidata_simple__dev::p22

### `224__wikidata_intersection__dev`
> Based on the provided sources, there are two movies that Kamal Haasan both directed and screenwritten:

"Hey Ram" (2000) was written, directed, and starred in by Kamal Haasan. [alce::224__wikidata_intersection__dev::p0]
> "Vishwaroopam" (2013) was written, directed and co-produced by Kamal Haasan, who also enacted the lead role. [alce::224__wikidata_intersection__dev::p43]

Cited: alce::224__wikidata_intersection__dev::p0, alce::224__wikidata_intersection__dev::p43

### `577__wikidata_simple__dev`
> Clive Burr was a member of Iron Maiden from 1979 to 1982. [alce::577__wikidata_simple__dev::p8]
> Nicko McBrain is a drummer of the British heavy metal band Iron Maiden, which he joined in 1982 and has remained with since. [alce::577__wikidata_simple__dev::p40]
> Doug Sampson was the drummer for Iron Maiden from 1978 to 1979. [alce::577__wikidata_simple__dev::p41]

Cited: alce::577__wikidata_simple__dev::p40, alce::577__wikidata_simple__dev::p41, alce::577__wikidata_simple__dev::p8

### `12__wikitables_composition__dev`
_Refused._

### `699__wikidata_simple__dev`
> Nia Vardalos was the screenwriter for "My Big Fat Greek Wedding." [alce::699__wikidata_simple__dev::p5]
> She also wrote the screenplay for "My Big Fat Greek Wedding 2." [alce::699__wikidata_simple__dev::p5]

Cited: alce::699__wikidata_simple__dev::p5

### `285__wikidata_intersection__dev`
> Arsenal F.C. competed in and won multiple competitions. The club won the Inter-Cities Fairs Cup in 1970 and the Cup Winners' Cup in 1994. [alce::285__wikidata_intersection__dev::p3]
> Additionally, Arsenal has won 13 League titles, a record 13 FA Cups, two League Cups, the League Centenary Trophy, and 15 FA Community Shields. [alce::285__wikidata_intersection__dev::p79]

Cited: alce::285__wikidata_intersection__dev::p3, alce::285__wikidata_intersection__dev::p79

### `891__wikidata_simple__dev`
> Naomi Broady won the $100,000 event in Midland, beating US youngster Robin Anderson in the final. [alce::891__wikidata_simple__dev::p3]
> She also won the 2017 Empire Slovak Open doubles competition on clay, partnered by Heather Watson. [alce::891__wikidata_simple__dev::p15]

Cited: alce::891__wikidata_simple__dev::p15, alce::891__wikidata_simple__dev::p3

### `804__wikidata_simple__dev`
> The Shackleton Ice Shelf separates the Queen Mary Coast to the west from the Knox Coast of Wilkes Land to the east. [alce::804__wikidata_simple__dev::p0]
> Both of these are coastal land masses found next to the ice shelf.

Cited: alce::804__wikidata_simple__dev::p0

### `972__wikidata_comp__dev`
> Based on the provided sources, Joe Pasternak produced motion pictures directed by several filmmakers. These included William Dieterle [alce::972__wikidata_comp__dev::p0]
> , Edmund Heuberger [alce::972__wikidata_comp__dev::p0]
> , Ernst Laemmle [alce::972__wikidata_comp__dev::p0]
> , Henry Koster [alce::972__wikidata_comp__dev::p97]
> , and Norman Taurog [alce::972__wikidata_comp__dev::p97]
> .

Cited: alce::972__wikidata_comp__dev::p0, alce::972__wikidata_comp__dev::p97

### `642__wikidata_simple__dev`
_Refused._

### `1008__wikidata_comp__dev`
> Multiple drivers have won a Coke Zero Sugar 400 competition:

Jimmie Johnson won the 2013 Coke Zero 400. [alce::1008__wikidata_comp__dev::p0]
> David Ragan won the 2011 Coke Zero 400. [alce::1008__wikidata_comp__dev::p3]
> Kyle Busch won a Coke Zero Sugar 400 race. [alce::1008__wikidata_comp__dev::p60]
> Dale Earnhardt, Jr. won the 2015 Coke Zero 400. [alce::1008__wikidata_comp__dev::p8]

Cited: alce::1008__wikidata_comp__dev::p0, alce::1008__wikidata_comp__dev::p3, alce::1008__wikidata_comp__dev::p60, alce::1008__wikidata_comp__dev::p8

### `930__wikidata_simple__dev`
> Rick Alverson directed several films. His first film was "The Builder" (2010). [alce::930__wikidata_simple__dev::p1]
> His second feature was "New Jerusalem" (2011). [alce::930__wikidata_simple__dev::p1]
> He also directed a short film entitled "William Eggleston: Musik" in 2017. [alce::930__wikidata_simple__dev::p2]
> His fifth feature was "The Mountain" (2018), which premiered at the Venice International Film Festival. [alce::930__wikidata_simple__dev::p2]

Cited: alce::930__wikidata_simple__dev::p1, alce::930__wikidata_simple__dev::p2

### `62__wikitables_composition__dev`
> Based on the provided sources, the following cities and municipalities are located in the province of Basilan:

Isabela City is a component city and the capital of the province. [alce::62__wikitables_composition__dev::p13]
> The municipalities in Basilan are Isabela, Lamitan, Tuburan, Tipo-Tipo, Sumisip, Maluso, and Lantawan. [alce::62__wikitables_composition__dev::p5]
> Basilan is subdivided into 11 municipalities and two cities in total. [alce::62__wikitables_composition__dev::p13]

Cited: alce::62__wikitables_composition__dev::p13, alce::62__wikitables_composition__dev::p5

### `317__wikidata_comp__dev`
> The Detroit Tigers participated in multiple competitions mentioned in the sources. In the 1907 World Series, the Chicago Cubs emerged victorious over the Detroit Tigers, winning the Series four games to none (with one tie). [alce::317__wikidata_comp__dev::p42]
> In a more recent competition, the Tigers themselves won the World Series championship, leading their division wire-to-wire and culminating in the championship victory.

Cited: alce::317__wikidata_comp__dev::p42

### `902__wikidata_simple__dev`
> i☆Ris (pronounced "Iris") is a Japanese voice acting and singing female idol group that consists of six members: Saki Yamakita, Yū Serizawa, Himika Akaneya, Yūki Wakai, Miyu Kubota, and Azuki Shibuya. [alce::902__wikidata_simple__dev::p0]
> The leader of the group is Saki Yamakita. [alce::902__wikidata_simple__dev::p0]

Cited: alce::902__wikidata_simple__dev::p0

### `29__wikitables_composition__dev`
> Based on the provided sources, multiple North American Soccer League players transferred to Edmonton in 2016:

Papé Diakite signed for FC Edmonton on 8 February 2016. [alce::29__wikitables_composition__dev::p21]
> Jason Plumhoff joined FC Edmonton on February 25, 2016. [alce::29__wikitables_composition__dev::p45]
> Ledgerwood signed with FC Edmonton on 12 January 2016. [alce::29__wikitables_composition__dev::p19]

Cited: alce::29__wikitables_composition__dev::p19, alce::29__wikitables_composition__dev::p21, alce::29__wikitables_composition__dev::p45

### `851__wikidata_simple__dev`
> Jason Robert Brown composed "Parade" and "The Bridges of Madison County," for which he won Tony Awards. [alce::851__wikidata_simple__dev::p1]
> He also composed "Songs for a New World," his first produced show, which was originally produced Off-Broadway at the WPA Theatre in 1995. [alce::851__wikidata_simple__dev::p5]

Cited: alce::851__wikidata_simple__dev::p1, alce::851__wikidata_simple__dev::p5

### `719__wikidata_simple__dev`
> Based on the provided sources, Ernesto Alonso executive produced (produced) multiple telenovelas:

"El maleficio" is a Mexican telenovela produced by Ernesto Alonso for Televisa in 1983. [alce::719__wikidata_simple__dev::p18]
> "El engaño" is a Mexican telenovela produced by Ernesto Alonso for Televisa in 1986. [alce::719__wikidata_simple__dev::p29]

Cited: alce::719__wikidata_simple__dev::p18, alce::719__wikidata_simple__dev::p29

### `739__wikidata_simple__dev`
> Several individuals served as Deputy Chief of the General Staff of the Israel Defense Forces.

Maj. Gen. Moshe Kaplinsky served as Deputy Chief of the General Staff of the Israel Defense Forces, where he was second in command of the IDF. [alce::739__wikidata_simple__dev::p51]
> Maj. Gen. Dan Harel was a former Deputy Chief of the General Staff, having been appointed to this position on October 1, 2007, replacing Maj. General Moshe Kaplinsky. [alce::739__wikidata_simple__dev::p39]
> Maj. Gen. Yair Naveh is a former Deputy Chief of the General Staff of the Israel Defense Forces. [alce::739__wikidata_simple__dev::p7]

Cited: alce::739__wikidata_simple__dev::p39, alce::739__wikidata_simple__dev::p51, alce::739__wikidata_simple__dev::p7

### `639__wikidata_simple__dev`
_Refused._

### `607__wikidata_simple__dev`
> The Maryland Transportation Authority is in charge of eight toll facilities, currently consisting of two toll roads, two tunnels, and four bridges in Maryland. [alce::607__wikidata_simple__dev::p0]

Cited: alce::607__wikidata_simple__dev::p0

### `897__wikidata_simple__dev`
> David Pithey was an individual who came from Rhodesia. [alce::897__wikidata_simple__dev::p10]

Cited: alce::897__wikidata_simple__dev::p10

### `437__wikidata_intersection__dev`
> Based on the provided sources, Radha Mohan directed multiple films produced by Prakash Raj. The films directed by Radha Mohan and produced by Prakash Raj under Duet Films include: "Azhagiya Theeye" (Tamil), "Mozhi" (Tamil), "Abhiyum Naanum" (Tamil), "Payanam" (Tamil), "Gaganam" (Telugu), and "Gouravam" (Tamil/Telugu). [alce::437__wikidata_intersection__dev::p0]

Cited: alce::437__wikidata_intersection__dev::p0

### `758__wikidata_simple__dev`
> According to the sources provided, Jesus taught his disciples and the people living in Palestine. [alce::758__wikidata_simple__dev::p55]
> Specifically, Jesus taught the message of Jewish messianism to his disciples and to the people living in Palestine. [alce::758__wikidata_simple__dev::p55]

Cited: alce::758__wikidata_simple__dev::p55

### `599__wikidata_simple__dev`
> Based on the provided sources, the following submarines were classified as Type IXC/40:

U-1235 was a Type IXC/40 U-boat of Nazi Germany's Kriegsmarine during World War II. [alce::599__wikidata_simple__dev::p21]
> U-1230 was a Type IXC/40 U-boat of Nazi Germany's Kriegsmarine during World War II. [alce::599__wikidata_simple__dev::p3]
> U-842 was a Type IXC/40 U-boat built for Nazi Germany's Kriegsmarine during World War II. [alce::599__wikidata_simple__dev::p28]
> U-194 was a Type IXC/40 U-boat of Nazi Germany's Kriegsmarine built during World War II. [alce::599__wikidata_simple__dev::p17]
> Additionally, 87 Type IXC/40 submarines were built in total by DeSchiMAG AG Weser and Seebeckwerft of Bremen, and Deutsche Werft of Hamburg. [alce::599__wikidata_simple__dev::p0]

Cited: alce::599__wikidata_simple__dev::p0, alce::599__wikidata_simple__dev::p17, alce::599__wikidata_simple__dev::p21, alce::599__wikidata_simple__dev::p28, alce::599__wikidata_simple__dev::p3

### `927__wikidata_simple__dev`
> Cedric Bixler-Zavala is part of several bands. He is best known as the lead singer and lyricist of the progressive rock band The Mars Volta. [alce::927__wikidata_simple__dev::p1]
> He is the only constant member of the post-hardcore group At the Drive-In, for which he is the lead singer and occasional guitarist. [alce::927__wikidata_simple__dev::p1]
> He is also the lead singer of the band Antemasque. [alce::927__wikidata_simple__dev::p1]
> Additionally, he sings and plays guitar in his band Zavalaz. [alce::927__wikidata_simple__dev::p1]

Cited: alce::927__wikidata_simple__dev::p1

### `834__wikidata_simple__dev`
> Metro-North Railroad owns a fleet of electric railcars, including M2, M3A, M7A, and M8 models. [alce::834__wikidata_simple__dev::p0]
> Metro-North also owns diesel locomotives and push-pull coaches for use on non-electrified portions of the system. [alce::834__wikidata_simple__dev::p6]

Cited: alce::834__wikidata_simple__dev::p0, alce::834__wikidata_simple__dev::p6

### `815__wikidata_simple__dev`
> Studio 4°C was responsible for producing the OVA series "Detroit Metal City". [alce::815__wikidata_simple__dev::p1]
> Additionally, Studio 4°C contributed animation work to the series "ThunderCats", where they adjusted basic concepts provided by Warner Bros. into Japanese anime design. [alce::815__wikidata_simple__dev::p21]

Cited: alce::815__wikidata_simple__dev::p1, alce::815__wikidata_simple__dev::p21

### `174__wikidata_intersection__dev`
_Refused._

### `487__wikitables_simple__dev`
> A text editor is a type of computer program that edits plain text. [alce::487__wikitables_simple__dev::p0]
> Text editors are programs used for typing, copying, pasting, and printing text, and they do not format lines or pages. [alce::487__wikitables_simple__dev::p19]
> Examples of text editors include Microsoft Notepad and gPHPedit. [alce::487__wikitables_simple__dev::p1]

Cited: alce::487__wikitables_simple__dev::p0, alce::487__wikitables_simple__dev::p1, alce::487__wikitables_simple__dev::p19

### `414__wikidata_comp__dev`
> Based on the provided sources, several entities employ consultants:

Medical device manufacturers employ consultants and contractors when introducing new quality practices and methods, particularly where relevant skills and expertise are not available within the organization. [alce::414__wikidata_comp__dev::p80]
> The NHS (National Health Service) employs locum consultants, who are doctors on fixed, short-term contracts. [alce::414__wikidata_comp__dev::p38]
> Solicitors employ employment consultants to advise courts and tribunals on employment-related issues. [alce::414__wikidata_comp__dev::p0]
> Client companies employ consultants who are external to the client and provide services to that company. [alce::414__wikidata_comp__dev::p3]

Cited: alce::414__wikidata_comp__dev::p0, alce::414__wikidata_comp__dev::p3, alce::414__wikidata_comp__dev::p38, alce::414__wikidata_comp__dev::p80

### `460__wikidata_intersection__dev`
> Bob Cobert composed music for several works directed by Dan Curtis:

He is best known for his work on the TV mini-series "The Winds of War" (1983) and "War and Remembrance" (1988). [alce::460__wikidata_intersection__dev::p1]
> His early work included composing the soap opera "Dark Shadows" and two tie-in films. [alce::460__wikidata_intersection__dev::p1]
> He composed the score for the 1972 TV movie "The Night Stalker" and "The Night Strangler," which became pilots for a TV series. [alce::460__wikidata_intersection__dev::p1]
> He composed the music for the horror film "Burnt Offerings" (1976). [alce::460__wikidata_intersection__dev::p2]
> His other scores for Dan Curtis include the TV movies "The Norliss Tapes" (1973), "Dracula" (1973), "Scream of the Wolf" (1974), "The Turn of the Screw" (1974), "The Great Ice Rip-Off" (1974), "Trilogy of Terror" (1975), "Dead of Night" (1977), "Curse of the Black Widow" (1977), and "Trilogy of Terror II" (1996). [alce::460__wikidata_intersection__dev::p3]

Cited: alce::460__wikidata_intersection__dev::p1, alce::460__wikidata_intersection__dev::p2, alce::460__wikidata_intersection__dev::p3

### `859__wikidata_simple__dev`
_Refused._

### `610__wikidata_simple__dev`
> Key West National Wildlife Refuge contains keys as its primary landform. [alce::610__wikidata_simple__dev::p0]
> Only 2,019 acres of land are above sea level, located on several keys within the refuge. [alce::610__wikidata_simple__dev::p0]

Cited: alce::610__wikidata_simple__dev::p0

### `278__wikidata_comp__dev`
_Refused._

### `743__wikidata_simple__dev`
_Refused._

### `948__wikidata_simple__dev`
_Refused._

### `524__wikitables_simple__dev`
> Fictional diseases are mentioned in multiple art sources:

Literature is a primary source where fictional diseases appear. Diseases, both real and fictional, play a significant role in fiction, with pandemic plagues threatening all human life, such as "The Andromeda Strain", being among the many fictional diseases described in literature and film. [alce::524__wikitables_simple__dev::p0]
> Specific literary works featuring fictional diseases include Michael Crichton's 1969 "The Andromeda Strain", a science fiction thriller about a world-threatening microbe. [alce::524__wikitables_simple__dev::p1]
> Other notable literary examples include Daniel Defoe's 1722 "A Journal of the Plague Year", Mary Shelley's 1826 "The Last Man" which created the genre of "post-apocalyptic pandemic thriller", and Edgar Allan Poe's 1842 "The Masque of the Red Death". [alce::524__wikitables_simple__dev::p3]
> Science fiction is also identified as an art source where fictional diseases are mentioned. [alce::524__wikitables_simple__dev::p4]

Cited: alce::524__wikitables_simple__dev::p0, alce::524__wikitables_simple__dev::p1, alce::524__wikitables_simple__dev::p3, alce::524__wikitables_simple__dev::p4

### `353__wikidata_comp__dev`
> Arnold Leibovit directed a George Pal production. [alce::353__wikidata_comp__dev::p0]
> Specifically, he wrote, directed, and produced "The Fantasy Film Worlds of George Pal," a 1985 documentary film about George Pal. [alce::353__wikidata_comp__dev::p0]

Cited: alce::353__wikidata_comp__dev::p0

### `818__wikidata_simple__dev`
> Glenn T. Seaborg was involved in the synthesis, discovery and investigation of ten transuranium elements. [alce::818__wikidata_simple__dev::p4]
> The chemical element Seaborgium was named after him. [alce::818__wikidata_simple__dev::p22]
> The asteroid 4856 Seaborg was also named after him. [alce::818__wikidata_simple__dev::p22]

Cited: alce::818__wikidata_simple__dev::p22, alce::818__wikidata_simple__dev::p4

### `403__wikidata_intersection__dev`
> Richard Stoehr was employed by both the Curtis Institute of Music and the Juilliard School. [alce::403__wikidata_intersection__dev::p65]
> He was hired by the Curtis Institute of Music in Philadelphia as a music librarian and subsequently to teach courses in theory and composition. [alce::403__wikidata_intersection__dev::p65]
> The sources indicate he was also associated with Juilliard, though the specific employment details at Juilliard are not explicitly stated in the provided passages.

Cited: alce::403__wikidata_intersection__dev::p65

### `387__wikidata_intersection__dev`
> Asuravithu is a movie directed by A. Vincent that had its music composed by G. Devarajan. [alce::387__wikidata_intersection__dev::p65]

Cited: alce::387__wikidata_intersection__dev::p65

### `360__wikidata_intersection__dev`
> Based on the provided sources, there are two individuals who were both graduates from Ananda College and University of Ceylon:

1. L. H. Sumanadasa was educated at Ananda College, Colombo and completed his BSc degree in Physics at Ceylon University College. [alce::360__wikidata_intersection__dev::p69]
> 2. Samaranayake started his primary schooling at Ananda College and went on to do his higher studies at the University of Ceylon, graduating with a BSc in Special Mathematics (First Class Honors) in 1961. [alce::360__wikidata_intersection__dev::p9]
> 3. J. B. Disanayake received secondary education at Ananda College and graduated from the University of Ceylon, Peradeniya campus in 1961. [alce::360__wikidata_intersection__dev::p81]

Cited: alce::360__wikidata_intersection__dev::p69, alce::360__wikidata_intersection__dev::p81, alce::360__wikidata_intersection__dev::p9

### `1012__wikidata_comp__dev`
> Melbourne played in a competition won by Collingwood Football Club. [alce::1012__wikidata_comp__dev::p53]

Cited: alce::1012__wikidata_comp__dev::p53

### `1002__wikidata_comp__dev`
> Based on the provided sources, I can identify headquarters locations for two non-metropolitan Roman Catholic archdioceses:

The Roman Catholic Archdiocese of Strasbourg is a non-metropolitan archdiocese located in France. [alce::1002__wikidata_comp__dev::p72]
> The Roman Catholic Archdiocese of Rhodes is a non-metropolitan archdiocese with its cathedral see at the St. Francis of Assisi Cathedral in Rhodes, Greece. [alce::1002__wikidata_comp__dev::p18]

Cited: alce::1002__wikidata_comp__dev::p18, alce::1002__wikidata_comp__dev::p72

### `234__wikidata_intersection__dev`
_Refused._

### `555__wikidata_simple__dev`
> Based on the provided sources, "Non-Summit" and "Please Take Care of My Refrigerator" are TV shows distributed by JTBC. [alce::555__wikidata_simple__dev::p0]
> These popular JTBC programs are broadcast around the world through the sale of broadcast rights to overseas networks.

Cited: alce::555__wikidata_simple__dev::p0

### `449__wikidata_intersection__dev`
_Refused._

### `893__wikidata_simple__dev`
> "Where the Wild Things Are" is a book featuring Maurice Sendak's artwork. [alce::893__wikidata_simple__dev::p0]
> Additionally, "A Very Special House," written by Ruth Krauss and illustrated by Maurice Sendak, is a 1953 picture book. [alce::893__wikidata_simple__dev::p11]
> Another example is "Mr. Rabbit and the Lovely Present," written by Charlotte Zolotow and illustrated by Maurice Sendak, published in 1962. [alce::893__wikidata_simple__dev::p14]

Cited: alce::893__wikidata_simple__dev::p0, alce::893__wikidata_simple__dev::p11, alce::893__wikidata_simple__dev::p14

### `633__wikidata_simple__dev`
> As of 2007, Tagalog was the first language of 28 million people, or about one-third of the Philippine population, who spoke it as their mother tongue. [alce::633__wikidata_simple__dev::p4]
> Additionally, 22 million people, or 28% of the total Philippine population, speak Tagalog as a native language. [alce::633__wikidata_simple__dev::p6]
> In Toronto specifically, over 70,000 people in the Filipino community listed Tagalog as their mother tongue according to the 2011 census. [alce::633__wikidata_simple__dev::p0]

Cited: alce::633__wikidata_simple__dev::p0, alce::633__wikidata_simple__dev::p4, alce::633__wikidata_simple__dev::p6

### `935__wikidata_simple__dev`
> Pauline Baynes illustrated several notable books. She is probably best known for her covers and interior illustrations for "The Chronicles of Narnia" by C. S. Lewis. [alce::935__wikidata_simple__dev::p2]
> Her illustrations also appeared in "Farmer Giles of Ham," "The Adventures of Tom Bombadil," "Smith of Wootton Major," "Tree and Leaf," and "Bilbo's Last Song" by J. R. R. Tolkien. [alce::935__wikidata_simple__dev::p8]
> Additionally, she illustrated "A Dictionary of Chivalry" (1968), for which she won the Kate Greenaway Medal. [alce::935__wikidata_simple__dev::p3]
> She also illustrated "The Borrowers Avenged" by Mary Norton. [alce::935__wikidata_simple__dev::p3]

Cited: alce::935__wikidata_simple__dev::p2, alce::935__wikidata_simple__dev::p3, alce::935__wikidata_simple__dev::p8

### `253__wikidata_comp__dev`
_Refused._

### `951__wikidata_comp__dev`
_Refused._

### `498__wikitables_simple__dev`
> Some notable mailing list software programs include:

GNU Mailman, LISTSERV, Majordomo, and qmail's ezmlm are modern mailing list management programs that support confirmed opt-in by default. [alce::498__wikitables_simple__dev::p59]
> Hypermail, MHonArc, and FUDforum are popular free software programs for collecting mailing list archives. [alce::498__wikitables_simple__dev::p1]
> LISTSERV is early mailing list software that allows a sender to send one email to the list, which is then transparently sent on to the addresses of the subscribers. [alce::498__wikitables_simple__dev::p7]

Cited: alce::498__wikitables_simple__dev::p1, alce::498__wikitables_simple__dev::p59, alce::498__wikitables_simple__dev::p7

### `374__wikidata_intersection__dev`
> Jack Nicklaus won multiple PGA Championships. He won the 1963 PGA Championship at the Blue Course of Dallas Athletic Club in Dallas, Texas. [alce::374__wikidata_intersection__dev::p2]
> He won the 1971 PGA Championship at PGA National Golf Club in Palm Beach Gardens, Florida. [alce::374__wikidata_intersection__dev::p5]
> He won the 1973 PGA Championship at Canterbury Golf Club in Beachwood, Ohio. [alce::374__wikidata_intersection__dev::p0]
> He won the 1980 PGA Championship at the East Course of Oak Hill Country Club in Rochester, New York. [alce::374__wikidata_intersection__dev::p7]

Cited: alce::374__wikidata_intersection__dev::p0, alce::374__wikidata_intersection__dev::p2, alce::374__wikidata_intersection__dev::p5, alce::374__wikidata_intersection__dev::p7

### `721__wikidata_simple__dev`
> Betfred is partnered with multiple sporting events. In October 2016, Betfred began a three-year period as the main sponsor of Rugby League's Super League, the northern hemisphere's premier Rugby League competition. [alce::721__wikidata_simple__dev::p0]
> In May 2016, Betfred took over sponsorship of the Scottish League Cup for three years, rebranding it the Betfred Cup. [alce::721__wikidata_simple__dev::p2]
> Additionally, Betfred is one of the largest sponsors of horse racing in the United Kingdom, sponsoring races including the Midlands National, the Dante Stakes, the Ebor Handicap, and the Betfred Cesarewitch. [alce::721__wikidata_simple__dev::p1]

Cited: alce::721__wikidata_simple__dev::p0, alce::721__wikidata_simple__dev::p1, alce::721__wikidata_simple__dev::p2

### `377__wikidata_comp__dev`
_Refused._

### `587__wikidata_simple__dev`
_Refused._

### `741__wikidata_simple__dev`
_Refused._

### `707__wikidata_simple__dev`
> Martha Graham choreographed several dances. Two notable examples are "Lamentation," a modern dance solo choreographed to Zoltán Kodály's 1910 "Piano Piece, Op. 3, No. 2," which premiered on January 8, 1930 at Maxine Elliott's Theatre in New York City. [alce::707__wikidata_simple__dev::p33]
> She also choreographed "Columbiad," a solo modern dance set to music by Louis Horst. [alce::707__wikidata_simple__dev::p9]

Cited: alce::707__wikidata_simple__dev::p33, alce::707__wikidata_simple__dev::p9

### `293__wikidata_intersection__dev`
_Refused._

### `773__wikidata_simple__dev`
> "Pride of Baltimore II" calls Baltimore her home port. [alce::773__wikidata_simple__dev::p13]

Cited: alce::773__wikidata_simple__dev::p13

### `212__wikidata_comp__dev`
> Debra Ann Livingston, a United States Circuit Judge of the United States Court of Appeals for the Second Circuit, was educated at Princeton University, where she received a Bachelor of Arts degree from the Woodrow Wilson School of Public and International Affairs in 1980. [alce::212__wikidata_comp__dev::p86]
> She also received a Juris Doctor from Harvard Law School in 1984. [alce::212__wikidata_comp__dev::p86]

Cited: alce::212__wikidata_comp__dev::p86

### `195__wikidata_intersection__dev`
> Michael Schumacher won the United States Grand Prix. [alce::195__wikidata_intersection__dev::p70]

Cited: alce::195__wikidata_intersection__dev::p70

### `283__wikidata_intersection__dev`
> Based on the provided sources, Larry Cohen wrote and directed the TV film "In Broad Daylight" (1971). [alce::283__wikidata_intersection__dev::p84]
> However, I should note that the source indicates Cohen wrote the film, but it was actually directed by Robert Day, not by Cohen himself. [alce::283__wikidata_intersection__dev::p84]
> A work that Larry Cohen both wrote and directed is the "Masters of Horror" TV series episode "Pick Me Up" (2006). [alce::283__wikidata_intersection__dev::p0]

Cited: alce::283__wikidata_intersection__dev::p0, alce::283__wikidata_intersection__dev::p84

### `569__wikidata_simple__dev`
_Refused._

### `675__wikidata_simple__dev`
> Based on the provided sources, victims of bomb attacks included:

Six adults were killed in one bombing attack, with a granite memorial fountain dedicated in 1995 honoring these victims. [alce::675__wikidata_simple__dev::p15]
> Muslim victims were killed in blasts, with 12 casualties caused by the blast near the RS Puram police station, the most powerful amongst the bombings. [alce::675__wikidata_simple__dev::p0]
> The victims of another bombing included people of many backgrounds and ages: Protestants, Catholics, six teenagers, six children, a mother pregnant with twins, two Spanish tourists, and others on a day trip from the Republic of Ireland. [alce::675__wikidata_simple__dev::p3]
> Six women and three men were murdered in another attack, with seven dying immediately and two dying of their wounds in the following weeks. [alce::675__wikidata_simple__dev::p1]
> Victims of a bombing ranged from 20 to 60 years old with an average age of 34, including 32 British nationals and one victim each from Afghanistan, France, Ghana, Grenada, India, Iran, Israel, Italy, Kenya, Mauritius, New Zealand, Nigeria, Romania, Sri Lanka, and Turkey, among others. [alce::675__wikidata_simple__dev::p2]

Cited: alce::675__wikidata_simple__dev::p0, alce::675__wikidata_simple__dev::p1, alce::675__wikidata_simple__dev::p15, alce::675__wikidata_simple__dev::p2, alce::675__wikidata_simple__dev::p3

### `1351__wikidata_simple__dev`
> David E. Kelley was the executive producer for "Harry's Law". [alce::1351__wikidata_simple__dev::p10]

Cited: alce::1351__wikidata_simple__dev::p10

### `14__wikitables_composition__dev`
> There are eleven Welsh principal areas that are styled as county boroughs. [alce::14__wikitables_composition__dev::p38]
> One example of a Welsh county borough is Merthyr Tydfil County Borough. [alce::14__wikitables_composition__dev::p83]

Cited: alce::14__wikitables_composition__dev::p38, alce::14__wikitables_composition__dev::p83

### `461__wikidata_intersection__dev`
> James R. Webb served as screenwriter for "Nevada City" (1941) directed by Joseph Kane. [alce::461__wikidata_intersection__dev::p0]

Cited: alce::461__wikidata_intersection__dev::p0

### `903__wikidata_simple__dev`
> R. Scott Dunbar discovered comets and minor planets. [alce::903__wikidata_simple__dev::p1]
> His most notable discoveries include the potentially hazardous object and Aten asteroid 3362 Khufu, which he co-discovered with Maria A. Barucci, as well as the near-Earth object, Mars-crosser and Aten asteroid 3551 Verenia. [alce::903__wikidata_simple__dev::p1]
> Together with Eleanor Helin, he co-discovered the minor planets 3360 Syrinx, 6065 Chesneau, 6435 Daveross, and 7163 Barenboim. [alce::903__wikidata_simple__dev::p1]
> The Minor Planet Center credits him with the co-discovery of 10 numbered minor planets during 1981–1987. [alce::903__wikidata_simple__dev::p1]

Cited: alce::903__wikidata_simple__dev::p1

### `325__wikidata_intersection__dev`
> Based on the provided sources, several movies were scored by Vijaya Bhaskar and directed by Puttanna Kanagal. These include "Belli Moda" [alce::325__wikidata_intersection__dev::p10]
> , "Gejje Pooje" [alce::325__wikidata_intersection__dev::p10]
> , and "Naagarahaavu" [alce::325__wikidata_intersection__dev::p10]
> . Additionally, "Maanasa Sarovara" was scored by Bhaskar for Kanagal [alce::325__wikidata_intersection__dev::p10]
> .

Cited: alce::325__wikidata_intersection__dev::p10

### `58__wikitables_composition__dev`
_Refused._

### `916__wikidata_simple__dev`
_Refused._

### `919__wikidata_simple__dev`
> Saipa manufactured trucks and trailers. [alce::919__wikidata_simple__dev::p0]
> Saipa also manufactured licensed versions of the Renault 5 and Renault 21. [alce::919__wikidata_simple__dev::p1]
> Additionally, Saipa manufactured the Citroën C5 and the Renault Tondar 90. [alce::919__wikidata_simple__dev::p8]

Cited: alce::919__wikidata_simple__dev::p0, alce::919__wikidata_simple__dev::p1, alce::919__wikidata_simple__dev::p8

### `723__wikidata_simple__dev`
> Based on the provided sources, I can identify the following choral symphonies:

1. Beethoven's Ninth Symphony is a direct antecedent for the choral symphony form. [alce::723__wikidata_simple__dev::p0]
> 2. Hector Berlioz's "Roméo et Juliette" was described by Berlioz himself as a choral symphony. [alce::723__wikidata_simple__dev::p0]
> 3. Gustav Holst's Choral Symphony is a work for soprano soloist, chorus, and orchestra in a setting of verses by John Keats, written in 1923–24. [alce::723__wikidata_simple__dev::p3]
> 4. George Dyson's Psalm CVII Symphony and Overture is a choral symphony written in 1910. [alce::723__wikidata_simple__dev::p18]
> The sources also mention that composers including Philip Glass, Hans Werner Henze, Krzysztof Penderecki, William Bolcom and Robert Strassburg have written choral symphonies, though specific works are not named. [alce::723__wikidata_simple__dev::p11]

Cited: alce::723__wikidata_simple__dev::p0, alce::723__wikidata_simple__dev::p11, alce::723__wikidata_simple__dev::p18, alce::723__wikidata_simple__dev::p3

### `628__wikidata_simple__dev`
> The inhabitants of Guam are called Guamanians, and they are American citizens by birth. [alce::628__wikidata_simple__dev::p1]
> Those born on Guam are U.S. citizens at birth on the same terms as persons born in other parts of the United States, as established by the Immigration and Nationality Act of 1952. [alce::628__wikidata_simple__dev::p15]

Cited: alce::628__wikidata_simple__dev::p1, alce::628__wikidata_simple__dev::p15

### `379__wikidata_intersection__dev`
_Refused._

### `654__wikidata_simple__dev`
> Based on the provided sources, Joan Daemen designed the following objects:

The Rijndael cipher, which was co-designed with Vincent Rijmen and selected as the Advanced Encryption Standard (AES) in 2001. [alce::654__wikidata_simple__dev::p1]
> The Keccak cryptographic hash, which was co-designed and selected as the new SHA-3 hash by NIST in October 2012. [alce::654__wikidata_simple__dev::p1]

Cited: alce::654__wikidata_simple__dev::p1

### `714__wikidata_simple__dev`
> John Cyril Porte created several aircraft, including the Felixstowe F5L, a twin-engine flying boat developed during the First World War. [alce::714__wikidata_simple__dev::p69]
> He also designed the Felixstowe F.4 Fury, a large British five-engined triplane flying-boat. [alce::714__wikidata_simple__dev::p60]
> Additionally, Porte designed the Felixstowe Porte Baby, a British reconnaissance flying boat that first flew in 1915. [alce::714__wikidata_simple__dev::p38]

Cited: alce::714__wikidata_simple__dev::p38, alce::714__wikidata_simple__dev::p60, alce::714__wikidata_simple__dev::p69

### `338__wikidata_intersection__dev`
_Refused._

### `1352__wikidata_simple__dev`
> Bridge House Estates maintains the five City Bridges. [alce::1352__wikidata_simple__dev::p0]
> It was originally established to maintain London Bridge and, subsequently, other bridges. [alce::1352__wikidata_simple__dev::p1]

Cited: alce::1352__wikidata_simple__dev::p0, alce::1352__wikidata_simple__dev::p1

### `196__wikidata_intersection__dev`
> Ethan Coen produced "The Man Who Wasn't There" (2001), which was directed by Joel Coen. [alce::196__wikidata_intersection__dev::p27]

Cited: alce::196__wikidata_intersection__dev::p27

### `289__wikidata_comp__dev`
_Refused._

### `1000__wikidata_comp__dev`
> Multiple winners of the Tyson Holly Farms 400 are mentioned in the sources:

Jeff Gordon won the 1996 Tyson Holly Farms 400. [alce::1000__wikidata_comp__dev::p2]
> Geoff Bodine won the Tyson Holly Farms 400 in 1994 by one lap over Terry Labonte.
> Mark Martin won the Tyson Holly Farms 400 in another year, picking up his second win at the track. [alce::1000__wikidata_comp__dev::p8]

Cited: alce::1000__wikidata_comp__dev::p2, alce::1000__wikidata_comp__dev::p8

### `965__wikidata_comp__dev`
> Based on the provided sources, persons who held the position Dean of Norwich were educated at various institutions:

John Paul Burbridge, Dean of Norwich (1983-1995), was educated at The King's School, Canterbury, King's College Cambridge, New College Oxford, and Wells Theological College. [alce::965__wikidata_comp__dev::p2]
> George Pellew, Dean of Norwich, was educated at Eton College and Trinity College, Cambridge. [alce::965__wikidata_comp__dev::p9]
> Jane Hedges, Dean of Norwich (installed 2014), completed a General Arts degree at Durham University and trained for ministry at Cranmer Hall, Durham. [alce::965__wikidata_comp__dev::p20]

Cited: alce::965__wikidata_comp__dev::p2, alce::965__wikidata_comp__dev::p20, alce::965__wikidata_comp__dev::p9

### `333__wikidata_intersection__dev`
> Several films were directed and produced by Christopher Nolan:

"The Prestige" (2006) was directed, co-written, and produced by Christopher Nolan. [alce::333__wikidata_intersection__dev::p1]
> "Interstellar" (2014) was directed, written, and produced by Christopher Nolan. [alce::333__wikidata_intersection__dev::p15]
> "The Dark Knight" (2008) was directed, co-produced, and co-written by Christopher Nolan. [alce::333__wikidata_intersection__dev::p53]

Cited: alce::333__wikidata_intersection__dev::p1, alce::333__wikidata_intersection__dev::p15, alce::333__wikidata_intersection__dev::p53

### `281__wikidata_intersection__dev`
> Jackson graduated from Stuyvesant High School and Brooklyn Law School. [alce::281__wikidata_intersection__dev::p93]

Cited: alce::281__wikidata_intersection__dev::p93

### `539__wikitables_simple__dev`
> Here are some notable diamonds:

The Golden Jubilee Diamond is the largest cut and faceted diamond in the world, weighing 545.67 carats. [alce::539__wikitables_simple__dev::p77]
> The Great Chrysanthemum is considered one of the most famous diamonds in the world and is the 2nd largest pear-shaped brown diamond, weighing 198 carats and discovered in 1963 at the Kimberley Mines in South Africa. [alce::539__wikitables_simple__dev::p7]
> Cullinan I, also known as the Great Star of Africa, held the title of the largest cut and faceted diamond from 1908 until the discovery of the Golden Jubilee Diamond. [alce::539__wikitables_simple__dev::p77]
> The top four pink diamonds of the world are from Golconda, and several famous diamonds from this region are kept by monarchs and legendary personalities as marks of pride. [alce::539__wikitables_simple__dev::p37]

Cited: alce::539__wikitables_simple__dev::p37, alce::539__wikitables_simple__dev::p7, alce::539__wikitables_simple__dev::p77

### `52__wikitables_composition__dev`
> KXLG (99.1 FM) is a radio station serving the Watertown, South Dakota area. [alce::52__wikitables_composition__dev::p3]

Cited: alce::52__wikitables_composition__dev::p3

### `80__wikitables_composition__dev`
> Based on the provided sources, the following Russian cities and towns are located in Komi Republic:

Syktyvkar is the capital city of the Komi Republic, Russia. [alce::80__wikitables_composition__dev::p10]
> Usinsk is a town in the Komi Republic, Russia, located east of the republic's capital city of Syktyvkar. [alce::80__wikitables_composition__dev::p13]
> Sosnogorsk is a town in the Komi Republic, Russia, located on the Izhma River. [alce::80__wikitables_composition__dev::p52]

Cited: alce::80__wikitables_composition__dev::p10, alce::80__wikitables_composition__dev::p13, alce::80__wikitables_composition__dev::p52

### `310__wikidata_intersection__dev`
> Based on the provided sources, I can identify the following competitions that both Liverpool F.C. and West Ham United F.C. participated in:

The UEFA Cup. [alce::310__wikidata_intersection__dev::p0]
> The sources confirm that West Ham United "competed in the UEFA Cup" [alce::310__wikidata_intersection__dev::p0]
> , and the first source indicates that Liverpool qualified for the UEFA Cup in the 2005-06 season [alce::310__wikidata_intersection__dev::p42]
> , establishing that both clubs participated in this competition.

Cited: alce::310__wikidata_intersection__dev::p0, alce::310__wikidata_intersection__dev::p42

### `657__wikidata_simple__dev`
> Several geographic features can be found in or around Runde:

Cliffs are present on the island, where most of the seabirds are found. [alce::657__wikidata_simple__dev::p2]
> Runde lies on the west coast of Norway. [alce::657__wikidata_simple__dev::p3]
> The region is famous for its long fjords and steep, snow-clad mountains. [alce::657__wikidata_simple__dev::p4]
> A mountain plateau is located on Runde, with blanket bog dominating the northwestern part of it. [alce::657__wikidata_simple__dev::p5]

Cited: alce::657__wikidata_simple__dev::p2, alce::657__wikidata_simple__dev::p3, alce::657__wikidata_simple__dev::p4, alce::657__wikidata_simple__dev::p5

### `429__wikidata_intersection__dev`
> The Central Branch is a transportation branch owned and operated by the Long Island Rail Road. [alce::429__wikidata_intersection__dev::p66]

Cited: alce::429__wikidata_intersection__dev::p66

### `508__wikitables_simple__dev`
> The Deep Field is the fourth album by Joan as Police Woman, released January 24, 2011. [alce::508__wikitables_simple__dev::p0]
> The Deep Lens Survey (DLS) is an ultra-deep multi-band optical survey of seven 4 square degree fields. [alce::508__wikitables_simple__dev::p16]
> Deepfield was an American post-grunge band from Charleston, South Carolina. [alce::508__wikitables_simple__dev::p10]

Cited: alce::508__wikitables_simple__dev::p0, alce::508__wikitables_simple__dev::p10, alce::508__wikitables_simple__dev::p16

### `936__wikidata_simple__dev`
> Several fictional characters had their debut appearance in Star Wars: Episode V – The Empire Strikes Back:

Admiral Firmus Piett is a fictional character from the "Star Wars" franchise, first introduced in the 1980 film "The Empire Strikes Back". [alce::936__wikidata_simple__dev::p14]
> Boba Fett is a fictional character and bounty hunter in the "Star Wars" franchise who appears in "Episode V: The Empire Strikes Back" (1980). [alce::936__wikidata_simple__dev::p27]
> Lando Calrissian first appears in "The Empire Strikes Back" (1980) as the administrator of Cloud City. [alce::936__wikidata_simple__dev::p24]

Cited: alce::936__wikidata_simple__dev::p14, alce::936__wikidata_simple__dev::p24, alce::936__wikidata_simple__dev::p27

### `362__wikidata_comp__dev`
> JASON is a scientific advisory group whose activities are administratively run through the MITRE Corporation, a non-profit corporation that operates Federally Funded Research and Development Centers for the Federal Government of the United States. [alce::362__wikidata_comp__dev::p1]
> JASON's sponsors include the Department of Defense, the Department of Energy, and the U.S. Intelligence Community. [alce::362__wikidata_comp__dev::p1]

Cited: alce::362__wikidata_comp__dev::p1

### `784__wikidata_simple__dev`
> Based on the provided sources, Loyola Law School alumni are individuals who have graduated from Loyola Law School, which is the law school of Loyola Marymount University in Los Angeles, California. [alce::784__wikidata_simple__dev::p6]
> Examples of notable Loyola Law School alumni include Barbara Broccoli, a producer of James Bond films since 1990; James Wong, creator of "American Horror Story"; Brian Helgeland, writer/director of the Jackie Robinson biopic "42"; Francis Lawrence, director of 3 of "The Hunger Games" films; and David Mirkin, an executive producer and showrunner for "The Simpsons". [alce::784__wikidata_simple__dev::p38]
> Additionally, Bernard Beazley is identified as a 1950 Loyola Law graduate who became the former general counsel and senior vice president of Dentsply International. [alce::784__wikidata_simple__dev::p23]

Cited: alce::784__wikidata_simple__dev::p23, alce::784__wikidata_simple__dev::p38, alce::784__wikidata_simple__dev::p6

### `231__wikidata_comp__dev`
> Lee Enterprises is based in Davenport, Iowa. [alce::231__wikidata_comp__dev::p0]

Cited: alce::231__wikidata_comp__dev::p0

### `247__wikidata_intersection__dev`
> The LA Dodgers and Philadelphia Phillies participated together in multiple National League Championship Series (NLCS) competitions. [alce::247__wikidata_intersection__dev::p0]
> Specifically, they met in the 1983 National League Championship Series, which was a best-of-five matchup between the West Division champion Los Angeles Dodgers and the East Division champion Philadelphia Phillies. [alce::247__wikidata_intersection__dev::p8]
> They also competed in the 2009 National League Championship Series, which was a best-of-seven baseball game series pitting the Los Angeles Dodgers against the Philadelphia Phillies for the National League Championship. [alce::247__wikidata_intersection__dev::p2]

Cited: alce::247__wikidata_intersection__dev::p0, alce::247__wikidata_intersection__dev::p2, alce::247__wikidata_intersection__dev::p8

### `644__wikidata_simple__dev`
> The Gulf of Boothia is surrounded by several land masses. Clockwise around the gulf, you will find Baffin Island, the Melville Peninsula, the Canadian mainland, and the Boothia Peninsula. [alce::644__wikidata_simple__dev::p0]
> Additionally, the Simpson Peninsula is located northwest of Committee Bay at the south end of the gulf. [alce::644__wikidata_simple__dev::p0]

Cited: alce::644__wikidata_simple__dev::p0

### `71__wikitables_composition__dev`
> There are multiple Michigan radio stations with licenses in Saginaw. The sources identify the following call signs:

WGER is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p33]
> WKCQ is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p2]
> WSAM is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p1]
> WTLZ is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p9]
> If you are looking for a specific station, please provide additional details to narrow down which call sign you are asking about.

Cited: alce::71__wikitables_composition__dev::p1, alce::71__wikitables_composition__dev::p2, alce::71__wikitables_composition__dev::p33, alce::71__wikitables_composition__dev::p9

### `492__wikitables_simple__dev`
> Based on the provided sources, I can identify the following bridges with a deck height of at least 200 meters:

The Ingeniero Carlos Fernández Casado Bridge has a total height of 220 meters. [alce::492__wikitables_simple__dev::p19]
> However, I should note that the sources mention several other bridges with very high deck heights, but the specific deck height measurements are not fully provided in the text. The Royal Gorge Bridge, Liuguanghe Bridge, and Beipan River Guanxing Highway Bridge are referenced as having exceptionally high deck heights that would likely exceed 200 meters, but the exact measurements are indicated as missing or incomplete in the source material. [alce::492__wikitables_simple__dev::p49]

Cited: alce::492__wikitables_simple__dev::p19, alce::492__wikitables_simple__dev::p49

### `562__wikidata_simple__dev`
> Several people are from the Mataram Sultanate:

Kyai Gedhe Pamanahan became the ruler of the Mataram area in the 1570s and was often referred to as Kyai Gedhe Mataram after his ascension. [alce::562__wikidata_simple__dev::p4]
> Panembahan Senapati Ingalaga, Pamanahan's son, replaced his father on the throne around 1584 and is also known as Senopati Sutawijaya, the founder of the Mataram Sultanate. [alce::562__wikidata_simple__dev::p4]
> Sultan Agung Hanyokrokusumo was a powerful ruler who brought the Mataram Sultanate to its peak of power before his death in 1645. [alce::562__wikidata_simple__dev::p2]
> Amangkurat I was the sultan of Mataram from 1646 to 1677 and was the son of Sultan Agung. [alce::562__wikidata_simple__dev::p16]

Cited: alce::562__wikidata_simple__dev::p16, alce::562__wikidata_simple__dev::p2, alce::562__wikidata_simple__dev::p4

### `979__wikidata_comp__dev`
_Refused._

### `636__wikidata_simple__dev`
> Vietnam Airlines operated the following services:

Vietnam Airlines flew to 64 destinations in 17 countries, excluding codeshared services. [alce::636__wikidata_simple__dev::p2]
> The airline operated approximately 70 aircraft, serving 46 destinations from its hubs at Noi Bai and Tan Son Nhat International Airports. [alce::636__wikidata_simple__dev::p4]
> Vietnam Airlines earned revenue from airline catering and the maintenance and overhauling of aircraft through subsidiaries including Vietnam Airlines Engineering Company and Vietnam Airlines Caterers. [alce::636__wikidata_simple__dev::p0]
> The company controlled and operated a cargo division called Vietnam Airlines Cargo. [alce::636__wikidata_simple__dev::p0]
> Vietnam Airlines had diversified its investments in the aircraft-leasing and airport ground-servicing industries. [alce::636__wikidata_simple__dev::p0]

Cited: alce::636__wikidata_simple__dev::p0, alce::636__wikidata_simple__dev::p2, alce::636__wikidata_simple__dev::p4

### `39__wikitables_composition__dev`
> Sandviken is a city located in Sandviken Municipality in Sweden. [alce::39__wikitables_composition__dev::p2]

Cited: alce::39__wikitables_composition__dev::p2

### `226__wikidata_comp__dev`
> Fitzroy Football Club was the first club to win a VFL Grand Final. [alce::226__wikidata_comp__dev::p4]
> The club also achieved a total of eight VFL premierships between 1898 and 1944. [alce::226__wikidata_comp__dev::p4]

Cited: alce::226__wikidata_comp__dev::p4

### `757__wikidata_simple__dev`
> Several people have been coaches for the LA Galaxy:

Sigi Schmid was a head coach of the Los Angeles Galaxy. [alce::757__wikidata_simple__dev::p33]
> Dominic Kinnear is currently serving as the head coach of LA Galaxy. [alce::757__wikidata_simple__dev::p3]
> Curt Onalfo most recently served as the head coach of the LA Galaxy. [alce::757__wikidata_simple__dev::p11]

Cited: alce::757__wikidata_simple__dev::p11, alce::757__wikidata_simple__dev::p3, alce::757__wikidata_simple__dev::p33

### `618__wikidata_simple__dev`
_Refused._

### `418__wikidata_intersection__dev`
> Michael Schumacher won the Monaco Grand Prix on multiple occasions. He won the 1994 Monaco Grand Prix. [alce::418__wikidata_intersection__dev::p22]
> He also won the 1997 Monaco Grand Prix driving for Ferrari. [alce::418__wikidata_intersection__dev::p4]
> Additionally, he won the 1999 Monaco Grand Prix for Ferrari. [alce::418__wikidata_intersection__dev::p1]
> He further won the 2001 Monaco Grand Prix driving for the Ferrari team. [alce::418__wikidata_intersection__dev::p0]

Cited: alce::418__wikidata_intersection__dev::p0, alce::418__wikidata_intersection__dev::p1, alce::418__wikidata_intersection__dev::p22, alce::418__wikidata_intersection__dev::p4

### `56__wikitables_composition__dev`
> Several English recipients of the Victoria Cross received the award after 1918:

Thomas James Harris VC MM was an English recipient of the Victoria Cross. [alce::56__wikitables_composition__dev::p32]
> James Pitts VC MSM was an English recipient of the Victoria Cross. [alce::56__wikitables_composition__dev::p58]
> However, I should note that the sources provided primarily document recipients from 1918 or earlier.
> Ernest Frederick Beal died on 22 March 1918, Thomas James Harris died on 9 August 1918, and Eric Stuart Dougall died on 14 April 1918.
> James Pitts lived until 1955, but the source indicates his Victoria Cross was awarded for actions during the Second Boer War, not after 1918.
> The sources do not clearly identify English Victoria Cross recipients whose awards were specifically granted after 1918.

Cited: alce::56__wikitables_composition__dev::p32, alce::56__wikitables_composition__dev::p58

### `767__wikidata_simple__dev`
> Jules Engel taught several generations of animators at the California Institute of the Arts, where he was the founding director of the Experimental Animation Program. [alce::767__wikidata_simple__dev::p0]
> His notable students included John Lasseter, Henry Selick, Tim Burton, and Stephen Hillenburg. [alce::767__wikidata_simple__dev::p7]

Cited: alce::767__wikidata_simple__dev::p0, alce::767__wikidata_simple__dev::p7

### `594__wikidata_simple__dev`
_Refused._

### `648__wikidata_simple__dev`
_Refused._

### `4__wikitables_composition__dev`
> The Greensboro Historical Museum is a Greensboro, North Carolina-based museum. [alce::4__wikitables_composition__dev::p0]
> It consists of the former First Presbyterian Church of Greensboro and Smith Memorial Building, located at 130 Summit Ave. in Greensboro, Guilford County, North Carolina. [alce::4__wikitables_composition__dev::p0]
> Additionally, the Greensboro Science Center is another Greensboro, North Carolina-based museum, established in 1957 as a science museum and zoological park. [alce::4__wikitables_composition__dev::p2]
> The International Civil Rights Center & Museum is also located in Greensboro, North Carolina. [alce::4__wikitables_composition__dev::p60]

Cited: alce::4__wikitables_composition__dev::p0, alce::4__wikitables_composition__dev::p2, alce::4__wikitables_composition__dev::p60

### `875__wikidata_simple__dev`
> The Royal College of Nursing publishes several pieces of literature. RCN Publishing (branded as RCNi since March 2015) produces "RCN Bulletin", a monthly member publication, and "Nursing Standard", which is available through subscription and on news stands. [alce::875__wikidata_simple__dev::p28]
> It also publishes a range of journals for specialist nurses including "Cancer Nursing Practice", "Emergency Nurse", "Learning Disability Practice", "Mental Health Practice", "Nursing Children and Young People", "Nursing Management", "Nursing Older People", "Nurse Researcher", and "Primary Health Care". [alce::875__wikidata_simple__dev::p28]

Cited: alce::875__wikidata_simple__dev::p28

### `826__wikidata_simple__dev`
> Red Chillies Entertainment produced "Main Hoon Na," which was Farah Khan's directorial debut. [alce::826__wikidata_simple__dev::p43]
> The company also produced or co-produced "Om Shanti Om" (2007) and "Happy New Year" (2014). [alce::826__wikidata_simple__dev::p43]
> Additionally, Red Chillies Entertainment produced "Ra.One" (2011). [alce::826__wikidata_simple__dev::p3]

Cited: alce::826__wikidata_simple__dev::p3, alce::826__wikidata_simple__dev::p43

### `868__wikidata_simple__dev`
> Eskay Movies produced numerous films. Their first feature film was "Chore Chore Mastuto Bhai" released in 2005. [alce::868__wikidata_simple__dev::p2]
> From 2008 onwards, they released films annually including "Bhalobasa Bhalobasa," "Dujone," and "Jamai Raja." [alce::868__wikidata_simple__dev::p2]
> In 2010, they released "Kohono Biday Bolo Na" and "Wanted." [alce::868__wikidata_simple__dev::p2]
> In 2014, they co-produced "Ami Shudhu Cheyechi Tomay." [alce::868__wikidata_simple__dev::p3]
> In 2015, they co-produced "Romeo vs Juliet," "Agnee 2," and "Aashiqui: True Love" with Jaaz Multimedia. [alce::868__wikidata_simple__dev::p3]
> In 2016, they released seven films: "Angaar," "Hero 420," "Niyoti," "Badsha – The Don," "Shikari," "Prem Ki Bujhini," and "Rokto." [alce::868__wikidata_simple__dev::p4]

Cited: alce::868__wikidata_simple__dev::p2, alce::868__wikidata_simple__dev::p3, alce::868__wikidata_simple__dev::p4

### `191__wikidata_comp__dev`
_Refused._

### `769__wikidata_simple__dev`
_Refused._

### `855__wikidata_simple__dev`
> Samuel R. Delany edited "Nebula Winners Thirteen," an anthology of science fiction short works. [alce::855__wikidata_simple__dev::p35]
> It was first published in hardcover by Harper & Row in February 1980, with a paperback edition following from Bantam Books in August 1981. [alce::855__wikidata_simple__dev::p35]

Cited: alce::855__wikidata_simple__dev::p35

### `593__wikidata_simple__dev`
_Refused._

### `73__wikitables_composition__dev`
> Lillico is a Tasmanian locality found in the Devonport local government area. [alce::73__wikitables_composition__dev::p1]

Cited: alce::73__wikitables_composition__dev::p1

### `846__wikidata_simple__dev`
> Lincoln Motors makes the Lincoln Continental and the Lincoln Town Car.

The Lincoln Continental is a series of mid-sized and full-sized luxury cars produced by Lincoln, a division of the American automaker Ford Motor Company. [alce::846__wikidata_simple__dev::p24]
> The Lincoln Town Car is a model line of full-size luxury sedans that was marketed by the Lincoln division of the American automaker Ford Motor Company from 1980 to 2011. [alce::846__wikidata_simple__dev::p63]

Cited: alce::846__wikidata_simple__dev::p24, alce::846__wikidata_simple__dev::p63

### `1252__wikitables_composition__dev`
> Based on the provided sources, here are cities and municipalities located in Tarlac province:

Tarlac City is the provincial capital and the one city in Tarlac province. [alce::1252__wikitables_composition__dev::p1]
> Pura is a municipality in the province of Tarlac. [alce::1252__wikitables_composition__dev::p20]
> Camiling is a first-class urban municipality of the province of Tarlac. [alce::1252__wikitables_composition__dev::p31]
> Victoria is a municipality in the province of Tarlac. [alce::1252__wikitables_composition__dev::p8]

Cited: alce::1252__wikitables_composition__dev::p1, alce::1252__wikitables_composition__dev::p20, alce::1252__wikitables_composition__dev::p31, alce::1252__wikitables_composition__dev::p8

### `494__wikitables_simple__dev`
_Refused._

### `205__wikidata_comp__dev`
_Refused._

### `632__wikidata_simple__dev`
> Eidgenoessische Konstruktionswerkstaette manufactured artillery, vehicles, and other typical military equipment. [alce::632__wikidata_simple__dev::p0]
> It also produced the DH-1 aircraft starting in 1914. [alce::632__wikidata_simple__dev::p0]
> After its aviation department became a separate unit in 1943, the company focused on producing armoured fighting vehicles for the Swiss Army, including both its own designs and licensed production of M113 armored personnel carriers and Leopard 2 tanks and other land systems. [alce::632__wikidata_simple__dev::p1]

Cited: alce::632__wikidata_simple__dev::p0, alce::632__wikidata_simple__dev::p1

### `865__wikidata_simple__dev`
> Relativity Media distributed "The Warrior's Way," which was directed by Sngmoo Lee and starred Jang Dong-gun, Geoffrey Rush, and Kate Bosworth. [alce::865__wikidata_simple__dev::p2]

Cited: alce::865__wikidata_simple__dev::p2

### `690__wikidata_simple__dev`
> Based on the provided sources, I can identify the following Via Rail-owned stations:

The station in Amherst is owned and operated by Via Rail. [alce::690__wikidata_simple__dev::p2]
> Additionally, a station (identified in the first source but not named) was acquired by Via Rail in 1986. [alce::690__wikidata_simple__dev::p13]
> Via Rail also operates out of Union Station in Winnipeg. [alce::690__wikidata_simple__dev::p56]

Cited: alce::690__wikidata_simple__dev::p13, alce::690__wikidata_simple__dev::p2, alce::690__wikidata_simple__dev::p56

### `704__wikidata_simple__dev`
> Several counties are next to Lake Okeechobee. Glades County is one of five counties surrounding Lake Okeechobee. [alce::704__wikidata_simple__dev::p9]
> Okeechobee County borders Lake Okeechobee. [alce::704__wikidata_simple__dev::p92]
> Additionally, Hendry County and Martin County are adjacent to Lake Okeechobee, as about three-quarters of the lake was divided among Glades, Hendry, Martin, and Okeechobee counties in 1963. [alce::704__wikidata_simple__dev::p11]

Cited: alce::704__wikidata_simple__dev::p11, alce::704__wikidata_simple__dev::p9, alce::704__wikidata_simple__dev::p92

### `456__wikidata_intersection__dev`
> "Vellanakalude Nadu" is a film that Priyadarshan directed and that was penned by Sreenivasan. [alce::456__wikidata_intersection__dev::p2]

Cited: alce::456__wikidata_intersection__dev::p2

### `929__wikidata_simple__dev`
> The Sunbeam Rapier is the automobile most associated with the Sunbeam brand. [alce::929__wikidata_simple__dev::p35]
> It was an automobile produced by Rootes Group from 1955 to 1976 in two different body-styles. [alce::929__wikidata_simple__dev::p70]

Cited: alce::929__wikidata_simple__dev::p35, alce::929__wikidata_simple__dev::p70

### `13__wikitables_composition__dev`
> Based on the provided sources, the following fashion periodicals were launched after 1996:

Lucire originally began on the web in 1997. [alce::13__wikitables_composition__dev::p9]
> MODE launched in February 1997. [alce::13__wikitables_composition__dev::p22]
> SLiNK, a fashion and lifestyle magazine for full-figured women, was launched in 2011. [alce::13__wikitables_composition__dev::p4]

Cited: alce::13__wikitables_composition__dev::p22, alce::13__wikitables_composition__dev::p4, alce::13__wikitables_composition__dev::p9

### `713__wikidata_simple__dev`
> The Omphalos of Delphi is an ancient marble monument that was found at the archaeological site of Delphi, Greece. [alce::713__wikidata_simple__dev::p3]
> Additionally, a stele of the Labyadai, which was inscribed on all four sides, was discovered at Delphi in 1893. [alce::713__wikidata_simple__dev::p69]

Cited: alce::713__wikidata_simple__dev::p3, alce::713__wikidata_simple__dev::p69

### `519__wikitables_simple__dev`
> Based on the provided sources, the following are popcorn brands:

Butterkist is the United Kingdom's best-selling brand of popcorn. [alce::519__wikitables_simple__dev::p13]
> Orville Redenbacher's Gourmet Popping Corn is a brand of popcorn made originally by Chester Inc. [alce::519__wikitables_simple__dev::p0]
> Popcorn, Indiana is a brand of popcorn in North America founded in 2002. [alce::519__wikitables_simple__dev::p5]
> Specialised popcorn pots have been marketed under various brand names, including The Detonator, Whirley Pop, Theater II and Sweet & Easy. [alce::519__wikitables_simple__dev::p71]

Cited: alce::519__wikitables_simple__dev::p0, alce::519__wikitables_simple__dev::p13, alce::519__wikitables_simple__dev::p5, alce::519__wikitables_simple__dev::p71

### `914__wikidata_simple__dev`
> Doug Scott was one of the climbers in the 1975 British Mt. Everest Southwest Face expedition. [alce::914__wikidata_simple__dev::p49]
> He reached the summit on 24 September 1975 along with Dougal Haston. [alce::914__wikidata_simple__dev::p7]

Cited: alce::914__wikidata_simple__dev::p49, alce::914__wikidata_simple__dev::p7

### `749__wikidata_simple__dev`
> Based on the provided sources, several operations were under EDF Energy:

EDF Energy operated electricity generation and the sale of gas and electricity to homes and businesses throughout the United Kingdom. [alce::749__wikidata_simple__dev::p0]
> EDF Energy was formed in 2002 following the acquisition and mergers of SEEBOARD Plc (formerly the South Eastern Electricity Board), London Electricity Plc (formerly the London Electricity Board or LEB), and SWEB Energy Plc (formerly the South Western Electricity Board). [alce::749__wikidata_simple__dev::p0]
> British Energy was rebranded to EDF Energy in July 2010, after being purchased by EDF Energy. [alce::749__wikidata_simple__dev::p26]

Cited: alce::749__wikidata_simple__dev::p0, alce::749__wikidata_simple__dev::p26

### `586__wikidata_simple__dev`
_Refused._

### `798__wikidata_simple__dev`
_Refused._

### `162__wikidata_intersection__dev`
> John Milius authored and directed several films. He wrote and directed "The Wind and the Lion" (1975). [alce::162__wikidata_intersection__dev::p7]
> He also wrote and directed "Dillinger" (1973). [alce::162__wikidata_intersection__dev::p1]
> Additionally, he wrote and directed "Conan the Barbarian" and "Red Dawn." [alce::162__wikidata_intersection__dev::p4]

Cited: alce::162__wikidata_intersection__dev::p1, alce::162__wikidata_intersection__dev::p4, alce::162__wikidata_intersection__dev::p7

### `184__wikidata_comp__dev`
> Belle of the Nineties (1934) is Mae West's fourth motion picture, directed by Leo McCarey. [alce::184__wikidata_comp__dev::p19]

Cited: alce::184__wikidata_comp__dev::p19

### `658__wikidata_simple__dev`
> Mary Garden was Sarah Robinson-Duff's first pupil. [alce::658__wikidata_simple__dev::p1]
> Additionally, Sarah Robinson-Duff taught many famous students in New York City, including Mary McCormic, Dorothy Gish, Helen Hayes, Kenneth MacKenna, Catherine Calvert, Ina Claire, Miriam Hopkins, Ruth Chatterton, Mary Pickford, Clark Gable, Norma Shearer, and Katharine Hepburn. [alce::658__wikidata_simple__dev::p2]

Cited: alce::658__wikidata_simple__dev::p1, alce::658__wikidata_simple__dev::p2

### `288__wikidata_intersection__dev`
> Charlie Chaplin composed music for "City Lights" (1931), which he also directed. [alce::288__wikidata_intersection__dev::p0]

Cited: alce::288__wikidata_intersection__dev::p0

### `103__wikidata_intersection__dev`
> Ayrton Senna won multiple Monaco Grand Prix races. He won the 1987 Monaco Grand Prix, driving a Lotus-Honda, which was his first of an eventual six wins at Monaco. [alce::103__wikidata_intersection__dev::p2]
> He won the 1990 Monaco Grand Prix, driving a McLaren-Honda, which was his second consecutive Monaco win and third in all. [alce::103__wikidata_intersection__dev::p5]
> He won the 1992 Monaco Grand Prix, driving a McLaren-Honda. [alce::103__wikidata_intersection__dev::p3]
> He also won his fourth Monaco Grand Prix in five years in 1991. [alce::103__wikidata_intersection__dev::p7]

Cited: alce::103__wikidata_intersection__dev::p2, alce::103__wikidata_intersection__dev::p3, alce::103__wikidata_intersection__dev::p5, alce::103__wikidata_intersection__dev::p7

### `630__wikidata_simple__dev`
> One game that id Software released is "Doom." [alce::630__wikidata_simple__dev::p3]
> Another example is "Wolfenstein 3D," which was the second major release by id Software. [alce::630__wikidata_simple__dev::p39]

Cited: alce::630__wikidata_simple__dev::p3, alce::630__wikidata_simple__dev::p39

### `819__wikidata_simple__dev`
> Several organizations serve the intersex community. The Organisation Intersex International (OII) is a global advocacy and support group for people with intersex traits and is described as the world's largest organization of intersex persons. [alce::819__wikidata_simple__dev::p6]
> Other notable intersex rights organizations include interACT and Intersex Campaign for Equality. [alce::819__wikidata_simple__dev::p8]

Cited: alce::819__wikidata_simple__dev::p6, alce::819__wikidata_simple__dev::p8

### `672__wikidata_simple__dev`
> The Union Jack can be found in the canton of the flags of several nations and territories that are former British possessions or dominions. [alce::672__wikidata_simple__dev::p0]
> It also appears in the state flag of Hawaii. [alce::672__wikidata_simple__dev::p0]
> Additionally, the coat of arms of the Chilean city of Coquimbo features the Union Jack. [alce::672__wikidata_simple__dev::p1]

Cited: alce::672__wikidata_simple__dev::p0, alce::672__wikidata_simple__dev::p1

### `351__wikidata_comp__dev`
> Multiple drivers won French Grand Prix competitions:

Juan Manuel Fangio and Luigi Fagioli won the 1951 French Grand Prix driving an Alfa Romeo. [alce::351__wikidata_comp__dev::p5]
> Jacky Ickx won the 1968 French Grand Prix driving for Ferrari. [alce::351__wikidata_comp__dev::p21]
> Giancarlo Baghetti won the French Grand Prix in a privately entered Ferrari on his championship debut. [alce::351__wikidata_comp__dev::p76]

Cited: alce::351__wikidata_comp__dev::p21, alce::351__wikidata_comp__dev::p5, alce::351__wikidata_comp__dev::p76

### `655__wikidata_simple__dev`
> During the Second Empire in Europe, several types of buildings were constructed, including theaters, churches, and public buildings.

Theaters were notable examples, with the Opéra Garnier being the most famous—it was begun in 1862 and was the largest theater in the world at the time. [alce::655__wikidata_simple__dev::p64]
> Public buildings such as the Palais de Justice, the Court of Cassation, the Tribunal de Commerce, and the Théâtre du Châtelet were also built during this period. [alce::655__wikidata_simple__dev::p26]
> Churches were extensively built and restored, including the Church of Saint Augustine (1860–71), which was the largest new church built in Paris during the Second Empire. [alce::655__wikidata_simple__dev::p21]
> These buildings were characterized by an eclectic style that drew from Gothic, Renaissance, and earlier European styles, often combined with mansard roofs and low, square-based domes. [alce::655__wikidata_simple__dev::p0]

Cited: alce::655__wikidata_simple__dev::p0, alce::655__wikidata_simple__dev::p21, alce::655__wikidata_simple__dev::p26, alce::655__wikidata_simple__dev::p64

### `934__wikidata_simple__dev`
> AVM Saeedullah Khan was a member of the Pakistan Air Force. [alce::934__wikidata_simple__dev::p23]
> He joined the newly formed air force as a flying officer (pilot) and rose to the rank of Air Vice Marshal, serving as Deputy Chief of Air Staff between 1972 and 1973. [alce::934__wikidata_simple__dev::p23]

Cited: alce::934__wikidata_simple__dev::p23

### `182__wikidata_intersection__dev`
> The VFL/AFL (Victorian Football League/Australian Football League) featured both Collingwood Football Club and Carlton Football Club as participants. [alce::182__wikidata_intersection__dev::p3]
> More specifically, the two clubs have played each other 256 times in the VFL/AFL competition. [alce::182__wikidata_intersection__dev::p3]
> Additionally, they met six times in Grand Finals of this competition. [alce::182__wikidata_intersection__dev::p8]

Cited: alce::182__wikidata_intersection__dev::p3, alce::182__wikidata_intersection__dev::p8

### `428__wikidata_comp__dev`
_Refused._

### `1010__wikidata_comp__dev`
> Jules Engel's students study at the California Institute of the Arts (CalArts). [alce::1010__wikidata_comp__dev::p0]
> He was the founding director of the Experimental Animation Program at this institution, where he taught until his death and served as mentor to several generations of animators. [alce::1010__wikidata_comp__dev::p0]

Cited: alce::1010__wikidata_comp__dev::p0

### `9__wikitables_composition__dev`
> KWOC is a Missouri radio station whose license is in the city of Poplar Bluff. [alce::9__wikitables_composition__dev::p26]

Cited: alce::9__wikitables_composition__dev::p26

### `37__wikitables_composition__dev`
> Based on the provided sources, the individuals who are not in favor of the BDS movement and are from Israel include:

Alan Dershowitz is associated with the Israeli Action Network and opposes the BDS movement. [alce::37__wikitables_composition__dev::p9]
> Israeli officials categorize the BDS movement as antisemitic and oppose it. [alce::37__wikitables_composition__dev::p5]
> Gerald Steinberg is an Israeli who opposes BDS, as evidenced by his op-ed published in "The Jerusalem Post" contending against the movement. [alce::37__wikitables_composition__dev::p6]

Cited: alce::37__wikitables_composition__dev::p5, alce::37__wikitables_composition__dev::p6, alce::37__wikitables_composition__dev::p9

### `416__wikidata_comp__dev`
_Refused._

### `835__wikidata_simple__dev`
> Victorian Railways manufactured several types of objects:

Wooden bogie passenger carriages with steel underframes and timber bodies were constructed, with a total of 640 such carriages built between 1874 and 1903. [alce::835__wikidata_simple__dev::p1]
> Hospital cars were constructed by converting second class passenger cars following the 1908 Sunshine collision. [alce::835__wikidata_simple__dev::p7]
> Rail tractors, which are small shunting units consisting of agricultural tractors mounted on four-wheeled steel rail wagon frames, were manufactured for moving railway wagons at country stations and private sidings. [alce::835__wikidata_simple__dev::p33]

Cited: alce::835__wikidata_simple__dev::p1, alce::835__wikidata_simple__dev::p33, alce::835__wikidata_simple__dev::p7

### `931__wikidata_simple__dev`
> Daniel Farke is the head coach of Norwich City FC. [alce::931__wikidata_simple__dev::p33]
> He was appointed to this position on 25 May 2017, becoming the first foreign head coach of the club in its 114-year history. [alce::931__wikidata_simple__dev::p44]

Cited: alce::931__wikidata_simple__dev::p33, alce::931__wikidata_simple__dev::p44

### `740__wikidata_simple__dev`
_Refused._

### `623__wikidata_simple__dev`
> Bryna Productions made the television series "Tales of the Vikings." [alce::623__wikidata_simple__dev::p48]
> This was an American first-run syndicated television series that first aired on September 8, 1959 and ran through June 2, 1960. [alce::623__wikidata_simple__dev::p48]

Cited: alce::623__wikidata_simple__dev::p48

### `638__wikidata_simple__dev`
> Several individuals were workers for the state of Nigeria:

Otunba Fatai Olukoga was a Permanent Secretary in Lagos State Civil Service. [alce::638__wikidata_simple__dev::p18]
> Iyabbo Jolaade Adewuyi was a Nigerian government official who served as a commissioner in Kwara State Government. [alce::638__wikidata_simple__dev::p88]
> Oseloka H. Obaze worked as a career Foreign Service Officer in the Nigerian Diplomatic Service from 1982-1991, and later served as Secretary to the State Government of Anambra State, Nigeria from June 2012 till June 2015. [alce::638__wikidata_simple__dev::p56]

Cited: alce::638__wikidata_simple__dev::p18, alce::638__wikidata_simple__dev::p56, alce::638__wikidata_simple__dev::p88

### `364__wikidata_intersection__dev`
_Refused._

### `958__wikidata_comp__dev`
> Kristie Canegallo, who served as Deputy White House Chief of Staff for Implementation under President Barack Obama, holds a Master of Arts degree from the Johns Hopkins School of Advanced International Studies and a Bachelor of Arts degree from Colgate University. [alce::958__wikidata_comp__dev::p27]

Cited: alce::958__wikidata_comp__dev::p27

### `522__wikitables_simple__dev`
> Based on the provided sources, famous grand mosques are located in the following cities:

Taipei has the Taipei Grand Mosque, which is the largest and most famous mosque in Taiwan. [alce::522__wikitables_simple__dev::p97]
> Beijing has the Niujie Mosque, the oldest and most famous mosque in the city. [alce::522__wikitables_simple__dev::p57]
> Paris has the Grand Mosque of Paris, which is the largest mosque in France and the third largest in Europe. [alce::522__wikitables_simple__dev::p25]
> Dubai has the Grand Mosque, which is the hub of Dubai's religious and cultural life. [alce::522__wikitables_simple__dev::p19]

Cited: alce::522__wikitables_simple__dev::p19, alce::522__wikitables_simple__dev::p25, alce::522__wikitables_simple__dev::p57, alce::522__wikitables_simple__dev::p97

### `447__wikidata_intersection__dev`
_Refused._

### `24__wikitables_composition__dev`
> A census designated place in Cumberland County, Maine is a type of geographic area used by the United States Census Bureau. [alce::24__wikitables_composition__dev::p3]
> Examples of census designated places in Cumberland County, Maine include Cumberland Center, which had a population of 2,499 at the 2010 census [alce::24__wikitables_composition__dev::p3]
> , Freeport, which had a population of 1,485 at the 2010 census [alce::24__wikitables_composition__dev::p48]
> , and Brunswick, which had a population of 15,175 at the 2010 census [alce::24__wikitables_composition__dev::p23]
> .

Cited: alce::24__wikitables_composition__dev::p23, alce::24__wikitables_composition__dev::p3, alce::24__wikitables_composition__dev::p48

### `653__wikidata_simple__dev`
> Multiple species were discovered in the Paja Formation. These include the ichthyosaur *Muiscasaurus catheti* [alce::653__wikidata_simple__dev::p43]
> , the sauropod dinosaur *Padillasaurus leivaensis* [alce::653__wikidata_simple__dev::p41]
> , the pliosaur *Stenorhynchosaurus munozi* [alce::653__wikidata_simple__dev::p3]
> , the ichthyosaur *Platypterygius sachicarum* [alce::653__wikidata_simple__dev::p3]
> , and the sea turtle *Desmatochelys padillai* [alce::653__wikidata_simple__dev::p4]
> .

Cited: alce::653__wikidata_simple__dev::p3, alce::653__wikidata_simple__dev::p4, alce::653__wikidata_simple__dev::p41, alce::653__wikidata_simple__dev::p43

### `1254__wikitables_composition__dev`
_Refused._

### `287__wikidata_comp__dev`
> John Hall, the current Dean of Westminster, was educated at St Dunstan's College, Catford and St Chad's. [alce::287__wikidata_comp__dev::p45]

Cited: alce::287__wikidata_comp__dev::p45

### `584__wikidata_simple__dev`
> Several military units belong to the EU Battlegroup framework:

Battlegroup 107 (BG-107) is an EU Battlegroup that originally consisted of military elements from the Netherlands, Germany, and Finland. [alce::584__wikidata_simple__dev::p12]
> The Nordic Battlegroup is a multi-national military unit and one of eighteen European Union Battlegroups, consisting of around 2,500 troops from Sweden, Finland, Norway, Ireland, Estonia, Latvia and Lithuania. [alce::584__wikidata_simple__dev::p94]
> More broadly, an EU Battlegroup is a military unit adhering to the Common Security and Defence Policy of the European Union, with each of the eighteen Battlegroups consisting of a battalion-sized force of approximately 1,500 troops reinforced with combat support elements. [alce::584__wikidata_simple__dev::p0]

Cited: alce::584__wikidata_simple__dev::p0, alce::584__wikidata_simple__dev::p12, alce::584__wikidata_simple__dev::p94

### `33__wikitables_composition__dev`
> The Aon Centre is a tall building in Wellington that houses offices. [alce::33__wikitables_composition__dev::p0]
> The Majestic Centre is the tallest building in Wellington and also houses offices. [alce::33__wikitables_composition__dev::p5]
> Additionally, Plimmer Towers is a high-rise office complex in central Wellington. [alce::33__wikitables_composition__dev::p1]

Cited: alce::33__wikitables_composition__dev::p0, alce::33__wikitables_composition__dev::p1, alce::33__wikitables_composition__dev::p5

### `95__wikitables_composition__dev`
> Based on the provided sources, the Atlus games released for the Nintendo 3DS console are:

1. "Persona Q: Shadow of the Labyrinth" is a role-playing video game developed by Atlus for the Nintendo 3DS handheld video game console. [alce::95__wikitables_composition__dev::p73]
> 2. "Etrian Odyssey V: Beyond the Myth" is a dungeon crawler role-playing video game developed and published by Atlus for the Nintendo 3DS. [alce::95__wikitables_composition__dev::p28]

Cited: alce::95__wikitables_composition__dev::p28, alce::95__wikitables_composition__dev::p73

### `1353__wikidata_simple__dev`
> Several individuals were members of the Croatian National Guard:

Damir Krstičević joined the Croatian National Guard in the summer of 1991 and was assigned to the 4th Guards Brigade, where he eventually rose to the position of brigade commander. [alce::1353__wikidata_simple__dev::p27]
> Imra Agotić defected to the Croatian National Guard in July 1991 and became its first commanding officer in August 1991. [alce::1353__wikidata_simple__dev::p63]
> An unnamed foreign volunteer joined the Croatian National Guard in Osijek in 1991 as its first foreign volunteer and participated in several battles in Slavonia. [alce::1353__wikidata_simple__dev::p95]

Cited: alce::1353__wikidata_simple__dev::p27, alce::1353__wikidata_simple__dev::p63, alce::1353__wikidata_simple__dev::p95

### `684__wikidata_simple__dev`
> K. S. Rama Rao produced several popular films, including Mounageetam, Abhilasha, Rakshasudu, Chanti, Matrudevobhava, and Swarna Kamalam. [alce::684__wikidata_simple__dev::p1]

Cited: alce::684__wikidata_simple__dev::p1

### `768__wikidata_simple__dev`
_Refused._

### `693__wikidata_simple__dev`
> SS501 is a South Korean boy band consisting of five members: Kim Hyun-joong, Heo Young-saeng, Kim Kyu-jong, Park Jung-min, and Kim Hyung-jun. [alce::693__wikidata_simple__dev::p1]

Cited: alce::693__wikidata_simple__dev::p1

### `230__wikidata_comp__dev`
> Media companies owned by Ohio Community Media published primarily in the state of Ohio. [alce::230__wikidata_comp__dev::p0]
> The company published 18 daily newspapers and about 30 weeklies (paid and free), in addition to several free weekly shopper publications, with publications located in Central Ohio (Columbus area), Mid-Ohio (Mansfield area), Northwest Ohio, Southern Ohio, and Western Ohio (Dayton area). [alce::230__wikidata_comp__dev::p5]

Cited: alce::230__wikidata_comp__dev::p0, alce::230__wikidata_comp__dev::p5

### `408__wikidata_comp__dev`
_Refused._

### `252__wikidata_intersection__dev`
> "The Phantom Tollbooth" had Abe Levitow as its director and Chuck Jones as producer. [alce::252__wikidata_intersection__dev::p1]

Cited: alce::252__wikidata_intersection__dev::p1

### `583__wikidata_simple__dev`
_Refused._

### `718__wikidata_simple__dev`
_Refused._

### `484__wikitables_simple__dev`
> Several power plants have held the title of largest power plant in the world at different points in time:

The Vemork power station was the world's largest power plant when it opened in 1911. [alce::484__wikitables_simple__dev::p0]
> The Volga Hydroelectric Station was the largest power station in the world between 1960 and 1963. [alce::484__wikitables_simple__dev::p26]
> Itaipu was the world's biggest power plant at the time of a power crisis in São Paulo state. [alce::484__wikitables_simple__dev::p1]
> The Three Gorges Dam is the world's largest power station in terms of installed capacity (22,500 MW). [alce::484__wikitables_simple__dev::p97]
> The Tuoketuo Power Station is the largest coal-fired power station in the world. [alce::484__wikitables_simple__dev::p7]

Cited: alce::484__wikitables_simple__dev::p0, alce::484__wikitables_simple__dev::p1, alce::484__wikitables_simple__dev::p26, alce::484__wikitables_simple__dev::p7, alce::484__wikitables_simple__dev::p97

### `616__wikidata_simple__dev`
> The Entertainment Consumers Association was a coalition partner with Reddit, Google, EFF, Public Knowledge, Major League Gaming, and Demand Progress in opposing the Stop Online Piracy Act (SOPA) and the Protect Intellectual Property Act (PIPA). [alce::616__wikidata_simple__dev::p4]
> Additionally, the ECA lists brands and companies which are marketing partners with the ECA on their website, most of which provide discounts and special promotions. [alce::616__wikidata_simple__dev::p30]

Cited: alce::616__wikidata_simple__dev::p30, alce::616__wikidata_simple__dev::p4

### `144__wikidata_intersection__dev`
> Sukumar chose Devi Sri Prasad to compose the soundtrack and background score for the films he directed. [alce::144__wikidata_intersection__dev::p2]
> Specifically, Devi Sri Prasad composed music for "Arya," which was Sukumar's directorial debut in 2004. [alce::144__wikidata_intersection__dev::p31]
> Additionally, Prasad served as Sukumar's usual composer and was chosen for the soundtrack and score of another film directed by Sukumar. [alce::144__wikidata_intersection__dev::p1]

Cited: alce::144__wikidata_intersection__dev::p1, alce::144__wikidata_intersection__dev::p2, alce::144__wikidata_intersection__dev::p31

### `592__wikidata_simple__dev`
> Steamboat Lake State Park is a natural place located near Steamboat Springs, Colorado. [alce::592__wikidata_simple__dev::p1]
> The Mount Zirkel Wilderness is also located near Steamboat Springs, Colorado. [alce::592__wikidata_simple__dev::p94]

Cited: alce::592__wikidata_simple__dev::p1, alce::592__wikidata_simple__dev::p94

### `925__wikidata_simple__dev`
> Based on the provided sources, the Pakistan Atomic Energy Commission has had the following people working for them:

Nazir Ahmad was the first chairman of PAEC when it was founded in 1956. [alce::925__wikidata_simple__dev::p1]
> Salimuzzaman Siddiqui served as Science Advisor to the Prime Minister at the agency. [alce::925__wikidata_simple__dev::p1]
> Dr. Naeem Ahmad Khan led the physics staff at PAEC. [alce::925__wikidata_simple__dev::p15]
> Parvez Butt worked as a Chief Scientist at PAEC until his retirement on 4 July 2006. [alce::925__wikidata_simple__dev::p25]
> Dr. Anwar Ali, a nuclear physicist, took over as Chairman of the Pakistan Atomic Energy Commission in 2006. [alce::925__wikidata_simple__dev::p25]
> Qureshi joined the physics staff at PAEC in 1963 and later worked at the Pakistan Institute of Nuclear Science and Technology (PINSTECH). [alce::925__wikidata_simple__dev::p15]

Cited: alce::925__wikidata_simple__dev::p1, alce::925__wikidata_simple__dev::p15, alce::925__wikidata_simple__dev::p25

### `775__wikidata_simple__dev`
> Natacha Rambova designed costumes for several films. She designed costumes for the comedy film "Billions" (1920) [alce::775__wikidata_simple__dev::p3]
> . She also designed costumes for two Cecil DeMille films in 1920: "Why Change Your Wife?" and "Something to Think About" [alce::775__wikidata_simple__dev::p3]
> . Additionally, she designed costumes for "Camille" (1921) [alce::775__wikidata_simple__dev::p2]
> .

Cited: alce::775__wikidata_simple__dev::p2, alce::775__wikidata_simple__dev::p3

### `110__wikidata_comp__dev`
_Refused._

### `426__wikidata_intersection__dev`
> Lewis Hamilton won the Formula One World Championship in 2008 with McLaren, becoming the youngest ever F1 world champion in his second season. [alce::426__wikidata_intersection__dev::p7]
> He subsequently won back-to-back titles in 2014 and 2015 with Mercedes. [alce::426__wikidata_intersection__dev::p46]

Cited: alce::426__wikidata_intersection__dev::p46, alce::426__wikidata_intersection__dev::p7

### `15__wikitables_composition__dev`
_Refused._

### `120__wikidata_intersection__dev`
> Otto Binder and Al Plastino were responsible for the development of multiple fictional characters. They co-created Supergirl in "Action Comics" #252 (May 1959). [alce::120__wikidata_intersection__dev::p23]
> They also debuted the supervillain Brainiac and the Bottle City of Kandor in "Action Comics" #242 (July 1958). [alce::120__wikidata_intersection__dev::p23]
> Additionally, they co-created the Legion of Super-Heroes, a teen superhero team from the future, with the first Legion characters being Cosmic Boy, Lightning Lad, and Saturn Girl. [alce::120__wikidata_intersection__dev::p56]

Cited: alce::120__wikidata_intersection__dev::p23, alce::120__wikidata_intersection__dev::p56

### `966__wikidata_comp__dev`
> Richard Lewis, a Bishop of St Edmundsbury and Ipswich, was educated at Radley College and trained for the priesthood at King's College London. [alce::966__wikidata_comp__dev::p14]

Cited: alce::966__wikidata_comp__dev::p14

### `440__wikidata_intersection__dev`
> Tímea Babos and Kristina Mladenovic won the 2018 Australian Open – Women's Doubles title, defeating Ekaterina Makarova and Elena Vesnina in the final, 6–4, 6–3. [alce::440__wikidata_intersection__dev::p2]
> They also won the 2018 Birmingham Classic, defeating Elise Mertens and Demi Schuurs in the final. [alce::440__wikidata_intersection__dev::p10]

Cited: alce::440__wikidata_intersection__dev::p10, alce::440__wikidata_intersection__dev::p2

### `413__wikidata_comp__dev`
_Refused._

### `820__wikidata_simple__dev`
> The United States Army Corps of Engineers maintained several major structures:

The Corps maintained direct control of 609 dams. [alce::820__wikidata_simple__dev::p6]
> The Corps maintained or operated 257 navigation locks. [alce::820__wikidata_simple__dev::p6]
> The Corps operated 75 hydroelectric facilities. [alce::820__wikidata_simple__dev::p6]
> The Corps maintained U.S. inland and intracoastal waterways, which included 191 commercially active lock sites with 237 lock chambers. [alce::820__wikidata_simple__dev::p45]
> The Corps inspected over 2,000 Federal and non-Federal levees every two years. [alce::820__wikidata_simple__dev::p6]

Cited: alce::820__wikidata_simple__dev::p45, alce::820__wikidata_simple__dev::p6

### `664__wikidata_simple__dev`
> Type VII submarines were German U-boats that were the most widely used submarines of World War II. [alce::664__wikidata_simple__dev::p4]
> Specific examples of Type VII variants included the Type VIIF, of which only four were built. [alce::664__wikidata_simple__dev::p8]
> The Type VII design was the most produced submarine class in history, with 703 built in total. [alce::664__wikidata_simple__dev::p4]

Cited: alce::664__wikidata_simple__dev::p4, alce::664__wikidata_simple__dev::p8

### `118__wikidata_comp__dev`
> The Security Force Assistance Brigades have multiple headquarters locations depending on which brigade:

The 1st Security Force Assistance Brigade is based in Fort Benning, Georgia. [alce::118__wikidata_comp__dev::p1]
> The 2nd Security Force Assistance Brigade is based in Fort Bragg, North Carolina, alongside the Security Force Assistance Command. [alce::118__wikidata_comp__dev::p0]
> The 3rd Security Force Assistance Brigade is based in Fort Hood, Texas. [alce::118__wikidata_comp__dev::p6]
> The 54th Security Force Assistance Brigade has its headquarters provided by the Indiana Army National Guard. [alce::118__wikidata_comp__dev::p9]

Cited: alce::118__wikidata_comp__dev::p0, alce::118__wikidata_comp__dev::p1, alce::118__wikidata_comp__dev::p6, alce::118__wikidata_comp__dev::p9

### `260__wikidata_intersection__dev`
> Baz Luhrmann directed and Craig Pearce screen wrote multiple films together. These include "Strictly Ballroom" (1992) [alce::260__wikidata_intersection__dev::p0]
> , "Romeo + Juliet" (1996) [alce::260__wikidata_intersection__dev::p0]
> , "Moulin Rouge!" (2001) [alce::260__wikidata_intersection__dev::p0]
> , and "The Great Gatsby" (2013) [alce::260__wikidata_intersection__dev::p0]
> .

Cited: alce::260__wikidata_intersection__dev::p0

### `1259__wikitables_composition__dev`
> Dick Vermeil coached a Super Bowl finalist after 1981. [alce::1259__wikitables_composition__dev::p33]
> He led the St. Louis Rams to Super Bowl XXXIV in 1999. [alce::1259__wikitables_composition__dev::p33]
> Additionally, Joe Gibbs coached a Super Bowl finalist after 1981, leading the Washington Redskins to three Super Bowl championships (XVII, XXII, and XXVI). [alce::1259__wikitables_composition__dev::p27]

Cited: alce::1259__wikitables_composition__dev::p27, alce::1259__wikitables_composition__dev::p33

### `358__wikidata_comp__dev`
_Refused._

### `711__wikidata_simple__dev`
_Refused._

### `751__wikidata_simple__dev`
> Several people are employed by India's Archaeological Survey:

Gautam Sengupta is an archaeologist who served as Director General of the Archaeological Survey of India. [alce::751__wikidata_simple__dev::p0]
> Rakesh Tiwari is a professional archaeologist and the present incumbent Director General of the Archaeological Survey of India. [alce::751__wikidata_simple__dev::p0]
> D. R. Bhandarkar was an Indian archaeologist and epigraphist who worked with the Archaeological Survey of India. [alce::751__wikidata_simple__dev::p61]
> Kashinath Narayan Dikshit was an Indian archaeologist who served as Director-general of the Archaeological Survey of India from 1937 to 1944. [alce::751__wikidata_simple__dev::p49]
> M. N. Deshpande is an Indian archaeologist, art historian and conservator who served as Director General of the Archaeological Survey of India from 1972 to 1978. [alce::751__wikidata_simple__dev::p36]
> J. F. Blakiston was a British Indian archaeologist who served as Director General of the Archaeological Survey of India from 1935 to 1937. [alce::751__wikidata_simple__dev::p58]

Cited: alce::751__wikidata_simple__dev::p0, alce::751__wikidata_simple__dev::p36, alce::751__wikidata_simple__dev::p49, alce::751__wikidata_simple__dev::p58, alce::751__wikidata_simple__dev::p61

### `354__wikidata_comp__dev`
> Based on the provided sources, multiple teams emerged victorious in competitions featuring the Essendon Football Club:

Footscray Football Club defeated Essendon by 28 points in the 1924 Championship of Victoria. [alce::354__wikidata_comp__dev::p20]
> Essendon won the 1981 Escort Cup, defeating Carlton 9.11 (65) to 6.5 (41). [alce::354__wikidata_comp__dev::p33]
> Essendon defeated Carlton in a Grand Final by 73 points, with a final score of 18.17 (125) to 6.16 (52). [alce::354__wikidata_comp__dev::p65]

Cited: alce::354__wikidata_comp__dev::p20, alce::354__wikidata_comp__dev::p33, alce::354__wikidata_comp__dev::p65

### `560__wikidata_simple__dev`
> Several players were drafted by the Los Angeles Angels:

Taylor Ward was drafted by the Angels in the first round of the 2015 MLB Draft. [alce::560__wikidata_simple__dev::p73]
> David Fletcher was drafted by the Los Angeles Angels in the sixth round of the 2015 Major League Baseball Draft. [alce::560__wikidata_simple__dev::p70]
> Michael Hermosillo was drafted by the Los Angeles Angels in the 28th round of the 2013 Major League Baseball Draft. [alce::560__wikidata_simple__dev::p13]
> Kaleb Cowart was drafted by the Los Angeles Angels in the first round (18th overall) in the 2010 Major League Baseball Draft. [alce::560__wikidata_simple__dev::p62]
> Tyler Skaggs was drafted by the Los Angeles Angels of Anaheim in the first round of the 2009 Major League Baseball draft. [alce::560__wikidata_simple__dev::p14]

Cited: alce::560__wikidata_simple__dev::p13, alce::560__wikidata_simple__dev::p14, alce::560__wikidata_simple__dev::p62, alce::560__wikidata_simple__dev::p70, alce::560__wikidata_simple__dev::p73

### `715__wikidata_simple__dev`
> Jonathan Strahan edited numerous written works. As a freelance editor, he edited or co-edited forty-one original and reprint anthologies, and seventeen single-author story collections published in Australia and the United States. [alce::715__wikidata_simple__dev::p0]
> He also edited an online extension of his Eclipse anthology series called *Eclipse Online* from October 2012 till March 2013. [alce::715__wikidata_simple__dev::p2]

Cited: alce::715__wikidata_simple__dev::p0, alce::715__wikidata_simple__dev::p2

### `643__wikidata_simple__dev`
> Several vehicle models belong to Autozam:

The Autozam Clef is a mid-size sedan that was sold by Autozam from 1992 until 1994. [alce::643__wikidata_simple__dev::p6]
> The Autozam Revue is a subcompact car that was sold by Autozam, introduced in 1990. [alce::643__wikidata_simple__dev::p7]
> The Autozam Scrum is a cabover microvan and kei truck sold exclusively in Japan by Mazda, originally part of the company's Autozam marque and first introduced in June 1989. [alce::643__wikidata_simple__dev::p36]

Cited: alce::643__wikidata_simple__dev::p36, alce::643__wikidata_simple__dev::p6, alce::643__wikidata_simple__dev::p7

### `790__wikidata_simple__dev`
> Based on the provided sources, ID Software developed and/or published the following electronic games:

The "Wolfenstein" franchise, including "Wolfenstein 3D" and "Return to Castle Wolfenstein."
> The "Doom" franchise, including "Doom" and "Doom 3."
> The "Quake" franchise, including "Quake," "Quake II," "Quake III Arena," and "Quake 4."
> "Rage" and "Rage 2." [alce::790__wikidata_simple__dev::p9]
> "Rage HD," a spin-off title for iPhone. [alce::790__wikidata_simple__dev::p3]
> Early 3D first-person shooter experiments including "Hovertank 3D" and "Catacomb 3D." [alce::790__wikidata_simple__dev::p3]
> The "Rescue Rover" series, which included "Rescue Rover" and "Rescue Rover 2." [alce::790__wikidata_simple__dev::p3]
> John Romero's "Dangerous Dave" series. [alce::790__wikidata_simple__dev::p3]

Cited: alce::790__wikidata_simple__dev::p3, alce::790__wikidata_simple__dev::p9

### `404__wikidata_intersection__dev`
_Refused._

### `148__wikidata_intersection__dev`
> Portsmouth F.C. participated in multiple FA Cup Finals:

On 17 May 2008, Portsmouth played Cardiff City in the FA Cup Final at the newly rebuilt Wembley Stadium, which Portsmouth won 1–0. [alce::148__wikidata_intersection__dev::p0]
> Portsmouth also reached the FA Cup Final in the 1933–34 season, where they were defeated by Manchester City. [alce::148__wikidata_intersection__dev::p11]
> Portsmouth contested the 1939 FA Cup Final against Wolverhampton Wanderers. [alce::148__wikidata_intersection__dev::p53]
> In the 2009–10 FA Cup, Portsmouth reached the final at Wembley Stadium against Chelsea, which Chelsea won 1–0. [alce::148__wikidata_intersection__dev::p37]

Cited: alce::148__wikidata_intersection__dev::p0, alce::148__wikidata_intersection__dev::p11, alce::148__wikidata_intersection__dev::p37, alce::148__wikidata_intersection__dev::p53

### `232__wikidata_comp__dev`
> Multiple teams competed in CAF Super Cup competitions. Al-Ahly of Egypt competed in the 2013 CAF Super Cup. [alce::232__wikidata_comp__dev::p14]
> TP Mazembe of the Democratic Republic of the Congo competed in the 2011 CAF Super Cup. [alce::232__wikidata_comp__dev::p6]
> ES Sahel competed in the 2008 CAF Super Cup. [alce::232__wikidata_comp__dev::p0]
> Mamelodi Sundowns of South Africa competed in the 2017 CAF Super Cup. [alce::232__wikidata_comp__dev::p15]

Cited: alce::232__wikidata_comp__dev::p0, alce::232__wikidata_comp__dev::p14, alce::232__wikidata_comp__dev::p15, alce::232__wikidata_comp__dev::p6

### `874__wikidata_simple__dev`
> CNN Philippines originally broadcast 9TV programming. [alce::874__wikidata_simple__dev::p0]
> More specifically, CNN Philippines replaced 9TV when it was launched on March 16, 2015. [alce::874__wikidata_simple__dev::p5]

Cited: alce::874__wikidata_simple__dev::p0, alce::874__wikidata_simple__dev::p5

### `670__wikidata_simple__dev`
> Penny Rose is a worker in the costume designer industry. [alce::670__wikidata_simple__dev::p88]
> Michael Kaplan is an American costume designer who has been working in the Hollywood film industry since 1981. [alce::670__wikidata_simple__dev::p23]
> Roshni Dinaker is an Indian costume designer who has worked in Kannada, Tamil, and Telugu film industries. [alce::670__wikidata_simple__dev::p40]

Cited: alce::670__wikidata_simple__dev::p23, alce::670__wikidata_simple__dev::p40, alce::670__wikidata_simple__dev::p88

### `211__wikidata_intersection__dev`
> The Baltimore Orioles (1882–99) won the National League pennant in 1894. [alce::211__wikidata_intersection__dev::p37]
> They finished in first place three consecutive years from 1894–1895–1896. [alce::211__wikidata_intersection__dev::p10]
> They won the "Temple Cup" national championship series in 1896 and 1897. [alce::211__wikidata_intersection__dev::p10]
> The Orioles participated in the first Temple Cup competition in 1894 against the second-place New York Giants, though they lost in a sweep, four games to none. [alce::211__wikidata_intersection__dev::p37]
> The Baltimore Orioles ice hockey team won the EAHL championship in the 1939–40 season. [alce::211__wikidata_intersection__dev::p95]

Cited: alce::211__wikidata_intersection__dev::p10, alce::211__wikidata_intersection__dev::p37, alce::211__wikidata_intersection__dev::p95

### `308__wikidata_comp__dev`
_Refused._

### `280__wikidata_intersection__dev`
_Refused._

### `150__wikidata_intersection__dev`
> Elena Vesnina and Ekaterina Valeryevna Makarova won the 2013 French Open doubles title. [alce::150__wikidata_intersection__dev::p3]
> They also won the 2014 US Open doubles title. [alce::150__wikidata_intersection__dev::p3]
> Additionally, they won the 2017 Wimbledon doubles title. [alce::150__wikidata_intersection__dev::p3]

Cited: alce::150__wikidata_intersection__dev::p3

### `917__wikidata_simple__dev`
> Avatar Press published comic books, including "Bad Girl" comics such as "Pandora", "Hellina", "Lookers", "The Ravening", and Brian Pulido's "Lady Death". [alce::917__wikidata_simple__dev::p0]
> They also published creator-owned books by notable creators including Frank Miller, Warren Ellis, Alan Moore, and Garth Ennis. [alce::917__wikidata_simple__dev::p1]
> Additionally, Avatar Press published licensed comic book adaptations of famous sci-fi and horror properties such as "RoboCop", "Night of the Living Dead", and "Friday the 13th". [alce::917__wikidata_simple__dev::p1]
> They published the webcomic "FreakAngels" by Warren Ellis. [alce::917__wikidata_simple__dev::p0]
> Avatar Press also published "Widow" and "Widow X" comics. [alce::917__wikidata_simple__dev::p6]

Cited: alce::917__wikidata_simple__dev::p0, alce::917__wikidata_simple__dev::p1, alce::917__wikidata_simple__dev::p6

### `933__wikidata_simple__dev`
_Refused._

### `629__wikidata_simple__dev`
> Speed Channel originally broadcasted "Car and Track," a 1960s and 1970s show that was hosted and narrated by Bud Lindemann. [alce::629__wikidata_simple__dev::p5]

Cited: alce::629__wikidata_simple__dev::p5

### `319__wikidata_intersection__dev`
> The Washington Football Team (formerly known as the Washington Redskins) played in five Super Bowls. [alce::319__wikidata_intersection__dev::p54]
> They won three of these Super Bowls: Super Bowl XVII, Super Bowl XXII, and Super Bowl XXVI. [alce::319__wikidata_intersection__dev::p1]
> They also played in and lost Super Bowl VII and Super Bowl XVIII. [alce::319__wikidata_intersection__dev::p1]

Cited: alce::319__wikidata_intersection__dev::p1, alce::319__wikidata_intersection__dev::p54

### `755__wikidata_simple__dev`
> One automobile model from Chery is the Tiggo. [alce::755__wikidata_simple__dev::p2]
> Another example is the Chery A3, a compact car built between 2008-2015. [alce::755__wikidata_simple__dev::p1]

Cited: alce::755__wikidata_simple__dev::p1, alce::755__wikidata_simple__dev::p2

### `235__wikidata_intersection__dev`
> James Gray wrote and directed "Ad Astra," a sci-fi space epic. [alce::235__wikidata_intersection__dev::p1]

Cited: alce::235__wikidata_intersection__dev::p1

### `46__wikitables_composition__dev`
_Refused._

### `698__wikidata_simple__dev`
_Refused._

### `105__wikidata_comp__dev`
_Refused._

### `343__wikidata_intersection__dev`
_Refused._

### `756__wikidata_simple__dev`
> The Richelieu River is located next to Lake Champlain. [alce::756__wikidata_simple__dev::p0]
> It also flows through the province of Quebec, Canada, and is situated on the border between Canada (Quebec) and the United States (Vermont and New York state). [alce::756__wikidata_simple__dev::p0]

Cited: alce::756__wikidata_simple__dev::p0

### `515__wikitables_simple__dev`
> Based on the provided sources, olive cultivars can be categorized by their use and geographic origin:

**By Use:**
Olives cultivated for consumption are generally referred to as table olives. [alce::515__wikitables_simple__dev::p52]
> Some cultivars are used for oil production, while others are used for both purposes.
> **Specific Cultivar Examples:**
Olive cultivars include Arbequina, Arecuzzo, Barnea, Barouni, Coratina, Correggiola, Del Morocco, Frantoio, Hojiblanca, Jumbo Kalamata, Kalamata, Koroneiki, Leccino, Manzanillo, Pendolino, Picholine, Picual, Sevillano, UC13A6, and Verdale. [alce::515__wikitables_simple__dev::p12]
> In Palestinian territories, the main olive cultivars used are Chemlali, Jebbah, K18, Manzolino, Nabali Baladi, Nabali Mohassan, Shami and Souri. [alce::515__wikitables_simple__dev::p42]
> Italian olive varieties include Baresane, Biancolilla, Brandofino, Buscionetto, Carolea, Cellina di Nardò, Cerasuola, Cerignola, Cima di Bitonto, Cima di Mola, Coratina, Frantoio, Garganica, La Minuta, Leccino, Moresca, Nocellara Etnea, Nocellara Messinese, Ogliarola, Ogliarola Barese, Ogliara Messinese, Ottobratica, Peranzana, Rotondella, Santagatese, Saracena, Tonda Iblea, and Verdello. [alce::515__wikitables_simple__dev::p3]
> **Modern Breeding Efforts:**
In recent times, efforts have been directed at producing hybrid cultivars with qualities useful to farmers, such as resistance to disease, quick growth, and larger or more consistent crops. [alce::515__wikitables_simple__dev::p52]

Cited: alce::515__wikitables_simple__dev::p12, alce::515__wikitables_simple__dev::p3, alce::515__wikitables_simple__dev::p42, alce::515__wikitables_simple__dev::p52

### `779__wikidata_simple__dev`
_Refused._

### `572__wikidata_simple__dev`
> Spjøtvoll is an employee of the Norwegian Institute of Technology. [alce::572__wikidata_simple__dev::p16]

Cited: alce::572__wikidata_simple__dev::p16

### `397__wikidata_intersection__dev`
> Chelsea F.C. played in the FA Cup Finals in 1994, 1995, 1996, 1999, 2000, 2002, 2004, 2005, 2007, 2009, and 2012. [alce::397__wikidata_intersection__dev::p26]

Cited: alce::397__wikidata_intersection__dev::p26

### `465__wikidata_intersection__dev`
_Refused._

### `949__wikidata_comp__dev`
_Refused._

### `800__wikidata_simple__dev`
> Sam Simon was a screenwriter for multiple TV shows. He wrote for "Taxi" [alce::800__wikidata_simple__dev::p0]
> , "Cheers" [alce::800__wikidata_simple__dev::p0]
> , and "It's Garry Shandling's Show" [alce::800__wikidata_simple__dev::p0]
> . He is most notably known for co-developing "The Simpsons" [alce::800__wikidata_simple__dev::p0]
> .

Cited: alce::800__wikidata_simple__dev::p0

### `538__wikitables_simple__dev`
> Based on the provided sources, here are the discovered ring galaxies:

Hoag's Object is a ring galaxy discovered by Art Hoag in 1950. [alce::538__wikitables_simple__dev::p0]
> The ring contains many massive, relatively young blue stars, which are extremely bright, while the central region contains relatively little luminous matter. [alce::538__wikitables_simple__dev::p0]
> NGC 1291, also known as NGC 1269, is a ring galaxy with an unusual inner bar and outer ring structure located about 33 million light-years away in the constellation Eridanus. [alce::538__wikitables_simple__dev::p14]
> It was discovered by James Dunlop in 1826. [alce::538__wikitables_simple__dev::p14]
> Another ring galaxy mentioned is one in Serpens with an outer ring largely composed of young blue stars and a core made up of older yellow stars. [alce::538__wikitables_simple__dev::p72]

Cited: alce::538__wikitables_simple__dev::p0, alce::538__wikitables_simple__dev::p14, alce::538__wikitables_simple__dev::p72

### `375__wikidata_intersection__dev`
> Tottenham Hotspur faced Manchester City in multiple matches documented in the sources. One notable match was the Fourth Round replay of the 2003–04 FA Cup, played at White Hart Lane, London, on 4 February 2004. [alce::375__wikidata_intersection__dev::p3]
> In this match, Tottenham led 3–0 at half-time but Manchester City won 4–3, with Jon Macken scoring the winning goal in the 90th minute. [alce::375__wikidata_intersection__dev::p54]
> Another match between the teams occurred when Manchester City faced Tottenham Hotspur at home in snowy conditions, in a match televised on "Match of the Day." [alce::375__wikidata_intersection__dev::p45]
> Additionally, Tottenham Hotspur beat Manchester City 4-2 at Maine Road in an FA Cup match. [alce::375__wikidata_intersection__dev::p15]

Cited: alce::375__wikidata_intersection__dev::p15, alce::375__wikidata_intersection__dev::p3, alce::375__wikidata_intersection__dev::p45, alce::375__wikidata_intersection__dev::p54

### `36__wikitables_composition__dev`
> The Mercedes-AMG GT is a model of a sports car manufactured by Mercedes-AMG. [alce::36__wikitables_composition__dev::p0]
> Another example is the Mercedes-AMG One, an upcoming limited-production plug-in hybrid sports car manufactured by Mercedes-AMG. [alce::36__wikitables_composition__dev::p8]

Cited: alce::36__wikitables_composition__dev::p0, alce::36__wikitables_composition__dev::p8

### `736__wikidata_simple__dev`
_Refused._

### `491__wikitables_simple__dev`
> # Existing Youth Councils

In the United States, several state governments have created youth councils, including Washington, Minnesota, Maine, Iowa, Indiana, Louisiana, New Mexico, Massachusetts, and New Hampshire. [alce::491__wikitables_simple__dev::p2]
> Many U.S. cities have active youth councils, including Boston, Los Angeles, San Francisco, Chicago, Miami, Houston, Dallas, Seattle, and San Jose, California. [alce::491__wikitables_simple__dev::p0]
> In the United Kingdom, the British Youth Council operates the UK Youth Parliament, which allows young people between the ages of 11-18 to vote for their local Member of Youth Parliament. [alce::491__wikitables_simple__dev::p1]
> In Europe, France has approximately 1,800 local youth and children's councils, with 500 members belonging to Anacej (National Association of youth and children councils), an umbrella organization founded in 1991. [alce::491__wikitables_simple__dev::p5]
> Greece operates the Greek Youth Parliament, which includes participation from youth in countries with large Greek communities such as Germany and Australia. [alce::491__wikitables_simple__dev::p5]
> In Israel, there is a National Youth Council whose members are elected from 7 Regional Youth Councils, which are in turn elected from Municipal councils formed from representatives of School Student Councils and Youth Movements. [alce::491__wikitables_simple__dev::p5]

Cited: alce::491__wikitables_simple__dev::p0, alce::491__wikitables_simple__dev::p1, alce::491__wikitables_simple__dev::p2, alce::491__wikitables_simple__dev::p5

### `750__wikidata_simple__dev`
> Stephen R. Fitzgarrald was a Colorado Lieutenant Governor. [alce::750__wikidata_simple__dev::p11]
> He served as the 17th Lieutenant Governor of Colorado from 1909 to 1915 under Governors John F. Shafroth and Elias M. Ammons. [alce::750__wikidata_simple__dev::p11]

Cited: alce::750__wikidata_simple__dev::p11

### `1256__wikitables_composition__dev`
_Refused._

### `809__wikidata_simple__dev`
> Albert Uderzo is best known for his work on the "Astérix" series. [alce::809__wikidata_simple__dev::p0]
> He also illustrated other comics such as "Oumpah-pah" in collaboration with René Goscinny. [alce::809__wikidata_simple__dev::p0]

Cited: alce::809__wikidata_simple__dev::p0

### `82__wikitables_composition__dev`
> The question asks about train stations in Birmingham, but the sources cover two different cities named Birmingham: Birmingham, Alabama (USA) and Birmingham, England (UK). I will provide information for both.

**Birmingham, England:**

The Birmingham station group consists of three railway stations in Birmingham city centre: New Street, Snow Hill, and Moor Street. [alce::82__wikitables_composition__dev::p3]
> Birmingham International is an international station located east of the city centre next to Birmingham Airport and the National Exhibition Centre. [alce::82__wikitables_composition__dev::p3]
> Five Ways is a railway station in the south west of the city centre with connections on the New Street to Redditch line. [alce::82__wikitables_composition__dev::p4]
> Jewellery Quarter is another railway station in central Birmingham. [alce::82__wikitables_composition__dev::p3]
> **Birmingham, Alabama:**

Birmingham station is a train station in Birmingham, Alabama that serves Amtrak's "Crescent" route. [alce::82__wikitables_composition__dev::p11]

Cited: alce::82__wikitables_composition__dev::p11, alce::82__wikitables_composition__dev::p3, alce::82__wikitables_composition__dev::p4

### `689__wikidata_simple__dev`
> Synapse Software published games for various computer systems. [alce::689__wikidata_simple__dev::p0]
> However, the sources also indicate that Synapse: The Electronic Music Magazine was a bi-monthly American magazine about synthesizers and electronic music published from March 1976 to June 1979. [alce::689__wikidata_simple__dev::p3]
> If the question is asking specifically about Synapse Software Corporation (the computer game company), the sources do not identify any written form of media they published—they are described as a game development and publishing company. If the question is asking about any entity named "Synapse," then **Synapse: The Electronic Music Magazine** was a written form of media published. [alce::689__wikidata_simple__dev::p3]

Cited: alce::689__wikidata_simple__dev::p0, alce::689__wikidata_simple__dev::p3

### `202__wikidata_comp__dev`
_Refused._

### `111__wikidata_intersection__dev`
> Ed Burns was co-screenwriter with David Simon on "The Corner" and "The Wire" (HBO). [alce::111__wikidata_intersection__dev::p1]

Cited: alce::111__wikidata_intersection__dev::p1

### `516__wikitables_simple__dev`
> WrestleCrap is a professional wrestling website created by R. D. Reynolds and Merle Vincent. [alce::516__wikitables_simple__dev::p2]
> The site is currently run by Reynolds, Blade Braxton and Justin Henry. [alce::516__wikitables_simple__dev::p2]
> Solowrestling.com is a professional wrestling news website that was created by Sebastián Martínez, one of WWE's Spanish-language commentators and former Impact Wrestling commentator. [alce::516__wikitables_simple__dev::p15]
> Earl Oliver launched Solie's Vintage Wrestling, a historical professional wrestling website, in 1995. [alce::516__wikitables_simple__dev::p11]

Cited: alce::516__wikitables_simple__dev::p11, alce::516__wikitables_simple__dev::p15, alce::516__wikitables_simple__dev::p2

### `645__wikidata_simple__dev`
> Javi Gracia is the head coach of Premier League club Watford. [alce::645__wikidata_simple__dev::p64]
> He was appointed as Head Coach on 21 January 2018 following Marco Silva's departure. [alce::645__wikidata_simple__dev::p0]

Cited: alce::645__wikidata_simple__dev::p0, alce::645__wikidata_simple__dev::p64

### `944__wikidata_simple__dev`
> Based on the provided sources, the Joint Institute for Nuclear Research has made more than 40 major discoveries. [alce::944__wikidata_simple__dev::p2]
> However, the sources do not specify which particular inventions or discoveries were made by JINR. The sources mention that the institute conducts research in theoretical physics, high energy physics, heavy ion physics, condensed matter physics, nuclear reactions, neutron physics, and information technology, [alce::944__wikidata_simple__dev::p1]
> but they do not identify specific inventions or discoveries by name.

Cited: alce::944__wikidata_simple__dev::p1, alce::944__wikidata_simple__dev::p2

### `6__wikitables_composition__dev`
> Malanje is a city located in the Angolan province of Malanje. [alce::6__wikitables_composition__dev::p3]
> It is the capital city of Malanje Province with a population of approximately 222,000. [alce::6__wikitables_composition__dev::p3]

Cited: alce::6__wikitables_composition__dev::p3

### `405__wikidata_comp__dev`
> Rouben Mamoulian directed a film that N. Richard Nash wrote for. [alce::405__wikidata_comp__dev::p96]
> Specifically, Nash wrote the screenplay for "Porgy and Bess" (1959), which was directed by Mamoulian. [alce::405__wikidata_comp__dev::p33]

Cited: alce::405__wikidata_comp__dev::p33, alce::405__wikidata_comp__dev::p96

### `464__wikidata_intersection__dev`
_Refused._

### `198__wikidata_intersection__dev`
> Thomas Walter Swan was a Judge of the United States Court of Appeals for the Second Circuit who worked for Yale Law School. [alce::198__wikidata_intersection__dev::p29]
> He became the Dean and a professor at Yale Law School in 1916, before being nominated to the Second Circuit in 1926. [alce::198__wikidata_intersection__dev::p29]
> Charles Edward Clark also served as a Judge of the United States Court of Appeals for the Second Circuit and was the Dean of Yale Law School from 1929 to 1939. [alce::198__wikidata_intersection__dev::p94]

Cited: alce::198__wikidata_intersection__dev::p29, alce::198__wikidata_intersection__dev::p94

### `634__wikidata_simple__dev`
> The National Panhellenic Conference (NPC) is an umbrella organization for 26 (inter)national women's sororities throughout the United States and Canada. [alce::634__wikidata_simple__dev::p0]
> While the sources do not name specific individual member sororities, they confirm that women's sororities are members of the NPC, though the particular names of these member organizations are not provided in the given source sentences.

Cited: alce::634__wikidata_simple__dev::p0

### `896__wikidata_simple__dev`
> August Derleth edited several written works, including:

"The Other Side of the Moon," an anthology of science fiction stories first published by Pellegrini & Cudahy in 1949. [alce::896__wikidata_simple__dev::p38]
> "Beyond Time and Space," an anthology of science fiction stories first published by Pellegrini & Cudahy in 1950. [alce::896__wikidata_simple__dev::p71]
> "Strange Ports of Call," an anthology of science fiction stories first published by Pellegrini & Cudahy in 1948. [alce::896__wikidata_simple__dev::p37]
> "The Outsider and Others" and "Beyond the Wall of Sleep," omnibus collections that Derleth co-edited with Wandrei. [alce::896__wikidata_simple__dev::p49]

Cited: alce::896__wikidata_simple__dev::p37, alce::896__wikidata_simple__dev::p38, alce::896__wikidata_simple__dev::p49, alce::896__wikidata_simple__dev::p71

### `161__wikidata_comp__dev`
> Sidney Franklin directed a movie that Norma Talmadge produced. [alce::161__wikidata_comp__dev::p16]
> Specifically, Franklin directed "Smilin' Through" (1922), which was produced by Talmadge and her husband Joseph M. Schenck for her company, the Norma Talmadge Film Corporation. [alce::161__wikidata_comp__dev::p16]

Cited: alce::161__wikidata_comp__dev::p16

### `122__wikidata_comp__dev`
> Organizations owned by Voice Media Group can be found in multiple cities across the United States. [alce::122__wikidata_comp__dev::p0]
> Specifically, Voice Media Group owns newspaper publications including "Denver Westword" in Denver, "Phoenix New Times" in Phoenix, "Houston Press" in Houston, "Dallas Observer" in Dallas, and "Miami New Times" and "Broward New Times" in the Miami area. [alce::122__wikidata_comp__dev::p0]
> Additionally, Voice Media Group operates a digital marketing agency called V Digital Services. [alce::122__wikidata_comp__dev::p1]

Cited: alce::122__wikidata_comp__dev::p0, alce::122__wikidata_comp__dev::p1

### `1354__wikidata_simple__dev`
> Montana has several indigenous languages. Crow is spoken by about 3,000 speakers in Montana. [alce::1354__wikidata_simple__dev::p0]
> Cheyenne is spoken by about 1,700 speakers in the state. [alce::1354__wikidata_simple__dev::p0]
> Blackfoot is spoken by about 100 speakers in Montana. [alce::1354__wikidata_simple__dev::p0]
> Salish (also known as Montana Salish) is spoken by about 64 elders of the Flathead Nation in north central Montana. [alce::1354__wikidata_simple__dev::p2]
> Kalispel-Pend d'Oreille is spoken by about 64 speakers in the state. [alce::1354__wikidata_simple__dev::p1]
> Assiniboine is spoken by about 150 speakers in Montana and Canada. [alce::1354__wikidata_simple__dev::p0]

Cited: alce::1354__wikidata_simple__dev::p0, alce::1354__wikidata_simple__dev::p1, alce::1354__wikidata_simple__dev::p2

### `321__wikidata_comp__dev`
> Several people have won the Indianapolis 500 competition:

Sam Hanks won the 1957 Indianapolis 500 in his thirteenth attempt. [alce::321__wikidata_comp__dev::p0]
> A. J. Foyt won the 1964 Indianapolis 500, which was his second of four Indy 500 victories. [alce::321__wikidata_comp__dev::p43]
> Dan Wheldon won the 2011 Indianapolis 500, which was his second victory in the race. [alce::321__wikidata_comp__dev::p85]
> Ryan Hunter-Reay won the 2014 Indianapolis 500. [alce::321__wikidata_comp__dev::p90]
> Will Power won the 2018 Indianapolis 500. [alce::321__wikidata_comp__dev::p23]

Cited: alce::321__wikidata_comp__dev::p0, alce::321__wikidata_comp__dev::p23, alce::321__wikidata_comp__dev::p43, alce::321__wikidata_comp__dev::p85, alce::321__wikidata_comp__dev::p90

### `301__wikidata_intersection__dev`
_Refused._

### `119__wikidata_comp__dev`
> Based on the provided sources, I can identify the following team that participated in a competition that Fitzroy FC won:

Brisbane Lions participated in a competition where Fitzroy won. Specifically, Fitzroy United defeated Brisbane Lions 4-1 in a match played at the Brunswick Street Oval on 2 May 1977. [alce::119__wikidata_comp__dev::p55]
> Additionally, the Collingwood Magpies met the Brisbane Lions in the AFL Heritage Round of 2003, at which the Fitzroy Reds played the curtain-raiser at the MCG. [alce::119__wikidata_comp__dev::p7]
> However, if the question is asking specifically about teams that competed against Fitzroy in competitions that Fitzroy won, the most direct answer is: **Brisbane Lions** competed against Fitzroy United in 1977, which Fitzroy won 4-1. [alce::119__wikidata_comp__dev::p55]

Cited: alce::119__wikidata_comp__dev::p55, alce::119__wikidata_comp__dev::p7

### `668__wikidata_simple__dev`
> Based on the provided sources, pickling is used to create two different types of objects:

1. Pickling (as a metal surface treatment) is used to clean and prepare metal objects such as ferrous metals, copper, precious metals, and aluminum alloys for further processing or use. [alce::668__wikidata_simple__dev::p4]
> 2. Pickling salt is used mainly for canning and manufacturing pickles. [alce::668__wikidata_simple__dev::p36]

Cited: alce::668__wikidata_simple__dev::p36, alce::668__wikidata_simple__dev::p4

### `805__wikidata_simple__dev`
> Several people were coaches of Weymouth F.C.:

Andy Tillson was appointed as Weymouth's Assistant Manager following Team Bath's disbandment at the end of the 2008/9 season. [alce::805__wikidata_simple__dev::p79]
> John Hollins took over as manager of Weymouth in January 2008. [alce::805__wikidata_simple__dev::p44]
> Gill was appointed manager of Weymouth in January 2010, though he resigned 44 days later. [alce::805__wikidata_simple__dev::p11]
> Mark Molesley is the current first team manager of Weymouth F.C. [alce::805__wikidata_simple__dev::p0]

Cited: alce::805__wikidata_simple__dev::p0, alce::805__wikidata_simple__dev::p11, alce::805__wikidata_simple__dev::p44, alce::805__wikidata_simple__dev::p79

### `284__wikidata_intersection__dev`
> Manchester City competed in multiple FA Cup Finals. They won the 1904 FA Cup Final, defeating Bolton Wanderers 1–0 with a goal by Billy Meredith. [alce::284__wikidata_intersection__dev::p0]
> They also won the 1934 FA Cup Final, defeating Portsmouth 2–1. [alce::284__wikidata_intersection__dev::p48]
> Manchester City reached the 2011 FA Cup Final, their first major final in over thirty years, and defeated Stoke City 1–0. [alce::284__wikidata_intersection__dev::p63]
> Additionally, Manchester City competed in the 2013 FA Cup Final against Wigan Athletic on 11 May 2013 at Wembley Stadium, which was Manchester City's 10th FA Cup final. [alce::284__wikidata_intersection__dev::p28]

Cited: alce::284__wikidata_intersection__dev::p0, alce::284__wikidata_intersection__dev::p28, alce::284__wikidata_intersection__dev::p48, alce::284__wikidata_intersection__dev::p63

### `595__wikidata_simple__dev`
> Shonda Rhimes was executive producer for several television series. She is best known as the showrunner—creator, head writer, and executive producer—of "Grey's Anatomy", its spin-off "Private Practice", and the political thriller series "Scandal". [alce::595__wikidata_simple__dev::p1]
> She has also served as the executive producer of the ABC television series "Off the Map", "How to Get Away with Murder", and "The Catch". [alce::595__wikidata_simple__dev::p1]

Cited: alce::595__wikidata_simple__dev::p1

### `369__wikidata_comp__dev`
> Laura Denvir Stith, a Supreme Court of Missouri justice, attended John Burroughs School, a private school in metro St. Louis, Missouri, for her secondary education. [alce::369__wikidata_comp__dev::p3]
> She then graduated from Jackson College for Women (now part of Tufts University) in 1975 and from Georgetown University Law Center in 1978. [alce::369__wikidata_comp__dev::p3]
> W. Brent Powell, another Supreme Court of Missouri justice, received his undergraduate degree from William Jewell College and his Juris Doctor from the University of Missouri School of Law in 1996. [alce::369__wikidata_comp__dev::p4]
> Michael A. Wolff, a former Chief Justice of the Supreme Court of Missouri, earned his undergraduate degree from Dartmouth College and his law degree from the University of Minnesota Law School. [alce::369__wikidata_comp__dev::p32]

Cited: alce::369__wikidata_comp__dev::p3, alce::369__wikidata_comp__dev::p32, alce::369__wikidata_comp__dev::p4

### `852__wikidata_simple__dev`
> Based on the provided sources, several pieces of literature featured drawings by Lewis Trondheim:

"La Mouche" ("The Fly") is a work for which Trondheim created drawings, first for the Japanese market and then redrew a French version from scratch. [alce::852__wikidata_simple__dev::p11]
> "Dungeon" (in French, "Donjon") is an ambitious series which Trondheim created with drawings. [alce::852__wikidata_simple__dev::p11]
> "The Spiffy Adventures of McConey" (originally "Les formidables aventures de Lapinot") is a work featuring Trondheim's drawings, with an initial 500 page graphic novel titled "Lapinot et les carottes de Patagonie." [alce::852__wikidata_simple__dev::p3]

Cited: alce::852__wikidata_simple__dev::p11, alce::852__wikidata_simple__dev::p3

### `729__wikidata_simple__dev`
> Desolation Wilderness contains alpine and wooded lakes of various sizes scattered throughout the area. [alce::729__wikidata_simple__dev::p1]
> It features steep canyons of the Mokelumne, Cosumnes, American, and Rubicon rivers, with plateaus of generally moderate relief located between these canyons. [alce::729__wikidata_simple__dev::p5]
> The wilderness has much barren rocky terrain at the edge of the tree line and extensive areas of bare granite rock formations. [alce::729__wikidata_simple__dev::p3]
> It supports predominantly red fir and lodgepole pine forests with associated species such as Jeffrey pine, mountain hemlock, ponderosa pine, western juniper, and western white pine. [alce::729__wikidata_simple__dev::p4]

Cited: alce::729__wikidata_simple__dev::p1, alce::729__wikidata_simple__dev::p3, alce::729__wikidata_simple__dev::p4, alce::729__wikidata_simple__dev::p5

### `659__wikidata_simple__dev`
_Refused._

### `208__wikidata_comp__dev`
_Refused._

### `419__wikidata_comp__dev`
_Refused._

### `898__wikidata_simple__dev`
_Refused._

### `963__wikidata_comp__dev`
> Several California Supreme Court members attended different schools:

Leondra Kruger attended Polytechnic School in Pasadena, California, and earned a Bachelor of Arts degree from Harvard University before graduating with a Juris Doctor degree from Yale Law School. [alce::963__wikidata_comp__dev::p89]
> Kathryn Werdegar earned her B.A. at the University of California, Berkeley and attended the University of California, Berkeley School of Law (Boalt Hall). [alce::963__wikidata_comp__dev::p15]
> Carol Corrigan graduated from Saint Mary's High School in Stockton and attended Holy Names College in Oakland. [alce::963__wikidata_comp__dev::p60]
> Raymond L. Sullivan graduated from St. Ignatius High School and was educated at St. Ignatius College, which was renamed the University of San Francisco. [alce::963__wikidata_comp__dev::p21]

Cited: alce::963__wikidata_comp__dev::p15, alce::963__wikidata_comp__dev::p21, alce::963__wikidata_comp__dev::p60, alce::963__wikidata_comp__dev::p89

### `49__wikitables_composition__dev`
_Refused._

### `695__wikidata_simple__dev`
_Refused._

### `637__wikidata_simple__dev`
> The sources mention several Mayors of Boston across different time periods:

Kevin White was Mayor of Boston from 1968 to 1984, serving four terms amounting to 16 years. [alce::637__wikidata_simple__dev::p5]
> John Frederick Collins was the mayor of Boston from 1960 to 1968. [alce::637__wikidata_simple__dev::p34]
> Daniel Aloysius Whelton was an American political figure who became mayor of Boston. [alce::637__wikidata_simple__dev::p40]
> The current mayor is Martin J. "Marty" Walsh. [alce::637__wikidata_simple__dev::p0]

Cited: alce::637__wikidata_simple__dev::p0, alce::637__wikidata_simple__dev::p34, alce::637__wikidata_simple__dev::p40, alce::637__wikidata_simple__dev::p5

### `793__wikidata_simple__dev`
> Based on the provided sources, Marshall had Lakota as his mother tongue. [alce::793__wikidata_simple__dev::p18]
> He was raised in a traditional Lakota household by his maternal grandparents, where his first language was Lakota, and he later learned English as a second language. [alce::793__wikidata_simple__dev::p18]

Cited: alce::793__wikidata_simple__dev::p18

### `272__wikidata_intersection__dev`
> "Kadal" is a movie that Mani Ratnam screen wrote and A. R. Rahman composed the music for. [alce::272__wikidata_intersection__dev::p2]

Cited: alce::272__wikidata_intersection__dev::p2

### `1251__wikitables_composition__dev`
_Refused._

### `588__wikidata_simple__dev`
> Many species were discovered in the Morrison Formation. Dinosaurs known from the Morrison Formation include the theropods "Allosaurus", "Ceratosaurus", "Ornitholestes", "Saurophaganax", and "Torvosaurus"; the sauropods "Brontosaurus", "Brachiosaurus", "Camarasaurus", and "Diplodocus"; and the ornithischians "Camptosaurus", "Dryosaurus", and "Stegosaurus". [alce::588__wikidata_simple__dev::p67]
> Additionally, other fossils discovered in the Morrison Formation include green algae, fungi, mosses, horsetails, ferns, cycads, ginkgoes, conifers, bivalves, snails, ray-finned fishes, frogs, salamanders, turtles, sphenodonts, lizards, crocodylomorphans, pterosaurs, and early mammals such as docodonts, multituberculates, symmetrodonts, and triconodonts. [alce::588__wikidata_simple__dev::p1]
> The genus Ctenacodon, an extinct mammal, was also discovered in the Morrison Formation. [alce::588__wikidata_simple__dev::p54]

Cited: alce::588__wikidata_simple__dev::p1, alce::588__wikidata_simple__dev::p54, alce::588__wikidata_simple__dev::p67

### `422__wikidata_intersection__dev`
_Refused._

### `911__wikidata_simple__dev`
_Refused._

### `40__wikitables_composition__dev`
> Based on the provided sources, the following companies are producing modern armament in Pakistan:

Pakistan Ordnance Factories (POF) is a major firearms and defence contractor that produces conventional arms and ammunition to international standards. [alce::40__wikitables_composition__dev::p15]
> POF produces approximately 70 major products for the Army, Navy and Air Force, including automatic rifles, machine guns, mortars, artillery ammunition, aircraft ammunition, anti-aircraft ammunition, tank ammunition, anti-tank ammunition, bombs, grenades, land mines, and pyrotechnics. [alce::40__wikitables_composition__dev::p5]
> Heavy Industries Taxila and Pakistan Aeronautical Complex are enterprises established to produce modern armament, developed with assistance from the People's Republic of China and European defence companies. [alce::40__wikitables_composition__dev::p18]
> Pakistan Hunting & Sporting Arms Development Company (PHSADC) is a sector development company involved in armament production. [alce::40__wikitables_composition__dev::p29]

Cited: alce::40__wikitables_composition__dev::p15, alce::40__wikitables_composition__dev::p18, alce::40__wikitables_composition__dev::p29, alce::40__wikitables_composition__dev::p5

### `341__wikidata_comp__dev`
> Sir William Martin, the first Chief Justice of New Zealand, was educated at King Edward VI Grammar School, Eton, and St John's College, Cambridge. [alce::341__wikidata_comp__dev::p13]
> Dame Sian Elias, the 12th and current Chief Justice of New Zealand, attended Diocesan School for Girls in Auckland and completed a law degree from the University of Auckland. [alce::341__wikidata_comp__dev::p95]
> Sir Humphrey Francis O'Leary, the seventh Chief Justice of New Zealand, attended Masterton Public school and state schools. [alce::341__wikidata_comp__dev::p67]

Cited: alce::341__wikidata_comp__dev::p13, alce::341__wikidata_comp__dev::p67, alce::341__wikidata_comp__dev::p95

### `565__wikidata_simple__dev`
> Independence Paragliding is known for manufacturing paragliders in the form of ready-to-fly aircraft as well as reserve parachutes, harnesses and paragliding accessories. [alce::565__wikidata_simple__dev::p1]
> The company's line of aircraft in the mid-2000s included the Akron intermediate glider, the Avalon beginner glider, the Dragon intermediate glider, and the Raptor competition glider. [alce::565__wikidata_simple__dev::p1]
> The company also sold a two-place glider for flight training called the Speed Tandem. [alce::565__wikidata_simple__dev::p0]

Cited: alce::565__wikidata_simple__dev::p0, alce::565__wikidata_simple__dev::p1

### `900__wikidata_simple__dev`
> Adam Sandler served as executive producer for "Deuce Bigalow: Male Gigalo." [alce::900__wikidata_simple__dev::p20]

Cited: alce::900__wikidata_simple__dev::p20

### `251__wikidata_comp__dev`
> Dan Gilroy directed the movie that was written by Frank D. Gilroy. [alce::251__wikidata_comp__dev::p24]
> However, I should clarify: the sources indicate that Dan Gilroy is Frank D. Gilroy's son, and Dan Gilroy wrote and directed "Nightcrawler" (2014). [alce::251__wikidata_comp__dev::p2]
> The sources do not explicitly state that Frank D.
> Gilroy wrote a movie that Dan Gilroy directed.
> The source mentioning Frank D.
> Gilroy wanting to direct a film discusses him consulting with his brother Tony Gilroy, but does not clearly identify which specific film Frank D.
> Gilroy wrote that was directed by one of his sons.
> Based on the available sources, I cannot definitively answer which movie Frank D.
> Gilroy wrote that was then directed by someone else, as the sources do not clearly establish this relationship.

Cited: alce::251__wikidata_comp__dev::p2, alce::251__wikidata_comp__dev::p24

### `742__wikidata_simple__dev`
> Psikyo published several video games, including the "Aero Fighters" series. [alce::742__wikidata_simple__dev::p0]
> Psikyo was also known for developing vertically scrolling shoot 'em ups and erotic mahjong games. [alce::742__wikidata_simple__dev::p0]
> Additionally, Psikyo published "Sengoku Ace" and "Sengoku Blade." [alce::742__wikidata_simple__dev::p5]

Cited: alce::742__wikidata_simple__dev::p0, alce::742__wikidata_simple__dev::p5

### `557__wikidata_simple__dev`
> The Detroit Red Wings won the Stanley Cup. [alce::557__wikidata_simple__dev::p15]
> They won it eleven times, more than any other American team in NHL history. [alce::557__wikidata_simple__dev::p15]
> Their first two Stanley Cup titles were won in 1936 and 1937. [alce::557__wikidata_simple__dev::p15]
> With owner Mike Ilitch, the Wings won the Cup in 1997, 1998, 2002, and 2008. [alce::557__wikidata_simple__dev::p63]

Cited: alce::557__wikidata_simple__dev::p15, alce::557__wikidata_simple__dev::p63

### `177__wikidata_intersection__dev`
> Raquel Atawo and Abigail Spears won multiple team sports events in tennis doubles. They won the 2012 Toray Pan Pacific Open [alce::177__wikidata_intersection__dev::p2]
> and the 2014 Cincinnati Masters [alce::177__wikidata_intersection__dev::p1]
> . They also won titles at Carlsbad, Seoul, Tokyo, and Osaka in 2012 [alce::177__wikidata_intersection__dev::p3]
> . Additionally, they won the Western & Southern Open [alce::177__wikidata_intersection__dev::p0]
> and the Aegon Classic [alce::177__wikidata_intersection__dev::p0]
> .

Cited: alce::177__wikidata_intersection__dev::p0, alce::177__wikidata_intersection__dev::p1, alce::177__wikidata_intersection__dev::p2, alce::177__wikidata_intersection__dev::p3

### `920__wikidata_simple__dev`
> Jerry Cantrell was a member of Alice in Chains, serving as guitarist and vocalist. [alce::920__wikidata_simple__dev::p0]
> Sean Kinney was a member as drummer. [alce::920__wikidata_simple__dev::p0]
> Mike Starr was a member as bassist. [alce::920__wikidata_simple__dev::p0]
> Layne Staley was a member as lead vocalist. [alce::920__wikidata_simple__dev::p0]
> Mike Inez replaced Mike Starr as bassist in 1993. [alce::920__wikidata_simple__dev::p0]
> William DuVall joined the band in 2006 as co-lead vocalist and rhythm guitarist. [alce::920__wikidata_simple__dev::p0]

Cited: alce::920__wikidata_simple__dev::p0

### `391__wikidata_intersection__dev`
_Refused._

### `1355__wikidata_simple__dev`
> FedEx served as sponsor of multiple sporting events. FedEx was the title sponsor of the Orange Bowl, a college football bowl game, beginning in 1990 and continuing as the longest continuous sponsor of any bowl game until ending its sponsorship. [alce::1355__wikidata_simple__dev::p1]
> FedEx also sponsored the Joe Gibbs NASCAR racing team. [alce::1355__wikidata_simple__dev::p79]
> Additionally, FedEx sponsored the FedEx St. Jude Classic, a professional golf tournament held annually on the PGA Tour from 1958 through 2018 in Memphis, Tennessee. [alce::1355__wikidata_simple__dev::p64]

Cited: alce::1355__wikidata_simple__dev::p1, alce::1355__wikidata_simple__dev::p64, alce::1355__wikidata_simple__dev::p79

### `309__wikidata_intersection__dev`
> The FA Cup Final events that featured Aston Villa F.C. were football matches. [alce::309__wikidata_intersection__dev::p63]
> The sources describe multiple FA Cup Finals involving Aston Villa, which were association football competitions—specifically the Football Association Challenge Cup, more usually known as the FA Cup. [alce::309__wikidata_intersection__dev::p25]

Cited: alce::309__wikidata_intersection__dev::p25, alce::309__wikidata_intersection__dev::p63

### `335__wikidata_comp__dev`
_Refused._

### `615__wikidata_simple__dev`
> Several manuscripts were created in the Konbaung Dynasty:

"Hmannan Yazawin" (1832) was produced by the Royal Historical Commission of the Konbaung Dynasty. [alce::615__wikidata_simple__dev::p2]
> "Dutiya Yazawin" (1869) was also produced by the Royal Historical Commission of the Konbaung Dynasty. [alce::615__wikidata_simple__dev::p2]
> "Konbaung Set Maha Yazawindawgyi" (the "Chronicle of Konbaung Dynasty") is the last and unofficial royal chronicle of Burma, covering the Konbaung Dynasty and first published in 1905. [alce::615__wikidata_simple__dev::p3]

Cited: alce::615__wikidata_simple__dev::p2, alce::615__wikidata_simple__dev::p3

### `597__wikidata_simple__dev`
_Refused._

### `945__wikidata_simple__dev`
> Lee Rose is employed as a lighting designer. [alce::945__wikidata_simple__dev::p60]
> Peter Barnes is employed as a lighting designer, lighting director, show producer and set designer. [alce::945__wikidata_simple__dev::p87]
> Peter Mumford is employed as an international lighting designer. [alce::945__wikidata_simple__dev::p86]

Cited: alce::945__wikidata_simple__dev::p60, alce::945__wikidata_simple__dev::p86, alce::945__wikidata_simple__dev::p87

### `318__wikidata_intersection__dev`
> Based on the provided sources, there are multiple matches between Burnley F.C. and Manchester City F.C.:

1. A Lancashire Senior Cup semi-final match on 9 May 1921, which ended in a 0–2 defeat for Burnley. [alce::318__wikidata_intersection__dev::p2]
> 2. A league fixture on 4 September 1920 at Hyde Road, where Burnley lost 0–3 to Manchester City. [alce::318__wikidata_intersection__dev::p1]
> 3. A league match on the last day of the 1959–60 season at Maine Road, Manchester, where Burnley won 2–1 against Manchester City with goals from Brian Pilkington and Trevor Meredith, clinching the championship. [alce::318__wikidata_intersection__dev::p15]

Cited: alce::318__wikidata_intersection__dev::p1, alce::318__wikidata_intersection__dev::p15, alce::318__wikidata_intersection__dev::p2

### `22__wikitables_composition__dev`
> Francisco José Lombardi directed two Peruvian films that were submitted for the Academy Awards for Best Foreign Language Film:

1. "Fallen from Heaven" (1990) was selected as the Peruvian entry for the Best Foreign Language Film at the 63rd Academy Awards. [alce::22__wikitables_composition__dev::p19]
> 2. "Captain Pantoja and the Special Services" (2000) was chosen as Peru's official Best Foreign Language Film submission at the 72nd Academy Awards. [alce::22__wikitables_composition__dev::p7]

Cited: alce::22__wikitables_composition__dev::p19, alce::22__wikitables_composition__dev::p7

### `766__wikidata_simple__dev`
> Cape Town is associated with the Cape Peninsula. [alce::766__wikidata_simple__dev::p22]
> Cape Town is also associated with Table Mountain, which influences the city's urban geography. [alce::766__wikidata_simple__dev::p22]
> Additionally, Cape Town is associated with Table Bay, which borders the City Bowl area. [alce::766__wikidata_simple__dev::p19]

Cited: alce::766__wikidata_simple__dev::p19, alce::766__wikidata_simple__dev::p22

### `1356__wikidata_simple__dev`
> "Blame It on the Bossa Nova" is a Bossa Nova song written by Cynthia Weil (lyrics) and Barry Mann, which was a 1963 hit single for Eydie Gormé. [alce::1356__wikidata_simple__dev::p32]

Cited: alce::1356__wikidata_simple__dev::p32

### `600__wikidata_simple__dev`
> # Jukebox Musicals

Early examples of jukebox musicals include "Jam Session," "An American in Paris" (1951), "Rock, Rock, Rock" (1956), "Rock Around the Clock" (1956), and "Juke Box Rhythm" (1959). [alce::600__wikidata_simple__dev::p0]
> "Buddy – The Buddy Holly Story" is a jukebox musical about the life of Buddy Holly that ran in the West End for 13 years from 1989 to 2003. [alce::600__wikidata_simple__dev::p4]
> "Mamma Mia!" is a jukebox musical built around the music of ABBA. [alce::600__wikidata_simple__dev::p3]
> "Tommy" and "The Wall" are jukebox musicals that adapted the entire song cycle from a single album by The Who and Pink Floyd, respectively. [alce::600__wikidata_simple__dev::p4]
> More recent jukebox musicals include "Movin' Out" (2002, based on Billy Joel's music), "Jersey Boys" (2006, featuring The Four Seasons), and "Rock of Ages" (2009, featuring classic rock of the 1980s). [alce::600__wikidata_simple__dev::p6]
> Other jukebox musicals include "Our House" (2002, based on the songs of Madness) and "We Will Rock You" (2002, based on the music of Queen). [alce::600__wikidata_simple__dev::p6]
> "Lennon" and "Good Vibrations" are jukebox musicals that have been critical and financial flops. [alce::600__wikidata_simple__dev::p3]

Cited: alce::600__wikidata_simple__dev::p0, alce::600__wikidata_simple__dev::p3, alce::600__wikidata_simple__dev::p4, alce::600__wikidata_simple__dev::p6

### `237__wikidata_comp__dev`
> Farren Blackburn was the director of "Shut In" (2016), a film penned by Christina Hodson. [alce::237__wikidata_comp__dev::p2]
> Travis Knight was the director of "Bumblebee" (2018), another film written by Christina Hodson. [alce::237__wikidata_comp__dev::p0]
> Denise Di Novi directed "Unforgettable" (2017), which Christina Hodson co-wrote. [alce::237__wikidata_comp__dev::p0]

Cited: alce::237__wikidata_comp__dev::p0, alce::237__wikidata_comp__dev::p2

### `549__wikitables_simple__dev`
_Refused._

### `109__wikidata_comp__dev`
_Refused._

### `734__wikidata_simple__dev`
> Ashleigh Barty was victorious in the 2018 US Open in doubles, winning the Grand Slam title with partner CoCo Vandeweghe. [alce::734__wikidata_simple__dev::p1]
> She also won the Nottingham Open on grass, defeating Johanna Konta in the final. [alce::734__wikidata_simple__dev::p2]

Cited: alce::734__wikidata_simple__dev::p1, alce::734__wikidata_simple__dev::p2

### `482__wikitables_simple__dev`
> Based on the provided sources, here are geothermal power stations with a capacity of at least 10 MW:

The Hatchōbaru Geothermal Power Plant in Ōita Prefecture, Japan has a total capacity of 112 MW, making it the largest geothermal power plant in the country. [alce::482__wikitables_simple__dev::p15]
> The Corbetti Geothermal Power Station and Tulu Moye Geothermal Power Station are both in the exploration phase with a combined capacity of approximately 500 megawatts. [alce::482__wikitables_simple__dev::p13]
> A geothermal power station with a 35 MW unit was put in operation, and a second 35 MW unit was installed in 1989. [alce::482__wikitables_simple__dev::p64]
> Ram Power operates the 10 MW San Jacinto Tizate geothermal plant. [alce::482__wikitables_simple__dev::p64]

Cited: alce::482__wikitables_simple__dev::p13, alce::482__wikitables_simple__dev::p15, alce::482__wikitables_simple__dev::p64

### `696__wikidata_simple__dev`
> Sydney Trains operated multiple railway stations. [alce::696__wikidata_simple__dev::p41]
> Specific examples include Campsie railway station, located on the Bankstown line serving the Sydney suburb of Campsie and served by Sydney Trains T3 Bankstown line services. [alce::696__wikidata_simple__dev::p55]
> Another example is Sydney Domestic Airport railway station, located on the Airport Link and operated by Sydney Trains with T8 Airport & South line services. [alce::696__wikidata_simple__dev::p65]
> St James railway station is also operated by Sydney Trains on the City Circle. [alce::696__wikidata_simple__dev::p75]

Cited: alce::696__wikidata_simple__dev::p41, alce::696__wikidata_simple__dev::p55, alce::696__wikidata_simple__dev::p65, alce::696__wikidata_simple__dev::p75

### `222__wikidata_intersection__dev`
_Refused._

### `621__wikidata_simple__dev`
> Leslie S. Hiscott directed "Alibi" (1931), the first ever depiction of Hercule Poirot, Agatha Christie's Belgian detective, with Austin Trevor in the lead role. [alce::621__wikidata_simple__dev::p1]
> He also directed "Black Coffee" (also 1931), a follow-up also starring Trevor. [alce::621__wikidata_simple__dev::p1]

Cited: alce::621__wikidata_simple__dev::p1

### `459__wikidata_intersection__dev`
> Jessie Carney Smith is a Fisk University employee and alumni. She is currently serving as Dean of the Fisk University Library and Camille Cosby Distinguished Chair in the Humanities. [alce::459__wikidata_intersection__dev::p89]
> James Raymond Lawson is also a Fisk University employee and alumni. He graduated from Fisk University with a bachelor's degree in Physics in 1935 and later served as president of Fisk University from 1967 to 1975. [alce::459__wikidata_intersection__dev::p52]

Cited: alce::459__wikidata_intersection__dev::p52, alce::459__wikidata_intersection__dev::p89

### `116__wikidata_comp__dev`
_Refused._

### `703__wikidata_simple__dev`
> The Volvo XC60 is a model automobile that belongs to the Volvo Cars brand. [alce::703__wikidata_simple__dev::p27]
> It is a compact luxury crossover SUV that has been manufactured and marketed by Volvo Cars since 2008. [alce::703__wikidata_simple__dev::p27]

Cited: alce::703__wikidata_simple__dev::p27

### `394__wikidata_intersection__dev`
> Based on the provided sources, several films were both produced and directed by Emeric Pressburger in collaboration with Michael Powell. These include "49th Parallel" (1941), "The Life and Death of Colonel Blimp" (1943), "A Matter of Life and Death" (1946), "Black Narcissus" (1947), "The Red Shoes" (1948), and "The Tales of Hoffmann" (1951). [alce::394__wikidata_intersection__dev::p1]
> The films were jointly credited as "Written, Produced and Directed by Michael Powell and Emeric Pressburger." [alce::394__wikidata_intersection__dev::p16]

Cited: alce::394__wikidata_intersection__dev::p1, alce::394__wikidata_intersection__dev::p16

### `238__wikidata_intersection__dev`
> Based on the provided sources, I can identify a specific Oscar Micheaux production that was penned by Micheaux himself.

The film with the working title "The Ghost of Tolston's Manor" was produced by Oscar Micheaux and had its scenario written by Oscar Micheaux. [alce::238__wikidata_intersection__dev::p27]
> Additionally, the sources indicate that Micheaux advertised that his films were "scripted and produced exclusively by African Americans," which would include Micheaux himself as the writer and producer of his productions. [alce::238__wikidata_intersection__dev::p12]

Cited: alce::238__wikidata_intersection__dev::p12, alce::238__wikidata_intersection__dev::p27

### `537__wikitables_simple__dev`
> Several professional wrestling organizations own streaming services:

The WWE owns WWE Network, a subscription-based video streaming service. [alce::537__wikitables_simple__dev::p2]
> New Japan Pro-Wrestling owns New Japan Pro-Wrestling World, a subscription-based video streaming service. [alce::537__wikitables_simple__dev::p7]
> Ring of Honor owns Honor Club, an OTT streaming service. [alce::537__wikitables_simple__dev::p95]
> Anthem Wrestling Exhibitions, a subsidiary of Anthem Sports & Entertainment and parent company of Impact Wrestling, owns Global Wrestling Network (GWN), a video streaming service. [alce::537__wikitables_simple__dev::p14]

Cited: alce::537__wikitables_simple__dev::p14, alce::537__wikitables_simple__dev::p2, alce::537__wikitables_simple__dev::p7, alce::537__wikitables_simple__dev::p95

### `502__wikitables_simple__dev`
_Refused._

### `559__wikidata_simple__dev`
> Joseph L. Mankiewicz produced "The Philadelphia Story," which was nominated for the Academy Award for Best Picture in 1941. [alce::559__wikidata_simple__dev::p2]
> He also produced "The Keys of" (a film whose full title is not completed in the sources). [alce::559__wikidata_simple__dev::p2]

Cited: alce::559__wikidata_simple__dev::p2

### `1357__wikidata_simple__dev`
> The Miami Dolphins compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) East division. [alce::1357__wikidata_simple__dev::p0]
> They began play in the AFL in 1966. [alce::1357__wikidata_simple__dev::p0]
> Additionally, the team participated in the 2012 season of "Hard Knocks." [alce::1357__wikidata_simple__dev::p78]

Cited: alce::1357__wikidata_simple__dev::p0, alce::1357__wikidata_simple__dev::p78

### `425__wikidata_intersection__dev`
> Philip Yordan wrote several films that Anthony Mann directed. "The Man from Laramie" (1955) was written by Yordan for James Stewart and director Anthony Mann. [alce::425__wikidata_intersection__dev::p39]
> Additionally, Yordan wrote "Men in War" (1957) for director Mann. [alce::425__wikidata_intersection__dev::p20]
> Mann also directed "El Cid" (1961), a medieval epic written by Yordan. [alce::425__wikidata_intersection__dev::p11]

Cited: alce::425__wikidata_intersection__dev::p11, alce::425__wikidata_intersection__dev::p20, alce::425__wikidata_intersection__dev::p39

### `327__wikidata_comp__dev`
_Refused._

### `181__wikidata_intersection__dev`
> Lewis Hamilton won the 2014 Japanese Grand Prix. [alce::181__wikidata_intersection__dev::p0]
> The race was held on 5 October 2014 at the Suzuka Circuit in Suzuka, Mie, and was the fifteenth race of the 2014 FIA Formula One World Championship. [alce::181__wikidata_intersection__dev::p0]

Cited: alce::181__wikidata_intersection__dev::p0

### `554__wikidata_simple__dev`
> Based on the provided sources, Boudleaux Bryant composed the following songs:

"Love Hurts" [alce::554__wikidata_simple__dev::p0]
> "All I Have to Do Is Dream" [alce::554__wikidata_simple__dev::p0]
> He also co-wrote "Rocky Top," "Bye Bye Love," and "Wake Up Little Susie" with his wife Felice Bryant [alce::554__wikidata_simple__dev::p0]

Cited: alce::554__wikidata_simple__dev::p0

### `477__wikitables_simple__dev`
> Based on the provided sources, the following hormones are found in Homo sapiens:

Epinephrine, norepinephrine, adrenocorticotropic hormone (ACTH), glucagon, and thyroxine are released by the thyroid and adrenal glands. [alce::477__wikitables_simple__dev::p1]
> Testosterone is produced by the fetal testis and is present in the human brain and body. [alce::477__wikitables_simple__dev::p62]
> Estrogen is produced in the brain through the conversion of testosterone by the enzyme aromatase, and estradiol is also present in humans. [alce::477__wikitables_simple__dev::p62]
> Follicle stimulating hormone, luteinising hormone, and estradiol are hormones found in humans, with evidence suggesting they may be present in semen. [alce::477__wikitables_simple__dev::p81]

Cited: alce::477__wikitables_simple__dev::p1, alce::477__wikitables_simple__dev::p62, alce::477__wikitables_simple__dev::p81

### `307__wikidata_intersection__dev`
> The St. Louis Cardinals participated in the World Series and were ultimate victors, winning 11 World Series championships. [alce::307__wikidata_intersection__dev::p2]

Cited: alce::307__wikidata_intersection__dev::p2

### `604__wikidata_simple__dev`
> The sources provided describe synesthesia as a neurological condition and mention specific individuals who experience it, but they do not identify a single person as being "the" person afflicted by synesthesia in a way that would suggest one particular historical figure.

However, the sources do mention several people who experience synesthesia: Pharrell Williams experiences synesthesia and used it as the basis of the album "Seeing Sounds" [alce::604__wikidata_simple__dev::p31]
> . Singer/songwriter Marina and the Diamonds experiences music → color synesthesia and reports colored days of the week [alce::604__wikidata_simple__dev::p31]
> .
> If you are asking about a specific historical figure or have answer options to choose from, please provide those details and I can give you a more precise answer.

Cited: alce::604__wikidata_simple__dev::p31

### `1006__wikidata_comp__dev`
> Robert C. Merton, a Nobel Prize-winning economist and co-founder of Long-Term Capital Management, was a professor at the MIT Sloan School of Management. [alce::1006__wikidata_comp__dev::p53]
> Additionally, one LTCM employee, Haghani, received a B.Sc. degree in finance and taught at the LSE (London School of Economics), where he was a Senior Research Associate. [alce::1006__wikidata_comp__dev::p23]

Cited: alce::1006__wikidata_comp__dev::p23, alce::1006__wikidata_comp__dev::p53

### `1103__wikidata_intersection__dev`
> Manchester United F.C. and Manchester City F.C. participated together in the Manchester derby, which refers to football matches between the two clubs. [alce::1103__wikidata_intersection__dev::p4]
> These fixtures are played in the Premier League. [alce::1103__wikidata_intersection__dev::p60]
> The two teams have played 177 matches in all competitions. [alce::1103__wikidata_intersection__dev::p4]

Cited: alce::1103__wikidata_intersection__dev::p4, alce::1103__wikidata_intersection__dev::p60

### `1253__wikitables_composition__dev`
> Based on the provided sources, the following volcanic complexes are located in Argentina:

1. Tastil volcanic complex is a volcanic complex in Argentina. [alce::1253__wikitables_composition__dev::p28]
> 2. Pairique volcanic complex is a volcanic complex in the Jujuy Province, Argentina. [alce::1253__wikitables_composition__dev::p43]
> 3. Rincon volcanic complex is a volcano in Argentina. [alce::1253__wikitables_composition__dev::p1]

Cited: alce::1253__wikitables_composition__dev::p1, alce::1253__wikitables_composition__dev::p28, alce::1253__wikitables_composition__dev::p43

### `55__wikitables_composition__dev`
_Refused._

### `889__wikidata_simple__dev`
_Refused._

### `17__wikitables_composition__dev`
> There are two radio stations licensed to broadcast in Lancaster, California with different identifiers:

KOSS is a radio station licensed to Lancaster, California. [alce::17__wikitables_composition__dev::p95]
> KFXM-LP is a radio station licensed to Lancaster, California. [alce::17__wikitables_composition__dev::p4]

Cited: alce::17__wikitables_composition__dev::p4, alce::17__wikitables_composition__dev::p95

### `70__wikitables_composition__dev`
_Refused._

### `849__wikidata_simple__dev`
_Refused._

### `513__wikitables_simple__dev`
> Based on the provided sources, the tunnels with a length larger than 13 km are:

The Arlberg Road Tunnel, with a length of 13,976 metres (approximately 14 km). [alce::513__wikitables_simple__dev::p17]
> The Kresna Gorge Tunnel, which was planned to have a length of over 15 km. [alce::513__wikitables_simple__dev::p18]
> Additionally, one tunnel system mentioned has a total of about 19 km of tunnel length (main and escape tubes plus cross passages combined). [alce::513__wikitables_simple__dev::p15]

Cited: alce::513__wikitables_simple__dev::p15, alce::513__wikitables_simple__dev::p17, alce::513__wikitables_simple__dev::p18

### `526__wikitables_simple__dev`
> Based on the provided sources, here are male names of drag kings:

Mo B. Dick, Gage Gatlyn, Murray Hill, Ian Blakk, Anson Reign, Damian Matrix, Owen McCord, Xander Kinidy, Remington Steal, Flare, Freddy Prinze Charming, Amadeus Karmani York, Richard Cranium, Gunner Gatlyn, Dred, Will Ryder, Buck Naked, and Spikey Van Dykey are stage names that have become cornerstones in the drag king community. [alce::526__wikitables_simple__dev::p0]
> Additional examples of drag king stage names include "Smack Diaz," "Stanley Knife," and "Razor Blade." [alce::526__wikitables_simple__dev::p1]

Cited: alce::526__wikitables_simple__dev::p0, alce::526__wikitables_simple__dev::p1

### `1358__wikidata_simple__dev`
> Several football teams are based in County Galway:

Galway United F.C. is an Irish association football club based in Galway that plays in the League of Ireland First Division. [alce::1358__wikidata_simple__dev::p7]
> Galway W.F.C. (Galway Women's Football Club) is an Irish association football club based in Galway that has played in the Women's National League since 2013–14.
> Galway Bohemians F.C. is an Irish association football club based in Galway whose senior men's team competes in the Galway & District League. [alce::1358__wikidata_simple__dev::p35]

Cited: alce::1358__wikidata_simple__dev::p35, alce::1358__wikidata_simple__dev::p7

### `976__wikidata_comp__dev`
> Philip Hinchcliffe produced "Doctor Who" from 1974 to 1977. [alce::976__wikidata_comp__dev::p0]
> He also produced "Private Schulz" for the BBC. [alce::976__wikidata_comp__dev::p0]
> Additionally, he produced "The Charmer" for London Weekend Television in 1987. [alce::976__wikidata_comp__dev::p0]
> He worked as an executive producer on series including "Taggart" and the John Hannah episodes of "Rebus" for Scottish Television. [alce::976__wikidata_comp__dev::p2]

Cited: alce::976__wikidata_comp__dev::p0, alce::976__wikidata_comp__dev::p2

### `716__wikidata_simple__dev`
> Several geographic features can be found in or around Surat Thani:

Surat Thani is located near the mouth of the Tapi River on the Gulf of Thailand. [alce::716__wikidata_simple__dev::p0]
> The province lies on the western shore of the Gulf of Thailand. [alce::716__wikidata_simple__dev::p2]
> Many islands in the Gulf of Thailand belong to the district, including Ko Samui, Ko Pha Ngan, Ko Tao, and the Ko Ang Thong Marine National Park. [alce::716__wikidata_simple__dev::p4]
> To the west are the limestone mountains of the Phuket range, which are mostly covered with forest and contain Khao Sok National Park. [alce::716__wikidata_simple__dev::p4]
> To the east, the hills of the Nakhon Si Thammarat mountain range rise and are protected in the Tai Rom Yen National Park. [alce::716__wikidata_simple__dev::p4]
> Khao Tha Phet is a hill near the town of Surat Thani with an altitude of about 210 meters above sea level. [alce::716__wikidata_simple__dev::p15]

Cited: alce::716__wikidata_simple__dev::p0, alce::716__wikidata_simple__dev::p15, alce::716__wikidata_simple__dev::p2, alce::716__wikidata_simple__dev::p4

### `552__wikitables_simple__dev`
> A hash function is any function that can be used to map data of arbitrary size to data of a fixed size. [alce::552__wikitables_simple__dev::p0]
> Hash functions are often used in combination with a hash table, a common data structure used in computer software for rapid data lookup. [alce::552__wikitables_simple__dev::p0]
> Hash functions accelerate table or database lookup by detecting duplicated records in a large file. [alce::552__wikitables_simple__dev::p0]
> Cryptographic hash functions are a type of cryptographic algorithm that take a message of any length as input and output a short, fixed length hash, which can be used in applications such as digital signatures. [alce::552__wikitables_simple__dev::p9]
> Examples of hash functions include MD4, MD5, and the Secure Hash Algorithm (SHA) series. [alce::552__wikitables_simple__dev::p9]

Cited: alce::552__wikitables_simple__dev::p0, alce::552__wikitables_simple__dev::p9

### `824__wikidata_simple__dev`
> Compton Bennett directed several films. He is perhaps best known for directing the 1945 film "The Seventh Veil" and the 1950 version of "King Solomon's Mines". [alce::824__wikidata_simple__dev::p0]
> He also directed "Madness of the Heart" (1949) with Margaret Lockwood. [alce::824__wikidata_simple__dev::p3]
> Additionally, in 1957 he produced and directed four films: "After the Ball", "Man-Eater", "That Woman Opposite" and "The Flying Scot". [alce::824__wikidata_simple__dev::p1]

Cited: alce::824__wikidata_simple__dev::p0, alce::824__wikidata_simple__dev::p1, alce::824__wikidata_simple__dev::p3

### `476__wikitables_simple__dev`
> Based on the provided sources, several magazines are satirical magazines:

Monocle was an American satirical magazine, published irregularly from the late 1950s until the mid-sixties. [alce::476__wikitables_simple__dev::p27]
> Eulenspiegel – Das Satiremagazin is a German humor and satirical magazine published by Eulenspiegel GmbH in Berlin. [alce::476__wikitables_simple__dev::p15]
> Penguen, LeMan, and Uykusuz are leading satirical magazines of Turkey, with historical examples including Gırgır and Marko Paşa. [alce::476__wikitables_simple__dev::p24]

Cited: alce::476__wikitables_simple__dev::p15, alce::476__wikitables_simple__dev::p24, alce::476__wikitables_simple__dev::p27

### `535__wikitables_simple__dev`
> Based on the provided sources, the following mosques are famous grand mosques:

The Grand Mosque in Kuwait is the largest and official mosque in the country. [alce::535__wikitables_simple__dev::p8]
> The Grand Mosque in Dubai is located in the Bur Dubai area and serves as the hub of Dubai's religious and cultural life. [alce::535__wikitables_simple__dev::p5]
> The Al-Fateh Grand Mosque is one of the largest mosques in the world and is the largest place of worship in Bahrain. [alce::535__wikitables_simple__dev::p81]
> The Grand Mosque of Paris is one of the largest mosques in France and is the oldest mosque in France's metropolitan area. [alce::535__wikitables_simple__dev::p0]

Cited: alce::535__wikitables_simple__dev::p0, alce::535__wikitables_simple__dev::p5, alce::535__wikitables_simple__dev::p8, alce::535__wikitables_simple__dev::p81

### `631__wikidata_simple__dev`
> Multimedia Group Limited owns six radio stations, six news websites, and a satellite television network called Multi TV. [alce::631__wikidata_simple__dev::p0]
> The six radio stations operate in the Ashanti Region and Greater Accra Region. [alce::631__wikidata_simple__dev::p0]

Cited: alce::631__wikidata_simple__dev::p0

### `735__wikidata_simple__dev`
> "Buffy the Vampire Slayer" is a TV show that had Mutant Enemy Productions as its producer. [alce::735__wikidata_simple__dev::p1]

Cited: alce::735__wikidata_simple__dev::p1

### `240__wikidata_intersection__dev`
_Refused._

### `44__wikitables_composition__dev`
> Powder Ridge Ski Area is a ski area with a vertical drop located in Connecticut. [alce::44__wikitables_composition__dev::p14]

Cited: alce::44__wikitables_composition__dev::p14

### `541__wikitables_simple__dev`
> Based on the provided sources, the following weapons are of the type battle rifle:

The FN FAL, M14, and H&K G3 are full-powered automatic rifles classified as battle rifles. [alce::541__wikitables_simple__dev::p0]
> The Mk 14 Enhanced Battle Rifle is used for medium to long range engagements. [alce::541__wikitables_simple__dev::p57]
> The ARX200 is a battle rifle configuration with a foldable telescoping stock, capable of fully automatic and semi-automatic fire. [alce::541__wikitables_simple__dev::p73]

Cited: alce::541__wikitables_simple__dev::p0, alce::541__wikitables_simple__dev::p57, alce::541__wikitables_simple__dev::p73

### `332__wikidata_intersection__dev`
> "En Thangai Kalyani" is a T. Rajendar production that featured compositions by T. Rajendar. [alce::332__wikidata_intersection__dev::p26]
> The film was directed and produced by T.
> Rajendar, and the soundtrack was written and composed by T.
> Rajendar himself.

Cited: alce::332__wikidata_intersection__dev::p26

### `457__wikidata_intersection__dev`
_Refused._

### `782__wikidata_simple__dev`
> Benny Parsons won the 1973 NASCAR Winston Cup championship. [alce::782__wikidata_simple__dev::p1]
> He also won the 1968 and 1969 ARCA championships. [alce::782__wikidata_simple__dev::p16]
> Additionally, he won the 1975 Daytona 500. [alce::782__wikidata_simple__dev::p84]

Cited: alce::782__wikidata_simple__dev::p1, alce::782__wikidata_simple__dev::p16, alce::782__wikidata_simple__dev::p84

### `561__wikidata_simple__dev`
> Mary Joe Fernández was a competitor in women's doubles tennis at the 1996 Summer Olympics. [alce::561__wikidata_simple__dev::p46]

Cited: alce::561__wikidata_simple__dev::p46

### `558__wikidata_simple__dev`
_Refused._

### `651__wikidata_simple__dev`
> Rubén Reyes is a person who spoke or wrote in Garifuna. [alce::651__wikidata_simple__dev::p26]
> He is a linguist and expert on the history and culture of the Garifuna people who created the world's first tri-lingual dictionary of Garifuna, "Garudia: Garifuna Trilingual Dictionary (Garifuna-English-Spanish)." [alce::651__wikidata_simple__dev::p26]

Cited: alce::651__wikidata_simple__dev::p26

### `964__wikidata_comp__dev`
_Refused._

### `79__wikitables_composition__dev`
_Refused._

### `67__wikitables_composition__dev`
> Zachary Sukunda transferred to the HFX Wanderers in the Canadian Premier League in 2019. [alce::67__wikitables_composition__dev::p18]
> He was announced as HFX Wanderers FC's first signing on November 29, 2018. [alce::67__wikitables_composition__dev::p18]

Cited: alce::67__wikitables_composition__dev::p18

### `367__wikidata_comp__dev`
> Based on the provided sources, several people coach employees of Crystal Palace F.C.:

Salako has coached Crystal Palace's under 16 team and was announced as Crystal Palace first team coach on 8 August 2015. [alce::367__wikidata_comp__dev::p65]
> Darren Powell is an academy coach for Crystal Palace. [alce::367__wikidata_comp__dev::p34]
> Derek Broadley served as Crystal Palace's Academy Director. [alce::367__wikidata_comp__dev::p74]

Cited: alce::367__wikidata_comp__dev::p34, alce::367__wikidata_comp__dev::p65, alce::367__wikidata_comp__dev::p74

### `771__wikidata_simple__dev`
> The Russell Education Trust sponsors free schools. [alce::771__wikidata_simple__dev::p0]
> Specifically, it has established free schools using both the Single Academy Trust model and the Multi-Academy Trust model. [alce::771__wikidata_simple__dev::p2]

Cited: alce::771__wikidata_simple__dev::p0, alce::771__wikidata_simple__dev::p2

### `1007__wikidata_comp__dev`
> Based on the provided sources, I can identify the following citizenships held by Chicago Bulls draftees:

Joakim Noah, selected by the Chicago Bulls with the ninth overall pick in the 2007 NBA draft, holds American, Swedish, and French citizenship. [alce::1007__wikidata_comp__dev::p11]
> Erik Murphy, drafted by the Chicago Bulls in 2013, holds American and Finnish citizenship. [alce::1007__wikidata_comp__dev::p14]
> Therefore, Chicago Bulls draftees hold citizenship from the following countries: **United States, Sweden, France, and Finland**.

Cited: alce::1007__wikidata_comp__dev::p11, alce::1007__wikidata_comp__dev::p14

### `576__wikidata_simple__dev`
> Bangor City F.C. entered the European Cup Winners' Cup in the 1962–63 season after winning the Welsh Cup. [alce::576__wikidata_simple__dev::p0]
> They competed in the European Cup Winners' Cup again during the 1985–86 season. [alce::576__wikidata_simple__dev::p0]
> The club also played in the UEFA Europa League. [alce::576__wikidata_simple__dev::p3]
> Additionally, Bangor City competed in the Welsh Cup, the Welsh Premier League, the English football pyramid system, the Northern Premier League, the Alliance Premier League, the League of Wales, the North Wales Coast League, the Welsh National League, and the North Wales Combination. [alce::576__wikidata_simple__dev::p12]

Cited: alce::576__wikidata_simple__dev::p0, alce::576__wikidata_simple__dev::p12, alce::576__wikidata_simple__dev::p3

### `622__wikidata_simple__dev`
_Refused._

### `407__wikidata_intersection__dev`
> Ethan Coen produced films directed by the Coen Brothers jointly, as the brothers write, direct and produce their films together. [alce::407__wikidata_intersection__dev::p2]
> However, until "The Ladykillers" (2004), Joel received sole credit for directing while Ethan received sole credit for producing. [alce::407__wikidata_intersection__dev::p0]
> Based on the sources provided, specific films where Ethan received producing credit while Joel received directing credit include works up through 2004, such as "The Man Who Wasn't There" (2001). [alce::407__wikidata_intersection__dev::p35]

Cited: alce::407__wikidata_intersection__dev::p0, alce::407__wikidata_intersection__dev::p2, alce::407__wikidata_intersection__dev::p35

### `973__wikidata_comp__dev`
> Suneel Darshan served as director of Akshay Kumar productions. [alce::973__wikidata_comp__dev::p41]
> Specifically, he both produced and directed Akshay Kumar's films "Jaanwar", "Andaaz", "Ek Rishtaa" and "Dosti: Friends Forever". [alce::973__wikidata_comp__dev::p41]
> Additionally, Vipul Amrutlal Shah directed four Hindi films starring Akshay Kumar. [alce::973__wikidata_comp__dev::p3]

Cited: alce::973__wikidata_comp__dev::p3, alce::973__wikidata_comp__dev::p41

### `813__wikidata_simple__dev`
> Blue Mesa Reservoir is located near Gunnison. [alce::813__wikidata_simple__dev::p1]
> The Black Canyon of the Gunnison National Park is also nearby. [alce::813__wikidata_simple__dev::p3]
> Additionally, the Currecanti Recreation Area is located nine miles west of Gunnison. [alce::813__wikidata_simple__dev::p3]

Cited: alce::813__wikidata_simple__dev::p1, alce::813__wikidata_simple__dev::p3

### `867__wikidata_simple__dev`
> Virginia Ruzicki won several competitions. She won the 1978 French Open singles championship. [alce::867__wikidata_simple__dev::p0]
> She also won the French Open doubles event with Jaušovec in 1978. [alce::867__wikidata_simple__dev::p0]
> Additionally, she won the 1982 U.S. Clay Court Championships singles title. [alce::867__wikidata_simple__dev::p20]

Cited: alce::867__wikidata_simple__dev::p0, alce::867__wikidata_simple__dev::p20

### `923__wikidata_simple__dev`
> Based on the provided sources, Serco Group took control of the following organizations:

Serco took over the operation of a London ferry crossing service from the London Borough of Greenwich. [alce::923__wikidata_simple__dev::p43]
> Serco manages and operates local education authorities, including those in Sheffield, Walsall, and Stoke-on-Trent. [alce::923__wikidata_simple__dev::p6]
> Serco operates leisure centers across the UK through Serco Leisure Operating Ltd. [alce::923__wikidata_simple__dev::p6]

Cited: alce::923__wikidata_simple__dev::p43, alce::923__wikidata_simple__dev::p6

### `114__wikidata_comp__dev`
> The Golden State Warriors won the NBA Finals. [alce::114__wikidata_comp__dev::p54]

Cited: alce::114__wikidata_comp__dev::p54

### `857__wikidata_simple__dev`
_Refused._

### `166__wikidata_intersection__dev`
> Manchester United won multiple FA Cup Finals. The sources document several of their victories:

Manchester United won the 1908–09 FA Cup Final, beating Bristol City 1–0 at Crystal Palace through a goal from Sandy Turnbull. [alce::166__wikidata_intersection__dev::p3]
> Manchester United won the 1995–96 FA Cup Final through a goal from Eric Cantona five minutes from the end of the game. [alce::166__wikidata_intersection__dev::p10]
> Manchester United won the 1998–99 FA Cup Final with a record 10th success, winning 2–0 with goals from Teddy Sheringham and Paul Scholes. [alce::166__wikidata_intersection__dev::p26]

Cited: alce::166__wikidata_intersection__dev::p10, alce::166__wikidata_intersection__dev::p26, alce::166__wikidata_intersection__dev::p3

### `257__wikidata_intersection__dev`
> Lucie Šafářová and Bethanie Mattek-Sands won five Grand Slam doubles titles together. [alce::257__wikidata_intersection__dev::p16]
> These titles include the 2015 Australian Open and French Open, the 2016 US Open, and the 2017 Australian Open and French Open. [alce::257__wikidata_intersection__dev::p9]
> Additionally, they won tournaments at Wuhan and Beijing in 2016. [alce::257__wikidata_intersection__dev::p26]

Cited: alce::257__wikidata_intersection__dev::p16, alce::257__wikidata_intersection__dev::p26, alce::257__wikidata_intersection__dev::p9

### `620__wikidata_simple__dev`
> Based on the provided sources, "Anthropoid" is a musical drama film that had its distribution done by LD Entertainment. [alce::620__wikidata_simple__dev::p2]
> "Anthropoid" is described as a "World War II drama" starring Jamie Dornan and Cilian Murphy, and it is listed among LD Entertainment's most recent films produced under the LD banner.

Cited: alce::620__wikidata_simple__dev::p2

### `124__wikidata_comp__dev`
> Garry Marshall directed "Georgia Rule," a movie whose script was created by Mark Andrus. [alce::124__wikidata_comp__dev::p2]
> Additionally, James L. Brooks directed "As Good as It Gets," which was based on Mark Andrus's screenplay "Old Friends" that Brooks reworked. [alce::124__wikidata_comp__dev::p6]

Cited: alce::124__wikidata_comp__dev::p2, alce::124__wikidata_comp__dev::p6

### `313__wikidata_comp__dev`
_Refused._

### `504__wikitables_simple__dev`
> Several computer programs are password manager software:

1Password is a popular password manager software. [alce::504__wikitables_simple__dev::p6]
> Password Safe is a free and open-source password manager program for use with Microsoft Windows. [alce::504__wikitables_simple__dev::p8]
> Pass is a password manager inspired by the Unix philosophy that has a command-line interface and uses GnuPG for encryption and decryption of stored passwords. [alce::504__wikitables_simple__dev::p72]

Cited: alce::504__wikitables_simple__dev::p6, alce::504__wikitables_simple__dev::p72, alce::504__wikitables_simple__dev::p8

### `60__wikitables_composition__dev`
> Richard Sánchez is an athlete who transferred to FC Dallas in 2009. [alce::60__wikitables_composition__dev::p50]

Cited: alce::60__wikitables_composition__dev::p50

### `135__wikidata_comp__dev`
_Refused._

### `323__wikidata_comp__dev`
_Refused._

### `402__wikidata_intersection__dev`
_Refused._

### `971__wikidata_comp__dev`
_Refused._

### `292__wikidata_intersection__dev`
> "Youth Runs Wild" is a 1944 B movie that had Mark Robson as its director and Val Lewton as its producer. [alce::292__wikidata_intersection__dev::p75]

Cited: alce::292__wikidata_intersection__dev::p75

### `829__wikidata_simple__dev`
> The Atlanta Falcons drafted multiple players across different years and rounds. In one draft, they selected Fralic in the first round [alce::829__wikidata_simple__dev::p16]
> , Christopher Owens in the third round [alce::829__wikidata_simple__dev::p22]
> , Lawrence Sidbury in the fourth round [alce::829__wikidata_simple__dev::p22]
> , William Middleton in the fifth round [alce::829__wikidata_simple__dev::p22]
> , Garrett Reynolds in the fifth round [alce::829__wikidata_simple__dev::p22]
> , Spencer Adkins in the sixth round [alce::829__wikidata_simple__dev::p22]
> , and Vance Walker in the seventh round [alce::829__wikidata_simple__dev::p22]
> . In the 2013 NFL Draft, they selected Vance Walker in the seventh round [alce::829__wikidata_simple__dev::p91]
> and Zeke Motta in the seventh round [alce::829__wikidata_simple__dev::p91]
> . In the 2016 NFL Draft, they selected Deion Jones in the second round [alce::829__wikidata_simple__dev::p61]
> and De'Vondre Campbell in the fourth round [alce::829__wikidata_simple__dev::p61]
> .

Cited: alce::829__wikidata_simple__dev::p16, alce::829__wikidata_simple__dev::p22, alce::829__wikidata_simple__dev::p61, alce::829__wikidata_simple__dev::p91

### `104__wikidata_comp__dev`
_Refused._

### `781__wikidata_simple__dev`
> Sheldon Lettich directed several motion pictures. He directed "Lionheart," which became Jean-Claude Van Damme's first movie to be released theatrically by a major U.S. studio. [alce::781__wikidata_simple__dev::p37]
> He also directed "Double Impact," which was filmed in Hong Kong and featured Van Damme in a double role as twin brothers. [alce::781__wikidata_simple__dev::p37]
> Additionally, he directed "Only the Strong," which introduced the Brazilian martial art of Capoeira to international audiences. [alce::781__wikidata_simple__dev::p37]
> He directed "The Order," an action-thriller starring Van Damme and Charlton Heston. [alce::781__wikidata_simple__dev::p3]
> He also directed "The Hard Corps," an urban action-romance starring Jean-Claude Van Damme and Vivica Fox. [alce::781__wikidata_simple__dev::p3]

Cited: alce::781__wikidata_simple__dev::p3, alce::781__wikidata_simple__dev::p37

### `20__wikitables_composition__dev`
_Refused._

### `568__wikidata_simple__dev`
> Several notable individuals served in the Bulgarian military. Bulgarian generals and military officers including Dimitar Popgeorgiev, Kliment Boyadzhiev, Konstantin Zhostov, Aleksandar Protogerov, Boris Drangov, Petar Darvingov, and Kiril Yanchulev served in the Bulgarian Army during various conflicts such as the Serbo-Bulgarian War, First Balkan War, Second Balkan War, World War I, and World War II. [alce::568__wikidata_simple__dev::p22]
> Petar Darvingov specifically served as a military organizer during the Ilinden uprising in 1903 and later held the rank of major in the Bulgarian Army. [alce::568__wikidata_simple__dev::p42]
> Danail Nikolaev was a Bulgarian officer who became the first person to attain the highest rank in the Bulgarian military, General of the Infantry, and served as Minister of War on the eve of the Balkan wars. [alce::568__wikidata_simple__dev::p66]

Cited: alce::568__wikidata_simple__dev::p22, alce::568__wikidata_simple__dev::p42, alce::568__wikidata_simple__dev::p66

### `879__wikidata_simple__dev`
_Refused._

### `378__wikidata_intersection__dev`
> Based on the provided sources, Tottenham Hotspur competed in multiple FA Cup Finals:

The 1982 FA Cup Final featured Tottenham Hotspur as competitors, where they faced Queens Park Rangers on 22 May 1982 at Wembley Stadium. [alce::378__wikidata_intersection__dev::p0]
> The 1962 FA Cup Final featured Tottenham Hotspur as competitors, where they defeated Burnley 3–1 on 5 May 1962 at Wembley Stadium. [alce::378__wikidata_intersection__dev::p8]
> The 1961 FA Cup Final featured Tottenham Hotspur as competitors, where they defeated Leicester City 2–0. [alce::378__wikidata_intersection__dev::p12]
> Additionally, Tottenham Hotspur competed in an FA Cup Final against Sheffield United at Crystal Palace. [alce::378__wikidata_intersection__dev::p56]

Cited: alce::378__wikidata_intersection__dev::p0, alce::378__wikidata_intersection__dev::p12, alce::378__wikidata_intersection__dev::p56, alce::378__wikidata_intersection__dev::p8

### `228__wikidata_comp__dev`
_Refused._

### `692__wikidata_simple__dev`
> Uyghur would be spoken as a native language by the Uyghur people, primarily those in the Xinjiang Uyghur Autonomous Region of Western China. [alce::692__wikidata_simple__dev::p0]
> Significant communities of Uyghur-speakers are also located in Kazakhstan, Kyrgyzstan, and Uzbekistan. [alce::692__wikidata_simple__dev::p0]
> However, not all people of Uyghur ethnicity speak Uyghur as their native language; for example, the Uyghurs of Hunan speak Chinese as their native language instead. [alce::692__wikidata_simple__dev::p96]

Cited: alce::692__wikidata_simple__dev::p0, alce::692__wikidata_simple__dev::p96

### `493__wikitables_simple__dev`
> Based on the provided sources, here are the existing allergens:

The major allergens recognized by the FDA include peanuts, tree nuts, eggs, milk, shellfish, fish, wheat, and soy and their derivatives, as well as sulfites at 10ppm and over. [alce::493__wikitables_simple__dev::p5]
> Canada recognizes all eight of the allergens recognized by the US, and also recognizes sesame seeds. [alce::493__wikitables_simple__dev::p5]
> Additional allergens that may be subject to mandatory labeling include wheat, rye, barley, oats and their hybrids, crustaceans, eggs, fish, peanuts, soybean, milk of all species of mammals, almonds, hazelnuts, cashew nuts, Brazil nuts, macadamia nuts, walnuts, pecan nuts, pistaches, pine nuts, and chestnuts. [alce::493__wikitables_simple__dev::p43]
> Common environmental allergens also include dust mite Der p 1, cat Fel d 1, grass pollen, and ragweed pollen. [alce::493__wikitables_simple__dev::p62]

Cited: alce::493__wikitables_simple__dev::p43, alce::493__wikitables_simple__dev::p5, alce::493__wikitables_simple__dev::p62

### `544__wikitables_simple__dev`
> Based on the provided sources, the following are national quality awards:

The Canada Awards for Excellence are the national quality awards of Canada. [alce::544__wikitables_simple__dev::p8]
> The Rajiv Gandhi National Quality Award is the national quality award given by the Bureau of Indian Standards to Indian organisations that show excellence in their performance. [alce::544__wikitables_simple__dev::p1]
> The Malcolm Baldrige National Quality Award recognizes U.S. organizations in the business, health care, education, and nonprofit sectors for performance excellence. [alce::544__wikitables_simple__dev::p11]
> The Philippine Quality Award Program or PQA is the national quality award for Total Quality Management (TQM) in the Philippines. [alce::544__wikitables_simple__dev::p4]

Cited: alce::544__wikitables_simple__dev::p1, alce::544__wikitables_simple__dev::p11, alce::544__wikitables_simple__dev::p4, alce::544__wikitables_simple__dev::p8

### `1250__wikitables_composition__dev`
_Refused._

### `895__wikidata_simple__dev`
> Philip Rhodes designed vessels. [alce::895__wikidata_simple__dev::p0]
> He was a naval architect known for his diverse yacht designs, creating a wide variety of vessels ranging from small dinghies to large motor yachts, as well as commercial and military vessels such as minesweepers and police boats. [alce::895__wikidata_simple__dev::p0]

Cited: alce::895__wikidata_simple__dev::p0

### `957__wikidata_comp__dev`
> The Metropolitan Archbishop of New York, Philip Saliba, was educated at Balamand Orthodox Theological Seminary in Lebanon and at schools in Syria. [alce::957__wikidata_comp__dev::p62]
> He later studied in England at the Anglican Kelham Theological College and the University of London. [alce::957__wikidata_comp__dev::p62]

Cited: alce::957__wikidata_comp__dev::p62

### `274__wikidata_comp__dev`
_Refused._

### `1011__wikidata_comp__dev`
> Based on the provided sources, multiple drivers arrived in first position at different Japanese Grand Prix races:

Kimi Räikkönen won the 2005 Japanese Grand Prix. [alce::1011__wikidata_comp__dev::p48]
> Fernando Alonso won the 2008 Japanese Grand Prix. [alce::1011__wikidata_comp__dev::p21]
> Sebastian Vettel won the 2010 Japanese Grand Prix. [alce::1011__wikidata_comp__dev::p7]
> Lewis Hamilton won the 2014 Japanese Grand Prix. [alce::1011__wikidata_comp__dev::p62]

Cited: alce::1011__wikidata_comp__dev::p21, alce::1011__wikidata_comp__dev::p48, alce::1011__wikidata_comp__dev::p62, alce::1011__wikidata_comp__dev::p7

### `881__wikidata_simple__dev`
> Avinor operated 46 airports in Norway. [alce::881__wikidata_simple__dev::p0]
> It also operated three Area Control Centers: Bodø Air Traffic Control Center, Stavanger Air Traffic Control Center, and Oslo ATCC. [alce::881__wikidata_simple__dev::p2]
> Additionally, Avinor operated a subsidiary company called Oslo Lufthavn AS, which operates Oslo Airport, Gardermoen. [alce::881__wikidata_simple__dev::p1]

Cited: alce::881__wikidata_simple__dev::p0, alce::881__wikidata_simple__dev::p1, alce::881__wikidata_simple__dev::p2

### `548__wikitables_simple__dev`
> Based on the provided sources, here are some football games:

Association football (known as soccer in some countries), gridiron football (specifically American football or Canadian football), Australian rules football, rugby football (either rugby league or rugby union), and Gaelic football are commonly called "football" in certain places. [alce::548__wikitables_simple__dev::p37]
> The NFL (National Football League) series is a video game simulation of American football developed by Gameloft, released on iOS, Palm, and originally on the Nintendo DS. [alce::548__wikitables_simple__dev::p10]
> High school football games and informal "Turkey Bowl" contests are frequently held on Thanksgiving weekend. [alce::548__wikitables_simple__dev::p12]
> Traditional football games have been played in cities, villages, and schools of Europe for many centuries, with early games having much in common with "mob football" played in England. [alce::548__wikitables_simple__dev::p80]
> Princeton University students played a game called "ballown" as early as 1820, and Harvard had a tradition known as "Bloody Monday" beginning in 1827, which consisted of a mass ballgame between freshmen. [alce::548__wikitables_simple__dev::p80]

Cited: alce::548__wikitables_simple__dev::p10, alce::548__wikitables_simple__dev::p12, alce::548__wikitables_simple__dev::p37, alce::548__wikitables_simple__dev::p80

### `1359__wikidata_simple__dev`
> George M. Harding designed the Thompson Block, a historic commercial building located at 117, 119, 121, 123 and 125 Middle Street in downtown Portland, Maine, which was constructed in 1867. [alce::1359__wikidata_simple__dev::p64]
> He also designed the neighboring Rackleff and Woodman Buildings. [alce::1359__wikidata_simple__dev::p64]
> More broadly, his works included private residences and a large number of school buildings. [alce::1359__wikidata_simple__dev::p0]

Cited: alce::1359__wikidata_simple__dev::p0, alce::1359__wikidata_simple__dev::p64

### `928__wikidata_simple__dev`
> There are multiple football clubs named Vitória FC, and they participated in different competitions:

Esporte Clube Vitória, a Brazilian team from Salvador, plays in the Campeonato Brasileiro Série A and the Campeonato Baiano. [alce::928__wikidata_simple__dev::p10]
> Vitória FC (Riboque), a club from São Tomé and Príncipe, plays in the São Tomé and Príncipe Championship. [alce::928__wikidata_simple__dev::p74]
> Associação Desportiva Vitória, a Brazilian club from Pernambuco state, competed in the Série C five times. [alce::928__wikidata_simple__dev::p11]
> Vitória Sport Clube (Vitória de Guimarães), a Portuguese club, competes in the Primeira Liga. [alce::928__wikidata_simple__dev::p3]

Cited: alce::928__wikidata_simple__dev::p10, alce::928__wikidata_simple__dev::p11, alce::928__wikidata_simple__dev::p3, alce::928__wikidata_simple__dev::p74

### `660__wikidata_simple__dev`
> Based on the provided sources, Shonda Rhimes served as executive producer for the following TV shows:

"Grey's Anatomy" [alce::660__wikidata_simple__dev::p1]
> "Private Practice" [alce::660__wikidata_simple__dev::p1]
> "Scandal" [alce::660__wikidata_simple__dev::p1]
> "Off the Map" [alce::660__wikidata_simple__dev::p1]
> "How to Get Away with Murder" [alce::660__wikidata_simple__dev::p1]
> "The Catch" [alce::660__wikidata_simple__dev::p1]

Cited: alce::660__wikidata_simple__dev::p1

### `759__wikidata_simple__dev`
_Refused._

### `125__wikidata_comp__dev`
> Several KC Royals draftees attended different schools:

Scott Thomas Blewett attended Charles W. Baker High School in Baldwinsville, New York. [alce::125__wikidata_comp__dev::p26]
> Jeremy Affeldt attended Northwest Christian High School in Colbert, Washington. [alce::125__wikidata_comp__dev::p2]
> Jonathan Dziedzic attended Atascocita High School in Humble, Texas, and later Lamar University in Beaumont, Texas. [alce::125__wikidata_comp__dev::p49]
> Eric Skoglund attended Sarasota High School in Sarasota, Florida, and later the University of Central Florida (UCF). [alce::125__wikidata_comp__dev::p13]
> Kevin McCarthy attended Kellenberg Memorial High School in Uniondale, New York, and played college baseball at Marist College. [alce::125__wikidata_comp__dev::p11]

Cited: alce::125__wikidata_comp__dev::p11, alce::125__wikidata_comp__dev::p13, alce::125__wikidata_comp__dev::p2, alce::125__wikidata_comp__dev::p26, alce::125__wikidata_comp__dev::p49

### `134__wikidata_intersection__dev`
_Refused._

### `434__wikidata_intersection__dev`
> Based on the provided sources, **Final Fantasy** was the software published by Square and directed by Hironobu Sakaguchi. [alce::434__wikidata_intersection__dev::p25]

Cited: alce::434__wikidata_intersection__dev::p25

### `788__wikidata_simple__dev`
_Refused._

### `564__wikidata_simple__dev`
> Real Times has control over several entities:

Real Times is the owner and publisher of the "Chicago Defender" and five other regional weeklies in the eastern and Midwestern United States. [alce::564__wikidata_simple__dev::p4]
> The company also owns RTM Digital Studios, a videography company. [alce::564__wikidata_simple__dev::p0]
> Real Times owns a large archive of newspaper clippings, artifacts and photographs connected with African-American history. [alce::564__wikidata_simple__dev::p0]
> In 2009, Real Times purchased Who's Who Publishing Company of Columbus, Ohio. [alce::564__wikidata_simple__dev::p0]
> In 2012, the "Atlanta Daily World" merged with Real Times. [alce::564__wikidata_simple__dev::p36]

Cited: alce::564__wikidata_simple__dev::p0, alce::564__wikidata_simple__dev::p36, alce::564__wikidata_simple__dev::p4

### `924__wikidata_simple__dev`
> Several people served as Solicitor General of Sri Lanka:

Yuwanjana Wijayatilake was the 43rd Solicitor General of Sri Lanka, appointed to that position in 2012. [alce::924__wikidata_simple__dev::p2]
> Elanga Wikramanayake was a Sri Lankan lawyer who served as the Solicitor General of Sri Lanka. [alce::924__wikidata_simple__dev::p17]
> Upawansa Yapa was the 37th Solicitor General of Sri Lanka. [alce::924__wikidata_simple__dev::p53]
> K. C. Kamalasabayson was a Sri Lankan Tamil lawyer and Solicitor General of Sri Lanka. [alce::924__wikidata_simple__dev::p76]

Cited: alce::924__wikidata_simple__dev::p17, alce::924__wikidata_simple__dev::p2, alce::924__wikidata_simple__dev::p53, alce::924__wikidata_simple__dev::p76

### `217__wikidata_intersection__dev`
> Based on the provided sources, Chelsea F.C. played in the following contests that were won by Manchester City F.C.:

The 2018 FA Community Shield was contested by Manchester City and Chelsea, with Manchester City winning 2–0. [alce::217__wikidata_intersection__dev::p0]
> Additionally, Chelsea faced Manchester City in a friendly match on 25 May, which Manchester City won 3–5. [alce::217__wikidata_intersection__dev::p8]

Cited: alce::217__wikidata_intersection__dev::p0, alce::217__wikidata_intersection__dev::p8

### `506__wikitables_simple__dev`
> # Existing Game Controllers

Game controllers are devices used with games or entertainment systems to provide input to a video game, typically to control an object or character in the game. [alce::506__wikitables_simple__dev::p0]
> Input devices that have been classified as game controllers include keyboards, mice, gamepads, joysticks, and special purpose devices such as steering wheels for driving games and light guns for shooting games. [alce::506__wikitables_simple__dev::p1]
> A gamepad, joypad, or controller is a type of game controller held in two hands, where the fingers (especially thumbs) are used to provide input, and they are typically the main input device for video game consoles. [alce::506__wikitables_simple__dev::p8]
> Gamepads generally feature a set of buttons handled with the right thumb and a direction controller handled with the left, which has traditionally been a four-way digital cross (d-pad), though most modern controllers additionally or alternatively feature one or more analog sticks. [alce::506__wikitables_simple__dev::p8]
> Controllers have evolved to include directional pads, multiple buttons, analog sticks, joysticks, motion detection, touch screens and other features. [alce::506__wikitables_simple__dev::p3]
> Before the seventh generation of video game consoles, controllers were plugged into console ports, but since then they have been replaced by wireless controllers, which are battery-powered and do not require controller ports on the console. [alce::506__wikitables_simple__dev::p0]

Cited: alce::506__wikitables_simple__dev::p0, alce::506__wikitables_simple__dev::p1, alce::506__wikitables_simple__dev::p3, alce::506__wikitables_simple__dev::p8

### `359__wikidata_comp__dev`
> A. R. Rahman composed music for "Kaaviya Thalaivan," a film directed by Vasanthabalan. [alce::359__wikidata_comp__dev::p97]
> G. V. Prakash Kumar composed the soundtrack for "Veyil," a film directed by Vasanthabalan. [alce::359__wikidata_comp__dev::p94]

Cited: alce::359__wikidata_comp__dev::p94, alce::359__wikidata_comp__dev::p97

### `720__wikidata_simple__dev`
_Refused._

### `589__wikidata_simple__dev`
> Akitoshi Kawazu designed the first installment of the SaGa series in Japan, which was the first Game Boy game produced by Square. [alce::589__wikidata_simple__dev::p83]

Cited: alce::589__wikidata_simple__dev::p83

### `21__wikitables_composition__dev`
> Based on the provided sources, the following 20th century classical composers were English:

Benjamin Britten emerged as an internationally recognised opera composer in the 20th century. [alce::21__wikitables_composition__dev::p0]
> Michael Tippett emerged as an internationally recognised opera composer in the 20th century. [alce::21__wikitables_composition__dev::p0]
> Ralph Vaughan Williams collected English folk tunes and adapted them to the concert hall in the 20th century. [alce::21__wikitables_composition__dev::p0]
> Additionally, Oliver Knussen and Judith Weir are mentioned as younger composers working in the early 21st century who were prominent figures in the 20th century. [alce::21__wikitables_composition__dev::p1]

Cited: alce::21__wikitables_composition__dev::p0, alce::21__wikitables_composition__dev::p1

### `894__wikidata_simple__dev`
> K' is a character from "The King of Fighters" series who first appeared in 1999. [alce::894__wikidata_simple__dev::p71]
> He debuted as the leader of the Hero Team in "The King of Fighters '99", released in 1999. [alce::894__wikidata_simple__dev::p71]

Cited: alce::894__wikidata_simple__dev::p71

### `244__wikidata_comp__dev`
_Refused._

### `864__wikidata_simple__dev`
> "Gasoline" is a song written by Halsey. [alce::864__wikidata_simple__dev::p21]
> "Sorry" is another song written by Halsey. [alce::864__wikidata_simple__dev::p0]
> "Colors" is a song written by Halsey. [alce::864__wikidata_simple__dev::p6]
> "Castle" is a song co-written by Halsey. [alce::864__wikidata_simple__dev::p3]

Cited: alce::864__wikidata_simple__dev::p0, alce::864__wikidata_simple__dev::p21, alce::864__wikidata_simple__dev::p3, alce::864__wikidata_simple__dev::p6

### `947__wikidata_simple__dev`
_Refused._

### `939__wikidata_simple__dev`
> The Acari National Park can be found in Novo Aripuanã. [alce::939__wikidata_simple__dev::p9]
> Additionally, the municipality contains about 74% of the Aripuanã National Forest. [alce::939__wikidata_simple__dev::p0]

Cited: alce::939__wikidata_simple__dev::p0, alce::939__wikidata_simple__dev::p9

### `679__wikidata_simple__dev`
> Based on the provided sources, Hum Films distributed multiple pieces of media:

Hum Films distributed the film "Verna." [alce::679__wikidata_simple__dev::p40]
> Hum Films also distributed the film "Na Maloom Afraad," which was the first film released under the Hum Films banner in October 2014. [alce::679__wikidata_simple__dev::p4]
> Additionally, Hum Films has distributed and produced over fifteen films both domestically and internationally following the release of "Bin Roye" in 2015. [alce::679__wikidata_simple__dev::p85]
> The film soundtrack album for "Chupan Chupai" was released by Hum Films on December 8, 2017. [alce::679__wikidata_simple__dev::p84]

Cited: alce::679__wikidata_simple__dev::p4, alce::679__wikidata_simple__dev::p40, alce::679__wikidata_simple__dev::p84, alce::679__wikidata_simple__dev::p85

### `130__wikidata_comp__dev`
_Refused._

### `269__wikidata_comp__dev`
> Based on the provided sources, multiple people who work for American Ballet Theatre hold citizenship for different countries:

Mikhail Baryshnikov, who returned to ABT in September 1980 as an artistic director and also performed as a dancer with ABT, became a naturalized citizen of the United States on July 3, 1986. [alce::269__wikidata_comp__dev::p38]
> Hee Seo is a South Korean principal dancer for American Ballet Theatre. [alce::269__wikidata_comp__dev::p45]
> Stella Abrera is a Filipina-American principal ballerina with American Ballet Theatre. [alce::269__wikidata_comp__dev::p9]
> Cynthia Harvey is an American former principal dancer for American Ballet Theatre. [alce::269__wikidata_comp__dev::p64]
> Since the question asks for "which country" (singular) without specifying which ABT employee, the sources support multiple answers: the United States, South Korea, and the Philippines.

Cited: alce::269__wikidata_comp__dev::p38, alce::269__wikidata_comp__dev::p45, alce::269__wikidata_comp__dev::p64, alce::269__wikidata_comp__dev::p9

### `462__wikidata_intersection__dev`
> Laurentine Hamilton was a minister who was an alumnus of both Auburn Theological Seminary and Hamilton College. [alce::462__wikidata_intersection__dev::p4]
> He graduated from Hamilton College in Clinton, New York in 1850 and attended Auburn Theological Seminary, from which he graduated in 1853. [alce::462__wikidata_intersection__dev::p4]

Cited: alce::462__wikidata_intersection__dev::p4

### `505__wikitables_simple__dev`
> Here are some notable wildfires that happened in Canada or the US:

The 2015 Canadian wildfires were a series of wildfires across Canada and Alaska in July 2015 which spread smoke across most of North America, with over two hundred fires ablaze across British Columbia, Saskatchewan, and Alberta. [alce::505__wikitables_simple__dev::p0]
> In 2017, the Lodgepole Complex Fire was the nation's largest wildfire that year in the US. [alce::505__wikitables_simple__dev::p4]
> The La Tuna Fire was the largest wildfire in Los Angeles history. [alce::505__wikitables_simple__dev::p4]
> The 2017 British Columbia wildfires were the worst in the history of the province. [alce::505__wikitables_simple__dev::p4]
> In 2017, the western U.S. witnessed about 50,000 wildfires, with more than 3.4 million hectares burned. [alce::505__wikitables_simple__dev::p4]

Cited: alce::505__wikitables_simple__dev::p0, alce::505__wikitables_simple__dev::p4

### `123__wikidata_intersection__dev`
_Refused._

### `470__wikitables_simple__dev`
> Based on the provided sources, the giant sequoias with a trunk volume larger than 912.5 cubic meters are:

General Sherman, with a volume of 1,486.9 cubic meters. [alce::470__wikitables_simple__dev::p0]
> General Grant, with a volume of 1,319.8 cubic meters. [alce::470__wikitables_simple__dev::p0]
> President, with a volume of 1,278.4 cubic meters. [alce::470__wikitables_simple__dev::p0]
> The sources also mention that there are at least five additional giant sequoias larger than Lost Monarch (1,203.5 cubic meters), and that Ishi Giant has a volume of 1,110 cubic meters, which ranks it as the 13th largest giant sequoia. [alce::470__wikitables_simple__dev::p10]

Cited: alce::470__wikitables_simple__dev::p0, alce::470__wikitables_simple__dev::p10

### `11__wikitables_composition__dev`
> Based on the provided sources, here are the onshore wind farms of the United Kingdom in Scotland:

Whitelee Wind Farm, located near Eaglesham in East Renfrewshire, is the largest onshore wind farm in the United Kingdom with 215 Siemens and Alstom wind turbines and a total capacity of 539 MW. [alce::11__wikitables_composition__dev::p1]
> Clyde Wind Farm near Abington, South Lanarkshire is the UK's second largest onshore wind farm, comprising 152 turbines with a total installed capacity of 350 MW. [alce::11__wikitables_composition__dev::p3]
> Crystal Rig Wind Farm is an operational onshore wind farm located on the Lammermuir Hills in the Scottish Borders region of Scotland, and is currently the 2nd largest wind farm in the UK in terms of nameplate capacity. [alce::11__wikitables_composition__dev::p26]
> The Viking Wind Farm in the Shetland Islands was first proposed as a 600 MW 150 turbine project in 2009, though it was later reduced in scope due to environmental concerns. [alce::11__wikitables_composition__dev::p1]
> There are many other large onshore wind farms in Scotland at various stages of development, including some that are in community ownership. [alce::11__wikitables_composition__dev::p1]

Cited: alce::11__wikitables_composition__dev::p1, alce::11__wikitables_composition__dev::p26, alce::11__wikitables_composition__dev::p3

### `398__wikidata_comp__dev`
> David Walker, the current Bishop of Manchester, was taught at King's College, Cambridge. [alce::398__wikidata_comp__dev::p25]
> He also trained for ministry at Queen's College, Edgbaston. [alce::398__wikidata_comp__dev::p25]

Cited: alce::398__wikidata_comp__dev::p25

### `113__wikidata_intersection__dev`
> "No Country for Old Men" is a film directed by Joel Coen and written by Ethan Coen. [alce::113__wikidata_intersection__dev::p35]

Cited: alce::113__wikidata_intersection__dev::p35

### `866__wikidata_simple__dev`
> René Clair directed several notable films. His best-known films include "The Italian Straw Hat" (1928), "Under the Roofs of Paris" (1930), "Le Million" (1931), "À nous la liberté" (1931), "I Married a Witch" (1942), and "And Then There Were None" (1945). [alce::866__wikidata_simple__dev::p3]
> He also directed "The Flame of New Orleans" (1941). [alce::866__wikidata_simple__dev::p63]

Cited: alce::866__wikidata_simple__dev::p3, alce::866__wikidata_simple__dev::p63

### `147__wikidata_intersection__dev`
> Based on the provided sources, several songs were composed by Kanye West and Kid Cudi:

"Cudi Montage" is a song composed by Kanye West and Kid Cudi, released as the seventh track off their eponymous debut album "Kids See Ghosts" (2018). [alce::147__wikidata_intersection__dev::p19]
> "Gorgeous" is a song written by West, Cudi, Raekwon, No I.D., Mike Dean and Rhymefest from Kanye West's fifth studio album "My Beautiful Dark Twisted Fantasy" (2010). [alce::147__wikidata_intersection__dev::p2]
> Additionally, Kid Cudi co-wrote and provided vocals on several tracks from Kanye West's "808s & Heartbreak" (2008), including "Heartless," "Welcome to Heartbreak," "Paranoid" and "RoboCop." [alce::147__wikidata_intersection__dev::p8]

Cited: alce::147__wikidata_intersection__dev::p19, alce::147__wikidata_intersection__dev::p2, alce::147__wikidata_intersection__dev::p8

### `941__wikidata_simple__dev`
> Southern Min (also called Hokkien language, Hoklo language, Hokkien-Taiwanese or Min-Nan) has its origins in Fujian. [alce::941__wikidata_simple__dev::p18]
> Specifically, Hokkien originated in the southern area of Fujian province, an important center for trade and migration. [alce::941__wikidata_simple__dev::p18]

Cited: alce::941__wikidata_simple__dev::p18

### `254__wikidata_comp__dev`
_Refused._

### `495__wikitables_simple__dev`
> Based on the provided sources, here are some gacha games that were released in English language:

Fire Emblem Heroes is a gacha game example. [alce::495__wikitables_simple__dev::p1]
> Puzzle & Dragons is a gacha game example. [alce::495__wikitables_simple__dev::p1]
> Dragon Collection is a gacha game example. [alce::495__wikitables_simple__dev::p1]
> Granblue Fantasy is a gacha game example. [alce::495__wikitables_simple__dev::p0]
> Girls' Frontline is a gacha game example. [alce::495__wikitables_simple__dev::p0]
> Monster Strike is a gacha game example. [alce::495__wikitables_simple__dev::p0]
> Fate/Grand Order is a gacha game example. [alce::495__wikitables_simple__dev::p0]
> Kingdom Hearts Union X is a gacha game example. [alce::495__wikitables_simple__dev::p0]
> Azur Lane is a Chinese gacha game example. [alce::495__wikitables_simple__dev::p0]
> League of Angels is a Chinese gacha game example. [alce::495__wikitables_simple__dev::p0]

Cited: alce::495__wikitables_simple__dev::p0, alce::495__wikitables_simple__dev::p1

### `811__wikidata_simple__dev`
> Dave Lebling designed several interactive fiction games. His games include "Zork I," "II" and "III", "Starcross", "Suspect", "Spellbreaker", "The Lurking Horror" and "James Clavell's Shogun". [alce::811__wikidata_simple__dev::p0]

Cited: alce::811__wikidata_simple__dev::p0

### `862__wikidata_simple__dev`
_Refused._

### `904__wikidata_simple__dev`
> Based on the provided sources, several people work in the country music industry:

Paul Worley is an American record producer and session guitarist known primarily for his work in country music. [alce::904__wikidata_simple__dev::p44]
> He has worked as a vice president at Sony BMG, chief creative officer at Warner Bros. Records' Nashville division, and as a record producer for acts such as Big & Rich. [alce::904__wikidata_simple__dev::p44]
> Cohen is a studio musician who has worked with prominent country music artists including Florida Georgia Line, Carrie Underwood, Old Dominion, Brett Eldredge, Chris Young, Walker Hayes, Jon Pardi, Cole Swindell, Josh Turner, Reba McEntire, Brooks and Dunn, and Kip Moore. [alce::904__wikidata_simple__dev::p79]
> Tony Byworth edited the monthly magazine Country Music People and co-founded Byworth-Wootton International, the UK's first country-music services company. [alce::904__wikidata_simple__dev::p94]
> He also provided PR services for artists like Garth Brooks and George Strait. [alce::904__wikidata_simple__dev::p94]
> Dave Cobb is a music producer who founded and runs Low Country Sound, a record label imprint based in Nashville, Tennessee. [alce::904__wikidata_simple__dev::p78]

Cited: alce::904__wikidata_simple__dev::p44, alce::904__wikidata_simple__dev::p78, alce::904__wikidata_simple__dev::p79, alce::904__wikidata_simple__dev::p94

### `627__wikidata_simple__dev`
_Refused._

### `421__wikidata_intersection__dev`
_Refused._

### `880__wikidata_simple__dev`
> Cyrus Edwin Dallin created several notable works of art. [alce::880__wikidata_simple__dev::p1]
> He created the equestrian statue of Paul Revere in Boston, Massachusetts; the Angel Moroni atop Salt Lake Temple in Salt Lake City, Utah; and his most famous work, "Appeal to the Great Spirit", at the Museum of Fine Arts, Boston. [alce::880__wikidata_simple__dev::p1]
> In total, he created more than 260 works. [alce::880__wikidata_simple__dev::p1]

Cited: alce::880__wikidata_simple__dev::p1

### `183__wikidata_comp__dev`
> Vishal served as producer on the film "3AM," which was directed by Vishal Mahadkar. [alce::183__wikidata_comp__dev::p15]

Cited: alce::183__wikidata_comp__dev::p15

### `712__wikidata_simple__dev`
> Caitlin "Kate" Todd first appeared in "Yankee White." [alce::712__wikidata_simple__dev::p5]

Cited: alce::712__wikidata_simple__dev::p5

### `550__wikitables_simple__dev`
> Based on the provided sources, the protected areas with an area larger than 250,000 km² are:

The Kermadec Sanctuary would be 620,000 square kilometers, making it the world's largest and most significant fully protected areas. [alce::550__wikitables_simple__dev::p5]
> An unnamed protected area with 620,000 square kilometres would be one of the world's largest fully protected areas. [alce::550__wikitables_simple__dev::p53]
> The Southern Tanami Indigenous Protected Area spans 10.15 million hectares (approximately 101,500 km²), which is below the 250,000 km² threshold, so it does not qualify.

Cited: alce::550__wikitables_simple__dev::p5, alce::550__wikitables_simple__dev::p53

### `656__wikidata_simple__dev`
> Jack Dann was responsible for editing several anthologies. He jointly edited a series of themed science fiction and fantasy anthologies with Gardner Dozois, known as "The Exclamatory series," which began in 1980 with "Aliens!" [alce::656__wikidata_simple__dev::p14]
> . He also co-edited "Future Power" (1976) with Gardner Dozois [alce::656__wikidata_simple__dev::p2]
> . Additionally, Jack Dann edited "Nebula Awards 32," an anthology of science fiction short works first published in April 1998 [alce::656__wikidata_simple__dev::p79]
> .

Cited: alce::656__wikidata_simple__dev::p14, alce::656__wikidata_simple__dev::p2, alce::656__wikidata_simple__dev::p79

### `480__wikitables_simple__dev`
> Based on the provided sources, the following are women's film festivals:

The Rocky Mountain Women's Film Festival (RMWFF) in Colorado Springs, Colorado is the longest-running women's film festival in North America. [alce::480__wikitables_simple__dev::p21]
> The Cairo International Women's Film Festival (CIWFF) is dedicated to introducing films directed by women from around the world. [alce::480__wikitables_simple__dev::p6]
> The China Women's Film Festival (CWFF) was established in 2013 as an annual event that features films from predominantly female filmmakers from around the world. [alce::480__wikitables_simple__dev::p0]
> Additional women's film festivals mentioned include the 10th International Women's Film Festival in Seoul and the St. John's International Women's Film Festival. [alce::480__wikitables_simple__dev::p87]

Cited: alce::480__wikitables_simple__dev::p0, alce::480__wikitables_simple__dev::p21, alce::480__wikitables_simple__dev::p6, alce::480__wikitables_simple__dev::p87

### `662__wikidata_simple__dev`
> Based on the provided sources, the ships registered in The Bay State (Massachusetts) were:

The USTS "Bay State" (originally named "Empire State IV") served as a training vessel for the Massachusetts Maritime Academy. [alce::662__wikidata_simple__dev::p0]
> Another ship named "Bay State" was a 6,583-ton British steamer operated by the Warren Line that departed from Boston. [alce::662__wikidata_simple__dev::p2]
> The "Doyen" was renamed "Bay State" and served as a training vessel, dormitory and classroom for the Massachusetts Maritime Academy in Buzzards Bay from 1957 to 1972. [alce::662__wikidata_simple__dev::p17]

Cited: alce::662__wikidata_simple__dev::p0, alce::662__wikidata_simple__dev::p17, alce::662__wikidata_simple__dev::p2

### `157__wikidata_intersection__dev`
_Refused._

### `613__wikidata_simple__dev`
> The Pirate Party Luxembourg follows the Pirate Party's ideology. [alce::613__wikidata_simple__dev::p47]
> The Pirate Party of Galicia also inherits the ideology from the Pirate Party of Sweden. [alce::613__wikidata_simple__dev::p77]

Cited: alce::613__wikidata_simple__dev::p47, alce::613__wikidata_simple__dev::p77

### `760__wikidata_simple__dev`
> Hall is a video game designer who previously served in the Royal New Zealand Air Force. [alce::760__wikidata_simple__dev::p7]
> He served as a commissioned officer in the Royal New Zealand Air Force for five years and completed a degree at the University of Otago under a Defense Scholarship. [alce::760__wikidata_simple__dev::p7]

Cited: alce::760__wikidata_simple__dev::p7

### `290__wikidata_intersection__dev`
> Alain Prost won multiple British Grand Prix races. He won the 1983 British Grand Prix, which was his first of five British Grand Prix victories. [alce::290__wikidata_intersection__dev::p0]
> He also won the 1985 British Grand Prix at Silverstone. [alce::290__wikidata_intersection__dev::p4]
> Additionally, Prost won the 1989 British Grand Prix at Silverstone, driving a McLaren-Honda. [alce::290__wikidata_intersection__dev::p2]
> He won the 1993 British Grand Prix at Silverstone, driving a Williams-Renault. [alce::290__wikidata_intersection__dev::p6]

Cited: alce::290__wikidata_intersection__dev::p0, alce::290__wikidata_intersection__dev::p2, alce::290__wikidata_intersection__dev::p4, alce::290__wikidata_intersection__dev::p6

### `764__wikidata_simple__dev`
> Jack Holt designed more than 40 boats, many of which were sailing dinghies. [alce::764__wikidata_simple__dev::p0]
> His notable designs included the Mirror dinghy, Enterprise, GP14, Cadet, Hornet, Pacer, Solo, Streaker, Miracle, Merlin Rocket, and National 12. [alce::764__wikidata_simple__dev::p28]
> His pioneering designs of dinghies using plywood helped popularize the sport of sailing in the period immediately following World War II. [alce::764__wikidata_simple__dev::p0]

Cited: alce::764__wikidata_simple__dev::p0, alce::764__wikidata_simple__dev::p28

### `233__wikidata_intersection__dev`
> The Boston Red Sox have won nine World Series championships, most recently in 2018. [alce::233__wikidata_intersection__dev::p0]
> Specifically, they won World Series championships in 2004, 2007, 2013, and 2018. [alce::233__wikidata_intersection__dev::p5]
> Additionally, the Red Sox won the American League pennant in 1903. [alce::233__wikidata_intersection__dev::p0]

Cited: alce::233__wikidata_intersection__dev::p0, alce::233__wikidata_intersection__dev::p5

### `97__wikitables_composition__dev`
> Several killers went on rampages in Europe after 1995:

Éric Borel carried out a shooting spree in France that resulted in 15 deaths, with the last victim dying on 2 March 1996. [alce::97__wikitables_composition__dev::p5]
> Gusztáv Nemeskéri, known as the Katóka Street Killer, was a Hungarian serial killer who killed 4 people between 1996 and 1999. [alce::97__wikitables_composition__dev::p62]
> The Nighttime Killers were two men, Vladyslav Volkovich and Volodymyr Kondratenko, who were responsible for a string of brutal murders in Kiev, Ukraine between 1991 and 1997, with 16 murders charged against them. [alce::97__wikitables_composition__dev::p34]

Cited: alce::97__wikitables_composition__dev::p34, alce::97__wikitables_composition__dev::p5, alce::97__wikitables_composition__dev::p62

### `72__wikitables_composition__dev`
> Based on the provided sources, the following lifestyle shopping malls are located in Alabama:

Bridge Street Town Centre is an upscale lifestyle center shopping center in Huntsville, Alabama. [alce::72__wikitables_composition__dev::p55]
> Brookwood Village is an upscale shopping mall located near Birmingham in the cities of Mountain Brook and Homewood, Alabama. [alce::72__wikitables_composition__dev::p68]
> Riverchase Galleria is a large upscale, super-regional shopping mall in Hoover, Alabama, close to Birmingham, Alabama. [alce::72__wikitables_composition__dev::p43]

Cited: alce::72__wikitables_composition__dev::p43, alce::72__wikitables_composition__dev::p55, alce::72__wikitables_composition__dev::p68

### `647__wikidata_simple__dev`
> Kenneth MacMillan created the choreography for several ballets. These include:

Elite Syncopations, a one-act ballet created in 1974 for The Royal Ballet. [alce::647__wikidata_simple__dev::p37]
> The Rite of Spring, a one-act ballet created in 1962 for the Royal Ballet. [alce::647__wikidata_simple__dev::p14]
> Romeo and Juliet, which premiered at the Royal Opera House, Covent Garden on 9 February 1965. [alce::647__wikidata_simple__dev::p2]
> Additionally, for the Berlin company, MacMillan created seven ballets: "Valses nobles et sentimentales", "Concerto", "Anastasia" (one act version), "The Sleeping Beauty", "Olympiad", "Cain and Abel" and "Swan Lake". [alce::647__wikidata_simple__dev::p8]

Cited: alce::647__wikidata_simple__dev::p14, alce::647__wikidata_simple__dev::p2, alce::647__wikidata_simple__dev::p37, alce::647__wikidata_simple__dev::p8

### `330__wikidata_intersection__dev`
> Isaac Asimov and Martin H. Greenberg edited multiple works together. They edited "Isaac Asimov Presents The Great SF Stories 13 (1951)," a collection of science fiction short stories. [alce::330__wikidata_intersection__dev::p21]
> They also edited "Isaac Asimov Presents The Great SF Stories 2 (1940)," an anthology of science fiction short stories. [alce::330__wikidata_intersection__dev::p7]

Cited: alce::330__wikidata_intersection__dev::p21, alce::330__wikidata_intersection__dev::p7

### `1003__wikidata_comp__dev`
_Refused._

### `486__wikitables_simple__dev`
> Based on the provided sources, the following weapons are of the bolt action rifle type:

The Prussian needle gun of 1841 was a paper-cartridge bolt action rifle. [alce::486__wikitables_simple__dev::p6]
> The Chassepot rifle, introduced by France in 1866, was also a paper-cartridge bolt action rifle. [alce::486__wikitables_simple__dev::p6]
> The Berdan Type II, introduced by Russia in 1870, was a metallic-cartridge bolt action rifle. [alce::486__wikitables_simple__dev::p6]
> The Mauser Model 1871 was a metallic-cartridge bolt action rifle. [alce::486__wikitables_simple__dev::p6]
> The Gras rifle of 1874 was a modified Chassepot and a metallic-cartridge bolt action rifle. [alce::486__wikitables_simple__dev::p6]
> The Mauser rifle of the late 19th and early 20th centuries is the most famous bolt action rifle type. [alce::486__wikitables_simple__dev::p0]
> The M1903 Springfield is a bolt action rifle derived from the Mauser design. [alce::486__wikitables_simple__dev::p0]
> The Karabiner 98 Kurz rifle (Kar98k or K98) is a bolt action rifle derived from the Mauser design. [alce::486__wikitables_simple__dev::p0]
> The Russian Mosin–Nagant rifle is a bolt action rifle. [alce::486__wikitables_simple__dev::p0]
> The British Lee–Enfield is a bolt action rifle. [alce::486__wikitables_simple__dev::p0]
> The Norwegian rifle mentioned is a bolt action rifle. [alce::486__wikitables_simple__dev::p0]

Cited: alce::486__wikitables_simple__dev::p0, alce::486__wikitables_simple__dev::p6

### `778__wikidata_simple__dev`
_Refused._

### `483__wikitables_simple__dev`
> The highest military medals in various countries are:

The Military Medal is the highest military decoration of Luxembourg. [alce::483__wikitables_simple__dev::p12]
> The Medal of Valor is the highest Israeli military decoration. [alce::483__wikitables_simple__dev::p55]
> The Medal of Honor is the highest military decoration awarded by the United States government. [alce::483__wikitables_simple__dev::p14]

Cited: alce::483__wikitables_simple__dev::p12, alce::483__wikitables_simple__dev::p14, alce::483__wikitables_simple__dev::p55

### `950__wikidata_comp__dev`
> Rajan-Nagendra are composers who have worked with director H.R. Bhargava. [alce::950__wikidata_comp__dev::p0]

Cited: alce::950__wikidata_comp__dev::p0

### `334__wikidata_comp__dev`
_Refused._

### `770__wikidata_simple__dev`
> Multiple individuals received their Ph.D. under the guidance of Franz Boas:

Paul Radin received his Ph.D. in 1911. [alce::770__wikidata_simple__dev::p0]
> Ruth Benedict received her Ph.D. in 1923. [alce::770__wikidata_simple__dev::p0]
> Gladys Reichard received her Ph.D. in 1925. [alce::770__wikidata_simple__dev::p0]
> Ruth Bunzel received her Ph.D. in 1929. [alce::770__wikidata_simple__dev::p0]
> Alexander Lesser received his Ph.D. in 1929. [alce::770__wikidata_simple__dev::p0]
> Margaret Mead received her Ph.D. in 1929. [alce::770__wikidata_simple__dev::p0]
> Gene Weltfish defended her dissertation in 1929. [alce::770__wikidata_simple__dev::p0]
> E. Adamson Hoebel received his Ph.D. in 1934. [alce::770__wikidata_simple__dev::p0]
> Jules Henry received his Ph.D. in 1935. [alce::770__wikidata_simple__dev::p0]
> George Herzog received his Ph.D. in 1938. [alce::770__wikidata_simple__dev::p0]
> Ashley Montagu received his Ph.D. in 1938. [alce::770__wikidata_simple__dev::p0]
> Additionally, an unnamed individual earned his M.A. and Ph.D. in Anthropology from Columbia University under Boas's guidance, with a dissertation titled "The Cattle Complex in East Africa." [alce::770__wikidata_simple__dev::p18]
> Another unnamed individual completed his Ph.D. under Boas's supervision with a thesis on the Alkatcho Carrier Indians of British Columbia. [alce::770__wikidata_simple__dev::p25]

Cited: alce::770__wikidata_simple__dev::p0, alce::770__wikidata_simple__dev::p18, alce::770__wikidata_simple__dev::p25

### `830__wikidata_simple__dev`
> Multiple countries sent competitors to the Hopman Cup. The Soviet Union competed at the Hopman Cup, first competing in the 2nd Hopman Cup in 1990. [alce::830__wikidata_simple__dev::p69]
> Canada competed at the Hopman Cup on four occasions, in 2004, 2014, 2015 and 2018. [alce::830__wikidata_simple__dev::p40]
> China competed at the Hopman Cup on two occasions, with their debut in 2006. [alce::830__wikidata_simple__dev::p14]
> Japan competed at the Hopman Cup on five occasions, with the first being at the inaugural staging in 1989. [alce::830__wikidata_simple__dev::p52]
> Additionally, Kazakhstan, Russia, Ukraine and Uzbekistan have competed in the Hopman Cup as independent states following the dissolution of the Soviet Union. [alce::830__wikidata_simple__dev::p69]

Cited: alce::830__wikidata_simple__dev::p14, alce::830__wikidata_simple__dev::p40, alce::830__wikidata_simple__dev::p52, alce::830__wikidata_simple__dev::p69

### `83__wikitables_composition__dev`
> Multiple Commodore products featured on-board BASIC. The PET 2001 included Commodore BASIC 1.0. [alce::83__wikitables_composition__dev::p2]
> The CBM-II series featured BASIC 4.0+. [alce::83__wikitables_composition__dev::p0]
> The Commodore 128 had BASIC 7.0. [alce::83__wikitables_composition__dev::p25]
> The Commodore LCD included a built-in Commodore BASIC 3.6 interpreter. [alce::83__wikitables_composition__dev::p40]

Cited: alce::83__wikitables_composition__dev::p0, alce::83__wikitables_composition__dev::p2, alce::83__wikitables_composition__dev::p25, alce::83__wikitables_composition__dev::p40

### `300__wikidata_comp__dev`
> Pamplin Media Group's publishing entities are operating primarily in the Portland metropolitan area in the U.S. state of Oregon. [alce::300__wikidata_comp__dev::p0]
> As of 2009, the group owned newspapers in Multnomah, Washington, Clackamas, and Columbia counties. [alce::300__wikidata_comp__dev::p0]
> The group also operates in Central Oregon, including publications such as "The Madras Pioneer" and the "Central Oregonian." [alce::300__wikidata_comp__dev::p2]

Cited: alce::300__wikidata_comp__dev::p0, alce::300__wikidata_comp__dev::p2

### `273__wikidata_intersection__dev`
> Lewis Hamilton won the 2008 British Grand Prix for the McLaren team, starting from fourth position on the grid. [alce::273__wikidata_intersection__dev::p1]
> He also won the 2014 British Grand Prix for the Mercedes team, starting from sixth position. [alce::273__wikidata_intersection__dev::p3]

Cited: alce::273__wikidata_intersection__dev::p1, alce::273__wikidata_intersection__dev::p3

### `575__wikidata_simple__dev`
> Yukihiro Takahashi is a member of several bands. He is best known as the drummer and lead vocalist of the Yellow Magic Orchestra. [alce::575__wikidata_simple__dev::p0]
> He is currently a member of the group METAFIVE. [alce::575__wikidata_simple__dev::p0]
> He is also a member of the duo Sketch Show with Haruomi Hosono. [alce::575__wikidata_simple__dev::p6]

Cited: alce::575__wikidata_simple__dev::p0, alce::575__wikidata_simple__dev::p6

### `1257__wikitables_composition__dev`
> Baltic 1 was a German offshore wind farm that was commissioned after 2010. [alce::1257__wikitables_composition__dev::p17]

Cited: alce::1257__wikitables_composition__dev::p17

### `132__wikidata_comp__dev`
> Sibi Malayl directed the film "Ustaad", which was produced by Ranjith and Shaji Kailas. [alce::132__wikidata_comp__dev::p47]

Cited: alce::132__wikidata_comp__dev::p47

### `901__wikidata_simple__dev`
> Martin Ohm was the doctoral advisor to multiple students. [alce::901__wikidata_simple__dev::p1]
> His students included Friedrich August, Friedrich Bachmann, Elwin Bruno Christoffel, Paul Bachmann, Joseph Brutkowski, Heinrich Eduard Heine, Rudolf Lipschitz, Leo Pochhammer, Friedrich Prym, Wilhelm Wagner, Hermann Waldaestel, Wilhelm Wernicke, Elena Gerz, Valentien Gerz, and Johanna Gerz. [alce::901__wikidata_simple__dev::p1]

Cited: alce::901__wikidata_simple__dev::p1

### `940__wikidata_simple__dev`
_Refused._

### `61__wikitables_composition__dev`
> Based on the provided sources, the call signs of radio stations whose city of license is Meridian, Mississippi are:

WOKK (97.1 FM) is licensed to Meridian, Mississippi. [alce::61__wikitables_composition__dev::p90]
> WKZB had its original city of license as Meridian, Mississippi. [alce::61__wikitables_composition__dev::p1]

Cited: alce::61__wikitables_composition__dev::p1, alce::61__wikitables_composition__dev::p90

### `1360__wikidata_simple__dev`
> The Caribbean is considered a part of North America. [alce::1360__wikidata_simple__dev::p10]

Cited: alce::1360__wikidata_simple__dev::p10

### `814__wikidata_simple__dev`
> Andrea del Verrocchio taught Leonardo da Vinci, who was one of his most famous students. [alce::814__wikidata_simple__dev::p0]
> Leonardo was apprenticed to Verrocchio at age 14 in 1466 and trained in his workshop for 7 years. [alce::814__wikidata_simple__dev::p5]

Cited: alce::814__wikidata_simple__dev::p0, alce::814__wikidata_simple__dev::p5

### `591__wikidata_simple__dev`
> Andrew J. Offutt edited a series of five anthologies entitled "Swords Against Darkness". [alce::591__wikidata_simple__dev::p6]

Cited: alce::591__wikidata_simple__dev::p6

### `159__wikidata_comp__dev`
_Refused._

### `531__wikitables_simple__dev`
> Some notable reefs include:

The Great Barrier Reef is Earth's largest and most famous reef. [alce::531__wikitables_simple__dev::p13]
> The Australian Great Barrier Reef is the best known and largest example of a barrier reef. [alce::531__wikitables_simple__dev::p1]
> The Belize Barrier Reef is another major example of a barrier reef. [alce::531__wikitables_simple__dev::p1]
> The New Caledonian Barrier Reef is also a major barrier reef. [alce::531__wikitables_simple__dev::p1]
> Lighthouse Reef is known as a snorkelling and diving destination, considered one of the best dive sites in Belize and the whole Caribbean. [alce::531__wikitables_simple__dev::p52]
> The Florida reef system includes notable individual reefs along the Florida coast north of the Florida Keys. [alce::531__wikitables_simple__dev::p0]

Cited: alce::531__wikitables_simple__dev::p0, alce::531__wikitables_simple__dev::p1, alce::531__wikitables_simple__dev::p13, alce::531__wikitables_simple__dev::p52

### `840__wikidata_simple__dev`
> SES Americom operated North American geosynchronous satellites. [alce::840__wikidata_simple__dev::p0]
> Before being merged into SES World Skies in 2009, SES Americom operated the following North American satellites in geosynchronous orbit, including AMC-21. [alce::840__wikidata_simple__dev::p1]

Cited: alce::840__wikidata_simple__dev::p0, alce::840__wikidata_simple__dev::p1

### `872__wikidata_simple__dev`
> Kofi Annan was one of the people involved in the Donostia-San Sebastián International Peace Conference. [alce::872__wikidata_simple__dev::p0]
> Bertie Ahern was another person involved in the conference. [alce::872__wikidata_simple__dev::p0]
> Gro Harlem Brundtland also participated in the conference. [alce::872__wikidata_simple__dev::p2]

Cited: alce::872__wikidata_simple__dev::p0, alce::872__wikidata_simple__dev::p2

### `303__wikidata_comp__dev`
> Multiple employees of Fidelity Investments attended different schools:

Peter Lynch graduated from Boston College where he studied history, psychology and philosophy, and earned a Master of Business Administration from the Wharton School of the University of Pennsylvania. [alce::303__wikidata_comp__dev::p0]
> Edward Johnson III attended prep school at Milton Academy before transferring to Tabor Academy and graduating with a Bachelor's degree from Harvard College in 1954. [alce::303__wikidata_comp__dev::p14]
> Kathleen Murphy graduated "summa cum laude" with a Bachelor of Arts degree in both Economics and Political Science from Fairfield University and holds a Juris Doctor degree with highest honors from the University of Connecticut School of Law. [alce::303__wikidata_comp__dev::p19]

Cited: alce::303__wikidata_comp__dev::p0, alce::303__wikidata_comp__dev::p14, alce::303__wikidata_comp__dev::p19

### `94__wikitables_composition__dev`
_Refused._

### `3__wikitables_composition__dev`
_Refused._

### `270__wikidata_intersection__dev`
> Val Guest directed "The Camp on Blood Island" for Hammer Film Productions. [alce::270__wikidata_intersection__dev::p50]

Cited: alce::270__wikidata_intersection__dev::p50

### `433__wikidata_intersection__dev`
_Refused._

### `63__wikitables_composition__dev`
> The Pilgrim Hall Museum is located in Plymouth, MA. [alce::63__wikitables_composition__dev::p0]
> Additionally, Plimoth Plantation is a living history museum in Plymouth, Massachusetts. [alce::63__wikitables_composition__dev::p2]
> The Plymouth Antiquarian House is also located in Plymouth, Massachusetts. [alce::63__wikitables_composition__dev::p89]

Cited: alce::63__wikitables_composition__dev::p0, alce::63__wikitables_composition__dev::p2, alce::63__wikitables_composition__dev::p89

### `530__wikitables_simple__dev`
> # Discovered or Hypothesized Physical Particles

Discovered elementary particles include quarks, gluons, leptons, neutrinos, and the Higgs boson. [alce::530__wikitables_simple__dev::p16]
> All Standard Model particles were discovered below the energy scale of approximately 1 TeV. [alce::530__wikitables_simple__dev::p68]
> The graviton is a hypothetical elementary spin-2 particle proposed to mediate gravitation that remains undiscovered due to detection difficulties. [alce::530__wikitables_simple__dev::p67]
> Hypothesized fundamental particles intermediate between the most fundamental particles and those observed in the Standard Model include "prequarks," "subquarks," "maons," "alphons," "quinks," "rishons," "tweedles," "helons," "haplons," "Y-particles," and "primons," with "preon" being the leading name in the physics community. [alce::530__wikitables_simple__dev::p48]
> Particles range in scale from subatomic particles like electrons, to microscopic particles like atoms and molecules, to macroscopic particles like powders and granular materials. [alce::530__wikitables_simple__dev::p30]

Cited: alce::530__wikitables_simple__dev::p16, alce::530__wikitables_simple__dev::p30, alce::530__wikitables_simple__dev::p48, alce::530__wikitables_simple__dev::p67, alce::530__wikitables_simple__dev::p68

### `676__wikidata_simple__dev`
> Anne Yvonne Gilbert created the cover art for multiple works of literature. She provided the cover art for several of Jennifer Roberson's novels, including "Lady of the Forest" (1992), "Lady of Sherwood" (1999), "Lady of the Glen" (1996), and the 2001 republications of her "Chronicles of the Cheysuli" fantasy series. [alce::676__wikidata_simple__dev::p5]
> She also designed the art for "The Wild Swans" in 2005, a republication of Hans Christian Andersen's story. [alce::676__wikidata_simple__dev::p5]
> Additionally, she redesigned the cover of George RR Martin's "The Ice Dragon" in 2006. [alce::676__wikidata_simple__dev::p4]
> She provided illustrations for "The Frog Prince," retold by Kathy-Jo Wargin in 2007. [alce::676__wikidata_simple__dev::p1]
> She illustrated an abridged, young adult version of Bram Stoker's "Dracula" in 2010. [alce::676__wikidata_simple__dev::p4]
> She also produced illustrations for Jodi Picoult's first young adult novel "Between the Lines," published in 2012. [alce::676__wikidata_simple__dev::p4]

Cited: alce::676__wikidata_simple__dev::p1, alce::676__wikidata_simple__dev::p4, alce::676__wikidata_simple__dev::p5

### `932__wikidata_simple__dev`
_Refused._

### `342__wikidata_intersection__dev`
> Wulfstan (died 1023) was both the Roman Catholic Archbishop of York and the Roman Catholic Bishop of Worcester in England. [alce::342__wikidata_intersection__dev::p26]
> In 1002 he was elected simultaneously to the diocese of Worcester and the archdiocese of York, holding both in plurality until 1016, when he relinquished Worcester; he remained archbishop of York until his death. [alce::342__wikidata_intersection__dev::p13]

Cited: alce::342__wikidata_intersection__dev::p13, alce::342__wikidata_intersection__dev::p26

### `823__wikidata_simple__dev`
> "Get a Job" is a movie distributed by Lionsgate Premiere. [alce::823__wikidata_simple__dev::p0]
> Additionally, "Joshy" is a movie released by Lionsgate Premiere. [alce::823__wikidata_simple__dev::p0]

Cited: alce::823__wikidata_simple__dev::p0

### `543__wikitables_simple__dev`
> Members of the 10cc band include:

Graham Gouldman was a founding member and multi-instrumentalist of 10cc. [alce::543__wikitables_simple__dev::p1]
> Eric Stewart was a founding member and multi-instrumentalist of 10cc. [alce::543__wikitables_simple__dev::p1]
> Kevin Godley was a founding member and multi-instrumentalist of 10cc. [alce::543__wikitables_simple__dev::p1]
> Lol Creme was a founding member and multi-instrumentalist of 10cc. [alce::543__wikitables_simple__dev::p1]
> Rick Fenn has been a member of the band 10cc since 1976. [alce::543__wikitables_simple__dev::p3]

Cited: alce::543__wikitables_simple__dev::p1, alce::543__wikitables_simple__dev::p3

### `838__wikidata_simple__dev`
> Many entities were part of NATO. The founding members included Belgium, Canada, Denmark, France, Iceland, Italy, Luxembourg, the Netherlands, Norway, Portugal, the United Kingdom, and the United States. [alce::838__wikidata_simple__dev::p8]
> Greece and Turkey joined NATO in 1952. [alce::838__wikidata_simple__dev::p8]
> Albania and Croatia joined on 1 April 2009. [alce::838__wikidata_simple__dev::p92]
> Montenegro joined on 5 June 2017 as the most recent member state. [alce::838__wikidata_simple__dev::p92]

Cited: alce::838__wikidata_simple__dev::p8, alce::838__wikidata_simple__dev::p92

### `1014__wikidata_comp__dev`
> N-class destroyer ships were operated by the Royal Navy and the Royal Australian Navy. [alce::1014__wikidata_comp__dev::p0]
> The Royal Australian Navy operated at least one N-class destroyer, HMAS Nepal (G25), which was launched in 1941 and commissioned into the RAN in 1942, though it remained the property of the Royal Navy. [alce::1014__wikidata_comp__dev::p89]

Cited: alce::1014__wikidata_comp__dev::p0, alce::1014__wikidata_comp__dev::p89

### `687__wikidata_simple__dev`
_Refused._

### `87__wikitables_composition__dev`
_Refused._

### `910__wikidata_simple__dev`
> "Actuality Specials" is an American television series produced by NBC News. [alce::910__wikidata_simple__dev::p7]
> Additionally, "NBC Nightly News" and "Meet The Press" are television series produced by NBC News. [alce::910__wikidata_simple__dev::p3]

Cited: alce::910__wikidata_simple__dev::p3, alce::910__wikidata_simple__dev::p7

### `34__wikitables_composition__dev`
> Eddie Anderson coached the Iowa Hawkeyes football team during the following seasons: 1939–1942 and 1946–1949. [alce::34__wikitables_composition__dev::p8]
> More specifically, he coached in 1939 [alce::34__wikitables_composition__dev::p86]
> , returned for his fifth season in 1946 [alce::34__wikitables_composition__dev::p5]
> , and his seventh and final season in 1948 [alce::34__wikitables_composition__dev::p4]
> .

Cited: alce::34__wikitables_composition__dev::p4, alce::34__wikitables_composition__dev::p5, alce::34__wikitables_composition__dev::p8, alce::34__wikitables_composition__dev::p86

### `842__wikidata_simple__dev`
> Professor Garry W. Jenkins was part of the University of Minnesota Law School staff, serving as the law school's 11th dean. [alce::842__wikidata_simple__dev::p3]

Cited: alce::842__wikidata_simple__dev::p3

### `489__wikitables_simple__dev`
> Based on the provided sources, here are the different professional wrestling streaming services:

WWE Network is a subscription-based video streaming service owned by the WWE. [alce::489__wikitables_simple__dev::p8]
> New Japan Pro-Wrestling World (also referred to as NJPW World) is a subscription-based video streaming service owned by New Japan Pro-Wrestling. [alce::489__wikitables_simple__dev::p7]
> Global Wrestling Network (GWN) is a video streaming service and mobile app owned by Anthem Wrestling Exhibitions, a subsidiary of Anthem Sports & Entertainment and parent company of Impact Wrestling. [alce::489__wikitables_simple__dev::p60]
> World Wrestling Network (WWN) is an internet streaming and video on demand service originating from the United States. [alce::489__wikitables_simple__dev::p14]
> Club WWN is a replacement streaming service launched by WWNLive. [alce::489__wikitables_simple__dev::p14]

Cited: alce::489__wikitables_simple__dev::p14, alce::489__wikitables_simple__dev::p60, alce::489__wikitables_simple__dev::p7, alce::489__wikitables_simple__dev::p8

### `1361__wikidata_simple__dev`
> Richard Sandomir is a writer for the New York Times. [alce::1361__wikidata_simple__dev::p86]
> Charles M. Blow is a visual op-ed columnist for The New York Times. [alce::1361__wikidata_simple__dev::p54]
> Tina Rosenberg is a longtime New York Times writer. [alce::1361__wikidata_simple__dev::p23]

Cited: alce::1361__wikidata_simple__dev::p23, alce::1361__wikidata_simple__dev::p54, alce::1361__wikidata_simple__dev::p86

### `614__wikidata_simple__dev`
_Refused._

### `54__wikitables_composition__dev`
_Refused._

### `142__wikidata_intersection__dev`
> Robert Zemeckis and Bob Gale were screenwriters together for "Back to the Future." [alce::142__wikidata_intersection__dev::p0]
> They also co-wrote the screenplays for the film's two sequels. [alce::142__wikidata_intersection__dev::p0]

Cited: alce::142__wikidata_intersection__dev::p0

### `209__wikidata_intersection__dev`
_Refused._

### `510__wikitables_simple__dev`
> Based on the provided sources, several ships are identified as river cruise ships:

"Crystal Bach" and "Crystal Mahler" are river cruise ships of the Rhine class. [alce::510__wikitables_simple__dev::p40]
> "Crystal Mozart" is a river cruise ship and is described as Europe's most spacious river ship. [alce::510__wikitables_simple__dev::p6]

Cited: alce::510__wikitables_simple__dev::p40, alce::510__wikitables_simple__dev::p6

### `762__wikidata_simple__dev`
_Refused._

### `188__wikidata_intersection__dev`
> "Jeevan Prabhat" (Dawn Of Life) is a 1937 Hindi film that was directed by Franz Osten and had music composed by Saraswati Devi. [alce::188__wikidata_intersection__dev::p3]

Cited: alce::188__wikidata_intersection__dev::p3

### `906__wikidata_simple__dev`
> Adithyan composed music for over 30 films including "Amaran" (1992), "Maman Magal", "Luckyman", "Asuran", "Sevaalaperi Paandi", and "Kovilpatti Veeralakshmi". [alce::906__wikidata_simple__dev::p0]

Cited: alce::906__wikidata_simple__dev::p0

### `546__wikitables_simple__dev`
> Notable landslides occurred in several places:

In California, landslides are common in Southern California, the San Francisco Bay Area and other parts of Northern California, and the Sierra Nevada. [alce::546__wikitables_simple__dev::p0]
> In New Zealand, notable landslides occurred in Napier, where several tonnes of rock fell from Bluff Hill during an earthquake, and near Wimbledon, with the largest landslide being near the top of Sergeant's Hill, about a 40–50 meter wide slump that took down hundreds of trees. [alce::546__wikitables_simple__dev::p5]
> In Germany, major landslides occurred on 3 June 2013 in the Öschingen cottage settlement area, as well as on the southwest side of the Farrenberg, on Buchberg, at the Talheim waterfalls and at the Talheim platforms. [alce::546__wikitables_simple__dev::p20]

Cited: alce::546__wikitables_simple__dev::p0, alce::546__wikitables_simple__dev::p20, alce::546__wikitables_simple__dev::p5

### `207__wikidata_comp__dev`
> The movie "Passengers" had Jon Spaihts as its screenwriter. [alce::207__wikidata_comp__dev::p2]
> This film was distributed by Sony Pictures. [alce::207__wikidata_comp__dev::p2]

Cited: alce::207__wikidata_comp__dev::p2

### `977__wikidata_comp__dev`
_Refused._

### `1009__wikidata_comp__dev`
> Several golfers have won the Evian Championship:

Chun In-gee won the 2016 Evian Championship, her first Evian and second major championship. [alce::1009__wikidata_comp__dev::p0]
> Lydia Ko won the 2015 Evian Championship, her first major championship at age 18. [alce::1009__wikidata_comp__dev::p1]
> Angela Stanford won the 2018 Evian Championship, her first major championship at age 40. [alce::1009__wikidata_comp__dev::p2]
> Inbee Park won the Evian Masters (as it was called at the time) in 2012. [alce::1009__wikidata_comp__dev::p24]

Cited: alce::1009__wikidata_comp__dev::p0, alce::1009__wikidata_comp__dev::p1, alce::1009__wikidata_comp__dev::p2, alce::1009__wikidata_comp__dev::p24

### `276__wikidata_comp__dev`
> David Nicholls screenwrote a film directed by Lone Scherfig. [alce::276__wikidata_comp__dev::p37]

Cited: alce::276__wikidata_comp__dev::p37

### `747__wikidata_simple__dev`
> Based on the provided sources, several individuals worked for military branches of the Kingdom of Prussia:

King Frederick William I of Prussia dramatically increased the size of the Prussian Army and improved its doctrines. [alce::747__wikidata_simple__dev::p1]
> King Frederick the Great led the disciplined Prussian troops as a formidable battle commander during the 18th-century Silesian Wars. [alce::747__wikidata_simple__dev::p1]
> An individual engaged himself to King Frederick William III of Prussia, who gave him a patent of nobility, the rank of lieutenant-colonel, and employment at the Prussian Military Academy in important instructional work. [alce::747__wikidata_simple__dev::p77]
> Field Marshal Helmuth von Moltke controlled the Prussian army as head of the General Staff. [alce::747__wikidata_simple__dev::p6]

Cited: alce::747__wikidata_simple__dev::p1, alce::747__wikidata_simple__dev::p6, alce::747__wikidata_simple__dev::p77

### `796__wikidata_simple__dev`
> Zee Horror Show is a television show that was a creation of Zee TV. [alce::796__wikidata_simple__dev::p0]
> It was presented by Ramsay Brothers and aired on Zee TV during the period 1993-1997. [alce::796__wikidata_simple__dev::p0]

Cited: alce::796__wikidata_simple__dev::p0

### `856__wikidata_simple__dev`
> Porto Velho is the capital of the Brazilian state of Rondônia, located in the upper Amazon River basin. [alce::856__wikidata_simple__dev::p1]
> It is situated on the eastern shore of the Madeira River, one of the main tributaries of the Amazon River. [alce::856__wikidata_simple__dev::p1]
> The town is located on the border of Rondônia and the state of Amazonas. [alce::856__wikidata_simple__dev::p1]

Cited: alce::856__wikidata_simple__dev::p1

### `151__wikidata_intersection__dev`
> The movie directed by Saran with musical composition by Bharathwaj is "Kaadhal Mannan". [alce::151__wikidata_intersection__dev::p2]
> This was Saran's first film, and it marked the debut of music composer Bharathwaj. [alce::151__wikidata_intersection__dev::p2]

Cited: alce::151__wikidata_intersection__dev::p2

### `392__wikidata_intersection__dev`
> "Goldfinger" was a Guy Hamilton-directed movie for which Harry Saltzman was responsible for production. [alce::392__wikidata_intersection__dev::p34]

Cited: alce::392__wikidata_intersection__dev::p34

### `580__wikidata_simple__dev`
> Based on the provided sources, Whitehawk F.C. has had multiple coaches:

Steve King was re-appointed as manager on 13 September 2017. [alce::580__wikidata_simple__dev::p3]
> Jude Macdonald replaced King at the end of the season, coming from his role as Hawks successful U18 manager. [alce::580__wikidata_simple__dev::p3]
> James Dack was most recently first team manager at Whitehawk. [alce::580__wikidata_simple__dev::p16]

Cited: alce::580__wikidata_simple__dev::p16, alce::580__wikidata_simple__dev::p3

### `701__wikidata_simple__dev`
> Tony Levin is best known for his work with King Crimson and Peter Gabriel. [alce::701__wikidata_simple__dev::p0]
> He has also been a member of several other bands including Liquid Tension Experiment, Bruford Levin Upper Extremities, ProjeKct One, and ProjeKct Four. [alce::701__wikidata_simple__dev::p0]
> Additionally, he has led his own band, Stick Men. [alce::701__wikidata_simple__dev::p0]

Cited: alce::701__wikidata_simple__dev::p0

### `168__wikidata_comp__dev`
> Dan Gilroy directed "Nightcrawler" (2014), the movie for which he wrote the screenplay. [alce::168__wikidata_comp__dev::p0]

Cited: alce::168__wikidata_comp__dev::p0

### `785__wikidata_simple__dev`
> Janine Marmot produced several movies, including the BAFTA-winning documentary Bodysong [alce::785__wikidata_simple__dev::p1]
> , the relationship drama Kelly + Victor, which won the Outstanding British Debut BAFTA award in 2014 [alce::785__wikidata_simple__dev::p1]
> , No Greater Love [alce::785__wikidata_simple__dev::p1]
> , Looking For Light [alce::785__wikidata_simple__dev::p1]
> , Institute Benjamenta directed by The Brothers Quay [alce::785__wikidata_simple__dev::p1]
> , I Could Read The Sky directed by Nichola Bruce [alce::785__wikidata_simple__dev::p0]
> , and Made In Heaven [alce::785__wikidata_simple__dev::p1]
> .

Cited: alce::785__wikidata_simple__dev::p0, alce::785__wikidata_simple__dev::p1

### `761__wikidata_simple__dev`
_Refused._

### `340__wikidata_comp__dev`
_Refused._

### `792__wikidata_simple__dev`
> The Defoe Shipbuilding Company produced multiple types of marine vessels. During World War II, from 1939 to 1945, the company built 154 ships, including four destroyer escorts, 13 destroyer escorts, 11 destroyer transports (converted destroyer escorts), patrol craft, and numerous landing craft of various types. [alce::792__wikidata_simple__dev::p2]
> In the early 1950s, Defoe Shipbuilding constructed two large Great Lakes freighters, including the M/V "Ojibway," a 642' 03" long bulk freight vessel. [alce::792__wikidata_simple__dev::p4]
> The company also built various government and commercial vessels, private yachts, and Coast Guard Cutters from 1920 to 1939. [alce::792__wikidata_simple__dev::p3]

Cited: alce::792__wikidata_simple__dev::p2, alce::792__wikidata_simple__dev::p3, alce::792__wikidata_simple__dev::p4

### `458__wikidata_intersection__dev`
> The 1974 FA Cup Final featured both Liverpool and Newcastle United as participants. [alce::458__wikidata_intersection__dev::p15]
> This match took place on Saturday, 4 May 1974 at Wembley Stadium in London, and Liverpool won the competition by defeating Newcastle United 3–0. [alce::458__wikidata_intersection__dev::p4]
> Additionally, Liverpool and Newcastle United also competed against each other in a Premier League fixture on 3 April 1996 at Anfield. [alce::458__wikidata_intersection__dev::p3]

Cited: alce::458__wikidata_intersection__dev::p15, alce::458__wikidata_intersection__dev::p3, alce::458__wikidata_intersection__dev::p4

### `888__wikidata_simple__dev`
> Brent Park is an area found adjacent to River Brent. [alce::888__wikidata_simple__dev::p96]

Cited: alce::888__wikidata_simple__dev::p96

### `839__wikidata_simple__dev`
> Alan Grant created several imaginary beings. He is the creator of the characters Anarky, Victor Zsasz, and the Ventriloquist. [alce::839__wikidata_simple__dev::p0]
> Anarky was initially intended as a vehicle for exploring his political opinions through the comic medium. [alce::839__wikidata_simple__dev::p2]

Cited: alce::839__wikidata_simple__dev::p0, alce::839__wikidata_simple__dev::p2

### `724__wikidata_simple__dev`
> San Diego is the home port for approximately 54 ships, including 46 U.S. Navy ships, two Littoral Combat Ships, two U.S. Coast Guard cutters, and eight ships of the Military Sealift Command. [alce::724__wikidata_simple__dev::p28]
> Additionally, several cruise lines home port in San Diego, such as Holland America, Celebrity Cruises, Disney Cruise Line, and Royal Caribbean. [alce::724__wikidata_simple__dev::p0]

Cited: alce::724__wikidata_simple__dev::p0, alce::724__wikidata_simple__dev::p28

### `363__wikidata_comp__dev`
> Greg Hawkes, a member of The Cars, attended Berklee College of Music. [alce::363__wikidata_comp__dev::p2]

Cited: alce::363__wikidata_comp__dev::p2

### `107__wikidata_intersection__dev`
> Lewis Hamilton won the Hungarian Grand Prix four times: in 2007, 2009, 2012, and 2013. [alce::107__wikidata_intersection__dev::p1]
> Specifically, he won the 2009 Hungarian Grand Prix for McLaren-Mercedes after starting from fourth place on the grid. [alce::107__wikidata_intersection__dev::p3]
> He also won the 2013 Hungarian Grand Prix for Mercedes after starting from pole position. [alce::107__wikidata_intersection__dev::p2]

Cited: alce::107__wikidata_intersection__dev::p1, alce::107__wikidata_intersection__dev::p2, alce::107__wikidata_intersection__dev::p3

### `574__wikidata_simple__dev`
> The first full-length Konkani film was "Mogacho Anvddo", released on 24 April 1950. [alce::574__wikidata_simple__dev::p0]

Cited: alce::574__wikidata_simple__dev::p0

### `501__wikitables_simple__dev`
> Rodney Agatupu Anoai was a yokozuna, an American professional wrestler who wrestled under the ring name Yokozuna in the World Wrestling Federation (WWF). [alce::501__wikitables_simple__dev::p0]
> Additionally, several sumo wrestlers held the yokozuna rank in Japan. Akashi Shiganosuke is purported to be formally recognized as the first yokozuna. [alce::501__wikitables_simple__dev::p10]
> Tanikaze was the first to receive a "yokozuna" licence and is often regarded as the first "real" yokozuna. [alce::501__wikitables_simple__dev::p10]
> Kitanofuji and Chiyonofuji also reached the yokozuna rank. [alce::501__wikitables_simple__dev::p72]

Cited: alce::501__wikitables_simple__dev::p0, alce::501__wikitables_simple__dev::p10, alce::501__wikitables_simple__dev::p72

### `1300__wikidata_simple__dev`
> Dr. James Hal Cone is a member of the Union Theological Seminary staff. [alce::1300__wikidata_simple__dev::p3]
> Dr. Gary Dorrien is a member of the Union Theological Seminary staff. [alce::1300__wikidata_simple__dev::p3]
> Delores S. Williams is a member of the Union Theological Seminary staff. [alce::1300__wikidata_simple__dev::p3]
> Dr. James A. Forbes is an adjunct professor at Union Theological Seminary. [alce::1300__wikidata_simple__dev::p3]

Cited: alce::1300__wikidata_simple__dev::p3

### `390__wikidata_comp__dev`
> Vetrimaaran created the script for a movie under the production of Dhanush. [alce::390__wikidata_comp__dev::p19]
> Vetrimaaran prepared a script for Dhanush, who was the lead hero of the film titled "Desiya Nedunchalai 47," and Dhanush immediately accepted the offer after hearing the story. [alce::390__wikidata_comp__dev::p64]

Cited: alce::390__wikidata_comp__dev::p19, alce::390__wikidata_comp__dev::p64

### `887__wikidata_simple__dev`
> Tesla produces the Model S, Model X, and Model 3. [alce::887__wikidata_simple__dev::p1]

Cited: alce::887__wikidata_simple__dev::p1

### `878__wikidata_simple__dev`
_Refused._

### `752__wikidata_simple__dev`
> Ivan Goff had screenwriting credits on the following films:

"White Heat" (1949) [alce::752__wikidata_simple__dev::p0]
> "Man of a Thousand Faces" (1957) [alce::752__wikidata_simple__dev::p0]
> "Charlie's Angels" pilot (1976) [alce::752__wikidata_simple__dev::p0]
> "The Captain from Köpenick" (1945) [alce::752__wikidata_simple__dev::p8]
> "Portrait in Black" (1960) [alce::752__wikidata_simple__dev::p15]
> "Captain Horatio Hornblower" (1951) [alce::752__wikidata_simple__dev::p9]
> "Into the Night" [alce::752__wikidata_simple__dev::p15]

Cited: alce::752__wikidata_simple__dev::p0, alce::752__wikidata_simple__dev::p15, alce::752__wikidata_simple__dev::p8, alce::752__wikidata_simple__dev::p9

### `423__wikidata_comp__dev`
> Utah Jazz draftees are citizens of multiple countries. Andrei Kirilenko, who was drafted by the Utah Jazz in 1999, is Russian-American. [alce::423__wikidata_comp__dev::p86]
> Dante Exum, who was selected by the Utah Jazz with the fifth overall pick in the 2014 draft, is Australian. [alce::423__wikidata_comp__dev::p2]
> Joe Ingles, a professional basketball player for the Utah Jazz, is Australian. [alce::423__wikidata_comp__dev::p9]

Cited: alce::423__wikidata_comp__dev::p2, alce::423__wikidata_comp__dev::p86, alce::423__wikidata_comp__dev::p9

### `214__wikidata_comp__dev`
> Based on the provided sources, alumni of St. Charles Borromeo Seminary hold the following positions:

Rector of St. Charles Borromeo Seminary. [alce::214__wikidata_comp__dev::p30]
> Dean, Theology Division, Saint Charles Borromeo Seminary. [alce::214__wikidata_comp__dev::p10]
> Chief Academic Officer, Saint Charles Borromeo Seminary. [alce::214__wikidata_comp__dev::p30]
> Pastor of parishes, including Our Lady of Grace in Penndel, Pennsylvania and St. John the Evangelist in Morrisville, Pennsylvania. [alce::214__wikidata_comp__dev::p10]
> Associate Pastor. [alce::214__wikidata_comp__dev::p10]
> Diocesan Superintendent of Schools.
> Assistant principal of Roman Catholic High School.
> Assistant rector of a church.
> Censor Librorum for the Archdiocese of Philadelphia. [alce::214__wikidata_comp__dev::p10]
> Faculty member in theology and religious studies. [alce::214__wikidata_comp__dev::p10]

Cited: alce::214__wikidata_comp__dev::p10, alce::214__wikidata_comp__dev::p30

### `304__wikidata_comp__dev`
_Refused._

### `411__wikidata_intersection__dev`
> Based on the provided sources, there are multiple directors named Ranjith who both directed and screen wrote films:

Ranjith Bajpe both directed and screen wrote "Dhand" (2015), which is the first Tulu language movie released in Israel, Australia and UK. [alce::411__wikidata_intersection__dev::p45]
> Additionally, Pa. Ranjith written and directed the gangster-drama "Kabali" in 2016 and "Kaala" in 2018. [alce::411__wikidata_intersection__dev::p52]
> Furthermore, Ranjith (Balakrishnan) co-produced, written, and directed "Thirakkatha" (2008), a Malayalam romantic drama film. [alce::411__wikidata_intersection__dev::p6]

Cited: alce::411__wikidata_intersection__dev::p45, alce::411__wikidata_intersection__dev::p52, alce::411__wikidata_intersection__dev::p6

### `84__wikitables_composition__dev`
_Refused._

### `153__wikidata_intersection__dev`
> Based on the provided sources, multiple Woody Allen films had both screenwriter Woody Allen and composer Dick Hyman on board.

These films include: "Zelig", "The Purple Rose of Cairo", "Broadway Danny Rose", "Stardust Memories", "Hannah and Her Sisters", "Radio Days", "Bullets Over Broadway", "Everyone Says I Love You", "Sweet and Lowdown", "The Curse of the Jade Scorpion", and "Melinda and Melinda". [alce::153__wikidata_intersection__dev::p0]
> Additionally, Dick Hyman served as music coordinator, arranger, and conductor for Allen's "Mighty Aphrodite". [alce::153__wikidata_intersection__dev::p0]

Cited: alce::153__wikidata_intersection__dev::p0

### `65__wikitables_composition__dev`
> Skövde Municipality is the municipality of the urban area of Skövde. [alce::65__wikitables_composition__dev::p2]

Cited: alce::65__wikitables_composition__dev::p2

### `265__wikidata_comp__dev`
> Lake Superior can be found near a state in the U.S. [alce::265__wikidata_comp__dev::p7]
> The Great Lakes, including Lake Erie and Lake Ontario, are also bodies of water near U.S. states. [alce::265__wikidata_comp__dev::p7]
> Additionally, the Mississippi River and Ohio River border U.S. states. [alce::265__wikidata_comp__dev::p74]

Cited: alce::265__wikidata_comp__dev::p7, alce::265__wikidata_comp__dev::p74

### `215__wikidata_intersection__dev`
> Richard Brooks received multiple credits including writing and directing for several films. He wrote and directed "In Cold Blood" (1967) [alce::215__wikidata_intersection__dev::p1]
> , and he also wrote and directed "Elmer Gantry" (1960), for which he won the Academy Award for Best Adapted Screenplay [alce::215__wikidata_intersection__dev::p1]
> . Additionally, he wrote and directed "Blackboard Jungle" (1955) [alce::215__wikidata_intersection__dev::p1]
> .

Cited: alce::215__wikidata_intersection__dev::p1

### `98__wikitables_composition__dev`
_Refused._

### `853__wikidata_simple__dev`
_Refused._

### `112__wikidata_comp__dev`
> Based on the provided sources, Aline Brosh McKenna wrote multiple screenplays. For "Annie" (2014), the director was Will Gluck. [alce::112__wikidata_comp__dev::p6]
> For "We Bought a Zoo" (2011), the sources do not specify the director. [alce::112__wikidata_comp__dev::p6]
> If you are asking about a specific film, the most complete answer from these sources is: Will Gluck directed "Annie," which Aline Brosh McKenna wrote for the screen. [alce::112__wikidata_comp__dev::p6]

Cited: alce::112__wikidata_comp__dev::p6

### `357__wikidata_intersection__dev`
> The 1964 VFL Grand Final was a competition that the Collingwood Football Club participated in and was won by the Melbourne Football Club. [alce::357__wikidata_intersection__dev::p70]

Cited: alce::357__wikidata_intersection__dev::p70

### `877__wikidata_simple__dev`
> J-Bus constructed the Isuzu Erga, a heavy-duty single-decker bus. [alce::877__wikidata_simple__dev::p86]
> J-Bus also built the Hino Rainbow, a medium-duty single-decker bus. [alce::877__wikidata_simple__dev::p32]

Cited: alce::877__wikidata_simple__dev::p32, alce::877__wikidata_simple__dev::p86

### `709__wikidata_simple__dev`
> Vice-Admiral Muzaffar Hassan served in the Pakistan Navy, where he was a three-star rank admiral who served as the last Commander-in-Chief of Pakistan Navy from 1969 until 1972. [alce::709__wikidata_simple__dev::p52]
> Admiral Zafar Mahmood Abbasi served in the Pakistan Navy as a four-star rank admiral and Chief of the Naval Staff since 7 October 2017, having joined the Pakistan Navy in 1979. [alce::709__wikidata_simple__dev::p67]
> Karimullah also served in the Pakistan Navy, joining in October 1965 after being trained at the Pakistan Military Academy and the Royal Navy's HMS Mercury. [alce::709__wikidata_simple__dev::p20]

Cited: alce::709__wikidata_simple__dev::p20, alce::709__wikidata_simple__dev::p52, alce::709__wikidata_simple__dev::p67

### `488__wikitables_simple__dev`
> Based on the provided sources, the following weapons are identified as carbines:

The Sturmgewehr 44, M16A1, FN FAL, FN CAL, Heckler & Koch G3, SIG SG 543, and SIG SG 542 are listed among carbines. [alce::488__wikitables_simple__dev::p13]
> Additionally, historical examples of recognizable carbines include the lever-action Winchester carbines, which fired revolver cartridges. [alce::488__wikitables_simple__dev::p17]
> The Lee Enfield Cavalry Carbine (LEC), a shortened version of the standard British Army infantry rifle introduced in 1896, is also identified as a carbine. [alce::488__wikitables_simple__dev::p17]

Cited: alce::488__wikitables_simple__dev::p13, alce::488__wikitables_simple__dev::p17

### `348__wikidata_comp__dev`
> Andrew Bovell wrote the screenplay for "A Most Wanted Man," which was directed by Anton Corbijn. [alce::348__wikidata_comp__dev::p0]

Cited: alce::348__wikidata_comp__dev::p0

### `912__wikidata_simple__dev`
> "The Circle" is a film produced by Jafar Panahi. [alce::912__wikidata_simple__dev::p2]

Cited: alce::912__wikidata_simple__dev::p2

### `266__wikidata_intersection__dev`
> Michael Mann produced and directed several films. His most acclaimed works include "Thief" (1981), "Manhunter" (1986), "Heat" (1995), "Collateral" (2004), "The Last of the Mohicans" (1992), and "The Insider" (1999). [alce::266__wikidata_intersection__dev::p2]
> He also directed the film adaptation of "Miami Vice," which he adapted from the TV series and also executive produced. [alce::266__wikidata_intersection__dev::p1]

Cited: alce::266__wikidata_intersection__dev::p1, alce::266__wikidata_intersection__dev::p2

### `74__wikitables_composition__dev`
_Refused._

### `890__wikidata_simple__dev`
> Based on the provided sources, John James (architect) created St Mary's Church in Twickenham. [alce::890__wikidata_simple__dev::p0]
> He also built Orleans House, a house for James Johnson, Secretary of State for Scotland, though this building has since been demolished. [alce::890__wikidata_simple__dev::p0]

Cited: alce::890__wikidata_simple__dev::p0

### `1013__wikidata_comp__dev`
_Refused._

### `581__wikidata_simple__dev`
> Thomas Hardwick designed several buildings. He designed the church of St Mary the Virgin at Wanstead, completed in 1790. [alce::581__wikidata_simple__dev::p48]
> He also designed St John's Church in St John's Wood High Street (1813–14) and the church of St Mary in Marylebone Road (1813–17). [alce::581__wikidata_simple__dev::p29]
> Additionally, he restored Sir Christopher Wren's St James, Piccadilly and re-built George Dance the Younger's St Bartholomew-the-Less in West Smithfield (1823–25). [alce::581__wikidata_simple__dev::p29]

Cited: alce::581__wikidata_simple__dev::p29, alce::581__wikidata_simple__dev::p48

### `345__wikidata_comp__dev`
_Refused._

### `294__wikidata_comp__dev`
> Based on the provided sources, I can identify one director who worked with Vijay Tendulkar as screenwriter:

Satyadev Dubey directed the 1971 movie "Śāntatā! Court Cālū Āhe" ("Silence! The Court Is in Session"), for which Tendulkar wrote the screenplay. [alce::294__wikidata_comp__dev::p26]
> Additionally, Jabbar Patel directed "Umbartha" ("The Threshold") (1981), which Tendulkar wrote the screenplay for. [alce::294__wikidata_comp__dev::p0]

Cited: alce::294__wikidata_comp__dev::p0, alce::294__wikidata_comp__dev::p26

### `1__wikitables_composition__dev`
> Marko Arnautović transferred to Stoke City in the summer of 2013. [alce::1__wikitables_composition__dev::p15]
> He joined on 2 September 2013 on a four-year contract for a fee of £2 million. [alce::1__wikitables_composition__dev::p15]

Cited: alce::1__wikitables_composition__dev::p15

### `337__wikidata_comp__dev`
_Refused._

### `571__wikidata_simple__dev`
> Several individuals have held the position of Chief of the National Guard Bureau:

Earl T. Ricks served as acting Chief of the National Guard Bureau in 1953, making him the first Air Guard officer to hold the chief's position. [alce::571__wikidata_simple__dev::p6]
> Robert F. Wilson was appointed chief of the National Guard Bureau in 1963, becoming the first Air Force officer to be officially named to the position. [alce::571__wikidata_simple__dev::p33]
> La Vern E. Weber became the first NGB chief to hold the position after it was upgraded from major general to lieutenant general in the mid-1970s. [alce::571__wikidata_simple__dev::p6]
> Joseph L. Lengyel has served as Chief of the National Guard Bureau since 2016. [alce::571__wikidata_simple__dev::p37]

Cited: alce::571__wikidata_simple__dev::p33, alce::571__wikidata_simple__dev::p37, alce::571__wikidata_simple__dev::p6

### `942__wikidata_simple__dev`
> Bryan Fuller served as executive producer for several TV series based on the provided sources.

He was expected to write the pilot episode and executive produce a series created by Steven Spielberg. [alce::942__wikidata_simple__dev::p54]
> He served as showrunner and co-creator of "Star Trek: Discovery" alongside Alex Kurtzman. [alce::942__wikidata_simple__dev::p26]
> Additionally, Bryan Fuller has created television series including "Dead Like Me", "Wonderfalls", "Pushing Daisies", "Hannibal", and "American Gods". [alce::942__wikidata_simple__dev::p1]

Cited: alce::942__wikidata_simple__dev::p1, alce::942__wikidata_simple__dev::p26, alce::942__wikidata_simple__dev::p54

### `101__wikidata_intersection__dev`
> Based on the provided sources, Manchester United F.C. and Arsenal F.C. featured in the following contests:

A Football League First Division fixture took place on 20 October 1990 at Old Trafford during the 1990–91 season, which was best remembered for a brawl between both teams. [alce::101__wikidata_intersection__dev::p8]
> The 1999 FA Charity Shield was contested between Manchester United and Arsenal at Wembley Stadium on 1 August. [alce::101__wikidata_intersection__dev::p15]
> The 2003 FA Community Shield was contested between Manchester United and Arsenal at Cardiff's Millennium Stadium on 10 August. [alce::101__wikidata_intersection__dev::p97]
> Additionally, the two clubs have frequently clashed in the Premier League and FA Cup during the late 1990s and early 2000s. [alce::101__wikidata_intersection__dev::p3]

Cited: alce::101__wikidata_intersection__dev::p15, alce::101__wikidata_intersection__dev::p3, alce::101__wikidata_intersection__dev::p8, alce::101__wikidata_intersection__dev::p97

### `922__wikidata_simple__dev`
> Paul Kupperberg created the "Takion" series. [alce::922__wikidata_simple__dev::p6]

Cited: alce::922__wikidata_simple__dev::p6

### `585__wikidata_simple__dev`
> Charles Keeping made illustrations for several books. He illustrated Rosemary Sutcliff's historical novels for children. [alce::585__wikidata_simple__dev::p0]
> He illustrated the complete works of Charles Dickens for the Folio Society. [alce::585__wikidata_simple__dev::p0]
> He drew fifteen illustrations for "The God Beneath the Sea". [alce::585__wikidata_simple__dev::p11]
> He illustrated an edition of Emily Brontë's "Wuthering Heights" in 1964. [alce::585__wikidata_simple__dev::p2]
> He illustrated Erich Maria Remarque's "All Quiet on the Western Front" (1966). [alce::585__wikidata_simple__dev::p2]
> He illustrated Alfred Noyes's poem "The Highwayman". [alce::585__wikidata_simple__dev::p0]

Cited: alce::585__wikidata_simple__dev::p0, alce::585__wikidata_simple__dev::p11, alce::585__wikidata_simple__dev::p2

### `807__wikidata_simple__dev`
> The Townsend Farmers' Mutual Fire Insurance Company was headquartered in Waterford, County Waterford. [alce::807__wikidata_simple__dev::p6]

Cited: alce::807__wikidata_simple__dev::p6

### `129__wikidata_intersection__dev`
> Blackburn Rovers F.C. competed in multiple FA Cup Finals. They played in the 1882 FA Cup Final, where they lost 1–0 to Old Etonians. [alce::129__wikidata_intersection__dev::p74]
> They also competed in the 1884 FA Cup Final against Queen's Park Glasgow, which they won 2–1. [alce::129__wikidata_intersection__dev::p74]
> Additionally, Blackburn Rovers faced Queen's Park Glasgow in the FA Cup Final on 4 April 1885, winning 2–0. [alce::129__wikidata_intersection__dev::p74]

Cited: alce::129__wikidata_intersection__dev::p74

### `795__wikidata_simple__dev`
_Refused._

### `451__wikidata_intersection__dev`
_Refused._

### `329__wikidata_intersection__dev`
> The San Francisco 49ers competed in Super Bowls XVI, XIX, XXIII, XXIV, and XXIX. [alce::329__wikidata_intersection__dev::p1]
> They were the first team to win five Super Bowls. [alce::329__wikidata_intersection__dev::p1]
> Additionally, the 49ers competed in Super Bowl XLVII, which featured brothers Jim Harbaugh (San Francisco's head coach) and John Harbaugh (Baltimore's head coach) as opposing head coaches. [alce::329__wikidata_intersection__dev::p88]

Cited: alce::329__wikidata_intersection__dev::p1, alce::329__wikidata_intersection__dev::p88

### `43__wikitables_composition__dev`
> Based on the provided sources, I can identify the following municipalities in Cameron County, Pennsylvania:

Shippen Township is a township in Cameron County, Pennsylvania. [alce::43__wikitables_composition__dev::p11]
> Lumber Township is a township in Cameron County, Pennsylvania. [alce::43__wikitables_composition__dev::p10]
> Portage Township is located in Cameron County, as it borders Lumber Township. [alce::43__wikitables_composition__dev::p10]
> Grove Township is located in Cameron County, as it borders Lumber Township. [alce::43__wikitables_composition__dev::p10]
> Gibson Township is located in Cameron County, as it borders Lumber Township. [alce::43__wikitables_composition__dev::p10]
> Emporium is a borough in Cameron County and serves as the county seat. [alce::43__wikitables_composition__dev::p6]
> The sources indicate that "the following boroughs and townships are located in Cameron County" but do not provide a complete list of all municipalities in the source text provided. [alce::43__wikitables_composition__dev::p1]

Cited: alce::43__wikitables_composition__dev::p1, alce::43__wikitables_composition__dev::p10, alce::43__wikitables_composition__dev::p11, alce::43__wikitables_composition__dev::p6

### `370__wikidata_intersection__dev`
> The River-class frigate was produced by Canadian Vickers. [alce::370__wikidata_intersection__dev::p17]

Cited: alce::370__wikidata_intersection__dev::p17

### `229__wikidata_intersection__dev`
> Carlton Football Club competed in multiple VFL/AFL Grand Finals. [alce::229__wikidata_intersection__dev::p2]
> The club has been involved in 29 VFL/AFL Grand Finals from 1897-2006, winning 16 premiership titles. [alce::229__wikidata_intersection__dev::p2]
> Specific Grand Finals mentioned in the sources include the 1909 VFL Grand Final against South Melbourne Football Club, held at the Melbourne Cricket Ground on 2 October 1909. [alce::229__wikidata_intersection__dev::p34]
> Carlton also competed in the 1981 VFL Grand Final against Collingwood Football Club, held at the Melbourne Cricket Ground on 26 September 1981, which Carlton won by 20 points. [alce::229__wikidata_intersection__dev::p6]

Cited: alce::229__wikidata_intersection__dev::p2, alce::229__wikidata_intersection__dev::p34, alce::229__wikidata_intersection__dev::p6

### `673__wikidata_simple__dev`
> The Florida Reef, the only barrier coral reef in North America and the third-largest coral barrier reef in the world, can be found within the Florida Keys National Marine Sanctuary. [alce::673__wikidata_simple__dev::p1]

Cited: alce::673__wikidata_simple__dev::p1

### `256__wikidata_comp__dev`
> Based on the provided sources, multiple Baltimore Orioles draftees attended different schools:

Dylan Bundy attended Owasso High School in Owasso, Oklahoma. [alce::256__wikidata_comp__dev::p86]
> Branden Becker attended Cajon High School in San Bernardino, California. [alce::256__wikidata_comp__dev::p52]
> Cedric Mullins attended Brookwood High School in Snellville, Georgia and played college baseball at Louisburg College and Campbell University. [alce::256__wikidata_comp__dev::p43]
> Baumann attended Mahtomedi High School in Mahtomedi, Minnesota, and later enrolled at Jacksonville University. [alce::256__wikidata_comp__dev::p5]

Cited: alce::256__wikidata_comp__dev::p43, alce::256__wikidata_comp__dev::p5, alce::256__wikidata_comp__dev::p52, alce::256__wikidata_comp__dev::p86

### `1005__wikidata_comp__dev`
> Detyens Shipyards, Inc. operates on vehicles at the Charleston Naval Shipyard. [alce::1005__wikidata_comp__dev::p2]
> The facility signed a long-term lease of the Charleston Naval Shipyard in 1996 and operates the largest commercial shipyard facility on the East Coast, handling military, commercial, and cruise ship projects. [alce::1005__wikidata_comp__dev::p2]

Cited: alce::1005__wikidata_comp__dev::p2

### `605__wikidata_simple__dev`
> Lizzy Gardiner was the costume designer for "The Adventures of Priscilla, Queen of the Desert." [alce::605__wikidata_simple__dev::p0]

Cited: alce::605__wikidata_simple__dev::p0

### `667__wikidata_simple__dev`
> Ralph Betza invented Betza's funny notation, also referred to as "Betza notation," which is a compact method to describe the way pieces move in chess-like board games. [alce::667__wikidata_simple__dev::p0]

Cited: alce::667__wikidata_simple__dev::p0

### `832__wikidata_simple__dev`
> Based on the provided sources, the first TV show broadcast on ABS-CBN was "Hiwaga sa Bahay na Bato," a Philippine drama program that launched officially in 1963. [alce::832__wikidata_simple__dev::p3]

Cited: alce::832__wikidata_simple__dev::p3

### `170__wikidata_comp__dev`
> The Bishop of Lewes, Richard Jackson, studied at Christ Church, Oxford, graduating with a Bachelor of Arts (BA) degree in 1983. [alce::170__wikidata_comp__dev::p34]

Cited: alce::170__wikidata_comp__dev::p34

### `66__wikitables_composition__dev`
> Based on the provided sources, the following museums are located in Richmond, Indiana:

The Richmond Art Museum was founded in 1898 as the Art Association of Richmond, Indiana. [alce::66__wikitables_composition__dev::p0]
> The Wayne County Historical Museum is located in Richmond. [alce::66__wikitables_composition__dev::p7]
> Earlham College's Joseph Moore Museum is located in Richmond. [alce::66__wikitables_composition__dev::p7]

Cited: alce::66__wikitables_composition__dev::p0, alce::66__wikitables_composition__dev::p7

### `523__wikitables_simple__dev`
> Current presidents of legislatures use the following titles:

"Mr. President" is used by anyone presiding over the United States Senate. [alce::523__wikitables_simple__dev::p33]
> "President" is the title used by the current President of the Legislative Council in Van Diemen's Land. [alce::523__wikitables_simple__dev::p0]
> In some countries, speakers of unicameral legislatures or of one or both houses of bicameral legislatures have the title of "President of the body," such as the President of the Congress of Deputies in Spain and the President of the Senate in Spain. [alce::523__wikitables_simple__dev::p85]

Cited: alce::523__wikitables_simple__dev::p0, alce::523__wikitables_simple__dev::p33, alce::523__wikitables_simple__dev::p85

### `271__wikidata_comp__dev`
> Soundaryan served as the composer on "Cheran Chozhan Pandian" (1998), which was directed by Senthamizhan. [alce::271__wikidata_comp__dev::p4]

Cited: alce::271__wikidata_comp__dev::p4

### `722__wikidata_simple__dev`
_Refused._

### `227__wikidata_comp__dev`
> Jon Spaihts wrote the screenplay for "Passengers," which was produced by Sony Pictures. [alce::227__wikidata_comp__dev::p2]

Cited: alce::227__wikidata_comp__dev::p2

### `727__wikidata_simple__dev`
> Venkatachalam Ramaswamy is an individual whose work involves climate modeling. [alce::727__wikidata_simple__dev::p46]
> He is the Director of the Geophysical Fluid Dynamics Laboratory of the National Oceanic and Atmospheric Administration (NOAA) and studies climate modeling and climate change. [alce::727__wikidata_simple__dev::p46]

Cited: alce::727__wikidata_simple__dev::p46

### `92__wikitables_composition__dev`
> Manistee Township is a civil township of Manistee County in the U.S. state of Michigan. [alce::92__wikitables_composition__dev::p1]

Cited: alce::92__wikitables_composition__dev::p1

### `496__wikitables_simple__dev`
_Refused._

### `961__wikidata_comp__dev`
_Refused._

### `905__wikidata_simple__dev`
_Refused._

### `204__wikidata_comp__dev`
> Mark Davies, the Bishop of Middleton, studied at the College of Ripon and York St John, from which he graduated in 1985 with a Bachelor of Arts (BA Hons) honours degree awarded by Leeds University. [alce::204__wikidata_comp__dev::p16]
> He also studied for the Anglican ministry at the College of the Resurrection in Mirfield starting in 1986. [alce::204__wikidata_comp__dev::p16]

Cited: alce::204__wikidata_comp__dev::p16

### `1004__wikidata_comp__dev`
_Refused._

### `612__wikidata_simple__dev`
> Several individuals' lives were claimed by erotic asphyxiation according to these sources.

Kotzwara died from erotic asphyxiation on September 2, 1791, in London, when he tied a ligature around his neck while engaging in sexual activity with a prostitute named Susannah Hill. [alce::612__wikidata_simple__dev::p0]
> Longhurst's life was claimed by erotic asphyxiation, according to an account given by Coutts, who stated he was masturbating while pulling a ligature around her neck when she died. [alce::612__wikidata_simple__dev::p14]
> Hutchence's death may have resulted from autoerotic asphyxiation, according to a claim made by Yates in a 1999 interview on "60 Minutes." [alce::612__wikidata_simple__dev::p43]

Cited: alce::612__wikidata_simple__dev::p0, alce::612__wikidata_simple__dev::p14, alce::612__wikidata_simple__dev::p43

### `503__wikitables_simple__dev`
_Refused._

### `18__wikitables_composition__dev`
> The Iceberg Skating Palace hosted both short track speed skating and figure skating. [alce::18__wikitables_composition__dev::p21]
> This venue is located at Sochi Olympic Park in Sochi, Russia, and hosted these events at the 2014 Winter Olympics. [alce::18__wikitables_composition__dev::p21]
> Additionally, the Hamar Olympic Amphitheatre hosted both figure skating and short track speed skating during the 1994 Winter Olympics. [alce::18__wikitables_composition__dev::p63]

Cited: alce::18__wikitables_composition__dev::p21, alce::18__wikitables_composition__dev::p63

### `533__wikitables_simple__dev`
> # Women Wrestling Promotions

Women's wrestling promotions include the following:

World Women's Wrestling Association (WWWA) was founded by Mildred Burke. [alce::533__wikitables_simple__dev::p20]
> All Japan Women's Pro-Wrestling Federation and All Japan Women's Wrestling Club (started in 1948, the first women's wrestling promotion in Japan) were early promotions. [alce::533__wikitables_simple__dev::p20]
> Women of Wrestling (WOW) is a women's professional wrestling promotion founded in 2000 by David McLane. [alce::533__wikitables_simple__dev::p17]
> Shimmer Women Athletes was established in 2005 in Illinois. [alce::533__wikitables_simple__dev::p3]
> Shine Wrestling was established in 2012 in Florida. [alce::533__wikitables_simple__dev::p3]
> Lucha Libre Femenil (LLF) is an all-woman promotion company started in Monterrey. [alce::533__wikitables_simple__dev::p0]
> Bellatrix Female Warriors and LCW Roses are independent promotions. [alce::533__wikitables_simple__dev::p0]
> Pro-Wrestling: EVE is a British independent women's professional wrestling promotion founded in 2010. [alce::533__wikitables_simple__dev::p45]
> WWE and Total Nonstop Action Wrestling (TNA) are major professional wrestling promotions with women's divisions. [alce::533__wikitables_simple__dev::p0]

Cited: alce::533__wikitables_simple__dev::p0, alce::533__wikitables_simple__dev::p17, alce::533__wikitables_simple__dev::p20, alce::533__wikitables_simple__dev::p3, alce::533__wikitables_simple__dev::p45

### `705__wikidata_simple__dev`
> Based on the provided sources, multiple people have served as coach of Sutton United F.C. at different times:

Ian Baird was appointed head coach at Sutton United in October 2014. [alce::705__wikidata_simple__dev::p40]
> Beadle was appointed head coach at Sutton United in May 2014 by manager Paul Doswell. [alce::705__wikidata_simple__dev::p2]
> A manager named Smith was appointed on 26 May 1956 to take up duties on 1 July 1956. [alce::705__wikidata_simple__dev::p0]
> Cann was appointed manager of Sutton United in July 1962. [alce::705__wikidata_simple__dev::p1]

Cited: alce::705__wikidata_simple__dev::p0, alce::705__wikidata_simple__dev::p1, alce::705__wikidata_simple__dev::p2, alce::705__wikidata_simple__dev::p40

### `726__wikidata_simple__dev`
> Lizzy Gardiner was the costume designer for "The Adventures of Priscilla, Queen of the Desert." [alce::726__wikidata_simple__dev::p0]

Cited: alce::726__wikidata_simple__dev::p0

### `302__wikidata_comp__dev`
_Refused._

### `400__wikidata_comp__dev`
_Refused._

### `381__wikidata_comp__dev`
_Refused._

### `137__wikidata_comp__dev`
> Allan Dwan directed "Bound in Morocco," a movie that Douglas Fairbanks produced. [alce::137__wikidata_comp__dev::p18]

Cited: alce::137__wikidata_comp__dev::p18

### `542__wikitables_simple__dev`
> Based on the provided sources, multiple teams have had goalkeepers who scored goals:

The Kansas City Blues had a goalkeeper who scored a goal. [alce::542__wikitables_simple__dev::p1]
> Michel Plasse, the goaltender for the Kansas City Blues, scored on an open net on February 21, 1971.

The Columbus Crew had a goalkeeper who scored a goal. [alce::542__wikitables_simple__dev::p9]
> Hesmer scored a goal for the Crew in a 2–2 draw with Toronto FC on October 16, 2010.

Additionally, the Fort Worth Fire, Austin Ice Bats, and San Jose Sharks are among other teams whose goalkeepers have scored goals. [alce::542__wikitables_simple__dev::p1]

Cited: alce::542__wikitables_simple__dev::p1, alce::542__wikitables_simple__dev::p9

### `176__wikidata_intersection__dev`
> Bolton Wanderers F.C. competed in multiple FA Cup Finals. They won the 1922–23 FA Cup Final, beating West Ham United 2–0 in the first final to be held at Wembley Stadium. [alce::176__wikidata_intersection__dev::p63]
> They also won the 1926 FA Cup Final, defeating Manchester City 1–0 at Wembley. [alce::176__wikidata_intersection__dev::p33]
> Additionally, Bolton played in the 1953 FA Cup Final (The Stanley Matthews Final), where they lost to Blackpool 4–3 after gaining a 3–1 lead. [alce::176__wikidata_intersection__dev::p0]
> Finally, Bolton Wanderers won the FA Cup Final in 1958, when two Lofthouse goals saw them overcome Manchester United. [alce::176__wikidata_intersection__dev::p0]

Cited: alce::176__wikidata_intersection__dev::p0, alce::176__wikidata_intersection__dev::p33, alce::176__wikidata_intersection__dev::p63

### `431__wikidata_intersection__dev`
> "Anandam" is a film directed by Srinu Vaitla with music composed by Devi Sri Prasad. [alce::431__wikidata_intersection__dev::p12]

Cited: alce::431__wikidata_intersection__dev::p12

### `926__wikidata_simple__dev`
> Dennis Spooner wrote for several TV shows. He was known primarily for his programmes about fictional spies and his work in children's television in the 1960s. [alce::926__wikidata_simple__dev::p0]
> Specifically, he contributed to "The Avengers" and "The New Avengers," where he and Brian Clemens wrote the overwhelming majority of scripts for the latter. [alce::926__wikidata_simple__dev::p2]
> He also wrote for "Doctor Who" [alce::926__wikidata_simple__dev::p5]
> and "The Baron," where he helped Terry Nation write the majority of scripts in 1966. [alce::926__wikidata_simple__dev::p5]
> Additionally, he contributed to children's drama programs in the Gerry Anderson universe [alce::926__wikidata_simple__dev::p4]
> and wrote an episode called "Flashback" for the children's supernatural anthology "Dramarama." [alce::926__wikidata_simple__dev::p4]

Cited: alce::926__wikidata_simple__dev::p0, alce::926__wikidata_simple__dev::p2, alce::926__wikidata_simple__dev::p4, alce::926__wikidata_simple__dev::p5

### `753__wikidata_simple__dev`
> Fred Frith played for several bands. He was one of the founding members of the English avant-rock group Henry Cow. [alce::753__wikidata_simple__dev::p0]
> He was also a member of the groups Art Bears, Massacre, and Skeleton Crew. [alce::753__wikidata_simple__dev::p0]

Cited: alce::753__wikidata_simple__dev::p0

### `438__wikidata_intersection__dev`
_Refused._

### `146__wikidata_comp__dev`
> Several drivers were victorious in Argentine Grand Prix races:

Bruce McLaren won the 1960 Argentine Grand Prix. [alce::146__wikidata_comp__dev::p8]
> Juan Manuel Fangio won the 1955 Argentine Grand Prix. [alce::146__wikidata_comp__dev::p1]
> Damon Hill won the modernized Argentine Grand Prix that returned in the 1990s. [alce::146__wikidata_comp__dev::p15]
> Jacques Villeneuve won the Argentine Grand Prix in his championship season. [alce::146__wikidata_comp__dev::p15]
> Michael Schumacher won the final Argentine Grand Prix in the 1990s, his ninth victory for Ferrari. [alce::146__wikidata_comp__dev::p15]

Cited: alce::146__wikidata_comp__dev::p1, alce::146__wikidata_comp__dev::p15, alce::146__wikidata_comp__dev::p8

### `579__wikidata_simple__dev`
> Bathurst Inlet has a hill located nearby. [alce::579__wikidata_simple__dev::p97]
> The Inuit name for this hill is "Qingaut" (new orthography) or "Kingaun" (old orthography), meaning "nose mountain." [alce::579__wikidata_simple__dev::p97]

Cited: alce::579__wikidata_simple__dev::p97

### `1362__wikidata_simple__dev`
> Several individuals were involved in the wedding of Prince Harry and Meghan Markle:

Prince Harry, the groom, is a member of the British royal family. [alce::1362__wikidata_simple__dev::p0]
> Meghan Markle, the bride, is an American and former actress. [alce::1362__wikidata_simple__dev::p0]
> Queen Elizabeth II, Prince Harry's grandmother, conferred titles upon him on the morning of the wedding. [alce::1362__wikidata_simple__dev::p0]
> The Archbishop of Canterbury, Justin Welby, officiated at the wedding. [alce::1362__wikidata_simple__dev::p0]
> Meghan Markle's mother accompanied her to the church. [alce::1362__wikidata_simple__dev::p4]
> Van Straubenzee served as an usher at the wedding. [alce::1362__wikidata_simple__dev::p54]
> Notable guests in attendance included David and Victoria Beckham, Sir Elton John, James Blunt, Joss Stone, Jonny Wilkinson, James Haskell, Jessica Mulroney, Cressida Bonas, Chelsy Davy, Prince Seeiso of Lesotho, and Princess Mabereng. [alce::1362__wikidata_simple__dev::p5]

Cited: alce::1362__wikidata_simple__dev::p0, alce::1362__wikidata_simple__dev::p4, alce::1362__wikidata_simple__dev::p5, alce::1362__wikidata_simple__dev::p54

### `282__wikidata_intersection__dev`
> Philip Kaufman wrote and directed "Fearless Frank" (1967). [alce::282__wikidata_intersection__dev::p9]
> He also wrote and directed "The Great Northfield Minnesota Raid" (1972). [alce::282__wikidata_intersection__dev::p9]
> Additionally, Kaufman wrote and directed the audio play "Hope Leaves the Theater". [alce::282__wikidata_intersection__dev::p39]

Cited: alce::282__wikidata_intersection__dev::p39, alce::282__wikidata_intersection__dev::p9

### `678__wikidata_simple__dev`
> Agostino Steffani composed several types of music. He composed motets, including six motets while studying in Rome. [alce::678__wikidata_simple__dev::p2]
> He published "Psalmodia vespertina," a sacred work. [alce::678__wikidata_simple__dev::p2]
> He composed opera overtures that combined Italian and French stylistic elements. [alce::678__wikidata_simple__dev::p1]
> He produced operas, including "Enea" and "Tassilone." [alce::678__wikidata_simple__dev::p33]

Cited: alce::678__wikidata_simple__dev::p1, alce::678__wikidata_simple__dev::p2, alce::678__wikidata_simple__dev::p33

### `609__wikidata_simple__dev`
> Based on the provided sources, the United Nations General Assembly passed the following:

Resolution 94 was passed on December 11, 1946, which called to establish a committee of legal experts to make recommendations on ways the General Assembly could encourage the progressive development of international law and its codification. [alce::609__wikidata_simple__dev::p41]
> Resolution 174 was passed on November 21, 1947, which provided for the creation of an "International Law Commission" to promote objectives related to international law development. [alce::609__wikidata_simple__dev::p41]
> The Arms Trade Treaty (ATT) was adopted on April 2, 2013, aimed at regulating international conventional weapons commerce, and was passed by a vote of 154–3. [alce::609__wikidata_simple__dev::p10]
> A resolution calling for independent investigations to be conducted by Israel and Hamas on allegations of war crimes was passed by overwhelming numbers with 114 in favour and 18 against, and 44 abstentions. [alce::609__wikidata_simple__dev::p42]
> Palestine was granted non-member observer status in the General Assembly on November 29, 2012, by a vote of 138–9. [alce::609__wikidata_simple__dev::p10]

Cited: alce::609__wikidata_simple__dev::p10, alce::609__wikidata_simple__dev::p41, alce::609__wikidata_simple__dev::p42

### `794__wikidata_simple__dev`
> Based on the provided sources, members of Offenbach (the Quebec blues rock band) include:

Pierre Harel was a vocalist and lyricist of Offenbach. [alce::794__wikidata_simple__dev::p0]
> Johnny Gravel was a guitarist of Offenbach. [alce::794__wikidata_simple__dev::p0]
> Gerry Boulet was an organist and singer of Offenbach. [alce::794__wikidata_simple__dev::p0]
> Michel Lamothe was a bassist of Offenbach. [alce::794__wikidata_simple__dev::p0]
> Denis Boulet was a drummer of Offenbach. [alce::794__wikidata_simple__dev::p0]

Cited: alce::794__wikidata_simple__dev::p0

### `567__wikidata_simple__dev`
> Based on the provided sources, here are the members of the band Sentenced:

The original line-up consisted of Miika Tenkula (lead guitar and vocals), Sami Lopakka (guitar), Vesa Ranta (drums), and Lari Kylmänen (bass). [alce::567__wikidata_simple__dev::p0]
> Miika Tenkula was the lead guitarist and main songwriter for the band Sentenced until it disbanded, and was also the band's original vocalist from 1989 to late 1992. [alce::567__wikidata_simple__dev::p5]
> Sami Kukkohovi joined the band in 1996 as bassist, replacing Taneli Jarva, and stayed with Sentenced until they disbanded in 2005. [alce::567__wikidata_simple__dev::p3]

Cited: alce::567__wikidata_simple__dev::p0, alce::567__wikidata_simple__dev::p3, alce::567__wikidata_simple__dev::p5

### `797__wikidata_simple__dev`
_Refused._

### `255__wikidata_intersection__dev`
> Chelsea F.C. won multiple FA Cup Finals. The 1997 FA Cup Final was won by Chelsea with a 2–0 victory over Middlesbrough. [alce::255__wikidata_intersection__dev::p13]
> Chelsea also won the 2000 FA Cup Final, beating Aston Villa. [alce::255__wikidata_intersection__dev::p15]
> Additionally, Chelsea won the 2007 FA Cup Final against Manchester United. [alce::255__wikidata_intersection__dev::p0]
> Chelsea also won an FA Cup Final against Liverpool, securing their seventh FA Cup title. [alce::255__wikidata_intersection__dev::p82]

Cited: alce::255__wikidata_intersection__dev::p0, alce::255__wikidata_intersection__dev::p13, alce::255__wikidata_intersection__dev::p15, alce::255__wikidata_intersection__dev::p82

### `424__wikidata_comp__dev`
_Refused._

### `946__wikidata_simple__dev`
_Refused._

### `128__wikidata_comp__dev`
> Based on the provided sources, Evan Reilly directed a TV show whose script he wrote. Specifically, Evan Reilly made his directorial debut on the FX series "Rescue Me" with the penultimate episode titled "Vows," and during his time on that series he wrote or co-wrote forty-three episodes. [alce::128__wikidata_comp__dev::p1]

Cited: alce::128__wikidata_comp__dev::p1

### `324__wikidata_intersection__dev`
> Based on the provided sources, Michael Moore produced and wrote several features:

"Bowling for Columbine" was produced by Michael Moore, a documentary that won the 2002 Academy Award for Best Documentary Feature. [alce::324__wikidata_intersection__dev::p1]
> "Fahrenheit 9/11" was directed and produced by Michael Moore, a critical look at the presidency of George W. Bush and the War on Terror. [alce::324__wikidata_intersection__dev::p1]
> "Roger & Me" is a 1989 American film written, produced, directed by and starring Michael Moore. [alce::324__wikidata_intersection__dev::p4]
> "The Big One" is a 1997 documentary film written and directed by Michael Moore. [alce::324__wikidata_intersection__dev::p54]

Cited: alce::324__wikidata_intersection__dev::p1, alce::324__wikidata_intersection__dev::p4, alce::324__wikidata_intersection__dev::p54

### `51__wikitables_composition__dev`
> Several Argentine volcanoes are classified as Complex Volcanoes:

Cerro Tipas is a massive complex volcano in the Andes, located in northwestern Argentina. [alce::51__wikitables_composition__dev::p52]
> Planchón-Peteroa is a complex volcano extending in a north-south direction along the border between Argentina and Chile. [alce::51__wikitables_composition__dev::p90]
> Tastil volcanic complex is a volcanic complex in Argentina. [alce::51__wikitables_composition__dev::p35]
> Rincon volcanic complex is a volcano in Argentina. [alce::51__wikitables_composition__dev::p3]

Cited: alce::51__wikitables_composition__dev::p3, alce::51__wikitables_composition__dev::p35, alce::51__wikitables_composition__dev::p52, alce::51__wikitables_composition__dev::p90

### `625__wikidata_simple__dev`
> Sajid Nadiadwala was a producer for numerous films. He has produced films including "Housefull" (2010), "Baaghi" (2016), "Judwaa 2", "Highway", "2 States", "Heropanti", "Mujhse Shaadi Karogi", "Jeet", "Judwaa", "Har Dil Jo Pyaar Karega", "Tamasha", and "Dishoom". [alce::625__wikidata_simple__dev::p0]

Cited: alce::625__wikidata_simple__dev::p0

### `1258__wikitables_composition__dev`
> Based on the provided sources, here are the Chillicothe, Ohio radio station call signs:

WZCP is an American non-commercial FM radio station located in Chillicothe, Ohio, operating on 89.3 MHz. [alce::1258__wikitables_composition__dev::p5]
> WQLX (106.5 FM) is a radio station licensed to Chillicothe, Ohio. [alce::1258__wikitables_composition__dev::p7]

Cited: alce::1258__wikitables_composition__dev::p5, alce::1258__wikitables_composition__dev::p7

### `203__wikidata_comp__dev`
_Refused._

### `450__wikidata_intersection__dev`
> Multiple competitions featured both PFC CSKA Sofia and PFC Levski Sofia as participants.

The 1985 Bulgarian Cup Final was contested between CSKA Sofia and Levski Sofia on 19 June 1985 at Vasil Levski National Stadium in Sofia. [alce::450__wikidata_intersection__dev::p28]
> Additionally, the Eternal Derby of Bulgarian Football is the name of the local derby football match between PFC Levski Sofia and PFC CSKA Sofia, representing their ongoing rivalry. [alce::450__wikidata_intersection__dev::p56]

Cited: alce::450__wikidata_intersection__dev::p28, alce::450__wikidata_intersection__dev::p56

### `967__wikidata_comp__dev`
_Refused._

### `180__wikidata_comp__dev`
> Christopher Nolan produced several films with different scriptwriters responsible for each:

For "The Prestige" (2006), Christopher Nolan co-wrote the screenplay with his brother Jonathan Nolan. [alce::180__wikidata_comp__dev::p2]
> For "Interstellar" (2014), the first drafts of the script were written by Jonathan Nolan. [alce::180__wikidata_comp__dev::p5]
> For "The Dark Knight" (2008), Jonathan and Christopher co-wrote the screenplay together. [alce::180__wikidata_comp__dev::p2]

Cited: alce::180__wikidata_comp__dev::p2, alce::180__wikidata_comp__dev::p5

### `30__wikitables_composition__dev`
> Turramurra is a place with a reduplicated name. [alce::30__wikitables_composition__dev::p0]
> However, the sources do not explicitly state that Turramurra is located in Western Australia.
> The source only mentions it as an example of a reduplicated Australian place name with Aboriginal origins, without specifying its location.
> If a place specifically in Western Australia with a reduplicated name is required, the sources provided do not contain sufficient information to answer this question, as the reduplicated place names mentioned (Turramurra, Parramatta, Woolloomooloo, Wagga Wagga, Gumly Gumly, Grong) are not identified as being in Western Australia.

Cited: alce::30__wikitables_composition__dev::p0

### `825__wikidata_simple__dev`
> René Arnoux won multiple competitions throughout his racing career. He won the 1975 Formule Super Renault title. [alce::825__wikidata_simple__dev::p0]
> He won the 1977 European Formula Two Championship. [alce::825__wikidata_simple__dev::p1]
> In Formula One, he won seven World Championship Grands Prix, including the 1980 Brazilian Grand Prix. [alce::825__wikidata_simple__dev::p61]
> He also won the 1982 Italian Grand Prix. [alce::825__wikidata_simple__dev::p82]

Cited: alce::825__wikidata_simple__dev::p0, alce::825__wikidata_simple__dev::p1, alce::825__wikidata_simple__dev::p61, alce::825__wikidata_simple__dev::p82

### `952__wikidata_comp__dev`
_Refused._

### `28__wikitables_composition__dev`
> Based on the provided sources, two Calgary Stampeders coaches have won the Grey Cup:

John Hufnagel won the Grey Cup as head coach of the Calgary Stampeders in 2008, leading the team to a 22–14 victory over the Montreal Alouettes. [alce::28__wikitables_composition__dev::p0]
> Buono became the first head coach to win multiple Grey Cup championships for the Calgary Stampeders franchise. [alce::28__wikitables_composition__dev::p38]
> Note: The sources also mention that Ken Higgins won a Grey Cup, but this was as head coach of the Edmonton Eskimos in 2003, not as a Calgary Stampeders coach. [alce::28__wikitables_composition__dev::p32]

Cited: alce::28__wikitables_composition__dev::p0, alce::28__wikitables_composition__dev::p32, alce::28__wikitables_composition__dev::p38

### `978__wikidata_comp__dev`
_Refused._

### `677__wikidata_simple__dev`
> Katoomba is the place where the following news media are published:

The Mountaineer was a newspaper published in Katoomba, New South Wales which circulated throughout the Blue Mountains and Hartley districts between 1894 and 1908. [alce::677__wikidata_simple__dev::p17]
> The Blue Mountain Echo, also published as "The Blue Mountain Star," "The Katoomba Daily," "The Blue Mountains Daily," and "The Blue Mountains Echo" was a semi-weekly English language newspaper published in Katoomba, New South Wales, Australia from 1909-1939. [alce::677__wikidata_simple__dev::p2]
> The Blue Mountains Advertiser was a weekly English language newspaper published in Katoomba, New South Wales, Australia from 1939 to 1978. [alce::677__wikidata_simple__dev::p1]
> The Mountain Daily was an English language newspaper published in Katoomba, New South Wales, Australia between 1919 and 1920. [alce::677__wikidata_simple__dev::p8]

Cited: alce::677__wikidata_simple__dev::p1, alce::677__wikidata_simple__dev::p17, alce::677__wikidata_simple__dev::p2, alce::677__wikidata_simple__dev::p8

### `331__wikidata_comp__dev`
_Refused._

### `210__wikidata_intersection__dev`
_Refused._

### `165__wikidata_intersection__dev`
_Refused._

### `117__wikidata_intersection__dev`
_Refused._

### `854__wikidata_simple__dev`
> John Browning designed a vast array of military and civilian small arms, including firearms for his own company as well as for Winchester, Colt, Remington, Savage, Stevens, and Fabrique Nationale de Herstal of Belgium. [alce::854__wikidata_simple__dev::p9]
> His designs included many varieties of military and civilian firearms, cartridges, and gun mechanisms, many of which are still in use around the world. [alce::854__wikidata_simple__dev::p0]
> Specific firearm designs attributed to him include the Auto-5 shotgun, the Winchester Model 1897 shotgun, and the M1895 Machine Gun. [alce::854__wikidata_simple__dev::p7]

Cited: alce::854__wikidata_simple__dev::p0, alce::854__wikidata_simple__dev::p7, alce::854__wikidata_simple__dev::p9

### `602__wikidata_simple__dev`
> Paul-Pierre Henry and his brother Prosper Henry made refracting telescopes and instruments for observatories. [alce::602__wikidata_simple__dev::p2]
> They were also involved in the origin of the "Carte du Ciel" project. [alce::602__wikidata_simple__dev::p2]
> Additionally, they created sky charts designed to facilitate the search for minor planets, for which they were jointly awarded the first Valz Prize in 1877. [alce::602__wikidata_simple__dev::p1]

Cited: alce::602__wikidata_simple__dev::p1, alce::602__wikidata_simple__dev::p2

### `446__wikidata_intersection__dev`
> "Lost" was the TV show that had both Carlton Cuse and Damon Lindelof as screenwriters. [alce::446__wikidata_intersection__dev::p16]
> Throughout the show's run, Lindelof and Carlton Cuse served as showrunners and head writers. [alce::446__wikidata_intersection__dev::p16]

Cited: alce::446__wikidata_intersection__dev::p16

### `666__wikidata_simple__dev`
_Refused._

### `732__wikidata_simple__dev`
> LD Entertainment has issued multiple movies. Some of their most recent films include "Jackie," a biopic about Jackie Kennedy starring Natalie Portman, "Anthropoid," a World War II drama starring Jamie Dornan and Cilian Murphy, and "Risen," a fictional account of the Resurrection with Joseph Fiennes. [alce::732__wikidata_simple__dev::p2]
> Other films produced under the LD banner include "The Grey" with Liam Neeson and "Albert Nobbs" with Glenn Close. [alce::732__wikidata_simple__dev::p0]
> LD Entertainment has also distributed films such as "Killer Joe," a dark comedy by William Friedkin starring Matthew McConaughey, "Disconnect" starring Jason Bateman and Alexander Skarsgard, "The Collection," a horror film by "Saw" writers Marcus Dunstan and Patrick Melton, and "Black Rock" starring Kate Bosworth, Lake Bell and Katie Aselton. [alce::732__wikidata_simple__dev::p0]
> Additionally, LD Entertainment has acquired or produced films including the Academy Award nominated "Biutiful" starring Javier Bardem, "I Love You Phillip Morris" starring Jim Carrey and Ewan McGregor, "Good Hair" starring Chris Rock, and "The Details" starring Tobey Maguire and Elizabeth Banks. [alce::732__wikidata_simple__dev::p0]

Cited: alce::732__wikidata_simple__dev::p0, alce::732__wikidata_simple__dev::p2

### `78__wikitables_composition__dev`
> The tallest building in Croatia is the Zagreb Cathedral, located on Kaptol. [alce::78__wikitables_composition__dev::p8]
> The Zagreb Cathedral is not only the tallest building in Croatia but also the most monumental sacral building in Gothic style southeast of the Alps. [alce::78__wikitables_composition__dev::p9]
> Among modern high-rise office buildings in Zagreb, Zagrepčanka is ranked 1st by height in Croatia, standing 94.6 meters (310 feet) tall with 27 levels, and reaching 109 meters (363 feet) when including its antenna. [alce::78__wikitables_composition__dev::p3]
> Other notable tall buildings in Zagreb include the Almeria Tower, Eurotower, HOTO Tower, Zagrebtower, and Sky Office Tower. [alce::78__wikitables_composition__dev::p0]

Cited: alce::78__wikitables_composition__dev::p0, alce::78__wikitables_composition__dev::p3, alce::78__wikitables_composition__dev::p8, alce::78__wikitables_composition__dev::p9

### `968__wikidata_comp__dev`
> Based on the provided sources, I can identify the educational backgrounds of several people who worked for the New York Supreme Court:

Karla Moskowitz, an Associate Justice of the New York Appellate Division of the Supreme Court, graduated from Alfred University in 1963 and from Columbia Law School in 1966. [alce::968__wikidata_comp__dev::p71]
> Janet DiFiore, who served as a justice of the New York Supreme Court from 2003 to 2005, graduated from Long Island University and St. John's University School of Law. [alce::968__wikidata_comp__dev::p59]
> One individual who was elected to the New York State Supreme Court attended the Cardozo School of Law from 1985 to 1986 and the Pace University School of Law in 1984. [alce::968__wikidata_comp__dev::p39]
> Another Supreme Court justice attended night classes at Siena College and graduated with a B.A. in 1946. [alce::968__wikidata_comp__dev::p72]

Cited: alce::968__wikidata_comp__dev::p39, alce::968__wikidata_comp__dev::p59, alce::968__wikidata_comp__dev::p71, alce::968__wikidata_comp__dev::p72

### `787__wikidata_simple__dev`
> The Haitian Revolution was led by multiple key figures. Toussaint Louverture was the best-known leader of the Haitian Revolution. [alce::787__wikidata_simple__dev::p5]
> Jean-Jacques Dessalines was also a leader of the Haitian Revolution and became the first ruler of independent Haiti. [alce::787__wikidata_simple__dev::p13]
> Additionally, Henri Christophe was a key leader in the Haitian Revolution. [alce::787__wikidata_simple__dev::p15]

Cited: alce::787__wikidata_simple__dev::p13, alce::787__wikidata_simple__dev::p15, alce::787__wikidata_simple__dev::p5

### `512__wikitables_simple__dev`
> The major wire services agencies are Reuters, Associated Press, Agence France Press, and United Press International. [alce::512__wikitables_simple__dev::p4]
> These four agencies, known as the "Big Four" news agencies, dominated global news coverage in the 20th century and represented the Western bloc. [alce::512__wikitables_simple__dev::p4]
> Studies of major world events consistently found that a large majority of news items originated from these four biggest wire services. [alce::512__wikitables_simple__dev::p4]
> Additionally, communist-era agencies included TASS from the Soviet Union and Xinhua from China. [alce::512__wikitables_simple__dev::p4]
> Television news agencies include Associated Press Television News and Reuters Television. [alce::512__wikitables_simple__dev::p4]

Cited: alce::512__wikitables_simple__dev::p4

### `845__wikidata_simple__dev`
> Club Atlético River Plate participated in multiple competitions. The Argentine club won the Copa Libertadores, Copa Intercontinental, and Copa Sudamericana at the international level. [alce::845__wikidata_simple__dev::p8]
> The club also participated in the CONMEBOL cup and Liguilla Pre Libertadores. [alce::845__wikidata_simple__dev::p56]
> Domestically, River Plate competed in Argentina's Primera División championship and National cups. [alce::845__wikidata_simple__dev::p3]

Cited: alce::845__wikidata_simple__dev::p3, alce::845__wikidata_simple__dev::p56, alce::845__wikidata_simple__dev::p8

### `652__wikidata_simple__dev`
_Refused._

### `131__wikidata_intersection__dev`
> Tottenham Hotspur played against Liverpool in the Football League Cup. [alce::131__wikidata_intersection__dev::p6]
> Specifically, they met in the 1982 Football League Cup Final on 13 March 1982 at Wembley Stadium. [alce::131__wikidata_intersection__dev::p6]

Cited: alce::131__wikidata_intersection__dev::p6

### `399__wikidata_intersection__dev`
> P. Adinarayana Rao composed and produced music for several Tamil and Hindi movies. [alce::399__wikidata_intersection__dev::p0]
> He also composed music for Telugu films, establishing himself as a well-known music director in the Telugu film industry. [alce::399__wikidata_intersection__dev::p2]

Cited: alce::399__wikidata_intersection__dev::p0, alce::399__wikidata_intersection__dev::p2

### `372__wikidata_intersection__dev`
> The New York Yankees emerged victorious in multiple World Series. They won the 1947 World Series against the Brooklyn Dodgers in seven games for their eleventh World Series championship in team history. [alce::372__wikidata_intersection__dev::p54]
> They won the 1953 World Series, their fourth straight World Series victory. [alce::372__wikidata_intersection__dev::p17]
> They won the 1996 World Series against the Atlanta Braves four games to two, earning their 23rd World Series title. [alce::372__wikidata_intersection__dev::p52]
> They won the 1998, 1999, and 2000 World Series, with the 2000 victory being their third successive title against the Mets. [alce::372__wikidata_intersection__dev::p7]

Cited: alce::372__wikidata_intersection__dev::p17, alce::372__wikidata_intersection__dev::p52, alce::372__wikidata_intersection__dev::p54, alce::372__wikidata_intersection__dev::p7

### `96__wikitables_composition__dev`
_Refused._

### `75__wikitables_composition__dev`
> Monroe is a city in the U.S. state of Michigan located on the western shore of Lake Erie. [alce::75__wikitables_composition__dev::p2]
> It is the county seat and largest city of Monroe County. [alce::75__wikitables_composition__dev::p2]

Cited: alce::75__wikitables_composition__dev::p2

### `780__wikidata_simple__dev`
> Official Films distributed multiple TV shows during the late 1950s and early 1960s. [alce::780__wikidata_simple__dev::p7]
> These included "Peter Gunn", "Yancy Derringer", "The Adventures of Robin Hood", "Decoy", "H.G. Wells: The Invisible Man", "Mr. Lucky", "The Adventures of Sir Lancelot", "Four Star Playhouse", "The Buccaneers", "Colonel March of Scotland Yard", "The Stu Erwin Show", "My Little Margie", and the original "Biography". [alce::780__wikidata_simple__dev::p7]

Cited: alce::780__wikidata_simple__dev::p7

### `178__wikidata_intersection__dev`
> Gregory Nava served dual roles as director and writer for the film "El Norte." [alce::178__wikidata_intersection__dev::p37]
> The screenplay was written by Gregory Nava and Anna Thomas, based on Nava's story, and the film was directed by Gregory Nava. [alce::178__wikidata_intersection__dev::p37]

Cited: alce::178__wikidata_intersection__dev::p37

### `90__wikitables_composition__dev`
> Kirk Ferentz has served as the head football coach at the University of Iowa since the 1999 season. [alce::90__wikitables_composition__dev::p4]
> He was hired on December 2, 1998, to replace the retiring Hayden Fry. [alce::90__wikitables_composition__dev::p15]

Cited: alce::90__wikitables_composition__dev::p15, alce::90__wikitables_composition__dev::p4

### `115__wikidata_comp__dev`
_Refused._

### `837__wikidata_simple__dev`
> Nicolas Bourbaki was the collective pseudonym of a group of (mainly French) mathematicians. [alce::837__wikidata_simple__dev::p2]
> Their aim was to reformulate mathematics on an extremely abstract and formal but self-contained basis in a series of books beginning in 1935. [alce::837__wikidata_simple__dev::p2]
> While there is no one person named Nicolas Bourbaki, the group was officially known as the "Association des collaborateurs de Nicolas Bourbaki" (Association of Collaborators of Nicolas Bourbaki). [alce::837__wikidata_simple__dev::p2]

Cited: alce::837__wikidata_simple__dev::p2

### `314__wikidata_comp__dev`
> Based on the provided sources, several manufacturers produced objects that Bertone designed:

FIAT manufactured cars that Bertone styled. [alce::314__wikidata_comp__dev::p0]
> Kiwi, a Swiss bicycle and motorcycle helmet manufacturer, manufactured the K20 motorcycle helmet that Bertone styled. [alce::314__wikidata_comp__dev::p0]
> Alstom produced the regional train "Jazz" that Bertone designed. [alce::314__wikidata_comp__dev::p2]
> Trenitalia manufactured the Frecciarossa 1000 train that Bertone designed. [alce::314__wikidata_comp__dev::p2]

Cited: alce::314__wikidata_comp__dev::p0, alce::314__wikidata_comp__dev::p2

### `296__wikidata_comp__dev`
> Geoffrey Allen, the third Bishop of Derby, received his education at Dulwich College and University College, Oxford. [alce::296__wikidata_comp__dev::p70]

Cited: alce::296__wikidata_comp__dev::p70

### `869__wikidata_simple__dev`
_Refused._

### `848__wikidata_simple__dev`
> Jim Bentley coached Morecambe F.C. [alce::848__wikidata_simple__dev::p42]
> He was appointed player-manager of Morecambe on 13 May 2011 on a two-year contract, and subsequently concentrated on the managerial role. [alce::848__wikidata_simple__dev::p42]
> Additionally, other managers of Morecambe F.C. included Harvey, who joined as player-manager in July 1994 and led them into the Football Conference in 1996. [alce::848__wikidata_simple__dev::p3]

Cited: alce::848__wikidata_simple__dev::p3, alce::848__wikidata_simple__dev::p42

### `441__wikidata_intersection__dev`
> Based on the provided sources, Chelsea F.C. and Manchester City F.C. featured together in the following athletic contests:

The 2018 FA Community Shield was contested by Manchester City and Chelsea at Wembley Stadium in London on 5 August 2018. [alce::441__wikidata_intersection__dev::p2]
> The two sides faced each other in the Community Shield once previously, in 2012, a match won 3–2 by Manchester City. [alce::441__wikidata_intersection__dev::p4]
> Chelsea and Manchester City met in two friendly matches during a post-season trip to the United States, with matches at Busch Stadium in St. Louis, Missouri and at Yankee Stadium in New York City on 25 May. [alce::441__wikidata_intersection__dev::p17]
> Both Chelsea and Manchester City were participants in the Premier League Asia Trophy tournament.

Cited: alce::441__wikidata_intersection__dev::p17, alce::441__wikidata_intersection__dev::p2, alce::441__wikidata_intersection__dev::p4

### `937__wikidata_simple__dev`
> The question asks about "William Adams" but the sources contain information about multiple people with similar names:

1. **William Adam (architect)** designed country houses and public buildings, including Hopetoun House near Edinburgh and Duff House in Banff. [alce::937__wikidata_simple__dev::p0]
> 2. **William Adams (potter)** produced fine jasperware table sets, plaques, medallions and other products. [alce::937__wikidata_simple__dev::p2]
> 3. **William Adams Nicholson** was an architect, but the sources do not specify which objects he designed. [alce::937__wikidata_simple__dev::p48]
> Without clarification of which "William Adams" is being asked about, the most prominent figure in the sources is William Adam the Scottish architect, who designed numerous country houses and public buildings.

Cited: alce::937__wikidata_simple__dev::p0, alce::937__wikidata_simple__dev::p2, alce::937__wikidata_simple__dev::p48

### `173__wikidata_comp__dev`
> A. Karunakaran directed the film "Balu ABCDEFG" which was produced by C. Ashwini Dutt under Vyjayanthi Movies banner. [alce::173__wikidata_comp__dev::p56]

Cited: alce::173__wikidata_comp__dev::p56

### `680__wikidata_simple__dev`
> North of Blue is an animated film directed by Joanna Priestley. [alce::680__wikidata_simple__dev::p3]

Cited: alce::680__wikidata_simple__dev::p3

### `836__wikidata_simple__dev`
_Refused._

### `509__wikitables_simple__dev`
> # Existing Restaurant Chains

A restaurant chain is a set of related restaurants in many different locations that are either under shared corporate ownership or franchising agreements. [alce::509__wikitables_simple__dev::p0]
> Examples of sit-down restaurant chains include Timber Lodge Steakhouse, Buffalo Wild Wings, Outback Steakhouse, T.G.I. Friday's, Legal Sea Foods, Ruby Tuesday, and Olive Garden. [alce::509__wikitables_simple__dev::p0]
> International foreign-owned restaurant chains currently operating in some countries include A&W, Burger King, Baskin Robbins, Chatime, Cold Stone Creamery, Fish & Co, Gloria Jean's Coffee, and Johnny Rocket's, among others. [alce::509__wikitables_simple__dev::p4]
> Barbecue restaurant chains in the U.S. include Sonny's Real Pit BBQ (which had over 130 stores in 2010), Smokey Bones (with over 70 stores in 2010), Rib Crib (with 41 stores in 2008), and Dickey's Barbecue Pit. [alce::509__wikitables_simple__dev::p2]
> Dark restaurant chains include "Dans le Noir?" which operates in Europe, Russia, and the Pacific, and Opaque, which is the only chain operation in the USA. [alce::509__wikitables_simple__dev::p3]

Cited: alce::509__wikitables_simple__dev::p0, alce::509__wikitables_simple__dev::p2, alce::509__wikitables_simple__dev::p3, alce::509__wikitables_simple__dev::p4

### `499__wikitables_simple__dev`
> Based on the provided sources, here are the discovered galaxy clusters mentioned:

CL J1001+0220 is the most distant known galaxy cluster as of 2016, discovered by the Chandra X-ray Observatory in conjunction with the ESO's UltraVISTA telescope and the Atacama Large Millimeter Array. [alce::499__wikitables_simple__dev::p9]
> SPT-CL J0546-5345 and SPT-CL J2106-5844 are notable galaxy clusters in the distant, high-redshift Universe and are among the most massive galaxy clusters found in the early Universe. [alce::499__wikitables_simple__dev::p2]

Cited: alce::499__wikitables_simple__dev::p2, alce::499__wikitables_simple__dev::p9

### `89__wikitables_composition__dev`
> Based on the provided sources, several museums are located in Florence, Tuscany:

The National Archaeological Museum (Museo archeologico nazionale di Firenze) is an archaeological museum in Florence, Italy, located at piazza Santissima Annunziata in the Palazzo della Crocetta. [alce::89__wikitables_composition__dev::p1]
> The Uffizi Gallery is a prominent art museum located adjacent to the Piazza della Signoria in the Historic Centre of Florence in the region of Tuscany, Italy. [alce::89__wikitables_composition__dev::p6]
> Additional museums in Florence include the Palatina gallery, the Bargello, the museum of San Marco, the Academy, Buonarroti's house, the Bardini, Horne, Stibbert, Romano, and Corsini museums, the Gallery of Modern Art, the Museo dell'Opera del Duomo, the museum of Silverware, and the museum of Precious Stones. [alce::89__wikitables_composition__dev::p0]

Cited: alce::89__wikitables_composition__dev::p0, alce::89__wikitables_composition__dev::p1, alce::89__wikitables_composition__dev::p6

### `528__wikitables_simple__dev`
> Several notable philanthropists are mentioned in the sources:

Robert Treat Paine, Jr. was a Boston lawyer, philanthropist and social reformer known for his work as chairman of the building committee of Boston's Trinity Church in Copley Square, his leadership of 19th century Boston philanthropists, and his experiments in building housing for low- and middle-income workers. [alce::528__wikitables_simple__dev::p74]
> Sir William Henderson was a Scottish merchant and philanthropist who was knighted in Queen Victoria's 1893 Birthday Honours. [alce::528__wikitables_simple__dev::p87]
> Rosalind P. Walter became a noted philanthropist during the latter part of the 20th century, best known for her support of public television programming in the United States and her service as a trustee for various cultural institutions. [alce::528__wikitables_simple__dev::p0]
> Edward Denison was an English philanthropist known for his benevolent labours in the East End of London and served as a Liberal Member of Parliament from 1868 to 1870. [alce::528__wikitables_simple__dev::p61]

Cited: alce::528__wikitables_simple__dev::p0, alce::528__wikitables_simple__dev::p61, alce::528__wikitables_simple__dev::p74, alce::528__wikitables_simple__dev::p87

### `754__wikidata_simple__dev`
> Molde FK competed in several sports competitions. The club participated in the Eliteserien, the Norwegian top division. [alce::754__wikidata_simple__dev::p4]
> They also competed in the Norwegian Cup. [alce::754__wikidata_simple__dev::p3]
> Additionally, Molde FK participated in European football competitions, including 15 seasons of Union of European Football Associations (UEFA) club competitions, which included the Champions League, UEFA Cup, Europa League, and the Cup Winners' Cup. [alce::754__wikidata_simple__dev::p2]

Cited: alce::754__wikidata_simple__dev::p2, alce::754__wikidata_simple__dev::p3, alce::754__wikidata_simple__dev::p4

### `85__wikitables_composition__dev`
_Refused._

### `355__wikidata_intersection__dev`
> Essendon Football Club competed against Carlton Football Club at the 1962 VFL Grand Final. [alce::355__wikidata_intersection__dev::p8]

Cited: alce::355__wikidata_intersection__dev::p8

### `1101__wikidata_intersection__dev`
> The New York Giants took part in multiple Super Bowls. They played in Super Bowl XXI against the Denver Broncos. [alce::1101__wikidata_intersection__dev::p56]
> They also played in Super Bowl XLII against the New England Patriots on February 3, 2008. [alce::1101__wikidata_intersection__dev::p8]
> Additionally, the Giants returned to the Super Bowl in 2011, again defeating the New England Patriots. [alce::1101__wikidata_intersection__dev::p2]

Cited: alce::1101__wikidata_intersection__dev::p2, alce::1101__wikidata_intersection__dev::p56, alce::1101__wikidata_intersection__dev::p8

### `706__wikidata_simple__dev`
_Refused._

### `241__wikidata_comp__dev`
_Refused._

### `1363__wikidata_simple__dev`
> Cananéia is associated with the Cananéia-Iguape-Peruíbe Environmental Protection Area. [alce::1363__wikidata_simple__dev::p2]
> This protected area covers parts of the municipality of Cananéia in the state of São Paulo. [alce::1363__wikidata_simple__dev::p2]

Cited: alce::1363__wikidata_simple__dev::p2

### `371__wikidata_comp__dev`
> Edmund C. Tarbell was a member of the Ten American Painters. [alce::371__wikidata_comp__dev::p30]
> He was educated at the School of the Museum of Fine Arts, Boston, where he entered in 1879 and studied under Otto Grundmann. [alce::371__wikidata_comp__dev::p4]
> He subsequently continued his education in Paris, France, entering the Académie Julian in 1883 to study under Gustave Boulanger and Jules Joseph Lefebvre. [alce::371__wikidata_comp__dev::p4]

Cited: alce::371__wikidata_comp__dev::p30, alce::371__wikidata_comp__dev::p4

### `969__wikidata_comp__dev`
_Refused._

### `858__wikidata_simple__dev`
> The native languages of Camarines Sur are the Coastal Bikol (especially Central Bikol) and Inland Bikol group of languages. [alce::858__wikidata_simple__dev::p1]
> The Inland Bikol group includes Albay Bikol and Rinconada Bikol, while Coastal Bikol consists of dialects. [alce::858__wikidata_simple__dev::p1]

Cited: alce::858__wikidata_simple__dev::p1

### `1255__wikitables_composition__dev`
> Constantine XI was killed in Constantinople. [alce::1255__wikitables_composition__dev::p38]
> He died fighting at the gates of the city on 29 May 1453, the day the city fell. [alce::1255__wikitables_composition__dev::p89]

Cited: alce::1255__wikitables_composition__dev::p38, alce::1255__wikitables_composition__dev::p89

### `681__wikidata_simple__dev`
> Dmitry Tursunov won the Hopman Cup on 6 January 2007 in Perth, Australia, while representing Russia alongside Nadia Petrova. [alce::681__wikidata_simple__dev::p14]
> He also won the 2008 Medibank International in Sydney, Australia. [alce::681__wikidata_simple__dev::p45]
> Additionally, Tursunov won the 2008 Open de Moselle in Metz. [alce::681__wikidata_simple__dev::p63]

Cited: alce::681__wikidata_simple__dev::p14, alce::681__wikidata_simple__dev::p45, alce::681__wikidata_simple__dev::p63

### `32__wikitables_composition__dev`
> Based on the provided sources, there were nightclub fires in the following locations in the United States:

Boston, Massachusetts - The Cocoanut Grove fire occurred on November 28, 1942, killing 492 people and injuring hundreds more. [alce::32__wikitables_composition__dev::p5]
> West Warwick, Rhode Island - The 2003 Station nightclub fire occurred in this location. [alce::32__wikitables_composition__dev::p43]
> Southgate, Kentucky - The Beverly Hills Supper Club fire occurred on May 28, 1977, killing 165 people and injuring more than 200. [alce::32__wikitables_composition__dev::p13]

Cited: alce::32__wikitables_composition__dev::p13, alce::32__wikitables_composition__dev::p43, alce::32__wikitables_composition__dev::p5

### `352__wikidata_intersection__dev`
> Craig Pearce and Baz Luhrmann scripted multiple motion pictures together. These include "Strictly Ballroom" (1992) [alce::352__wikidata_intersection__dev::p0]
> , "Romeo + Juliet" (1996) [alce::352__wikidata_intersection__dev::p0]
> , "Moulin Rouge!" (2001) [alce::352__wikidata_intersection__dev::p0]
> , and "The Great Gatsby" (2013) [alce::352__wikidata_intersection__dev::p0]
> .

Cited: alce::352__wikidata_intersection__dev::p0

### `786__wikidata_simple__dev`
> James Connor Robertson is an athlete drafted by the Oakland Athletics. [alce::786__wikidata_simple__dev::p33]

Cited: alce::786__wikidata_simple__dev::p33

### `47__wikitables_composition__dev`
> Balıkesir is located in Balıkesir Province. [alce::47__wikitables_composition__dev::p2]
> Balıkesir is the capital city of Balıkesir Province and has a population of 331,788 inhabitants. [alce::47__wikitables_composition__dev::p2]

Cited: alce::47__wikitables_composition__dev::p2

### `817__wikidata_simple__dev`
> One example of a D-class vessel is the D-class destroyer, which was a group of torpedo boat destroyers built for the Royal Navy in the mid-1890s. [alce::817__wikidata_simple__dev::p0]
> Another example is the D-class lifeboat (EA16), an inflatable boat operated since 1987 by the Royal National Lifeboat Institution of the United Kingdom and Ireland. [alce::817__wikidata_simple__dev::p81]
> A third example is the D-class cruiser, a pair of German cruisers classified as "Panzerschiffe" by the Kriegsmarine. [alce::817__wikidata_simple__dev::p10]

Cited: alce::817__wikidata_simple__dev::p0, alce::817__wikidata_simple__dev::p10, alce::817__wikidata_simple__dev::p81

### `646__wikidata_simple__dev`
_Refused._

### `702__wikidata_simple__dev`
> Luna Rossa participated in the America's Cup competition. [alce::702__wikidata_simple__dev::p1]
> The team competed in the Louis Vuitton Cup multiple times, including in 2000, 2007, and 2013. [alce::702__wikidata_simple__dev::p1]
> Luna Rossa also competed in the America's Cup World Series. [alce::702__wikidata_simple__dev::p4]

Cited: alce::702__wikidata_simple__dev::p1, alce::702__wikidata_simple__dev::p4

### `384__wikidata_intersection__dev`
_Refused._

### `158__wikidata_intersection__dev`
> Multiple football matches featured Manchester United versus Leicester City:

The 1962–63 FA Cup Final was played on 25 May 1963 at Wembley, with Manchester United defeating Leicester City 3–1. [alce::158__wikidata_intersection__dev::p23]
> The 2016 FA Community Shield was contested by Manchester United and Leicester City at Wembley Stadium, with Manchester United winning 2–1. [alce::158__wikidata_intersection__dev::p1]

Cited: alce::158__wikidata_intersection__dev::p1, alce::158__wikidata_intersection__dev::p23

### `453__wikidata_intersection__dev`
> The Europa League featured Manchester United F.C. as both participant and winner. [alce::453__wikidata_intersection__dev::p7]
> United won the 2016–17 UEFA Europa League after defeating AFC Ajax 2–0 in the final, giving them their first win of the competition. [alce::453__wikidata_intersection__dev::p7]

Cited: alce::453__wikidata_intersection__dev::p7

### `455__wikidata_intersection__dev`
> John Carpenter directed and composed the music for several films. "Assault on Precinct 13" (1976) is one example, as he wrote, directed, and scored it. [alce::455__wikidata_intersection__dev::p78]
> Additionally, "Halloween" (1978) is notable, as Carpenter is recognized for having composed most of his films' music, with the main theme of "Halloween" being considered a part of popular culture. [alce::455__wikidata_intersection__dev::p0]
> He also returned to the "Halloween" franchise as both composer and executive producer for "Halloween" (2018). [alce::455__wikidata_intersection__dev::p0]

Cited: alce::455__wikidata_intersection__dev::p0, alce::455__wikidata_intersection__dev::p78

### `871__wikidata_simple__dev`
> The Atlanta Thrashers drafted multiple players. Patrik Štefan was drafted 1st overall by the Atlanta Thrashers in the 1999 NHL Entry Draft. [alce::871__wikidata_simple__dev::p4]
> Daultan Leveille was drafted by the Atlanta Thrashers in the first round, 29th overall, in the 2008 NHL Entry Draft. [alce::871__wikidata_simple__dev::p87]
> Zach Bogosian was drafted third overall by the Atlanta Thrashers. [alce::871__wikidata_simple__dev::p39]
> Dany Heatley was drafted second overall by the Atlanta Thrashers in the 2000 NHL Entry Draft. [alce::871__wikidata_simple__dev::p45]
> Riley Holzapfel was drafted by the Atlanta Thrashers at the 2006 NHL Entry Draft, chosen 43rd overall. [alce::871__wikidata_simple__dev::p85]

Cited: alce::871__wikidata_simple__dev::p39, alce::871__wikidata_simple__dev::p4, alce::871__wikidata_simple__dev::p45, alce::871__wikidata_simple__dev::p85, alce::871__wikidata_simple__dev::p87

### `297__wikidata_intersection__dev`
> Sam Raimi both wrote and directed "Drag Me to Hell". [alce::297__wikidata_intersection__dev::p1]

Cited: alce::297__wikidata_intersection__dev::p1

### `882__wikidata_simple__dev`
> Toby Howarth was a Bishop of Bradford. [alce::882__wikidata_simple__dev::p38]
> He is the current and first area Bishop of Bradford in the Diocese of Leeds. [alce::882__wikidata_simple__dev::p38]
> Additionally, Nick Baines was the last diocesan Bishop of Bradford, serving from 21 May 2011 until 20 April 2014. [alce::882__wikidata_simple__dev::p0]

Cited: alce::882__wikidata_simple__dev::p0, alce::882__wikidata_simple__dev::p38

### `406__wikidata_comp__dev`
_Refused._

### `507__wikitables_simple__dev`
> Pharaoh is the common title of the monarchs of ancient Egypt from the First Dynasty (c. 3150 BCE) until the annexation of Egypt by the Roman Empire in 30 BCE. [alce::507__wikitables_simple__dev::p1]
> The actual term "Pharaoh" was not used contemporaneously for a ruler until Merneptah, c. 1200 BCE. [alce::507__wikitables_simple__dev::p1]
> In the early dynasty, ancient Egyptian kings used to have up to three titles, the Horus, the Sedge and Bee ("nswt-bjtj") name, and the Two Ladies ("nbtj") name. [alce::507__wikitables_simple__dev::p1]

Cited: alce::507__wikitables_simple__dev::p1

### `669__wikidata_simple__dev`
> George L. Little was the costume designer for multiple movies. He was best known for his work on "The Hurt Locker" and "Zero Dark Thirty" [alce::669__wikidata_simple__dev::p0]
> . He also served as costume designer on "The Prince and the Surfer", "Things You Can Tell Just by Looking at Her", "Behind Enemy Lines", "Flight of the Phoenix", and "The Omen" [alce::669__wikidata_simple__dev::p1]
> . Additional films for which he was costume designer include "The Crazies", "Warm Bodies", "Transcendence", and "The Fantastic Four" [alce::669__wikidata_simple__dev::p3]
> .

Cited: alce::669__wikidata_simple__dev::p0, alce::669__wikidata_simple__dev::p1, alce::669__wikidata_simple__dev::p3

### `844__wikidata_simple__dev`
> Josh Homme is the founder and only continuous member of the rock band Queens of the Stone Age. [alce::844__wikidata_simple__dev::p0]
> He was formerly a guitarist and founder of the stoner rock band Kyuss. [alce::844__wikidata_simple__dev::p0]
> He also co-founded Eagles of Death Metal. [alce::844__wikidata_simple__dev::p0]

Cited: alce::844__wikidata_simple__dev::p0

### `50__wikitables_composition__dev`
> Hickory, North Carolina is home to multiple museums. The Hickory Museum of Art (HMA) is an art museum in downtown Hickory, North Carolina that holds exhibitions, events, and public educational programs based on a permanent collection of 19th through 21st century American art. [alce::50__wikitables_composition__dev::p2]
> Additionally, the Sabre Society of North Carolina/Hickory Aviation Museum is a volunteer aviation historical society located at Hickory Regional Airport in Hickory, North Carolina that restores and preserves vintage jet fighter aircraft from the Korean and Vietnam eras. [alce::50__wikitables_composition__dev::p24]

Cited: alce::50__wikitables_composition__dev::p2, alce::50__wikitables_composition__dev::p24

### `469__wikitables_simple__dev`
> Several individuals were nuclear whistleblowers:

Gregory Minor, Richard Hubbard, and Dale Bridenbaugh were nuclear engineers who "blew the whistle" on safety problems at nuclear power plants in the United States in 1976. [alce::469__wikitables_simple__dev::p0]
> George Galatis was a senior nuclear engineer who reported safety problems at the Millstone 1 Nuclear Power Plant relating to reactor refueling procedures in 1995. [alce::469__wikitables_simple__dev::p0]
> Richard Levernier is an American nuclear whistleblower who worked for 23 years as a nuclear security professional and identified security problems at U.S. nuclear facilities, specifically problems with contingency planning to protect US nuclear plants from terrorist attacks after 9/11. [alce::469__wikitables_simple__dev::p6]
> Rainer Moormann is a German chemist and nuclear whistleblower who published a critical paper on the safety of pebble bed reactors in 2008. [alce::469__wikitables_simple__dev::p31]

Cited: alce::469__wikitables_simple__dev::p0, alce::469__wikitables_simple__dev::p31, alce::469__wikitables_simple__dev::p6

### `139__wikidata_comp__dev`
_Refused._

### `200__wikidata_comp__dev`
_Refused._

### `478__wikitables_simple__dev`
_Refused._

### `943__wikidata_simple__dev`
> The sources mention three specific ships of the Fubuki-class destroyer:

Japanese destroyer Fubuki (1927) was a Fubuki-class destroyer built at the Maizuru Naval Arsenal. [alce::943__wikidata_simple__dev::p2]
> Japanese destroyer Ayanami (1929) was a Fubuki-class destroyer built at the Fujinagata Shipyards in Osaka. [alce::943__wikidata_simple__dev::p19]
> Japanese destroyer Uranami (1928) was a Fubuki-class destroyer built at the Uraga Dock Company. [alce::943__wikidata_simple__dev::p29]
> The sources indicate that the Fubuki-class consisted of twenty-four destroyers total, [alce::943__wikidata_simple__dev::p1]
> but only these three individual ships are specifically named in the provided sources.

Cited: alce::943__wikidata_simple__dev::p1, alce::943__wikidata_simple__dev::p19, alce::943__wikidata_simple__dev::p2, alce::943__wikidata_simple__dev::p29

### `199__wikidata_comp__dev`
> Based on the provided sources, several teams competed in Major League Soccer All-Star Games:

The MLS All-Stars faced Manchester United of the English Premier League in the 2010 All-Star Game. [alce::199__wikidata_comp__dev::p0]
> Chelsea FC, England's 2012 champions of both the FA Cup and UEFA Champions League, was the opponent in the 2012 MLS All-Star Game. [alce::199__wikidata_comp__dev::p9]
> Bayern Munich competed against the MLS All-Stars in the 2014 All-Star Game, becoming the first German team to play in the All-Star Game. [alce::199__wikidata_comp__dev::p4]
> Additionally, the sources indicate that historically, the Eastern Conference and Western Conference of Major League Soccer squared off against each other in the traditional all-star game format before the league evolved to invite international clubs. [alce::199__wikidata_comp__dev::p13]

Cited: alce::199__wikidata_comp__dev::p0, alce::199__wikidata_comp__dev::p13, alce::199__wikidata_comp__dev::p4, alce::199__wikidata_comp__dev::p9

### `812__wikidata_simple__dev`
> Marion Zimmer Bradley edited several pieces of literature. She founded and initially edited Marion Zimmer Bradley's Fantasy Magazine, a quarterly fantasy magazine that ran from summer 1988 through December 2000. [alce::812__wikidata_simple__dev::p6]
> She was also the editor of the long-running "Sword and Sorceress" anthology series, which featured fantasy stories with original and non-traditional heroines. [alce::812__wikidata_simple__dev::p9]
> Additionally, she edited Marion Zimmer Bradley's Darkover, a collection of science fantasy short stories set in her Darkover world. [alce::812__wikidata_simple__dev::p10]

Cited: alce::812__wikidata_simple__dev::p10, alce::812__wikidata_simple__dev::p6, alce::812__wikidata_simple__dev::p9

### `179__wikidata_intersection__dev`
> Based on the provided sources, several films produced by B. Nagi Reddy had music composed by Ghantasala Venkateswara.

"Patala Bhairavi" (1951) was produced by B. Nagi Reddy and had music composed by Ghantasala. [alce::179__wikidata_intersection__dev::p2]
> and [alce::179__wikidata_intersection__dev::p7]
> "Mayabazaar" (1957) was produced by B. Nagi Reddy and had music composed by Ghantasala. [alce::179__wikidata_intersection__dev::p2]
> and [alce::179__wikidata_intersection__dev::p7]
> "Gundamma Katha" (1962) was produced by B. Nagi Reddy and had music composed by Ghantasala. [alce::179__wikidata_intersection__dev::p2]
> and [alce::179__wikidata_intersection__dev::p7]

Cited: alce::179__wikidata_intersection__dev::p2, alce::179__wikidata_intersection__dev::p7

### `25__wikitables_composition__dev`
> Based on the provided sources, here are the museums in Cambridge, Cambridgeshire:

The Museum of Cambridge, formerly known as the Cambridge & County Folk Museum, is located on Castle Street in central Cambridge. [alce::25__wikitables_composition__dev::p0]
> The Fitzwilliam Museum is the art and antiquities museum of the University of Cambridge, located on Trumpington Street in central Cambridge. [alce::25__wikitables_composition__dev::p28]
> Other University of Cambridge Museums include the Museum of Archaeology and Anthropology, The Polar Museum, The Sedgwick Museum of Earth Sciences, Museum of Classical Archaeology, The Whipple Museum of the History of Science, and the University Museum of Zoology. [alce::25__wikitables_composition__dev::p2]
> The Cambridge Museum of Technology is an industrial heritage museum situated in Cambridge. [alce::25__wikitables_composition__dev::p11]

Cited: alce::25__wikitables_composition__dev::p0, alce::25__wikitables_composition__dev::p11, alce::25__wikitables_composition__dev::p2, alce::25__wikitables_composition__dev::p28

### `409__wikidata_intersection__dev`
_Refused._

### `497__wikitables_simple__dev`
> Based on the provided sources, the lighthouses with a height of at least 26 meters are:

1. The Polish lighthouse located close to town is 26 metres tall. [alce::497__wikitables_simple__dev::p5]
> 2. The tallest Portuguese lighthouse in Barra is 62 metres from the ground (but 66 metres above sea level). [alce::497__wikitables_simple__dev::p36]

Cited: alce::497__wikitables_simple__dev::p36, alce::497__wikitables_simple__dev::p5

### `376__wikidata_comp__dev`
> The Bishop of Reading, Eric Henry Knell, was educated at Trinity College, Oxford. [alce::376__wikidata_comp__dev::p47]

Cited: alce::376__wikidata_comp__dev::p47

### `385__wikidata_intersection__dev`
> Based on the provided sources, Everton FC competed in the following FA Cup Finals:

Everton reached an FA Cup final on 26 March 1893, losing 1–0 against Wolverhampton Wanderers at Fallowfield Stadium, Manchester. [alce::385__wikidata_intersection__dev::p25]
> Everton reached another FA Cup final on 10 April 1897, losing 3–2 against Aston Villa at Crystal Palace. [alce::385__wikidata_intersection__dev::p25]
> Everton won an FA Cup final on 20 April 1906 against Newcastle United at Crystal Palace. [alce::385__wikidata_intersection__dev::p25]
> Everton reached their second successive FA Cup final on 20 April 1907, finishing in a 2–1 defeat to Sheffield Wednesday. [alce::385__wikidata_intersection__dev::p25]
> Everton reached an FA Cup final after the 2009–10 season, where they were overcome by Chelsea and lost 2–1. [alce::385__wikidata_intersection__dev::p75]
> Everton reached the FA Cup semi-finals during the 2015–16 season. [alce::385__wikidata_intersection__dev::p58]

Cited: alce::385__wikidata_intersection__dev::p25, alce::385__wikidata_intersection__dev::p58, alce::385__wikidata_intersection__dev::p75

### `626__wikidata_simple__dev`
> The Boston Celtics selected multiple players in NBA drafts across different years:

Jaylen Brown from the University of California, Guerschon Yabusele from France, and Ante Žižić from Croatia were drafted in the first round. [alce::626__wikidata_simple__dev::p1]
> In another draft, the Celtics drafted Jared Sullinger, Fab Melo, and Kris Joseph with their 21st, 22nd, and 51st picks respectively. [alce::626__wikidata_simple__dev::p0]
> Larry Bird of Indiana State was selected with the 6th pick. [alce::626__wikidata_simple__dev::p36]
> Tom Heinsohn from the College of the Holy Cross was selected as Boston Celtics' territorial pick. [alce::626__wikidata_simple__dev::p76]
> Bill Russell from the University of San Francisco was selected by the St. Louis Hawks and immediately traded to the Boston Celtics. [alce::626__wikidata_simple__dev::p76]
> Terry Rozier, R.J. Hunter, Jordan Mickey, and Marcus Thornton were selected with the 16th, 28th, 33rd, and 45th selections respectively in the 2015 NBA draft. [alce::626__wikidata_simple__dev::p39]

Cited: alce::626__wikidata_simple__dev::p0, alce::626__wikidata_simple__dev::p1, alce::626__wikidata_simple__dev::p36, alce::626__wikidata_simple__dev::p39, alce::626__wikidata_simple__dev::p76

### `193__wikidata_intersection__dev`
> The Miami Dolphins participated in multiple Super Bowls. They made their first Super Bowl appearance in Super Bowl VI, where they lost to the Dallas Cowboys. [alce::193__wikidata_intersection__dev::p2]
> The following year, they won Super Bowl VIII. [alce::193__wikidata_intersection__dev::p62]
> The Dolphins also appeared in Super Bowl VII, which they won. [alce::193__wikidata_intersection__dev::p88]
> Additionally, they were the first team to appear in three consecutive Super Bowls. [alce::193__wikidata_intersection__dev::p10]
> The Dolphins also appeared in Super Bowl XVII and Super Bowl XIX, losing both games. [alce::193__wikidata_intersection__dev::p62]
> They entered their fifth Super Bowl in team history after posting a 14–2 regular season record, where they faced the San Francisco 49ers. [alce::193__wikidata_intersection__dev::p17]

Cited: alce::193__wikidata_intersection__dev::p10, alce::193__wikidata_intersection__dev::p17, alce::193__wikidata_intersection__dev::p2, alce::193__wikidata_intersection__dev::p62, alce::193__wikidata_intersection__dev::p88

### `737__wikidata_simple__dev`
> Janine Marmot produced several creative works. She is best known for the BAFTA-winning documentary Bodysong and the relationship drama Kelly + Victor, which won the Outstanding British Debut BAFTA award in 2014. [alce::737__wikidata_simple__dev::p0]
> Her other feature credits as producer include No Greater Love, Looking For Light, Institute Benjamenta directed by The Brothers Quay, I Could Read The Sky directed by Nichola Bruce, and Made In Heaven. [alce::737__wikidata_simple__dev::p1]

Cited: alce::737__wikidata_simple__dev::p0, alce::737__wikidata_simple__dev::p1

### `746__wikidata_simple__dev`
> The members of (G)I-dle were Miyeon, Minnie, Soojin, Soyeon, Yuqi, and Shuhua. [alce::746__wikidata_simple__dev::p0]

Cited: alce::746__wikidata_simple__dev::p0

### `412__wikidata_comp__dev`
> Richland High School is a school attended by an athlete drafted by the Milwaukee Brewers. [alce::412__wikidata_comp__dev::p63]

Cited: alce::412__wikidata_comp__dev::p63

### `873__wikidata_simple__dev`
> Several rulers hail from Characene:

Abinergaios II was a ruler of Characene who reigned around 170 AD. [alce::873__wikidata_simple__dev::p12]
> Meredates was a ruler of Characene who ruled from 131 to 150/151. [alce::873__wikidata_simple__dev::p72]
> Artabazos I of Characene was a king of Characene whose reign lasted from 49/48-48/47 BC. [alce::873__wikidata_simple__dev::p47]
> Orabazes II was a King of Characene whose reign was from 150/51 to 165 AD. [alce::873__wikidata_simple__dev::p19]

Cited: alce::873__wikidata_simple__dev::p12, alce::873__wikidata_simple__dev::p19, alce::873__wikidata_simple__dev::p47, alce::873__wikidata_simple__dev::p72

### `261__wikidata_intersection__dev`
> Multiple movies had Adam Sandler and Tim Herlihy as screenwriters. "Billy Madison" (1995) was written by Sandler and Tim Herlihy. [alce::261__wikidata_intersection__dev::p36]
> "Happy Gilmore" (1996) had its screenplay written by Sandler and Tim Herlihy. [alce::261__wikidata_intersection__dev::p2]
> "The Ridiculous 6" (2015) was written by Tim Herlihy and Adam Sandler. [alce::261__wikidata_intersection__dev::p44]

Cited: alce::261__wikidata_intersection__dev::p2, alce::261__wikidata_intersection__dev::p36, alce::261__wikidata_intersection__dev::p44

### `527__wikitables_simple__dev`
> Based on the provided sources, I can identify the following commercially available software-defined radios:

Universal Software Radio Peripheral (USRP) is a range of software-defined radios designed and sold by Ettus Research and its parent company, National Instruments. [alce::527__wikitables_simple__dev::p65]
> The USRP product family is intended to be a comparatively inexpensive hardware platform for software radio and is commonly used by research labs, universities, and hobbyists. [alce::527__wikitables_simple__dev::p65]
> GNU Radio is a free software development toolkit that can be used with external RF hardware to create software-defined radios and is widely used in hobbyist, academic, and commercial environments. [alce::527__wikitables_simple__dev::p25]
> However, the sources provided do not contain a comprehensive list of all commercially available software-defined radios beyond these two examples.

Cited: alce::527__wikitables_simple__dev::p25, alce::527__wikitables_simple__dev::p65

### `566__wikidata_simple__dev`
> Cherokee is the native language of the Cherokee people. [alce::566__wikidata_simple__dev::p7]
> The Cherokee are one of the indigenous people of the Southeastern Woodlands who were concentrated in southwestern North Carolina, southeastern Tennessee, and the tips of western South Carolina and northeastern Georgia prior to the 18th century. [alce::566__wikidata_simple__dev::p5]

Cited: alce::566__wikidata_simple__dev::p5, alce::566__wikidata_simple__dev::p7

### `312__wikidata_comp__dev`
_Refused._

### `311__wikidata_intersection__dev`
> Based on the provided sources, here are the competitions in which Everton F.C. and Liverpool F.C. participated:

**Everton F.C.** competes in the Premier League, the top flight of English football. [alce::311__wikidata_intersection__dev::p2]
> Everton have competed in the League Championship, the FA Cup, and the UEFA Cup Winners Cup. [alce::311__wikidata_intersection__dev::p1]
> Both Everton and Liverpool competed in the Champions League. [alce::311__wikidata_intersection__dev::p4]
> **Liverpool F.C.** have competed in top-flight titles and the FA Cup. [alce::311__wikidata_intersection__dev::p1]
> Liverpool have won the European Cup 5 times. [alce::311__wikidata_intersection__dev::p1]
> Liverpool competed in the Champions League. [alce::311__wikidata_intersection__dev::p4]

Cited: alce::311__wikidata_intersection__dev::p1, alce::311__wikidata_intersection__dev::p2, alce::311__wikidata_intersection__dev::p4

### `295__wikidata_intersection__dev`
> The movie "Madrasapattinam" featured A.L. Vijay as director and G. V. Prakash Kumar as composer. [alce::295__wikidata_intersection__dev::p0]

Cited: alce::295__wikidata_intersection__dev::p0

### `954__wikidata_comp__dev`
_Refused._

### `427__wikidata_intersection__dev`
> Based on the provided sources, Manchester United and Tottenham Hotspur F.C. both participated in the following competitions:

Manchester United participated in the European Cup, which they won in 1968, becoming the first English club to win it. [alce::427__wikidata_intersection__dev::p39]
> Tottenham Hotspur won the Cup Winners' Cup in 1963. [alce::427__wikidata_intersection__dev::p15]
> During the 2000–01 season, Tottenham Hotspur participated in the English Premier League, FA Cup, and Football League Cup. [alce::427__wikidata_intersection__dev::p51]
> During the 2018–19 season, Tottenham competed in the Premier League, FA Cup, EFL Cup, and the Champions League. [alce::427__wikidata_intersection__dev::p66]
> Manchester United has competed in every UEFA-organised competition except the now-defunct Intertoto Cup. [alce::427__wikidata_intersection__dev::p39]

Cited: alce::427__wikidata_intersection__dev::p15, alce::427__wikidata_intersection__dev::p39, alce::427__wikidata_intersection__dev::p51, alce::427__wikidata_intersection__dev::p66

### `220__wikidata_intersection__dev`
_Refused._

### `468__wikidata_intersection__dev`
> Rangers F.C. won the 1946–47 Scottish League Cup, which had Aberdeen F.C. participating in it as the finalist. [alce::468__wikidata_intersection__dev::p23]
> Rangers defeated Aberdeen 4–0 in the Final of that competition. [alce::468__wikidata_intersection__dev::p23]

Cited: alce::468__wikidata_intersection__dev::p23

### `841__wikidata_simple__dev`
> The Privy Council of the United Kingdom's membership mainly comprises senior politicians, who are current or former members of either the House of Commons or the House of Lords. [alce::841__wikidata_simple__dev::p0]
> Additionally, officials from other Commonwealth realms are also appointed to the body, with Prime Ministers of Commonwealth countries which retain the British monarch as their sovereign being conventionally sworn as Privy Counsellors. [alce::841__wikidata_simple__dev::p32]
> The Judicial Committee of the Privy Council consists of senior judges appointed as Privy Counsellors, predominantly Justices of the Supreme Court of the United Kingdom and senior judges from the Commonwealth. [alce::841__wikidata_simple__dev::p13]

Cited: alce::841__wikidata_simple__dev::p0, alce::841__wikidata_simple__dev::p13, alce::841__wikidata_simple__dev::p32

### `921__wikidata_simple__dev`
> Based on the provided sources, several groups served the Union:

Nearly 100,000 white Southern men served in the Union army during the American Civil War. [alce::921__wikidata_simple__dev::p98]
> About 700 African-American soldiers from St. Mary's County served on the Union side during the war, including many men who escaped slavery and joined the Union cause, as well as free Black citizens. [alce::921__wikidata_simple__dev::p39]
> White soldiers from all walks of life also served in the Union Army. [alce::921__wikidata_simple__dev::p39]
> USS Union (AKA-106) was a ship of the United States Navy that served as a commissioned ship for 25 years and 1 month. [alce::921__wikidata_simple__dev::p52]

Cited: alce::921__wikidata_simple__dev::p39, alce::921__wikidata_simple__dev::p52, alce::921__wikidata_simple__dev::p98

### `803__wikidata_simple__dev`
> Based on the provided sources, the Eagle brand's most known model was the AMC Eagle. The AMC Eagle "rapidly became one of the company's best-known products and is considered one of the first 'crossover SUVs'." [alce::803__wikidata_simple__dev::p44]
> Additionally, the "Eagle" name was taken by Chrysler from "the four-wheel drive AMC Eagle models that were introduced for the 1980 model year," which was "arguably the first modern mass-production crossover automobile." [alce::803__wikidata_simple__dev::p2]

Cited: alce::803__wikidata_simple__dev::p2, alce::803__wikidata_simple__dev::p44

### `218__wikidata_intersection__dev`
> The movie "Neelakkuyil" was directed by P. Bhaskaran (along with Ramu Kariat) with music composed by K. Raghavan. [alce::218__wikidata_intersection__dev::p0]

Cited: alce::218__wikidata_intersection__dev::p0

### `194__wikidata_intersection__dev`
> Based on the provided sources, I can identify multiple movies that were EON productions with Richard Maibaum as screenwriter:

"For Your Eyes Only" was an EON production with Richard Maibaum as screenwriter. [alce::194__wikidata_intersection__dev::p54]
> "Licence to Kill" was also an EON production with Richard Maibaum as screenwriter. [alce::194__wikidata_intersection__dev::p54]
> Additionally, there was another film for which Richard Maibaum was the scriptwriter, assisted by Michael G. Wilson, produced by EON Productions. [alce::194__wikidata_intersection__dev::p47]

Cited: alce::194__wikidata_intersection__dev::p47, alce::194__wikidata_intersection__dev::p54

### `1350__wikidata_simple__dev`
> Daniele Bracciali won his only ATP singles title in April 2006, at Casablanca, on clay. [alce::1350__wikidata_simple__dev::p1]
> In the final he beat Nicolás Massú. [alce::1350__wikidata_simple__dev::p1]

Cited: alce::1350__wikidata_simple__dev::p1

### `76__wikitables_composition__dev`
_Refused._

### `236__wikidata_intersection__dev`
> The principal pupils of Arnold Schoenberg who counted themselves among the Second Viennese School were Alban Berg and Anton Webern, who were among his first composition pupils. [alce::236__wikidata_intersection__dev::p1]
> Other pupils of this generation included Ernst Krenek, Heinrich Jalowetz, Erwin Stein and Egon Wellesz. [alce::236__wikidata_intersection__dev::p1]
> Additional pupils included Eduard Steuermann, Hanns Eisler, Roberto Gerhard, Norbert von Hannenheim, Rudolf Kolisch, Paul A. Pisk, Karl Rankl, Josef Rufer, Nikos Skalkottas, Viktor Ullmann, and Winfried Zillig. [alce::236__wikidata_intersection__dev::p2]

Cited: alce::236__wikidata_intersection__dev::p1, alce::236__wikidata_intersection__dev::p2

### `598__wikidata_simple__dev`
> Tolly Cobbold sponsored the Tolly Cobbold Classic, a non-ranking snooker tournament staged between 1979 and 1984. [alce::598__wikidata_simple__dev::p1]
> After 1984, Tolly Cobbold decided to sponsor the English Professional Championship instead. [alce::598__wikidata_simple__dev::p0]

Cited: alce::598__wikidata_simple__dev::p0, alce::598__wikidata_simple__dev::p1

### `185__wikidata_comp__dev`
> The question asks "Which driver was the winner of the Daytona 500?" without specifying which year. The sources provide information about multiple Daytona 500 winners from different years.

Based on the most recent winner mentioned in the sources: Kurt Busch won the 2017 Daytona 500. [alce::185__wikidata_comp__dev::p34]
> However, if you are asking about the defending champion at the time the sources were written: Austin Dillon is the defending winner of the Daytona 500, having won it in 2018.
> Other Daytona 500 winners mentioned in the sources include Dale Earnhardt, Jr., who won in 2014 [alce::185__wikidata_comp__dev::p5]
> , Lee Petty, who won in 1959 [alce::185__wikidata_comp__dev::p73]
> , and Michael Waltrip, who won in an earlier race. [alce::185__wikidata_comp__dev::p39]

Cited: alce::185__wikidata_comp__dev::p34, alce::185__wikidata_comp__dev::p39, alce::185__wikidata_comp__dev::p5, alce::185__wikidata_comp__dev::p73

### `53__wikitables_composition__dev`
> Based on the provided sources, I can identify one Indonesian mosque located in South Sulawesi Province:

The Great Mosque of Makassar is a mosque located in Makassar, Indonesia, and serves as the main mosque of South Sulawesi Province. [alce::53__wikitables_composition__dev::p41]
> The sources provided do not contain information about other mosques in South Sulawesi beyond the Great Mosque of Makassar.

Cited: alce::53__wikitables_composition__dev::p41

### `187__wikidata_intersection__dev`
_Refused._

### `915__wikidata_simple__dev`
_Refused._

### `42__wikitables_composition__dev`
> Genesee Township is a township in Michigan in Genesee County. [alce::42__wikitables_composition__dev::p1]

Cited: alce::42__wikitables_composition__dev::p1

### `816__wikidata_simple__dev`
_Refused._

### `1364__wikidata_simple__dev`
> Mercer Island is a natural place adjacent to Lake Washington. [alce::1364__wikidata_simple__dev::p5]

Cited: alce::1364__wikidata_simple__dev::p5

### `763__wikidata_simple__dev`
> Setsuna F. Seiei made his first appearance in Mobile Suit Gundam 00. [alce::763__wikidata_simple__dev::p20]

Cited: alce::763__wikidata_simple__dev::p20

### `339__wikidata_intersection__dev`
> MLB umpires work for both the National and American Leagues. [alce::339__wikidata_intersection__dev::p45]
> Beginning with the 2000 season, every umpire would work in both leagues as a result of the end of separate umpiring staffs for the American and National Leagues. [alce::339__wikidata_intersection__dev::p6]
> As a result of the 2000 collective bargaining agreement between Major League Baseball and the newly formed World Umpires Association, all umpires were placed on one roster and can work in either league.

Cited: alce::339__wikidata_intersection__dev::p45, alce::339__wikidata_intersection__dev::p6

### `828__wikidata_simple__dev`
> Dev Anand produced several movies. [alce::828__wikidata_simple__dev::p3]
> He produced a total of 35 films, of which 18 were commercially successful at the box office. [alce::828__wikidata_simple__dev::p3]
> Specific examples of films he produced include:

Kala Bazar, a 1960 Hindi film produced for Navketan Films. [alce::828__wikidata_simple__dev::p84]
> Kala Pani, a 1958 Hindi film produced for Navketan Films. [alce::828__wikidata_simple__dev::p70]
> Hum Dono, a 1961 Hindi film produced by Dev Anand and Navketan Films. [alce::828__wikidata_simple__dev::p15]

Cited: alce::828__wikidata_simple__dev::p15, alce::828__wikidata_simple__dev::p3, alce::828__wikidata_simple__dev::p70, alce::828__wikidata_simple__dev::p84

### `774__wikidata_simple__dev`
_Refused._

### `396__wikidata_intersection__dev`
_Refused._

### `955__wikidata_comp__dev`
_Refused._

### `731__wikidata_simple__dev`
_Refused._

### `861__wikidata_simple__dev`
> Edgar F. Codd invented the relational model for database management, which serves as the theoretical basis for relational databases and relational database management systems. [alce::861__wikidata_simple__dev::p0]
> He also devised Codd's cellular automaton in 1968, which was designed to recreate the computation- and construction-universality of von Neumann's cellular automaton but with fewer states. [alce::861__wikidata_simple__dev::p4]
> Additionally, Codd created a systematic method to decompose and organize relational databases, known as database normalization. [alce::861__wikidata_simple__dev::p11]

Cited: alce::861__wikidata_simple__dev::p0, alce::861__wikidata_simple__dev::p11, alce::861__wikidata_simple__dev::p4

### `532__wikitables_simple__dev`
> Based on the provided sources, **Xi** is an alternate reality game. [alce::532__wikitables_simple__dev::p87]
> Xi was the world's first console-based and virtual world-based alternate reality game that unfolded in real time on the PlayStation 3 through PlayStation Home. [alce::532__wikitables_simple__dev::p87]

Cited: alce::532__wikitables_simple__dev::p87

### `553__wikitables_simple__dev`
_Refused._

### `635__wikidata_simple__dev`
> The Roman Republic had different representatives depending on the time period. In the 18th century Roman Republic (proclaimed 15 February 1798), Louis Alexandre Berthier, a general of Napoleon, invaded Rome and established it as a client republic under the French Directory. [alce::635__wikidata_simple__dev::p9]
> In the 19th century Roman Republic (declared 9 February 1849), the republic was led by Carlo Armellini, Giuseppe Mazzini, and Aurelio Saffi, who together formed a triumvirate. [alce::635__wikidata_simple__dev::p0]

Cited: alce::635__wikidata_simple__dev::p0, alce::635__wikidata_simple__dev::p9

### `907__wikidata_simple__dev`
_Refused._

### `511__wikitables_simple__dev`
> Based on the provided sources, the following typhoons were classified as super typhoons:

From the 1997 season: Isa, Nestor, Rosie, Winnie, Bing, Oliwa, Ginger, Ivan, Joan, Keith, and Paka. [alce::511__wikitables_simple__dev::p14]
> From the 1962 season: Georgia, Emma, Ruth, Opal, Amy, and Karen. [alce::511__wikitables_simple__dev::p3]
> From the 2014 season: Neoguri, Rammasun, Halong, Genevieve, Vongfong, Nuri, and Hagupit. [alce::511__wikitables_simple__dev::p22]

Cited: alce::511__wikitables_simple__dev::p14, alce::511__wikitables_simple__dev::p22, alce::511__wikitables_simple__dev::p3

### `467__wikidata_intersection__dev`
> Manchester City FC won multiple FA Cups. They won the 1903–04 FA Cup, beating Bolton Wanderers 1–0 in the final at Crystal Palace through a goal scored by Billy Meredith. [alce::467__wikidata_intersection__dev::p0]
> They also won the 1934 FA Cup Final with a 2–1 victory over Portsmouth. [alce::467__wikidata_intersection__dev::p52]
> Additionally, Manchester City won the 1955–56 FA Cup, defeating Birmingham City 3–1 in the final at Wembley, London. [alce::467__wikidata_intersection__dev::p4]

Cited: alce::467__wikidata_intersection__dev::p0, alce::467__wikidata_intersection__dev::p4, alce::467__wikidata_intersection__dev::p52

### `789__wikidata_simple__dev`
> Noggin broadcasted several television programs. Programs that aired on Noggin included "Phred on Your Head Show", "A Walk In Your Shoes", "Sponk!", and "Bill Nye the Science Guy". [alce::789__wikidata_simple__dev::p7]
> Noggin also became the primary broadcaster of "Tiny Planets", "Pinky Dinky Doo", and "The Upside Down Show". [alce::789__wikidata_simple__dev::p21]

Cited: alce::789__wikidata_simple__dev::p21, alce::789__wikidata_simple__dev::p7

### `617__wikidata_simple__dev`
> Based on the provided sources, several written works were produced in or set in Katoomba:

"The Bogan Mondrian" is a novel located in modern-day Katoomba. [alce::617__wikidata_simple__dev::p0]
> "Love, ghosts and nose-hair" is a verse-novel also set in the town of Katoomba. [alce::617__wikidata_simple__dev::p0]
> "The Pure Land" is a novel by David Foster with Part One set in 1930s Katoomba, New South Wales. [alce::617__wikidata_simple__dev::p6]

Cited: alce::617__wikidata_simple__dev::p0, alce::617__wikidata_simple__dev::p6

### `365__wikidata_comp__dev`
> Stephen Gaghan wrote the screenplay for "Traffic," which was directed by Steven Soderbergh. [alce::365__wikidata_comp__dev::p0]
> Stephen Gaghan also wrote and directed "Syriana." [alce::365__wikidata_comp__dev::p32]

Cited: alce::365__wikidata_comp__dev::p0, alce::365__wikidata_comp__dev::p32

### `821__wikidata_simple__dev`
> Malcolm X belonged to the Nation of Islam faith. [alce::821__wikidata_simple__dev::p33]
> Muhammad Ali also belonged to the Nation of Islam faith. [alce::821__wikidata_simple__dev::p33]
> Elijah Muhammad was a leader of the Nation of Islam. [alce::821__wikidata_simple__dev::p33]
> Clarence 13X was a former member of the Nation of Islam before founding his own organization. [alce::821__wikidata_simple__dev::p84]

Cited: alce::821__wikidata_simple__dev::p33, alce::821__wikidata_simple__dev::p84

### `1365__wikidata_simple__dev`
_Refused._

### `7__wikitables_composition__dev`
> New York City is known for its ballet, specifically as the home of the New York City Ballet (NYCB). [alce::7__wikitables_composition__dev::p1]
> The New York City Ballet has been housed at the David H. Koch Theater (originally named the New York State Theater) at Lincoln Center since its opening in 1964. [alce::7__wikitables_composition__dev::p14]

Cited: alce::7__wikitables_composition__dev::p1, alce::7__wikitables_composition__dev::p14

### `395__wikidata_comp__dev`
> Dan Halsted served as producer on projects directed by Oliver Stone. [alce::395__wikidata_comp__dev::p5]
> Specifically, Halsted partnered with filmmaker Oliver Stone in 1995 to create Illusion Entertainment, and together they produced films such as "Nixon," "U Turn," "Any Given Sunday," and other projects. [alce::395__wikidata_comp__dev::p1]

Cited: alce::395__wikidata_comp__dev::p1, alce::395__wikidata_comp__dev::p5

### `383__wikidata_intersection__dev`
> Multiple films were directed by both Emeric Pressburger and Michael Powell. [alce::383__wikidata_intersection__dev::p22]
> Notable examples include "49th Parallel" (1941), "The Life and Death of Colonel Blimp" (1943), "A Matter of Life and Death" (1946), "Black Narcissus" (1947), "The Red Shoes" (1948), and "The Tales of Hoffmann" (1951). [alce::383__wikidata_intersection__dev::p22]
> In total, they made 19 feature films together as co-producers, writers and directors under their production company "The Archers." [alce::383__wikidata_intersection__dev::p2]

Cited: alce::383__wikidata_intersection__dev::p2, alce::383__wikidata_intersection__dev::p22

### `201__wikidata_comp__dev`
> Ranjan was doing the screenwriting for the movie produced by Antony Perumbavoor. [alce::201__wikidata_comp__dev::p1]

Cited: alce::201__wikidata_comp__dev::p1

### `192__wikidata_comp__dev`
> Gustav Holst was a choral symphony composer. [alce::192__wikidata_comp__dev::p3]
> George Dyson was also a choral symphony composer. [alce::192__wikidata_comp__dev::p11]

Cited: alce::192__wikidata_comp__dev::p11, alce::192__wikidata_comp__dev::p3

### `243__wikidata_comp__dev`
> In movies where Bill Condon was screenwriter, Bill Condon himself was a director. [alce::243__wikidata_comp__dev::p4]
> Specifically, for "Gods and Monsters" (1998), "Kinsey" (2004), and "Dreamgirls" (2006), Bill Condon both wrote and directed these films. [alce::243__wikidata_comp__dev::p4]
> For "Chicago" (2002), where Condon wrote the screenplay, the sources do not specify who the director was.

Cited: alce::243__wikidata_comp__dev::p4

### `167__wikidata_comp__dev`
> Many teams have competed in a Super Bowl. The Green Bay Packers and New York Giants have won four Super Bowl championships. [alce::167__wikidata_comp__dev::p0]
> Fourteen other NFL franchises have won at least one Super Bowl. [alce::167__wikidata_comp__dev::p0]
> Eight teams have appeared in Super Bowl games without a win. [alce::167__wikidata_comp__dev::p0]
> The New England Patriots have made nine appearances in the Super Bowl. [alce::167__wikidata_comp__dev::p71]
> The Dallas Cowboys and Pittsburgh Steelers are among four teams that have made eight appearances in the Super Bowl. [alce::167__wikidata_comp__dev::p71]

Cited: alce::167__wikidata_comp__dev::p0, alce::167__wikidata_comp__dev::p71

### `748__wikidata_simple__dev`
> Errol Morris created several films. "The Thin Blue Line" is a 1988 documentary that he is perhaps best known for. [alce::748__wikidata_simple__dev::p0]
> He also directed "The Fog of War: Eleven Lessons from the Life of Robert S. McNamara," a documentary film that won the Academy Award for Best Documentary Feature in 2003. [alce::748__wikidata_simple__dev::p0]
> Additionally, Morris directed "Gates of Heaven," a 1978 documentary about the pet cemetery business. [alce::748__wikidata_simple__dev::p20]
> He also produced and directed "Vernon, Florida," a 1981 documentary profiling residents of Vernon, Florida. [alce::748__wikidata_simple__dev::p36]
> Morris directed "Tabloid," a 2010 American documentary film. [alce::748__wikidata_simple__dev::p32]

Cited: alce::748__wikidata_simple__dev::p0, alce::748__wikidata_simple__dev::p20, alce::748__wikidata_simple__dev::p32, alce::748__wikidata_simple__dev::p36

### `810__wikidata_simple__dev`
> Betty Ross made her first appearance in The Incredible Hulk. [alce::810__wikidata_simple__dev::p1]
> She appeared in "Incredible Hulk" #1 (1962) as a romantic interest of the Hulk (Dr. Bruce Banner). [alce::810__wikidata_simple__dev::p1]

Cited: alce::810__wikidata_simple__dev::p1

### `91__wikitables_composition__dev`
_Refused._

### `938__wikidata_simple__dev`
> Orson Scott Card edited "Orson Scott Card's InterGalactic Medicine Show," an anthology published in 2008. [alce::938__wikidata_simple__dev::p21]
> He also worked as an editor for "The Ensign," the official LDS magazine. [alce::938__wikidata_simple__dev::p64]

Cited: alce::938__wikidata_simple__dev::p21, alce::938__wikidata_simple__dev::p64

### `831__wikidata_simple__dev`
> Based on the provided sources, several individuals came from the Kingdom of Iberia:

Mirian III was a king of Iberia or Kartli (Georgia), contemporaneous to the Roman emperor Constantine the Great. [alce::831__wikidata_simple__dev::p95]
> Artaxias I of the Artaxiad dynasty was a king of Iberia (modern-day Georgia) from 90 to 78 BC. [alce::831__wikidata_simple__dev::p45]
> The Iberians, who formed the nucleus of the Georgians (Kartvelians), were the population of the Kingdom of Iberia. [alce::831__wikidata_simple__dev::p2]

Cited: alce::831__wikidata_simple__dev::p2, alce::831__wikidata_simple__dev::p45, alce::831__wikidata_simple__dev::p95

### `463__wikidata_intersection__dev`
> Telemundo produced and broadcast "Boxeo Telemundo", a weekly late-night boxing series that airs on most Friday nights showcasing fights from up-and-coming boxing talents. [alce::463__wikidata_intersection__dev::p50]

Cited: alce::463__wikidata_intersection__dev::p50

### `913__wikidata_simple__dev`
> The Cleveland Cavaliers drafted several notable players across different years:

In 1986, the Cavaliers drafted Ron Harper with the eighth pick and obtained the rights to Mark Price with the 25th pick in the second round. [alce::913__wikidata_simple__dev::p79]
> In 2011, the Cavaliers selected guard Kyrie Irving with the first pick and power forward Tristan Thompson with the 4th pick. [alce::913__wikidata_simple__dev::p0]
> In 2013, the Cavaliers drafted forward Anthony Bennett of UNLV with the number one pick, making him the first Canadian-born player to be selected first overall. [alce::913__wikidata_simple__dev::p3]
> With the 19th pick that year, they selected swingman Sergey Karasev. [alce::913__wikidata_simple__dev::p3]
> In 2003, the Cavaliers selected LeBron James from St. Vincent-St. Mary High School in Akron through the draft lottery. [alce::913__wikidata_simple__dev::p20]

Cited: alce::913__wikidata_simple__dev::p0, alce::913__wikidata_simple__dev::p20, alce::913__wikidata_simple__dev::p3, alce::913__wikidata_simple__dev::p79

### `246__wikidata_comp__dev`
> Several Associate Justices of the Supreme Court of the United States attended different schools:

Katherine Leatherman Adams earned a Bachelor's degree in Comparative Literature from Brown University and a Juris Doctoral degree from the University of Chicago Law School. [alce::246__wikidata_comp__dev::p37]
> Elena Kagan attended Princeton University, Worcester College, Oxford, and Harvard Law School. [alce::246__wikidata_comp__dev::p72]
> Antonin Scalia attended Xavier High School in Manhattan, Georgetown University, and Harvard Law School. [alce::246__wikidata_comp__dev::p49]
> David Souter attended Harvard College, Oxford University, and Harvard Law School. [alce::246__wikidata_comp__dev::p13]
> Stephen Johnson Field, Henry Billings Brown, and David Josiah Brewer were educated in Stockbridge. [alce::246__wikidata_comp__dev::p94]

Cited: alce::246__wikidata_comp__dev::p13, alce::246__wikidata_comp__dev::p37, alce::246__wikidata_comp__dev::p49, alce::246__wikidata_comp__dev::p72, alce::246__wikidata_comp__dev::p94

### `149__wikidata_comp__dev`
_Refused._

### `346__wikidata_comp__dev`
> John Cairncross, one of the Cambridge Five, worked for MI6. [alce::346__wikidata_comp__dev::p13]
> He was posted from MI6 to work at Bletchley Park. [alce::346__wikidata_comp__dev::p13]

Cited: alce::346__wikidata_comp__dev::p13

### `38__wikitables_composition__dev`
> "Twelfth Night" is an example of a movie made after 1997. [alce::38__wikitables_composition__dev::p65]

Cited: alce::38__wikitables_composition__dev::p65

### `190__wikidata_intersection__dev`
> "Matula" was a movie with production by The Teng Chun that was directed by Tan Tjoei Hock. [alce::190__wikidata_intersection__dev::p83]

Cited: alce::190__wikidata_intersection__dev::p83

### `275__wikidata_intersection__dev`
> Katy Perry and Max Martin created "I Kissed a Girl" and "Hot n Cold". [alce::275__wikidata_intersection__dev::p18]

Cited: alce::275__wikidata_intersection__dev::p18

### `802__wikidata_simple__dev`
> Aston Villa F.C. has participated in multiple competitions. The club currently competes in the Championship, the second tier of the English football league system. [alce::802__wikidata_simple__dev::p12]
> Historically, they competed in the FA Premier League during the 1997–98, 1999–2000, and 2006–07 seasons. [alce::802__wikidata_simple__dev::p61]
> Aston Villa also competed in the UEFA Europa League, marking consecutive seasons in European competition. [alce::802__wikidata_simple__dev::p19]
> Additionally, the club reached the FA Cup final. [alce::802__wikidata_simple__dev::p31]
> As a founder member, Aston Villa participated in the Football League in 1888 and the Premier League in 1992. [alce::802__wikidata_simple__dev::p12]

Cited: alce::802__wikidata_simple__dev::p12, alce::802__wikidata_simple__dev::p19, alce::802__wikidata_simple__dev::p31, alce::802__wikidata_simple__dev::p61

### `102__wikidata_intersection__dev`
> Based on the provided sources, Natasha Zvereva and Gigi Fernández won multiple competitions together:

1. The 1997 French Open – Women's Doubles, where they defeated Mary Joe Fernández and Lisa Raymond 6–2, 6–3 in the final. [alce::102__wikidata_intersection__dev::p1]
> 2. The 1997 Wimbledon Championships – Women's Doubles, where they defeated Nicole Arendt and Manon Bollegraf 7–6, 6–4 in the final. [alce::102__wikidata_intersection__dev::p3]
> 3. The 1994 Lipton Championships – Women's Doubles, where they won in the final 6–3, 6–1 against Patty Fendick and Meredith McGrath. [alce::102__wikidata_intersection__dev::p4]

Cited: alce::102__wikidata_intersection__dev::p1, alce::102__wikidata_intersection__dev::p3, alce::102__wikidata_intersection__dev::p4

### `264__wikidata_intersection__dev`
_Refused._

### `382__wikidata_comp__dev`
_Refused._

### `221__wikidata_intersection__dev`
> Several movies were directed by Shaji Kailas and screenwritten by Renji Panicker. These include "Thalastaanam" (1992), "Sthalathe Pradhana Payyans" (1993), "Ekalavyan" (1993), "Mafia" (1993), "Commissioner" (1994), and "The King" (1995). [alce::221__wikidata_intersection__dev::p1]

Cited: alce::221__wikidata_intersection__dev::p1

### `69__wikitables_composition__dev`
_Refused._

### `326__wikidata_comp__dev`
_Refused._

### `959__wikidata_comp__dev`
_Refused._

### `650__wikidata_simple__dev`
> Beatrix Potter illustrated several children's books. "The Tale of Peter Rabbit" is a children's book written and illustrated by Beatrix Potter. [alce::650__wikidata_simple__dev::p34]
> "The Tale of Mrs. Tiggy-Winkle" is a children's book written and illustrated by Beatrix Potter. [alce::650__wikidata_simple__dev::p24]
> "The Tale of Jemima Puddle-Duck" is a children's book written and illustrated by Beatrix Potter. [alce::650__wikidata_simple__dev::p25]
> "The Tale of Two Bad Mice" is a children's book written and illustrated by Beatrix Potter. [alce::650__wikidata_simple__dev::p53]

Cited: alce::650__wikidata_simple__dev::p24, alce::650__wikidata_simple__dev::p25, alce::650__wikidata_simple__dev::p34, alce::650__wikidata_simple__dev::p53

### `545__wikitables_simple__dev`
> Based on the provided sources, here are specific island countries mentioned:

The United Kingdom is an island country. [alce::545__wikitables_simple__dev::p1]
> The Republic of Ireland is an island country. [alce::545__wikitables_simple__dev::p1]
> Haiti is an island country. [alce::545__wikitables_simple__dev::p1]
> The Dominican Republic is an island country. [alce::545__wikitables_simple__dev::p1]
> Indonesia is an island country. [alce::545__wikitables_simple__dev::p1]
> Japan is an island country. [alce::545__wikitables_simple__dev::p0]
> New Zealand is an island country. [alce::545__wikitables_simple__dev::p0]
> Cuba is an island country. [alce::545__wikitables_simple__dev::p0]
> Bahrain is an island country. [alce::545__wikitables_simple__dev::p0]
> Singapore is an island country. [alce::545__wikitables_simple__dev::p0]
> Iceland is an island country. [alce::545__wikitables_simple__dev::p0]
> Malta is an island country. [alce::545__wikitables_simple__dev::p0]
> Taiwan is an island country. [alce::545__wikitables_simple__dev::p0]
> The Philippines is an island country. [alce::545__wikitables_simple__dev::p0]
> The Bahamas is an island country. [alce::545__wikitables_simple__dev::p0]
> Seychelles is an island country. [alce::545__wikitables_simple__dev::p0]
> The Maldives is an island country. [alce::545__wikitables_simple__dev::p0]
> Trinidad and Tobago is an island country. [alce::545__wikitables_simple__dev::p0]

Cited: alce::545__wikitables_simple__dev::p0, alce::545__wikitables_simple__dev::p1

### `471__wikitables_simple__dev`
> Here are some existing search engines:

Notable historical and current search engines include Archie (developed in 1990), Lycos (1994), Alta Vista (1995), Magellan (1995), Google (1998), Yahoo! Search (2004), MSN Search (2005), and Bing (2009). [alce::471__wikitables_simple__dev::p13]
> Other search engines that have been developed include Excite, Infoseek, Inktomi, Northern Light, and Netscape. [alce::471__wikitables_simple__dev::p1]
> Some of the most popular search engines today are Google, Yahoo, Bing, and Baidu. [alce::471__wikitables_simple__dev::p8]
> Additional search engines include regional competitors such as Naver.com and Daum.net in South Korea, Yandex in Russia, Seznam.cz in the Czech Republic, and DuckDuckGo. [alce::471__wikitables_simple__dev::p81]

Cited: alce::471__wikitables_simple__dev::p1, alce::471__wikitables_simple__dev::p13, alce::471__wikitables_simple__dev::p8, alce::471__wikitables_simple__dev::p81

### `258__wikidata_intersection__dev`
> The 2007 UEFA Champions League Final was a competition in which Liverpool F.C. participated. [alce::258__wikidata_intersection__dev::p10]
> This match was played between A.C. Milan of Italy and Liverpool F.C. of England on 23 May 2007 at the Olympic Stadium, Athens, Greece. [alce::258__wikidata_intersection__dev::p10]

Cited: alce::258__wikidata_intersection__dev::p10

### `68__wikitables_composition__dev`
_Refused._

### `262__wikidata_comp__dev`
> Meredith Corporation's headquarters are located in Des Moines, Iowa, USA. [alce::262__wikidata_comp__dev::p1]

Cited: alce::262__wikidata_comp__dev::p1

### `268__wikidata_intersection__dev`
> Tottenham Hotspur F.C. battled Arsenal F.C. in the North London Derby. [alce::268__wikidata_intersection__dev::p12]
> One notable match occurred on 30 April 2017, when Tottenham beat Arsenal 2-0 in the final North London Derby at White Hart Lane. [alce::268__wikidata_intersection__dev::p48]
> Additionally, they competed in the 2008–09 Premier Academy League Play-off Final, where Arsenal defeated Tottenham Hotspur 1-0 at White Hart Lane on 17 May. [alce::268__wikidata_intersection__dev::p29]

Cited: alce::268__wikidata_intersection__dev::p12, alce::268__wikidata_intersection__dev::p29, alce::268__wikidata_intersection__dev::p48

### `518__wikitables_simple__dev`
> Here are some notable nightclub fires:

The 2001 Canecão Mineiro nightclub fire occurred in Belo Horizonte, Brazil. [alce::518__wikitables_simple__dev::p2]
> The 2003 Station nightclub fire took place in West Warwick, Rhode Island, in the United States. [alce::518__wikitables_simple__dev::p49]
> The 2004 República Cromañón nightclub fire happened in Buenos Aires, Argentina. [alce::518__wikitables_simple__dev::p49]
> The 2008 Wuwang Club fire occurred in Shenzhen, China. [alce::518__wikitables_simple__dev::p49]
> The 2009 Santika Club fire took place in Watthana, Bangkok, Thailand. [alce::518__wikitables_simple__dev::p49]
> The 2009 Lame Horse fire occurred in Perm, Russia. [alce::518__wikitables_simple__dev::p49]
> The 2013 Kiss nightclub fire started on January 27, 2013, in Santa Maria, Rio Grande do Sul, Brazil, killing 242 people and injuring at least 630 others, making it the third-deadliest nightclub fire in history. [alce::518__wikitables_simple__dev::p3]
> The 2015 Colectiv nightclub fire occurred in Bucharest, Romania. [alce::518__wikitables_simple__dev::p2]
> The Cocoanut Grove fire was a nightclub fire in Boston, Massachusetts, on November 28, 1942, killing 492 people and representing the deadliest nightclub fire in history. [alce::518__wikitables_simple__dev::p11]

Cited: alce::518__wikitables_simple__dev::p11, alce::518__wikitables_simple__dev::p2, alce::518__wikitables_simple__dev::p3, alce::518__wikitables_simple__dev::p49

### `2__wikitables_composition__dev`
> Based on the provided sources, the following villages are located in Okinawa, Japan:

Onna Village is located in the central part of Okinawa Island. [alce::2__wikitables_composition__dev::p62]
> Tarama is a village located in Okinawa Prefecture. [alce::2__wikitables_composition__dev::p8]

Cited: alce::2__wikitables_composition__dev::p62, alce::2__wikitables_composition__dev::p8

### `31__wikitables_composition__dev`
> South Sumter is a census-designated place in Sumter County, South Carolina. [alce::31__wikitables_composition__dev::p2]
> East Sumter is also a census-designated place in Sumter County, South Carolina. [alce::31__wikitables_composition__dev::p7]

Cited: alce::31__wikitables_composition__dev::p2, alce::31__wikitables_composition__dev::p7

### `808__wikidata_simple__dev`
> Several individuals served with the Singapore Armed Forces:

Chan served in the Singapore Army from 1987 to 2011, holding positions including Commanding Officer of the 2nd Battalion, Singapore Infantry Regiment, Army Attaché in Jakarta, Commander of the 10th Singapore Infantry Brigade, and Chief of Staff - Joint Staff. [alce::808__wikidata_simple__dev::p48]
> Choo enlisted in the Singapore Military Forces (renamed Singapore Armed Forces in 1961) in December 1959 and was commissioned as a Second Lieutenant in December 1961, serving as a platoon commander in the 1st Battalion Singapore Infantry Regiment and participating in operations during the Konfrontasi and in patrolling duties. [alce::808__wikidata_simple__dev::p92]
> Singh enlisted in the Singapore Armed Forces in December 1982, was commissioned as a signals officer in December 1986, served in active duty with the United Nations Iraq–Kuwait Observation Mission in Kuwait in 1991, and held various appointments including Commander of the 2nd Singapore Infantry Brigade and Commander of the 6th Division before retiring in 2009 as Chief of Staff, Joint Staff. [alce::808__wikidata_simple__dev::p61]
> Lim served in the Singapore Armed Forces and was the Chief of Army from 1992–1995, holding the rank of Major-General. [alce::808__wikidata_simple__dev::p69]

Cited: alce::808__wikidata_simple__dev::p48, alce::808__wikidata_simple__dev::p61, alce::808__wikidata_simple__dev::p69, alce::808__wikidata_simple__dev::p92

### `827__wikidata_simple__dev`
_Refused._

### `547__wikitables_simple__dev`
> Based on the provided sources, the structures with a height larger than 600 m are:

The largest structure is a single-storey, concrete building with dimensions of 680 m and 2,300 m. [alce::547__wikitables_simple__dev::p63]
> The Warszawa Radio Mast at Konstantynów, Poland was 646.38 metres (2,120.67 ft) tall at the time of its collapse in 1991. [alce::547__wikitables_simple__dev::p10]

Cited: alce::547__wikitables_simple__dev::p10, alce::547__wikitables_simple__dev::p63

### `445__wikidata_intersection__dev`
> Based on the provided sources, I can identify the following match where West Ham United F.C. was both competitor and victor:

On 13 May, West Ham played Manchester United at Old Trafford and were victorious. [alce::445__wikidata_intersection__dev::p10]
> Tevez sent West Ham 1–0 ahead at the end of the first half injury time, and West Ham secured 15th place in the Premiership. [alce::445__wikidata_intersection__dev::p10]
> Additionally, on 5 May 2007, West Ham moved out of the relegation zone with a 3–1 win over Bolton. [alce::445__wikidata_intersection__dev::p10]

Cited: alce::445__wikidata_intersection__dev::p10

### `619__wikidata_simple__dev`
> Jon Bon Jovi composed "Blaze of Glory," his debut solo studio album released in 1990. [alce::619__wikidata_simple__dev::p11]
> He also composed "Destination Anywhere," his second solo studio album released in 1997. [alce::619__wikidata_simple__dev::p37]

Cited: alce::619__wikidata_simple__dev::p11, alce::619__wikidata_simple__dev::p37

### `239__wikidata_comp__dev`
_Refused._

### `373__wikidata_comp__dev`
_Refused._

### `443__wikidata_intersection__dev`
_Refused._

### `263__wikidata_comp__dev`
_Refused._

### `1366__wikidata_simple__dev`
> Norman Reilly Raine wrote the screenplay for "The Life of Emile Zola" (1937), for which he won an Oscar. [alce::1366__wikidata_simple__dev::p2]
> He also wrote screenplays for many other films, including "The Perfect Specimen," "God's Country and the Woman," "The Adventures of Robin Hood," "Each Dawn I Die," "The Private Lives of Elizabeth and Essex," "Mountain Justice," "The Fighting 69th," "Men Are Such Fools," "Eagle Squadron," "Ladies Courageous," "We've Never Been Licked," "Nob Hill," "A Bell for Adano," "Captain Kidd," and "Captains of the Clouds." [alce::1366__wikidata_simple__dev::p0]
> Additionally, in 1933 he wrote the screenplay for the "Tugboat Annie" film, in which Marie Dressler played Annie and Wallace Beery portrayed Terry. [alce::1366__wikidata_simple__dev::p8]

Cited: alce::1366__wikidata_simple__dev::p0, alce::1366__wikidata_simple__dev::p2, alce::1366__wikidata_simple__dev::p8

### `738__wikidata_simple__dev`
> The Minnesota Timberwolves drafted several notable players:

Pooh Richardson was drafted by the Timberwolves with the tenth overall pick in the 1989 NBA draft as their first ever draft pick. [alce::738__wikidata_simple__dev::p0]
> Doug West was selected by the Minnesota Timberwolves in the second round of the 1989 NBA Draft. [alce::738__wikidata_simple__dev::p86]
> Kevin Garnett was picked fifth overall by the Timberwolves in 1995 and went on to be a 13-time All-Star. [alce::738__wikidata_simple__dev::p0]
> Ray Allen was drafted fifth overall by the Timberwolves in 1996 but was traded to the Milwaukee Bucks. [alce::738__wikidata_simple__dev::p0]
> Ricky Rubio was drafted 5th by the Minnesota Timberwolves. [alce::738__wikidata_simple__dev::p33]
> O. J. Mayo was drafted third overall by the Timberwolves in the 2008 NBA draft but was traded to the Memphis Grizzlies. [alce::738__wikidata_simple__dev::p0]
> Josh Okogie was drafted by the Minnesota Timberwolves with the 20th overall pick in the 2018 NBA draft. [alce::738__wikidata_simple__dev::p21]
> Karl-Anthony Towns was selected No. 1 overall by Minnesota in the draft. [alce::738__wikidata_simple__dev::p69]

Cited: alce::738__wikidata_simple__dev::p0, alce::738__wikidata_simple__dev::p21, alce::738__wikidata_simple__dev::p33, alce::738__wikidata_simple__dev::p69, alce::738__wikidata_simple__dev::p86

### `640__wikidata_simple__dev`
> "Ganga Maiyya Tohe Piyari Chadhaibo" is a movie whose original language was Bhojpuri. [alce::640__wikidata_simple__dev::p0]
> Another example is "Nadiya Ke Paar," which is described as one of the best-known Bhojpuri-language movies. [alce::640__wikidata_simple__dev::p5]

Cited: alce::640__wikidata_simple__dev::p0, alce::640__wikidata_simple__dev::p5

### `466__wikidata_intersection__dev`
> "Attakathi" was a film produced by C.V. Kumar and had music composed by Santhosh Narayanan. [alce::466__wikidata_intersection__dev::p70]

Cited: alce::466__wikidata_intersection__dev::p70

### `368__wikidata_comp__dev`
> Based on the provided sources, I can identify several draft picks by the Portland Trail Blazers and their citizenships:

Meyers Leonard is an American professional basketball player who was selected by the Trail Blazers with the 11th overall pick in the 2012 NBA draft. [alce::368__wikidata_comp__dev::p20]
> Maurice Harkless is an American-Puerto Rican professional basketball player who was drafted 15th overall in the 2012 NBA draft by the Trail Blazers. [alce::368__wikidata_comp__dev::p17]
> Patty Mills is an Australian professional basketball player who was selected by the Portland Trail Blazers with the 55th overall pick in the 2009 NBA draft. [alce::368__wikidata_comp__dev::p87]

Cited: alce::368__wikidata_comp__dev::p17, alce::368__wikidata_comp__dev::p20, alce::368__wikidata_comp__dev::p87

### `349__wikidata_intersection__dev`
> Arthur P. Jacobs produced "Battle for the Planet of the Apes," which was directed by J. Lee Thompson. [alce::349__wikidata_intersection__dev::p11]

Cited: alce::349__wikidata_intersection__dev::p11

### `863__wikidata_simple__dev`
> Nagoya Expressway Public Corporation owned and managed the Nagoya Expressway, a network of urban expressways in Japan serving the greater Nagoya area. [alce::863__wikidata_simple__dev::p0]

Cited: alce::863__wikidata_simple__dev::p0

### `883__wikidata_simple__dev`
> David Boaz is employed by the Cato Institute as executive vice president. [alce::883__wikidata_simple__dev::p29]
> Doug Bandow is employed by the Cato Institute as a Senior Fellow. [alce::883__wikidata_simple__dev::p84]

Cited: alce::883__wikidata_simple__dev::p29, alce::883__wikidata_simple__dev::p84

### `520__wikitables_simple__dev`
> Based on the provided sources, the following weapons are of the type rocket launchers:

The Soviet "Katyusha" was a self-propelled rocket launcher system mounted on trucks, tanks, and trains. [alce::520__wikitables_simple__dev::p0]
> The United States Army's T34 Calliope was a tank-mounted rocket launcher system deployed late in World War II. [alce::520__wikitables_simple__dev::p0]
> Shoulder-fired rocket launchers are a category that includes weapons small enough to be carried by a single person and fired while held on one's shoulder, with examples including bazookas and RPGs. [alce::520__wikitables_simple__dev::p0]
> The Type 4 20 cm rocket launcher was a 203 mm rocket mortar used by the Imperial Japanese Army in the final stages of World War II. [alce::520__wikitables_simple__dev::p56]
> The Type 4 40 cm rocket launcher was a rocket launcher used by the Imperial Japanese Army in the final stages of World War II. [alce::520__wikitables_simple__dev::p78]
> The BM-27 Uragan and M270 Multiple Launch Rocket System are examples of modern surface-to-surface rocket launcher systems. [alce::520__wikitables_simple__dev::p23]

Cited: alce::520__wikitables_simple__dev::p0, alce::520__wikitables_simple__dev::p23, alce::520__wikitables_simple__dev::p56, alce::520__wikitables_simple__dev::p78

### `833__wikidata_simple__dev`
> Based on the provided sources, I can identify a game released by Atari Corporation:

"Breakout" is a paddle and ball video game that was created by Atari Games Corporation and released in 1976. [alce::833__wikidata_simple__dev::p65]
> However, I should note that the sources distinguish between Atari Corporation (founded in 1984 by Jack Tramiel) and Atari Games Corporation (the arcade division). The sources do not explicitly list specific games released by Atari Corporation itself during its 1984-1996 operating period, though they mention its chief products were the Atari ST, Atari 7800, Atari Lynx, and Atari Jaguar, which were consoles and computers rather than individual games. [alce::833__wikidata_simple__dev::p6]

Cited: alce::833__wikidata_simple__dev::p6, alce::833__wikidata_simple__dev::p65

### `454__wikidata_intersection__dev`
> Manchester City F.C. and Newcastle United F.C. both participated in the Premier League. [alce::454__wikidata_intersection__dev::p78]
> Additionally, both clubs have participated in European competitions. Manchester City has competed in UEFA competitions including the European Cup (now the Champions League) on eight occasions. [alce::454__wikidata_intersection__dev::p0]
> Newcastle United first played European football in the 1968–69 Inter-Cities Fairs Cup and their first Champions League appearance came in 1997–98. [alce::454__wikidata_intersection__dev::p2]

Cited: alce::454__wikidata_intersection__dev::p0, alce::454__wikidata_intersection__dev::p2, alce::454__wikidata_intersection__dev::p78

### `847__wikidata_simple__dev`
_Refused._

### `160__wikidata_comp__dev`
_Refused._

### `525__wikitables_simple__dev`
> Here are the names of motorcycle-related clubs mentioned in the sources:

The Harley Owners Group is a major brand club. [alce::525__wikitables_simple__dev::p0]
> The BMW Motorcycle Owners of America is a large national independent motorcycle club. [alce::525__wikitables_simple__dev::p0]
> The Women's International Motorcycle Association caters to women riders. [alce::525__wikitables_simple__dev::p0]
> Dykes on Bikes is a club for lesbians and gays. [alce::525__wikitables_simple__dev::p0]
> The Vintage Motor Cycle Club caters to those interested in vintage machines. [alce::525__wikitables_simple__dev::p0]
> The Motorcycle Action Group focuses on riders' rights. [alce::525__wikitables_simple__dev::p0]
> The Royal British Legion Riders Branch is a charity for motorcycle riders. [alce::525__wikitables_simple__dev::p0]
> The American Motorcyclist Association is a social motorcycle organization. [alce::525__wikitables_simple__dev::p2]
> Bikers Against Child Abuse exists primarily as a social benefit organization. [alce::525__wikitables_simple__dev::p2]
> The Christian Motorcyclists Association is a religiously-oriented club and biker ministry. [alce::525__wikitables_simple__dev::p3]
> Freewheelers EVS is a charity that uses motorcycles for emergency medical courier service. [alce::525__wikitables_simple__dev::p3]
> The Blue Knights Law Enforcement Motorcycle Club attracts law enforcement personnel. [alce::525__wikitables_simple__dev::p3]
> The Patriot Guard Riders provide funeral escorts for military veterans. [alce::525__wikitables_simple__dev::p6]
> Rolling Thunder advocates for troops missing in action and prisoners of war. [alce::525__wikitables_simple__dev::p6]

Cited: alce::525__wikitables_simple__dev::p0, alce::525__wikitables_simple__dev::p2, alce::525__wikitables_simple__dev::p3, alce::525__wikitables_simple__dev::p6

### `521__wikitables_simple__dev`
> An archivist is an information professional who assesses, collects, organizes, preserves, maintains control over, and provides access to records and archives determined to have long-term value. [alce::521__wikitables_simple__dev::p0]
> The records maintained by an archivist can consist of a variety of forms, including letters, diaries, logs, other personal documents, government documents, sound and/or picture recordings, digital files, or other physical objects. [alce::521__wikitables_simple__dev::p0]
> Additionally, R.D.W. Connor was the first Archivist of the United States, beginning to serve in 1934 when the National Archives was established as an independent federal agency by Congress. [alce::521__wikitables_simple__dev::p3]
> Matthias Lane, a character in Martha Cooley's novel "The Archivist," also worked as an archivist at an unnamed library. [alce::521__wikitables_simple__dev::p4]

Cited: alce::521__wikitables_simple__dev::p0, alce::521__wikitables_simple__dev::p3, alce::521__wikitables_simple__dev::p4

### `909__wikidata_simple__dev`
> The Pittsburgh Pirates won the World Series in 1960, 1971, and 1979.

The Pirates defeated the New York Yankees in the 1960 World Series (4–3). [alce::909__wikidata_simple__dev::p49]
> The Pirates defeated the Baltimore Orioles in the 1971 World Series (4–3). [alce::909__wikidata_simple__dev::p18]
> The Pirates defeated the Baltimore Orioles in the 1979 World Series (4–3). [alce::909__wikidata_simple__dev::p3]

Cited: alce::909__wikidata_simple__dev::p18, alce::909__wikidata_simple__dev::p3, alce::909__wikidata_simple__dev::p49

### `1102__wikidata_intersection__dev`
_Refused._

### `783__wikidata_simple__dev`
> Cinergi Pictures produced several notable films. [alce::783__wikidata_simple__dev::p0]
> The company's major hit films included "Tombstone", "Die Hard with a Vengeance" and "Evita". [alce::783__wikidata_simple__dev::p8]
> Other films produced by Cinergi include "Medicine Man", "Renaissance Man", "Color of Night", "Judge Dredd", "The Scarlet Letter", and "Nixon". [alce::783__wikidata_simple__dev::p0]

Cited: alce::783__wikidata_simple__dev::p0, alce::783__wikidata_simple__dev::p8

### `850__wikidata_simple__dev`
> Based on the provided sources, several businesses have Myanmar as their headquarters:

The Myanmar Economic Corporation has its headquarters located on Ahlon Road in Yangon's Ahlon Township. [alce::850__wikidata_simple__dev::p17]
> Myanmar Airways International is a privately owned airline headquartered in Yangon, Myanmar. [alce::850__wikidata_simple__dev::p22]
> The Ministry of Commerce has its headquarters located at Building 3 and 52, Nay Pyi Taw, in Myanmar. [alce::850__wikidata_simple__dev::p18]

Cited: alce::850__wikidata_simple__dev::p17, alce::850__wikidata_simple__dev::p18, alce::850__wikidata_simple__dev::p22

### `1001__wikidata_comp__dev`
> A.C. Milan was a finalist in the 2007 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p3]
> Liverpool F.C. was a finalist in the 2007 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p3]
> Barcelona was a finalist in the 2006 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p41]
> Arsenal was a finalist in the 2006 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p41]

Cited: alce::1001__wikidata_comp__dev::p3, alce::1001__wikidata_comp__dev::p41

### `956__wikidata_comp__dev`
_Refused._

### `975__wikidata_comp__dev`
_Refused._

### `596__wikidata_simple__dev`
_Refused._

### `436__wikidata_intersection__dev`
> Christopher Nolan wrote and produced several movies. "The Prestige" (2006) is one example, as Nolan directed, co-wrote, and produced this film. [alce::436__wikidata_intersection__dev::p0]
> Additionally, Nolan wrote and produced "Interstellar" (2014), a science-fiction film that he also directed. [alce::436__wikidata_intersection__dev::p6]
> He also produced "Man of Steel" (2013), though David S. Goyer wrote that film rather than Nolan. [alce::436__wikidata_intersection__dev::p31]

Cited: alce::436__wikidata_intersection__dev::p0, alce::436__wikidata_intersection__dev::p31, alce::436__wikidata_intersection__dev::p6

### `57__wikitables_composition__dev`
_Refused._

### `389__wikidata_comp__dev`
_Refused._

### `186__wikidata_intersection__dev`
> Manchester City competed in the European Cup Winners' Cup and won it. [alce::186__wikidata_intersection__dev::p2]
> Specifically, Manchester City won the 1969–70 Cup Winners' Cup. [alce::186__wikidata_intersection__dev::p2]

Cited: alce::186__wikidata_intersection__dev::p2

### `745__wikidata_simple__dev`
> Based on the provided sources, Scots is the mother tongue of over 300 residents of Nova Scotia and Prince Edward Island. [alce::745__wikidata_simple__dev::p71]

Cited: alce::745__wikidata_simple__dev::p71

### `822__wikidata_simple__dev`
_Refused._

### `485__wikitables_simple__dev`
> Based on the provided sources, several individuals were psychiatrists:

Roy Thinnes played the title role of Dr. James Whitman, a young psychiatrist with unorthodox methods of helping his patients. [alce::485__wikitables_simple__dev::p1]
> Luther Adler co-starred as Dr. Bernard Altman, an older psychiatrist. [alce::485__wikitables_simple__dev::p1]
> Adolf Meyer was a psychiatrist who rose to prominence as the first psychiatrist-in-chief of the Johns Hopkins Hospital (1910-1941). [alce::485__wikitables_simple__dev::p43]

Cited: alce::485__wikitables_simple__dev::p1, alce::485__wikitables_simple__dev::p43

### `401__wikidata_comp__dev`
> Charles E. Barber designed coins. [alce::401__wikidata_comp__dev::p0]
> The objects he designed depicted the United States, as evidenced by his role as Chief Engraver of the United States Mint and his design of coins such as the Barber dime, quarter, and half-dollar. [alce::401__wikidata_comp__dev::p13]

Cited: alce::401__wikidata_comp__dev::p0, alce::401__wikidata_comp__dev::p13

### `717__wikidata_simple__dev`
> Goffredo Petrassi had many famous students, including Franco Donatoni, Aldo Clementi, Cornelius Cardew, Ennio Morricone, Karl Korte, Boris Porena, Norma Beecroft, Mario Bertoncini, Ernesto Rubin de Cervin, Eric Salzman, Kenneth Leighton, Peter Maxwell Davies, Michael Dellaira, Armando Santiago, and Richard Teitelbaum. [alce::717__wikidata_simple__dev::p1]

Cited: alce::717__wikidata_simple__dev::p1

### `141__wikidata_intersection__dev`
> The Pittsburgh Steelers competed in multiple Super Bowls. They won Super Bowl XL and Super Bowl XLIII. [alce::141__wikidata_intersection__dev::p8]
> In Super Bowl XLIII, played on February 1, 2009, the Steelers defeated the Arizona Cardinals 27–23. [alce::141__wikidata_intersection__dev::p7]
> The Steelers also lost Super Bowl XLV. [alce::141__wikidata_intersection__dev::p8]
> Additionally, the Steelers played against the Dallas Cowboys in a Super Bowl in Miami, winning 21–17. [alce::141__wikidata_intersection__dev::p28]
> Overall, the Steelers have won 6 Super Bowl titles. [alce::141__wikidata_intersection__dev::p40]

Cited: alce::141__wikidata_intersection__dev::p28, alce::141__wikidata_intersection__dev::p40, alce::141__wikidata_intersection__dev::p7, alce::141__wikidata_intersection__dev::p8

### `590__wikidata_simple__dev`
> Based on the provided sources, the following buildings were built in saltbox style:

The Prentis House was built in 1773 in Hadley, Massachusetts and is typical of the indigenous saltbox architecture style that developed in New England during the Colonial period. [alce::590__wikidata_simple__dev::p9]
> The Josiah Day House in West Springfield, Massachusetts is constructed in saltbox style. [alce::590__wikidata_simple__dev::p5]
> The Salt Box was a house built in the 1880s in the Bunker Hill section of Los Angeles, California, designed in the saltbox style. [alce::590__wikidata_simple__dev::p0]
> The Montgomery Saltbox Houses are a pair of historic saltbox houses in Montgomery, Ohio, United States, built in 1800. [alce::590__wikidata_simple__dev::p3]

Cited: alce::590__wikidata_simple__dev::p0, alce::590__wikidata_simple__dev::p3, alce::590__wikidata_simple__dev::p5, alce::590__wikidata_simple__dev::p9

### `953__wikidata_comp__dev`
_Refused._

### `918__wikidata_simple__dev`
_Refused._

### `694__wikidata_simple__dev`
> Several individuals worked for the Western Roman Empire based on the provided sources:

Olympius was a minister of the Western Roman Empire in the court of emperor Honorius. [alce::694__wikidata_simple__dev::p84]
> Stilicho was a military strongman who effectively ruled the Western Roman Empire as regent from 395 to 408. [alce::694__wikidata_simple__dev::p17]
> Constantius, Aëtius, and Ricimer were military strongmen who held the titles of "magister militum," "patrician," or both and ruled the Western Roman Empire during the periods of about 411 to 421, 433 to 454, and about 457 to 472, respectively. [alce::694__wikidata_simple__dev::p17]
> Julius Nepos was appointed Western Emperor in 473 CE and ruled the Province from 468 CE. [alce::694__wikidata_simple__dev::p16]
> Orestes was a Germanic "Magister militum" who deposed Julius Nepos. [alce::694__wikidata_simple__dev::p16]
> Theoderic acted as a subordinate ruler and had the army and military offices staffed by Goths under his authority. [alce::694__wikidata_simple__dev::p30]

Cited: alce::694__wikidata_simple__dev::p16, alce::694__wikidata_simple__dev::p17, alce::694__wikidata_simple__dev::p30, alce::694__wikidata_simple__dev::p84

### `601__wikidata_simple__dev`
> Based on the provided sources, the following vessels were home-ported at Halifax:

HMCS Halifax (FFH 330) is homeported at CFB Halifax in Halifax, Nova Scotia. [alce::601__wikidata_simple__dev::p7]
> HMCS Goose Bay is homeported at CFB Halifax. [alce::601__wikidata_simple__dev::p60]
> HMCS Glace Bay is homeported at CFB Halifax. [alce::601__wikidata_simple__dev::p79]
> Additionally, approximately 2/3 of the navy's major ships are home ported in Halifax overall. [alce::601__wikidata_simple__dev::p3]

Cited: alce::601__wikidata_simple__dev::p3, alce::601__wikidata_simple__dev::p60, alce::601__wikidata_simple__dev::p7, alce::601__wikidata_simple__dev::p79

### `691__wikidata_simple__dev`
> One product of the company Sukhoi is the Su-57, a stealth, single-seat, twin-engine multirole fifth-generation jet fighter. [alce::691__wikidata_simple__dev::p59]
> Another product is the Superjet 100, which is the company's most important civilian project. [alce::691__wikidata_simple__dev::p5]

Cited: alce::691__wikidata_simple__dev::p5, alce::691__wikidata_simple__dev::p59

### `860__wikidata_simple__dev`
> Cyrus Chothia supervised 19 successful PhD students to completion. [alce::860__wikidata_simple__dev::p2]
> These students included Alex Bateman, Steven E. Brenner, Mark Bender Gerstein, Julian Gough, Sarah Teichmann, Bissan Al-Lazikani, Goga Apic, Samantha Barré Matthew Bashton, Dan Bolser, Michael Bremang, Bernard de Bono, Emma Ganley (née Hill), Martin Madera, Siarhei Maslau, Susan Miller, Jong Park (aka Jong Bhak), Rajkumar Sasidharan, and Christine Vogel. [alce::860__wikidata_simple__dev::p2]

Cited: alce::860__wikidata_simple__dev::p2

### `490__wikitables_simple__dev`
> # Sex Worker Organizations: Names and Abbreviations

In the United States, COYOTE (Call Off Your Old Tired Ethics) is an American advocacy group for prostitutes founded in 1973 in San Francisco, California. [alce::490__wikitables_simple__dev::p12]
> Another U.S. organization is the North American Task Force on Prostitution. [alce::490__wikitables_simple__dev::p13]
> In Australia, Scarlet Alliance is the lead sex worker rights organisation and peak body for sex worker organizations. [alce::490__wikitables_simple__dev::p3]
> The Prostitutes Collective of Victoria (PCV) was founded in Melbourne, Victoria, and was the first sex workers' organization in the world to receive government funding. [alce::490__wikitables_simple__dev::p10]
> In Ireland, the Sex Workers Alliance Ireland (SWAI) was established in 2009. [alce::490__wikitables_simple__dev::p3]
> In the San Francisco Bay Area, BAYSWAN is a non-profit organization for sex workers. [alce::490__wikitables_simple__dev::p3]
> Internationally, the International Committee for Prostitutes' Rights and the Network of Sex Workers are prostitutes' rights organizations. [alce::490__wikitables_simple__dev::p13]
> The International Union of Sex Workers (IUSW), headquartered in the United Kingdom, is one of the largest sex worker unions worldwide. [alce::490__wikitables_simple__dev::p12]
> In Asia, the Asia Pacific Network of Sex Workers (APNSW) is a regional organization headquartered in Thailand. [alce::490__wikitables_simple__dev::p26]
> SISTERS works with transgender sex workers in Bangkok and Pattaya, and M Plus is an organization for male sex workers in Chiang Mai. [alce::490__wikitables_simple__dev::p26]

Cited: alce::490__wikitables_simple__dev::p10, alce::490__wikitables_simple__dev::p12, alce::490__wikitables_simple__dev::p13, alce::490__wikitables_simple__dev::p26, alce::490__wikitables_simple__dev::p3

### `250__wikidata_comp__dev`
_Refused._

### `776__wikidata_simple__dev`
> Howard Steven Friedman is an individual employed in the field of statistics. [alce::776__wikidata_simple__dev::p40]
> He is a prominent American statistician currently employed at the United Nations Population Fund (UNFPA) and as an adjunct Associate Professor at Columbia University. [alce::776__wikidata_simple__dev::p40]

Cited: alce::776__wikidata_simple__dev::p40

### `316__wikidata_comp__dev`
> Geoff Barrow worked as a composer on movies that Alex Garland wrote for the screen. [alce::316__wikidata_comp__dev::p2]
> Together with Geoff Barrow, he scored the feature film "Ex Machina", Alex Garland's directorial debut, released in the UK in January 2015. [alce::316__wikidata_comp__dev::p2]
> The two teamed up again to score Garland's "Annihilation" (2018). [alce::316__wikidata_comp__dev::p2]

Cited: alce::316__wikidata_comp__dev::p2

### `608__wikidata_simple__dev`
> Based on the provided sources, the following paintings have Victorine Meurent in them:

"The Luncheon on the Grass" (also called "Le déjeuner sur l'herbe") is a painting by Manet that includes a nude portrayal of Meurent. [alce::608__wikidata_simple__dev::p3]
> "Olympia" is a Manet masterpiece from 1863 that includes a nude portrayal of Meurent. [alce::608__wikidata_simple__dev::p3]
> "Gare Saint-Lazare" is the last Manet painting in which Meurent appears. [alce::608__wikidata_simple__dev::p3]

Cited: alce::608__wikidata_simple__dev::p3

### `733__wikidata_simple__dev`
> Benny Chan directed several films. "New Police Story" is a 2004 Hong Kong action film produced and directed by Benny Chan. [alce::733__wikidata_simple__dev::p19]
> "Who Am I?" is a 1998 Hong Kong action comedy film directed by Benny Chan and Jackie Chan. [alce::733__wikidata_simple__dev::p83]

Cited: alce::733__wikidata_simple__dev::p19, alce::733__wikidata_simple__dev::p83

### `970__wikidata_comp__dev`
> Ian Chubb, who was the Chief Scientist of Australia from 23 May 2011 to 22 January 2016, has a Masters in Science and a DPhil from the University of Oxford. [alce::970__wikidata_comp__dev::p24]

Cited: alce::970__wikidata_comp__dev::p24

### `163__wikidata_intersection__dev`
> "Pattanapravesham" is a 1988 Malayalam film written by Sreenivasan and directed by Sathyan Anthikad. [alce::163__wikidata_intersection__dev::p56]

Cited: alce::163__wikidata_intersection__dev::p56

### `415__wikidata_comp__dev`
_Refused._

### `442__wikidata_intersection__dev`
> S.L. Benfica and Sporting CP were participating in the Taça de Portugal. [alce::442__wikidata_intersection__dev::p1]
> In this competition, they faced each other in the sixth round, where Benfica defeated Sporting CP 7–6 on penalties after a 3–3 draw. [alce::442__wikidata_intersection__dev::p1]

Cited: alce::442__wikidata_intersection__dev::p1

### `710__wikidata_simple__dev`
> Lewis Trondheim did illustrations for the comic "The Nimrod". [alce::710__wikidata_simple__dev::p0]

Cited: alce::710__wikidata_simple__dev::p0

### `765__wikidata_simple__dev`
> Isaac Asimov edited about 147 books during his writing career spanning 53 years (1939–1992). [alce::765__wikidata_simple__dev::p16]

Cited: alce::765__wikidata_simple__dev::p16

### `361__wikidata_intersection__dev`
_Refused._

### `536__wikitables_simple__dev`
> Captain Sir John Franklin led a lost expedition. [alce::536__wikitables_simple__dev::p5]
> This was a British voyage of Arctic exploration that departed England in 1845 aboard two ships. [alce::536__wikitables_simple__dev::p5]
> The expedition was meant to traverse the last unnavigated section of the Northwest Passage. [alce::536__wikitables_simple__dev::p5]
> The entire expedition comprised 129 men including Franklin, and all perished when the two ships became icebound in Victoria Strait near King William Island in the Canadian Arctic. [alce::536__wikitables_simple__dev::p5]

Cited: alce::536__wikitables_simple__dev::p5

### `138__wikidata_intersection__dev`
> Wonder Woman is a fictional character who is an Amazon from Themyscira. [alce::138__wikidata_intersection__dev::p13]

Cited: alce::138__wikidata_intersection__dev::p13

### `641__wikidata_simple__dev`
_Refused._

### `219__wikidata_comp__dev`
> William Pine directed a film produced by Pine-Thomas Productions. [alce::219__wikidata_comp__dev::p7]
> Specifically, William Pine directed "Aerial Gunner," which was produced by the Paramount Pictures Pine-Thomas Productions unit, and it was his first feature film. [alce::219__wikidata_comp__dev::p7]

Cited: alce::219__wikidata_comp__dev::p7

### `556__wikidata_simple__dev`
> Anthony Kimmins directed multiple films. His first directorial assignment was "Keep Fit" [alce::556__wikidata_simple__dev::p0]
> . He also directed many of George Formby's comedies [alce::556__wikidata_simple__dev::p2]
> , as well as films including "Mine Own Executioner" (1947) [alce::556__wikidata_simple__dev::p2]
> , "Bonnie Prince Charlie" (1948) [alce::556__wikidata_simple__dev::p2]
> , "Mr. Denning Drives North" (1951) [alce::556__wikidata_simple__dev::p2]
> , "The Captain's Paradise" [alce::556__wikidata_simple__dev::p2]
> , the "Smiley" series [alce::556__wikidata_simple__dev::p2]
> , and "The Amorous Prawn" (1962) [alce::556__wikidata_simple__dev::p2]
> .

Cited: alce::556__wikidata_simple__dev::p0, alce::556__wikidata_simple__dev::p2

### `126__wikidata_intersection__dev`
> Lewis Hamilton won the 2007 Canadian Grand Prix. [alce::126__wikidata_intersection__dev::p0]
> He also won the 2010 Canadian Grand Prix, which was his second Canadian Grand Prix victory. [alce::126__wikidata_intersection__dev::p4]

Cited: alce::126__wikidata_intersection__dev::p0, alce::126__wikidata_intersection__dev::p4

### `155__wikidata_comp__dev`
_Refused._

### `686__wikidata_simple__dev`
> Canada participated in the 2017 World Championships in Athletics. [alce::686__wikidata_simple__dev::p2]
> Great Britain and Northern Ireland participated in the 2017 World Championships in Athletics. [alce::686__wikidata_simple__dev::p18]
> The United States participated in the 2017 World Championships in Athletics. [alce::686__wikidata_simple__dev::p5]

Cited: alce::686__wikidata_simple__dev::p18, alce::686__wikidata_simple__dev::p2, alce::686__wikidata_simple__dev::p5

### `886__wikidata_simple__dev`
> The Chicago Cubs compete in Major League Baseball (MLB) as a member club of the National League (NL) Central division. [alce::886__wikidata_simple__dev::p0]
> The Cubs play home games at Wrigley Field. [alce::886__wikidata_simple__dev::p0]
> The Cubs have competed against the Los Angeles Dodgers in the NLCS in 7 games. [alce::886__wikidata_simple__dev::p66]
> The Cubs participate in a rivalry with the Milwaukee Brewers, including spring training Cactus League games. [alce::886__wikidata_simple__dev::p66]

Cited: alce::886__wikidata_simple__dev::p0, alce::886__wikidata_simple__dev::p66

### `472__wikitables_simple__dev`
> Based on the provided sources, the following weapons are anti-materiel rifles:

The Barrett M107 is an anti-materiel rifle that fires a .50 BMG caliber bullet and weighs 28.7 pounds. [alce::472__wikitables_simple__dev::p4]
> Other popular anti-materiel rifles include the Zastava M93 Black arrow, McMillan Tac-50, Gepard GM6 Lynx, AMSD OM 50 Nemesis, Accuracy International AS50, Mechem NTW-20, and Istiglal. [alce::472__wikitables_simple__dev::p4]
> The Gepárd anti-materiel rifles are a family of Hungarian weapons designed to destroy unarmored and lightly armored targets. [alce::472__wikitables_simple__dev::p9]
> The IST-14.5, WKW Wilk, and CheyTac Intervention M-200 are also anti-materiel rifles. [alce::472__wikitables_simple__dev::p1]
> The NTW-20 is a South African anti-materiel rifle developed by Denel Mechem in the 1990s. [alce::472__wikitables_simple__dev::p40]

Cited: alce::472__wikitables_simple__dev::p1, alce::472__wikitables_simple__dev::p4, alce::472__wikitables_simple__dev::p40, alce::472__wikitables_simple__dev::p9

### `106__wikidata_intersection__dev`
> Based on the provided sources, multiple competitions featured both Manchester City and Arsenal as participants:

The Premier League Asia Trophy featured both Manchester City and Arsenal as participants. [alce::106__wikidata_intersection__dev::p69]
> The Emirates Cup also featured both clubs, with Arsenal as the host for the eighth edition in 2015. [alce::106__wikidata_intersection__dev::p25]
> Additionally, Manchester City and Arsenal have contested league competition against each other on 170 occasions. [alce::106__wikidata_intersection__dev::p92]

Cited: alce::106__wikidata_intersection__dev::p25, alce::106__wikidata_intersection__dev::p69, alce::106__wikidata_intersection__dev::p92

### `299__wikidata_intersection__dev`
> The 1971 European Cup Winners' Cup Final featured Chelsea F.C. as participant and winner. [alce::299__wikidata_intersection__dev::p85]
> In this match, Chelsea defeated Real Madrid of Spain, with Chelsea scoring two goals through Peter Osgood and John Dempsey in the first half, while Real Madrid scored one goal, resulting in a final score of 2–1. [alce::299__wikidata_intersection__dev::p85]

Cited: alce::299__wikidata_intersection__dev::p85

### `175__wikidata_intersection__dev`
> Based on the provided sources, SL Benfica and SC Braga participated in a match on 19 November. [alce::175__wikidata_intersection__dev::p84]
> Benfica scored first through Anderson, but Braga came back with goals from Césinha and Julio Bevacqua, with Bevacqua scoring the winning goal in the 95th minute. [alce::175__wikidata_intersection__dev::p84]
> Additionally, Benfica hosted Braga on 25 March, with Benfica winning 1–0 through a Nuno Gomes goal. [alce::175__wikidata_intersection__dev::p8]
> However, the sources do not specify the name of the competition or tournament for these matches.

Cited: alce::175__wikidata_intersection__dev::p8, alce::175__wikidata_intersection__dev::p84

### `152__wikidata_intersection__dev`
> Based on the provided sources, the work that featured direction by Adurthi Subba Rao and was produced by D. Madhusudhana Rao is not explicitly named in the sources. However, source [alce::152__wikidata_intersection__dev::p15]
> describes a film produced by Madhusudhana Rao under his banner Annapurna Pictures and directed by Adurthi Subba Rao, but the title of this specific film is not stated in that sentence.
> The source only mentions that "The film was also made in Telugu with the title 'Thodi Kodallu'" and references a story based on Sharat Chandra Chatterjee's novel "Nishkruti," but does not provide the name of the original film being discussed.
> I cannot definitively answer which specific work this is from the provided sources, as the title is not explicitly given in the relevant passage.

Cited: alce::152__wikidata_intersection__dev::p15

### `0__wikitables_composition__dev`
> Several museums are located in Victoria, British Columbia:

The Royal British Columbia Museum (also referred to as Royal BC Museum) is located in Victoria, British Columbia, Canada. [alce::0__wikitables_composition__dev::p2]
> The McNamara House, a social history museum, is located in Victoria. [alce::0__wikitables_composition__dev::p8]
> The Nave, an art museum, is located in Victoria. [alce::0__wikitables_composition__dev::p8]
> The Children's Discovery Museum is located in Victoria. [alce::0__wikitables_composition__dev::p8]
> The Museum of the Coastal Bend (MCB) is located in Victoria. [alce::0__wikitables_composition__dev::p8]
> The Victoria Art Gallery is located in Victoria, BC. [alce::0__wikitables_composition__dev::p73]
> Notable museums just outside of Victoria include the Maritime Museum of British Columbia and the British Columbia Aviation Museum on the north edge of the Victoria International Airport. [alce::0__wikitables_composition__dev::p1]

Cited: alce::0__wikitables_composition__dev::p1, alce::0__wikitables_composition__dev::p2, alce::0__wikitables_composition__dev::p73, alce::0__wikitables_composition__dev::p8

### `884__wikidata_simple__dev`
> Blessy was a screenwriter for several films. He scripted and directed his debut movie "Kaazhcha" in 2004. [alce::884__wikidata_simple__dev::p1]
> He also wrote the screenplay for "Pranayam," his 2011 film. [alce::884__wikidata_simple__dev::p0]

Cited: alce::884__wikidata_simple__dev::p0, alce::884__wikidata_simple__dev::p1

### `908__wikidata_simple__dev`
> Shrabani Deodhar directed the 1993 feature film "Lapandav". [alce::908__wikidata_simple__dev::p0]
> She also directed a film called "Stat Lota". [alce::908__wikidata_simple__dev::p1]

Cited: alce::908__wikidata_simple__dev::p0, alce::908__wikidata_simple__dev::p1

### `64__wikitables_composition__dev`
> Peter Lilley is a Conservative British politician who called for cannabis to be legalised in 2001 in a Social Market Foundation pamphlet. [alce::64__wikitables_composition__dev::p2]
> However, the sources do not indicate that Lilley acknowledged personal cannabis use—only that he advocated for cannabis legalization as a policy position.

Cited: alce::64__wikitables_composition__dev::p2

### `624__wikidata_simple__dev`
> Based on the provided sources, Eitan Ezra and Harrison Hurt are alumni of Poly Prep Country Day School. [alce::624__wikidata_simple__dev::p42]

Cited: alce::624__wikidata_simple__dev::p42

### `708__wikidata_simple__dev`
> Nordwind Airlines has its head office within Sheremetyevo International Airport. [alce::708__wikidata_simple__dev::p10]

Cited: alce::708__wikidata_simple__dev::p10

### `143__wikidata_comp__dev`
_Refused._

### `474__wikitables_simple__dev`
_Refused._

### `870__wikidata_simple__dev`
> Orson Welles was responsible for production of the Mercury Theatre offerings. [alce::870__wikidata_simple__dev::p30]
> He also produced, directed, and starred in the 1951 stage production of "Othello." [alce::870__wikidata_simple__dev::p4]
> Additionally, Welles was responsible for the film "It's All True," which was an ill-fated film project. [alce::870__wikidata_simple__dev::p69]

Cited: alce::870__wikidata_simple__dev::p30, alce::870__wikidata_simple__dev::p4, alce::870__wikidata_simple__dev::p69

### `45__wikitables_composition__dev`
_Refused._

### `298__wikidata_comp__dev`
_Refused._

### `197__wikidata_intersection__dev`
> Several movies were written and directed by Paul Schrader:

"First Reformed" is a 2017 American drama film written and directed by Paul Schrader. [alce::197__wikidata_intersection__dev::p32]
> "The Walker" is a 2007 American-British drama film written and directed by Paul Schrader. [alce::197__wikidata_intersection__dev::p35]
> Additionally, "Hardcore" is a crime drama that was also written by Schrader and directed by him. [alce::197__wikidata_intersection__dev::p0]

Cited: alce::197__wikidata_intersection__dev::p0, alce::197__wikidata_intersection__dev::p32, alce::197__wikidata_intersection__dev::p35

### `417__wikidata_comp__dev`
> Terrel Bell, a US Secretary of Education, graduated from Lava Hot Springs High School and the Albion State Normal School in 1946. [alce::417__wikidata_comp__dev::p19]
> Paul Parks attended Crispus Attucks High School in Indianapolis and was accepted to Purdue University. [alce::417__wikidata_comp__dev::p17]
> However, Parks was a state Secretary of Education for Massachusetts, not a US Secretary of Education.

Cited: alce::417__wikidata_comp__dev::p17, alce::417__wikidata_comp__dev::p19

### `603__wikidata_simple__dev`
> The cut and cover technique was used to create shallow tunnels. [alce::603__wikidata_simple__dev::p2]
> Specifically, railway tunnels were built using this method, such as those on the Circle, District, Hammersmith & City, and Metropolitan lines in the sub-surface network. [alce::603__wikidata_simple__dev::p3]

Cited: alce::603__wikidata_simple__dev::p2, alce::603__wikidata_simple__dev::p3

### `306__wikidata_intersection__dev`
> The Victorian Football League (VFL) included both Collingwood Football Club and Richmond Football Club as teams in the tournament. [alce::306__wikidata_intersection__dev::p1]
> In 1897, Collingwood joined the VFL along with fellow clubs, and Richmond became the 10th team to join the league two weeks after its founding clubs voted to include University as the ninth team. [alce::306__wikidata_intersection__dev::p22]

Cited: alce::306__wikidata_intersection__dev::p1, alce::306__wikidata_intersection__dev::p22

### `35__wikitables_composition__dev`
> The question "What is the locality of George Town?" is ambiguous because there are multiple places named George Town in the provided sources. Here are the localities for each:

George Town, Tasmania is located in north-east Tasmania, on the eastern bank of the mouth of the Tamar River. [alce::35__wikitables_composition__dev::p4]
> George Town, Chennai is a neighbourhood in Chennai city (formerly Madras), Tamil Nadu, India. [alce::35__wikitables_composition__dev::p2]
> George Town, Bahamas is located on Exuma island. [alce::35__wikitables_composition__dev::p69]
> If you are asking about a specific George Town, please clarify which one you mean.

Cited: alce::35__wikitables_composition__dev::p2, alce::35__wikitables_composition__dev::p4, alce::35__wikitables_composition__dev::p69

### `1367__wikidata_simple__dev`
> Thomas Cocheé had a job in the Los Angeles County Sheriff's Department as a deputy sheriff. [alce::1367__wikidata_simple__dev::p98]

Cited: alce::1367__wikidata_simple__dev::p98

### `225__wikidata_comp__dev`
> Andrew Overtoom was the screenwriter for "My Life with Morrissey," a feature film that he directed. [alce::225__wikidata_comp__dev::p0]

Cited: alce::225__wikidata_comp__dev::p0

### `682__wikidata_simple__dev`
> One film that Ayngaran International produced was "Karuppu Roja" (1996). [alce::682__wikidata_simple__dev::p0]

Cited: alce::682__wikidata_simple__dev::p0

### `267__wikidata_comp__dev`
_Refused._

### `876__wikidata_simple__dev`
> Nexstar Media Group owns 171 television stations across the United States. [alce::876__wikidata_simple__dev::p0]
> It also operates all of the stations owned by Mission Broadcasting, an affiliated company, under local marketing agreements. [alce::876__wikidata_simple__dev::p0]

Cited: alce::876__wikidata_simple__dev::p0

### `444__wikidata_intersection__dev`
> Based on the provided sources, Venkat Prabhu directed "Kattradhu Thamizh," which had music composed by Yuvan Shankar Raja. [alce::444__wikidata_intersection__dev::p3]

Cited: alce::444__wikidata_intersection__dev::p3

### `728__wikidata_simple__dev`
> Based on the provided sources, Los Angeles maintains the segment of a roadway that was formerly designated as part of California State Route 170. [alce::728__wikidata_simple__dev::p7]
> Specifically, the segment from the US 101 Freeway south to Santa Monica Boulevard is now maintained by the City of Los Angeles after California's legislature relinquished state control of that portion. [alce::728__wikidata_simple__dev::p7]

Cited: alce::728__wikidata_simple__dev::p7

### `432__wikidata_intersection__dev`
> "Hard Times" was written for the screen and directed by Jack Hill. [alce::432__wikidata_intersection__dev::p22]

Cited: alce::432__wikidata_intersection__dev::p22

### `570__wikidata_simple__dev`
> The Woodland Trust maintains ownership of over 1,000 sites covering over 22,500 hectares. [alce::570__wikidata_simple__dev::p0]

Cited: alce::570__wikidata_simple__dev::p0

### `259__wikidata_intersection__dev`
> "Where Danger Lives" (1950) was produced by Irwin Allen and had Charles Bennett as screenwriter. [alce::259__wikidata_intersection__dev::p1]

Cited: alce::259__wikidata_intersection__dev::p1

### `974__wikidata_comp__dev`
> Don Boyd directed a project that was produced by Don Boyd himself. Boyd produced and co-directed the film documentary "Jimi Hendrix" (1973). [alce::974__wikidata_comp__dev::p77]
> Additionally, Don Boyd directed "Intimate Reflections," a 1975 British independent drama film that was his first feature film. [alce::974__wikidata_comp__dev::p18]

Cited: alce::974__wikidata_comp__dev::p18, alce::974__wikidata_comp__dev::p77

### `435__wikidata_intersection__dev`
> Based on the provided sources, the competitions that featured both Burnley F.C. and Liverpool F.C. as participants are:

The 1914 FA Cup Final was a football match between Burnley and Liverpool on 25 April 1914 at Crystal Palace, London. [alce::435__wikidata_intersection__dev::p14]
> Additionally, Burnley and Liverpool faced each other in the League Cup, as indicated by a reference to "the League Cup meeting" between the two teams. [alce::435__wikidata_intersection__dev::p45]

Cited: alce::435__wikidata_intersection__dev::p14, alce::435__wikidata_intersection__dev::p45

### `305__wikidata_comp__dev`
_Refused._

### `320__wikidata_intersection__dev`
_Refused._

### `649__wikidata_simple__dev`
> The Somali Armed Forces are the military forces of Somalia, officially known as the "Federal Republic of Somalia." [alce::649__wikidata_simple__dev::p2]
> They are headed by the President as Commander in Chief. [alce::649__wikidata_simple__dev::p2]
> The Somali Armed Forces were initially made up of the Army, Navy, Air Force and Police Force. [alce::649__wikidata_simple__dev::p2]

Cited: alce::649__wikidata_simple__dev::p2

### `286__wikidata_comp__dev`
> Ray directed "55 Days at Peking," a motion picture authored by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]
> Guy Green also directed "55 Days at Peking," which was authored by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]
> Mann directed "The Fall of the Roman Empire," a motion picture written by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]
> Henry Hathaway directed "Circus World," which was mostly written by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]

Cited: alce::286__wikidata_comp__dev::p3

### `171__wikidata_intersection__dev`
_Refused._

### `563__wikidata_simple__dev`
> Prime Press published science fiction books during its brief four-year lifespan. [alce::563__wikidata_simple__dev::p0]
> One work they were involved with was "Lost Continents" by L. Sprague de Camp, though Prime Press printed the signatures but handed the project off to Gnome Press who completed the binding with a new title page. [alce::563__wikidata_simple__dev::p1]

Cited: alce::563__wikidata_simple__dev::p0, alce::563__wikidata_simple__dev::p1

### `245__wikidata_intersection__dev`
> Based on the provided sources, there are multiple movies directed by Gautham Menon that had music composed by Harris Jayaraj:

"Minnale" was directed by Gautham Menon with music composed by Harris Jayaraj. [alce::245__wikidata_intersection__dev::p11]
> "Kaakha Kaakha" was directed by Gautham Menon with music composed by Harris Jayaraj. [alce::245__wikidata_intersection__dev::p11]
> "Vettaiyaadu Vilaiyaadu" was directed by Gautham Menon with music composed by Harris Jayaraj. [alce::245__wikidata_intersection__dev::p47]
> "Yennai Arindhaal" was directed by Gautham Menon with music composed by Harris Jayaraj. [alce::245__wikidata_intersection__dev::p1]

Cited: alce::245__wikidata_intersection__dev::p1, alce::245__wikidata_intersection__dev::p11, alce::245__wikidata_intersection__dev::p47

### `534__wikitables_simple__dev`
> Based on the provided sources, the following professional wrestling memorial shows since 1980 are documented:

The Mike Marino Memorial Shield was a British professional wrestling single-elimination tournament that took place on 29 September 1981 at Fairfield Halls in Croydon, England, and is described as one of the first, if not the first, memorial shows in British professional wrestling. [alce::534__wikitables_simple__dev::p12]
> The Terry Gordy Memorial Show was a professional wrestling memorial event produced by the Legends of Pro Wrestling (LPW) promotion. [alce::534__wikitables_simple__dev::p7]
> The Fourth Annual Mark Curtis Memorial Weekend of Champions was a two-day professional wrestling memorial show produced by Southern States Wrestling (SSW), which took place from May 9–10, 2003, at the Civic Auditorium in Kingsport, Tennessee. [alce::534__wikitables_simple__dev::p89]
> The Fred Ward Memorial Show was an annual professional wrestling memorial event produced by the Georgia Championship Wrestling (GCW) promotion, which was held from 2004 to 2009. [alce::534__wikitables_simple__dev::p18]

Cited: alce::534__wikitables_simple__dev::p12, alce::534__wikitables_simple__dev::p18, alce::534__wikitables_simple__dev::p7, alce::534__wikitables_simple__dev::p89

### `26__wikitables_composition__dev`
> "The Terror" is a British thriller film released in 1938. [alce::26__wikitables_composition__dev::p66]

Cited: alce::26__wikitables_composition__dev::p66

### `169__wikidata_comp__dev`
> Jonas Jerebko, a Detroit Pistons draft selection, holds Swedish citizenship. [alce::169__wikidata_comp__dev::p1]

Cited: alce::169__wikidata_comp__dev::p1

### `674__wikidata_simple__dev`
> Several schools are of the Free Methodist Church confession:

Azusa Pacific University is supported by the Free Methodist Church. [alce::674__wikidata_simple__dev::p0]
> The College of the Japanese Free Methodist Church is affiliated with the Free Methodist Church. [alce::674__wikidata_simple__dev::p18]
> Hope Africa University in Bujumbura, Burundi is associated with the Free Methodist Church. [alce::674__wikidata_simple__dev::p18]
> Haiti Providence University is affiliated with the Free Methodist Church. [alce::674__wikidata_simple__dev::p18]
> The Faculdade de Teologia Metodista Livre in São Paulo, Brazil is a Free Methodist theological school. [alce::674__wikidata_simple__dev::p18]
> Osaka Christian University is an international Free Methodist educational institution. [alce::674__wikidata_simple__dev::p0]

Cited: alce::674__wikidata_simple__dev::p0, alce::674__wikidata_simple__dev::p18

### `725__wikidata_simple__dev`
> Vladimir Albitsky discovered 10 asteroids during 1923–1925. [alce::725__wikidata_simple__dev::p1]

Cited: alce::725__wikidata_simple__dev::p1

### `730__wikidata_simple__dev`
> Chabad Lubavitch was founded by Rabbi Schneur Zalman of Liadi. [alce::730__wikidata_simple__dev::p1]
> He founded the movement in 1775. [alce::730__wikidata_simple__dev::p1]

Cited: alce::730__wikidata_simple__dev::p1

### `430__wikidata_intersection__dev`
> Michael Schumacher won the French Grand Prix on multiple occasions. [alce::430__wikidata_intersection__dev::p4]
> He won the 1994 French Grand Prix driving a Benetton-Ford. [alce::430__wikidata_intersection__dev::p0]
> He won the 1998 French Grand Prix driving a Ferrari. [alce::430__wikidata_intersection__dev::p2]
> He won the 2001 French Grand Prix driving a Ferrari. [alce::430__wikidata_intersection__dev::p44]
> He won the 2004 French Grand Prix using an unprecedented four-stop strategy.

Cited: alce::430__wikidata_intersection__dev::p0, alce::430__wikidata_intersection__dev::p2, alce::430__wikidata_intersection__dev::p4, alce::430__wikidata_intersection__dev::p44

### `172__wikidata_comp__dev`
> The Canadian Grand Prix has had multiple winners across different years:

Sebastian Vettel won the 2018 Canadian Grand Prix. [alce::172__wikidata_comp__dev::p12]
> Jenson Button won the 2011 Canadian Grand Prix. [alce::172__wikidata_comp__dev::p5]
> Robert Kubica won the 2008 Canadian Grand Prix. [alce::172__wikidata_comp__dev::p16]
> Lewis Hamilton won the 2007 Canadian Grand Prix. [alce::172__wikidata_comp__dev::p10]
> Daniel Ricciardo won the 2014 Canadian Grand Prix. [alce::172__wikidata_comp__dev::p1]

Cited: alce::172__wikidata_comp__dev::p1, alce::172__wikidata_comp__dev::p10, alce::172__wikidata_comp__dev::p12, alce::172__wikidata_comp__dev::p16, alce::172__wikidata_comp__dev::p5

### `606__wikidata_simple__dev`
> Based on the provided sources, several professional beach volleyball players are mentioned:

Brooke Niles is a professional beach volleyball player from the United States who plays on the FIVB World Tour and Top US Pro Tour. [alce::606__wikidata_simple__dev::p55]
> Marloes Wesselink is a Dutch professional beach volleyball player born in Doetinchem. [alce::606__wikidata_simple__dev::p94]
> Patricia Labee is a Dutch female professional beach volleyball and indoor volleyball player born in Rotterdam. [alce::606__wikidata_simple__dev::p99]

Cited: alce::606__wikidata_simple__dev::p55, alce::606__wikidata_simple__dev::p94, alce::606__wikidata_simple__dev::p99

### `700__wikidata_simple__dev`
> The first Tulu film was "Enna Thangadi" released in 1971. [alce::700__wikidata_simple__dev::p1]

Cited: alce::700__wikidata_simple__dev::p1

### `452__wikidata_intersection__dev`
> Irwin Allen both directed and produced "The Swarm" (1978) and "Beyond the Poseidon Adventure" (1979). [alce::452__wikidata_intersection__dev::p1]

Cited: alce::452__wikidata_intersection__dev::p1

### `213__wikidata_intersection__dev`
> Several individuals graduated from the US Coast Guard Academy and joined the US Coast Guard:

Thomas H. Collins graduated from the U.S. Coast Guard Academy in 1968 and served in the U.S. Coast Guard, eventually becoming the 22nd Commandant. [alce::213__wikidata_intersection__dev::p13]
> Karl L. Schultz graduated from the U.S. Coast Guard Academy in 1983 and became the 26th Commandant of the U.S. Coast Guard. [alce::213__wikidata_intersection__dev::p12]
> Patrick M. Stillman graduated from the Coast Guard Academy in 1972 and served as a Rear Admiral in the United States Coast Guard. [alce::213__wikidata_intersection__dev::p96]
> Robert S. Lucas graduated from the United States Coast Guard Academy in 1952 and served as a rear admiral in the United States Coast Guard. [alce::213__wikidata_intersection__dev::p46]
> John B. Hayes graduated from the United States Coast Guard Academy in 1946 and served as the 16th Commandant of the U.S. Coast Guard. [alce::213__wikidata_intersection__dev::p91]

Cited: alce::213__wikidata_intersection__dev::p12, alce::213__wikidata_intersection__dev::p13, alce::213__wikidata_intersection__dev::p46, alce::213__wikidata_intersection__dev::p91, alce::213__wikidata_intersection__dev::p96

### `410__wikidata_intersection__dev`
_Refused._

### `514__wikitables_simple__dev`
> Based on the provided sources, the following are documentary film festivals:

Doc/Fest is a documentary film festival held in Sheffield, described as "one of the Top Five Coolest Documentary Film Festivals in the World." [alce::514__wikitables_simple__dev::p12]
> The Full Frame Documentary Film Festival is an annual international event dedicated to the theatrical exhibition of non-fiction cinema. [alce::514__wikitables_simple__dev::p27]
> Al Jazeera International Documentary Film Festival is an international film festival showcasing documentaries organized by Al Jazeera. [alce::514__wikitables_simple__dev::p9]
> DOC LA (Los Angeles Documentary Film Festival) is an international documentary film festival in Hollywood, California. [alce::514__wikitables_simple__dev::p10]
> Dokufest is an International Documentary and Short Film Festival held in the Kosovo town of Prizren. [alce::514__wikitables_simple__dev::p2]

Cited: alce::514__wikitables_simple__dev::p10, alce::514__wikitables_simple__dev::p12, alce::514__wikitables_simple__dev::p2, alce::514__wikitables_simple__dev::p27, alce::514__wikitables_simple__dev::p9

### `81__wikitables_composition__dev`
> During the summer of 2015, Sunderland made several transfers:

Jeremain Lens joined as a winger. [alce::81__wikitables_composition__dev::p7]
> Fabio Borini joined as a striker. [alce::81__wikitables_composition__dev::p7]
> Yann M'Vila joined on a season-long loan on 6 August 2015. [alce::81__wikitables_composition__dev::p85]
> DeAndre Yedlin joined on a loan signing. [alce::81__wikitables_composition__dev::p7]
> Ola Toivonen joined on a season-long loan on 28 August 2015. [alce::81__wikitables_composition__dev::p6]

Cited: alce::81__wikitables_composition__dev::p6, alce::81__wikitables_composition__dev::p7, alce::81__wikitables_composition__dev::p85

### `475__wikitables_simple__dev`
> Based on the provided sources, reefs are located in the following places:

Coral reefs are found in the Pacific and western Atlantic regions. [alce::475__wikitables_simple__dev::p92]
> There are coral reefs in the Persian Gulf, Madagascar, the Philippines, Hawaiian Islands and off Southeast Asia. [alce::475__wikitables_simple__dev::p92]
> Shallow-water reefs are only found in areas between 30° N to 30° S from the equator. [alce::475__wikitables_simple__dev::p42]
> Coral reefs are rare along the west coasts of the Americas and Africa due to upwelling and strong cold coastal currents. [alce::475__wikitables_simple__dev::p5]
> Corals are seldom found along the coastline of South Asia—from the eastern tip of India (Chennai) to the Bangladesh and Myanmar borders—as well as along the coasts of northeastern South America and Bangladesh. [alce::475__wikitables_simple__dev::p5]
> Reefs are located in the northern Tasman Sea, around 95 km north from Lord Howe Island and 555 km off the New South Wales coast. [alce::475__wikitables_simple__dev::p6]
> These represent the southernmost platform reefs in the world. [alce::475__wikitables_simple__dev::p6]
> Fringing reefs are distributed widely in the Great Barrier Reef system, most common towards the southern part and attached to high islands like the Whitsunday Islands. [alce::475__wikitables_simple__dev::p8]
> Lagoonal reefs are found in the southern Great Barrier Reef and off the coast of Princess Charlotte Bay. [alce::475__wikitables_simple__dev::p8]

Cited: alce::475__wikitables_simple__dev::p42, alce::475__wikitables_simple__dev::p5, alce::475__wikitables_simple__dev::p6, alce::475__wikitables_simple__dev::p8, alce::475__wikitables_simple__dev::p92

### `99__wikitables_composition__dev`
> Dalby is a Swedish locality found in Lund Municipality. [alce::99__wikitables_composition__dev::p26]

Cited: alce::99__wikitables_composition__dev::p26

### `688__wikidata_simple__dev`
> Fox Business Morning was the first show to be aired on the Fox Business Network when it launched on October 15, 2007. [alce::688__wikidata_simple__dev::p4]

Cited: alce::688__wikidata_simple__dev::p4

### `1368__wikidata_simple__dev`
_Refused._

### `206__wikidata_intersection__dev`
> Attarintiki Daredi is the film whose soundtrack was written by Devi Sri Prasad and was authored by Trivikram Srinivas. [alce::206__wikidata_intersection__dev::p8]

Cited: alce::206__wikidata_intersection__dev::p8

### `661__wikidata_simple__dev`
> Victor W. Marek was the doctoral advisor to 16 doctoral candidates in mathematics and computer science. [alce::661__wikidata_simple__dev::p2]
> In mathematics, his students included Małgorzata Dubiel-Lachlan, Roman Kossak, Adam Krawczyk, Tadeusz Kreid, Roman Murawski, Andrzej Pelc, Zygmunt Ratajczyk, Marian Srebrny, and Zygmunt Vetulani. [alce::661__wikidata_simple__dev::p2]
> In computer science, his students were V. K. Cody Bumgardner, Waldemar W. Koczkodaj, Witold Lipski Jr., Joseph Oldham, Inna Pivkina, Michał Sobolewski, Paweł Traczyk, and Zygmunt Vetulani. [alce::661__wikidata_simple__dev::p2]

Cited: alce::661__wikidata_simple__dev::p2

### `540__wikitables_simple__dev`
> Several commonly used chord progressions are documented in Western music:

The 12 bar blues progression is a widely used chord progression in Western traditional music and blues. [alce::540__wikitables_simple__dev::p9]
> The V–I progression, known as an authentic cadence, is a common cadential progression that returns to the tonic or I chord. [alce::540__wikitables_simple__dev::p39]
> The ⅱ–Ⅴ–I progression is a common cadential chord progression used in a wide variety of music genres, including jazz harmony. [alce::540__wikitables_simple__dev::p64]
> In Western tonal music, chord progressions between chords whose roots are related by perfect fifth are commonly found. [alce::540__wikitables_simple__dev::p29]

Cited: alce::540__wikitables_simple__dev::p29, alce::540__wikitables_simple__dev::p39, alce::540__wikitables_simple__dev::p64, alce::540__wikitables_simple__dev::p9

### `517__wikitables_simple__dev`
> Based on the provided sources, the following weapons are of the type grenade launcher:

The Mk 19 is a crew-served automatic grenade launcher. [alce::517__wikitables_simple__dev::p1]
> The CIS 40 GL is a Singaporean grenade launcher. [alce::517__wikitables_simple__dev::p26]
> The M203 is an American grenade launcher. [alce::517__wikitables_simple__dev::p26]
> The HK69A1 is a 40 mm grenade launcher developed and produced by Heckler & Koch. [alce::517__wikitables_simple__dev::p26]
> The Type 91 Grenade Launcher is a Chinese grenade launcher used to launch 35mm non-lethal grenades. [alce::517__wikitables_simple__dev::p2]

Cited: alce::517__wikitables_simple__dev::p1, alce::517__wikitables_simple__dev::p2, alce::517__wikitables_simple__dev::p26

### `962__wikidata_comp__dev`
_Refused._

### `473__wikitables_simple__dev`
> A bounty hunter is a person who captures fugitives for a bounty. [alce::473__wikitables_simple__dev::p3]
> One specific example of a bounty hunter is Connie Kalitta, an American businessman and former drag racing driver who was nicknamed "The Bounty Hunter." [alce::473__wikitables_simple__dev::p76]

Cited: alce::473__wikitables_simple__dev::p3, alce::473__wikitables_simple__dev::p76

### `697__wikidata_simple__dev`
> Lesley Thomson was one of Scotland's Solicitor General, serving in that position from 2011 to 2016. [alce::697__wikidata_simple__dev::p20]

Cited: alce::697__wikidata_simple__dev::p20

### `388__wikidata_comp__dev`
_Refused._

### `133__wikidata_comp__dev`
_Refused._

### `86__wikitables_composition__dev`
> Henry L. Williams served as the head football coach at the University of Minnesota from 1900 to 1921. [alce::86__wikitables_composition__dev::p1]
> This means the football seasons under his leadership spanned from the 1900 season through the 1921 season, inclusive.

Cited: alce::86__wikitables_composition__dev::p1

### `322__wikidata_comp__dev`
_Refused._

### `27__wikitables_composition__dev`
> Based on the provided sources, here are the saints canonized by Pope Francis after 17 December 2013:

Angela of Foligno was canonized through equipollent canonization on 9 October 2013, which is before the specified date. [alce::27__wikitables_composition__dev::p3]
> Peter Faber was canonized through equipollent canonization on 17 December 2013, which is not after that date. [alce::27__wikitables_composition__dev::p50]
> José de Anchieta and Marie of the Incarnation were approved for equipollent canonization on 3 April 2014. [alce::27__wikitables_composition__dev::p3]
> John XXIII and John Paul II were canonized on 27 April 2014. [alce::27__wikitables_composition__dev::p0]
> Six additional saints were canonized on 23 November 2014. [alce::27__wikitables_composition__dev::p0]
> Joseph Vaz was canonized on 14 January 2015. [alce::27__wikitables_composition__dev::p0]
> Four saints were canonized on 17 May 2015. [alce::27__wikitables_composition__dev::p0]
> Junípero Serra was canonized on 23 September 2015. [alce::27__wikitables_composition__dev::p0]
> Four saints were canonized on 18 October 2015, including the first married couple to be named as saints. [alce::27__wikitables_composition__dev::p0]
> Maria Elisabeth Hesselblad and Stanislaus Papczyński were canonized on 5 June 2016. [alce::27__wikitables_composition__dev::p0]

Cited: alce::27__wikitables_composition__dev::p0, alce::27__wikitables_composition__dev::p3, alce::27__wikitables_composition__dev::p50

### `791__wikidata_simple__dev`
> The Gornergrat railway station is part of the Gornergrat Railway. [alce::791__wikidata_simple__dev::p2]
> Additionally, the Rotenboden railway station is part of the Gornergrat Railway system. [alce::791__wikidata_simple__dev::p10]

Cited: alce::791__wikidata_simple__dev::p10, alce::791__wikidata_simple__dev::p2

### `88__wikitables_composition__dev`
> Several organizations in Canada have endorsed the BDS movement:

The political party Québec solidaire, the second largest public sector union Centrale des syndicats du Québec, and the feminist organization Fédération des femmes du Québec have all supported the BDS campaign. [alce::88__wikitables_composition__dev::p0]
> The Ontario wing of the Canadian Union of Public Employees (CUPE) has supported the Boycott, Divestment and Sanctions (BDS) campaign against Israel since 2006. [alce::88__wikitables_composition__dev::p17]
> Members of the Green Party of Canada voted to endorse BDS in August 2016. [alce::88__wikitables_composition__dev::p3]
> The Fédération des syndicats nationaux in Quebec, Canada, representing 325,000 in nearly 2,000 unions, voted to join the campaign for BDS and support a military embargo against Israel. [alce::88__wikitables_composition__dev::p6]

Cited: alce::88__wikitables_composition__dev::p0, alce::88__wikitables_composition__dev::p17, alce::88__wikitables_composition__dev::p3, alce::88__wikitables_composition__dev::p6

### `899__wikidata_simple__dev`
_Refused._

### `108__wikidata_intersection__dev`
> Francis Searle directed multiple Hammer Film Productions movies. [alce::108__wikidata_intersection__dev::p27]
> Beginning with "Paranoiac" (1963), he made numerous films for Hammer throughout the 1960s and 1970s, including thrillers such as "Nightmare" (1964) and "Hysteria" (1965). [alce::108__wikidata_intersection__dev::p27]
> He also directed monster films for Hammer including "The Evil of Frankenstein" (1964) and "Dracula Has Risen from the Grave" (1968). [alce::108__wikidata_intersection__dev::p3]

Cited: alce::108__wikidata_intersection__dev::p27, alce::108__wikidata_intersection__dev::p3

### `892__wikidata_simple__dev`
> The North Dakota Wing was part of the Civil Air Patrol. [alce::892__wikidata_simple__dev::p97]
> The New Hampshire Wing was also part of the Civil Air Patrol. [alce::892__wikidata_simple__dev::p44]

Cited: alce::892__wikidata_simple__dev::p44, alce::892__wikidata_simple__dev::p97

### `500__wikitables_simple__dev`
> The New York Times provides a daily news podcast called "The Daily," hosted by political journalist Michael Barbaro. [alce::500__wikitables_simple__dev::p2]
> CBS News provided a daily news audio podcast called the "CBS News iCast," created and hosted by Correspondent and Anchor Chris Mavridis. [alce::500__wikitables_simple__dev::p3]
> ABC News began its first daily podcast called "Start Here" on March 28, 2018. [alce::500__wikitables_simple__dev::p9]

Cited: alce::500__wikitables_simple__dev::p2, alce::500__wikitables_simple__dev::p3, alce::500__wikitables_simple__dev::p9

### `529__wikitables_simple__dev`
> Based on the provided sources, here are the existing environmental film festivals:

The Environmental Film Festival Australia is a film festival which screens domestically and internationally produced environmental films around Australia, having launched in 2010. [alce::529__wikitables_simple__dev::p1]
> The San Francisco Green Film Festival is an environmental film festival which was first held in March 2011. [alce::529__wikitables_simple__dev::p7]
> The Environmental Film Festival in the Nation's Capital hosts the largest environmental film festival in the United States each March in Washington, DC, presenting more than 100 films to an audience of over 30,000. [alce::529__wikitables_simple__dev::p2]
> The G2 Green Earth Film Festival is an annual environmental film festival that takes place at The G2 Gallery in Venice, California, and began in 2013. [alce::529__wikitables_simple__dev::p10]

Cited: alce::529__wikitables_simple__dev::p1, alce::529__wikitables_simple__dev::p10, alce::529__wikitables_simple__dev::p2, alce::529__wikitables_simple__dev::p7

### `551__wikitables_simple__dev`
> Several magazines are carnivorous plant periodicals:

AIPC Magazine is a quarterly Italian-language periodical and the official publication of a carnivorous plant society based in Italy. [alce::551__wikitables_simple__dev::p36]
> Planta Carnivora is a biannual periodical and the official publication of The Carnivorous Plant Society of the United Kingdom. [alce::551__wikitables_simple__dev::p2]
> The Carnivorous Plant Newsletter is the official publication of the International Carnivorous Plant Society. [alce::551__wikitables_simple__dev::p1]
> The Bulletin of the Australian Carnivorous Plant Society was a quarterly periodical and the official publication of the Australian Carnivorous Plant Society. [alce::551__wikitables_simple__dev::p4]

Cited: alce::551__wikitables_simple__dev::p1, alce::551__wikitables_simple__dev::p2, alce::551__wikitables_simple__dev::p36, alce::551__wikitables_simple__dev::p4

### `578__wikidata_simple__dev`
> Acura produces several car models. The initial offerings included the Legend and Integra. [alce::578__wikidata_simple__dev::p51]
> Later models include the Acura TL, which was first offered as a Type-S variant in 2002. [alce::578__wikidata_simple__dev::p18]
> Acura also produced the Acura NSX. [alce::578__wikidata_simple__dev::p18]
> The Acura RL is a mid-sized/executive luxury car that was manufactured by Acura for the 1996–2012 model years. [alce::578__wikidata_simple__dev::p58]
> Additionally, Acura produced the Acura RLX, which replaced the RL in 2013. [alce::578__wikidata_simple__dev::p58]
> Acura also produced the Acura ILX. [alce::578__wikidata_simple__dev::p11]

Cited: alce::578__wikidata_simple__dev::p11, alce::578__wikidata_simple__dev::p18, alce::578__wikidata_simple__dev::p51, alce::578__wikidata_simple__dev::p58

### `448__wikidata_intersection__dev`
> The FA Charity Shield featured both Manchester United and Liverpool FC as competitors. [alce::448__wikidata_intersection__dev::p25]
> Liverpool and United contested the Shield multiple times, with United winning in 1983 and the Shield being shared on three other occasions in 1965, 1977, and 1990. [alce::448__wikidata_intersection__dev::p97]

Cited: alce::448__wikidata_intersection__dev::p25, alce::448__wikidata_intersection__dev::p97

### `154__wikidata_comp__dev`
> Multiple golfers have won the Masters Tournament. Jack Nicklaus won the most Masters victories with six titles between 1963 and 1986. [alce::154__wikidata_comp__dev::p2]
> Arnold Palmer and Tiger Woods have each won four Masters titles. [alce::154__wikidata_comp__dev::p2]
> Other notable Masters winners include Horton Smith, who won in 1934 and 1936, [alce::154__wikidata_comp__dev::p2]
> Zach Johnson, who won in 2007, [alce::154__wikidata_comp__dev::p4]
> Bubba Watson, who won in 2014, [alce::154__wikidata_comp__dev::p39]
> and Danny Willett, who won in 2016. [alce::154__wikidata_comp__dev::p83]

Cited: alce::154__wikidata_comp__dev::p2, alce::154__wikidata_comp__dev::p39, alce::154__wikidata_comp__dev::p4, alce::154__wikidata_comp__dev::p83

### `582__wikidata_simple__dev`
> Jerome Robbins choreographed dances in numerous stage productions. [alce::582__wikidata_simple__dev::p3]
> These included "On the Town", "Peter Pan", "High Button Shoes", "The King and I", "The Pajama Game", "Bells Are Ringing", "West Side Story", "Gypsy", and "Fiddler on the Roof". [alce::582__wikidata_simple__dev::p3]
> Additionally, Robbins choreographed several ballets for New York City Ballet, including "The Goldberg Variations", "Glass Pieces", "Eight Lines", "The Four Seasons", "Fanfare", "Piccolo Balletto", "Verdi Variations", and "Dances at a Gathering". [alce::582__wikidata_simple__dev::p50]
> He also choreographed the ballet "Les Noces" to Stravinsky's music. [alce::582__wikidata_simple__dev::p8]

Cited: alce::582__wikidata_simple__dev::p3, alce::582__wikidata_simple__dev::p50, alce::582__wikidata_simple__dev::p8

### `156__wikidata_intersection__dev`
> Flavia Pennetta and Gisela Dulko won the 2010 WTA Tour Championships and the 2011 Australian Open in doubles. [alce::156__wikidata_intersection__dev::p0]
> They also won multiple titles in 2010, including the Sony Ericsson Open, Porsche Tennis Grand Prix, Internazionali BNL d'Italia, Swedish Open, and Rogers Cup. [alce::156__wikidata_intersection__dev::p7]

Cited: alce::156__wikidata_intersection__dev::p0, alce::156__wikidata_intersection__dev::p7

### `121__wikidata_comp__dev`
> Based on the provided sources, I can identify the following directors for TV programs that David Simon screenwrote:

For "The Corner" miniseries, Charles S. Dutton was the director. [alce::121__wikidata_comp__dev::p13]
> For "Treme," Ernest Dickerson directed several episodes, including the season 2 finale "Do Watcha Wanna." [alce::121__wikidata_comp__dev::p4]
> For "The Wire," Ernest Dickerson also served as a director, helming multiple episodes across different seasons. [alce::121__wikidata_comp__dev::p7]

Cited: alce::121__wikidata_comp__dev::p13, alce::121__wikidata_comp__dev::p4, alce::121__wikidata_comp__dev::p7

### `140__wikidata_comp__dev`
> Arthur Hiller directed "The Hospital" (1971), a movie for which Paddy Chayefsky was the screenwriter. [alce::140__wikidata_comp__dev::p91]

Cited: alce::140__wikidata_comp__dev::p91

### `328__wikidata_intersection__dev`
_Refused._
