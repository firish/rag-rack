# Eval Report: alce_qampari_gtr

- **Pipeline:** `anthropic/claude-haiku-4-5 | bge-small | hybrid(BM25+lance) | min_tokens=100 | cohere-rerank-v3 | retrieve=100/rerank=5 | no-verifier | loose | gen=constrained`
- **Run at:** 2026-05-18 22:32:36
- **Questions:** 1000

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.000 |
| `citation_recall` | 1.000 |
| `citation_f1` | 0.000 |
| `coverage` | 0.000 |
| `localization_accuracy` | 0.121 |
| `abstention_precision` | 0.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.000 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `799__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.64 |
| `136__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `248__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.35 |
| `366__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `663__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.61 |
| `777__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `386__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `843__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `801__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `8__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `481__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `439__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `772__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `336__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `479__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `573__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.72 |
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
| `806__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `224__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `577__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `12__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `699__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `285__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `891__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `804__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.39 |
| `972__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `642__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1008__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `930__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `62__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `317__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.65 |
| `902__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `29__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `851__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `719__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `739__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `639__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `607__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `897__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.44 |
| `437__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `758__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.81 |
| `599__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `927__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `834__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `815__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.92 |
| `174__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `487__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `414__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.98 |
| `460__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `859__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `610__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `278__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `743__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.02 |
| `948__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.39 |
| `524__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.56 |
| `353__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `818__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `403__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.80 |
| `387__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `360__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.81 |
| `1012__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1002__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.69 |
| `234__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `555__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `449__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `893__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `633__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `935__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `253__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `951__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `498__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.78 |
| `374__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `721__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `377__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `587__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `741__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `707__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `293__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `773__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.88 |
| `212__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `195__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `283__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `569__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.84 |
| `675__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.74 |
| `1351__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `14__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `461__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.90 |
| `903__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.76 |
| `325__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `58__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `916__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `919__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `723__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `628__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.70 |
| `379__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `654__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.59 |
| `714__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `338__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.53 |
| `1352__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `196__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `289__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.48 |
| `1000__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `965__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `333__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `281__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `539__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.50 |
| `52__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `80__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `310__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `657__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.28 |
| `429__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `508__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `936__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `362__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.84 |
| `784__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.81 |
| `231__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `247__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `644__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.48 |
| `71__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `492__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.63 |
| `562__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `979__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.83 |
| `636__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `39__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `226__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `757__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `618__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.57 |
| `418__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `56__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `767__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `594__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `648__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.32 |
| `4__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `875__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.77 |
| `826__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `868__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `191__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.69 |
| `769__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.76 |
| `855__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `593__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `73__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `846__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `1252__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `494__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.51 |
| `205__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `632__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.41 |
| `865__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `690__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `704__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.60 |
| `456__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `929__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `13__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.68 |
| `713__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `519__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.95 |
| `914__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `749__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `586__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `798__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.16 |
| `162__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `184__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `658__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.88 |
| `288__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `103__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `630__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `819__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `672__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `351__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `655__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `934__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `182__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `428__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.73 |
| `1010__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `9__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `37__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `416__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `835__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.82 |
| `931__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `740__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.45 |
| `623__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.76 |
| `638__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.26 |
| `364__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `958__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `522__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.95 |
| `447__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `24__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `653__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `1254__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `287__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `584__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `33__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `95__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `1353__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `684__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `768__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `693__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `230__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `408__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.64 |
| `252__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `583__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.20 |
| `718__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.70 |
| `484__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `616__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.63 |
| `144__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `592__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `925__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.57 |
| `775__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `110__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `426__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `15__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `120__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.63 |
| `966__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `440__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `413__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.82 |
| `820__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `664__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `118__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `260__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1259__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.20 |
| `358__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.72 |
| `711__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `751__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.95 |
| `354__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.84 |
| `560__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `715__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `643__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `790__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `404__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.84 |
| `148__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `232__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `874__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `670__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `211__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.95 |
| `308__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `280__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `150__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `917__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `933__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.79 |
| `629__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `319__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `755__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `235__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `46__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `698__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.85 |
| `105__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `343__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `756__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.59 |
| `515__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `779__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `572__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `397__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `465__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `949__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.85 |
| `800__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `538__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `375__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `36__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `736__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `491__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `750__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `1256__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `809__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.77 |
| `82__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `689__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `202__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.32 |
| `111__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `516__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `645__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `944__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `6__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `405__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `464__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `198__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `634__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `896__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `161__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `122__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `1354__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.87 |
| `321__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `301__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `119__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `668__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `805__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `284__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `595__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `369__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `852__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.90 |
| `729__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `659__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.31 |
| `208__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `419__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `898__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `963__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `49__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `695__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `637__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `793__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.78 |
| `272__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1251__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.91 |
| `588__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `422__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `911__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `40__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.82 |
| `341__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `565__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.86 |
| `900__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `251__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `742__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.74 |
| `557__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `177__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `920__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `391__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.44 |
| `1355__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.76 |
| `309__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `335__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.19 |
| `615__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `597__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `945__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `318__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.95 |
| `22__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `766__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.27 |
| `1356__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `600__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `237__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.79 |
| `549__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.24 |
| `109__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `734__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `482__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `696__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `222__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `621__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `459__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.81 |
| `116__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.24 |
| `703__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `394__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `238__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `537__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `502__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.97 |
| `559__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1357__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `425__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `327__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.69 |
| `181__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `554__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `477__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.10 |
| `307__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.88 |
| `604__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.58 |
| `1006__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.10 |
| `1103__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1253__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `55__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `889__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `17__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.73 |
| `70__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `849__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.26 |
| `513__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.67 |
| `526__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `1358__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `976__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `716__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.24 |
| `552__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `824__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `476__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `535__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `631__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `735__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.73 |
| `240__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `44__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `541__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.05 |
| `332__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `457__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `782__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `561__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `558__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.55 |
| `651__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `964__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `79__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.68 |
| `67__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `367__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `771__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `1007__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.18 |
| `576__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `622__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.70 |
| `407__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `973__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.79 |
| `813__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.68 |
| `867__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `923__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `114__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `857__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `166__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `257__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `620__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `124__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `313__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `504__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `60__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `135__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.56 |
| `323__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.61 |
| `402__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `971__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.77 |
| `292__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `829__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `104__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `781__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `20__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `568__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `879__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.27 |
| `378__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `228__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `692__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `493__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.19 |
| `544__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `1250__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `895__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `957__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.90 |
| `274__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `1011__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.85 |
| `881__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `548__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.52 |
| `1359__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `928__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `660__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `759__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.07 |
| `125__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `134__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `434__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `788__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.26 |
| `564__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.54 |
| `924__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `217__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `506__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `359__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.91 |
| `720__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.86 |
| `589__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `21__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `894__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `244__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `864__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `947__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.76 |
| `939__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `679__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.69 |
| `130__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.57 |
| `269__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.29 |
| `462__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.66 |
| `505__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.61 |
| `123__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `470__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.84 |
| `11__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `398__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `113__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `866__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `147__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `941__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `254__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.84 |
| `495__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `811__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.40 |
| `862__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.09 |
| `904__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.81 |
| `627__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `421__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `880__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
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
| `764__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `233__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `97__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.02 |
| `72__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `647__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `330__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `1003__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.90 |
| `486__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.45 |
| `778__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `483__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `950__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `334__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.60 |
| `770__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `830__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `83__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `300__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.83 |
| `273__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `575__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `1257__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.85 |
| `132__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `901__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.43 |
| `940__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `61__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.78 |
| `1360__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `814__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.76 |
| `591__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `159__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.88 |
| `531__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.66 |
| `840__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `872__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.78 |
| `303__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.69 |
| `94__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.11 |
| `3__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `270__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `433__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `63__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `530__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.16 |
| `676__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.83 |
| `932__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.85 |
| `342__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `823__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `543__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `838__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.72 |
| `1014__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `687__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.75 |
| `87__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.76 |
| `910__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `34__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `842__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.78 |
| `489__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.93 |
| `1361__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `614__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `54__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `142__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `209__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `510__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `762__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `188__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `906__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `546__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.74 |
| `207__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.91 |
| `977__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.96 |
| `1009__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `276__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `747__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.38 |
| `796__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `856__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `151__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.88 |
| `392__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `580__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `701__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `168__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `785__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.60 |
| `761__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.17 |
| `340__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `792__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `458__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `888__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.75 |
| `839__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.58 |
| `724__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `363__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.26 |
| `107__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `574__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `501__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `1300__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.86 |
| `390__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `887__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `878__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.52 |
| `752__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `423__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.17 |
| `214__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.83 |
| `304__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `411__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `84__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.78 |
| `153__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.67 |
| `65__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `265__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.39 |
| `215__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `98__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.68 |
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
| `1013__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `581__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `345__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.74 |
| `294__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `1__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `337__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.64 |
| `571__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `942__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `101__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `922__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `585__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `807__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.47 |
| `129__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `795__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.74 |
| `451__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.89 |
| `329__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `43__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `370__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `229__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `673__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `256__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `1005__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.89 |
| `605__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `667__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.39 |
| `832__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `170__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.37 |
| `66__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `523__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.85 |
| `271__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `722__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.09 |
| `227__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `727__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.08 |
| `92__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `496__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.78 |
| `961__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.63 |
| `905__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.53 |
| `204__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `1004__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.23 |
| `612__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.65 |
| `503__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.02 |
| `18__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `533__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `705__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `726__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `302__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.36 |
| `400__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.76 |
| `381__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.61 |
| `137__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `542__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `176__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `431__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.96 |
| `926__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `753__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `438__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `146__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `579__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `1362__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.92 |
| `282__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `678__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.91 |
| `609__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.81 |
| `794__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `567__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `797__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `255__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `424__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.83 |
| `946__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `128__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.92 |
| `324__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `51__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `625__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1258__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `203__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `450__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `967__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.68 |
| `180__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.93 |
| `30__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.49 |
| `825__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `952__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.57 |
| `28__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `978__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `677__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `331__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `210__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `165__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.92 |
| `117__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `854__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `602__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.89 |
| `446__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `666__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `732__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `78__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `968__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.08 |
| `787__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `512__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `845__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `652__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `131__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `399__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `372__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `96__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `75__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `780__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `178__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `90__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `115__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `837__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `314__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `296__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `869__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.56 |
| `848__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `441__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.74 |
| `937__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `173__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.52 |
| `680__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `836__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.91 |
| `509__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.85 |
| `499__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `89__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `528__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.72 |
| `754__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `85__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `355__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `1101__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `706__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `241__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.54 |
| `1363__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.67 |
| `371__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.93 |
| `969__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.82 |
| `858__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `1255__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.43 |
| `681__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `32__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `352__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `786__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `47__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `817__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `646__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.58 |
| `702__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `384__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.58 |
| `158__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `453__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `455__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `871__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `297__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `882__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `406__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.86 |
| `507__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `669__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `844__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `50__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `469__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `139__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.44 |
| `200__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.57 |
| `478__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.28 |
| `943__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `199__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `812__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `179__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `25__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `409__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `497__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.72 |
| `376__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.61 |
| `385__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.98 |
| `626__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `193__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `737__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.61 |
| `746__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `412__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `873__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `261__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `527__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `566__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `312__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `311__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `295__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `954__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.93 |
| `427__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.97 |
| `220__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `468__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `841__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `921__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.91 |
| `803__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `218__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `194__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.95 |
| `1350__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `76__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `236__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `598__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `185__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `53__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `187__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `915__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.07 |
| `42__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `816__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `1364__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.59 |
| `763__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `339__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.74 |
| `828__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `774__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.72 |
| `396__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.17 |
| `955__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.72 |
| `731__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.91 |
| `861__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.92 |
| `532__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `553__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `635__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `907__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `511__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.90 |
| `467__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.96 |
| `789__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `617__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.84 |
| `365__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `821__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.47 |
| `1365__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `7__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `395__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.70 |
| `383__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `201__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `192__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `243__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.97 |
| `167__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `748__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `810__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `91__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.49 |
| `938__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `831__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `463__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `913__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `246__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `149__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.38 |
| `346__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.83 |
| `38__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.69 |
| `190__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `275__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `802__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `102__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `264__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.95 |
| `382__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.84 |
| `221__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `69__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 1.00 |
| `326__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `959__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `650__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `545__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `471__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.84 |
| `258__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `68__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `262__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `268__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.97 |
| `518__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.87 |
| `2__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `31__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `808__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `827__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.27 |
| `547__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.20 |
| `445__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.69 |
| `619__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `239__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `373__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.23 |
| `443__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.91 |
| `263__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `1366__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `738__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `640__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `466__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `368__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.35 |
| `349__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `863__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `883__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `520__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `833__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `454__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `847__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.30 |
| `160__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.95 |
| `525__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `521__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `909__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `1102__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `783__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `850__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.46 |
| `1001__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.98 |
| `956__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `975__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.81 |
| `596__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.80 |
| `436__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `57__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.64 |
| `389__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `186__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `745__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.71 |
| `822__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `485__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.89 |
| `401__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.84 |
| `717__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.53 |
| `141__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.97 |
| `590__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `953__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.65 |
| `918__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.42 |
| `694__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.83 |
| `601__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `691__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `860__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.58 |
| `490__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.50 |
| `250__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `776__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.04 |
| `316__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.90 |
| `608__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `733__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `970__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.87 |
| `163__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `415__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.97 |
| `442__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `710__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `765__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `361__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.45 |
| `536__wikitables_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `138__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `641__wikidata_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.94 |
| `219__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `556__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.64 |
| `126__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `155__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.94 |
| `686__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `886__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.62 |
| `472__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `106__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.93 |
| `299__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.83 |
| `175__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.12 |
| `152__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `0__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `884__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `908__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `64__wikitables_composition__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.63 |
| `624__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.71 |
| `708__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `143__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.31 |
| `474__wikitables_simple__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.84 |
| `870__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `45__wikitables_composition__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.52 |
| `298__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.88 |
| `197__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `417__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.85 |
| `603__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `306__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.81 |
| `35__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `1367__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `225__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.76 |
| `682__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `267__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `876__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `444__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `728__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.87 |
| `432__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `570__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.46 |
| `259__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `974__wikidata_comp__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `435__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `305__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.92 |
| `320__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.81 |
| `649__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `286__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `171__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.99 |
| `563__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.94 |
| `245__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `534__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.91 |
| `26__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.87 |
| `169__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.11 |
| `674__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.95 |
| `725__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.77 |
| `730__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `430__wikidata_intersection__dev` | ✗ | ✗ | 0 | 4 | 0 | 1.00 |
| `172__wikidata_comp__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `606__wikidata_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `700__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `452__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `213__wikidata_intersection__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `410__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.98 |
| `514__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 1.00 |
| `81__wikitables_composition__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.92 |
| `475__wikitables_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.87 |
| `99__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `688__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `1368__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `206__wikidata_intersection__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `661__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.80 |
| `540__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 1.00 |
| `517__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.99 |
| `962__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.94 |
| `473__wikitables_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `697__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 1.00 |
| `388__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.58 |
| `133__wikidata_comp__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.97 |
| `86__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `322__wikidata_comp__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.96 |
| `27__wikitables_composition__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.96 |
| `791__wikidata_simple__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `88__wikitables_composition__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `899__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.99 |
| `108__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.83 |
| `892__wikidata_simple__dev` | ✗ | ✗ | 0 | 2 | 0 | 0.98 |
| `500__wikitables_simple__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `529__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `551__wikitables_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `578__wikidata_simple__dev` | ✗ | ✗ | 0 | 5 | 0 | 0.99 |
| `448__wikidata_intersection__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.98 |
| `154__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.99 |
| `582__wikidata_simple__dev` | ✗ | ✗ | 0 | 4 | 0 | 0.99 |
| `156__wikidata_intersection__dev` | ✗ | ✗ | 0 | 2 | 0 | 1.00 |
| `121__wikidata_comp__dev` | ✗ | ✗ | 0 | 3 | 0 | 0.80 |
| `140__wikidata_comp__dev` | ✗ | ✗ | 0 | 1 | 0 | 0.98 |
| `328__wikidata_intersection__dev` | ✓ | ✗ | 0 | 0 | 0 | 0.44 |

## Per-question answers

### `799__wikidata_simple__dev`
> **Crying Freeman**
> Crying Freeman is a manga drawn by Ryoichi Ikegami, created with writer Kazuo Koike. [alce::799__wikidata_simple__dev::p12]

Cited: alce::799__wikidata_simple__dev::p12

### `136__wikidata_intersection__dev`
> **Spring Breakers, Gummo, Julien Donkey-Boy, Mister Lonely, and Trash Humpers**
> Harmony Korine is best known for writing and directing 'Spring Breakers', 'Gummo', 'Julien Donkey-Boy' and 'Mister Lonely'. [alce::136__wikidata_intersection__dev::p0]
> Trash Humpers is a 2009 experimental black comedy-drama horror film written and directed by Harmony Korine. [alce::136__wikidata_intersection__dev::p6]

Cited: alce::136__wikidata_intersection__dev::p0, alce::136__wikidata_intersection__dev::p6

### `248__wikidata_comp__dev`
> **Multiple administrators attended different schools including the University of Michigan, International Christian University of Tokyo, Washington University in St. Louis, Collège du Léman in Geneva, International Community School of Addis Ababa, Euro-American Institute of Technology in Sophia Antipolis, and American University in Washington, D.C.**
> Sukehiro Hasegawa holds a Bachelor of Arts degree in political science from the University of Michigan, a Master of Arts degree in public administration from International Christian University of Tokyo, and a Ph.D. in international relations from Washington University in St. Louis, Missouri. [alce::248__wikidata_comp__dev::p96]
> Makonnen was educated in Switzerland and France, having attended the Collège du Léman in Geneva and a boarding school in Haute Savoie, and later attended International Community School of Addis Ababa until 2001, then enrolled at the Euro-American Institute of Technology in Sophia Antipolis, France, and transferred to American University in Washington, D.C. in 2003. [alce::248__wikidata_comp__dev::p44]

Cited: alce::248__wikidata_comp__dev::p44, alce::248__wikidata_comp__dev::p96

### `366__wikidata_comp__dev`
> **P. Balachandran**
> Ivan Megharoopan is a 2012 Malayalam biographical film written and directed by P. Balachandran. [alce::366__wikidata_comp__dev::p78]
> P. Balachandran is an Indian writer, playwright, scenarist, director, and actor who has scripted many films including 'Ulladakkam' (1991), 'Pavithram' (1994), 'Agnidevan' (1995), 'Punaradhivasam' (2000), and 'Kammatti Paadam' (2016). [alce::366__wikidata_comp__dev::p2]

Cited: alce::366__wikidata_comp__dev::p2, alce::366__wikidata_comp__dev::p78

### `663__wikidata_simple__dev`
_Refused._

### `777__wikidata_simple__dev`
> **Jewell Loyd**
> Jewell Loyd was drafted first overall in the 2015 WNBA Draft by the Seattle Storm. [alce::777__wikidata_simple__dev::p69]

Cited: alce::777__wikidata_simple__dev::p69

### `386__wikidata_comp__dev`
> **Yale University, Wycliffe Hall Oxford, and Birmingham University**
> Toby Howarth, the current and first area Bishop of Bradford, was educated at Yale University and Wycliffe Hall, Oxford. [alce::386__wikidata_comp__dev::p22]
> He studied at Birmingham University for his MA. [alce::386__wikidata_comp__dev::p22]

Cited: alce::386__wikidata_comp__dev::p22

### `843__wikidata_simple__dev`
> **The Bourne Ultimatum, The Informant!, Contagion, and Side Effects**
> Scott Z. Burns has written screenplays for "The Bourne Ultimatum" (2007), "The Informant!" (2009), and "Contagion" (2011). [alce::843__wikidata_simple__dev::p0]
> His films "The Informant!", "Contagion," and "Side Effects" were directed by Steven Soderbergh. [alce::843__wikidata_simple__dev::p0]

Cited: alce::843__wikidata_simple__dev::p0

### `801__wikidata_simple__dev`
> **Multiple works including "Timescape," "The Claw of the Conciliator," "No Enemy But Time," "Hominids," "The Shadow of the Torturer," "The Dragon Waiting," "Cosmos" magazine, "The New York Review of Science Fiction," "Year's Best SF," and "Year's Best Fantasy"**
> He edited the best-novel Nebula Award-winners "Timescape" by Gregory Benford (published 1980), "The Claw of the Conciliator" by Gene Wolfe (published 1981), and "No Enemy But Time" by Michael Bishop (published 1982), the best-novel Hugo Award-winner "Hominids" by Robert J. Sawyer (published 2002), and the World Fantasy Award-winning novels "The Shadow of the Torturer" by Gene Wolfe (1981) and "The Dragon Waiting" by John M. Ford (1984). [alce::801__wikidata_simple__dev::p4]
> In 1977, Hartwell edited the short-lived "Cosmos" magazine for the newly formed Baronet publishing. [alce::801__wikidata_simple__dev::p5]
> In 1988, Hartwell founded "The New York Review of Science Fiction", where he served as reviews editor. [alce::801__wikidata_simple__dev::p5]
> Hartwell edited two annual anthologies: "Year's Best SF", started in 1996 and co-edited with Kathryn Cramer since 2002, and "Year's Best Fantasy", co-edited with Cramer. [alce::801__wikidata_simple__dev::p3]

Cited: alce::801__wikidata_simple__dev::p3, alce::801__wikidata_simple__dev::p4, alce::801__wikidata_simple__dev::p5

### `8__wikitables_composition__dev`
> **One Marine Midland Center**
> One Marine Midland Center at 1 Seneca Tower is the tallest building in Buffalo. [alce::8__wikitables_composition__dev::p5]
> One Marine Midland Center is located in downtown Buffalo, New York. [alce::8__wikitables_composition__dev::p5]

Cited: alce::8__wikitables_composition__dev::p5

### `481__wikitables_simple__dev`
> **Science fiction magazine is a publication that offers primarily science fiction**
> A science fiction magazine is a publication that offers primarily science fiction, either in a hard copy periodical format or on the Internet. [alce::481__wikitables_simple__dev::p1]
> Science fiction magazines traditionally featured speculative fiction in short story, novelette, novella or (usually serialized) novel form, and many also contain editorials, book reviews or articles, and some also include stories in the fantasy and horror genres. [alce::481__wikitables_simple__dev::p1]

Cited: alce::481__wikitables_simple__dev::p1

### `439__wikidata_intersection__dev`
> **Thiruda Thiruda**
> Mani Ratnam worked on the script of 'Thiruda Thiruda' and served as producer under his production studio Aalayam Productions. [alce::439__wikidata_intersection__dev::p6]
> With the script of 'Thiruda Thiruda', he wanted to attempt the caper film genre for the first time. [alce::439__wikidata_intersection__dev::p6]

Cited: alce::439__wikidata_intersection__dev::p6

### `772__wikidata_simple__dev`
> **German submarine U-31 (S181)**
> German submarine U-31 (S181) is a Type 212A submarine of the German Navy, and the lead ship of her class. [alce::772__wikidata_simple__dev::p15]
> U-31 was built by TKMS, with construction taking place at the shipyards of Thyssen Nordseewerke of Emden and Howaldtswerke at Kiel, and was launched on 20 March 2002. [alce::772__wikidata_simple__dev::p15]

Cited: alce::772__wikidata_simple__dev::p15

### `336__wikidata_comp__dev`
> **Czechoslovakia and Australia**
> Kamila Vodičková was born in Litoměřice, Czechoslovakia and was made the first draft choice of the Seattle Storm franchise. [alce::336__wikidata_comp__dev::p27]
> Batkovic was drafted by the Seattle Storm in 2003 and was the only Australian drafted by the WNBA that year. [alce::336__wikidata_comp__dev::p13]

Cited: alce::336__wikidata_comp__dev::p13, alce::336__wikidata_comp__dev::p27

### `479__wikitables_simple__dev`
> **Bog bodies are naturally mummified human cadavers found in peat bogs, primarily in Northern Europe, dating from 8000 BCE to the Second World War, with notable examples including Lindow Man and Cashel Man**
> A bog body is a human cadaver that has been naturally mummified in a peat bog. [alce::479__wikitables_simple__dev::p2]
> Bog bodies have been found in Northern European countries of Denmark, Germany, the Netherlands, the United Kingdom and Ireland, with the oldest dating to about 8000 BCE. [alce::479__wikitables_simple__dev::p7]
> Bog bodies are dated to between 8000 BCE and the Second World War, and unlike most ancient human remains, they often retain their skin and internal organs due to the unusual conditions of the surrounding area. [alce::479__wikitables_simple__dev::p2]
> Notable bog bodies include Lindow Man, discovered in 1984 at Lindow Moss in Cheshire, North West England, and Cashel Man, a Bronze Age bog body from 2000 BCE. [alce::479__wikitables_simple__dev::p23, alce::479__wikitables_simple__dev::p26]
> As of 2006, more than 700 ancient bodies have been discovered in these sites, although other estimates have placed the number in the thousands. [alce::479__wikitables_simple__dev::p7]

Cited: alce::479__wikitables_simple__dev::p2, alce::479__wikitables_simple__dev::p23, alce::479__wikitables_simple__dev::p26, alce::479__wikitables_simple__dev::p7

### `573__wikidata_simple__dev`
> **Multiple films including "Tractor Drivers" (1939), "The Swineherd and the Shepherd" (1941), and "Cossacks of the Kuban" (1949)**
> Ivan Pyryev was a Soviet-Russian film director and screenwriter remembered as the high priest of Stalinist cinema. [alce::573__wikidata_simple__dev::p0]
> His films included 'Tractor Drivers' (1939), 'The Swineherd and the Shepherd' (1941), and his most famous, 'Cossacks of the Kuban' (1949), all of which starred his wife, Marina Ladynina. [alce::573__wikidata_simple__dev::p9]

Cited: alce::573__wikidata_simple__dev::p0, alce::573__wikidata_simple__dev::p9

### `885__wikidata_simple__dev`
> **Phish**
> Trey Anastasio is best known as the lead vocalist and guitarist for the rock band Phish, which he co-founded in 1983. [alce::885__wikidata_simple__dev::p1]

Cited: alce::885__wikidata_simple__dev::p1

### `683__wikidata_simple__dev`
_Refused._

### `356__wikidata_intersection__dev`
_Refused._

### `960__wikidata_comp__dev`
> **Multiple First-Circuit Appeals Court Judges attended different colleges: Plymouth State College, Amherst College, and Harvard University**
> Jeffrey Robert Howard is the Chief United States Circuit Judge of the United States Court of Appeals for the First Circuit and graduated from Plymouth State College (now Plymouth State University) in 1978 with a Bachelor of Arts degree. [alce::960__wikidata_comp__dev::p0]
> William Joseph Kayatta Jr. is a United States Circuit Judge of the United States Court of Appeals for the First Circuit and earned a Bachelor of Arts degree in 1976 from Amherst College. [alce::960__wikidata_comp__dev::p27]
> Levin Hicks Campbell is a Senior United States Circuit Judge of the United States Court of Appeals for the First Circuit and received an Artium Baccalaureus degree from Harvard University in 1948. [alce::960__wikidata_comp__dev::p56]
> Bailey Aldrich was a United States Circuit Judge of the United States Court of Appeals for the First Circuit and graduated from Harvard University with an Artium Baccalaureus degree in 1928. [alce::960__wikidata_comp__dev::p30]

Cited: alce::960__wikidata_comp__dev::p0, alce::960__wikidata_comp__dev::p27, alce::960__wikidata_comp__dev::p30, alce::960__wikidata_comp__dev::p56

### `744__wikidata_simple__dev`
> **Automobiles (cars and SUVs)**
> Baojun is a Chinese automobile marque owned by a joint venture of General Motors and SAIC Motor, SAIC-GM-Wuling Automobile. [alce::744__wikidata_simple__dev::p0]
> The Baojun marque was established in 2010 as a cheaper alternative to existing GM brands Chevrolet and Buick, which are also on sale in China. [alce::744__wikidata_simple__dev::p0]
> Baojun manufactures various vehicle models including the Baojun 630 (a compact sedan), the Baojun 310 (a subcompact hatchback), and the Baojun RS-5 (a compact crossover SUV). [alce::744__wikidata_simple__dev::p1, alce::744__wikidata_simple__dev::p2, alce::744__wikidata_simple__dev::p5]

Cited: alce::744__wikidata_simple__dev::p0, alce::744__wikidata_simple__dev::p1, alce::744__wikidata_simple__dev::p2, alce::744__wikidata_simple__dev::p5

### `671__wikidata_simple__dev`
> **Hachinohe Expressway, Kamaishi Expressway (partially), and Hokuriku Expressway (partially)**
> The Hachinohe Expressway is maintained and tolled by the East Nippon Expressway Company. [alce::671__wikidata_simple__dev::p3]
> From Hanamaki to Tōwa the Kamaishi Expressway is maintained and tolled by the East Nippon Expressway Company. [alce::671__wikidata_simple__dev::p12]
> The Hokuriku Expressway is owned and managed by East Nippon Expressway Company and Central Nippon Expressway Company. [alce::671__wikidata_simple__dev::p31]

Cited: alce::671__wikidata_simple__dev::p12, alce::671__wikidata_simple__dev::p3, alce::671__wikidata_simple__dev::p31

### `665__wikidata_simple__dev`
> **German submarine U-74**
> German submarine U-74 was a Type VIIB U-boat of Nazi Germany's Kriegsmarine during World War II. [alce::665__wikidata_simple__dev::p24]

Cited: alce::665__wikidata_simple__dev::p24

### `1334__wikidata_simple__dev`
> **Celebrity Solstice, Celebrity Equinox, Celebrity Eclipse, Celebrity Silhouette, and Celebrity Reflection**
> At present, there are five active 'Solstice'-class ships: the lead vessel of the class, 'Celebrity Solstice'; the second ship of the class, 'Celebrity Equinox'; and the third ship of the class, 'Celebrity Eclipse', which was delivered on 15 April 2010. [alce::1334__wikidata_simple__dev::p0]
> The fourth ship, 'Celebrity Silhouette', sailed on her Maiden Voyage on 23 July 2011; and the fifth, 'Celebrity Reflection', was launched in August 2012. [alce::1334__wikidata_simple__dev::p0]

Cited: alce::1334__wikidata_simple__dev::p0

### `145__wikidata_comp__dev`
> **Multiple directors directed TV shows with screenplays written by B. J. Novak: Ken Kwapis, Jeffrey Blitz, and Jason Reitman**
> "Sexual Harassment" was written by B. J. Novak, and the episode was directed by Ken Kwapis. [alce::145__wikidata_comp__dev::p32]
> "Counseling" was written by B. J. Novak, and the entry was directed by Jeffrey Blitz. [alce::145__wikidata_comp__dev::p2]
> "Local Ad" was written by B. J. Novak, and was the first episode directed by Jason Reitman. [alce::145__wikidata_comp__dev::p78]

Cited: alce::145__wikidata_comp__dev::p2, alce::145__wikidata_comp__dev::p32, alce::145__wikidata_comp__dev::p78

### `611__wikidata_simple__dev`
_Refused._

### `806__wikidata_simple__dev`
> **Museum of Fine Arts, Boston**
> Museum trustees decided to hire architect Guy Lowell to create a design for a museum that could be built in stages, as funding was obtained for each phase. [alce::806__wikidata_simple__dev::p22]
> The museum moved to its new location later that year on Huntington Avenue in Boston's Fenway-Kenmore neighborhood, near the recently-constructed mansion that would later become the Isabella Stewart Gardner Museum. [alce::806__wikidata_simple__dev::p22]

Cited: alce::806__wikidata_simple__dev::p22

### `224__wikidata_intersection__dev`
> **Hey Ram**
> Kamal Haasan wrote, directed, and starred in "Hey Ram" (2000) film about the Partition and the assassination of Gandhi. [alce::224__wikidata_intersection__dev::p0]

Cited: alce::224__wikidata_intersection__dev::p0

### `577__wikidata_simple__dev`
> **Multiple members including Clive Burr, Nicko McBrain, and Doug Sampson**
> Clive Burr was an English drummer who was a member of Iron Maiden from 1979 to 1982, playing on their first three records including 'Iron Maiden', 'Killers' and 'The Number of the Beast'. [alce::577__wikidata_simple__dev::p8]
> Nicko McBrain is an English musician and drummer of the British heavy metal band Iron Maiden, which he joined in 1982, debuting on their fourth album 'Piece of Mind' (1983), and has remained with them since. [alce::577__wikidata_simple__dev::p40]
> Doug Sampson was the drummer for Iron Maiden from 1978 to 1979. [alce::577__wikidata_simple__dev::p41]

Cited: alce::577__wikidata_simple__dev::p40, alce::577__wikidata_simple__dev::p41, alce::577__wikidata_simple__dev::p8

### `12__wikitables_composition__dev`
_Refused._

### `699__wikidata_simple__dev`
> **My Big Fat Greek Wedding**
> Nia Vardalos is a Canadian-American actress, screenwriter, and producer of Greek descent whose most notable work is the 2002 film 'My Big Fat Greek Wedding', which was based on a one-woman stage play she dramatized and in which she starred. [alce::699__wikidata_simple__dev::p4]
> 'My Big Fat Greek Wedding' is a 2002 romantic comedy film directed by Joel Zwick and written by Nia Vardalos, who also stars in the film. [alce::699__wikidata_simple__dev::p5]

Cited: alce::699__wikidata_simple__dev::p4, alce::699__wikidata_simple__dev::p5

### `285__wikidata_intersection__dev`
> **Arsenal F.C. competed in and won the Inter-Cities Fairs Cup (1970) and the Cup Winners' Cup (1994), among other competitions including FA Cups, League titles, and League Cups**
> Arsenal has won two European honours: the Inter-Cities Fairs Cup in 1970 and the Cup Winners' Cup in 1994. [alce::285__wikidata_intersection__dev::p3]
> The club has won 13 League titles, a record 13 FA Cups, two League Cups, the League Centenary Trophy, 15 FA Community Shields, one UEFA Cup Winners' Cup and one Inter-Cities Fairs Cup. [alce::285__wikidata_intersection__dev::p79]

Cited: alce::285__wikidata_intersection__dev::p3, alce::285__wikidata_intersection__dev::p79

### `891__wikidata_simple__dev`
> **Multiple competitions including the $100,000 event in Midland and the 2017 Empire Slovak Open doubles**
> Naomi Broady won the $100,000 event in Midland, beating US youngster Robin Anderson in the final. [alce::891__wikidata_simple__dev::p3]
> In May in the 2017 Empire Slovak Open, Broady, partnered by Heather Watson, won the doubles competition on clay in two sets. [alce::891__wikidata_simple__dev::p15]
> She won one singles title in April 2006 at the 'Sutton ITF Junior Tournament' as a junior player. [alce::891__wikidata_simple__dev::p0]

Cited: alce::891__wikidata_simple__dev::p0, alce::891__wikidata_simple__dev::p15, alce::891__wikidata_simple__dev::p3

### `804__wikidata_simple__dev`
> **Coasts (Queen Mary Coast and Knox Coast)**
> The Shackleton Ice Shelf separates the Queen Mary Coast to the west from the Knox Coast of Wilkes Land to the east. [alce::804__wikidata_simple__dev::p0]
> These coasts are land masses found adjacent to the Shackleton Ice Shelf. [alce::804__wikidata_simple__dev::p0]

Cited: alce::804__wikidata_simple__dev::p0

### `972__wikidata_comp__dev`
> **Multiple directors including William Dieterle, Edmund Heuberger, Ernst Laemmle, Henry Koster, and Norman Taurog**
> Joe Pasternak produced movies directed by William Dieterle, including 'The Brandenburg Arch' (1929), 'Triumph of Love' (1929), 'Silence in the Forest' (1929), 'Rustle of Spring' (1930), 'Ludwig II, King of Bavaria' (1930), and 'One Hour of Happiness' (1931). [alce::972__wikidata_comp__dev::p0]
> Pasternak also produced three films directed by Edmund Heuberger: 'Secret Police' (1929), 'Witnesses Wanted' (1930), and 'Of Life and Death' (1930). [alce::972__wikidata_comp__dev::p0]
> Pasternak produced 'The Daredevil Reporter' (1929), directed by Ernst Laemmle. [alce::972__wikidata_comp__dev::p0]
> Pasternak produced 'One Hundred Men and a Girl' (1937) directed by Koster and 'Mad About Music' (1938) directed by Norman Taurog. [alce::972__wikidata_comp__dev::p97]
> Henry Koster directed three films for Pasternak, including 'Catherine the Last', and later got a contract to work with Universal Pictures in Hollywood with Pasternak. [alce::972__wikidata_comp__dev::p62]

Cited: alce::972__wikidata_comp__dev::p0, alce::972__wikidata_comp__dev::p62, alce::972__wikidata_comp__dev::p97

### `642__wikidata_simple__dev`
> **The Carlyle Group is an American multinational private equity and financial services corporation that worked for various clients and investors**
> The Carlyle Group is an American multinational private equity, alternative asset management and financial services corporation that specializes in corporate private equity, real assets, global credit, and investment solutions. [alce::642__wikidata_simple__dev::p4]
> Carlyle invests across four segments – Corporate Private Equity, Real Assets, Global Market Strategies and Investment Solutions, serving as a global alternative asset manager. [alce::642__wikidata_simple__dev::p28]

Cited: alce::642__wikidata_simple__dev::p28, alce::642__wikidata_simple__dev::p4

### `1008__wikidata_comp__dev`
> **Multiple winners across different years: Jimmie Johnson (2013), David Ragan (2011), and Dale Earnhardt Jr. (2015)**
> Jimmie Johnson of Hendrick Motorsports won the 2013 Coke Zero 400 race, his fourth win of the season and his first Coke Zero 400 win. [alce::1008__wikidata_comp__dev::p0]
> The 2011 Coke Zero 400 race was won by David Ragan of Roush Fenway Racing, his first in the series. [alce::1008__wikidata_comp__dev::p3]
> Dale Earnhardt, Jr. won the 2015 Coke Zero 400 race, his second win of the season. [alce::1008__wikidata_comp__dev::p8]

Cited: alce::1008__wikidata_comp__dev::p0, alce::1008__wikidata_comp__dev::p3, alce::1008__wikidata_comp__dev::p8

### `930__wikidata_simple__dev`
> **The Builder (2010), New Jerusalem (2011), and The Mountain (2018)**
> Rick Alverson is an American film director and screenwriter. His first film, 'The Builder' (2010), featured co-writer Colm O'Leary in his debut performance as an Irish immigrant struggling to reconcile the American ideal and its manifestation in the real world. [alce::930__wikidata_simple__dev::p1]
> Premiering at Rotterdam Film Festival, 'New Jerusalem' (2011), his second feature, starred Colm. [alce::930__wikidata_simple__dev::p1]
> Alverson's fifth feature, 'The Mountain' (2018), premiered in competition at the 75th Venice International Film Festival and stars Tye Sheridan, Jeff Goldblum, Hannah Gross, Udo Kier and Denis Lavant. [alce::930__wikidata_simple__dev::p2]

Cited: alce::930__wikidata_simple__dev::p1, alce::930__wikidata_simple__dev::p2

### `62__wikitables_composition__dev`
> **Basilan is subdivided into 11 municipalities and two cities, including Isabela City, Lamitan, Tuburan, Tipo-Tipo, Sumisip, Maluso, and Lantawan**
> Basilan is subdivided into 11 municipalities and two cities. [alce::62__wikitables_composition__dev::p13]
> Isabela City is a component city and the capital of the province. [alce::62__wikitables_composition__dev::p13]
> The municipalities specified in the province were: Isabela, Lamitan, Tuburan, Tipo-Tipo, Sumisip, Maluso and Lantawan. [alce::62__wikitables_composition__dev::p2]

Cited: alce::62__wikitables_composition__dev::p13, alce::62__wikitables_composition__dev::p2

### `317__wikidata_comp__dev`
> **The Detroit Tigers emerged victorious in competitions they participated in, including winning the World Series championship**
> The Tigers led their division wire-to-wire, from opening day and every day thereafter, culminating in the World Series championship. [alce::317__wikidata_comp__dev::p41]
> In the 1907 World Series, the Chicago Cubs defeated the Detroit Tigers, winning the Series four games to none (with one tie). [alce::317__wikidata_comp__dev::p42]

Cited: alce::317__wikidata_comp__dev::p41, alce::317__wikidata_comp__dev::p42

### `902__wikidata_simple__dev`
> **The members of i☆Ris are: Saki Yamakita, Yū Serizawa, Himika Akaneya, Yūki Wakai, Miyu Kubota, and Azuki Shibuya**
> i☆Ris (pronounced "Iris", as in English) is a Japanese voice acting and singing female idol group, formed in 2012 by Avex. It consists of six members: Saki Yamakita, Yū Serizawa, Himika Akaneya, Yūki Wakai, Miyu Kubota, and Azuki Shibuya. [alce::902__wikidata_simple__dev::p0]
> The leader is Saki Yamakita. [alce::902__wikidata_simple__dev::p0]

Cited: alce::902__wikidata_simple__dev::p0

### `29__wikitables_composition__dev`
> **Papé Diakité**
> Papé Abdoulaye Diakite is a Senegalese football defender who signed for FC Edmonton in the North American Soccer League on 8 February 2016. [alce::29__wikitables_composition__dev::p21]
> After a strong 2016 season, Diakite was named the NASL's Young Player of the Year for the 2016 season. [alce::29__wikitables_composition__dev::p21]

Cited: alce::29__wikitables_composition__dev::p21

### `851__wikidata_simple__dev`
> **Musical works by Jason Robert Brown include "Parade," "The Bridges of Madison County," and "Songs for a New World"**
> Jason Robert Brown is an American musical theatre composer, lyricist, and playwright. [alce::851__wikidata_simple__dev::p1]
> He has won Tony Awards for his work on "Parade" and "The Bridges of Madison County". [alce::851__wikidata_simple__dev::p1]
> Songs for a New World is a work of musical theatre written and composed by Jason Robert Brown, originally produced Off-Broadway at the WPA Theatre in 1995. [alce::851__wikidata_simple__dev::p5]

Cited: alce::851__wikidata_simple__dev::p1, alce::851__wikidata_simple__dev::p5

### `719__wikidata_simple__dev`
> **El maleficio and El engaño**
> El maleficio is a Mexican telenovela produced by Ernesto Alonso for Televisa in 1983. [alce::719__wikidata_simple__dev::p18]
> El engaño is a Mexican telenovela produced by Ernesto Alonso for Televisa in 1986. [alce::719__wikidata_simple__dev::p29]

Cited: alce::719__wikidata_simple__dev::p18, alce::719__wikidata_simple__dev::p29

### `739__wikidata_simple__dev`
> **Moshe Kaplinsky, Dan Harel, and Yair Naveh**
> Maj. Gen. Moshe Kaplinsky was Deputy Chief of the General Staff of the Israel Defense Forces. [alce::739__wikidata_simple__dev::p51]
> Dan Harel is a retired general in the Israel Defense Forces and a former Deputy Chief of the General Staff. [alce::739__wikidata_simple__dev::p85]
> Yair Naveh is a Major General in the Israel Defense Forces and a former Deputy Chief of the General Staff. [alce::739__wikidata_simple__dev::p7]

Cited: alce::739__wikidata_simple__dev::p51, alce::739__wikidata_simple__dev::p7, alce::739__wikidata_simple__dev::p85

### `639__wikidata_simple__dev`
> **Television drama series**
> Kay Mellor is an English actress, scriptwriter, and director best known for her work on several successful television drama series. [alce::639__wikidata_simple__dev::p0, alce::639__wikidata_simple__dev::p2]

Cited: alce::639__wikidata_simple__dev::p0, alce::639__wikidata_simple__dev::p2

### `607__wikidata_simple__dev`
> **Eight toll facilities consisting of two toll roads, two tunnels, and four bridges**
> The Maryland Transportation Authority (MDTA) is an independent state agency responsible for financing, constructing, operating, and maintaining eight toll facilities, currently consisting of two toll roads, two tunnels, and four bridges in Maryland. [alce::607__wikidata_simple__dev::p0]

Cited: alce::607__wikidata_simple__dev::p0

### `897__wikidata_simple__dev`
> **David Pithey**
> David Pithey was a Rhodesian-born cricketer who represented South Africa. [alce::897__wikidata_simple__dev::p10]

Cited: alce::897__wikidata_simple__dev::p10

### `437__wikidata_intersection__dev`
> **Multiple films directed by Radha Mohan and produced by Prakash Raj**
> Radha Mohan is an Indian film director who has directed five films for Prakash Raj's Duet films: 'Azhagiya Theeye' (Tamil), 'Mozhi' (Tamil), 'Abhiyum Naanum' (Tamil), 'Payanam' (Tamil), 'Gaganam' (Telugu) and 'Gouravam' (Tamil/Telugu). [alce::437__wikidata_intersection__dev::p0]
> Prakash Raj is a close friend and producer of Radha Mohan's earlier ventures, and they have collaborated on multiple films. [alce::437__wikidata_intersection__dev::p11]

Cited: alce::437__wikidata_intersection__dev::p0, alce::437__wikidata_intersection__dev::p11

### `758__wikidata_simple__dev`
> **Jesus taught his disciples and the people living in Palestine**
> According to Ghulam Ahmad, Jesus taught the message of Jewish messianism to his disciples and to the people living in Palestine. [alce::758__wikidata_simple__dev::p55]

Cited: alce::758__wikidata_simple__dev::p55

### `599__wikidata_simple__dev`
> **U-1235, U-1230, U-842, and U-194 were classified as Type IXC/40**
> German submarine U-1235 was a Type IXC/40 U-boat of Nazi Germany's Kriegsmarine during World War II. [alce::599__wikidata_simple__dev::p21]
> German submarine U-1230 was a Type IXC/40 U-boat of Nazi Germany's Kriegsmarine during World War II. [alce::599__wikidata_simple__dev::p3]
> German submarine U-842 was a Type IXC/40 U-boat built for Nazi Germany's Kriegsmarine during World War II. [alce::599__wikidata_simple__dev::p28]
> German submarine U-194 was a Type IXC/40 U-boat of Nazi Germany's Kriegsmarine built during World War II. [alce::599__wikidata_simple__dev::p17]

Cited: alce::599__wikidata_simple__dev::p17, alce::599__wikidata_simple__dev::p21, alce::599__wikidata_simple__dev::p28, alce::599__wikidata_simple__dev::p3

### `927__wikidata_simple__dev`
> **The Mars Volta, At the Drive-In, Antemasque, and Zavalaz**
> He is best known as the lead singer and lyricist of the Grammy Award-winning progressive rock band The Mars Volta and the only constant member of the post-hardcore group At the Drive-In, for which he is the lead singer and occasional guitarist. [alce::927__wikidata_simple__dev::p1]
> He is also the lead singer of the band Antemasque, and sings and plays guitar in his band Zavalaz. [alce::927__wikidata_simple__dev::p1]

Cited: alce::927__wikidata_simple__dev::p1

### `834__wikidata_simple__dev`
> **Metro-North Railroad owns electric railcars (M2, M3A, M7A, and M8 models), diesel locomotives, and push-pull coaches**
> The Metro-North Railroad uses an electric fleet of M2, M3A, M7A, and M8 railcars. [alce::834__wikidata_simple__dev::p0]
> Multiple diesel locomotives and push-pull coaches are in use as well. [alce::834__wikidata_simple__dev::p0]
> Metro-North owned and marked equipment operated by NJ Transit can also be seen on other NJ Transit lines. [alce::834__wikidata_simple__dev::p0]

Cited: alce::834__wikidata_simple__dev::p0

### `815__wikidata_simple__dev`
> **Detroit Metal City**
> Studio 4°C produced the OVA series 'Detroit Metal City'. [alce::815__wikidata_simple__dev::p1]
> Studio 4°C also contributed animation work to 'ThunderCats', a series animated by Warner Bros. Animation and Studio 4°C. [alce::815__wikidata_simple__dev::p21]

Cited: alce::815__wikidata_simple__dev::p1, alce::815__wikidata_simple__dev::p21

### `174__wikidata_intersection__dev`
_Refused._

### `487__wikitables_simple__dev`
> **A text editor is a type of computer program that edits plain text**
> A text editor is a type of computer program that edits plain text. [alce::487__wikitables_simple__dev::p0]
> Text editors are provided with operating systems and software development packages, and can be used to change files such as configuration files, documentation files and programming language source code. [alce::487__wikitables_simple__dev::p0]
> A text editor is a program that is used for typing, copying, pasting, and printing text. [alce::487__wikitables_simple__dev::p19]

Cited: alce::487__wikitables_simple__dev::p0, alce::487__wikitables_simple__dev::p19

### `414__wikidata_comp__dev`
> **Medical device manufacturers, hospitals/NHS, courts and tribunals, and client companies employ consultants**
> Consultants and contractors are sometimes employed when introducing new quality practices and methods, particularly where the relevant skills and expertise are not available within the organization or when allocating the available internal resources are not available. [alce::414__wikidata_comp__dev::p80]
> In the United Kingdom, Republic of Ireland, and parts of the Commonwealth, consultants are senior hospital-based physicians or surgeons who may be employed as substantive consultants or as locum consultants by the NHS. [alce::414__wikidata_comp__dev::p38, alce::414__wikidata_comp__dev::p8]
> Employment consultants are expert witnesses who advise courts and tribunals on employment related issues. [alce::414__wikidata_comp__dev::p0]
> Consultants work with the clients of a company and are external to the client, providing a service to that company. [alce::414__wikidata_comp__dev::p3]

Cited: alce::414__wikidata_comp__dev::p0, alce::414__wikidata_comp__dev::p3, alce::414__wikidata_comp__dev::p38, alce::414__wikidata_comp__dev::p8, alce::414__wikidata_comp__dev::p80

### `460__wikidata_intersection__dev`
> **The Winds of War, War and Remembrance, Dark Shadows, The Night Stalker, The Night Strangler, Burnt Offerings, The Norliss Tapes, Dracula, Scream of the Wolf, The Turn of the Screw, The Great Ice Rip-Off, Trilogy of Terror, Dead of Night, Curse of the Black Widow, Trilogy of Terror II, and Me and the Kid**
> Bob Cobert is best known for his work with producer/director Dan Curtis, especially on the TV mini-series 'The Winds of War' (1983) and 'War and Remembrance' (1988). [alce::460__wikidata_intersection__dev::p1]
> His early work included composing the soap opera 'Dark Shadows' and the two tie-in films, and for composing the score for the 1972 TV movie 'The Night Stalker', together with 'The Night Strangler'. [alce::460__wikidata_intersection__dev::p1]
> Like most other Dan Curtis works, the music for 'Burnt Offerings' was composed and conducted by Robert Cobert. [alce::460__wikidata_intersection__dev::p2]
> His other scores include the horror film 'Burnt Offerings' (1976), the comedy film 'Me and the Kid' (1993), and the TV movies 'The Norliss Tapes' (1973), 'Dracula' (1973), 'Scream of the Wolf' (1974), 'The Turn of the Screw' (1974), 'The Great Ice Rip-Off' (1974), 'Trilogy of Terror' (1975), 'Dead of Night' (1977), 'Curse of the Black Widow' (1977) and 'Trilogy of Terror II' (1996). [alce::460__wikidata_intersection__dev::p3]

Cited: alce::460__wikidata_intersection__dev::p1, alce::460__wikidata_intersection__dev::p2, alce::460__wikidata_intersection__dev::p3

### `859__wikidata_simple__dev`
_Refused._

### `610__wikidata_simple__dev`
> **Keys**
> Key West National Wildlife Refuge contains several keys, which are landforms with only 2,019 acres (8.171 km) of land above sea level. [alce::610__wikidata_simple__dev::p0]
> These keys within the refuge are unpopulated and are designated as Wilderness within the Florida Keys Wilderness. [alce::610__wikidata_simple__dev::p0]

Cited: alce::610__wikidata_simple__dev::p0

### `278__wikidata_comp__dev`
_Refused._

### `743__wikidata_simple__dev`
_Refused._

### `948__wikidata_simple__dev`
> **What Dreams May Come (1998)**
> He signed on to direct "What Dreams May Come" (1998), after injecting the plot idea that gives the film its unusual painterly look. [alce::948__wikidata_simple__dev::p96]

Cited: alce::948__wikidata_simple__dev::p96

### `524__wikitables_simple__dev`
> **Fiction (literature and film)**
> Diseases, both real and fictional, play a significant role in fiction, with certain diseases like Huntington's disease and tuberculosis appearing in many books and films. [alce::524__wikitables_simple__dev::p0]
> Pandemic plagues threatening all human life, such as 'The Andromeda Strain', are among the many fictional diseases described in literature and film. [alce::524__wikitables_simple__dev::p0]
> Diseases, especially if infectious, have long been popular themes and plot devices in fiction, as exemplified by works like Daniel Defoe's 'A Journal of the Plague Year', Mary Shelley's 'The Last Man', and Edgar Allan Poe's 'The Masque of the Red Death'. [alce::524__wikitables_simple__dev::p3]

Cited: alce::524__wikitables_simple__dev::p0, alce::524__wikitables_simple__dev::p3

### `353__wikidata_comp__dev`
> **Arnold Leibovit**
> Arnold Leibovit wrote, directed, and produced the 1985 documentary film 'The Fantasy Film Worlds of George Pal', which is about Academy Award winning producer/director George Pal. [alce::353__wikidata_comp__dev::p0]
> Arnold Leibovit also wrote, produced, and directed 'The Puppetoon Movie', a 1987 animated film based on Puppetoon characters created by George Pal. [alce::353__wikidata_comp__dev::p3]

Cited: alce::353__wikidata_comp__dev::p0, alce::353__wikidata_comp__dev::p3

### `818__wikidata_simple__dev`
> **Seaborgium (chemical element), asteroid 4856 Seaborg, ten transuranium elements, and the actinide series arrangement**
> Glenn T. Seaborg was involved in the synthesis, discovery and investigation of ten transuranium elements. [alce::818__wikidata_simple__dev::p4]
> His work led to his development of the actinide concept and the arrangement of the actinide series in the periodic table of the elements. [alce::818__wikidata_simple__dev::p4]
> The chemical element Seaborgium was named after Seaborg, making it the first element ever to have been officially named after a living person. [alce::818__wikidata_simple__dev::p1, alce::818__wikidata_simple__dev::p22]
> The asteroid 4856 Seaborg was also named after him. [alce::818__wikidata_simple__dev::p22]

Cited: alce::818__wikidata_simple__dev::p1, alce::818__wikidata_simple__dev::p22, alce::818__wikidata_simple__dev::p4

### `403__wikidata_intersection__dev`
> **Richard Stoehr**
> Richard Stoehr was hired by the Curtis Institute of Music in Philadelphia initially as music librarian and subsequently to teach courses in theory and composition. [alce::403__wikidata_intersection__dev::p65]
> Singer began attending the Juilliard School in 1927, studying with Leopold Auer, Paul Kochanski, and Rubin Goldmark, and graduated from Juilliard in 1930. [alce::403__wikidata_intersection__dev::p32]

Cited: alce::403__wikidata_intersection__dev::p32, alce::403__wikidata_intersection__dev::p65

### `387__wikidata_intersection__dev`
> **Asuravithu**
> Asuravithu is a 1968 Malayalam film directed by A. Vincent and starring Prem Nazir and Sharada. [alce::387__wikidata_intersection__dev::p41]
> The music was composed by G. Devarajan and lyrics was written by Vayalar Ramavarma. [alce::387__wikidata_intersection__dev::p65]

Cited: alce::387__wikidata_intersection__dev::p41, alce::387__wikidata_intersection__dev::p65

### `360__wikidata_intersection__dev`
> **L. H. Sumanadasa and J. B. Disanayake**
> L. H. Sumanadasa was educated at Ananda College, Colombo and completed his BSc degree in Physics at Ceylon University College. [alce::360__wikidata_intersection__dev::p69]
> J. B. Disanayake received secondary education at Ananda College and graduated from the University of Ceylon, Peradeniya campus in 1961. [alce::360__wikidata_intersection__dev::p81]

Cited: alce::360__wikidata_intersection__dev::p69, alce::360__wikidata_intersection__dev::p81

### `1012__wikidata_comp__dev`
> **Melbourne**
> Collingwood won the 1941 VFL Lightning Premiership competition by 1 point, defeating Melbourne in the final. [alce::1012__wikidata_comp__dev::p53]

Cited: alce::1012__wikidata_comp__dev::p53

### `1002__wikidata_comp__dev`
> **Strasbourg, France and Rhodes, Greece**
> The Roman Catholic Archdiocese of Strasbourg is a non-metropolitan archdiocese of the Latin Rite of the Catholic Church in France. [alce::1002__wikidata_comp__dev::p72]
> The Roman Catholic Archdiocese of Rhodes is an exempt, non-Metropolitan archdiocese with its cathedral see at the St. Francis of Assisi Cathedral in the eponymous capital of the island of Rhodes in Greece. [alce::1002__wikidata_comp__dev::p18]

Cited: alce::1002__wikidata_comp__dev::p18, alce::1002__wikidata_comp__dev::p72

### `234__wikidata_intersection__dev`
> **The sources do not specify a single movie, but indicate K. S. L. Swamy and Vijaya Bhaskar worked together on multiple films**
> Vijaya Bhaskar was a part of all of popular Kannada film director KSL Swamy's movies [alce::234__wikidata_intersection__dev::p0]

Cited: alce::234__wikidata_intersection__dev::p0

### `555__wikidata_simple__dev`
> **Non-Summit and Please Take Care of My Refrigerator**
> Popular JTBC programs such as 'Non-Summit' and 'Please Take Care of My Refrigerator' are broadcast around the world through the sale of broadcast rights to overseas networks. [alce::555__wikidata_simple__dev::p0]

Cited: alce::555__wikidata_simple__dev::p0

### `449__wikidata_intersection__dev`
_Refused._

### `893__wikidata_simple__dev`
> **Where the Wild Things Are**
> Maurice Sendak was an American illustrator and writer of children's books who became widely known for his book "Where the Wild Things Are", first published in 1963. [alce::893__wikidata_simple__dev::p0]
> Sendak won the Caldecott Medal in 1964 for "Where the Wild Things Are", which he both authored and illustrated. [alce::893__wikidata_simple__dev::p11]

Cited: alce::893__wikidata_simple__dev::p0, alce::893__wikidata_simple__dev::p11

### `633__wikidata_simple__dev`
> **Approximately 28 million Filipinos spoke Filipino/Tagalog as their mother tongue**
> As of 2007, Tagalog is the first language of 28 million people, or about one-third of the Philippine population. [alce::633__wikidata_simple__dev::p1, alce::633__wikidata_simple__dev::p4]
> Filipino is a standardized variety of the Tagalog language and is the national language of the Philippines. [alce::633__wikidata_simple__dev::p1]
> 22 million, or 28% of the total Philippine population, speak it as a native language. [alce::633__wikidata_simple__dev::p6]

Cited: alce::633__wikidata_simple__dev::p1, alce::633__wikidata_simple__dev::p4, alce::633__wikidata_simple__dev::p6

### `935__wikidata_simple__dev`
> **Multiple books including The Chronicles of Narnia, Farmer Giles of Ham, The Adventures of Tom Bombadil, and others**
> Pauline Baynes was an English illustrator whose work encompassed more than 100 books, notably several by C. S. Lewis and J. R. R. Tolkien. [alce::935__wikidata_simple__dev::p1]
> Baynes is probably best known for her covers and interior illustrations for The Chronicles of Narnia by C. S. Lewis, seven books published, one volume a year, from 1950 to 1956. [alce::935__wikidata_simple__dev::p2]
> Drawings by Baynes appeared in Farmer Giles of Ham, The Adventures of Tom Bombadil, Smith of Wootton Major, Tree and Leaf, and Bilbo's Last Song. [alce::935__wikidata_simple__dev::p8]
> Baynes illustrated A Dictionary of Chivalry (1968) and The Borrowers Avenged by Mary Norton (1982). [alce::935__wikidata_simple__dev::p3]

Cited: alce::935__wikidata_simple__dev::p1, alce::935__wikidata_simple__dev::p2, alce::935__wikidata_simple__dev::p3, alce::935__wikidata_simple__dev::p8

### `253__wikidata_comp__dev`
> **Herbert Kline and Alexander Hammid**
> The Forgotten Village is a 1941 American documentary film directed by Herbert Kline and Alexander Hammid. The film was written by John Steinbeck. [alce::253__wikidata_comp__dev::p16]

Cited: alce::253__wikidata_comp__dev::p16

### `951__wikidata_comp__dev`
_Refused._

### `498__wikitables_simple__dev`
> **Notable mailing list software programs include GNU Mailman, LISTSERV, Majordomo, qmail's ezmlm, Hypermail, MHonArc, and FUDforum**
> Some popular free software programs for collecting mailing list archives are Hypermail, MHonArc, and FUDforum. [alce::498__wikitables_simple__dev::p1]
> Modern mailing list management programs include GNU Mailman, LISTSERV, Majordomo, and qmail's ezmlm. [alce::498__wikitables_simple__dev::p59]
> LISTSERV is mailing list software that allows a sender to send one email to the list, and then transparently sends it on to the addresses of the subscribers to the list. [alce::498__wikitables_simple__dev::p7]

Cited: alce::498__wikitables_simple__dev::p1, alce::498__wikitables_simple__dev::p59, alce::498__wikitables_simple__dev::p7

### `374__wikidata_intersection__dev`
> **Jack Nicklaus won five PGA Championships: 1963, 1971, 1973, 1980, and one other**
> Jack Nicklaus won the first of his five PGA Championship titles at the 1963 PGA Championship, played July 18–21 at the Blue Course of Dallas Athletic Club in Dallas, Texas. [alce::374__wikidata_intersection__dev::p2]
> Jack Nicklaus won the second of his five PGA Championships at the 1971 PGA Championship, played February 25–28 at the original PGA National Golf Club in Palm Beach Gardens, Florida. [alce::374__wikidata_intersection__dev::p5]
> Jack Nicklaus won the third of his five PGA Championships at the 1973 PGA Championship, played August 9–12 at Canterbury Golf Club in Beachwood, Ohio. [alce::374__wikidata_intersection__dev::p0]
> Jack Nicklaus won his fifth PGA Championship at the 1980 PGA Championship, held August 7–10 at the East Course of Oak Hill Country Club in Rochester, New York. [alce::374__wikidata_intersection__dev::p7]

Cited: alce::374__wikidata_intersection__dev::p0, alce::374__wikidata_intersection__dev::p2, alce::374__wikidata_intersection__dev::p5, alce::374__wikidata_intersection__dev::p7

### `721__wikidata_simple__dev`
> **Multiple sporting events are partnered with Betfred, including the Scottish League Cup (Betfred Cup), Rugby League's Super League, the Cheltenham Gold Cup, World Snooker Championships, and various horse racing events**
> In May 2016, it was announced that Betfred would take over sponsorship of the Scottish League Cup for three years, rebranding it the Betfred Cup. [alce::721__wikidata_simple__dev::p2]
> In October 2016, Betfred began a three year period as the main sponsor of Rugby League's Super League, the northern hemisphere's premier Rugby League competition with twelve teams spread across England, and Catalans Dragons based in Perpignan, France. [alce::721__wikidata_simple__dev::p0]
> Betfred also sponsored the most prestigious jumps race the Cheltenham Gold Cup between the years of 2012 and 2015. [alce::721__wikidata_simple__dev::p0]
> Betfred sponsored the World Snooker Championships from 2009 to 2012, before losing the sponsorship rights. [alce::721__wikidata_simple__dev::p0]
> Betfred is one of the largest sponsors of horse racing in the United Kingdom, with races spread across racecourses in the country, including the Midlands National run at Uttoxeter Racecourse, the Dante Stakes and Ebor Handicap both at York Racecourse and the Betfred Cesarewitch on the Rowley Mile course at Newmarket. [alce::721__wikidata_simple__dev::p1]

Cited: alce::721__wikidata_simple__dev::p0, alce::721__wikidata_simple__dev::p1, alce::721__wikidata_simple__dev::p2

### `377__wikidata_comp__dev`
> **Multiple directors worked on films Richard Gordon produced, including Spencer Gordon Bennet, Frank McDonald, and Edward Bernds**
> Gordon worked with a new director, Spencer Gordon Bennet, on the war film, 'Submarine Seahawk' (1958). [alce::377__wikidata_comp__dev::p38]
> Gordon produced 'The Atomic Submarine' (1959) for Allied Artists, directed by Bennett. [alce::377__wikidata_comp__dev::p38]
> He wrote and produced 'The Underwater City' (1962), directed by Frank McDonald. [alce::377__wikidata_comp__dev::p38]
> His last feature film credits were two Westerns directed by Bennett, 'Requiem for a Gunfighter' (1965) and 'The Bounty Killer' (1965). [alce::377__wikidata_comp__dev::p38]
> Gordon helped with the casting on 'Reform School Girl' (1957) directed by Edward Bernds. [alce::377__wikidata_comp__dev::p38]

Cited: alce::377__wikidata_comp__dev::p38

### `587__wikidata_simple__dev`
_Refused._

### `741__wikidata_simple__dev`
_Refused._

### `707__wikidata_simple__dev`
> **Martha Graham choreographed multiple dances, including Lamentation and Columbiad**
> Lamentation is a modern dance solo choreographed by Martha Graham to Zoltán Kodály's 1910 'Piano Piece, Op. 3, No. 2', which premiered on January 8, 1930 at Maxine Elliott's Theatre in New York City. [alce::707__wikidata_simple__dev::p33]
> Columbiad is a solo modern dance choreographed by Martha Graham to music by Louis Horst. [alce::707__wikidata_simple__dev::p9]

Cited: alce::707__wikidata_simple__dev::p33, alce::707__wikidata_simple__dev::p9

### `293__wikidata_intersection__dev`
> **Kadavul Mama**
> The last collaboration was 'Kadavul Mama' (1974) before the demise of Panthulu, where B. R. Panthulu worked with T. G. Lingappa. [alce::293__wikidata_intersection__dev::p83]
> T. G. Lingappa continued working with Panthulu in many more Kannada films till the early 1970s. [alce::293__wikidata_intersection__dev::p83]

Cited: alce::293__wikidata_intersection__dev::p83

### `773__wikidata_simple__dev`
> **Pride of Baltimore II**
> The Inner Harbor also is the home port of 'Pride of Baltimore II', the state of Maryland's 'goodwill ambassador' ship, a reconstruction of a famous Baltimore Clipper ship. [alce::773__wikidata_simple__dev::p13]

Cited: alce::773__wikidata_simple__dev::p13

### `212__wikidata_comp__dev`
> **Princeton University**
> Debra Ann Livingston is a United States Circuit Judge of the United States Court of Appeals for the Second Circuit who received a Bachelor of Arts degree, magna cum laude, from the Woodrow Wilson School of Public and International Affairs at Princeton University in 1980. [alce::212__wikidata_comp__dev::p86]

Cited: alce::212__wikidata_comp__dev::p86

### `195__wikidata_intersection__dev`
> **The United States Grand Prix**
> Schumacher won the United States Grand Prix, his fourth consecutive victory at Indianapolis and fifth career victory there, and the French Grand Prix. [alce::195__wikidata_intersection__dev::p70]

Cited: alce::195__wikidata_intersection__dev::p70

### `283__wikidata_intersection__dev`
> **In Broad Daylight**
> In Broad Daylight is a 1971 American TV film starring Richard Boone, Stella Stevens and Suzanne Pleshette. It was directed by Robert Day and written by Larry Cohen. [alce::283__wikidata_intersection__dev::p84]

Cited: alce::283__wikidata_intersection__dev::p84

### `569__wikidata_simple__dev`
> **Multiple works including "Gods for Future Religions: Surreal Sculpture", "The Free Thinker", and "A Novel Romance"**
> Fred Baron published his second book, 'Gods for Future Religions: Surreal Sculpture', in 2012. [alce::569__wikidata_simple__dev::p7]
> Baron's surrealistic bronze, 'The Free Thinker,' is on permanent display at Baltimore's American Visionary Art Museum. [alce::569__wikidata_simple__dev::p8]
> Baron has a permanent public art sculpture, 'A Novel Romance', at the El Paso Public Library. [alce::569__wikidata_simple__dev::p8]

Cited: alce::569__wikidata_simple__dev::p7, alce::569__wikidata_simple__dev::p8

### `675__wikidata_simple__dev`
> **Multiple bomb attack victims from different incidents**
> Victims of a bombing in Austin included six adults who were killed in the attack, with individuals such as Smith, Kirkpatrick, Knapp, Macko, Mercado, and DiGiovanni being in the vicinity at the time of the bombing. [alce::675__wikidata_simple__dev::p15]
> Muslim victims were killed in blasts, with the blast near the RS Puram police station causing 12 casualties, and most victims being youth who were participants in Advani's rally. [alce::675__wikidata_simple__dev::p0]
> Victims of a bombing in Northern Ireland included people of many backgrounds and ages: Protestants, Catholics, six teenagers, six children, a mother pregnant with twins, two Spanish tourists, and others on a day trip from the Republic of Ireland. [alce::675__wikidata_simple__dev::p3]
> Six women and three men were murdered in an attack, with seven dying immediately and two dying of their wounds in the following weeks, including Israelis, Arabs, four Americans and three South Koreans among the approximately 100 injured. [alce::675__wikidata_simple__dev::p1]
> Victims of bombings ranged from 20 to 60 years old with an average age of 34, including 32 British nationals and victims from Afghanistan, France, Ghana, Grenada, India, Iran, Israel, Italy, Kenya, Mauritius, New Zealand, Nigeria, Romania, Sri Lanka, Turkey, Poland, Australia, and Vietnam. [alce::675__wikidata_simple__dev::p2]

Cited: alce::675__wikidata_simple__dev::p0, alce::675__wikidata_simple__dev::p1, alce::675__wikidata_simple__dev::p15, alce::675__wikidata_simple__dev::p2, alce::675__wikidata_simple__dev::p3

### `1351__wikidata_simple__dev`
> **Harry's Law**
> Kelley was the creator and executive producer of "Harry's Law", which premiered on NBC on January 17, 2011. [alce::1351__wikidata_simple__dev::p10]

Cited: alce::1351__wikidata_simple__dev::p10

### `14__wikitables_composition__dev`
> **Merthyr Tydfil**
> There are 22 principal areas in Wales, with eleven styled as county boroughs. [alce::14__wikitables_composition__dev::p38]
> Merthyr Tydfil County Borough is one of the Principal Areas of Wales. [alce::14__wikitables_composition__dev::p83]

Cited: alce::14__wikitables_composition__dev::p38, alce::14__wikitables_composition__dev::p83

### `461__wikidata_intersection__dev`
> **Nevada City**
> James R. Webb did a series of films starring Roy Rogers and directed by Joseph Kane, including 'Nevada City' (1941) and 'Bad Man of Deadwood'. [alce::461__wikidata_intersection__dev::p0]

Cited: alce::461__wikidata_intersection__dev::p0

### `903__wikidata_simple__dev`
> **Comets and minor planets**
> R. Scott Dunbar is an American astronomer, planetologist and discoverer of comets and minor planets. [alce::903__wikidata_simple__dev::p1]
> His most notable discoveries include the potentially hazardous object and Aten asteroid 3362 Khufu, which he co-discovered with Maria A. Barucci, as well as the near-Earth object, Mars-crosser and Aten asteroid, 3551 Verenia. [alce::903__wikidata_simple__dev::p1]
> Together with Eleanor Helin he co-discovered the minor planets 3360 Syrinx, 6065 Chesneau, 6435 Daveross and 7163 Barenboim. [alce::903__wikidata_simple__dev::p1]

Cited: alce::903__wikidata_simple__dev::p1

### `325__wikidata_intersection__dev`
> **Belli Moda**
> Puttanna Kanagal became an independent Director with Bellimoda, and Vijaya Bhaskar was the music director for 'Belli Moda'. [alce::325__wikidata_intersection__dev::p10]
> The film became an instant success and cemented their association between Vijaya Bhaskar and Puttanna Kanagal. [alce::325__wikidata_intersection__dev::p10]

Cited: alce::325__wikidata_intersection__dev::p10

### `58__wikitables_composition__dev`
_Refused._

### `916__wikidata_simple__dev`
> **Asianet was the first private TV channel to broadcast in Malayalam**
> Asianet is the first and biggest private television channel in the state. It started functioning from Thiruvananthapuram in 1993. [alce::916__wikidata_simple__dev::p1]
> Asianet, is an Indian general channel broadcasting in Malayalam language, headquartered in Thiruvananthapuram, Kerala. [alce::916__wikidata_simple__dev::p8]
> Asianet (1993), the first privately owned satellite channel broadcasting in Malayalam. [alce::916__wikidata_simple__dev::p9]

Cited: alce::916__wikidata_simple__dev::p1, alce::916__wikidata_simple__dev::p8, alce::916__wikidata_simple__dev::p9

### `919__wikidata_simple__dev`
> **Trucks and trailers**
> Saipa Diesel Company, originally branded Iran Kaveh, is an Iranian-based manufacturer of trucks and trailers. [alce::919__wikidata_simple__dev::p0]
> SAIPA also manufactures the Citroen C5 and the New C5, as well as the Renault Tondar 90 and Renault Logan. [alce::919__wikidata_simple__dev::p8]
> In 1975 Saipa began manufacturing licensed versions of the original Renault 5 and later the Renault 21. [alce::919__wikidata_simple__dev::p1]

Cited: alce::919__wikidata_simple__dev::p0, alce::919__wikidata_simple__dev::p1, alce::919__wikidata_simple__dev::p8

### `723__wikidata_simple__dev`
> **Choral symphonies cited in sources: Beethoven's Ninth Symphony, Berlioz's Roméo et Juliette, Holst's Choral Symphony, and Dyson's Psalm CVII Symphony**
> The direct antecedent for the choral symphony is Ludwig van Beethoven's Ninth Symphony, which incorporates part of the 'Ode an die Freude' ('Ode to Joy') with text sung by soloists and chorus in the last movement. [alce::723__wikidata_simple__dev::p0]
> Hector Berlioz described his 'Roméo et Juliette' as a choral symphony in his five-paragraph introduction to that work. [alce::723__wikidata_simple__dev::p0]
> Gustav Holst's Choral Symphony is a work for soprano soloist, chorus, and orchestra in a setting of verses by John Keats, written in 1923–24 and premiered in Leeds Town Hall on October 7, 1925. [alce::723__wikidata_simple__dev::p3]
> George Dyson's Psalm CVII Symphony and Overture is a choral symphony written in 1910 as part of the composer's studies at Oxford for his Doctorate in Music. [alce::723__wikidata_simple__dev::p18]

Cited: alce::723__wikidata_simple__dev::p0, alce::723__wikidata_simple__dev::p18, alce::723__wikidata_simple__dev::p3

### `628__wikidata_simple__dev`
> **Inhabitants of Guam (Guamanians)**
> The inhabitants of Guam are called Guamanians, and they are American citizens by birth. [alce::628__wikidata_simple__dev::p1]
> The Immigration and Nationality Act of 1952 expanded the definition of the 'United States' for nationality purposes to include Guam, therefore those born on Guam are 'U.S. citizens at birth on the same terms as persons born in other parts of the United States.' [alce::628__wikidata_simple__dev::p15]

Cited: alce::628__wikidata_simple__dev::p1, alce::628__wikidata_simple__dev::p15

### `379__wikidata_intersection__dev`
> **Inception**
> Syncopy Inc. is a British film production company founded by Christopher Nolan and his wife Emma Thomas. [alce::379__wikidata_intersection__dev::p0]
> Christopher Nolan has co-written several of his films with his brother Jonathan, and runs the production company Syncopy Inc. with his wife Emma Thomas. [alce::379__wikidata_intersection__dev::p21]
> Syncopy produced 'Inception' (2010), directed by Christopher Nolan. [alce::379__wikidata_intersection__dev::p0]

Cited: alce::379__wikidata_intersection__dev::p0, alce::379__wikidata_intersection__dev::p21

### `654__wikidata_simple__dev`
> **Rijndael cipher and Keccak cryptographic hash**
> Joan Daemen is a Belgian cryptographer who co-designed the Rijndael cipher with Vincent Rijmen, which was selected as the Advanced Encryption Standard (AES) in 2001. [alce::654__wikidata_simple__dev::p1]
> He co-designed the Keccak cryptographic hash, which was selected as the new SHA-3 hash by NIST in October 2012. [alce::654__wikidata_simple__dev::p1]

Cited: alce::654__wikidata_simple__dev::p1

### `714__wikidata_simple__dev`
> **Multiple aircraft including the Felixstowe F5L, Felixstowe F.4 Fury, and Felixstowe Porte Baby**
> The twin-engine F5L was one of the Felixstowe F series of flying boats developed by John Cyril Porte at the Seaplane Experimental Station, Felixstowe, England, during the First World War. [alce::714__wikidata_simple__dev::p69]
> The Felixstowe F.4 Fury, also known as the Porte Super-Baby, was a large British, five-engined triplane flying-boat designed by John Cyril Porte at the Seaplane Experimental Station, Felixstowe. [alce::714__wikidata_simple__dev::p60]
> The Felixstowe Porte Baby was a British reconnaissance flying boat of the First World War, first flying in 1915, designed by John Cyril Porte RN at the naval air station, Felixstowe. [alce::714__wikidata_simple__dev::p38]

Cited: alce::714__wikidata_simple__dev::p38, alce::714__wikidata_simple__dev::p60, alce::714__wikidata_simple__dev::p69

### `338__wikidata_intersection__dev`
> **Manahan**
> He graduated from the Manhattan School of Music with a Bachelor of Music degree in 1973 and a Master of Music degree in 1976. [alce::338__wikidata_intersection__dev::p1]
> The Juilliard School awarded him a fellowship as Assistant Conductor with the American Opera Center. [alce::338__wikidata_intersection__dev::p1]

Cited: alce::338__wikidata_intersection__dev::p1

### `1352__wikidata_simple__dev`
> **City Bridges and properties with extensive property portfolio**
> It was originally established to maintain London Bridge and, subsequently, other bridges. [alce::1352__wikidata_simple__dev::p1]
> The Fund administered by the Bridge House Estates is solely responsible for the five City Bridges. [alce::1352__wikidata_simple__dev::p0]
> Funded by bridge tolls and charitable donations, the trust acquired an extensive property portfolio which made it more than self-sufficient. [alce::1352__wikidata_simple__dev::p1]

Cited: alce::1352__wikidata_simple__dev::p0, alce::1352__wikidata_simple__dev::p1

### `196__wikidata_intersection__dev`
> **The Man Who Wasn't There**
> The Man Who Wasn't There is a 2001 British-American neo-noir crime film written, produced and directed by Joel and Ethan Coen. [alce::196__wikidata_intersection__dev::p27]
> Until 'The Ladykillers' (2004), Joel received sole credit for directing and Ethan for producing, meaning Ethan Coen produced films that Joel Coen directed. [alce::196__wikidata_intersection__dev::p0]

Cited: alce::196__wikidata_intersection__dev::p0, alce::196__wikidata_intersection__dev::p27

### `289__wikidata_comp__dev`
_Refused._

### `1000__wikidata_comp__dev`
> **Multiple winners across different years: Jeff Gordon (1996), Geoff Bodine (1994), and Mark Martin (another year)**
> The 1996 Tyson Holly Farms 400 was won by Jeff Gordon of the Hendrick Motorsports team after he started from second position. [alce::1000__wikidata_comp__dev::p2]
> In 1994, Geoff Bodine won the Tyson Holly Farms 400 by one lap over Terry Labonte. [alce::1000__wikidata_comp__dev::p12]
> Mark Martin picked up his second win at the track in the Tyson Holly Farms 400. [alce::1000__wikidata_comp__dev::p8]

Cited: alce::1000__wikidata_comp__dev::p12, alce::1000__wikidata_comp__dev::p2, alce::1000__wikidata_comp__dev::p8

### `965__wikidata_comp__dev`
> **Multiple institutions including The King's School Canterbury, King's College Cambridge, New College Oxford, Wells Theological College, Eton College, Trinity College Cambridge, Cranmer Hall Durham, and Durham University**
> John Paul Burbridge was the Dean of Norwich in the latter part of the 20th century (1983-1995) and was educated at The King's School, Canterbury and King's College, Cambridge, New College, Oxford, and Wells Theological College. [alce::965__wikidata_comp__dev::p2]
> George Pellew, who was Dean of Norwich, was educated at Eton College, before studying at Trinity College, Cambridge, obtaining a Bachelor of Arts degree in 1850. [alce::965__wikidata_comp__dev::p9]
> Jane Hedges, the current Dean of Norwich, trained for ministry at Cranmer Hall, Durham in 1978 and had previously completed a General Arts degree at Durham University. [alce::965__wikidata_comp__dev::p20, alce::965__wikidata_comp__dev::p30]

Cited: alce::965__wikidata_comp__dev::p2, alce::965__wikidata_comp__dev::p20, alce::965__wikidata_comp__dev::p30, alce::965__wikidata_comp__dev::p9

### `333__wikidata_intersection__dev`
> **The Prestige**
> Christopher Nolan directed, co-wrote, and produced 'The Prestige' (2006), an adaptation of the Christopher Priest novel about two rival 19th-century magicians. [alce::333__wikidata_intersection__dev::p1]

Cited: alce::333__wikidata_intersection__dev::p1

### `281__wikidata_intersection__dev`
> **Jackson**
> Jackson attended public schools in the Bedford-Stuyvesant neighborhood of Brooklyn, culminating with Stuyvesant High School, before leaving for college. [alce::281__wikidata_intersection__dev::p93]
> Jackson went on to obtain a JD at Brooklyn Law School, where he studied as a night student, and graduated in 1969. [alce::281__wikidata_intersection__dev::p93]

Cited: alce::281__wikidata_intersection__dev::p93

### `539__wikitables_simple__dev`
> **Notable diamonds include the Golden Jubilee Diamond, the Great Chrysanthemum, Golconda Diamonds, and the Cullinan I**
> The Golden Jubilee Diamond is the largest cut and faceted diamond in the world, weighing 545.67 carats (109.13 g). [alce::539__wikitables_simple__dev::p77]
> The Great Chrysanthemum, considered one of the most famous diamonds in the world, is the 2nd largest pear-shaped brown diamond and was discovered in 1963 at the Kimberley Mines in South Africa, weighing 198 carats. [alce::539__wikitables_simple__dev::p7]
> Some of the most famous diamonds from Golconda are notable, with the top four pink diamonds of the world coming from Golconda, and several monarchs and legendary personalities keeping them as a mark of pride. [alce::539__wikitables_simple__dev::p37]
> Cullinan I, also known as the Great Star of Africa, held the title of the largest cut and faceted diamond since 1908. [alce::539__wikitables_simple__dev::p77]

Cited: alce::539__wikitables_simple__dev::p37, alce::539__wikitables_simple__dev::p7, alce::539__wikitables_simple__dev::p77

### `52__wikitables_composition__dev`
> **KXLG**
> KXLG (99.1 FM) is a radio station serving the Watertown, South Dakota area (licensed to serve Milbank, South Dakota). [alce::52__wikitables_composition__dev::p1]

Cited: alce::52__wikitables_composition__dev::p1

### `80__wikitables_composition__dev`
> **Russian cities and towns in Komi Republic include Syktyvkar, Usinsk, and Sosnogorsk**
> Syktyvkar is the capital city of the Komi Republic, Russia. [alce::80__wikitables_composition__dev::p10]
> Usinsk is a town in the Komi Republic, Russia, located east of the republic's capital city of Syktyvkar. [alce::80__wikitables_composition__dev::p13]
> Sosnogorsk is a town in the Komi Republic, Russia, located on the Izhma River. [alce::80__wikitables_composition__dev::p52]

Cited: alce::80__wikitables_composition__dev::p10, alce::80__wikitables_composition__dev::p13, alce::80__wikitables_composition__dev::p52

### `310__wikidata_intersection__dev`
> **Premier League, FA Cup, League Cup, UEFA Cup, UEFA Europa League, European Cup Winners Cup, Intertoto Cup**
> West Ham United competed in the FA Premier League during the 2005–06 season, and the Premier League is their primary domestic competition. [alce::310__wikidata_intersection__dev::p42, alce::310__wikidata_intersection__dev::p86]
> Both clubs have competed in the UEFA Cup and UEFA Europa League. [alce::310__wikidata_intersection__dev::p0]
> West Ham United took part in the FA Cup and League Cup in the 2016–17 season. [alce::310__wikidata_intersection__dev::p45]
> West Ham United won the European Cup Winners Cup in 1965 and the Intertoto Cup in 1999. [alce::310__wikidata_intersection__dev::p0]

Cited: alce::310__wikidata_intersection__dev::p0, alce::310__wikidata_intersection__dev::p42, alce::310__wikidata_intersection__dev::p45, alce::310__wikidata_intersection__dev::p86

### `657__wikidata_simple__dev`
> **Cliffs and blanket bog**
> Runde is famous for its enormous number of birds, with about 500,000 to 700,000 seabirds inhabiting the island, most of them found in the cliffs. [alce::657__wikidata_simple__dev::p2]
> The Goksøyr Mires Nature Reserve is located on the island of Runde and encompasses a bog area with blanket bog, a bog type that was common in coastal areas. [alce::657__wikidata_simple__dev::p5]

Cited: alce::657__wikidata_simple__dev::p2, alce::657__wikidata_simple__dev::p5

### `429__wikidata_intersection__dev`
> **Central Branch**
> The Central Branch is a rail line owned and operated by the Long Island Rail Road (LIRR) in the U.S. state of New York, extending from just east of Bethpage station to just west of Babylon station. [alce::429__wikidata_intersection__dev::p66]
> It was built in 1873 as part of the Babylon Extension of the Central Railroad of Long Island (CRRLI), which was owned by Alexander Turney Stewart. [alce::429__wikidata_intersection__dev::p66]
> The branch was mostly unused following the 1876 merger of the CRRLI and the LIRR, but in 1925 it was rebuilt and reconfigured to connect Bethpage and Babylon stations. [alce::429__wikidata_intersection__dev::p66]

Cited: alce::429__wikidata_intersection__dev::p66

### `508__wikitables_simple__dev`
> **Deep Lens Survey (DLS) - seven 4 square degree fields**
> The Deep Lens Survey (DLS, short for 'Deep Gravitational Lensing Survey') is an ultra-deep multi-band optical survey of seven 4 square degree fields. [alce::508__wikitables_simple__dev::p16]
> The deep fields took five years to complete (2001–2006), in four bands: B, V, R, and z', to 29/29/29/28 mag per square arcsecond surface brightness. [alce::508__wikitables_simple__dev::p16]

Cited: alce::508__wikitables_simple__dev::p16

### `936__wikidata_simple__dev`
> **Admiral Piett**
> Admiral Firmus Piett is a fictional character from the Star Wars franchise, first introduced and portrayed by Kenneth Colley in the 1980 film The Empire Strikes Back. [alce::936__wikidata_simple__dev::p14]

Cited: alce::936__wikidata_simple__dev::p14

### `362__wikidata_comp__dev`
> **The Federal Government of the United States (through the MITRE Corporation and sponsors including the Department of Defense, Department of Energy, and U.S. Intelligence Community)**
> For administrative purposes, JASON's activities are run through the MITRE Corporation, a non-profit corporation in McLean, Virginia, which operates seven Federally Funded Research and Development Centers (FFRDCs) for the Federal Government of the United States. [alce::362__wikidata_comp__dev::p1]
> Its sponsors include the Department of Defense, the Department of Energy, and the U.S. Intelligence Community. [alce::362__wikidata_comp__dev::p1]

Cited: alce::362__wikidata_comp__dev::p1

### `784__wikidata_simple__dev`
> **Individuals who have graduated from Loyola Law School, including notable figures in law, entertainment, and other fields**
> Loyola Law School is the law school of Loyola Marymount University, a private Catholic university in the Jesuit and Marymount traditions, in Los Angeles, California. [alce::784__wikidata_simple__dev::p6]
> Notable Loyola Law School alumni include Barbara Broccoli (producer of James Bond films), James Wong (creator of 'American Horror Story'), Brian Helgeland (writer/director of '42'), Francis Lawrence (director of 'The Hunger Games' films), and David Mirkin (executive producer and showrunner for 'The Simpsons'). [alce::784__wikidata_simple__dev::p38]
> A 1950 Loyola Law graduate, Bernard Beazley is the former general counsel and senior vice president of Dentsply International, one of the largest professional dental products companies in the world. [alce::784__wikidata_simple__dev::p23]

Cited: alce::784__wikidata_simple__dev::p23, alce::784__wikidata_simple__dev::p38, alce::784__wikidata_simple__dev::p6

### `231__wikidata_comp__dev`
> **Davenport, Iowa**
> Lee Enterprises is a publicly traded American media company that is based in Davenport, Iowa. [alce::231__wikidata_comp__dev::p0]

Cited: alce::231__wikidata_comp__dev::p0

### `247__wikidata_intersection__dev`
> **National League Championship Series (NLCS)**
> The 1983 National League Championship Series was a best-of-five matchup between the West Division champion Los Angeles Dodgers and the East Division champion Philadelphia Phillies. [alce::247__wikidata_intersection__dev::p8]
> The 2009 National League Championship Series (NLCS) was a best-of-seven baseball game series pitting the Los Angeles Dodgers against the Philadelphia Phillies for the National League Championship. [alce::247__wikidata_intersection__dev::p2]
> Overall, this was the fourth time these two teams had met in the postseason, with meetings in 1977, 1978, 1983, and 2009. [alce::247__wikidata_intersection__dev::p0]

Cited: alce::247__wikidata_intersection__dev::p0, alce::247__wikidata_intersection__dev::p2, alce::247__wikidata_intersection__dev::p8

### `644__wikidata_simple__dev`
> **Baffin Island, the Melville Peninsula, the Boothia Peninsula, and the Canadian mainland**
> The Gulf of Boothia is surrounded by, clockwise, Baffin Island, Fury and Hecla Strait, the Melville Peninsula, the Canadian mainland, the Boothia Peninsula and perhaps Bellot Strait. [alce::644__wikidata_simple__dev::p0]

Cited: alce::644__wikidata_simple__dev::p0

### `71__wikitables_composition__dev`
> **WGER, WKCQ, WSAM, and WTLZ**
> WGER (106.3 FM) is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p33]
> WKCQ (98.1 FM) is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p2]
> WSAM (1400 AM) is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p1]
> WTLZ (107.1 FM) is a radio station licensed to Saginaw, Michigan. [alce::71__wikitables_composition__dev::p9]

Cited: alce::71__wikitables_composition__dev::p1, alce::71__wikitables_composition__dev::p2, alce::71__wikitables_composition__dev::p33, alce::71__wikitables_composition__dev::p9

### `492__wikitables_simple__dev`
> **Ingeniero Carlos Fernández Casado Bridge, Liuguanghe Bridge, Royal Gorge Bridge, Beipan River Guanxing Highway Bridge**
> The Ingeniero Carlos Fernández Casado Bridge has a total height of 220 meters. [alce::492__wikitables_simple__dev::p19]
> The Liuguanghe Bridge in China surpassed the Royal Gorge Bridge in 2001 to become the new highest bridge with a deck height of over 200 meters. [alce::492__wikitables_simple__dev::p49]
> The Royal Gorge Bridge had a deck height of at least 200 meters before being surpassed in 2001. [alce::492__wikitables_simple__dev::p49]
> The Beipan River Guanxing Highway Bridge in China was completed in 2003 with a deck height of over 200 meters. [alce::492__wikitables_simple__dev::p49]

Cited: alce::492__wikitables_simple__dev::p19, alce::492__wikitables_simple__dev::p49

### `562__wikidata_simple__dev`
> **Panembahan Senopati, Sultan Agung Hanyokrokusumo, and Amangkurat I**
> Panembahan Senopati (1586–1601 AD) was the founder of the Mataram Sultanate. [alce::562__wikidata_simple__dev::p14]
> Sultan Agung Hanyokrokusumo reigned during the peak of power of the Mataram Sultanate until his death in 1645. [alce::562__wikidata_simple__dev::p2]
> Amangkurat I was the sultan of Mataram from 1646 to 1677 and was the son of the powerful Sultan Agung. [alce::562__wikidata_simple__dev::p16]

Cited: alce::562__wikidata_simple__dev::p14, alce::562__wikidata_simple__dev::p16, alce::562__wikidata_simple__dev::p2

### `979__wikidata_comp__dev`
> **Multiple directors directed pieces of media produced by This Is That corporation**
> This Is That's first production was '21 Grams' directed by Alejandro González Iñárritu. [alce::979__wikidata_comp__dev::p2]
> This Is That's second year brought 'Eternal Sunshine of the Spotless Mind' directed by Michel Gondry. [alce::979__wikidata_comp__dev::p2]
> This Is That produced 'The Door in the Floor', directed by Tod Williams. [alce::979__wikidata_comp__dev::p2]
> This Is That produced Jeff Feuerzeig's documentary 'The Devil and Daniel Johnston'. [alce::979__wikidata_comp__dev::p8]
> This Is That released Nicole Holofcener-directed 'Friends with Money'. [alce::979__wikidata_comp__dev::p8]
> In 2009, This Is That released 'Adventureland', written and directed by Greg Mottola. [alce::979__wikidata_comp__dev::p40]
> In 2010, This Is That completed 'SUPER', written and directed by James Gunn. [alce::979__wikidata_comp__dev::p40]
> This Is That produced 'Towelhead', directed by Alan Ball. [alce::979__wikidata_comp__dev::p16]

Cited: alce::979__wikidata_comp__dev::p16, alce::979__wikidata_comp__dev::p2, alce::979__wikidata_comp__dev::p40, alce::979__wikidata_comp__dev::p8

### `636__wikidata_simple__dev`
> **Vietnam Airlines operated scheduled passenger flights, cargo services, and airline catering and aircraft maintenance services**
> Vietnam Airlines is the flag carrier of Vietnam that flies to 64 destinations in 17 countries, excluding codeshared services. [alce::636__wikidata_simple__dev::p2]
> Vietnam Airlines operates approximately 70 aircraft, serving 46 destinations from its hubs at Noi Bai and Tan Son Nhat International Airports. [alce::636__wikidata_simple__dev::p4]
> The corporation earns revenue from airline catering and the maintenance and overhauling of aircraft through subsidiaries, including Vietnam Airlines Engineering Company and Vietnam Airlines Caterers. [alce::636__wikidata_simple__dev::p0]
> Vietnam Airlines controls and operates a cargo division, Vietnam Airlines Cargo. [alce::636__wikidata_simple__dev::p0]

Cited: alce::636__wikidata_simple__dev::p0, alce::636__wikidata_simple__dev::p2, alce::636__wikidata_simple__dev::p4

### `39__wikitables_composition__dev`
> **Sandviken**
> Sandviken is a locality and the seat of Sandviken Municipality in Gävleborg County, Sweden. [alce::39__wikitables_composition__dev::p2]

Cited: alce::39__wikitables_composition__dev::p2

### `226__wikidata_comp__dev`
> **VFL Grand Final**
> Fitzroy Football Club was the first club to win a VFL Grand Final. [alce::226__wikidata_comp__dev::p4]
> The club achieved a total of eight VFL premierships between 1898 and 1944. [alce::226__wikidata_comp__dev::p4]

Cited: alce::226__wikidata_comp__dev::p4

### `757__wikidata_simple__dev`
> **Sigi Schmid, Dominic Kinnear, and Curt Onalfo**
> Sigi Schmid is a German soccer coach who was most recently the head coach of the Los Angeles Galaxy of Major League Soccer (MLS). [alce::757__wikidata_simple__dev::p33]
> Dominic Kinnear is an American soccer coach who is currently serving as the head coach of LA Galaxy. [alce::757__wikidata_simple__dev::p3]
> Curt Onalfo is an American former soccer player and coach who most recently served as the head coach of the LA Galaxy. [alce::757__wikidata_simple__dev::p11]

Cited: alce::757__wikidata_simple__dev::p11, alce::757__wikidata_simple__dev::p3, alce::757__wikidata_simple__dev::p33

### `618__wikidata_simple__dev`
> **Animation work at Disney and DreamWorks films**
> Randy Cartwright is an American animator who began his career at Walt Disney Studios after being accepted into their animation training program in 1975. [alce::618__wikidata_simple__dev::p1]
> He worked on DreamWorks films including 'Antz' and 'Shrek', and also worked at Disney storyboarding and animating on 'The Princess and the Frog' with John Musker and Ron Clements. [alce::618__wikidata_simple__dev::p0]

Cited: alce::618__wikidata_simple__dev::p0, alce::618__wikidata_simple__dev::p1

### `418__wikidata_intersection__dev`
> **Michael Schumacher won the Monaco Grand Prix in 1994, 1997, 1999, and 2001**
> The German Michael Schumacher won the 1994 Monaco event. [alce::418__wikidata_intersection__dev::p22]
> The 1997 Monaco Grand Prix was won by Michael Schumacher, driving a Ferrari, after starting from second position. [alce::418__wikidata_intersection__dev::p4]
> The 1999 Monaco Grand Prix was won by Ferrari driver Michael Schumacher after starting from second position. [alce::418__wikidata_intersection__dev::p1]
> The 2001 Monaco Grand Prix was won by Michael Schumacher driving for the Ferrari team. [alce::418__wikidata_intersection__dev::p0]

Cited: alce::418__wikidata_intersection__dev::p0, alce::418__wikidata_intersection__dev::p1, alce::418__wikidata_intersection__dev::p22, alce::418__wikidata_intersection__dev::p4

### `56__wikitables_composition__dev`
> **Ernest Frederick Beal, Thomas James Harris, Eric Stuart Dougall, and Major Lumsden**
> Ernest Frederick Beal VC (27 January 1883 – 22 March 1918) was an English recipient of the Victoria Cross, the highest and most prestigious award for gallantry in the face of the enemy that can be awarded to British and Commonwealth forces. [alce::56__wikitables_composition__dev::p95]
> Thomas James Harris VC MM (30 January 1892 – 9 August 1918) was an English recipient of the Victoria Cross, the highest and most prestigious award for gallantry in the face of the enemy that can be awarded to British and Commonwealth forces. [alce::56__wikitables_composition__dev::p32]
> Major Eric Stuart Dougall VC MC (13 April 1886 – 14 April 1918) was an English recipient of the Victoria Cross, the highest and most prestigious award for gallantry in the face of the enemy that can be awarded to British and Commonwealth forces. He was awarded the Victoria Cross for his deeds on 10 April 1918 at Messines, Belgium. [alce::56__wikitables_composition__dev::p91]
> On 8 June 1917, the awarding of the Victoria Cross to Major Lumsden was approved. This was for actions that took place between 3 and 4 April 1917 in Francilly, France. He was killed in action at Blairvill, near Arras, France, on 4 June 1918. [alce::56__wikitables_composition__dev::p25]

Cited: alce::56__wikitables_composition__dev::p25, alce::56__wikitables_composition__dev::p32, alce::56__wikitables_composition__dev::p91, alce::56__wikitables_composition__dev::p95

### `767__wikidata_simple__dev`
> **Jules Engel taught several generations of animators at the California Institute of the Arts, including John Lasseter, Henry Selick, Tim Burton, and Stephen Hillenburg**
> He was the founding director of the Experimental Animation Program at the California Institute of the Arts, where he taught until his death, serving as mentor to several generations of animators. [alce::767__wikidata_simple__dev::p0]
> Stephen Hillenburg was one of Engel's students at the California Institute of the Arts. [alce::767__wikidata_simple__dev::p6]
> Many of his students carry out his influence through their work, including John Lasseter, Henry Selick, Tim Burton, and Stephen Hillenburg. [alce::767__wikidata_simple__dev::p7]

Cited: alce::767__wikidata_simple__dev::p0, alce::767__wikidata_simple__dev::p6, alce::767__wikidata_simple__dev::p7

### `594__wikidata_simple__dev`
> **Native American languages (multiple languages native to Arizona)**
> Arizona has the largest number of Native American language speakers in the United States, with twelve Native American languages spoken in Arizona. [alce::594__wikidata_simple__dev::p0]
> Quechan (also known as Yuma) is the native language of the Quechan people of southeastern California and southwestern Arizona in the Lower Colorado River Valley and Sonoran Desert. [alce::594__wikidata_simple__dev::p21]

Cited: alce::594__wikidata_simple__dev::p0, alce::594__wikidata_simple__dev::p21

### `648__wikidata_simple__dev`
> **Kerry County Museum**
> Kerry County Museum is a museum located in Tralee, County Kerry in Ireland. [alce::648__wikidata_simple__dev::p1]
> The aim of the museum is to collect, record, preserve and display the material heritage of Co. Kerry. [alce::648__wikidata_simple__dev::p1]

Cited: alce::648__wikidata_simple__dev::p1

### `4__wikitables_composition__dev`
> **Greensboro Science Center**
> The Greensboro Science Center is a science museum and zoological park established in 1957 and located in Greensboro, North Carolina, United States. [alce::4__wikitables_composition__dev::p2]
> Other Greensboro-based museums include the Greensboro Historical Museum, located at 130 Summit Ave. in Greensboro, North Carolina, and the International Civil Rights Center & Museum, located in Greensboro, North Carolina. [alce::4__wikitables_composition__dev::p0, alce::4__wikitables_composition__dev::p60]

Cited: alce::4__wikitables_composition__dev::p0, alce::4__wikitables_composition__dev::p2, alce::4__wikitables_composition__dev::p60

### `875__wikidata_simple__dev`
> **Multiple publications including "RCN Bulletin", "Nursing Standard", and various specialist nursing journals**
> RCN Publishing (branded as RCNi since March 2015) produces "RCN Bulletin", a monthly member publication, and "Nursing Standard", which is available through subscription and on news stands. [alce::875__wikidata_simple__dev::p28]
> It also publishes a range of journals for specialist nurses: "Cancer Nursing Practice", "Emergency Nurse", "Learning Disability Practice", "Mental Health Practice", "Nursing Children and Young People", "Nursing Management", "Nursing Older People", "Nurse Researcher", and "Primary Health Care". [alce::875__wikidata_simple__dev::p28]

Cited: alce::875__wikidata_simple__dev::p28

### `826__wikidata_simple__dev`
> **Main Hoon Na, Om Shanti Om, Happy New Year, Ra.One**
> Red Chillies Entertainment is an Indian motion picture production, distribution and visual effects company founded in 2002 by Bollywood actor Shah Rukh Khan and his wife Gauri Khan. [alce::826__wikidata_simple__dev::p4]
> The first film produced by Red Chillies Entertainment was Farah Khan's directorial debut 'Main Hoon Na'. [alce::826__wikidata_simple__dev::p43]
> Red Chillies Entertainment has produced or co-produced at least nine films as of 2015, including 'Ra.One' (2011). [alce::826__wikidata_simple__dev::p3]
> Gauri Khan has appeared in films she produced including 'Om Shanti Om' (2007) and 'Happy New Year' (2014). [alce::826__wikidata_simple__dev::p43]

Cited: alce::826__wikidata_simple__dev::p3, alce::826__wikidata_simple__dev::p4, alce::826__wikidata_simple__dev::p43

### `868__wikidata_simple__dev`
> **Multiple films including "Chore Chore Mastuto Bhai", "Bhalobasa Bhalobasa", "Dujone", "Jamai Raja", "Kohono Biday Bolo Na", "Wanted", "Ami Shudhu Cheyechi Tomay", "Romeo vs Juliet", "Agnee 2", "Aashiqui: True Love", "Angaar", "Hero 420", "Niyoti", "Badsha – The Don", "Shikari", "Prem Ki Bujhini", and "Rokto"**
> In 2005, Eskay released their first feature film, 'Chore Chore Mastuto Bhai', starring Mithun Chakraborty, Chiranjeet Chakraborty, Jisshu Sengupta. [alce::868__wikidata_simple__dev::p2]
> From 2008, Eskay would begin to release films every year, such as 'Bhalobasa Bhalobasa', 'Dujone', and 'Jamai Raja'. [alce::868__wikidata_simple__dev::p2]
> Eskay Movies released two films in 2010, 'Kohono Biday Bolo Na' and 'Wanted'. [alce::868__wikidata_simple__dev::p2]
> In 2014, Eskay released 'Ami Shudhu Cheyechi Tomay', which was co-produced with Bangladeshi film company Action Cut Entertainment and won the award for Best Bengali Film at the 2015 Kalakar Awards. [alce::868__wikidata_simple__dev::p3]
> Eskay Movies co-produced three films with Jaaz Multimedia in 2015: 'Romeo vs Juliet', 'Agnee 2' and 'Aashiqui: True Love'. [alce::868__wikidata_simple__dev::p3]
> Eskay Movies released seven films in 2016, all of which were co-produced by Jaaz Multimedia: 'Angaar', 'Hero 420', 'Niyoti', 'Badsha – The Don', 'Shikari', 'Prem Ki Bujhini' and 'Rokto'. [alce::868__wikidata_simple__dev::p4]

Cited: alce::868__wikidata_simple__dev::p2, alce::868__wikidata_simple__dev::p3, alce::868__wikidata_simple__dev::p4

### `191__wikidata_comp__dev`
_Refused._

### `769__wikidata_simple__dev`
_Refused._

### `855__wikidata_simple__dev`
> **Nebula Winners Thirteen**
> Nebula Winners Thirteen is an anthology of science fiction short works edited by Samuel R. Delany. [alce::855__wikidata_simple__dev::p35]
> It was first published in hardcover by Harper & Row in February 1980, with a paperback edition following from Bantam Books in August 1981. [alce::855__wikidata_simple__dev::p35]

Cited: alce::855__wikidata_simple__dev::p35

### `593__wikidata_simple__dev`
> **Osvaldo Golijov**
> George Crumb was a professor of piano and composition at the University of Colorado and later at the University of Pennsylvania, where he taught prominent students including Margaret Brouwer, Uri Caine, Christopher Rouse, Osvaldo Golijov, Jennifer Higdon, Cynthia Cozette Lee, Yen Lu, Ofer Ben-Amots, Robert Carl, and Gerald Levinson. [alce::593__wikidata_simple__dev::p1]
> Among George Crumb's most prominent students, Osvaldo Golijov is widely recognized as one of the most known, having achieved significant recognition as a composer. [alce::593__wikidata_simple__dev::p1]

Cited: alce::593__wikidata_simple__dev::p1

### `73__wikitables_composition__dev`
> **Lillico**
> The Devonport local government area encompasses Lillico, Tugrah and part of Spreyton. [alce::73__wikitables_composition__dev::p1]

Cited: alce::73__wikitables_composition__dev::p1

### `846__wikidata_simple__dev`
> **Lincoln Continental and Lincoln Town Car**
> The Lincoln Continental is a series of mid-sized and full-sized luxury cars produced by Lincoln, a division of the American automaker Ford Motor Company. [alce::846__wikidata_simple__dev::p24]
> The Lincoln Town Car is a model line of full-size luxury sedans that was marketed by the Lincoln division of the American automaker Ford Motor Company from 1980 to 2011. [alce::846__wikidata_simple__dev::p63]

Cited: alce::846__wikidata_simple__dev::p24, alce::846__wikidata_simple__dev::p63

### `1252__wikitables_composition__dev`
> **Cities and municipalities in Tarlac province include Tarlac City, Pura, Victoria, and Camiling**
> The province comprises three congressional districts and is subdivided into 17 municipalities and one city, Tarlac City, which is the provincial capital. [alce::1252__wikitables_composition__dev::p1]
> Pura is a municipality in the province of Tarlac located at the northeastern part of the Province of Tarlac. [alce::1252__wikitables_composition__dev::p20]
> Victoria is a municipality in the province of Tarlac, geographically located in the central part of Luzon. [alce::1252__wikitables_composition__dev::p8]
> Camiling is a first-class urban municipality of the province of Tarlac in the Philippines. [alce::1252__wikitables_composition__dev::p31]

Cited: alce::1252__wikitables_composition__dev::p1, alce::1252__wikitables_composition__dev::p20, alce::1252__wikitables_composition__dev::p31, alce::1252__wikitables_composition__dev::p8

### `494__wikitables_simple__dev`
> **Triads and extended chords are the main types of existing musical chords**
> A chord, in music, is any harmonic set of pitches consisting of two or more (usually three or more) notes that are heard as if sounding simultaneously. [alce::494__wikitables_simple__dev::p2]
> The most frequently encountered chords are triads, so called because they consist of three distinct notes; further notes may be added to create larger form melodies. [alce::494__wikitables_simple__dev::p12]
> In every key signature there are seven chords, and each of these chords are identified on the chordboard. [alce::494__wikitables_simple__dev::p27]

Cited: alce::494__wikitables_simple__dev::p12, alce::494__wikitables_simple__dev::p2, alce::494__wikitables_simple__dev::p27

### `205__wikidata_comp__dev`
> **Multiple colleges: Florida State University, Oregon State University, Tulane University, and Southeastern Louisiana**
> The St. Louis Cardinals selected him in the first round of the 2012 Major League Baseball draft from Florida State University. [alce::205__wikidata_comp__dev::p32]
> He committed to play college baseball at Oregon State University. He was drafted by the St. Louis Cardinals in the eighth round of the 2015 MLB draft. [alce::205__wikidata_comp__dev::p92]
> He signed with Tulane University to play college baseball. Hicks was drafted by the St. Louis Cardinals in the third round of the 2015 Major League Baseball Draft out of Cypress Creek High School in Houston, Texas. [alce::205__wikidata_comp__dev::p7]
> He played college football at Southeastern Louisiana. The St. Louis Cardinals selected Favron in the second round (46th overall) of the 1979 NFL Draft. [alce::205__wikidata_comp__dev::p93]

Cited: alce::205__wikidata_comp__dev::p32, alce::205__wikidata_comp__dev::p7, alce::205__wikidata_comp__dev::p92, alce::205__wikidata_comp__dev::p93

### `632__wikidata_simple__dev`
> **Artillery, vehicles, military equipment, and armoured fighting vehicles**
> Eidgenössische Konstruktionswerkstätte was a Swiss state-owned enterprise that produced artillery, vehicles and other typical military equipment. [alce::632__wikidata_simple__dev::p0]
> After 1943, the Eidgenoessische Konstruktionswerkstaette focused on the production of armoured fighting vehicles for the Swiss Army, including both its own designs and licensed production of M113 armored personnel carriers and Leopard 2 tanks. [alce::632__wikidata_simple__dev::p1]

Cited: alce::632__wikidata_simple__dev::p0, alce::632__wikidata_simple__dev::p1

### `865__wikidata_simple__dev`
> **The Warrior's Way**
> Relativity Media distributed its first film on December 3, 2010, which was 'The Warrior's Way' directed by Sngmoo Lee and starring Jang Dong-gun, Geoffrey Rush and Kate Bosworth. [alce::865__wikidata_simple__dev::p2]

Cited: alce::865__wikidata_simple__dev::p2

### `690__wikidata_simple__dev`
> **Amherst Railway Station**
> Via is the owner and operator of the station, which serves the 3 days a week 'Ocean' route. [alce::690__wikidata_simple__dev::p2]
> The station referred to is the Amherst Railway Station, which was transferred to Via Rail's ownership in 1978 when CN transferred responsibility for passenger rail services to Via Rail. [alce::690__wikidata_simple__dev::p2]

Cited: alce::690__wikidata_simple__dev::p2

### `704__wikidata_simple__dev`
> **Glades County, Hendry County, Martin County, and Okeechobee County**
> Glades County is one of five counties surrounding Lake Okeechobee. [alce::704__wikidata_simple__dev::p9]
> About three-quarters of Lake Okeechobee was divided among Glades, Hendry, Martin, and Okeechobee counties in 1963. [alce::704__wikidata_simple__dev::p11]
> Okeechobee County borders Glades County at one point in the center of the lake. [alce::704__wikidata_simple__dev::p92]

Cited: alce::704__wikidata_simple__dev::p11, alce::704__wikidata_simple__dev::p9, alce::704__wikidata_simple__dev::p92

### `456__wikidata_intersection__dev`
> **Vellanakalude Nadu**
> He directed "Vellanakalude Nadu", based on a script by Sreenivasan, with Mohanlal in the lead role. [alce::456__wikidata_intersection__dev::p2]

Cited: alce::456__wikidata_intersection__dev::p2

### `929__wikidata_simple__dev`
> **Sunbeam Rapier**
> The Sunbeam Rapier is an automobile produced by Rootes Group from 1955 to 1976, in two different body-styles, the 'Series' cars (which underwent several revisions) and the later (1967–76) fastback shape, part of the 'Arrow' range. [alce::929__wikidata_simple__dev::p35]
> The Sunbeam Rapier was announced at the London Motor Show in October 1955 and was the first of the 'Audax' range of light cars produced by the Rootes Group as part of their Sunbeam marque. [alce::929__wikidata_simple__dev::p35]

Cited: alce::929__wikidata_simple__dev::p35

### `13__wikitables_composition__dev`
> **Lucire (1997), MODE (1997), and SLiNK (2011)**
> Lucire is a fashion magazine that originally began on the web in 1997, before branching into a monthly print edition in its home country of New Zealand in 2004, and is now published seasonally. [alce::13__wikitables_composition__dev::p9]
> MODE was launched in the spring of 1997 as a fashion magazine specifically targeted at the plus-size consumer. [alce::13__wikitables_composition__dev::p33]
> Fashion editor Rivkie Baum launched SLiNK, a fashion and lifestyle magazine for full-figured women in 2011. [alce::13__wikitables_composition__dev::p4]

Cited: alce::13__wikitables_composition__dev::p33, alce::13__wikitables_composition__dev::p4, alce::13__wikitables_composition__dev::p9

### `713__wikidata_simple__dev`
> **Omphalos of Delphi**
> The Omphalos of Delphi is an ancient marble monument that was found at the archaeological site of Delphi, Greece. [alce::713__wikidata_simple__dev::p3]
> Among the inscriptions found at Delphi is a stele, written on all four sides, which seems to have regulated the phratry of the Labyadai. [alce::713__wikidata_simple__dev::p69]
> Room 10 contains parts of the Tholos of Delphi, the round building standing out in the sanctuary of Athena Pronaia, dated to the first quarter of the 4th century BC. [alce::713__wikidata_simple__dev::p4]

Cited: alce::713__wikidata_simple__dev::p3, alce::713__wikidata_simple__dev::p4, alce::713__wikidata_simple__dev::p69

### `519__wikitables_simple__dev`
> **Butterkist, Orville Redenbacher's, Popcorn Indiana, and other brands including The Detonator, Whirley Pop, Theater II, and Sweet & Easy**
> Butterkist is the United Kingdom's best-selling brand of popcorn, with around 40% of the £90 million market. [alce::519__wikitables_simple__dev::p13]
> Orville Redenbacher's Gourmet Popping Corn is a brand of popcorn made originally by Chester Inc. [alce::519__wikitables_simple__dev::p0]
> Popcorn, Indiana is a brand of popcorn in North America founded in 2002. [alce::519__wikitables_simple__dev::p5]
> Specialised popcorn pots have been marketed under various brand names, including The Detonator, Whirley Pop, Theater II and Sweet & Easy. [alce::519__wikitables_simple__dev::p71]

Cited: alce::519__wikitables_simple__dev::p0, alce::519__wikitables_simple__dev::p13, alce::519__wikitables_simple__dev::p5, alce::519__wikitables_simple__dev::p71

### `914__wikidata_simple__dev`
> **Doug Scott**
> Doug Scott was an English mountaineer noted for the first ascent of the south-west face of Mount Everest on 24 September 1975. [alce::914__wikidata_simple__dev::p49]
> Doug Scott and Dougal Haston became the first Britons to climb Everest during this expedition. [alce::914__wikidata_simple__dev::p49]
> The 1975 British Mount Everest Southwest Face expedition was led by Chris Bonington and was the first to successfully climb Mount Everest by ascending one of its faces. [alce::914__wikidata_simple__dev::p0]

Cited: alce::914__wikidata_simple__dev::p0, alce::914__wikidata_simple__dev::p49

### `749__wikidata_simple__dev`
> **British Energy, SEEBOARD Plc, London Electricity Plc, and SWEB Energy Plc were operating under EDF Energy**
> EDF Energy Customers (trading as EDF Energy) is wholly owned by the French state owned EDF (Électricité de France) and was formed in 2002, following the acquisition and mergers of SEEBOARD Plc (formerly the South Eastern Electricity Board), London Electricity Plc (formerly the London Electricity Board or LEB), SWEB Energy Plc (formerly the South Western Electricity Board). [alce::749__wikidata_simple__dev::p0]
> British Energy was rebranded to EDF Energy in July 2010. [alce::749__wikidata_simple__dev::p26]

Cited: alce::749__wikidata_simple__dev::p0, alce::749__wikidata_simple__dev::p26

### `586__wikidata_simple__dev`
> **Léopold Sédar Senghor**
> Léopold Sédar Senghor was a poet and statesman known for writing and defending the French language, and is described as a great defender of the French language and of Negritude. [alce::586__wikidata_simple__dev::p28]

Cited: alce::586__wikidata_simple__dev::p28

### `798__wikidata_simple__dev`
_Refused._

### `162__wikidata_intersection__dev`
> **The Wind and the Lion, Conan the Barbarian, and Red Dawn**
> John Milius wrote and directed "The Wind and the Lion", "Conan the Barbarian" and "Red Dawn." [alce::162__wikidata_intersection__dev::p4]
> Milius wrote and directed the popular adventure film "The Wind and the Lion" (1975), which starred Sean Connery and Candice Bergen. [alce::162__wikidata_intersection__dev::p7]
> Milius wrote and directed "Dillinger" (1973), which was moderately successful and launched Milius's directing career. [alce::162__wikidata_intersection__dev::p1]

Cited: alce::162__wikidata_intersection__dev::p1, alce::162__wikidata_intersection__dev::p4, alce::162__wikidata_intersection__dev::p7

### `184__wikidata_comp__dev`
> **Leo McCarey**
> Belle of the Nineties (1934) is Mae West's fourth motion picture, directed by Leo McCarey and released by Paramount Pictures. [alce::184__wikidata_comp__dev::p19]

Cited: alce::184__wikidata_comp__dev::p19

### `658__wikidata_simple__dev`
> **Mary Garden, Mary McCormic, Dorothy Gish, Helen Hayes, Kenneth MacKenna, Catherine Calvert, Ina Claire, Miriam Hopkins, Ruth Chatterton, Mary Pickford, Clark Gable, Norma Shearer, and Katharine Hepburn**
> Sarah Robinson-Duff was a noted opera singer and singing teacher, and her first pupil was future opera star Mary Garden. [alce::658__wikidata_simple__dev::p1]
> Frances Robinson-Duff, Sarah's daughter, established herself as a leading voice teacher in New York City, whose many famous pupils included Mary McCormic, Dorothy Gish, Helen Hayes, Kenneth MacKenna, Catherine Calvert, Ina Claire, Miriam Hopkins, Ruth Chatterton, Mary Pickford, Clark Gable, Norma Shearer, and Katharine Hepburn. [alce::658__wikidata_simple__dev::p2]

Cited: alce::658__wikidata_simple__dev::p1, alce::658__wikidata_simple__dev::p2

### `288__wikidata_intersection__dev`
> **City Lights**
> With the advent of sound technology, Chaplin began using a synchronised orchestral soundtrack – composed by himself – for "City Lights" (1931). [alce::288__wikidata_intersection__dev::p0]
> Charlie Chaplin directed "City Lights" (1931) among his other notable films. [alce::288__wikidata_intersection__dev::p10]

Cited: alce::288__wikidata_intersection__dev::p0, alce::288__wikidata_intersection__dev::p10

### `103__wikidata_intersection__dev`
> **1987, 1990, 1991, and 1992 Monaco Grand Prix**
> The 1987 Monaco Grand Prix was won by Ayrton Senna, driving a Lotus-Honda, and it was the first of an eventual six wins for the Brazilian driver at Monaco. [alce::103__wikidata_intersection__dev::p2]
> The 1990 Monaco Grand Prix was won by Brazilian driver Ayrton Senna, driving a McLaren-Honda, which was his second consecutive Monaco win and third in all. [alce::103__wikidata_intersection__dev::p5]
> Senna won his fourth Monaco Grand Prix in five years in 1991. [alce::103__wikidata_intersection__dev::p7]
> The 1992 Monaco Grand Prix was won by Ayrton Senna, driving a McLaren-Honda. [alce::103__wikidata_intersection__dev::p3]

Cited: alce::103__wikidata_intersection__dev::p2, alce::103__wikidata_intersection__dev::p3, alce::103__wikidata_intersection__dev::p5, alce::103__wikidata_intersection__dev::p7

### `630__wikidata_simple__dev`
> **Doom**
> id Software made important technological developments in video game technologies for the PC (running MS-DOS and Windows), including work done for the "Wolfenstein", "Doom", and "Quake" franchises. [alce::630__wikidata_simple__dev::p4]
> After "Wolfenstein 3D"s great success, id began working on "Doom", which was released in December 1993. [alce::630__wikidata_simple__dev::p3]

Cited: alce::630__wikidata_simple__dev::p3, alce::630__wikidata_simple__dev::p4

### `819__wikidata_simple__dev`
> **interACT**
> Notable intersex rights organizations include interACT and Intersex Campaign for Equality. [alce::819__wikidata_simple__dev::p8]

Cited: alce::819__wikidata_simple__dev::p8

### `672__wikidata_simple__dev`
> **flags of nations and territories, ensigns of vessels and aircraft, coat of arms, and computer software/internet icons**
> The Union Flag also appears in the canton (upper left-hand quarter) of the flags of several nations and territories that are former British possessions or dominions, as well as the state flag of Hawaii. [alce::672__wikidata_simple__dev::p0]
> The Union Flag can be found in the canton of several of the ensigns flown by vessels and aircraft of the United Kingdom and its overseas territories. [alce::672__wikidata_simple__dev::p1]
> The coat of arms of the Chilean city of Coquimbo features the Union Jack, owing to its historical commercial links to Britain. [alce::672__wikidata_simple__dev::p1]
> Commonly the Union Flag is used on computer software and Internet pages as an icon representing a choice of the English language. [alce::672__wikidata_simple__dev::p22]

Cited: alce::672__wikidata_simple__dev::p0, alce::672__wikidata_simple__dev::p1, alce::672__wikidata_simple__dev::p22

### `351__wikidata_comp__dev`
> **Juan Manuel Fangio, Luigi Fagioli, Jacky Ickx, and Giancarlo Baghetti**
> The 1951 French Grand Prix was won by Juan Manuel Fangio and Luigi Fagioli driving an Alfa Romeo. [alce::351__wikidata_comp__dev::p5]
> The 1968 French Grand Prix was won by Ferrari driver Jacky Ickx after he started from third position. [alce::351__wikidata_comp__dev::p21]
> Giancarlo Baghetti in a privately entered Ferrari won the French Grand Prix on his championship debut. [alce::351__wikidata_comp__dev::p76]

Cited: alce::351__wikidata_comp__dev::p21, alce::351__wikidata_comp__dev::p5, alce::351__wikidata_comp__dev::p76

### `655__wikidata_simple__dev`
> **Public buildings including theaters, palaces of justice, churches, and other monumental structures**
> Second Empire architecture in Europe is an architectural style rooted in the 17th century Renaissance which grew to its greatest popularity in Europe in the last half of the nineteenth century and early years of the twentieth century. [alce::655__wikidata_simple__dev::p0]
> Notable examples of Second Empire public architecture include the Palais de Justice and the Court of Cassation, the Tribunal de Commerce, and the Théâtre du Châtelet. [alce::655__wikidata_simple__dev::p26]
> The best example was the Opéra Garnier, begun in 1862 but not finished until 1875, which was at the time the largest theater in the world. [alce::655__wikidata_simple__dev::p64]
> The largest new church built in Paris during the Second Empire was Church of Saint Augustine (1860–71), by Victor Baltard, with a modern structure inside supported by slender cast-iron columns. [alce::655__wikidata_simple__dev::p21]

Cited: alce::655__wikidata_simple__dev::p0, alce::655__wikidata_simple__dev::p21, alce::655__wikidata_simple__dev::p26, alce::655__wikidata_simple__dev::p64

### `934__wikidata_simple__dev`
> **AVM Saeedullah Khan**
> AVM Saeedullah Khan (23 July 1926 - 2002) was one of the pioneering officers of Pakistan Air Force. [alce::934__wikidata_simple__dev::p23]
> He joined the newly formed air force, then known as Royal Pakistan Air Force, as a flying officer (pilot) and rose to the rank of Air Vice Marshal. [alce::934__wikidata_simple__dev::p23]

Cited: alce::934__wikidata_simple__dev::p23

### `182__wikidata_intersection__dev`
> **VFL/AFL (Victorian Football League/Australian Football League)**
> The two clubs have played each other 256 times in the VFL/AFL, with Carlton ahead with 127 wins to Collingwood's 125, and 4 draws. [alce::182__wikidata_intersection__dev::p3]
> Collingwood and Carlton have met in six VFL Grand Finals. [alce::182__wikidata_intersection__dev::p8]
> In 1897, both Collingwood and Carlton were part of the eight teams which broke away from the VFA to form the Victorian Football League. [alce::182__wikidata_intersection__dev::p0]

Cited: alce::182__wikidata_intersection__dev::p0, alce::182__wikidata_intersection__dev::p3, alce::182__wikidata_intersection__dev::p8

### `428__wikidata_comp__dev`
_Refused._

### `1010__wikidata_comp__dev`
> **California Institute of the Arts (CalArts)**
> Jules Engel was the founding director of the Experimental Animation Program at the California Institute of the Arts, where he taught until his death, serving as mentor to several generations of animators. [alce::1010__wikidata_comp__dev::p0]
> Stephen Hillenburg was one of Engel's students at the California Institute of the Arts. [alce::1010__wikidata_comp__dev::p71]

Cited: alce::1010__wikidata_comp__dev::p0, alce::1010__wikidata_comp__dev::p71

### `9__wikitables_composition__dev`
> **KWOC**
> KWOC (930 AM, "News/Talk 930") is an American radio station licensed to serve the community of Poplar Bluff, Missouri. [alce::9__wikitables_composition__dev::p26]

Cited: alce::9__wikitables_composition__dev::p26

### `37__wikitables_composition__dev`
> **Israeli officials and Gerald Steinberg and Jason Edelstein**
> Israeli officials categorize the BDS movement as antisemitic. [alce::37__wikitables_composition__dev::p5]
> Gerald Steinberg and Jason Edelstein contend that the BDS movement's central actors should be marginalized and exposed as not representing a genuine grassroots protest against Israeli policy. [alce::37__wikitables_composition__dev::p6]

Cited: alce::37__wikitables_composition__dev::p5, alce::37__wikitables_composition__dev::p6

### `416__wikidata_comp__dev`
_Refused._

### `835__wikidata_simple__dev`
> **Railway vehicles including passenger carriages, hospital cars, and rail tractors**
> Victorian Railways manufactured wooden bogie passenger carriages, with a total of 640 wooden-body, bogie locomotive-hauled carriages constructed between 1874 and 1903. [alce::835__wikidata_simple__dev::p1]
> Victorian Railways constructed hospital cars, which were converted from second class passenger cars after the collision at Sunshine in 1908. [alce::835__wikidata_simple__dev::p7]
> Victorian Railways manufactured rail tractors, which are small shunting units used for moving railway wagons at country stations and private sidings. [alce::835__wikidata_simple__dev::p33, alce::835__wikidata_simple__dev::p48]

Cited: alce::835__wikidata_simple__dev::p1, alce::835__wikidata_simple__dev::p33, alce::835__wikidata_simple__dev::p48, alce::835__wikidata_simple__dev::p7

### `931__wikidata_simple__dev`
> **Daniel Farke**
> Daniel Farke is a German association football manager and former professional player who is the head coach of Championship club Norwich City. [alce::931__wikidata_simple__dev::p33]
> On 25 May 2017, the club appointed German coach Daniel Farke as head coach, becoming the first foreign head coach of the club in its 114-year history. [alce::931__wikidata_simple__dev::p44]

Cited: alce::931__wikidata_simple__dev::p33, alce::931__wikidata_simple__dev::p44

### `740__wikidata_simple__dev`
_Refused._

### `623__wikidata_simple__dev`
> **Tales of the Vikings**
> Tales of the Vikings is an American first-run syndicated television series, first telecast on 8 September 1959 and ran through June 2, 1960. The series was produced by Kirk Douglas' production company, Bryna Productions. [alce::623__wikidata_simple__dev::p48]
> In 1955 Douglas founded his own company, Bryna Productions, named after his mother. "Tales of the Vikings" was the company's first venture into television. [alce::623__wikidata_simple__dev::p48]

Cited: alce::623__wikidata_simple__dev::p48

### `638__wikidata_simple__dev`
> **Otunba Fatai Olukoga, Iyabbo Jolaade Adewuyi, and Oseloka H. Obaze**
> Otunba Fatai Olukoga was a retired Permanent Secretary in Lagos State Civil Service and worked in the Lagos State Public Service. [alce::638__wikidata_simple__dev::p18]
> Iyabbo Jolaade Adewuyi was a Nigerian government official who served as a commissioner in Kwara State Government. [alce::638__wikidata_simple__dev::p88]
> Oseloka H. Obaze worked as a career Foreign Service Officer in the Nigerian Diplomatic Service and later served as Secretary to the State Government of Anambra State, Nigeria. [alce::638__wikidata_simple__dev::p56]

Cited: alce::638__wikidata_simple__dev::p18, alce::638__wikidata_simple__dev::p56, alce::638__wikidata_simple__dev::p88

### `364__wikidata_intersection__dev`
> **Bhadradeepam**
> Bhadradeepam is a 1973 Indian Malayalam film, directed by M. Krishnan Nair and produced by Sharada and T Sathyadevi. [alce::364__wikidata_intersection__dev::p43]
> The film has a musical score by MS Baburaj. [alce::364__wikidata_intersection__dev::p43]

Cited: alce::364__wikidata_intersection__dev::p43

### `958__wikidata_comp__dev`
> **Johns Hopkins School of Advanced International Studies and Colgate University**
> Kristie Canegallo was the Deputy White House Chief of Staff for Implementation for U.S. President Barack Obama. [alce::958__wikidata_comp__dev::p27]
> She holds an MA from the Johns Hopkins School of Advanced International Studies and a BA from Colgate University. [alce::958__wikidata_comp__dev::p27]

Cited: alce::958__wikidata_comp__dev::p27

### `522__wikitables_simple__dev`
> **Taipei, Beijing, Paris, and Dubai**
> The Taipei Grand Mosque is the largest and most famous mosque in Taiwan, located in the Da'an district of Taipei City. [alce::522__wikitables_simple__dev::p97]
> Beijing has the Niujie Mosque, the oldest and most famous mosque in the city, founded in 996 during the Liao dynasty. [alce::522__wikitables_simple__dev::p57]
> The Grand Mosque of Paris is located in the 5th arrondissement and is one of the largest mosques in France, as well as the third largest in Europe. [alce::522__wikitables_simple__dev::p1, alce::522__wikitables_simple__dev::p25]
> The Grand Mosque in Dubai is located in the Bur Dubai area and is the hub of Dubai's religious and cultural life. [alce::522__wikitables_simple__dev::p19]

Cited: alce::522__wikitables_simple__dev::p1, alce::522__wikitables_simple__dev::p19, alce::522__wikitables_simple__dev::p25, alce::522__wikitables_simple__dev::p57, alce::522__wikitables_simple__dev::p97

### `447__wikidata_intersection__dev`
_Refused._

### `24__wikitables_composition__dev`
> **Cumberland Center, Maine**
> Cumberland Center is a census-designated place (CDP) within the town of Cumberland in Cumberland County, Maine, United States. [alce::24__wikitables_composition__dev::p3]
> Other examples of census-designated places in Cumberland County, Maine include Freeport and Brunswick. [alce::24__wikitables_composition__dev::p23, alce::24__wikitables_composition__dev::p48]

Cited: alce::24__wikitables_composition__dev::p23, alce::24__wikitables_composition__dev::p3, alce::24__wikitables_composition__dev::p48

### `653__wikidata_simple__dev`
> **Multiple species were discovered in the Paja Formation, including Muiscasaurus, Padillasaurus leivaensis, Desmatochelys padillai, Leyvachelys, and various marine reptiles**
> Muiscasaurus is an extinct genus of ophthalmosaurid Ichthyosaur that lived in modern Colombia during the Early Cretaceous, with fossils found in the Paja Formation. [alce::653__wikidata_simple__dev::p43]
> Padillasaurus leivaensis is an extinct genus of titanosauriform sauropod from the Early Cretaceous Paja Formation in Colombia, known from a single partial axial skeleton. [alce::653__wikidata_simple__dev::p41]
> From the Paja Formation, the oldest sea turtle known in the world, Desmatochelys padillai, has been reported, along with Leyvachelys. [alce::653__wikidata_simple__dev::p4]
> The Paja Formation is one of the richest fossiliferous stratigraphic units of Colombia, where marine reptiles including pliosaurs, ichthyosaurs, and plesiosaurs are found. [alce::653__wikidata_simple__dev::p4]

Cited: alce::653__wikidata_simple__dev::p4, alce::653__wikidata_simple__dev::p41, alce::653__wikidata_simple__dev::p43

### `1254__wikitables_composition__dev`
_Refused._

### `287__wikidata_comp__dev`
> **St Dunstan's College, Catford and St Chad's**
> John Robert Hall (born 13 March 1949) is an English priest of the Church of England. He is the current Dean of Westminster and a chaplain to Queen Elizabeth II. [alce::287__wikidata_comp__dev::p45]
> He was educated at St Dunstan's College, Catford and St Chad's [alce::287__wikidata_comp__dev::p45]

Cited: alce::287__wikidata_comp__dev::p45

### `584__wikidata_simple__dev`
> **Battlegroup 107 and the Nordic Battlegroup are military units that belong to the EU Battlegroup**
> Battlegroup 107 or BG-107 is an EU Battlegroup consisting of military elements from the Netherlands, Germany, and Finland. [alce::584__wikidata_simple__dev::p12]
> The Nordic Battlegroup is a multi-national military unit and one of eighteen European Union Battlegroups that support European Union defence and security objectives. [alce::584__wikidata_simple__dev::p94]
> An EU Battlegroup is a military unit adhering to the Common Security and Defence Policy of the European Union, consisting of a battalion-sized force of approximately 1,500 troops reinforced with combat support elements. [alce::584__wikidata_simple__dev::p0, alce::584__wikidata_simple__dev::p6]

Cited: alce::584__wikidata_simple__dev::p0, alce::584__wikidata_simple__dev::p12, alce::584__wikidata_simple__dev::p6, alce::584__wikidata_simple__dev::p94

### `33__wikitables_composition__dev`
> **Majestic Centre**
> The Majestic Centre is the tallest building in Wellington, New Zealand. [alce::33__wikitables_composition__dev::p5]
> The Majestic Centre houses offices, as it is a commercial building located on Willis Street. [alce::33__wikitables_composition__dev::p5, alce::33__wikitables_composition__dev::p9]

Cited: alce::33__wikitables_composition__dev::p5, alce::33__wikitables_composition__dev::p9

### `95__wikitables_composition__dev`
> **Persona Q: Shadow of the Labyrinth and Etrian Odyssey V**
> Persona Q: Shadow of the Labyrinth is a role-playing video game developed by Atlus for the Nintendo 3DS handheld video game console. [alce::95__wikitables_composition__dev::p73]
> Etrian Odyssey V: Beyond the Myth is a dungeon crawler role-playing video game developed and published by Atlus for the Nintendo 3DS. [alce::95__wikitables_composition__dev::p28]

Cited: alce::95__wikitables_composition__dev::p28, alce::95__wikitables_composition__dev::p73

### `1353__wikidata_simple__dev`
> **Damir Krstičević and Imra Agotić were members of the Croatian National Guard**
> Damir Krstičević joined the Croatian National Guard in the summer of 1991 and was assigned to the 4th Guards Brigade where he eventually rose to the position of the brigade's commander. [alce::1353__wikidata_simple__dev::p27]
> Imra Agotić defected to the fledgling Croatian National Guard in July 1991, becoming its first commanding officer in August 1991. [alce::1353__wikidata_simple__dev::p63]

Cited: alce::1353__wikidata_simple__dev::p27, alce::1353__wikidata_simple__dev::p63

### `684__wikidata_simple__dev`
> **Mounageetam, Abhilasha, Rakshasudu, Chanti, Matrudevobhava, and Swarna Kamalam**
> K. S. Rama Rao is a Tollywood producer who established the Creative Commercials banner and has produced a number of popular films, including Mounageetam, Abhilasha, Rakshasudu, Chanti, Matrudevobhava, and Swarna Kamalam. [alce::684__wikidata_simple__dev::p1]

Cited: alce::684__wikidata_simple__dev::p1

### `768__wikidata_simple__dev`
_Refused._

### `693__wikidata_simple__dev`
> **SS501 consisted of five members: Kim Hyun-joong, Heo Young-saeng, Kim Kyu-jong, Park Jung-min, and Kim Hyung-jun**
> SS501 is a South Korean boy band consisting of five members: Kim Hyun-joong, Heo Young-saeng, Kim Kyu-jong, Park Jung-min and Kim Hyung-jun. [alce::693__wikidata_simple__dev::p1]

Cited: alce::693__wikidata_simple__dev::p1

### `230__wikidata_comp__dev`
> **Ohio Community Media published primarily in the state of Ohio**
> Ohio Community Media was an American privately owned publisher of daily and weekly newspapers, primarily in the state of Ohio. [alce::230__wikidata_comp__dev::p0]
> Ohio Community Media published 18 daily newspapers and about 30 weeklies (paid and free), in addition to several free weekly shopper publications in Ohio, with coverage areas including Central Ohio (Columbus area), Mid-Ohio (Mansfield area), Northwest Ohio, Southern Ohio, and Western Ohio (Dayton area). [alce::230__wikidata_comp__dev::p5]

Cited: alce::230__wikidata_comp__dev::p0, alce::230__wikidata_comp__dev::p5

### `408__wikidata_comp__dev`
_Refused._

### `252__wikidata_intersection__dev`
> **The Phantom Tollbooth**
> He co-directed the feature film "The Phantom Tollbooth" with Chuck Jones at MGM. [alce::252__wikidata_intersection__dev::p1]

Cited: alce::252__wikidata_intersection__dev::p1

### `583__wikidata_simple__dev`
_Refused._

### `718__wikidata_simple__dev`
> **Russian**
> The population is mostly ethnic Russians, but indigenous people of the area are various Tungusic peoples (Evenks, Negidals, Ulchs, Nanai, Oroch, and others). [alce::718__wikidata_simple__dev::p3]
> While indigenous Tungusic peoples are native to the region, Russian is the dominant language of the population in Khabarovsk Krai. [alce::718__wikidata_simple__dev::p3]

Cited: alce::718__wikidata_simple__dev::p3

### `484__wikitables_simple__dev`
> **Vemork, Volga Hydroelectric Station, Itaipu, Three Gorges Dam, and Tuoketuo Power Station**
> The 108-MW Vemork power station at the Rjukan waterfall was the world's largest power plant when it opened in 1911. [alce::484__wikitables_simple__dev::p0]
> The Volga Hydroelectric Station was the largest powerstation in the world between 1960 and 1963. [alce::484__wikitables_simple__dev::p26]
> Itaipu was the world's biggest power plant at the time (referring to a period when it was supporting major loads in Brazil's power system). [alce::484__wikitables_simple__dev::p1]
> The Three Gorges Dam is the world's largest power station in terms of installed capacity (22,500 MW). [alce::484__wikitables_simple__dev::p97]
> The Tuoketuo Power Station is the largest coal-fired power station in the world. [alce::484__wikitables_simple__dev::p7]

Cited: alce::484__wikitables_simple__dev::p0, alce::484__wikitables_simple__dev::p1, alce::484__wikitables_simple__dev::p26, alce::484__wikitables_simple__dev::p7, alce::484__wikitables_simple__dev::p97

### `616__wikidata_simple__dev`
> **Reddit, Google, EFF, Public Knowledge, Major League Gaming, and Demand Progress**
> ECA was a coalition partner with Reddit, Google, EFF, Public Knowledge, Major League Gaming, Demand Progress and others in opposing the Stop Online Piracy Act (SOPA) and its counterpart, the Protect Intellectual Property Act (PIPA). [alce::616__wikidata_simple__dev::p4]
> The association also lists the brands and companies which are marketing partners with the ECA on their website. [alce::616__wikidata_simple__dev::p30]

Cited: alce::616__wikidata_simple__dev::p30, alce::616__wikidata_simple__dev::p4

### `144__wikidata_intersection__dev`
> **Arya, Jagadam, and 1: Nenokkadine**
> Sukumar chose Devi Sri Prasad to compose the soundtrack and background score for the films he directed. [alce::144__wikidata_intersection__dev::p2]
> Sukumar worked with cinematographer R. Rathnavelu for 'Arya', 'Jagadam', and '1: Nenokkadine'. [alce::144__wikidata_intersection__dev::p2]
> Sukumar's usual composer, Devi Sri Prasad, was chosen for the film's soundtrack and score. [alce::144__wikidata_intersection__dev::p1]

Cited: alce::144__wikidata_intersection__dev::p1, alce::144__wikidata_intersection__dev::p2

### `592__wikidata_simple__dev`
> **Steamboat Lake State Park and Mount Zirkel Wilderness**
> Steamboat Lake State Park is a Colorado state park located in Routt County north of Steamboat Springs, Colorado, and near the community of Hahns Peak Village. [alce::592__wikidata_simple__dev::p1]
> The Mount Zirkel Wilderness is a U.S. Wilderness Area located in Routt National Forest in northwest Colorado, with the closest city being Steamboat Springs, Colorado. [alce::592__wikidata_simple__dev::p94]

Cited: alce::592__wikidata_simple__dev::p1, alce::592__wikidata_simple__dev::p94

### `925__wikidata_simple__dev`
> **Multiple notable scientists and engineers including Nazir Ahmad (first chairman), Salimuzzaman Siddiqui, Dr. Anwar Ali, Parvez Butt, and others**
> In 1956, Pakistan Atomic Energy Commission (PAEC) was founded and its first chairman was Nazir Ahmad, and Science Advisor to the Prime minister, Salimuzzaman Siddiqui served agency's [alce::925__wikidata_simple__dev::p1]
> Dr. Anwar Ali, a known nuclear physicist and his fellow nuclear engineer, took over as Chairman of the Pakistan Atomic Energy Commission in a simple ceremony held at PAEC headquarters. [alce::925__wikidata_simple__dev::p25]
> On 4 July 2006, Parvez Butt retired from PAEC as a Chief Scientist. [alce::925__wikidata_simple__dev::p25]
> Qureshi joined Pakistan Atomic Energy Commission (PAEC) in 1963, where he joined the physics staff led by dr. Naeem Ahmad Khan. [alce::925__wikidata_simple__dev::p15]

Cited: alce::925__wikidata_simple__dev::p1, alce::925__wikidata_simple__dev::p15, alce::925__wikidata_simple__dev::p25

### `775__wikidata_simple__dev`
> **Multiple films including "Billions" (1920), "Why Change Your Wife?" (1920), "Something to Think About" (1920), "Forbidden Fruit" (1921), and "Camille" (1921)**
> Rambova immediately began working for Nazimova on the comedy film "Billions" (1920), for which she supplied the costumes and served as art director. [alce::775__wikidata_simple__dev::p3]
> She also designed the costumes for two Cecil DeMille films in 1920: "Why Change Your Wife?" and "Something to Think About". [alce::775__wikidata_simple__dev::p3]
> The following year, she served as the art director on the DeMille production "Forbidden Fruit" (1921), in which she designed (with Mitchell Leisen) an elaborate costume for a Cinderella-inspired fantasy sequence. [alce::775__wikidata_simple__dev::p3]
> Film historian Robert Klepper wrote of her designs in "Camille" (1921). [alce::775__wikidata_simple__dev::p2]

Cited: alce::775__wikidata_simple__dev::p2, alce::775__wikidata_simple__dev::p3

### `110__wikidata_comp__dev`
_Refused._

### `426__wikidata_intersection__dev`
> **Lewis Hamilton won multiple Formula One seasons, including 2008, 2014, 2015, and others**
> Lewis Hamilton became the youngest ever F1 world champion in 2008 with McLaren, winning the title in his second season. [alce::426__wikidata_intersection__dev::p7]
> Lewis Hamilton won his first World Championship title with McLaren in 2008, then moved to Mercedes where he won back-to-back titles in 2014 and 2015 before winning back-to-back titles again in 2017 and 2018. [alce::426__wikidata_intersection__dev::p46]
> Lewis Hamilton won the Drivers' title by a point in 2008 by overtaking Toyota's Timo Glock on the final corner of the final lap of the final Grand Prix of the season. [alce::426__wikidata_intersection__dev::p24]
> Lewis Hamilton ended the 2015 season winning the championship, as well as the FIA Pole Trophy for most pole positions of the season and the DHL Fastest Lap Award. [alce::426__wikidata_intersection__dev::p17]

Cited: alce::426__wikidata_intersection__dev::p17, alce::426__wikidata_intersection__dev::p24, alce::426__wikidata_intersection__dev::p46, alce::426__wikidata_intersection__dev::p7

### `15__wikitables_composition__dev`
_Refused._

### `120__wikidata_intersection__dev`
> **Multiple fictional characters including Supergirl, Brainiac, and the Legion of Super-Heroes**
> With writer Otto Binder, he co-created the DC characters Supergirl and Brainiac, as well as the teenage team the Legion of Super-Heroes. [alce::120__wikidata_intersection__dev::p2]
> Binder and Plastino debuted the villain Brainiac and the Bottle City of Kandor in 'Action Comics' #242 and co-created Supergirl in 'Action Comics' #252 (May 1959). [alce::120__wikidata_intersection__dev::p23]
> Plastino drew the Superboy story in 'Adventure Comics' #247 (April 1958) that introduced the Legion of Super-Heroes, a teen superhero team from the future that eventually became one of DC's most popular features; with writer Otto Binder, Plastino co-created the first Legion characters: Cosmic Boy; Lightning Lad (as Lightning Boy) and Saturn Girl. [alce::120__wikidata_intersection__dev::p56]

Cited: alce::120__wikidata_intersection__dev::p2, alce::120__wikidata_intersection__dev::p23, alce::120__wikidata_intersection__dev::p56

### `966__wikidata_comp__dev`
> **Radley College and King's College London**
> Richard Lewis, a Bishop of St Edmundsbury and Ipswich, was educated at Radley College and trained for the priesthood at King's College London. [alce::966__wikidata_comp__dev::p10, alce::966__wikidata_comp__dev::p14]

Cited: alce::966__wikidata_comp__dev::p10, alce::966__wikidata_comp__dev::p14

### `440__wikidata_intersection__dev`
> **2018 Australian Open – Women's Doubles**
> Tímea Babos and Kristina Mladenovic won the title at the 2018 Australian Open – Women's Doubles, defeating Ekaterina Makarova and Elena Vesnina in the final, 6–4, 6–3. [alce::440__wikidata_intersection__dev::p2]
> It was the first Grand Slam title for Babos, who became the first Hungarian player to win a Grand Slam event since Andrea Temesvári in the 1986 French Open and the second Grand Slam title for Mladenovic. [alce::440__wikidata_intersection__dev::p2]

Cited: alce::440__wikidata_intersection__dev::p2

### `413__wikidata_comp__dev`
_Refused._

### `820__wikidata_simple__dev`
> **Waterways, dams, navigation locks, and hydroelectric facilities**
> The United States Army Corps of Engineers maintains inland and intracoastal waterways, including 191 commercially active lock sites with 237 lock chambers. [alce::820__wikidata_simple__dev::p45]
> USACE maintains direct control of 609 dams, maintains or operates 257 navigation locks, and operates 75 hydroelectric facilities generating 24% of the nation's hydropower. [alce::820__wikidata_simple__dev::p6]

Cited: alce::820__wikidata_simple__dev::p45, alce::820__wikidata_simple__dev::p6

### `664__wikidata_simple__dev`
> **Type VII submarines were German U-boats, including variants like Type VIIF**
> Type VII submarines were the most widely used U-boats of the war and were the most produced submarine class in history, with 703 built. [alce::664__wikidata_simple__dev::p4]
> The Type VII submarine was the most common U-boat of the Kriegsmarine. [alce::664__wikidata_simple__dev::p28]
> Type VIIF U-boats were the largest and heaviest type VII boats built, with only four Type VIIFs built, including U-1060 and U-1062 which were sent to support the Monsun Gruppe in the Far East. [alce::664__wikidata_simple__dev::p8]

Cited: alce::664__wikidata_simple__dev::p28, alce::664__wikidata_simple__dev::p4, alce::664__wikidata_simple__dev::p8

### `118__wikidata_comp__dev`
> **Fort Benning, Georgia; Fort Bragg, North Carolina; and Fort Hood, Texas**
> The 1st Security Force Assistance Brigade (1st SFAB) is based in Fort Benning, Georgia. [alce::118__wikidata_comp__dev::p1]
> The 2nd Security Force Assistance Brigade (2nd SFAB) is based in Fort Bragg, North Carolina, alongside the Security Force Assistance Command. [alce::118__wikidata_comp__dev::p0]
> The 3rd Security Force Assistance Brigade (3rd SFAB) is based in Fort Hood, Texas. [alce::118__wikidata_comp__dev::p6]

Cited: alce::118__wikidata_comp__dev::p0, alce::118__wikidata_comp__dev::p1, alce::118__wikidata_comp__dev::p6

### `260__wikidata_intersection__dev`
> **Strictly Ballroom, Romeo + Juliet, Moulin Rouge!, and The Great Gatsby**
> Pearce co-wrote the play 'Strictly Ballroom' and the screenplay of the 1992 movie adaptation with Baz Luhrmann. [alce::260__wikidata_intersection__dev::p0]
> He co-wrote the screenplay for the 1996 film 'Romeo + Juliet,' the 2001 film 'Moulin Rouge!', and the 2013 film 'The Great Gatsby'; all with Luhrmann. [alce::260__wikidata_intersection__dev::p0]

Cited: alce::260__wikidata_intersection__dev::p0

### `1259__wikitables_composition__dev`
> **Joe Gibbs**
> Joe Gibbs was hired to replace Pardee and led the Redskins to three Super Bowl championships (XVII, XXII, XXVI). [alce::1259__wikitables_composition__dev::p27]
> Super Bowl XVII occurred in 1983, which is after 1981, making the Redskins a Super Bowl finalist under Gibbs's coaching after 1981. [alce::1259__wikitables_composition__dev::p13]

Cited: alce::1259__wikitables_composition__dev::p13, alce::1259__wikitables_composition__dev::p27

### `358__wikidata_comp__dev`
> **Ted Kenney**
> Ted Kenney directed Guitar Center Sessions featuring Jane's Addiction and Peter Gabriel for DirectTV, as well as sessions with Buddy Guy, The Cult, Joe Bonamassa and Kenny Wayne Sheppard. [alce::358__wikidata_comp__dev::p9]
> Ted Kenney directed the 3D concert portion of the first live 3D country music concert movie: Kenny Chesney Summer in 3D, and produced the 3D concert in a box office hit, and is currently directing concert footage of JLo's Dance Again World Tour for a concert film/documentary. [alce::358__wikidata_comp__dev::p9]

Cited: alce::358__wikidata_comp__dev::p9

### `711__wikidata_simple__dev`
> **Joshua Green, the banker**
> Joshua Green, the banker, was a famous person who spoke Chinook Jargon in pioneer times. [alce::711__wikidata_simple__dev::p13]

Cited: alce::711__wikidata_simple__dev::p13

### `751__wikidata_simple__dev`
> **Multiple persons employed by India's Archaeological Survey**
> Devadatta Ramakrishna Bhandarkar (1875–1950) was an Indian archaeologist and epigraphist who worked with the Archaeological Survey of India (ASI). [alce::751__wikidata_simple__dev::p61]
> Kashinath Narayan Dikshit was an Indian archaeologist who served as Director-general of the Archaeological Survey of India (ASI) from 1937 to 1944. [alce::751__wikidata_simple__dev::p49]
> Madhusudan Narhar Deshpande (M. N. Deshpande) is an Indian archaeologist who served as Director General of the Archaeological Survey of India from 1972 to 1978. [alce::751__wikidata_simple__dev::p36]
> John Francis Blakiston was a British Indian archaeologist who served as Director General of the Archaeological Survey of India (ASI) from 1935 to 1937. [alce::751__wikidata_simple__dev::p58]
> Gautam Sengupta, an archaeologist, replaced K.M Srivastava as Director General, and was succeeded by Pravin Srivastava, another IAS officer, whose successor Rakesh Tiwari is also a professional archaeologist. [alce::751__wikidata_simple__dev::p0]

Cited: alce::751__wikidata_simple__dev::p0, alce::751__wikidata_simple__dev::p36, alce::751__wikidata_simple__dev::p49, alce::751__wikidata_simple__dev::p58, alce::751__wikidata_simple__dev::p61

### `354__wikidata_comp__dev`
> **Multiple victors depending on the competition: Footscray (1924), Essendon (1981 Escort Cup, 1980s Grand Final), and Carlton (in some Grand Finals)**
> Footscray recorded an upset victory against Essendon by 28 points in the 1924 Championship of Victoria match. [alce::354__wikidata_comp__dev::p20]
> Essendon won the 1981 Escort Cup over Carlton by defeating them 9.11 (65) to 6.5 (41). [alce::354__wikidata_comp__dev::p33]
> In the grand final, Essendon overwhelmed Carlton by 73 points, 18.17 (125) to 6.16 (52). [alce::354__wikidata_comp__dev::p65]
> Essendon and Carlton have contested six Grand Finals, with each team winning three of these encounters. [alce::354__wikidata_comp__dev::p33]

Cited: alce::354__wikidata_comp__dev::p20, alce::354__wikidata_comp__dev::p33, alce::354__wikidata_comp__dev::p65

### `560__wikidata_simple__dev`
> **Taylor Ward, David Fletcher, Michael Hermosillo, Kaleb Cowart, and Tyler Skaggs**
> Taylor Ward was drafted by the Angels in the first round of the 2015 MLB Draft. [alce::560__wikidata_simple__dev::p73]
> David Fletcher was drafted by the Los Angeles Angels in the sixth round of the 2015 Major League Baseball Draft. [alce::560__wikidata_simple__dev::p70]
> Michael Hermosillo was drafted by the Los Angeles Angels in the 28th round of the 2013 Major League Baseball Draft. [alce::560__wikidata_simple__dev::p13]
> Kaleb Cowart was drafted by the Los Angeles Angels in the first round (18th overall) in the 2010 Major League Baseball Draft. [alce::560__wikidata_simple__dev::p62]
> Tyler Skaggs was drafted by the Los Angeles Angels of Anaheim in the first round of the 2009 Major League Baseball draft. [alce::560__wikidata_simple__dev::p14]

Cited: alce::560__wikidata_simple__dev::p13, alce::560__wikidata_simple__dev::p14, alce::560__wikidata_simple__dev::p62, alce::560__wikidata_simple__dev::p70, alce::560__wikidata_simple__dev::p73

### `715__wikidata_simple__dev`
> **Multiple written works including anthologies, story collections, and the Eclipse anthology series**
> As a freelance editor, Jonathan has edited or co-edited forty-one original and reprint anthologies, and seventeen single-author story collections which have been published in Australia and the United States. [alce::715__wikidata_simple__dev::p0]
> From October 2012 till March 2013 Strahan edited an online extension of his Eclipse anthology series. [alce::715__wikidata_simple__dev::p2]
> In 1999 Jonathan founded The Coode Street Press, which published the one-shot review 'zine 'The Coode Street Review of Science Fiction' and co-published Terry Dowling's 'Antique Futures'. [alce::715__wikidata_simple__dev::p0]

Cited: alce::715__wikidata_simple__dev::p0, alce::715__wikidata_simple__dev::p2

### `643__wikidata_simple__dev`
> **Autozam Clef, Autozam Revue, and Autozam Scrum**
> The Autozam Clef is a mid-size sedan that was sold by Autozam from 1992 until 1994. [alce::643__wikidata_simple__dev::p6]
> The Autozam Revue is a subcompact car that was sold by Autozam, introduced in 1990. [alce::643__wikidata_simple__dev::p7]
> The Autozam Scrum, later known as Mazda Scrum, is a cabover microvan and kei truck sold exclusively in Japan by the Japanese automaker Mazda. [alce::643__wikidata_simple__dev::p36]

Cited: alce::643__wikidata_simple__dev::p36, alce::643__wikidata_simple__dev::p6, alce::643__wikidata_simple__dev::p7

### `790__wikidata_simple__dev`
> **Wolfenstein, Doom, Quake, Rage, Hovertank 3D, Catacomb 3D, Rescue Rover series, Dangerous Dave series, and other titles**
> id Software made important technological developments in video game technologies for the PC (running MS-DOS and Windows), including work done for the "Wolfenstein", "Doom", and "Quake" franchises. [alce::790__wikidata_simple__dev::p2]
> id Software announced at the 2008 E3 event that they would be publishing "Rage" through Electronic Arts, and later ZeniMax announced that they are publishing "Rage" through Bethesda Softworks. [alce::790__wikidata_simple__dev::p9]
> During its early days, id Software produced much more varied games; these include the early 3D first-person shooter experiments that led to "Wolfenstein 3D" and "Doom" – "Hovertank 3D" and "Catacomb 3D". There was also the "Rescue Rover" series, which had two games – "Rescue Rover" and "Rescue Rover 2". Also there was John Romero's "Dangerous Dave" series. [alce::790__wikidata_simple__dev::p3]
> Some id Software titles ported to Linux are "Doom" (the first id Software game to be ported), "Quake", "Quake II", "Quake III Arena", "Return to Castle Wolfenstein", "Doom 3", and "Quake 4". [alce::790__wikidata_simple__dev::p5]

Cited: alce::790__wikidata_simple__dev::p2, alce::790__wikidata_simple__dev::p3, alce::790__wikidata_simple__dev::p5, alce::790__wikidata_simple__dev::p9

### `404__wikidata_intersection__dev`
> **Alang-Alang**
> Sardi made his debut as music supervisor with JIF's 1939 hit "Alang-Alang". [alce::404__wikidata_intersection__dev::p0]
> Tan Tjoei Hock was a Chinese-Indonesian journalist and filmmaker who became one of the most productive film directors of the Dutch East Indies between 1940 and 1941, directing nine films. [alce::404__wikidata_intersection__dev::p11]
> Mas Sardi wrote and conducted several songs for the production, including "Oh Ajah dan Iboekoe" ("Oh My Father and Mother") and "Akoe Ta' Sangka" ("I Never Expected"). [alce::404__wikidata_intersection__dev::p19]

Cited: alce::404__wikidata_intersection__dev::p0, alce::404__wikidata_intersection__dev::p11, alce::404__wikidata_intersection__dev::p19

### `148__wikidata_intersection__dev`
> **Portsmouth F.C. participated in multiple FA Cup Finals: the 1929 FA Cup Final, the 1933-34 FA Cup Final, the 1939 FA Cup Final, the 2008 FA Cup Final, and the 2009-10 FA Cup Final**
> Portsmouth reached the 1929 FA Cup Final. [alce::148__wikidata_intersection__dev::p11]
> The 1933–34 season saw Portsmouth again reach the FA Cup final for a second time, having beaten Manchester United, Bolton Wanderers, Leicester City and Birmingham City on the way. [alce::148__wikidata_intersection__dev::p11]
> Portsmouth's Tommy Rowe was the last surviving player from the 1939 FA Cup Final match. [alce::148__wikidata_intersection__dev::p53]
> On 17 May 2008, Portsmouth played Cardiff City in the second FA Cup Final to be played at the newly rebuilt Wembley Stadium, winning 1–0. [alce::148__wikidata_intersection__dev::p0]
> In the 2009–10 FA Cup, Portsmouth advanced to the final after beating Coventry, Sunderland, Southampton, Birmingham and Tottenham Hotspur in the semi-final, and played at Wembley Stadium in the final against Chelsea, a game that Chelsea won by 1–0. [alce::148__wikidata_intersection__dev::p37]

Cited: alce::148__wikidata_intersection__dev::p0, alce::148__wikidata_intersection__dev::p11, alce::148__wikidata_intersection__dev::p37, alce::148__wikidata_intersection__dev::p53

### `232__wikidata_comp__dev`
> **Multiple teams competed in CAF Super Cup competitions, including Al-Ahly, AC Léopards, TP Mazembe, FUS Rabat, ES Sahel, CS Sfaxien, and Mamelodi Sundowns**
> Al-Ahly of Egypt competed in the 2013 CAF Super Cup as the 2012 CAF Champions League winner, facing AC Léopards of the Republic of the Congo. [alce::232__wikidata_comp__dev::p14]
> TP Mazembe of the Democratic Republic of the Congo competed in the 2011 CAF Super Cup as the winner of the 2010 CAF Champions League, facing FUS Rabat of Morocco. [alce::232__wikidata_comp__dev::p6]
> ES Sahel and CS Sfaxien competed in the 2008 CAF Super Cup as the 2007 CAF Champions League and CAF Confederation Cup winners respectively. [alce::232__wikidata_comp__dev::p0]
> Mamelodi Sundowns of South Africa competed in the 2017 CAF Super Cup as the 2016 CAF Champions League winners, facing TP Mazembe of the Democratic Republic of the Congo. [alce::232__wikidata_comp__dev::p15]

Cited: alce::232__wikidata_comp__dev::p0, alce::232__wikidata_comp__dev::p14, alce::232__wikidata_comp__dev::p15, alce::232__wikidata_comp__dev::p6

### `874__wikidata_simple__dev`
> **CNN Philippines Network News**
> CNN Philippines Network News was the first flagship evening newscast of CNN Philippines. [alce::874__wikidata_simple__dev::p10]
> CNN Philippines Network News premiered on June 18, 2012 as Solar Network News and ended on March 26, 2017 after almost five years under different incarnations. [alce::874__wikidata_simple__dev::p10]

Cited: alce::874__wikidata_simple__dev::p10

### `670__wikidata_simple__dev`
> **Penny Rose, Michael Kaplan, and Roshni Dinaker are workers in the costume designer industry**
> Penny Rose is a British costume designer who has worked in the film industry since the 1970s. [alce::670__wikidata_simple__dev::p88]
> Michael Kaplan is an American costume designer for film who has been working in the Hollywood film industry since 1981. [alce::670__wikidata_simple__dev::p23]
> Roshni Dinaker is an Indian costume designer and filmmaker, who has worked in Kannada, Tamil, and Telugu film industries. [alce::670__wikidata_simple__dev::p40]

Cited: alce::670__wikidata_simple__dev::p23, alce::670__wikidata_simple__dev::p40, alce::670__wikidata_simple__dev::p88

### `211__wikidata_intersection__dev`
> **Contests won and participated by the Baltimore Orioles**
> The Baltimore Orioles won their first National League pennant in 1894 and participated in the first Temple Cup competition against the second-place New York Giants, though they lost in a sweep, four games to none. [alce::211__wikidata_intersection__dev::p37]
> The Baltimore Orioles finished in first place three consecutive years (1894–1895–1896) and won the Temple Cup national championship series in 1896 and 1897. [alce::211__wikidata_intersection__dev::p10]
> The minor league Baltimore Orioles won the Governors' Cup, the championship of the IL, 2 times, and played in the championship games 'Little World Series', 5 times. [alce::211__wikidata_intersection__dev::p0]
> The Baltimore Orioles ice hockey team won the EAHL championship in the 1939–40 season. [alce::211__wikidata_intersection__dev::p95]

Cited: alce::211__wikidata_intersection__dev::p0, alce::211__wikidata_intersection__dev::p10, alce::211__wikidata_intersection__dev::p37, alce::211__wikidata_intersection__dev::p95

### `308__wikidata_comp__dev`
> **Andrew Bergman**
> Andrew Bergman is an American screenwriter, film director, and novelist whose best known films include "Blazing Saddles", "The In-Laws", and "The Freshman". [alce::308__wikidata_comp__dev::p1]
> Bergman wrote and directed "The Freshman" (1990) starring Marlon Brando and Matthew Broderick. [alce::308__wikidata_comp__dev::p4]

Cited: alce::308__wikidata_comp__dev::p1, alce::308__wikidata_comp__dev::p4

### `280__wikidata_intersection__dev`
_Refused._

### `150__wikidata_intersection__dev`
> **French Open, US Open, and Wimbledon**
> Elena Vesnina is a four-time Grand Slam champion in doubles competition, having won the 2013 French Open, 2014 US Open, and 2017 Wimbledon tournaments with Ekaterina Makarova. [alce::150__wikidata_intersection__dev::p3]
> Ekaterina Makarova is a four-time Grand Slam champion in doubles competition, having won the 2013 French Open, the 2014 US Open and 2017 Wimbledon Championships with Elena Vesnina. [alce::150__wikidata_intersection__dev::p2]

Cited: alce::150__wikidata_intersection__dev::p2, alce::150__wikidata_intersection__dev::p3

### `917__wikidata_simple__dev`
> **Avatar Press published comic books including "Bad Girl" comics, creator-owned works, and licensed adaptations**
> Avatar Press is most notable for publishing "Bad Girl" comics such as "Pandora", "Hellina", "Lookers", "The Ravening", and Brian Pulido's "Lady Death". [alce::917__wikidata_simple__dev::p0]
> As part of an effort to expand beyond their reputation as a bad girl publisher, it offered a number of noted creators an opportunity to publish creator-owned books with no content restrictions whatsoever, with creators such as Frank Miller, Warren Ellis, Alan Moore, and Garth Ennis taking them up on their offer. [alce::917__wikidata_simple__dev::p1]
> The company has taken to licensed comic book adaptations of famous sci-fi and horror shows from movies and television, such as "RoboCop", "Night of the Living Dead", and "Friday the 13th". [alce::917__wikidata_simple__dev::p1]
> Avatar Press incorporated "Widow" into their line-up and began reprinting the old Ground Zero Comics work as "Widow X," while also publishing new Widow material. [alce::917__wikidata_simple__dev::p6]

Cited: alce::917__wikidata_simple__dev::p0, alce::917__wikidata_simple__dev::p1, alce::917__wikidata_simple__dev::p6

### `933__wikidata_simple__dev`
> **Nonprofit organizations with headquarters in County Dublin include an organization working with rural communities in African countries and the RNLI Ireland.**
> An organisation works with rural communities in ten African countries and has its headquarters in Dublin, Ireland. [alce::933__wikidata_simple__dev::p31]
> In June 2006, the RNLI Ireland officially opened its new all-Ireland headquarters at Airside Business Park, within greater Swords. [alce::933__wikidata_simple__dev::p37]

Cited: alce::933__wikidata_simple__dev::p31, alce::933__wikidata_simple__dev::p37

### `629__wikidata_simple__dev`
> **Car and Track**
> Speed Channel originally broadcasted a repackaged version of the 1960s and 1970s show 'Car and Track', which was hosted and narrated by Bud Lindemann. [alce::629__wikidata_simple__dev::p5, alce::629__wikidata_simple__dev::p6]
> The syndicated 30-minute program carried highlights of major NASCAR races, before such coverage was widely available on network television. [alce::629__wikidata_simple__dev::p5, alce::629__wikidata_simple__dev::p6]

Cited: alce::629__wikidata_simple__dev::p5, alce::629__wikidata_simple__dev::p6

### `319__wikidata_intersection__dev`
> **Super Bowl VII, XVII, XVIII, XXII, and XXVI**
> The Washington Redskins won Super Bowl XVII, XXII, and XXVI, and also played in and lost Super Bowl VII and XVIII. [alce::319__wikidata_intersection__dev::p1]
> The team played in five Super Bowls total, winning three times (1982, 1987, and 1991), which correspond to Super Bowl XVII, XXII, and XXVI. [alce::319__wikidata_intersection__dev::p54]

Cited: alce::319__wikidata_intersection__dev::p1, alce::319__wikidata_intersection__dev::p54

### `755__wikidata_simple__dev`
> **Chery A3**
> The Chery A3 is a compact car built by the Chinese manufacturer Chery between 2008-2015, offered as a 4-door sedan and as a 5-door hatchback. [alce::755__wikidata_simple__dev::p1]

Cited: alce::755__wikidata_simple__dev::p1

### `235__wikidata_intersection__dev`
> **Ad Astra**
> James Gray is an American film director and screenwriter. [alce::235__wikidata_intersection__dev::p0]
> Gray first confirmed his plans to write and direct sci-fi space epic 'Ad Astra' on May 12 during the 2016 Cannes Film Festival. [alce::235__wikidata_intersection__dev::p1]

Cited: alce::235__wikidata_intersection__dev::p0, alce::235__wikidata_intersection__dev::p1

### `46__wikitables_composition__dev`
_Refused._

### `698__wikidata_simple__dev`
> **Dr. Allan Samson and Dr. Mikhail Brodsky**
> The university is currently led by Dr. Allan Samson, who is chairman of the board of trustees and instructor and by Dr. Mikhail Brodsky, President and CEO. [alce::698__wikidata_simple__dev::p0]

Cited: alce::698__wikidata_simple__dev::p0

### `105__wikidata_comp__dev`
> **Multiple winners across different years**
> The 2004 Belgian Grand Prix was won by Kimi Räikkönen, taking his and McLaren's only race win of the season from tenth place on the grid. [alce::105__wikidata_comp__dev::p19]
> The 2008 Belgian Grand Prix was won by Felipe Massa for the Ferrari team, after the initial winner, McLaren driver Lewis Hamilton, was penalised for cutting a chicane and gaining an advantage over Ferrari's Kimi Räikkönen. [alce::105__wikidata_comp__dev::p7]
> The 2013 Belgian Grand Prix was won by Sebastian Vettel in a Red Bull-Renault in a time of 1:23:42, registering an average speed of 220.80 km/h. [alce::105__wikidata_comp__dev::p2]
> The 2014 Belgian Grand Prix was won by Daniel Ricciardo for the Red Bull Racing team, after starting from fifth position. [alce::105__wikidata_comp__dev::p4]

Cited: alce::105__wikidata_comp__dev::p19, alce::105__wikidata_comp__dev::p2, alce::105__wikidata_comp__dev::p4, alce::105__wikidata_comp__dev::p7

### `343__wikidata_intersection__dev`
> **The sources do not explicitly name a single film where Trivikram Srinivas was screenwriter and K. Vijaya Bhaskar was director, but indicate they worked together on a project**
> Trivikram Srinivas worked as an assistant to director K. Vijaya Bhaskar on a project where he was asked to write dialogue for the climax scene. [alce::343__wikidata_intersection__dev::p1]
> During this project with K. Vijaya Bhaskar, Trivikram received an offer to write dialogue for the movie 'Swayamvaram', which was the first movie for which Trivikram wrote dialogue. [alce::343__wikidata_intersection__dev::p1]

Cited: alce::343__wikidata_intersection__dev::p1

### `756__wikidata_simple__dev`
> **Lake Champlain**
> The Richelieu River takes its source at the north end of Lake Champlain on the border between Canada (Quebec) and the United States (Vermont and New York state). [alce::756__wikidata_simple__dev::p0]
> The Richelieu River rises at Lake Champlain, from which it flows to the north in the province of Quebec, Canada and empties into the St. Lawrence river. [alce::756__wikidata_simple__dev::p6]

Cited: alce::756__wikidata_simple__dev::p0, alce::756__wikidata_simple__dev::p6

### `515__wikitables_simple__dev`
> **Olive cultivars vary widely and include varieties used for oil production, table olives, and dual-purpose cultivars, with examples including Arbequina, Kalamata, Frantoio, Manzanillo, Coratina, and many others**
> Olive cultivars include Arbequina, Arecuzzo, Barnea, Barouni, Coratina, Correggiola, Del Morocco, Frantoio, Hojiblanca, Jumbo Kalamata, Kalamata, Koroneiki, Leccino, Manzanillo, Pendulino, Picholine, Picual, Sevillano, UC13A6, and Verdale. [alce::515__wikitables_simple__dev::p12]
> The main olive cultivars used in the Palestinian territories are Chemlali, Jebbah, K18, Manzolino, Nabali Baladi, Nabali Mohassan, Shami and Souri. [alce::515__wikitables_simple__dev::p42]
> Olive varieties include: 'Baresane', 'Biancolilla', 'Brandofino', 'Buscionetto', 'Carolea', 'Cellina di Nardò', 'Cerasuola', 'Cerignola', 'Cima di Bitonto', 'Cima di Mola', 'Coratina', 'Frantoio', 'Garganica', 'La Minuta', 'Leccino', 'Moresca', 'Nocellara Etnea', 'Nocellara Messinese', 'Ogliarola', 'Ogliarola Barese', 'Ogliara Messinese', 'Ottobratica', 'Peranzana', 'Rotondella', 'Santagatese', 'Saracena', 'Tonda Iblea', and 'Verdello'. [alce::515__wikitables_simple__dev::p3]
> Olives cultivated for consumption are generally referred to as table olives, while many olive cultivars are used for oil production or both purposes. [alce::515__wikitables_simple__dev::p52]

Cited: alce::515__wikitables_simple__dev::p12, alce::515__wikitables_simple__dev::p3, alce::515__wikitables_simple__dev::p42, alce::515__wikitables_simple__dev::p52

### `779__wikidata_simple__dev`
> **Hridaynath Mangeshkar composed scores for various Marathi and Bollywood films**
> Hridaynath debuted his music career in 1955 with the Marathi film 'Akash Ganga'. Since then, he has composed for various Marathi films such as 'Sansar, Chaani, Ha Khel Savalyancha, Janaki, Jait Re Jait, Umbartha' and 'Nivdung' and a few Bollywood films; the most notable among them being 'Subah', 'Lekin...' and 'Maya Memsaab'. [alce::779__wikidata_simple__dev::p2]
> One of his most popular works is the composition for the Marathi film 'Nivdung'. [alce::779__wikidata_simple__dev::p1]

Cited: alce::779__wikidata_simple__dev::p1, alce::779__wikidata_simple__dev::p2

### `572__wikidata_simple__dev`
> **Spjøtvoll**
> In 1983 Spjøtvoll was hired at the Norwegian Institute of Technology. [alce::572__wikidata_simple__dev::p16]

Cited: alce::572__wikidata_simple__dev::p16

### `397__wikidata_intersection__dev`
> **1994, 1995, 1996, 1999, 2000, 2002, 2004, 2005, 2007, 2009, 2012, and 2015**
> Chelsea F.C. played in the 1994, 1995, 1996, 1999, 2004 and 2005 FA Cup Finals. [alce::397__wikidata_intersection__dev::p26]
> Chelsea were the last club to win the FA Cup at the old Wembley Stadium, when they beat Aston Villa in the 2000 Final. [alce::397__wikidata_intersection__dev::p26]
> Chelsea played Manchester United in the 2007 FA Cup Final. [alce::397__wikidata_intersection__dev::p0]
> The second FA Cup final to feature both Chelsea and Arsenal sides was in 2009, with Chelsea winning 2–1. [alce::397__wikidata_intersection__dev::p63]
> Chelsea's victory in the 2012 FA Cup Final was their most recent domestic cup final appearance mentioned. [alce::397__wikidata_intersection__dev::p7]
> Chelsea competed with Tottenham Hotspur in the first all-London FA Cup final, known as the 'Cockney Cup Final', which was Chelsea's first appearance in the final since 1915. [alce::397__wikidata_intersection__dev::p99]

Cited: alce::397__wikidata_intersection__dev::p0, alce::397__wikidata_intersection__dev::p26, alce::397__wikidata_intersection__dev::p63, alce::397__wikidata_intersection__dev::p7, alce::397__wikidata_intersection__dev::p99

### `465__wikidata_intersection__dev`
> **Multiple films: one with music released on Aditya Music (audio launch January 5, 2013), one with music released on Lahari Music Company, and one with music released on Sony Music (November 1, 2009)**
> Devi Sri Prasad composed the Music for this film. The audio launch was held on 5 January 2013 at Ramanaidu Studios in Nanakramguda at Hyderabad. Dil Raju, Shyam Prasad Reddy released the trailers on this occasion. [alce::465__wikidata_intersection__dev::p1]
> Music composed by Devi Sri Prasad. All songs are blockbusters. Music released on Aditya Music. The audio release was held on 10 September 2012 at Shilpakala Vedika in Hyderabad. [alce::465__wikidata_intersection__dev::p0]
> Music Composed by Devi Sri Prasad. Lyrics written by Ramajogayya Sastry. All songs are blockbusters. Music released on Lahari Music Company. [alce::465__wikidata_intersection__dev::p3]
> The soundtrack and background score were composed by Devi Sri Prasad. The music was released on 1 November 2009 at Rock Heights, Madhapur, Hyderabad. The audio rights of the soundtrack were purchased by Sony Music. [alce::465__wikidata_intersection__dev::p56]

Cited: alce::465__wikidata_intersection__dev::p0, alce::465__wikidata_intersection__dev::p1, alce::465__wikidata_intersection__dev::p3, alce::465__wikidata_intersection__dev::p56

### `949__wikidata_comp__dev`
_Refused._

### `800__wikidata_simple__dev`
> **The Simpsons**
> Sam Simon was an American director, producer, writer, animal rights activist and philanthropist, who co-developed the television series 'The Simpsons'. [alce::800__wikidata_simple__dev::p0]
> In 1988, Sam Simon, a reader of 'Army Man', recruited both Swartzwelder and Meyer to write for a new Fox animated sitcom he was executive producing: 'The Simpsons'. [alce::800__wikidata_simple__dev::p74]

Cited: alce::800__wikidata_simple__dev::p0, alce::800__wikidata_simple__dev::p74

### `538__wikitables_simple__dev`
> **Discovered ring galaxies include Hoag's Object, NGC 1291, and Arp 220**
> Hoag's Object, discovered by Art Hoag in 1950, is an example of a ring galaxy. [alce::538__wikitables_simple__dev::p0]
> NGC 1291, also known as NGC 1269, is a ring galaxy with an unusual inner bar and outer ring structure located about 33 million light-years away in the constellation Eridanus, discovered by James Dunlop in 1826. [alce::538__wikitables_simple__dev::p14]
> Arp 220 is another unusual galaxy in Serpens with an outer ring largely composed of young blue stars while the core is made up of older yellow stars. [alce::538__wikitables_simple__dev::p72]

Cited: alce::538__wikitables_simple__dev::p0, alce::538__wikitables_simple__dev::p14, alce::538__wikitables_simple__dev::p72

### `375__wikidata_intersection__dev`
> **Fourth Round of the 2003–04 FA Cup**
> In the Fourth Round of the 2003–04 FA Cup, the tie between Tottenham Hotspur and Manchester City went to a replay – played at White Hart Lane, London, on the evening of 4 February 2004 – after the original match 11 days earlier finished in a 1–1 draw. [alce::375__wikidata_intersection__dev::p3]
> Tottenham led the match 3–0 at half-time but Manchester City turned the match around in the second half to win 4–3, with Jon Macken scoring the winning goal in the 90th minute. [alce::375__wikidata_intersection__dev::p54]

Cited: alce::375__wikidata_intersection__dev::p3, alce::375__wikidata_intersection__dev::p54

### `36__wikitables_composition__dev`
> **Mercedes-AMG GT**
> The Mercedes-AMG GT is a two-door, two-seat sports car produced in coupé and roadster form by Mercedes-AMG. [alce::36__wikitables_composition__dev::p0]
> The car was introduced and officially unveiled to the public in October 2014 at the Paris Motor Show. [alce::36__wikitables_composition__dev::p0]

Cited: alce::36__wikitables_composition__dev::p0

### `736__wikidata_simple__dev`
_Refused._

### `491__wikitables_simple__dev`
> **Examples of existing youth councils include those in the United States, United Kingdom, France, Romania, Greece, Israel, and the Philippines**
> In the United States, many cities including Boston, Los Angeles, San Francisco, Chicago, Miami, Houston, Dallas, Seattle, and San Jose, California, have active youth councils that inform city government decision-making. [alce::491__wikitables_simple__dev::p0]
> Several U.S. states and legislatures have created youth councils, including Washington, Minnesota, Maine, Iowa, Indiana, Louisiana, New Mexico, Massachusetts, and New Hampshire. [alce::491__wikitables_simple__dev::p2]
> The UK's British Youth Council has operated the UK Youth Parliament for over a decade, where young people between the ages of 11-18 can vote for their local Member of Youth Parliament. [alce::491__wikitables_simple__dev::p1]
> Among 1800 local youth and children's councils exist in France, with 500 members of an umbrella organization called Anacej (National Association of youth and children councils) founded in 1991. [alce::491__wikitables_simple__dev::p5]
> In Israel, there is a National Youth Council whose members are elected from 7 Regional Youth Councils, which are elected from Municipal councils formed from representatives of School Student Councils and Youth Movements. [alce::491__wikitables_simple__dev::p5]
> The Greek Youth Parliament allows for the participation of youth not only from within Greece, but also from countries with large Greek communities such as Germany and Australia. [alce::491__wikitables_simple__dev::p5]

Cited: alce::491__wikitables_simple__dev::p0, alce::491__wikitables_simple__dev::p1, alce::491__wikitables_simple__dev::p2, alce::491__wikitables_simple__dev::p5

### `750__wikidata_simple__dev`
> **Stephen R. Fitzgarrald, Earl Cooley, Peter W. Breene, and Francis Patrick Carney were Colorado Lieutenant Governors**
> Stephen R. Fitzgarrald was the 17th Lieutenant Governor of Colorado, serving from 1909 to 1915 serving under Governors John F. Shafroth and Elias M. Ammons. [alce::750__wikidata_simple__dev::p11]
> Earl Cooley was the 21st Lieutenant Governor of Colorado, serving from 1921 to 1923 under Oliver Henry Shoup. [alce::750__wikidata_simple__dev::p4]
> Peter W. Breene was the fourth Lieutenant Governor of Colorado, serving from 1885 to 1887 under Governor Benjamin Harrison Eaton. [alce::750__wikidata_simple__dev::p21]
> Francis Patrick Carney was the tenth Lieutenant Governor of Colorado, serving from 1899 to 1901 under Governor Charles Spalding Thomas. [alce::750__wikidata_simple__dev::p28]

Cited: alce::750__wikidata_simple__dev::p11, alce::750__wikidata_simple__dev::p21, alce::750__wikidata_simple__dev::p28, alce::750__wikidata_simple__dev::p4

### `1256__wikitables_composition__dev`
_Refused._

### `809__wikidata_simple__dev`
> **Astérix series**
> Albert Uderzo is best known for his work on the "Astérix" series and also drew other comics such as "Oumpah-pah". [alce::809__wikidata_simple__dev::p0]

Cited: alce::809__wikidata_simple__dev::p0

### `82__wikitables_composition__dev`
> **Train stations in Birmingham include: New Street, Snow Hill, Moor Street, Birmingham International, Five Ways, Jewellery Quarter, Vauxhall, and Curzon Street**
> The Birmingham station group is a station group of three railway stations in Birmingham city centre, England consisting of New Street, Snow Hill and Moor Street. [alce::82__wikitables_composition__dev::p3]
> The station group does not include the international station of Birmingham International, which is located some east of the city centre next to Birmingham Airport and National Exhibition Centre. [alce::82__wikitables_composition__dev::p3]
> There are two other railway stations in central Birmingham, namely Five Ways in the south west of the city centre with connections on the New Street to Redditch line, and Jewellery Quarter. [alce::82__wikitables_composition__dev::p3]
> The first railway station to open in Birmingham was Vauxhall station, which opened in 1837 as a temporary railway shed, and Curzon Street railway station opened in 1838 as the permanent terminus in the city. [alce::82__wikitables_composition__dev::p7]

Cited: alce::82__wikitables_composition__dev::p3, alce::82__wikitables_composition__dev::p7

### `689__wikidata_simple__dev`
> **Magazine**
> Synapse: The Electronic Music Magazine was a bi-monthly American magazine about synthesizers and electronic music published March 1976 to June 1979. [alce::689__wikidata_simple__dev::p3]

Cited: alce::689__wikidata_simple__dev::p3

### `202__wikidata_comp__dev`
> **Dartmouth College and University of Chicago Booth School of Business**
> William E. Conway Jr., a co-founder of The Carlyle Group, received his undergraduate degree from Dartmouth College in 1971 and an MBA from the University of Chicago Booth School of Business. [alce::202__wikidata_comp__dev::p12]

Cited: alce::202__wikidata_comp__dev::p12

### `111__wikidata_intersection__dev`
> **"The Wire" and "The Corner"**
> Ed Burns and David Simon collaborated on "The Corner" and "The Wire" (HBO). [alce::111__wikidata_intersection__dev::p1]
> Burns was a producer, writer, and co-creator (also with Simon) of the HBO series "The Wire". [alce::111__wikidata_intersection__dev::p2]
> Simon adapted the latter book into the HBO mini-series "The Corner" (2000). [alce::111__wikidata_intersection__dev::p11]

Cited: alce::111__wikidata_intersection__dev::p1, alce::111__wikidata_intersection__dev::p11, alce::111__wikidata_intersection__dev::p2

### `516__wikitables_simple__dev`
> **R. D. Reynolds, Merle Vincent, Sebastián Martínez, and Earl Oliver own professional wrestling websites**
> WrestleCrap is a professional wrestling website created by R. D. Reynolds and Merle Vincent, and is currently run by Reynolds, Blade Braxton and Justin Henry. [alce::516__wikitables_simple__dev::p2]
> Solowrestling.com is a professional wrestling news website created by Sebastián Martínez, one of WWE's Spanish-language commentators. [alce::516__wikitables_simple__dev::p15]
> Earl Oliver launched Solie's Vintage Wrestling, a historical professional wrestling website, in 1995, named in honor of announcer Gordon Solie. [alce::516__wikitables_simple__dev::p11]

Cited: alce::516__wikitables_simple__dev::p11, alce::516__wikitables_simple__dev::p15, alce::516__wikitables_simple__dev::p2

### `645__wikidata_simple__dev`
> **Javi Gracia**
> Javi Gracia is a Spanish retired footballer who played as a defensive midfielder, and is the head coach of Premier League club Watford. [alce::645__wikidata_simple__dev::p64]
> Javi Gracia was appointed as Head Coach of Watford on 21 January 2018 following Marco Silva's departure. [alce::645__wikidata_simple__dev::p0]

Cited: alce::645__wikidata_simple__dev::p0, alce::645__wikidata_simple__dev::p64

### `944__wikidata_simple__dev`
> **More than 40 major discoveries**
> The Joint Institute for Nuclear Research (JINR) in Dubna, Russia is an international research center for nuclear sciences that has made more than 40 major discoveries. [alce::944__wikidata_simple__dev::p2]
> The Institute has seven laboratories specializing in theoretical physics, high energy physics, heavy ion physics, condensed matter physics, nuclear reactions, neutron physics, and information technology. [alce::944__wikidata_simple__dev::p1]

Cited: alce::944__wikidata_simple__dev::p1, alce::944__wikidata_simple__dev::p2

### `6__wikitables_composition__dev`
> **Malanje**
> Malanje is the capital of the province. [alce::6__wikitables_composition__dev::p0]
> Malanje is the capital city of Malanje Province in Angola with a population of approximately 222,000. [alce::6__wikitables_composition__dev::p3]

Cited: alce::6__wikitables_composition__dev::p0, alce::6__wikitables_composition__dev::p3

### `405__wikidata_comp__dev`
> **Rouben Mamoulian**
> N. Richard Nash wrote the screenplay for 'Porgy and Bess' (1959). [alce::405__wikidata_comp__dev::p33]
> Rouben Mamoulian directed 'Porgy and Bess', a film for which N. Richard Nash wrote the screenplay. [alce::405__wikidata_comp__dev::p96]

Cited: alce::405__wikidata_comp__dev::p33, alce::405__wikidata_comp__dev::p96

### `464__wikidata_intersection__dev`
> **Premaloka**
> V. Ravichandran cast himself in his directorial debut 'Premaloka' (1987), which became one of the highest grossing films. [alce::464__wikidata_intersection__dev::p9]
> V. Ravichandran is an Indian film actor, director, producer, music director and editor, indicating he has worked as a music director on various projects. [alce::464__wikidata_intersection__dev::p9]

Cited: alce::464__wikidata_intersection__dev::p9

### `198__wikidata_intersection__dev`
> **Thomas Walter Swan**
> Thomas Walter Swan was a longtime Judge of the United States Court of Appeals for the Second Circuit who became the Dean and a professor at Yale Law School in 1916. [alce::198__wikidata_intersection__dev::p29]

Cited: alce::198__wikidata_intersection__dev::p29

### `634__wikidata_simple__dev`
> **Women's sororities are members of the National Panhellenic Conference**
> The National Panhellenic Conference (NPC) is an umbrella organization for 26 (inter)national women's sororities throughout the United States and Canada. [alce::634__wikidata_simple__dev::p0]

Cited: alce::634__wikidata_simple__dev::p0

### `896__wikidata_simple__dev`
> **Multiple anthologies including "The Other Side of the Moon," "Beyond Time and Space," and "Strange Ports of Call"**
> The Other Side of the Moon is an anthology of science fiction stories edited by American writer August Derleth. It was first published by Pellegrini & Cudahy in 1949. [alce::896__wikidata_simple__dev::p38]
> Beyond Time and Space is an anthology of science fiction stories edited by American writer August Derleth. It was first published by Pellegrini & Cudahy in 1950. [alce::896__wikidata_simple__dev::p71]
> Strange Ports of Call is an anthology of science fiction stories edited by American writer August Derleth. It was first published by Pellegrini & Cudahy in 1948. [alce::896__wikidata_simple__dev::p37]
> Wandrei and Derleth co-edited the omnibus collections "The Outsider and Others" and "Beyond the Wall of Sleep". [alce::896__wikidata_simple__dev::p49]

Cited: alce::896__wikidata_simple__dev::p37, alce::896__wikidata_simple__dev::p38, alce::896__wikidata_simple__dev::p49, alce::896__wikidata_simple__dev::p71

### `161__wikidata_comp__dev`
> **Sidney Franklin**
> Sidney Franklin directed 'Smilin' Through' (1922), a film produced by Norma Talmadge and her husband Joseph M. Schenck for her company, the Norma Talmadge Film Corporation. [alce::161__wikidata_comp__dev::p16]
> The film 'Smilin' Through' (1922) was directed by Sidney Franklin and was one of Norma Talmadge's most popular films of her entire career. [alce::161__wikidata_comp__dev::p6]

Cited: alce::161__wikidata_comp__dev::p16, alce::161__wikidata_comp__dev::p6

### `122__wikidata_comp__dev`
> **Across the United States in various cities including Denver, Phoenix, Houston, Dallas, and Miami**
> Voice Media Group (VMG) is an American privately held media company headquartered in Denver, Colorado. VMG owns several newspaper publications across the country. [alce::122__wikidata_comp__dev::p0]
> Properties include 'Denver Westword', 'Phoenix New Times', 'Houston Press', 'Dallas Observer', 'Miami New Times', and 'Broward New Times', as well as a digital marketing agency. [alce::122__wikidata_comp__dev::p0]

Cited: alce::122__wikidata_comp__dev::p0

### `1354__wikidata_simple__dev`
> **Salish (Montana Salish)**
> The Salish or Séliš language, also known as Kalispel–Pend d'oreille, Kalispel–Spokane–Flathead, or Montana Salish, is a Salishan language spoken by about 64 elders of the Flathead Nation in north central Montana. [alce::1354__wikidata_simple__dev::p2]
> Montana is home to several indigenous languages including Crow (about 3,000 speakers), Cheyenne (about 1,700 speakers), Blackfoot (about 100 speakers), and Assiniboine (about 150 speakers). [alce::1354__wikidata_simple__dev::p0]

Cited: alce::1354__wikidata_simple__dev::p0, alce::1354__wikidata_simple__dev::p2

### `321__wikidata_comp__dev`
> **Multiple winners including Sam Hanks (1957), A. J. Foyt (1964), Will Power (2018), Dan Wheldon (2011), and Ryan Hunter-Reay (2014)**
> Sam Hanks won the Indianapolis 500 in 1957 in his thirteenth attempt. [alce::321__wikidata_comp__dev::p0]
> A. J. Foyt won the 1964 Indianapolis 500, which was his second of four Indy 500 victories. [alce::321__wikidata_comp__dev::p43]
> Will Power of Team Penske won the 2018 Indianapolis 500. [alce::321__wikidata_comp__dev::p23]
> Dan Wheldon won the 2011 Indianapolis 500, his second victory after winning in 2005. [alce::321__wikidata_comp__dev::p85]
> Ryan Hunter-Reay won the 2014 Indianapolis 500, the first American-born winner since 2006. [alce::321__wikidata_comp__dev::p90]

Cited: alce::321__wikidata_comp__dev::p0, alce::321__wikidata_comp__dev::p23, alce::321__wikidata_comp__dev::p43, alce::321__wikidata_comp__dev::p85, alce::321__wikidata_comp__dev::p90

### `301__wikidata_intersection__dev`
_Refused._

### `119__wikidata_comp__dev`
> **Brisbane Lions**
> In 2018, Fitzroy won both the VAFA Premier C and the VAFA Premier C reserves competitions. [alce::119__wikidata_comp__dev::p7]
> The Fitzroy Reds played the curtain-raiser at the MCG when the Brisbane Lions met the Collingwood Magpies in the AFL Heritage Round of 2003. [alce::119__wikidata_comp__dev::p7]

Cited: alce::119__wikidata_comp__dev::p7

### `668__wikidata_simple__dev`
> **Pickles and metal objects**
> Pickling salt is a salt that is used mainly for canning and manufacturing pickles. [alce::668__wikidata_simple__dev::p36]
> Pickling (metal) is a metal surface treatment used to remove impurities, such as stains, inorganic contaminants, rust or scale from ferrous metals, copper, precious metals and aluminum alloys. [alce::668__wikidata_simple__dev::p4]

Cited: alce::668__wikidata_simple__dev::p36, alce::668__wikidata_simple__dev::p4

### `805__wikidata_simple__dev`
> **Andy Tillson, John Hollins, and others**
> Andy Tillson was appointed as Weymouth's Assistant Manager in 2009. [alce::805__wikidata_simple__dev::p79]
> John Hollins took over as manager of Weymouth in January 2008. [alce::805__wikidata_simple__dev::p44]
> Gill was appointed manager of Conference South club Weymouth in January 2010. [alce::805__wikidata_simple__dev::p11]

Cited: alce::805__wikidata_simple__dev::p11, alce::805__wikidata_simple__dev::p44, alce::805__wikidata_simple__dev::p79

### `284__wikidata_intersection__dev`
> **Manchester City competed in multiple FA Cup Finals including the 1904, 1911, 1926, 1934, and 2013 FA Cup Finals**
> Manchester City competed in the 1904 FA Cup Final, where they won 1–0 thanks to a Billy Meredith goal. [alce::284__wikidata_intersection__dev::p0, alce::284__wikidata_intersection__dev::p41]
> Manchester City competed in the 2011 FA Cup Final, their first major final in over thirty years, where they defeated Stoke City 1–0. [alce::284__wikidata_intersection__dev::p63]
> Manchester City competed in the 1934 FA Cup Final, which they won 2–1 over Portsmouth. [alce::284__wikidata_intersection__dev::p48]
> Manchester City competed in the 2013 FA Cup Final, their 10th FA Cup final, against Wigan Athletic on 11 May 2013 at Wembley Stadium. [alce::284__wikidata_intersection__dev::p28]

Cited: alce::284__wikidata_intersection__dev::p0, alce::284__wikidata_intersection__dev::p28, alce::284__wikidata_intersection__dev::p41, alce::284__wikidata_intersection__dev::p48, alce::284__wikidata_intersection__dev::p63

### `595__wikidata_simple__dev`
> **Grey's Anatomy, Private Practice, Scandal, Off the Map, How to Get Away with Murder, and The Catch**
> Shonda Rhimes is best known as the showrunner—creator, head writer, and executive producer—of the television medical drama 'Grey's Anatomy', its spin-off 'Private Practice', and the political thriller series 'Scandal'. [alce::595__wikidata_simple__dev::p1]
> Rhimes has also served as the executive producer of the ABC television series 'Off the Map', 'How to Get Away with Murder', and 'The Catch'. [alce::595__wikidata_simple__dev::p1]

Cited: alce::595__wikidata_simple__dev::p1

### `369__wikidata_comp__dev`
> **Multiple Supreme Court of Missouri justices attended different schools, including John Burroughs School, Jackson College for Women (now part of Tufts University), Georgetown University Law Center, Dartmouth College, University of Minnesota Law School, William Jewell College, and University of Missouri School of Law**
> Laura Denvir Stith graduated in 1971 from John Burroughs School, a private school in metro St. Louis, Missouri, and then from Georgetown University Law Center in 1978. [alce::369__wikidata_comp__dev::p3]
> She also graduated from Jackson College for Women (now part of Tufts University). [alce::369__wikidata_comp__dev::p3]
> Michael A. Wolff, a former Chief Justice of the Supreme Court of Missouri, earned his undergraduate degree from Dartmouth College and his law degree from the University of Minnesota Law School. [alce::369__wikidata_comp__dev::p32]
> W. Brent Powell, a Judge on the Supreme Court of Missouri, received his undergraduate degree from William Jewell College and his Juris Doctor from the University of Missouri School of Law in 1996. [alce::369__wikidata_comp__dev::p4]

Cited: alce::369__wikidata_comp__dev::p3, alce::369__wikidata_comp__dev::p32, alce::369__wikidata_comp__dev::p4

### `852__wikidata_simple__dev`
> **Dungeon**
> Trondheim's greatest breakthrough after "Lapinot" is arguably "Dungeon" (in French, "Donjon"), an ambitious series which he created with [alce::852__wikidata_simple__dev::p11]
> NBM has published "Dungeon", both in comic book and graphic novel formats [alce::852__wikidata_simple__dev::p0]

Cited: alce::852__wikidata_simple__dev::p0, alce::852__wikidata_simple__dev::p11

### `729__wikidata_simple__dev`
> **Alpine and wooded lakes, bare granite rock formations, steep canyons, and plateaus with forests**
> Alpine and wooded lakes of various sizes are scattered throughout the area. [alce::729__wikidata_simple__dev::p1]
> The wilderness has extensive areas of bare granite rock formations and much barren rocky terrain at the edge of the tree line. [alce::729__wikidata_simple__dev::p3]
> Steep canyons of the Mokelumne, Cosumnes, American, and Rubicon rivers are found in the area, with plateaus of generally moderate relief located between these steep canyons. [alce::729__wikidata_simple__dev::p5]
> The Desolation Wilderness supports predominantly red fir and lodgepole pine forests with associated species such as Jeffrey pine, mountain hemlock, ponderosa pine, western juniper, and western white pine. [alce::729__wikidata_simple__dev::p4]

Cited: alce::729__wikidata_simple__dev::p1, alce::729__wikidata_simple__dev::p3, alce::729__wikidata_simple__dev::p4, alce::729__wikidata_simple__dev::p5

### `659__wikidata_simple__dev`
_Refused._

### `208__wikidata_comp__dev`
> **Spike Jonze**
> Tom Kaufman worked as a screenwriter on the TV shows 'The Edge', 'Ned and Stacey', and 'The Dana Carvey Show'. [alce::208__wikidata_comp__dev::p4]
> However, the sources do not provide information about who directed these TV shows. The sources primarily discuss Kaufman's film work, including 'Being John Malkovich' directed by Spike Jonze. [alce::208__wikidata_comp__dev::p4]

Cited: alce::208__wikidata_comp__dev::p4

### `419__wikidata_comp__dev`
> **John Schlesinger directed "Yanks" (1979), which Colin Welland wrote**
> Colin Welland's screenwriting credits include the film "Yanks" (1979), starring Vanessa Redgrave and Richard Gere, which was directed by John Schlesinger. [alce::419__wikidata_comp__dev::p5]

Cited: alce::419__wikidata_comp__dev::p5

### `898__wikidata_simple__dev`
_Refused._

### `963__wikidata_comp__dev`
> **Multiple California Supreme Court members attended various schools including Harvard University, Yale Law School, University of California Berkeley, George Washington University Law School, Holy Names College, and University of California Hastings College of the Law**
> Leondra Kruger, an Associate Justice of the Supreme Court of California, attended Polytechnic School in Pasadena, California, earned a Bachelor of Arts degree from Harvard University, and graduated with a Juris Doctor degree from Yale Law School. [alce::963__wikidata_comp__dev::p89]
> Kathryn Werdegar, an Associate Justice of the Supreme Court of California, earned her B.A. at the University of California, Berkeley and attended the University of California, Berkeley School of Law (Boalt Hall), before completing her J.D. degree at the George Washington University Law School. [alce::963__wikidata_comp__dev::p15]
> Carol Corrigan, an Associate Justice of the California Supreme Court, graduated from Saint Mary's High School in Stockton and attended Holy Names College in Oakland, graduating in 1970, and then enrolled at the University of California, Hastings College of the Law. [alce::963__wikidata_comp__dev::p60]

Cited: alce::963__wikidata_comp__dev::p15, alce::963__wikidata_comp__dev::p60, alce::963__wikidata_comp__dev::p89

### `49__wikitables_composition__dev`
_Refused._

### `695__wikidata_simple__dev`
> **Pennies from Heaven**
> Dennis Potter was an English television dramatist best known for his BBC TV serials including 'Pennies from Heaven' (1978), 'The Singing Detective' (1986), and television plays 'Blue Remembered Hills' (1979) and 'Brimstone and Treacle' (1976). [alce::695__wikidata_simple__dev::p0]
> His television dramas mixed fantasy and reality, the personal and the social, and often used themes and images from popular culture, making him widely regarded as one of the most influential and innovative dramatists in British television. [alce::695__wikidata_simple__dev::p0]

Cited: alce::695__wikidata_simple__dev::p0

### `637__wikidata_simple__dev`
> **Multiple mayors have served Boston, including Kevin White (1968-1984), John F. Collins (1960-1968), and Daniel A. Whelton. The current mayor is Martin J. "Marty" Walsh.**
> Kevin Hagan White was an American politician best known as the Mayor of Boston, an office he held for four terms amounting to 16 years, from 1968 to 1984. [alce::637__wikidata_simple__dev::p5]
> John Frederick Collins was the mayor of Boston, Massachusetts, United States from 1960 to 1968. [alce::637__wikidata_simple__dev::p34]
> Daniel Aloysius Whelton was an American political figure who became mayor of Boston. [alce::637__wikidata_simple__dev::p40]
> The current mayor is Martin J. "Marty" Walsh. [alce::637__wikidata_simple__dev::p0]

Cited: alce::637__wikidata_simple__dev::p0, alce::637__wikidata_simple__dev::p34, alce::637__wikidata_simple__dev::p40, alce::637__wikidata_simple__dev::p5

### `793__wikidata_simple__dev`
> **Marshall (Lakota person)**
> He was raised in a traditional Lakota household by his maternal grandparents, where his first language was Lakota. [alce::793__wikidata_simple__dev::p18]

Cited: alce::793__wikidata_simple__dev::p18

### `272__wikidata_intersection__dev`
> **Kadal**
> By the end of the year his music for Mani Ratnam's "Kadal" was critically acclaimed, and the album topped the iTunes India chart for December. [alce::272__wikidata_intersection__dev::p2]
> In an interview with Deccan Chronicle, Rahman mentioned that his request to Mani Ratnam, a complete song was dropped after filming because of the explicit lyrical content. [alce::272__wikidata_intersection__dev::p35]

Cited: alce::272__wikidata_intersection__dev::p2, alce::272__wikidata_intersection__dev::p35

### `1251__wikitables_composition__dev`
> **Dan Meridor, Yitzhak Mordechai, and other Centre Party members from the 1999 elections**
> The Centre Party was established on 23 February 1999 by Mordechai, David Magen and Dan Meridor from Likud, Hagai Meirom and Nissim Zvili of Labour, and Eliezer Sandberg of Tzomet. [alce::1251__wikitables_composition__dev::p0]
> In elections to the Knesset itself the Centre Party took roughly 5% of the vote, enough for 6 seats. [alce::1251__wikitables_composition__dev::p1]
> Dan Meridor was elected as a Centre Party MK in the 1999 elections. [alce::1251__wikitables_composition__dev::p74]
> By the end of the Knesset term only Meridor and Nehama Ronen remained in the faction. [alce::1251__wikitables_composition__dev::p2]

Cited: alce::1251__wikitables_composition__dev::p0, alce::1251__wikitables_composition__dev::p1, alce::1251__wikitables_composition__dev::p2, alce::1251__wikitables_composition__dev::p74

### `588__wikidata_simple__dev`
> **Multiple species were discovered in the Morrison Formation, including dinosaurs and other organisms**
> Dinosaurs known from the Morrison Formation include the theropods Allosaurus, Ceratosaurus, Ornitholestes, Saurophaganax, and Torvosaurus; the sauropods Brontosaurus, Brachiosaurus, Camarasaurus, and Diplodocus; and the ornithischians Camptosaurus, Dryosaurus, and Stegosaurus. [alce::588__wikidata_simple__dev::p67]
> Other fossils discovered include bivalves, snails, ray-finned fishes, frogs, salamanders, turtles, sphenodonts, lizards, terrestrial and aquatic crocodylomorphans, several species of pterosaur, numerous dinosaur species, and early mammals such as docodonts, multituberculates, symmetrodonts, and triconodonts. [alce::588__wikidata_simple__dev::p1]
> Ctenacodon is a genus of extinct mammal that lived in what is now North America during the Upper Jurassic period, with remains found in the Morrison Formation of Wyoming. [alce::588__wikidata_simple__dev::p54]

Cited: alce::588__wikidata_simple__dev::p1, alce::588__wikidata_simple__dev::p54, alce::588__wikidata_simple__dev::p67

### `422__wikidata_intersection__dev`
_Refused._

### `911__wikidata_simple__dev`
> **Multiple notable graduates from different Southwestern Colleges**
> Southwestern College (Kansas) is a four-year private higher educational institution affiliated with the United Methodist Church located in Winfield, Kansas, and graduated its first class of three in June 1889. [alce::911__wikidata_simple__dev::p3]
> Southwestern Seminary has graduated more than 40,000 students since 1908. [alce::911__wikidata_simple__dev::p8]
> Notable graduates of Arizona Christian University (formerly Southwestern College) include Dr. Mark Bailey, President of Dallas Theological Seminary, and former NBA All-Star and NBA Coach Paul Westphal. [alce::911__wikidata_simple__dev::p0]

Cited: alce::911__wikidata_simple__dev::p0, alce::911__wikidata_simple__dev::p3, alce::911__wikidata_simple__dev::p8

### `40__wikitables_composition__dev`
> **Pakistan Ordnance Factories (POF), Heavy Industries Taxila, Pakistan Aeronautical Complex, and Pakistan Hunting & Sporting Arms Development Company (PHSADC)**
> Pakistan Ordnance Factories (POF) is a major firearms, defence contractor, and military corporation headquartered in Wah Cantt, Punjab, Pakistan, and is the largest defence industrial complex under the Ministry of Defence Production, producing conventional arms & ammo to international standards. [alce::40__wikitables_composition__dev::p15]
> POF produces approximately 70 major products for Army, Navy and Air Force, including automatic rifles, machine guns, mortar and artillery ammunition, aircraft ammunition, anti-aircraft ammunition, tank ammunition, anti-tank ammunition, bombs, grenades, land mines, and pyrotechnics. [alce::40__wikitables_composition__dev::p5]
> Pakistan established enterprises such as Heavy Industries Taxila and Pakistan Aeronautical Complex to produce modern armament. [alce::40__wikitables_composition__dev::p18]
> Pakistan Hunting & Sporting Arms Development Company (PHSADC) is a sector development company, a subsidiary of Pakistan Industrial Development Corporation (PIDC), Ministry of Industries & Production. [alce::40__wikitables_composition__dev::p29]

Cited: alce::40__wikitables_composition__dev::p15, alce::40__wikitables_composition__dev::p18, alce::40__wikitables_composition__dev::p29, alce::40__wikitables_composition__dev::p5

### `341__wikidata_comp__dev`
> **Multiple schools: King Edward VI Grammar School, Eton, and St John's College, Cambridge (William Martin); Masterton Public and state schools (Humphrey O'Leary); Diocesan School for Girls in Auckland and University of Auckland (Sian Elias)**
> Sir William Martin, the first Chief Justice of New Zealand, was educated at King Edward VI Grammar School, Eton, and St John's College, Cambridge. [alce::341__wikidata_comp__dev::p13]
> Humphrey O'Leary, the seventh Chief Justice of New Zealand, attended Masterton Public and state schools after initially attending a local Catholic school. [alce::341__wikidata_comp__dev::p67]
> Dame Sian Elias, the 12th and current Chief Justice of New Zealand, attended Diocesan School for Girls in Auckland and completed a law degree from the University of Auckland in 1970. [alce::341__wikidata_comp__dev::p95]

Cited: alce::341__wikidata_comp__dev::p13, alce::341__wikidata_comp__dev::p67, alce::341__wikidata_comp__dev::p95

### `565__wikidata_simple__dev`
> **Paragliders, reserve parachutes, harnesses, and paragliding accessories**
> Independence Paragliding specializes in the design and manufacture of paragliders in the form of ready-to-fly aircraft as well as reserve parachutes, harnesses and paragliding accessories. [alce::565__wikidata_simple__dev::p1]

Cited: alce::565__wikidata_simple__dev::p1

### `900__wikidata_simple__dev`
> **Deuce Bigalow: Male Gigolo**
> Adam Sandler served as the executive producer for "Deuce Bigalow: Male Gigolo", which was the first film released by the Happy Madison Productions film production company. [alce::900__wikidata_simple__dev::p20]

Cited: alce::900__wikidata_simple__dev::p20

### `251__wikidata_comp__dev`
> **Dan Gilroy**
> Dan Gilroy is an American screenwriter and film director who is best known for writing and directing 'Nightcrawler' (2014). [alce::251__wikidata_comp__dev::p2]
> Frank D. Gilroy was an American playwright, screenwriter, and film producer and director. [alce::251__wikidata_comp__dev::p3]
> Dan Gilroy is Frank D. Gilroy's son, as indicated by the context that Frank Gilroy's three sons from his marriage to Ruth Dorothy Gaydos include Dan Gilroy who is a screenwriter and director. [alce::251__wikidata_comp__dev::p0]

Cited: alce::251__wikidata_comp__dev::p0, alce::251__wikidata_comp__dev::p2, alce::251__wikidata_comp__dev::p3

### `742__wikidata_simple__dev`
> **Sengoku Ace & Sengoku Blade**
> Psikyo was a Japanese video game developer founded in 1992 that mainly developed arcade games, mostly vertically scrolling shoot 'em ups and erotic mahjong games. [alce::742__wikidata_simple__dev::p0]
> In 2004, the game was also ported to PlayStation 2 as part of the 'Psikyo Shooting Collection Vol. 2: Sengoku Ace & Sengoku Blade' by Taito. [alce::742__wikidata_simple__dev::p5]

Cited: alce::742__wikidata_simple__dev::p0, alce::742__wikidata_simple__dev::p5

### `557__wikidata_simple__dev`
> **Stanley Cup**
> The Detroit Red Wings won the National Hockey League's Stanley Cup in 1936 and 1937. [alce::557__wikidata_simple__dev::p59]
> The Red Wings have won the Cup eleven times, more than any other American team in NHL history. [alce::557__wikidata_simple__dev::p15]
> With Ilitch as owner the Wings won the Cup in 1997, 1998, 2002, and 2008. [alce::557__wikidata_simple__dev::p63]

Cited: alce::557__wikidata_simple__dev::p15, alce::557__wikidata_simple__dev::p59, alce::557__wikidata_simple__dev::p63

### `177__wikidata_intersection__dev`
> **Tennis (WTA doubles)**
> Raquel Atawo (née Kops-Jones) is a professional tennis player from the United States of America who is primarily a doubles specialist, winning 18 WTA doubles titles alongside her regular partner, fellow American Abigail Spears. [alce::177__wikidata_intersection__dev::p1]
> Raquel Kops-Jones and Abigail Spears won four titles in the 2012 season at Carlsbad, Seoul, Tokyo, and Osaka, and also won the Western & Southern Open and the Aegon Classic. [alce::177__wikidata_intersection__dev::p0, alce::177__wikidata_intersection__dev::p3]

Cited: alce::177__wikidata_intersection__dev::p0, alce::177__wikidata_intersection__dev::p1, alce::177__wikidata_intersection__dev::p3

### `920__wikidata_simple__dev`
> **Jerry Cantrell, Sean Kinney, Mike Starr, Layne Staley, Mike Inez, and William DuVall**
> Alice in Chains was formed in 1987 by guitarist and vocalist Jerry Cantrell and drummer Sean Kinney, who later recruited bassist Mike Starr and lead vocalist Layne Staley. [alce::920__wikidata_simple__dev::p0]
> Mike Starr was replaced by Mike Inez in 1993. [alce::920__wikidata_simple__dev::p0]
> William DuVall joined the band in 2006 as co-lead vocalist and rhythm guitarist, replacing Staley, who died in 2002. [alce::920__wikidata_simple__dev::p0]

Cited: alce::920__wikidata_simple__dev::p0

### `391__wikidata_intersection__dev`
_Refused._

### `1355__wikidata_simple__dev`
> **Multiple sporting events: Orange Bowl, Joe Gibbs NASCAR racing team, FedEx St. Jude Classic (golf tournament)**
> FedEx served as the title sponsor of the Orange Bowl, becoming the bowl's title sponsor in 1990 and serving as the longest continuous sponsor of any bowl game. [alce::1355__wikidata_simple__dev::p1, alce::1355__wikidata_simple__dev::p13]
> FedEx sponsored the Joe Gibbs NASCAR racing team. [alce::1355__wikidata_simple__dev::p79]
> FedEx sponsored the FedEx St. Jude Classic, a professional golf tournament held in Memphis, Tennessee on the PGA Tour from 1958 through 2018. [alce::1355__wikidata_simple__dev::p64]

Cited: alce::1355__wikidata_simple__dev::p1, alce::1355__wikidata_simple__dev::p13, alce::1355__wikidata_simple__dev::p64, alce::1355__wikidata_simple__dev::p79

### `309__wikidata_intersection__dev`
> **A football match / association football competition**
> The FA Cup Final is a football match that is part of the FA Cup, which is described as 'the world's oldest association football competition, the Football Association Challenge Cup.' [alce::309__wikidata_intersection__dev::p25]
> The FA Cup Finals involving Aston Villa were football matches, such as the 1957 FA Cup Final which was 'a football match played on 4 May 1957 at Wembley Stadium between Aston Villa and Manchester United.' [alce::309__wikidata_intersection__dev::p63]

Cited: alce::309__wikidata_intersection__dev::p25, alce::309__wikidata_intersection__dev::p63

### `335__wikidata_comp__dev`
_Refused._

### `615__wikidata_simple__dev`
> **Hmannan Yazawin, Dutiya Yazawin, and Konbaung Set Yazawin**
> The Royal Historical Commission of the Konbaung Dynasty produced the standard court chronicles of Konbaung era, 'Hmannan Yazawin' (1832) and 'Dutiya Yazawin' (1869). [alce::615__wikidata_simple__dev::p2]
> Konbaung Set Maha Yazawindawgyi is the last and unofficial royal chronicle of Burma covering the Konbaung Dynasty (1752–1885), first published in 1905. [alce::615__wikidata_simple__dev::p3]

Cited: alce::615__wikidata_simple__dev::p2, alce::615__wikidata_simple__dev::p3

### `597__wikidata_simple__dev`
> **Ships registered in England included R&K ships (from 1934 onwards) and UK-registered merchant marine vessels**
> From 1934 some R&K ships were registered in the UK. [alce::597__wikidata_simple__dev::p12]
> In 2012 British merchant marine interests consisted of 1,504 ships of or over, which included ships either directly UK-owned, parent-owned or managed by a British company. [alce::597__wikidata_simple__dev::p8]
> The Merchant Navy comprises the seagoing commercial interests of UK-registered ships and their crews. [alce::597__wikidata_simple__dev::p34]

Cited: alce::597__wikidata_simple__dev::p12, alce::597__wikidata_simple__dev::p34, alce::597__wikidata_simple__dev::p8

### `945__wikidata_simple__dev`
> **Lee Rose, Peter Barnes, and Peter Mumford are employed as lighting designers**
> Lee Rose (born July 30, 1955) is an American lighting designer that works in the mediums of film, television, stage, and concerts. [alce::945__wikidata_simple__dev::p60]
> Peter Barnes (born 25 February 1955 in Enfield, London, United Kingdom) is a lighting designer, lighting director, show producer and set designer. [alce::945__wikidata_simple__dev::p87]
> Peter Mumford is an international lighting designer who trained at the Central School of Art in London. [alce::945__wikidata_simple__dev::p86]

Cited: alce::945__wikidata_simple__dev::p60, alce::945__wikidata_simple__dev::p86, alce::945__wikidata_simple__dev::p87

### `318__wikidata_intersection__dev`
> **Multiple matches between Burnley F.C. and Manchester City F.C.**
> Burnley lost a league fixture when they were beaten 0–3 by Manchester City at Hyde Road on 4 September 1920. [alce::318__wikidata_intersection__dev::p1]
> Burnley were drawn against Manchester City in the Lancashire Senior Cup semi-finals, with the game on 9 May 1921 ending in a 0–2 defeat for Burnley. [alce::318__wikidata_intersection__dev::p2]
> Burnley clinched their second league championship on the last day of the season at Maine Road, Manchester with a 2–1 victory against Manchester City with goals from Brian Pilkington and Trevor Meredith in the 1959–60 season. [alce::318__wikidata_intersection__dev::p15, alce::318__wikidata_intersection__dev::p35]

Cited: alce::318__wikidata_intersection__dev::p1, alce::318__wikidata_intersection__dev::p15, alce::318__wikidata_intersection__dev::p2, alce::318__wikidata_intersection__dev::p35

### `22__wikitables_composition__dev`
> **Fallen from Heaven (1990) and Captain Pantoja and the Special Services (2000)**
> Fallen from Heaven is a 1990 Peruvian drama film directed by Francisco José Lombardi that was selected as the Peruvian entry for the Best Foreign Language Film at the 63rd Academy Awards. [alce::22__wikitables_composition__dev::p19]
> Captain Pantoja and the Special Services is a 2000 Spanish-Peruvian film co-production directed by Francisco J. Lombardi that was chosen as Peru's official Best Foreign Language Film submission at the 72nd Academy Awards. [alce::22__wikitables_composition__dev::p7]

Cited: alce::22__wikitables_composition__dev::p19, alce::22__wikitables_composition__dev::p7

### `766__wikidata_simple__dev`
> **Table Mountain**
> Cape Town's urban geography is influenced by the contours of Table Mountain, its surrounding peaks, the Durbanville Hills, and the expansive lowland region known as the Cape. [alce::766__wikidata_simple__dev::p22]
> The Cape Peninsula, which lies entirely within the city of Cape Town, has the highest concentration of threatened species of any continental area of equivalent size in the world. [alce::766__wikidata_simple__dev::p22]
> Cape Town is a coastal city in South Africa. [alce::766__wikidata_simple__dev::p2]

Cited: alce::766__wikidata_simple__dev::p2, alce::766__wikidata_simple__dev::p22

### `1356__wikidata_simple__dev`
> **Blame It on the Bossa Nova**
> "Blame It on the Bossa Nova" is a song written by Cynthia Weil (lyrics) and Barry Mann which was a 1963 hit single for Eydie Gormé, reaching number 7 on the Hot 100 in "Billboard" in March 1963. [alce::1356__wikidata_simple__dev::p32]

Cited: alce::1356__wikidata_simple__dev::p32

### `600__wikidata_simple__dev`
> **Multiple jukebox musicals and films including "Mamma Mia!", "Jersey Boys", "Movin' Out", "Rock of Ages", "Tommy", "The Wall", "Buddy – The Buddy Holly Story", "An American in Paris", "Rock, Rock, Rock", "Rock Around the Clock", and others**
> Examples are "Jam Session", "An American in Paris" (1951), "Rock, Rock, Rock" (1956); "Rock Around the Clock" (1956) and "Juke Box Rhythm" (1959). [alce::600__wikidata_simple__dev::p0]
> Both the movies of The Who's "Tommy" and of Pink Floyd's "The Wall" adapted the entire song cycle of a single album which already revolved around a fictional character. [alce::600__wikidata_simple__dev::p4]
> "Buddy – The Buddy Holly Story", the musical about the life of Buddy Holly which ran in the West End for 13 years from 1989 to 2003, had achieved success. [alce::600__wikidata_simple__dev::p4]
> A surge in popularity was led by the success of "Mamma Mia!", built around the music of ABBA. [alce::600__wikidata_simple__dev::p3]
> Some jukebox musicals, like "Lennon" and "Good Vibrations" have been critical and financial flops, while others, like "Jersey Boys" and "All Shook Up" have been popular with both fans and critics. [alce::600__wikidata_simple__dev::p3]
> These have included "Movin' Out" (2002, based on the tunes of Billy Joel), "Jersey Boys" (2006, The Four Seasons), "Rock of Ages" (2009, featuring classic rock of the 1980s) and many others. [alce::600__wikidata_simple__dev::p6]
> Similar musicals have been built around the canon of a particular pop group including "Mamma Mia!" (1999, based on the songs of ABBA), "Our House" (2002, based on the songs of Madness) and "We Will Rock You" (2002). [alce::600__wikidata_simple__dev::p6]

Cited: alce::600__wikidata_simple__dev::p0, alce::600__wikidata_simple__dev::p3, alce::600__wikidata_simple__dev::p4, alce::600__wikidata_simple__dev::p6

### `237__wikidata_comp__dev`
> **Farren Blackburn**
> Christina Hodson is a screenwriter whose screenplays include "Shut In" (2016) and "Bumblebee" (2018). [alce::237__wikidata_comp__dev::p3]
> Hodson's psychological thriller script "Shut In" was bought by David Linde's Lava Bear Films. The film, starring Naomi Watts, was directed by Farren Blackburn and released 11 November 2016. [alce::237__wikidata_comp__dev::p2]
> As of November 2016, she was working on the script for the "Transformers" movie that will focus on Bumblebee, set to be released June 2018. Travis Knight, director of "Kubo and the Two Strings", will direct. [alce::237__wikidata_comp__dev::p0]

Cited: alce::237__wikidata_comp__dev::p0, alce::237__wikidata_comp__dev::p2, alce::237__wikidata_comp__dev::p3

### `549__wikitables_simple__dev`
_Refused._

### `109__wikidata_comp__dev`
> **Sidney Lumet**
> Jay Presson Allen wrote the novel 'Just Tell Me What You Want!' in 1969, with the idea of turning it into a screenplay, and sent it to Sidney Lumet, who wanted to direct it. [alce::109__wikidata_comp__dev::p22]

Cited: alce::109__wikidata_comp__dev::p22

### `734__wikidata_simple__dev`
> **Nottingham Open**
> Barty won the Nottingham Open on grass for her second career WTA title. [alce::734__wikidata_simple__dev::p2]
> She defeated home favourite and British No. 1 Konta in the final. [alce::734__wikidata_simple__dev::p2]

Cited: alce::734__wikidata_simple__dev::p2

### `482__wikitables_simple__dev`
> **Geothermal power stations with capacity of at least 10 MW include: Hatchōbaru Geothermal Power Plant (112 MW), Corbetti and Tulu Moye Geothermal Power Stations (~500 MW each), and San Jacinto Tizate geothermal plant (10 MW)**
> Hatchōbaru Geothermal Power Plant is a large geothermal power station in Ōita Prefecture, Japan with a capacity of 112 MW, making it the largest geothermal power plant in the country. [alce::482__wikitables_simple__dev::p15]
> Corbetti Geothermal Power Station and Tulu Moye Geothermal Power Station are both in exploration phase with a capacity of approximately 500 megawatts each. [alce::482__wikitables_simple__dev::p13]
> Ram Power currently operates the 10 MW San Jacinto Tizate geothermal plant. [alce::482__wikitables_simple__dev::p64]

Cited: alce::482__wikitables_simple__dev::p13, alce::482__wikitables_simple__dev::p15, alce::482__wikitables_simple__dev::p64

### `696__wikidata_simple__dev`
> **Multiple railway stations were operated by Sydney Trains, including Campsie railway station, Domestic Airport railway station, and St James railway station**
> Campsie railway station is located on the Bankstown line, serving the Sydney suburb of Campsie. It is served by Sydney Trains T3 Bankstown line services. [alce::696__wikidata_simple__dev::p55]
> Domestic Airport railway station, Sydney Domestic Airport is a train station located on the Airport Link, serving Terminals 2 and 3 at Sydney Airport, Australia. The station is operated by Sydney Trains with T8 Airport & South line services. [alce::696__wikidata_simple__dev::p65]
> St James railway station is a heritage-listed underground commuter rail station that is located on the City Circle, at the northern end of Hyde Park in the Sydney central business district of New South Wales, Australia. It is served by Sydney Trains T2 Inner West & Leppington, T3. [alce::696__wikidata_simple__dev::p75]

Cited: alce::696__wikidata_simple__dev::p55, alce::696__wikidata_simple__dev::p65, alce::696__wikidata_simple__dev::p75

### `222__wikidata_intersection__dev`
> **Singam 2**
> Devi Sri Prasad will be the composer of the flick and collaborating again with Vikram for the second time after Kanthaswamy and Hari for the fifth time after Aaru, Venghai, Singam & Singam II. [alce::222__wikidata_intersection__dev::p41]

Cited: alce::222__wikidata_intersection__dev::p41

### `621__wikidata_simple__dev`
> **Alibi (1931)**
> Leslie S. Hiscott was an English film director and screenwriter who made over sixty films between 1925 and 1956. [alce::621__wikidata_simple__dev::p1]
> He directed "Alibi" (1931), the first ever depiction of Hercule Poirot, Agatha Christie's Belgian detective, with Austin Trevor in the lead role. [alce::621__wikidata_simple__dev::p1]
> He directed a follow-up, "Black Coffee" (also 1931), also starring Trevor. [alce::621__wikidata_simple__dev::p1]

Cited: alce::621__wikidata_simple__dev::p1

### `459__wikidata_intersection__dev`
> **Jessie Carney Smith**
> Jessie Carney Smith is an American librarian and educator, currently serving as Dean of the Fisk University Library and Camille Cosby Distinguished Chair in the Humanities. [alce::459__wikidata_intersection__dev::p89]
> James Raymond Lawson graduated from Fisk University and was the president of Fisk University from 1967 to 1975, making him both an alumnus and employee of the institution. [alce::459__wikidata_intersection__dev::p52]

Cited: alce::459__wikidata_intersection__dev::p52, alce::459__wikidata_intersection__dev::p89

### `116__wikidata_comp__dev`
_Refused._

### `703__wikidata_simple__dev`
> **Volvo XC60**
> The Volvo XC60 is a compact luxury crossover SUV manufactured and marketed by Swedish automaker Volvo Cars since 2008. [alce::703__wikidata_simple__dev::p27]
> The Volvo XC60 has been Volvo's best selling car, with sales increasing every year since its release in 2008. [alce::703__wikidata_simple__dev::p23]

Cited: alce::703__wikidata_simple__dev::p23, alce::703__wikidata_simple__dev::p27

### `394__wikidata_intersection__dev`
> **49th Parallel, The Life and Death of Colonel Blimp, A Matter of Life and Death, Black Narcissus, The Red Shoes, and The Tales of Hoffmann**
> Emeric Pressburger was a Hungarian British screenwriter, film director, and producer who is best known for his series of film collaborations with Michael Powell, in an award-winning collaboration partnership known as the Archers and produced a series of films, notably '49th Parallel' (1941), 'The Life and Death of Colonel Blimp' (1943), 'A Matter of Life and Death' (1946, also called 'Stairway to Heaven'), 'Black Narcissus' (1947), 'The Red Shoes' (1948), and 'The Tales of Hoffmann' (1951). [alce::394__wikidata_intersection__dev::p1]
> Working together as co-producers, writers and directors in a partnership they dubbed 'The Archers', Powell and Pressburger made 19 feature films, with their films jointly credited as 'Written, Produced and Directed by Michael Powell and Emeric Pressburger.' [alce::394__wikidata_intersection__dev::p16]

Cited: alce::394__wikidata_intersection__dev::p1, alce::394__wikidata_intersection__dev::p16

### `238__wikidata_intersection__dev`
> **The Ghost of Tolston's Manor**
> Oscar Micheaux was an African-American author, film director and independent producer of more than 44 films. [alce::238__wikidata_intersection__dev::p2]
> A film with the working title 'The Ghost of Tolston's Manor' was produced by Oscar Micheaux with a scenario (script) also by Oscar Micheaux. [alce::238__wikidata_intersection__dev::p27]

Cited: alce::238__wikidata_intersection__dev::p2, alce::238__wikidata_intersection__dev::p27

### `537__wikitables_simple__dev`
> **Multiple professional wrestling organizations own streaming services**
> WWE Network is a subscription-based video streaming service owned by the WWE. [alce::537__wikitables_simple__dev::p2]
> Global Wrestling Network (GWN) is a video streaming service and mobile app owned by Anthem Wrestling Exhibitions, a subsidiary of Anthem Sports & Entertainment and parent company of Impact Wrestling. [alce::537__wikitables_simple__dev::p14]
> New Japan Pro-Wrestling World is a subscription-based video streaming service owned by New Japan Pro-Wrestling. [alce::537__wikitables_simple__dev::p7]
> Honor Club is a OTT streaming service owned by professional wrestling promotion Ring of Honor. [alce::537__wikitables_simple__dev::p95]

Cited: alce::537__wikitables_simple__dev::p14, alce::537__wikitables_simple__dev::p2, alce::537__wikitables_simple__dev::p7, alce::537__wikitables_simple__dev::p95

### `502__wikitables_simple__dev`
> **There are currently 47 sumo stables (as of 2018), including Fujishima stable, Kise stable, Tagonoura stable, and Musashigawa stable**
> There are currently 47 'heya' (sumo stables) as of 2018, all of which belong to one of six 'ichimon' (groupings of stables). [alce::502__wikitables_simple__dev::p94]
> Specific examples of sumo stables include Fujishima stable (formerly known as Musashigawa stable), which is part of the Dewanoumi ichimon. [alce::502__wikitables_simple__dev::p4]
> Kise stable, also known as Kimura Sehei stable, was a heya or stable of sumo wrestlers, part of the Tatsunami ichimon. [alce::502__wikitables_simple__dev::p89]
> Tagonoura stable (formerly Naruto stable) is a stable of sumo wrestlers, one of the Nishonoseki group of stables. [alce::502__wikitables_simple__dev::p24]
> Musashigawa stable is a stable of sumo wrestlers. [alce::502__wikitables_simple__dev::p14]

Cited: alce::502__wikitables_simple__dev::p14, alce::502__wikitables_simple__dev::p24, alce::502__wikitables_simple__dev::p4, alce::502__wikitables_simple__dev::p89, alce::502__wikitables_simple__dev::p94

### `559__wikidata_simple__dev`
> **The Philadelphia Story**
> Joseph L. Mankiewicz was an American film director, screenwriter, and producer. [alce::559__wikidata_simple__dev::p1]
> He produced more than twenty films including 'The Philadelphia Story' which was nominated for the Academy Award for Best Picture in 1941. [alce::559__wikidata_simple__dev::p2]
> In 1944, he produced 'The Keys of' (title continues in next source). [alce::559__wikidata_simple__dev::p2]

Cited: alce::559__wikidata_simple__dev::p1, alce::559__wikidata_simple__dev::p2

### `1357__wikidata_simple__dev`
> **National Football League (NFL)**
> The Miami Dolphins compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) East division. [alce::1357__wikidata_simple__dev::p0]
> They began play in the AFL in 1966. [alce::1357__wikidata_simple__dev::p0]

Cited: alce::1357__wikidata_simple__dev::p0

### `425__wikidata_intersection__dev`
> **The Man from Laramie**
> Yordan wrote "The Man from Laramie" (1955) for James Stewart and director Anthony Mann, the last film Stewart and Mann made together. [alce::425__wikidata_intersection__dev::p39]

Cited: alce::425__wikidata_intersection__dev::p39

### `327__wikidata_comp__dev`
_Refused._

### `181__wikidata_intersection__dev`
> **2014 Japanese Grand Prix**
> The 2014 Japanese Grand Prix was a Formula One motor race held on 5 October 2014 at the Suzuka Circuit in Suzuka, Mie, and the 44-lap race was won by Mercedes driver Lewis Hamilton. [alce::181__wikidata_intersection__dev::p0]

Cited: alce::181__wikidata_intersection__dev::p0

### `554__wikidata_simple__dev`
> **Songs composed by Boudleaux Bryant include "Rocky Top," "Love Hurts," "All I Have to Do Is Dream," "Bye Bye Love," and "Wake Up Little Susie"**
> Boudleaux Bryant and his wife Felice were best known for songs such as 'Rocky Top,' 'Love Hurts' (credited solely to Boudleaux), and numerous hits by the Everly Brothers, including 'All I Have to Do Is Dream' (credited solely to Boudleaux), 'Bye Bye Love' and 'Wake Up Little Susie.' [alce::554__wikidata_simple__dev::p0]

Cited: alce::554__wikidata_simple__dev::p0

### `477__wikitables_simple__dev`
> **Hormones found in Homo sapiens include epinephrine, norepinephrine, ACTH, glucagon, thyroxine, testosterone, estrogen, estradiol, follicle stimulating hormone, and luteinising hormone**
> Hominins have evolved larger thyroid and adrenal glands which enable them to utilize the energy in carbohydrates and fatty acids more readily and efficiently. These organs are responsible for releasing hormones including epinephrine, norepinephrine, adrenocorticotropic hormone (ACTH), glucagon, and thyroxine. [alce::477__wikitables_simple__dev::p1]
> Sexual differentiation in the human brain from the undifferentiated state is triggered by testosterone from the fetal testis. Testosterone is converted to estrogen in the brain through the action of the enzyme aromatase. [alce::477__wikitables_simple__dev::p62]
> Within the brain, testosterone is aromatized (to estradiol), which is the principal active hormone for developmental influences. The human testis secretes high levels of testosterone from about week 8 of fetal life until 5–6 months after birth. [alce::477__wikitables_simple__dev::p14]
> Follicle stimulating hormone, luteinising hormone, and estradiol may encourage ovulation in women exposed to semen. [alce::477__wikitables_simple__dev::p81]

Cited: alce::477__wikitables_simple__dev::p1, alce::477__wikitables_simple__dev::p14, alce::477__wikitables_simple__dev::p62, alce::477__wikitables_simple__dev::p81

### `307__wikidata_intersection__dev`
> **World Series**
> The St. Louis Cardinals have won 11 World Series championships, the second-most in Major League Baseball (behind the New York Yankees) and the most in the National League. [alce::307__wikidata_intersection__dev::p2]
> The St. Louis Cardinals are an American professional baseball team based in St. Louis, Missouri, competing in Major League Baseball (MLB) as a member club of the National League (NL) Central division. [alce::307__wikidata_intersection__dev::p2]

Cited: alce::307__wikidata_intersection__dev::p2

### `604__wikidata_simple__dev`
> **Pharrell Williams and Marina and the Diamonds**
> Pharrell Williams, of the groups The Neptunes and N.E.R.D., also experiences synesthesia and used it as the basis of the album 'Seeing Sounds'. [alce::604__wikidata_simple__dev::p31]
> Singer/songwriter Marina and the Diamonds experiences music → color synesthesia and reports colored days of the week. [alce::604__wikidata_simple__dev::p31]

Cited: alce::604__wikidata_simple__dev::p31

### `1006__wikidata_comp__dev`
> **MIT Sloan School of Management and LSE (London School of Economics)**
> Robert Cox Merton is a professor at the MIT Sloan School of Management and co-founded Long-Term Capital Management in 1993. [alce::1006__wikidata_comp__dev::p53]
> Victor Haghani, a co-founder of Long-Term Capital Management in 1993, has taught at the LSE (London School of Economics) where he is a Senior Research Associate. [alce::1006__wikidata_comp__dev::p23]
> Among LTCM's principals were several former university professors, including two Nobel Prize-winning economists. [alce::1006__wikidata_comp__dev::p5]

Cited: alce::1006__wikidata_comp__dev::p23, alce::1006__wikidata_comp__dev::p5, alce::1006__wikidata_comp__dev::p53

### `1103__wikidata_intersection__dev`
> **The Manchester Derby**
> The Manchester derby refers to football matches between Manchester City and Manchester United, first contested in 1881. [alce::1103__wikidata_intersection__dev::p4]
> The teams have played 177 matches in all competitions, United winning 73, City 52, and the remaining 52 having been drawn. [alce::1103__wikidata_intersection__dev::p4]
> Fixtures between the clubs are referred to as the Manchester Derby. [alce::1103__wikidata_intersection__dev::p60]

Cited: alce::1103__wikidata_intersection__dev::p4, alce::1103__wikidata_intersection__dev::p60

### `1253__wikitables_composition__dev`
> **Tastil volcanic complex, Pairique volcanic complex, and Rincon volcanic complex**
> Tastil volcanic complex is a volcanic complex in Argentina. [alce::1253__wikitables_composition__dev::p28]
> Pairique volcanic complex is a volcanic complex in the Jujuy Province, Argentina. [alce::1253__wikitables_composition__dev::p43]
> Rincon volcanic complex is a volcano in Argentina. [alce::1253__wikitables_composition__dev::p1]

Cited: alce::1253__wikitables_composition__dev::p1, alce::1253__wikitables_composition__dev::p28, alce::1253__wikitables_composition__dev::p43

### `55__wikitables_composition__dev`
> **Minamiashigara**
> Minamiashigara was elevated in status to that of a town on April 1, 1940, and annexed neighboring Fukusawa, Okamoto and Kitaashigara villages in 1955, and was elevated to city status on April 1, 1972. [alce::55__wikitables_composition__dev::p21]
> On April 1, 1972, part of Ashigarakami District became the city of Minamiashigara. [alce::55__wikitables_composition__dev::p1]

Cited: alce::55__wikitables_composition__dev::p1, alce::55__wikitables_composition__dev::p21

### `889__wikidata_simple__dev`
> **Multiple heads of Chelsea F.C. across different time periods**
> Joe Mears (1905 – 30 June 1966) was chairman of Chelsea Football Club and became Chelsea chairman in 1940 following the death of Colonel Crisp. [alce::889__wikidata_simple__dev::p11]
> Brian Mears (25 April 1931 – 28 July 2009) was a chairman of Chelsea Football Club and took over as chairman following the death of Len Withey. [alce::889__wikidata_simple__dev::p50]
> Guy Laurence was appointed as the club's Chief Executive on 11 January 2018. [alce::889__wikidata_simple__dev::p2]

Cited: alce::889__wikidata_simple__dev::p11, alce::889__wikidata_simple__dev::p2, alce::889__wikidata_simple__dev::p50

### `17__wikitables_composition__dev`
> **KOSS and KFXM-LP**
> KOSS (1380 AM, "NewsTalk 1380") is a commercial radio station broadcasting a news/talk format licensed to Lancaster, California, United States. [alce::17__wikitables_composition__dev::p95]
> KFXM-LP (98.3 FM) is a low-power FM radio station broadcasting an oldies music format, licensed to Lancaster, California, United States. [alce::17__wikitables_composition__dev::p4]

Cited: alce::17__wikitables_composition__dev::p4, alce::17__wikitables_composition__dev::p95

### `70__wikitables_composition__dev`
> **1968–69 Northern Rugby Football League season**
> Leeds won their second Championship in the 1968–69 Rugby Football League season when they beat Castleford 16-14 in the Championship Final. [alce::70__wikitables_composition__dev::p0]

Cited: alce::70__wikitables_composition__dev::p0

### `849__wikidata_simple__dev`
_Refused._

### `513__wikitables_simple__dev`
> **Arlberg Road Tunnel, Kresna Gorge Tunnel**
> The Arlberg Road Tunnel has a length of 13,976 metres (approximately 13.976 km), making it Austria's longest road tunnel. [alce::513__wikitables_simple__dev::p17]
> The Kresna Gorge Tunnel was a planned tunnel with a proposed length of over 15 km, which would place it among the longest road tunnels in the world. [alce::513__wikitables_simple__dev::p18]

Cited: alce::513__wikitables_simple__dev::p17, alce::513__wikitables_simple__dev::p18

### `526__wikitables_simple__dev`
> **Male stage names of drag kings include Mo B. Dick, Gage Gatlyn, Murray Hill, Ian Blakk, Anson Reign, Damian Matrix, Owen McCord, Xander Kinidy, Remington Steal, Flare, Freddy Prinze Charming, Amadeus Karmani York, Richard Cranium, Gunner Gatlyn, Dred, Will Ryder, Buck Naked, Spikey Van Dykey, Smack Diaz, Stanley Knife, and Razor Blade**
> Some of these names have become Cornerstones in the King community, including Mo B. Dick, Gage Gatlyn, Murray Hill, Ian Blakk, Anson Reign, Damian Matrix, Owen McCord, Xander Kinidy, Remington Steal, Flare, Freddy Prinze Charming, Amadeus Karmani York, Richard Cranium, Gunner Gatlyn, Dred, Will Ryder, Buck Naked, Spikey Van Dykey. [alce::526__wikitables_simple__dev::p0]
> Drag kings often take on playful names to reflect their stage personas. Sexual based names like 'Smack Diaz' are common, as are general macho names like 'Stanley Knife' and 'Razor Blade'. [alce::526__wikitables_simple__dev::p1]

Cited: alce::526__wikitables_simple__dev::p0, alce::526__wikitables_simple__dev::p1

### `1358__wikidata_simple__dev`
> **Galway United F.C.**
> Galway United Football Club is an Irish association football club based in Galway. [alce::1358__wikidata_simple__dev::p7]
> They play in the League of Ireland First Division. [alce::1358__wikidata_simple__dev::p7]

Cited: alce::1358__wikidata_simple__dev::p7

### `976__wikidata_comp__dev`
> **Doctor Who (1974-1977), Private Schulz, The Charmer, Take Me Home, Friday on My Mind, Taggart, Rebus, and others**
> Philip Hinchcliffe joined the BBC to produce "Doctor Who" in one of its most popular eras from 1974 to 1977. [alce::976__wikidata_comp__dev::p0]
> He remained with the BBC as a producer for several years, working on series such as "Private Schulz", before launching a freelance career in the mid-1980s, which included making "The Charmer" for London Weekend Television in 1987. [alce::976__wikidata_comp__dev::p0]
> He was engaged as an Executive Producer by Scottish Television from 1998 to 2001, overseeing series including "Taggart" and the John Hannah episodes of "Rebus". [alce::976__wikidata_comp__dev::p2]
> He also worked on "Take Me Home", "Friday on My Mind" and many others. [alce::976__wikidata_comp__dev::p2]

Cited: alce::976__wikidata_comp__dev::p0, alce::976__wikidata_comp__dev::p2

### `716__wikidata_simple__dev`
> **Multiple geographic features including mountains, national parks, islands, and rivers**
> To the west are the limestone mountains of the Phuket range which are mostly covered with forest, with Khao Sok National Park found there. [alce::716__wikidata_simple__dev::p4]
> To the east the hills of the Nakhon Si Thammarat mountain range start to rise, protected in the Tai Rom Yen National Park. [alce::716__wikidata_simple__dev::p4]
> Many islands in the Gulf of Thailand belong to the district, including the tourist islands Ko Samui, Ko Pha Ngan and Ko Tao, as well as the Ko Ang Thong Marine National Park. [alce::716__wikidata_simple__dev::p4]
> The main rivers of Surat Thani Province are the Tapi River and the Phum Duang River. [alce::716__wikidata_simple__dev::p4]
> Khao Tha Phet is a hill near the town of Surat Thani with an altitude of about 210m above sea level. [alce::716__wikidata_simple__dev::p15]

Cited: alce::716__wikidata_simple__dev::p15, alce::716__wikidata_simple__dev::p4

### `552__wikitables_simple__dev`
> **Functions that map data of arbitrary size to fixed-size data**
> A hash function is any function that can be used to map data of arbitrary size to data of a fixed size. [alce::552__wikitables_simple__dev::p0, alce::552__wikitables_simple__dev::p1]
> The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. [alce::552__wikitables_simple__dev::p0, alce::552__wikitables_simple__dev::p1]
> Hash functions are often used in combination with a hash table, a common data structure used in computer software for rapid data lookup. [alce::552__wikitables_simple__dev::p0, alce::552__wikitables_simple__dev::p1]
> Hash functions take a message of any length as input, and output a short, fixed length hash, which can be used in (for example) a digital signature. [alce::552__wikitables_simple__dev::p9]

Cited: alce::552__wikitables_simple__dev::p0, alce::552__wikitables_simple__dev::p1, alce::552__wikitables_simple__dev::p9

### `824__wikidata_simple__dev`
> **Compton Bennett directed multiple films, most notably "The Seventh Veil" (1945) and "King Solomon's Mines" (1950)**
> Compton Bennett was an English film director, writer and producer who is perhaps best known for directing the 1945 film 'The Seventh Veil' and the 1950 version of the film 'King Solomon's Mines'. [alce::824__wikidata_simple__dev::p0]
> He also directed 'Madness of the Heart' (1949) with Margaret Lockwood, and produced four films in 1957: 'After the Ball', 'Man-Eater', 'That Woman Opposite' and 'The Flying Scot'. [alce::824__wikidata_simple__dev::p1, alce::824__wikidata_simple__dev::p3]

Cited: alce::824__wikidata_simple__dev::p0, alce::824__wikidata_simple__dev::p1, alce::824__wikidata_simple__dev::p3

### `476__wikitables_simple__dev`
> **Monocle and Eulenspiegel are satirical magazines**
> Monocle was an American satirical magazine, published irregularly from the late 1950s until the mid-sixties. [alce::476__wikitables_simple__dev::p27]
> Eulenspiegel – Das Satiremagazin is a German humor and satirical magazine. [alce::476__wikitables_simple__dev::p15]

Cited: alce::476__wikitables_simple__dev::p15, alce::476__wikitables_simple__dev::p27

### `535__wikitables_simple__dev`
> **Grand Mosque of Kuwait, Grand Mosque of Dubai, Al Fateh Grand Mosque, and Grand Mosque of Paris**
> The Grand Mosque in Kuwait is the largest and the official mosque in the country of Kuwait, with the main prayer hall being wide on all sides and having teakwood doors, and the dome decorated with the 99 names of God. [alce::535__wikitables_simple__dev::p8]
> The Grand Mosque in Dubai is located in the Bur Dubai area and is the hub of Dubai's religious and cultural life, holding up to 1,200 worshippers. [alce::535__wikitables_simple__dev::p5]
> Al-Fateh Grand Mosque is one of the largest mosques in the world, encompassing 6,500 square meters with the capacity to accommodate over 7,000 worshippers, and is the largest place of worship in Bahrain. [alce::535__wikitables_simple__dev::p81]
> The Grand Mosque of Paris is one of the largest mosques in France and is the oldest mosque in France's metropolitan area, playing an important role in promoting the visibility of Islam and Muslims in France. [alce::535__wikitables_simple__dev::p0]

Cited: alce::535__wikitables_simple__dev::p0, alce::535__wikitables_simple__dev::p5, alce::535__wikitables_simple__dev::p8, alce::535__wikitables_simple__dev::p81

### `631__wikidata_simple__dev`
> **Six radio stations, six news websites, and a satellite television network (Multi TV)**
> Multimedia Group Limited has six radio stations, six news websites and a satellite television network. [alce::631__wikidata_simple__dev::p0]
> The group operates Multi TV, a satellite television station with several channels. [alce::631__wikidata_simple__dev::p0]

Cited: alce::631__wikidata_simple__dev::p0

### `735__wikidata_simple__dev`
> **Buffy the Vampire Slayer**
> Mutant Enemy Productions is a production company that was created in 1996 by Joss Whedon to produce "Buffy the Vampire Slayer." [alce::735__wikidata_simple__dev::p1]

Cited: alce::735__wikidata_simple__dev::p1

### `240__wikidata_intersection__dev`
> **World Snooker Championship**
> Stephen Hendry won multiple World Snooker Championships that were sponsored by cigarette manufacturer Embassy, including the 1992, 1993, 1994, and 1996 tournaments. [alce::240__wikidata_intersection__dev::p0, alce::240__wikidata_intersection__dev::p1, alce::240__wikidata_intersection__dev::p3, alce::240__wikidata_intersection__dev::p5]

Cited: alce::240__wikidata_intersection__dev::p0, alce::240__wikidata_intersection__dev::p1, alce::240__wikidata_intersection__dev::p3, alce::240__wikidata_intersection__dev::p5

### `44__wikitables_composition__dev`
> **Powder Ridge Ski Area**
> Powder Ridge Ski Area is a relatively small ski area located in Middlefield, Connecticut. [alce::44__wikitables_composition__dev::p14]
> The vertical drop is from the summit at an elevation of to the base at, and the park's total area covers facilities for freestyle skiing, snowboarding, snowtubing, racing, and snowbiking. [alce::44__wikitables_composition__dev::p14]

Cited: alce::44__wikitables_composition__dev::p14

### `541__wikitables_simple__dev`
> **FN FAL, M14, H&K G3, Heckler & Koch HK417, SR-25, Mk 14 Enhanced Battle Rifle, and ARX200**
> Battle rifle is a post-World War II term for military service rifles that are fed ammunition via detachable magazines and fire a full-powered rifle cartridge. [alce::541__wikitables_simple__dev::p0]
> Full-powered automatic rifles include the FN FAL, M14 and H&K G3. [alce::541__wikitables_simple__dev::p0]
> For medium to long range engagements the Heckler & Koch HK417, SR-25 marksman rifle, and Mk 14 Enhanced Battle Rifle are also used. [alce::541__wikitables_simple__dev::p57]
> The Italian Army is planning to introduce two configurations of the ARX200; a battle rifle with a foldable telescoping stock, capable of fully automatic and semi-automatic fire. [alce::541__wikitables_simple__dev::p73]

Cited: alce::541__wikitables_simple__dev::p0, alce::541__wikitables_simple__dev::p57, alce::541__wikitables_simple__dev::p73

### `332__wikidata_intersection__dev`
> **En Thangai Kalyani**
> En Thangai Kalyani is a Tamil film released in 1988, directed and produced by T. Rajendar. [alce::332__wikidata_intersection__dev::p26]
> The soundtrack was written and composed by T. Rajendar. [alce::332__wikidata_intersection__dev::p26]

Cited: alce::332__wikidata_intersection__dev::p26

### `457__wikidata_intersection__dev`
> **The Ladykillers (2004)**
> Until 'The Ladykillers' (2004), Joel received sole credit for directing and Ethan for producing, but starting with this film they were able to share the director credit. [alce::457__wikidata_intersection__dev::p3, alce::457__wikidata_intersection__dev::p5]
> The Ladykillers (2004) was the first film where Ethan Coen received credit as both producer and director, marking a change from the previous guild rules that had prevented multiple director credits. [alce::457__wikidata_intersection__dev::p3, alce::457__wikidata_intersection__dev::p5]

Cited: alce::457__wikidata_intersection__dev::p3, alce::457__wikidata_intersection__dev::p5

### `782__wikidata_simple__dev`
> **1973 NASCAR Winston Cup Championship and 1975 Daytona 500**
> Benny Parsons became famous as the 1973 NASCAR Winston Cup (now Monster Energy NASCAR Cup) champion. [alce::782__wikidata_simple__dev::p1]
> Benny Parsons won the 1975 Daytona 500, taking the lead three laps from the finish when leader David Pearson spun on the backstretch. [alce::782__wikidata_simple__dev::p84]
> Parsons also won the 1968 and 1969 ARCA championships. [alce::782__wikidata_simple__dev::p16]

Cited: alce::782__wikidata_simple__dev::p1, alce::782__wikidata_simple__dev::p16, alce::782__wikidata_simple__dev::p84

### `561__wikidata_simple__dev`
> **Mary Joe Fernández**
> Mary Joe Fernández was a competitor in women's doubles tennis at the 1996 Summer Olympics in Atlanta. [alce::561__wikidata_simple__dev::p46]
> She won a second straight women's doubles gold medal in partnership with Gigi Fernández. [alce::561__wikidata_simple__dev::p46]

Cited: alce::561__wikidata_simple__dev::p46

### `558__wikidata_simple__dev`
_Refused._

### `651__wikidata_simple__dev`
> **Rubén Reyes**
> Rubén Reyes is a linguist and expert on the history and culture of the Garifuna people, who created the world's first tri-lingual dictionary of Garifuna, 'Garudia: Garifuna Trilingual Dictionary (Garifuna-English-Spanish).' [alce::651__wikidata_simple__dev::p26]

Cited: alce::651__wikidata_simple__dev::p26

### `964__wikidata_comp__dev`
> **University of Texas at Austin**
> Dan Bartlett was a Counselor to the President in the administration of George W. Bush and graduated from the University of Texas at Austin with a Bachelor of Arts in political science. [alce::964__wikidata_comp__dev::p5]

Cited: alce::964__wikidata_comp__dev::p5

### `79__wikitables_composition__dev`
_Refused._

### `67__wikitables_composition__dev`
> **Zachary Sukunda**
> Zachary Sukunda is a Canadian soccer player who currently plays for HFX Wanderers FC of the Canadian Premier League. [alce::67__wikitables_composition__dev::p18]
> On 29 November 2018, Sukunda was announced as HFX Wanderers FC first signing. [alce::67__wikitables_composition__dev::p18]

Cited: alce::67__wikitables_composition__dev::p18

### `367__wikidata_comp__dev`
_Refused._

### `771__wikidata_simple__dev`
> **free schools**
> The Russell Education Trust (RET) is a Multi-Academy free school Trust that provides educational support services in the creation and operation of free schools. [alce::771__wikidata_simple__dev::p0]
> The Russell Education Trust has worked in partnership with parents, communities, and diocesan authorities to establish free schools. [alce::771__wikidata_simple__dev::p2]

Cited: alce::771__wikidata_simple__dev::p0, alce::771__wikidata_simple__dev::p2

### `1007__wikidata_comp__dev`
> **United States, Sweden, France, and Finland**
> Joakim Noah was selected by the Chicago Bulls with the ninth overall pick in the 2007 NBA draft and holds American, Swedish and French citizenship. [alce::1007__wikidata_comp__dev::p11]
> Erik Murphy was drafted by the Chicago Bulls in 2013 and holds both American and Finnish passports. [alce::1007__wikidata_comp__dev::p14]

Cited: alce::1007__wikidata_comp__dev::p11, alce::1007__wikidata_comp__dev::p14

### `576__wikidata_simple__dev`
> **Bangor City F.C. entered the European Cup Winners' Cup, UEFA Europa League, Welsh Cup, Welsh Premier League, League of Wales, English football pyramid (Northern Premier League, Alliance Premier League), North Wales Coast League, Welsh National League, and North Wales Combination**
> City's first participation in European competition was during the 1962–63 season, when they competed in the European Cup Winners' Cup after winning the Welsh Cup. [alce::576__wikidata_simple__dev::p0]
> Bangor did not compete again in Europe for 23 years until the 1985–86 season when they once again played in the European Cup Winners' Cup. [alce::576__wikidata_simple__dev::p0]
> The club competed in the Welsh Premier League, being ever present since the league was founded in 1992. [alce::576__wikidata_simple__dev::p3]
> Bangor City have played in the inaugural season of the Welsh Cup and the UEFA Europa League, along with being founder members of the North Wales Coast League, the Welsh National League, the North Wales Combination. [alce::576__wikidata_simple__dev::p3]
> Before 1992 they were members of the English football pyramid, peaking with the Northern Premier League title in 1982. [alce::576__wikidata_simple__dev::p8]
> The club's home colours have traditionally been Royal blue shirts, Royal blue shorts and Royal blue socks, although over the years home colours have varied to include Royal blue and yellow and scarlet and Royal blue. Bangor City F.C. is one of Wales' older football clubs, and has played in European football, the English pyramid system and the Welsh Premier League. Bangor was a founding member of the North Wales Coast League in 1893, the Welsh National League in 1921, the North Wales Combination in [alce::576__wikidata_simple__dev::p12]

Cited: alce::576__wikidata_simple__dev::p0, alce::576__wikidata_simple__dev::p12, alce::576__wikidata_simple__dev::p3, alce::576__wikidata_simple__dev::p8

### `622__wikidata_simple__dev`
> **US Open (girls' singles event)**
> Cori Gauff is the youngest ever finalist in the girls' singles event at the US Open. [alce::622__wikidata_simple__dev::p1]

Cited: alce::622__wikidata_simple__dev::p1

### `407__wikidata_intersection__dev`
> **The Man Who Wasn't There**
> The Man Who Wasn't There is a 2001 British-American neo-noir crime film written, produced and directed by Joel and Ethan Coen. [alce::407__wikidata_intersection__dev::p35]
> The brothers write, direct and produce their films jointly. [alce::407__wikidata_intersection__dev::p2]

Cited: alce::407__wikidata_intersection__dev::p2, alce::407__wikidata_intersection__dev::p35

### `973__wikidata_comp__dev`
> **Suneel Darshan, Vipul Amrutlal Shah, and Chandraprakash Dwivedi**
> Suneel Darshan produced and directed Akshay Kumar films including 'Jaanwar', 'Andaaz', 'Ek Rishtaa' and 'Dosti: Friends Forever'. [alce::973__wikidata_comp__dev::p41]
> Vipul Amrutlal Shah is a film producer and director who has directed four Hindi films starring Akshay Kumar. [alce::973__wikidata_comp__dev::p3]
> Chandraprakash Dwivedi is directing a movie on Prithviraj Chauhan produced by Yash Raj Films, starring Akshay Kumar. [alce::973__wikidata_comp__dev::p73]

Cited: alce::973__wikidata_comp__dev::p3, alce::973__wikidata_comp__dev::p41, alce::973__wikidata_comp__dev::p73

### `813__wikidata_simple__dev`
> **Blue Mesa Reservoir**
> Gunnison is near Blue Mesa Reservoir. [alce::813__wikidata_simple__dev::p1]
> Currecanti Recreation Area and Blue Mesa Reservoir is located nine (9) miles West of Gunnison. [alce::813__wikidata_simple__dev::p3]
> Also nearby is the Black Canyon of the Gunnison National Park, Taylor Reservoir, and Roaring Judy fish hatchery. [alce::813__wikidata_simple__dev::p3]

Cited: alce::813__wikidata_simple__dev::p1, alce::813__wikidata_simple__dev::p3

### `867__wikidata_simple__dev`
> **1978 French Open and 1982 U.S. Clay Court Championships**
> Virginia Ruzicki won the 1978 French Open singles championship. [alce::867__wikidata_simple__dev::p0]
> She also won the 1982 U.S. Clay Court Championships, defeating Helena Suková 6–2, 6–0 in the singles final. [alce::867__wikidata_simple__dev::p20]

Cited: alce::867__wikidata_simple__dev::p0, alce::867__wikidata_simple__dev::p20

### `923__wikidata_simple__dev`
> **Multiple organizations including local education authorities, leisure centers, ferry services, and public services operations**
> Serco took control of local education authorities, managing and operating education support services for cities including Birmingham, Walsall, and Stoke-on-Trent. [alce::923__wikidata_simple__dev::p6]
> Serco Leisure Operating Ltd. operates leisure centres across the UK including Wet 'n' Wild in South Shields and the Manchester Aquatics Centre. [alce::923__wikidata_simple__dev::p6]
> Serco took over the operation of a ferry crossing service from the London Borough of Greenwich, with the contract beginning on 1 October 2008. [alce::923__wikidata_simple__dev::p43]
> Serco operates the Santander Cycles scheme for Transport for London and the NorthLink Ferries Northern Isles lifeline ferry service in Scotland. [alce::923__wikidata_simple__dev::p8]

Cited: alce::923__wikidata_simple__dev::p43, alce::923__wikidata_simple__dev::p6, alce::923__wikidata_simple__dev::p8

### `114__wikidata_comp__dev`
> **Golden State Warriors**
> The Golden State Warriors are the current NBA Finals champion. [alce::114__wikidata_comp__dev::p54]

Cited: alce::114__wikidata_comp__dev::p54

### `857__wikidata_simple__dev`
_Refused._

### `166__wikidata_intersection__dev`
> **Manchester United won multiple FA Cup Finals, including the 1908–09 FA Cup (their first), the 1995–96 FA Cup, and the 1998–99 FA Cup (their record 10th success)**
> Manchester United won the 1908–09 FA Cup competition for the first time, beating Bristol City 1–0 in the final at Crystal Palace, through a goal from Sandy Turnbull. [alce::166__wikidata_intersection__dev::p3]
> The 1995–96 FA Cup was won by Manchester United, who won the final through a goal from Eric Cantona five minutes from the end of the game. [alce::166__wikidata_intersection__dev::p10]
> Manchester United claimed a record 10th success in the 1998–99 FA Cup final with a 2–0 win, with goals from Teddy Sheringham and Paul Scholes. [alce::166__wikidata_intersection__dev::p26]

Cited: alce::166__wikidata_intersection__dev::p10, alce::166__wikidata_intersection__dev::p26, alce::166__wikidata_intersection__dev::p3

### `257__wikidata_intersection__dev`
> **Multiple Grand Slam doubles titles and WTA tournaments including the 2015 Australian Open, 2015 French Open, 2016 US Open, 2017 Australian Open, 2017 French Open, Wuhan, and Beijing**
> Lucie Šafářová and Bethanie Mattek-Sands won five Grand Slam doubles titles together: the 2015 Australian Open and French Open, the 2016 US Open, and the 2017 Australian Open and French Open. [alce::257__wikidata_intersection__dev::p16, alce::257__wikidata_intersection__dev::p9]
> In 2016, Šafářová and Mattek-Sands won two additional tournaments: Wuhan and Beijing. [alce::257__wikidata_intersection__dev::p26]

Cited: alce::257__wikidata_intersection__dev::p16, alce::257__wikidata_intersection__dev::p26, alce::257__wikidata_intersection__dev::p9

### `620__wikidata_simple__dev`
> **Anthropoid**
> LD Entertainment is an independent American film studio and sales company that finances, produces, acquires and distributes full-length theatrical motion pictures around the world. [alce::620__wikidata_simple__dev::p2]
> Among LD's films is 'Anthropoid', a World War II drama starring Jamie Dornan and Cilian Murphy. [alce::620__wikidata_simple__dev::p2]

Cited: alce::620__wikidata_simple__dev::p2

### `124__wikidata_comp__dev`
> **Garry Marshall and James L. Brooks**
> Mark Andrus wrote the original scripts 'Life as a House' and 'Georgia Rule', which won him and director Garry Marshall the Entertainment Industries Council PRISM Award for Best Feature Film. [alce::124__wikidata_comp__dev::p2]
> Brooks agreed to produce and direct 'Old Friends', a screenplay by Mark Andrus, which became 'As Good as It Gets'. [alce::124__wikidata_comp__dev::p6]

Cited: alce::124__wikidata_comp__dev::p2, alce::124__wikidata_comp__dev::p6

### `313__wikidata_comp__dev`
> **Egypt and France**
> Egypt is the first and so far only country in Africa or the Middle East to possess an aircraft carrier. [alce::313__wikidata_comp__dev::p15]
> A CATOBAR carrier is a 42,000 tonne nuclear-powered aircraft carrier, commissioned in 2001 and is the flagship of the French Navy (Marine Nationale). [alce::313__wikidata_comp__dev::p15]

Cited: alce::313__wikidata_comp__dev::p15

### `504__wikitables_simple__dev`
> **Password manager software includes programs like 1Password, Pass, and Password Safe**
> A password manager is a software application that helps a user store and organize passwords. [alce::504__wikitables_simple__dev::p0]
> Password manager programs include stand-alone applications, web browser extensions, or a manager built into the operating system. [alce::504__wikitables_simple__dev::p1]
> A popular password manager software is 1Password. [alce::504__wikitables_simple__dev::p6]
> Pass is a password manager inspired by the Unix philosophy that uses GnuPG for encryption and decryption of stored passwords. [alce::504__wikitables_simple__dev::p72]
> Password Safe is a free and open-source password manager program for use with Microsoft Windows. [alce::504__wikitables_simple__dev::p8]

Cited: alce::504__wikitables_simple__dev::p0, alce::504__wikitables_simple__dev::p1, alce::504__wikitables_simple__dev::p6, alce::504__wikitables_simple__dev::p72, alce::504__wikitables_simple__dev::p8

### `60__wikitables_composition__dev`
> **Hernández**
> After brief stints back in Mexico with Puebla and Chiapas F.C. in 2007 and 2008, Hernández signed with FC Dallas in September 2009. [alce::60__wikitables_composition__dev::p6]

Cited: alce::60__wikitables_composition__dev::p6

### `135__wikidata_comp__dev`
> **George Lucas, Steven Spielberg, Oliver Stone, and Alfonso Cuarón**
> Kenneth Wannberg's music editing credits include "Star Wars" (George Lucas, 1977), "Raiders of the Lost Ark" (Steven Spielberg, 1981), "JFK" (Oliver Stone, 1991), "Schindler's List" (Spielberg, 1993), and "Harry Potter and the Prisoner of Azkaban" (Alfonso Cuarón, 2004). [alce::135__wikidata_comp__dev::p0]
> Wannberg's film score compositions include "The Tender Warrior" (1971), "The Great American Beauty Contest" (1973), "Lepke" (1975), "The Four Deuces" (1975), "Bittersweet Love" (1976), "The Late Show" (1977), "Tribute" (1980), "The Amateur" (1981), "Mother Lode" (1982), "Losin' It" (1983), "Draw!" (1984), "Blame It on Rio" (1984) and "The Philadelphia Experiment" (1984). [alce::135__wikidata_comp__dev::p1]

Cited: alce::135__wikidata_comp__dev::p0, alce::135__wikidata_comp__dev::p1

### `323__wikidata_comp__dev`
> **Larry Charles**
> In 2006 Baynham co-wrote the film 'Borat' together with star Sacha Baron Cohen, Anthony Hines and Dan Mazer, for which they received a 2007 Oscar nomination for Best Adapted Screenplay. [alce::323__wikidata_comp__dev::p11]
> The film 'Borat' was directed by Larry Charles. [alce::323__wikidata_comp__dev::p11]

Cited: alce::323__wikidata_comp__dev::p11

### `402__wikidata_intersection__dev`
> **Maalayogam**
> Maalayogam is a Malayalam film released in 1990 directed by Sibi Malayil. [alce::402__wikidata_intersection__dev::p47]
> Sibi Malayil directed Maalayogam (1990), which is listed among his notable films from the late 1980s and early 1990s. [alce::402__wikidata_intersection__dev::p0, alce::402__wikidata_intersection__dev::p47]
> From 1996 to 2001 Vidyasagar mainly concentrated on Malayalam films, and during this period he composed for various Malayalam movies. [alce::402__wikidata_intersection__dev::p21]

Cited: alce::402__wikidata_intersection__dev::p0, alce::402__wikidata_intersection__dev::p21, alce::402__wikidata_intersection__dev::p47

### `971__wikidata_comp__dev`
_Refused._

### `292__wikidata_intersection__dev`
> **Youth Runs Wild**
> Youth Runs Wild is a 1944 B movie about unattentive parents and juvenile delinquency, produced by Val Lewton, directed by Mark Robson and starring Bonita Granville, Kent Smith, Jean Brooks, Glen Vernon and Vanessa Brown. [alce::292__wikidata_intersection__dev::p75]
> Additionally, Robson and Lewton reunited on Bedlam (1946), which was the last horror movie made by Lewton. [alce::292__wikidata_intersection__dev::p50]

Cited: alce::292__wikidata_intersection__dev::p50, alce::292__wikidata_intersection__dev::p75

### `829__wikidata_simple__dev`
> **Multiple players across different draft years**
> The Atlanta Falcons selected Fralic in the first round, who signed the most lucrative contract for any lineman in the draft. [alce::829__wikidata_simple__dev::p16]
> In another draft, the Falcons chose Christopher Owens of San Jose State in the third round, along with Lawrence Sidbury of Richmond in the fourth round, William Middleton from Furman in the fifth round, Garrett Reynolds of North Carolina in the fifth round, Spencer Adkins from Miami in the sixth round, and Vance Walker from Georgia Tech in the seventh round. [alce::829__wikidata_simple__dev::p22]
> The Atlanta Falcons drafted Zeke Motta in the seventh round (244th overall) of the 2013 NFL Draft. [alce::829__wikidata_simple__dev::p91]
> The Atlanta Falcons selected Deion Jones in the second round (52nd overall) of the 2016 NFL Draft, along with fourth round pick De'Vondre Campbell. [alce::829__wikidata_simple__dev::p61]

Cited: alce::829__wikidata_simple__dev::p16, alce::829__wikidata_simple__dev::p22, alce::829__wikidata_simple__dev::p61, alce::829__wikidata_simple__dev::p91

### `104__wikidata_comp__dev`
_Refused._

### `781__wikidata_simple__dev`
> **Multiple motion pictures - Lionheart, Double Impact, Only the Strong, The Last Patrol, Perfect Target, The Order, and The Hard Corps**
> Van Damme helped to launch Lettich's directing career with the film, 'Lionheart', which became Van Damme's first movie to be released theatrically by a major U.S. studio. [alce::781__wikidata_simple__dev::p37]
> This was followed by 'Double Impact', which was filmed in Hong Kong, with Lettich directing Van Damme in a challenging double role as twin brothers seeking revenge for their parents' murder. [alce::781__wikidata_simple__dev::p37]
> Lettich next discovered Mark Dacascos, who made his starring debut in 'Only the Strong', a film that introduced the Brazilian martial art of Capoeira to international audiences. [alce::781__wikidata_simple__dev::p37]
> He also directed Dolph Lundgren in The Last Patrol, and Daniel Bernhardt in 'Perfect Target'. [alce::781__wikidata_simple__dev::p3]
> He directed The Order, an action-thriller starring Van Damme and Charlton Heston, which was filmed on locations in Israel and Bulgaria. [alce::781__wikidata_simple__dev::p3]
> His most recent directorial effort, which he also co-wrote, is 'The Hard Corps', an urban action-romance. [alce::781__wikidata_simple__dev::p3]

Cited: alce::781__wikidata_simple__dev::p3, alce::781__wikidata_simple__dev::p37

### `20__wikitables_composition__dev`
> **Boston College, Clemson University, Duke University, Georgia Institute of Technology, Florida State University, North Carolina State University, Syracuse, and others listed in ACC membership**
> The Atlantic Coast Conference (ACC) is a collegiate athletic conference in the United States of America in which its fifteen member universities compete in the National Collegiate Athletic Association (NCAA)'s Division I. [alce::20__wikitables_composition__dev::p77]
> Current members of the conference are Boston College, Clemson University, Duke University, Georgia Institute of Technology, Florida State University, North Carolina State University, Syracuse. [alce::20__wikitables_composition__dev::p77]
> Virginia Tech joined in 2004 and Boston College joined in 2005, and a later realignment in 2013 saw Notre Dame and Pittsburgh join the ACC. [alce::20__wikitables_composition__dev::p88]

Cited: alce::20__wikitables_composition__dev::p77, alce::20__wikitables_composition__dev::p88

### `568__wikidata_simple__dev`
> **Multiple Bulgarian military officers and generals served in the Bulgarian military, including Dimitar Popgeorgiev, Kliment Boyadzhiev, Konstantin Zhostov, Aleksandar Protogerov, Boris Drangov, Petar Darvingov, Kiril Yanchulev, and Danail Nikolaev**
> Bulgarian generals and military officers Dimitar Popgeorgiev, Kliment Boyadzhiev, Konstantin Zhostov, Aleksandar Protogerov, Boris Drangov, Petar Darvingov and Kiril Yanchulev served in the Bulgarian Army in the Serbo-Bulgarian War, First Balkan War, Second Balkan War, World War I and World War II, respectively. [alce::568__wikidata_simple__dev::p22]
> Danail Nikolaev was a Bulgarian officer and Minister of War on the eve of the Balkan wars and was the first person to attain the highest rank in the Bulgarian military, General of the infantry. [alce::568__wikidata_simple__dev::p66]
> Petar Darvingov served in the Bulgarian Army and took part in the First Balkan war, having been promoted to the rank of major in 1911 and appointed assistant chief of the Intelligence Department in the headquarters of the Bulgarian Army. [alce::568__wikidata_simple__dev::p42]

Cited: alce::568__wikidata_simple__dev::p22, alce::568__wikidata_simple__dev::p42, alce::568__wikidata_simple__dev::p66

### `879__wikidata_simple__dev`
_Refused._

### `378__wikidata_intersection__dev`
> **Multiple FA Cup Finals featured Tottenham Hotspur: the 1961 FA Cup Final (vs Leicester City), the 1962 FA Cup Final (vs Burnley), and the 1982 FA Cup Final (vs Queens Park Rangers)**
> The 1961 FA Cup Final saw Tottenham Hotspur defeat Leicester City 2–0. [alce::378__wikidata_intersection__dev::p12]
> The 1962 FA Cup Final took place on 5 May 1962 at Wembley Stadium and was won by Tottenham Hotspur over Burnley, by a 3–1 scoreline. [alce::378__wikidata_intersection__dev::p8]
> The 1982 FA Cup Final took place on 22 May 1982 at Wembley Stadium and was contested between Tottenham Hotspur and Queens Park Rangers, with Spurs winning 1–0 in the replay. [alce::378__wikidata_intersection__dev::p0]

Cited: alce::378__wikidata_intersection__dev::p0, alce::378__wikidata_intersection__dev::p12, alce::378__wikidata_intersection__dev::p8

### `228__wikidata_comp__dev`
_Refused._

### `692__wikidata_simple__dev`
> **The Uyghur people in the Xinjiang Uyghur Autonomous Region of Western China**
> The Uyghur language is a Turkic language with 10 to 15 million speakers, spoken primarily by the Uyghur people in the Xinjiang Uyghur Autonomous Region of Western China. [alce::692__wikidata_simple__dev::p0]
> Significant communities of Uyghur-speakers are also located in Kazakhstan, Kyrgyzstan and Uzbekistan, and various other countries have Uyghur-speaking expatriate communities. [alce::692__wikidata_simple__dev::p0]
> Uyghur was spoken by some 300,000 people in Kazakhstan in 1993, some 90,000 in Kyrgyzstan and Uzbekistan in 1998, 3,000 in Afghanistan and 1,000 in Mongolia, with smaller communities in Albania, Australia, Belgium, Canada, Germany, Indonesia, Pakistan, Saudi Arabia, Sweden, Taiwan, Tajikistan, Turkey, United Kingdom and the United States. [alce::692__wikidata_simple__dev::p1]

Cited: alce::692__wikidata_simple__dev::p0, alce::692__wikidata_simple__dev::p1

### `493__wikitables_simple__dev`
> **Common allergens include wheat, rye, barley, oats, crustaceans, eggs, fish, peanuts, soybean, milk, tree nuts (almonds, hazelnuts, cashew nuts, Brazil nuts, macadamia nuts, walnuts, pecan nuts, pistaches, pine nuts, chestnuts), sesame seeds, sulfites, and various environmental allergens like dust mites, cat dander, and pollen**
> Common food allergens recognized by the FDA include peanuts, tree nuts, eggs, milk, shellfish, fish, wheat and their derivatives, and soy and their derivatives, as well as sulfites at 10ppm and over. [alce::493__wikitables_simple__dev::p5]
> Additional allergens include wheat, rye, barley, oats and their hybrids, crustaceans, eggs, fish, peanuts, soybean, milk of all species of mammalians, almonds, hazelnuts, cashew nuts, Brazil nuts, macadamia nuts, walnuts, pecan nuts, pistaches, pine nuts, and chestnuts. [alce::493__wikitables_simple__dev::p43]
> Canada recognizes all eight of the allergens recognized by the US, and also recognizes sesame seeds. [alce::493__wikitables_simple__dev::p5]
> Environmental allergens include proteins such as dust mite Der p 1, cat Fel d 1, grass or ragweed pollen. [alce::493__wikitables_simple__dev::p62]

Cited: alce::493__wikitables_simple__dev::p43, alce::493__wikitables_simple__dev::p5, alce::493__wikitables_simple__dev::p62

### `544__wikitables_simple__dev`
> **National quality awards include the Rajiv Gandhi National Quality Award (India), Malcolm Baldrige National Quality Award (USA), Canada Awards for Excellence (Canada), and Philippine Quality Award (Philippines)**
> The Rajiv Gandhi National Quality Award is the national quality award given by the Bureau of Indian Standards to Indian organisations that show excellence in their performance. [alce::544__wikitables_simple__dev::p1]
> The Malcolm Baldrige National Quality Award recognizes U.S. organizations in the business, health care, education, and nonprofit sectors for performance excellence. [alce::544__wikitables_simple__dev::p11]
> The Canada Awards for Excellence are the national quality awards of Canada. [alce::544__wikitables_simple__dev::p8]
> The Philippine Quality Award Program or PQA is the national quality award for Total Quality Management (TQM) in the Philippines. [alce::544__wikitables_simple__dev::p4]

Cited: alce::544__wikitables_simple__dev::p1, alce::544__wikitables_simple__dev::p11, alce::544__wikitables_simple__dev::p4, alce::544__wikitables_simple__dev::p8

### `1250__wikitables_composition__dev`
_Refused._

### `895__wikidata_simple__dev`
> **Yachts and vessels**
> Philip Leonard Rhodes (1895–1974) was a naval architect known for his diverse yacht designs. [alce::895__wikidata_simple__dev::p0]
> He designed a wide variety of vessels from 123' motor-sailors to 7' dinghies, from hydrofoil racers to giant motor yachts, and his work also included commercial and military vessels such as minesweepers and police boats. [alce::895__wikidata_simple__dev::p0]

Cited: alce::895__wikidata_simple__dev::p0

### `957__wikidata_comp__dev`
> **Balamand Orthodox Theological Seminary in Lebanon, schools in Syria, Kelham Theological College in England, and the University of London**
> Metropolitan Philip (born Abdullah Saliba; June 10, 1931 – March 19, 2014) was the Archbishop of New York and Metropolitan of All North America, which is the leadership position for the Antiochian Orthodox Christian Archdiocese of North America. [alce::957__wikidata_comp__dev::p62]
> Saliba was educated at Balamand Orthodox Theological Seminary in Lebanon and at schools in Syria. He later studied in England at the Anglican Kelham Theological College and the University of London. [alce::957__wikidata_comp__dev::p62]

Cited: alce::957__wikidata_comp__dev::p62

### `274__wikidata_comp__dev`
> **Carl Franklin**
> Carl Franklin directed the film 'One False Move', which was based on a screenplay by Howard Franklin. [alce::274__wikidata_comp__dev::p37]
> Franklin's approach to the screenplay produced a thriller of the Film Noir genre, dealing with themes of drugs, violence, and sexual relationships. [alce::274__wikidata_comp__dev::p37]

Cited: alce::274__wikidata_comp__dev::p37

### `1011__wikidata_comp__dev`
> **Multiple drivers won Japanese Grand Prix races from first position**
> Sebastian Vettel won the 2010 Japanese Grand Prix after starting from pole position. [alce::1011__wikidata_comp__dev::p7]
> Fernando Alonso won the 2008 Japanese Grand Prix from fourth position on the starting grid. [alce::1011__wikidata_comp__dev::p21]
> Lewis Hamilton won the 2014 Japanese Grand Prix after starting from second position. [alce::1011__wikidata_comp__dev::p62]
> Kimi Räikkönen won the 2005 Japanese Grand Prix after starting from 17th place. [alce::1011__wikidata_comp__dev::p48]

Cited: alce::1011__wikidata_comp__dev::p21, alce::1011__wikidata_comp__dev::p48, alce::1011__wikidata_comp__dev::p62, alce::1011__wikidata_comp__dev::p7

### `881__wikidata_simple__dev`
> **46 airports in Norway, air traffic control services, and three Area Control Centers**
> Avinor owns and operates 46 airports in Norway, fourteen in association with the Royal Norwegian Air Force, and is responsible for air traffic control services in Norway. [alce::881__wikidata_simple__dev::p0]
> In addition to 46 airports, it operates three Area Control Centers: Bodø Air Traffic Control Center, Stavanger Air Traffic Control Center and Oslo ATCC. [alce::881__wikidata_simple__dev::p2]
> This company still operates Oslo Airport, Gardermoen. [alce::881__wikidata_simple__dev::p1]

Cited: alce::881__wikidata_simple__dev::p0, alce::881__wikidata_simple__dev::p1, alce::881__wikidata_simple__dev::p2

### `548__wikitables_simple__dev`
> **Various forms of football including association football, gridiron football, Australian rules football, rugby football, and Gaelic football**
> Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. [alce::548__wikitables_simple__dev::p37]
> Sports commonly called 'football' in certain places include association football (known as soccer in some countries); gridiron football (specifically American football or Canadian football); Australian rules football; rugby football (either rugby league or rugby union); and Gaelic football. [alce::548__wikitables_simple__dev::p37]
> High school football games and informal 'Turkey Bowl' contests are frequently held on Thanksgiving weekend. [alce::548__wikitables_simple__dev::p12]
> NFL is a series of American football games developed by Gameloft that simulates the National Football League. [alce::548__wikitables_simple__dev::p10]
> Traditional football games were played in the cities, villages and schools of Europe for many centuries, and early intramural games of football began to be played on college campuses in the 19th century. [alce::548__wikitables_simple__dev::p80]

Cited: alce::548__wikitables_simple__dev::p10, alce::548__wikitables_simple__dev::p12, alce::548__wikitables_simple__dev::p37, alce::548__wikitables_simple__dev::p80

### `1359__wikidata_simple__dev`
> **Private residences, school buildings, and commercial buildings including the Thompson Block**
> George Milford Harding (1827–1910) was an American architect who practiced in nineteenth-century Massachusetts, New Hampshire, and Maine. [alce::1359__wikidata_simple__dev::p1]
> His works were made up of private residences and a large number of school buildings. [alce::1359__wikidata_simple__dev::p0]
> The Thompson Block, a historic commercial building located at 117, 119, 121, 123 and 125 Middle Street in downtown Portland, Maine, was designed by architect George M. Harding and constructed in 1867. [alce::1359__wikidata_simple__dev::p64]

Cited: alce::1359__wikidata_simple__dev::p0, alce::1359__wikidata_simple__dev::p1, alce::1359__wikidata_simple__dev::p64

### `928__wikidata_simple__dev`
> **Multiple competitions including Campeonato Brasileiro Série A, Campeonato Brasileiro Série C, Campeonato Baiano, São Tomé and Príncipe Championship, and Primeira Liga**
> Esporte Clube Vitória is a Brazilian football team from Salvador in Bahia that plays in the Campeonato Brasileiro Série A and the Campeonato Baiano. [alce::928__wikidata_simple__dev::p10]
> In 1977, the club competed in the Campeonato Brasileiro Série A for the first time, and in 2006, Vitória competed in the Campeonato Brasileiro Série C. [alce::928__wikidata_simple__dev::p93]
> Vitória FC (Riboque) plays in the São Tomé and Príncipe Championship. [alce::928__wikidata_simple__dev::p74]
> Associação Desportiva Vitória competed in the Série C five times between 1992 and 1995. [alce::928__wikidata_simple__dev::p11]
> Vitória de Guimarães competes in the Primeira Liga, the top-flight of football in Portugal. [alce::928__wikidata_simple__dev::p3]

Cited: alce::928__wikidata_simple__dev::p10, alce::928__wikidata_simple__dev::p11, alce::928__wikidata_simple__dev::p3, alce::928__wikidata_simple__dev::p74, alce::928__wikidata_simple__dev::p93

### `660__wikidata_simple__dev`
> **Grey's Anatomy, Private Practice, Scandal, Off the Map, How to Get Away with Murder, and The Catch**
> Shonda Rhimes is best known as the showrunner—creator, head writer, and executive producer—of the television medical drama 'Grey's Anatomy', its spin-off 'Private Practice', and the political thriller series 'Scandal'. [alce::660__wikidata_simple__dev::p1]
> Rhimes has also served as the executive producer of the ABC television series 'Off the Map', 'How to Get Away with Murder', and 'The Catch'. [alce::660__wikidata_simple__dev::p1]
> In 2011, Rhimes served as executive producer for the medical drama, 'Off the Map', which was created by 'Grey's Anatomy' writer, Jenna Bans. [alce::660__wikidata_simple__dev::p11]

Cited: alce::660__wikidata_simple__dev::p1, alce::660__wikidata_simple__dev::p11

### `759__wikidata_simple__dev`
> **Leitrim GAA**
> Leitrim GAA is one of the 32 county boards of the GAA in Ireland, and is responsible for Gaelic games in County Leitrim. [alce::759__wikidata_simple__dev::p22]

Cited: alce::759__wikidata_simple__dev::p22

### `125__wikidata_comp__dev`
> **Multiple KC Royals draftees attended different schools including Charles W. Baker High School, Northwest Christian High School, Sarasota High School, and Kellenberg Memorial High School**
> Scott Thomas Blewett was drafted by the Kansas City Royals in the second round of the 2014 MLB Draft and attended Charles W. Baker High School in Baldwinsville, New York. [alce::125__wikidata_comp__dev::p26]
> Affeldt was drafted by the Kansas City Royals in the third round of the 1997 MLB draft and attended Northwest Christian High School in Colbert, Washington. [alce::125__wikidata_comp__dev::p2]
> Eric Skoglund was drafted by the Kansas City Royals in the third round of the 2014 MLB Draft and attended Sarasota High School in Sarasota, Florida. [alce::125__wikidata_comp__dev::p13]
> Kevin McCarthy was drafted by the Kansas City Royals in the 16th round of the 2013 Major League Baseball draft and attended Kellenberg Memorial High School in Uniondale, New York. [alce::125__wikidata_comp__dev::p11]

Cited: alce::125__wikidata_comp__dev::p11, alce::125__wikidata_comp__dev::p13, alce::125__wikidata_comp__dev::p2, alce::125__wikidata_comp__dev::p26

### `134__wikidata_intersection__dev`
_Refused._

### `434__wikidata_intersection__dev`
> **Final Fantasy**
> In 1987, Square designer Hironobu Sakaguchi chose to create a new fantasy role-playing game for the cartridge-based NES, and drew inspiration from popular fantasy games: Enix's 'Dragon Quest', Nintendo's 'The Legend of Zelda', and Origin Systems's 'Ultima' series. [alce::434__wikidata_intersection__dev::p25]
> The game's title, 'Final Fantasy', stemmed from his feelings at the time; had the game not sold well, he would have quit the business. [alce::434__wikidata_intersection__dev::p25]

Cited: alce::434__wikidata_intersection__dev::p25

### `788__wikidata_simple__dev`
_Refused._

### `564__wikidata_simple__dev`
> **Chicago Defender and other newspapers**
> Real Times Media LLC is the owner and publisher of the 'Chicago Defender', the largest and most influential African-American weekly newspaper, as well as five other regional weeklies in the eastern and Midwestern United States. [alce::564__wikidata_simple__dev::p4]
> The company also owns RTM Digital Studios, a videography company, and a large archive of newspaper clippings, artifacts and photographs connected with African-American history. [alce::564__wikidata_simple__dev::p0]
> In 2009, Real Times purchased Who's Who Publishing Company of Columbus, Ohio, which publishes biographical and networking guides for and about African American businesspeople in 25 cities across the country. [alce::564__wikidata_simple__dev::p0]

Cited: alce::564__wikidata_simple__dev::p0, alce::564__wikidata_simple__dev::p4

### `924__wikidata_simple__dev`
> **Yuwanjana Wijayatilake, Elanga Wikramanayake, Upawansa Yapa, and K. C. Kamalasabayson**
> Yuwanjana Jawaharlal Wanasundera Wijayatilake PC was the 43rd Solicitor General of Sri Lanka, appointed in 2012. [alce::924__wikidata_simple__dev::p2]
> Elanga Devapriya Wikramanayake was a Sri Lankan lawyer who served as the Solicitor General of Sri Lanka. [alce::924__wikidata_simple__dev::p17]
> Upawansa Yapa PC was the 37th Solicitor General of Sri Lanka. [alce::924__wikidata_simple__dev::p53]
> K. C. Kamalasabayson was a Sri Lankan Tamil lawyer and Solicitor General of Sri Lanka. [alce::924__wikidata_simple__dev::p76]

Cited: alce::924__wikidata_simple__dev::p17, alce::924__wikidata_simple__dev::p2, alce::924__wikidata_simple__dev::p53, alce::924__wikidata_simple__dev::p76

### `217__wikidata_intersection__dev`
> **2018 FA Community Shield**
> The 2018 FA Community Shield was contested by Manchester City, champions of the 2017–18 Premier League, and Chelsea, the winners of the 2017–18 FA Cup, at Wembley Stadium in London on 5 August 2018. [alce::217__wikidata_intersection__dev::p0]
> Manchester City won 2–0, with both goals scored by Sergio Agüero. [alce::217__wikidata_intersection__dev::p0]

Cited: alce::217__wikidata_intersection__dev::p0

### `506__wikitables_simple__dev`
> **Existing game controllers include keyboards, mice, gamepads, joysticks, steering wheels, light guns, and dance pads**
> Input devices that have been classified as game controllers include keyboards, mouses, gamepads, joysticks, etc. [alce::506__wikitables_simple__dev::p1]
> Special purpose devices, such as steering wheels for driving games and light guns for shooting games, are also game controllers. [alce::506__wikitables_simple__dev::p1]
> Some controllers are designed to be best for one type of game, such as steering wheels for driving games, or dance pads for dancing games. [alce::506__wikitables_simple__dev::p1]
> A gamepad, joypad, or simply controller is a type of game controller held in two hands, where the fingers (especially thumbs) are used to provide input. [alce::506__wikitables_simple__dev::p8]
> Controllers have evolved to include directional pads, multiple buttons, analog sticks, joysticks, motion detection, touch screens and a plethora of other features. [alce::506__wikitables_simple__dev::p3]

Cited: alce::506__wikitables_simple__dev::p1, alce::506__wikitables_simple__dev::p3, alce::506__wikitables_simple__dev::p8

### `359__wikidata_comp__dev`
> **A. R. Rahman and G. V. Prakash Kumar**
> Oscar Award-winner AR Rahman is composing the music for 'Kaaviya Thalaivan', a fictional Tamil historic movie directed by Vasanthabalan. [alce::359__wikidata_comp__dev::p97]
> The team signed A. R. Rahman to compose the music for the film 'Kaaviya Thalaivan' in December 2012. [alce::359__wikidata_comp__dev::p24]
> Soundtrack for 'Veyil', directed by Vasanthabalan, was composed by debutant G. V. Prakash Kumar, nephew of A. R. Rahman. [alce::359__wikidata_comp__dev::p94]

Cited: alce::359__wikidata_comp__dev::p24, alce::359__wikidata_comp__dev::p94, alce::359__wikidata_comp__dev::p97

### `720__wikidata_simple__dev`
> **Ernest Rutherford**
> Hans Geiger was a German physicist born in 1882 who started studying physics and mathematics at the University of Erlangen in 1902. [alce::720__wikidata_simple__dev::p3]
> While the sources do not explicitly name Geiger's doctoral advisor, they indicate he attended Husserl's lectures in Göttingen in 1906 and passed his thesis in 1907, suggesting his doctoral work was conducted in Göttingen. [alce::720__wikidata_simple__dev::p14]

Cited: alce::720__wikidata_simple__dev::p14, alce::720__wikidata_simple__dev::p3

### `589__wikidata_simple__dev`
> **SaGa (the first installment of the SaGa series)**
> Akitoshi Kawazu was the director of the first installment of the SaGa series in Japan, which was the first Game Boy game produced by Square. [alce::589__wikidata_simple__dev::p83]
> Kawazu and partner Koichi Ishii decided to produce a role-playing game for the Game Boy handheld system after Square president Masafumi Miyamoto requested developers create a Game Boy game. [alce::589__wikidata_simple__dev::p83]

Cited: alce::589__wikidata_simple__dev::p83

### `21__wikitables_composition__dev`
> **Benjamin Britten, Michael Tippett, and Ralph Vaughan Williams**
> In the 20th century, Benjamin Britten and Michael Tippett emerged as internationally recognised opera composers, and Ralph Vaughan Williams and others collected English folk tunes and adapted them to the concert hall. [alce::21__wikitables_composition__dev::p0]
> There was a revival in the profile of composers from England in the 20th century led by Edward Elgar, Benjamin Britten. [alce::21__wikitables_composition__dev::p54]

Cited: alce::21__wikitables_composition__dev::p0, alce::21__wikitables_composition__dev::p54

### `894__wikidata_simple__dev`
> **K'**
> K' is a video game character from "The King of Fighters" fighting game series developed by SNK who debuted as the leader of the Hero Team in "The King of Fighters '99", released in 1999. [alce::894__wikidata_simple__dev::p71]

Cited: alce::894__wikidata_simple__dev::p71

### `244__wikidata_comp__dev`
> **John Farrow**
> John Farrow was an Australian film director, producer and screenwriter who won the Academy Award for Best Writing/Best Screenplay for 'Around the World in Eighty Days' in 1957. [alce::244__wikidata_comp__dev::p19]
> John Farrow directed the film 'Men in Exile' in 1937, which was a Warner Bros 'B' movie and his first feature film as director. [alce::244__wikidata_comp__dev::p21]

Cited: alce::244__wikidata_comp__dev::p19, alce::244__wikidata_comp__dev::p21

### `864__wikidata_simple__dev`
> **Gasoline**
> "Gasoline" is a song by American singer and songwriter Halsey. [alce::864__wikidata_simple__dev::p21]
> It was written by Halsey and Lido, the latter also producing the song. [alce::864__wikidata_simple__dev::p21]

Cited: alce::864__wikidata_simple__dev::p21

### `947__wikidata_simple__dev`
> **The Neon Demon**
> Neon is a film distribution company co-founded by Tim League and Tom Quinn in 2017. [alce::947__wikidata_simple__dev::p82]
> The Neon Demon is a film for which Neon was involved in distribution, with Amazon Studios acquiring distribution rights in the United States in partnership with Broad Green Pictures. [alce::947__wikidata_simple__dev::p9]

Cited: alce::947__wikidata_simple__dev::p82, alce::947__wikidata_simple__dev::p9

### `939__wikidata_simple__dev`
> **Acari National Park and Aripuanã National Forest**
> Novo Aripuanã contains 29% of the Acari National Park, which was created at the same time. [alce::939__wikidata_simple__dev::p0]
> The municipality contains about 74% of the Aripuanã National Forest, a sustainable development unit. [alce::939__wikidata_simple__dev::p0]
> The Acari National Park covers parts of the municipalities of Apuí (11.77%), Borba (59.55%) and Novo Aripuanã (28.68%) in Amazonas. [alce::939__wikidata_simple__dev::p9]

Cited: alce::939__wikidata_simple__dev::p0, alce::939__wikidata_simple__dev::p9

### `679__wikidata_simple__dev`
> **Multiple films including "Verna", "Na Maloom Afraad", "Bin Roye", and "Chupan Chupai"**
> Hum Films came on board as a distributor for Shoaib Mansoor's film 'Verna'. [alce::679__wikidata_simple__dev::p40]
> In September 2014, the Network launched Hum Films, a film production and distributor banner, with the first film released under the banner being 'Na Maloom Afraad' which released domestically on October 5. [alce::679__wikidata_simple__dev::p4]
> In 2015, Hum Films produced 'Bin Roye', and after its release, Hum Films has distributed and produced over fifteen films both domestically and internationally. [alce::679__wikidata_simple__dev::p85]
> The film soundtrack album for 'Chupan Chupai' was released by Hum Films on 8 December 2017. [alce::679__wikidata_simple__dev::p84]

Cited: alce::679__wikidata_simple__dev::p4, alce::679__wikidata_simple__dev::p40, alce::679__wikidata_simple__dev::p84, alce::679__wikidata_simple__dev::p85

### `130__wikidata_comp__dev`
> **Andrew Stanton (for WALL-E)**
> Reardon supervised the storyboard department and co-wrote the Pixar film "WALL-E" with Andrew Stanton, which was released on June 27, 2008. [alce::130__wikidata_comp__dev::p0]

Cited: alce::130__wikidata_comp__dev::p0

### `269__wikidata_comp__dev`
> **Multiple countries (Philippines, South Korea, and the United States)**
> Stella Abrera is a Filipina-American principal ballerina with American Ballet Theatre, one of the three leading classical ballet companies in the United States. [alce::269__wikidata_comp__dev::p9]
> Hee Seo is a South Korean principal dancer for American Ballet Theatre (ABT), one of the three leading classical ballet companies in the United States. [alce::269__wikidata_comp__dev::p45]
> Cynthia Harvey is an American dance teacher and former ballet dancer who was a principal dancer for the American Ballet Theatre. [alce::269__wikidata_comp__dev::p64]
> Mikhail Baryshnikov returned to ABT in September 1980 as an artistic director and became a naturalized citizen of the United States on July 3, 1986. [alce::269__wikidata_comp__dev::p38]

Cited: alce::269__wikidata_comp__dev::p38, alce::269__wikidata_comp__dev::p45, alce::269__wikidata_comp__dev::p64, alce::269__wikidata_comp__dev::p9

### `462__wikidata_intersection__dev`
> **Laurentine Hamilton**
> Laurentine Hamilton was a Presbyterian minister who graduated from Hamilton College in Clinton, New York in 1850 and attended Auburn Theological Seminary, from which he graduated in 1853. [alce::462__wikidata_intersection__dev::p4]

Cited: alce::462__wikidata_intersection__dev::p4

### `505__wikitables_simple__dev`
> **Notable wildfires in Canada and the US include the 2015 Canadian wildfires, the 2017 Lodgepole Complex Fire, the 2017 La Tuna Fire, and the 2017 British Columbia wildfires**
> The 2015 Canadian wildfires were a series of wildfires across Canada and Alaska in July 2015 which spread smoke across most of North America, with over two hundred fires ablaze across British Columbia, Saskatchewan, and Alberta. [alce::505__wikitables_simple__dev::p0]
> In 2017, record setting fires included the Lodgepole Complex Fire, the nation's largest that year; the La Tuna Fire, which was the largest in Los Angeles history; and the 2017 British Columbia wildfires, worst in the history of the province. [alce::505__wikitables_simple__dev::p4]
> 2017 was the most expensive firefighting year on record for the US Forest Service with over $2 billion spent. [alce::505__wikitables_simple__dev::p4]

Cited: alce::505__wikitables_simple__dev::p0, alce::505__wikitables_simple__dev::p4

### `123__wikidata_intersection__dev`
> **Mahakavi Kalidasu**
> Mahakavi Kalidasu is a 1960 Telugu movie directed by Kamalakara Kameswara Rao with music composed by Pendyala Nageswara Rao. [alce::123__wikidata_intersection__dev::p51]

Cited: alce::123__wikidata_intersection__dev::p51

### `470__wikitables_simple__dev`
> **General Sherman, General Grant, and President**
> The largest trees in the world by volume are all Giant Sequoias in King's Canyon National Park. They have been previously reported by trunk volume as: General Sherman at 52,508 cubic feet (1,486.9 m); General Grant at 46,608 cubic feet (1,319.8 m); and President at 45,148 cubic feet (1,278.4 m). [alce::470__wikitables_simple__dev::p0]
> All three of these giant sequoias have trunk volumes larger than 912.5 cubic meters: General Sherman (1,486.9 m³), General Grant (1,319.8 m³), and President (1,278.4 m³). [alce::470__wikitables_simple__dev::p0]

Cited: alce::470__wikitables_simple__dev::p0

### `11__wikitables_composition__dev`
> **Major onshore wind farms in Scotland include Whitelee Wind Farm, Clyde Wind Farm, and Crystal Rig Wind Farm**
> Whitelee Wind Farm, near Eaglesham, East Renfrewshire is the largest on-shore wind farm in the United Kingdom with 215 Siemens and Alstom wind turbines and a total capacity of 539 MW. [alce::11__wikitables_composition__dev::p1]
> The Clyde Wind Farm is a 548 MW wind farm under construction near Abington, South Lanarkshire, Scotland, which will be Europe's largest onshore wind farm when completed. [alce::11__wikitables_composition__dev::p2]
> Crystal Rig Wind Farm is an operational onshore wind farm located on the Lammermuir Hills in the Scottish Borders region of Scotland. [alce::11__wikitables_composition__dev::p26]
> There are many other large onshore wind farms in Scotland, at various stages of development, including some that are in community ownership. [alce::11__wikitables_composition__dev::p1]

Cited: alce::11__wikitables_composition__dev::p1, alce::11__wikitables_composition__dev::p2, alce::11__wikitables_composition__dev::p26

### `398__wikidata_comp__dev`
> **King's College, Cambridge**
> David Walker, the current Bishop of Manchester since 2013, studied at King's College, Cambridge. [alce::398__wikidata_comp__dev::p25]

Cited: alce::398__wikidata_comp__dev::p25

### `113__wikidata_intersection__dev`
> **No Country for Old Men**
> No Country for Old Men is a 2007 American crime thriller film written and directed by Joel and Ethan Coen. [alce::113__wikidata_intersection__dev::p35]

Cited: alce::113__wikidata_intersection__dev::p35

### `866__wikidata_simple__dev`
> **René Clair directed multiple films including "The Italian Straw Hat" (1928), "Under the Roofs of Paris" (1930), "Le Million" (1931), "À nous la liberté" (1931), "I Married a Witch" (1942), "And Then There Were None" (1945), and "The Flame of New Orleans" (1941)**
> Clair's best known films include "The Italian Straw Hat" (1928), "Under the Roofs of Paris" (1930), "Le Million" (1931), "À nous la liberté" (1931), "I Married a Witch" (1942), and "And Then There Were None" (1945). [alce::866__wikidata_simple__dev::p3]
> "À nous la liberté" (English: Freedom for Us) is a 1931 French film directed by René Clair. [alce::866__wikidata_simple__dev::p51]
> "The Flame of New Orleans" is a 1941 comedy film directed by René Clair and starring Marlene Dietrich and Bruce Cabot. [alce::866__wikidata_simple__dev::p63]

Cited: alce::866__wikidata_simple__dev::p3, alce::866__wikidata_simple__dev::p51, alce::866__wikidata_simple__dev::p63

### `147__wikidata_intersection__dev`
> **Cudi Montage**
> "Cudi Montage" is a song by American hip hop duo Kids See Ghosts, composed of Kanye West and Kid Cudi, released as the seventh track off their eponymous debut album "Kids See Ghosts" (2018). [alce::147__wikidata_intersection__dev::p19]

Cited: alce::147__wikidata_intersection__dev::p19

### `941__wikidata_simple__dev`
> **Hokkien (Southern Min)**
> Hokkien originated in the southern area of Fujian province, an important center for trade and migration. [alce::941__wikidata_simple__dev::p18]
> Southern Min, also called the Hokkien language, Hoklo language, Hokkien-Taiwanese or Min-Nan, belongs to the Min Chinese subgroup of Chinese language family. [alce::941__wikidata_simple__dev::p95]

Cited: alce::941__wikidata_simple__dev::p18, alce::941__wikidata_simple__dev::p95

### `254__wikidata_comp__dev`
> **North Dakota State University and Metropolitan State University of Denver**
> He played college football at North Dakota State University where he earned all-conference honors as a senior and was drafted by the Broncos in the 12th round of the 1987 NFL Draft. [alce::254__wikidata_comp__dev::p34]
> He has a Master of Social Work from Metropolitan State University of Denver. [alce::254__wikidata_comp__dev::p34]

Cited: alce::254__wikidata_comp__dev::p34

### `495__wikitables_simple__dev`
> **Gacha games released in English include Fire Emblem Heroes, Puzzle & Dragons, Dragon Collection, Granblue Fantasy, Girls' Frontline, Monster Strike, Fate/Grand Order, and Kingdom Hearts Union X**
> Examples of Gacha games are "Fire Emblem Heroes", "Puzzle & Dragons", and "Dragon Collection". [alce::495__wikitables_simple__dev::p1]
> Additional examples of Gacha games include "Granblue Fantasy", "Girls' Frontline", "Monster Strike", "Fate/Grand Order", and "Kingdom Hearts Union X." [alce::495__wikitables_simple__dev::p0]
> Most of these games are free-to-play mobile games that are available outside Japan, where the game type is gaining popularity. [alce::495__wikitables_simple__dev::p3]

Cited: alce::495__wikitables_simple__dev::p0, alce::495__wikitables_simple__dev::p1, alce::495__wikitables_simple__dev::p3

### `811__wikidata_simple__dev`
> **Interactive fiction games including Zork I, II, and III, Starcross, Suspect, Spellbreaker, The Lurking Horror, and James Clavell's Shogun**
> Dave Lebling is an interactive fiction game designer (implementor) and programmer who has worked at various companies, including Infocom and Avid. [alce::811__wikidata_simple__dev::p1]
> His games include "Zork I," "II" and "III", "Starcross", "Suspect", "Spellbreaker", "The Lurking Horror" and "James Clavell's Shogun". [alce::811__wikidata_simple__dev::p0]

Cited: alce::811__wikidata_simple__dev::p0, alce::811__wikidata_simple__dev::p1

### `862__wikidata_simple__dev`
> **Music producers, television and film producers, industrial rock musicians, and Nazi armaments industry personnel**
> Jeff Panzer is a music producer, music video producer and record label executive who has produced over 2,000 music videos in his career. [alce::862__wikidata_simple__dev::p7]
> William Norton Panzer was an American television and film producer best known as one half of Davis-Panzer Inc, the production company behind the 'Highlander' franchise. [alce::862__wikidata_simple__dev::p36]
> Panzer AG is an aggrotech/industrial rock side-project that combines elements of industrial music, Trance Music and Hard rock. [alce::862__wikidata_simple__dev::p49]
> In the Nazi armaments industry, nearly all of the deputies and directors were in the SS, the Gestapo or the SA, with Wilhelm Renner notably becoming the head of the military business and helping develop the Panzerfaust. [alce::862__wikidata_simple__dev::p11]

Cited: alce::862__wikidata_simple__dev::p11, alce::862__wikidata_simple__dev::p36, alce::862__wikidata_simple__dev::p49, alce::862__wikidata_simple__dev::p7

### `904__wikidata_simple__dev`
> **Multiple professionals work in the country music industry, including record producers, session musicians, studio musicians, and music journalists**
> Paul Worley is an American record producer and session guitarist, known primarily for his work in country music. [alce::904__wikidata_simple__dev::p44]
> Cohen has worked in the studio with a wide range of artists from country music, including Florida Georgia Line, Carrie Underwood, Old Dominion, Brett Eldredge, Chris Young, Walker Hayes, Jon Pardi, Cole Swindell, Josh Turner, Reba McEntire, Brooks and Dunn, and Kip Moore. [alce::904__wikidata_simple__dev::p79]
> Byworth edited the monthly magazine Country Music People for six years (1977–83) and co-founded Byworth-Wootton International, the UK's first country-music services company. [alce::904__wikidata_simple__dev::p94]
> Dave Cobb is a music producer who founded and runs Low Country Sound, a record label imprint based in Nashville, Tennessee. [alce::904__wikidata_simple__dev::p78]

Cited: alce::904__wikidata_simple__dev::p44, alce::904__wikidata_simple__dev::p78, alce::904__wikidata_simple__dev::p79, alce::904__wikidata_simple__dev::p94

### `627__wikidata_simple__dev`
> **Kristína Gavnholt and Olga Konon**
> Kristína Gavnholt was the girls' doubles champion of the 2007 European Junior Championships partnering with Belarusian player, Olga Konon. [alce::627__wikidata_simple__dev::p54]

Cited: alce::627__wikidata_simple__dev::p54

### `421__wikidata_intersection__dev`
_Refused._

### `880__wikidata_simple__dev`
> **Cyrus Edwin Dallin created multiple works of art, including the equestrian statue of Paul Revere in Boston, the Angel Moroni atop Salt Lake Temple in Salt Lake City, and his most famous work "Appeal to the Great Spirit" at the Museum of Fine Arts, Boston.**
> He created more than 260 works, including the equestrian statue of Paul Revere in Boston, Massachusetts; the Angel Moroni atop Salt Lake Temple in Salt Lake City, Utah; and his most famous work, "Appeal to the Great Spirit", at the Museum of Fine Arts, Boston. [alce::880__wikidata_simple__dev::p1]
> Appeal to the Great Spirit is a 1909 equestrian statue by Cyrus Dallin, at the Museum of Fine Arts, Boston, and was the last in his four-piece series, "The Epic of the Indian". [alce::880__wikidata_simple__dev::p8]

Cited: alce::880__wikidata_simple__dev::p1, alce::880__wikidata_simple__dev::p8

### `183__wikidata_comp__dev`
> **B. Unnikrishnan**
> Vishal served as producer on the Mohanlal-starrer 'Villain', which was directed by B. Unnikrishnan. [alce::183__wikidata_comp__dev::p26]

Cited: alce::183__wikidata_comp__dev::p26

### `712__wikidata_simple__dev`
> **Caitlin "Kate" Todd**
> The episode introduces Caitlin "Kate" Todd (as a replacement for NCIS agent Vivian "Viv" Blackadder), and FBI Agent Tobias Fornell, who would later become a major recurring character of the show. [alce::712__wikidata_simple__dev::p5]

Cited: alce::712__wikidata_simple__dev::p5

### `550__wikitables_simple__dev`
> **Kermadec Sanctuary (620,000 km²)**
> The Kermadec Sanctuary would be 620,000 square kilometers, making it the world's largest and most significant fully protected areas. [alce::550__wikitables_simple__dev::p5]
> Another protected area with 620,000 square kilometres would be one of the world's largest fully protected areas. [alce::550__wikitables_simple__dev::p53]

Cited: alce::550__wikitables_simple__dev::p5, alce::550__wikitables_simple__dev::p53

### `656__wikidata_simple__dev`
> **Nebula Awards 32**
> Nebula Awards 32 is an anthology of science fiction short works edited by Jack Dann. [alce::656__wikidata_simple__dev::p79]
> Jack Dann and Gardner Dozois have jointly edited a series of themed science fiction and fantasy anthologies, mostly published by Ace Books, known as 'The Exclamatory series,' which began in 1980 with 'Aliens!' [alce::656__wikidata_simple__dev::p14]
> Jack Dann and Gardner Dozois have also co-edited anthologies that are not part of this series, such as 'Future Power' (1976). [alce::656__wikidata_simple__dev::p2]

Cited: alce::656__wikidata_simple__dev::p14, alce::656__wikidata_simple__dev::p2, alce::656__wikidata_simple__dev::p79

### `480__wikitables_simple__dev`
> **Rocky Mountain Women's Film Festival, Cairo International Women's Film Festival, China Women's Film Festival, and In Other Words**
> The Rocky Mountain Women's Film Festival (RMWFF) in Colorado Springs, Colorado in the United States, is the longest-running women's film festival in North America. [alce::480__wikitables_simple__dev::p21]
> The Cairo International Women's Film Festival (CIWFF) is an independent initiative dedicated to introducing films directed by women from around the world. [alce::480__wikitables_simple__dev::p6]
> The China Women's Film Festival (CWFF) was established in 2013 as an annual event dedicated to promoting women's rights and raising awareness of gender inequality through film and art. [alce::480__wikitables_simple__dev::p0]
> In Other Words (Portland, 2013) is listed among women's film festivals. [alce::480__wikitables_simple__dev::p87]

Cited: alce::480__wikitables_simple__dev::p0, alce::480__wikitables_simple__dev::p21, alce::480__wikitables_simple__dev::p6, alce::480__wikitables_simple__dev::p87

### `662__wikidata_simple__dev`
> **USTS "Bay State" and the British steamer "Bay State"**
> A training vessel named USTS "Bay State" served the Massachusetts Maritime Academy in Buzzards Bay from 1957 to 1972, and was later transferred to the Massachusetts Maritime Academy in 1973 where she continued service as a training vessel. [alce::662__wikidata_simple__dev::p0, alce::662__wikidata_simple__dev::p17]
> The British steamer "Bay State", a 6,583-ton Warren Line cargo steamer, was sank by U-66 on 10 June after departing from Boston with a war cargo destined for Liverpool. [alce::662__wikidata_simple__dev::p2]

Cited: alce::662__wikidata_simple__dev::p0, alce::662__wikidata_simple__dev::p17, alce::662__wikidata_simple__dev::p2

### `157__wikidata_intersection__dev`
_Refused._

### `613__wikidata_simple__dev`
> **Pirate Party Luxembourg and Pirate Party of Galicia**
> The Pirate Party Luxembourg is a registered political party in Luxembourg that follows the pirate political doctrine developed by the Swedish Pirate Party. [alce::613__wikidata_simple__dev::p47]
> The Pirate Party of Galicia inherits the ideology from Pirate Party of Sweden, that seeks the reform of intellectual property and patent laws, the inclusion of direct democracy in the political system and the defense of Human Rights. [alce::613__wikidata_simple__dev::p77]

Cited: alce::613__wikidata_simple__dev::p47, alce::613__wikidata_simple__dev::p77

### `760__wikidata_simple__dev`
> **Hall**
> Hall served as a commissioned officer in the Royal New Zealand Air Force for five years, completing a degree at the University of Otago under a Defense Scholarship. [alce::760__wikidata_simple__dev::p7]
> Hall started video game development on an Amiga personal computer that his parents purchased him as a child, indicating he was a video game designer. [alce::760__wikidata_simple__dev::p7]

Cited: alce::760__wikidata_simple__dev::p7

### `290__wikidata_intersection__dev`
> **1983, 1985, 1989, and 1993 British Grand Prix**
> In 1983, Prost won his 1st of 5 British Grands Prix. [alce::290__wikidata_intersection__dev::p0]
> The 1985 British Grand Prix was won by McLaren driver Alain Prost after he started from third position. [alce::290__wikidata_intersection__dev::p4]
> The 1989 British Grand Prix was won by Frenchman Alain Prost, driving a McLaren-Honda, after he started from second position. [alce::290__wikidata_intersection__dev::p2]
> The 1993 British Grand Prix was won from pole position by Alain Prost, driving a Williams-Renault. [alce::290__wikidata_intersection__dev::p6]

Cited: alce::290__wikidata_intersection__dev::p0, alce::290__wikidata_intersection__dev::p2, alce::290__wikidata_intersection__dev::p4, alce::290__wikidata_intersection__dev::p6

### `764__wikidata_simple__dev`
> **Sailing dinghies**
> Jack Holt (1912–1995) was a prolific designer of sailing dinghies. [alce::764__wikidata_simple__dev::p0]
> He designed more than 40 boats, including famous designs such as the Mirror dinghy, Enterprise, GP14, Cadet, Hornet, Pacer, Solo, Streaker, Merlin Rocket, National 12, and Miracle. [alce::764__wikidata_simple__dev::p0, alce::764__wikidata_simple__dev::p1, alce::764__wikidata_simple__dev::p28]

Cited: alce::764__wikidata_simple__dev::p0, alce::764__wikidata_simple__dev::p1, alce::764__wikidata_simple__dev::p28

### `233__wikidata_intersection__dev`
> **World Series championships (9 total, most recently in 2018) and American League pennants**
> The Boston Red Sox have won nine World Series championships, most recently in 2018, and they have played in 13. [alce::233__wikidata_intersection__dev::p0, alce::233__wikidata_intersection__dev::p1]
> The Red Sox won World Series championships in 2004, 2007, 2013, and 2018. [alce::233__wikidata_intersection__dev::p5]
> In addition, they won the American League pennant, but were not able to defend their 1903 World Series championship when the New York Giants refused to participate in the 1904 World Series. [alce::233__wikidata_intersection__dev::p0, alce::233__wikidata_intersection__dev::p1]

Cited: alce::233__wikidata_intersection__dev::p0, alce::233__wikidata_intersection__dev::p1, alce::233__wikidata_intersection__dev::p5

### `97__wikitables_composition__dev`
> **Multiple killers went on rampages in Europe after 1995, including: Éric Borel (France), Gusztáv Nemeskéri (Hungary), and the Nighttime Killers - Vladyslav Volkovich and Volodymyr Kondratenko (Ukraine)**
> Éric Borel committed a shooting spree in France that resulted in 15 deaths, with the last death occurring on 2 March 1996. [alce::97__wikitables_composition__dev::p5]
> Gusztáv Nemeskéri, known as the Katóka Street Killer, is a Hungarian serial killer who killed 4 people between 1996 and 1999. [alce::97__wikitables_composition__dev::p62]
> The Nighttime Killers, Vladyslav Volkovich and Volodymyr Kondratenko, were responsible for a string of brutal murders in Kiev, Ukraine between 1991 and 1997, with two men arrested and charged with 16 murders. [alce::97__wikitables_composition__dev::p34]

Cited: alce::97__wikitables_composition__dev::p34, alce::97__wikitables_composition__dev::p5, alce::97__wikitables_composition__dev::p62

### `72__wikitables_composition__dev`
> **Bridge Street Town Centre (Huntsville), Brookwood Village (Mountain Brook/Homewood), and Riverchase Galleria (Hoover)**
> Bridge Street Town Centre is an upscale lifestyle center shopping center in Huntsville, Alabama, developed by O&S Holdings and designed by TSArchitects, both of Los Angeles. [alce::72__wikitables_composition__dev::p86]
> Brookwood Village is a upscale shopping mall located near Birmingham in the cities of Mountain Brook and Homewood, Alabama. [alce::72__wikitables_composition__dev::p68]
> Riverchase Galleria, locally known as The Galleria, is a large upscale, super–regional shopping mall in Hoover, Alabama, close to Birmingham, Alabama. [alce::72__wikitables_composition__dev::p43]

Cited: alce::72__wikitables_composition__dev::p43, alce::72__wikitables_composition__dev::p68, alce::72__wikitables_composition__dev::p86

### `647__wikidata_simple__dev`
> **Kenneth MacMillan created choreography for multiple ballets including Elite Syncopations, The Rite of Spring, and Romeo and Juliet**
> Elite Syncopations is a one-act ballet created in 1974 by Kenneth MacMillan for The Royal Ballet. [alce::647__wikidata_simple__dev::p37]
> The Rite of Spring is a one-act ballet created by Kenneth MacMillan in 1962 for the Royal Ballet. [alce::647__wikidata_simple__dev::p14]
> Choreographer Sir Kenneth MacMillan's Royal Ballet production of Sergei Prokofiev's Romeo and Juliet premiered at the Royal Opera House, Covent Garden on 9 February 1965. [alce::647__wikidata_simple__dev::p2]

Cited: alce::647__wikidata_simple__dev::p14, alce::647__wikidata_simple__dev::p2, alce::647__wikidata_simple__dev::p37

### `330__wikidata_intersection__dev`
> **Isaac Asimov Presents The Great SF Stories series**
> Isaac Asimov and Martin H. Greenberg edited multiple works in the 'Isaac Asimov Presents The Great SF Stories' series, including 'Isaac Asimov Presents The Great SF Stories 13 (1951)' and 'Isaac Asimov Presents The Great SF Stories 2 (1940)', which are collections of science fiction short stories from the Golden Age of Science Fiction. [alce::330__wikidata_intersection__dev::p21, alce::330__wikidata_intersection__dev::p7]

Cited: alce::330__wikidata_intersection__dev::p21, alce::330__wikidata_intersection__dev::p7

### `1003__wikidata_comp__dev`
> **The sources do not specify a single movie company for which George L. Little was a costume designer; rather, he worked as a costume designer for multiple films across different studios and directors.**
> George L. Little was an American costume designer who was best known for his work on Kathryn Bigelow's acclaimed war films, 'The Hurt Locker' and 'Zero Dark Thirty'. [alce::1003__wikidata_comp__dev::p0]
> He worked as costume designer on numerous films including 'The Prince and the Surfer', 'Things You Can Tell Just by Looking at Her', 'Behind Enemy Lines', 'Flight of the Phoenix', 'The Omen', 'The Crazies', 'Warm Bodies', 'Transcendence', and 'The Fantastic Four'. [alce::1003__wikidata_comp__dev::p1, alce::1003__wikidata_comp__dev::p4]
> His first film as head costume designer was Tony Scott's 1995 thriller 'Crimson Tide'. [alce::1003__wikidata_comp__dev::p3]

Cited: alce::1003__wikidata_comp__dev::p0, alce::1003__wikidata_comp__dev::p1, alce::1003__wikidata_comp__dev::p3, alce::1003__wikidata_comp__dev::p4

### `486__wikitables_simple__dev`
> **Prussian needle gun, Chassepot rifle, Berdan Type II, Mauser Model 1871, Gras rifle, M1903 Springfield, Karabiner 98 Kurz, Mosin-Nagant rifle, Lee-Enfield**
> The first general-issue military breechloader was a single-shot bolt action: the paper-cartridge Prussian needle gun of 1841. [alce::486__wikitables_simple__dev::p4]
> France countered in 1866 with its superior Chassepot rifle, also a paper-cartridge bolt action. [alce::486__wikitables_simple__dev::p4]
> The first metallic-cartridge bolt actions in general military service were the Berdan Type II introduced by Russia in 1870, the Mauser Model 1871, and a modified Chassepot, the Gras rifle of 1874. [alce::486__wikitables_simple__dev::p4]
> The Mauser rifle of the late 19th and early 20th centuries is the most famous of the bolt action types, with most similar weapons derived from this pioneering design, such as the M1903 Springfield and the Karabiner 98 Kurz rifle. [alce::486__wikitables_simple__dev::p0]
> The Russian Mosin–Nagant rifle, the British Lee–Enfield, and the Norwegian are bolt action rifles. [alce::486__wikitables_simple__dev::p0]

Cited: alce::486__wikitables_simple__dev::p0, alce::486__wikitables_simple__dev::p4

### `778__wikidata_simple__dev`
> **Thomas Hardesty Campbell, Samuel King, and Finis Ewing were ministers of the Cumberland Presbyterian Church**
> Thomas Hardesty Campbell (1907 – 1989) was a Cumberland Presbyterian minister, a former president and dean of Memphis Theological Seminary, and a former director of the Historical Foundation of the Cumberland Presbyterian Church. [alce::778__wikidata_simple__dev::p19]
> Reverend Samuel King (April 29, 1775 – September 13, 1842), was a Presbyterian minister and one of the founders of the Cumberland Presbyterian Church. [alce::778__wikidata_simple__dev::p32]
> Finis Ewing (July 10, 1773 – July 4, 1841) was the primary founder of the Cumberland Presbyterian Denomination on February 4, 1810. [alce::778__wikidata_simple__dev::p71]

Cited: alce::778__wikidata_simple__dev::p19, alce::778__wikidata_simple__dev::p32, alce::778__wikidata_simple__dev::p71

### `483__wikitables_simple__dev`
> **The highest military medals vary by country: Military Medal (Luxembourg), Medal of Valor (Israel), Medal of Honor (United States), and Hilal-i-Imtiaz (Pakistan)**
> The Military Medal is the highest military decoration of Luxembourg. [alce::483__wikitables_simple__dev::p12]
> The Medal of Valor is the highest Israeli military decoration. [alce::483__wikitables_simple__dev::p55]
> The Medal of Honor is the highest military decoration awarded by the United States government. [alce::483__wikitables_simple__dev::p14]
> The Hilal-i-Imtiaz is the highest medal awarded to military officers at the rank of Major General or Lieutenant General (Army), Air Vice-Marshals or Air Marshals (Air Force) and Rear-Admiral or Vice-Admiral (Navy, Coast Guard, and Marines) in Pakistan. [alce::483__wikitables_simple__dev::p7]

Cited: alce::483__wikitables_simple__dev::p12, alce::483__wikitables_simple__dev::p14, alce::483__wikitables_simple__dev::p55, alce::483__wikitables_simple__dev::p7

### `950__wikidata_comp__dev`
> **Rajan-Nagendra**
> The music Directors Rajan-Nagendra have worked with H.R. Bhargava for more than 20 films. [alce::950__wikidata_comp__dev::p0]

Cited: alce::950__wikidata_comp__dev::p0

### `334__wikidata_comp__dev`
_Refused._

### `770__wikidata_simple__dev`
> **Multiple students received their Ph.D. under Franz Boas, including John R. Swanton, Paul Radin, Ruth Benedict, Gladys Reichard, Ruth Bunzel, Alexander Lesser, Margaret Mead, Gene Weltfish, E. Adamson Hoebel, Jules Henry, George Herzog, and Ashley Montagu**
> Franz Boas trained numerous Ph.D. students at Columbia University, including John R. Swanton (who received his doctorate from Harvard in 1900), Paul Radin (1911), Ruth Benedict (1923), Gladys Reichard (1925), Ruth Bunzel (1929), Alexander Lesser (1929), Margaret Mead (1929), Gene Weltfish (1929), E. Adamson Hoebel (1934), Jules Henry (1935), George Herzog (1938), and Ashley Montagu (1938). [alce::770__wikidata_simple__dev::p0]
> Additional students who earned their Ph.D. under Boas's guidance include an unnamed student who earned his Ph.D. in Anthropology from Columbia University with a dissertation titled 'The Cattle Complex in East Africa,' and another student who completed his PhD under Boas's supervision with a thesis on the Alkatcho Carrier Indians of British Columbia. [alce::770__wikidata_simple__dev::p18, alce::770__wikidata_simple__dev::p25]

Cited: alce::770__wikidata_simple__dev::p0, alce::770__wikidata_simple__dev::p18, alce::770__wikidata_simple__dev::p25

### `830__wikidata_simple__dev`
> **Multiple countries including Soviet Union, Canada, China, Japan, Kazakhstan, Russia, Ukraine, Uzbekistan, and the Commonwealth of Independent States**
> The Soviet Union competed at two consecutive Hopman Cup tournaments and first competed in the 2nd Hopman Cup in 1990. [alce::830__wikidata_simple__dev::p69]
> Canada competed at the Hopman Cup tennis tournament on four occasions, in 2004, 2014, 2015 and 2018. [alce::830__wikidata_simple__dev::p40]
> China competed at the Hopman Cup tournament on two occasions, their debut coming at the 18th annual staging of the tournament in 2006. [alce::830__wikidata_simple__dev::p14]
> Japan competed at the Hopman Cup tournament on five occasions, the first being at the inaugural annual staging in 1989. [alce::830__wikidata_simple__dev::p52]
> Since the dissolution of the Soviet Union, four of the fifteen independent states formed from the former Soviet Union have competed in the Hopman Cup: Kazakhstan, Russia, Ukraine and Uzbekistan. [alce::830__wikidata_simple__dev::p69]
> The Commonwealth of Independent States competed at the Hopman Cup in 1992. [alce::830__wikidata_simple__dev::p83]

Cited: alce::830__wikidata_simple__dev::p14, alce::830__wikidata_simple__dev::p40, alce::830__wikidata_simple__dev::p52, alce::830__wikidata_simple__dev::p69, alce::830__wikidata_simple__dev::p83

### `83__wikitables_composition__dev`
> **Multiple Commodore products featured on-board BASIC**
> The BASIC included with the CBM-II series is known as BASIC 4.0+. [alce::83__wikitables_composition__dev::p0]
> The BASIC included on the original PET 2001 was known as Commodore BASIC 1.0. [alce::83__wikitables_composition__dev::p2]
> The Commodore LCD featured a built-in Commodore BASIC 3.6 interpreter. [alce::83__wikitables_composition__dev::p40]
> BASIC 7.0 was included on the Commodore 128. [alce::83__wikitables_composition__dev::p25]

Cited: alce::83__wikitables_composition__dev::p0, alce::83__wikitables_composition__dev::p2, alce::83__wikitables_composition__dev::p25, alce::83__wikitables_composition__dev::p40

### `300__wikidata_comp__dev`
> **Pamplin Media Group operates primarily in the Portland metropolitan area in Oregon, with publishing entities in multiple counties including Multnomah, Washington, Clackamas, and Columbia counties, as well as in Central Oregon and Salem.**
> Pamplin Media Group (PMG) is a media conglomerate owned by Robert B. Pamplin, Jr. and operating primarily in the Portland metropolitan area in the U.S. state of Oregon. [alce::300__wikidata_comp__dev::p0]
> As of 2009, it owned newspapers in Multnomah, Washington, Clackamas, and Columbia counties. [alce::300__wikidata_comp__dev::p0]
> The company also acquired newspapers in the Portland area and 'The Madras Pioneer' in Central Oregon, and in 2018, the 'Salem Reporter' joined the bureau. [alce::300__wikidata_comp__dev::p16, alce::300__wikidata_comp__dev::p2]

Cited: alce::300__wikidata_comp__dev::p0, alce::300__wikidata_comp__dev::p16, alce::300__wikidata_comp__dev::p2

### `273__wikidata_intersection__dev`
> **2008 British Grand Prix and 2014 British Grand Prix (and others)**
> The 2008 British Grand Prix was won by Lewis Hamilton for the McLaren team after starting from fourth position on the grid. [alce::273__wikidata_intersection__dev::p1]
> The 2014 British Grand Prix was won by Lewis Hamilton for the Mercedes team, from a sixth position start. [alce::273__wikidata_intersection__dev::p3]
> Lewis Hamilton achieved his fifth British Grand Prix win, equalling the records of Alain Prost and Jim Clark, who won the race five times each. [alce::273__wikidata_intersection__dev::p8]

Cited: alce::273__wikidata_intersection__dev::p1, alce::273__wikidata_intersection__dev::p3, alce::273__wikidata_intersection__dev::p8

### `575__wikidata_simple__dev`
> **Yellow Magic Orchestra, Sadistic Mika Band, METAFIVE, and Sketch Show**
> Yukihiro Takahashi is best known internationally as the drummer and lead vocalist of the Yellow Magic Orchestra, and as the former drummer of the Sadistic Mika Band. [alce::575__wikidata_simple__dev::p0]
> He is currently a member of the group METAFIVE. [alce::575__wikidata_simple__dev::p0]
> Since 2002 he has been working in the duo Sketch Show with his ex-YMO bandmate Haruomi Hosono. [alce::575__wikidata_simple__dev::p6]

Cited: alce::575__wikidata_simple__dev::p0, alce::575__wikidata_simple__dev::p6

### `1257__wikitables_composition__dev`
> **Baltic 1 wind farm**
> Among many ongoing developments in wind power, the Baltic 1 wind farm was commissioned on 2 May 2011. [alce::1257__wikitables_composition__dev::p17]

Cited: alce::1257__wikitables_composition__dev::p17

### `132__wikidata_comp__dev`
> **Sibi Malayil directed a film produced by Ranjith**
> Ranjith and Shaji Kailas produced the film 'Ustaad', directed by Sibi Malayil, starring Mohanlal. [alce::132__wikidata_comp__dev::p47]

Cited: alce::132__wikidata_comp__dev::p47

### `901__wikidata_simple__dev`
> **Friedrich August, Friedrich Bachmann, Elwin Bruno Christoffel, Paul Bachmann, Joseph Brutkowski, Heinrich Eduard Heine, Rudolf Lipschitz, Leo Pochhammer, Friedrich Prym, Wilhelm Wagner, Hermann Waldaestel, Wilhelm Wernicke, Elena Gerz, Valentien Gerz, and Johanna Gerz**
> Ohm's students included Friedrich August, Friedrich Bachmann, Elwin Bruno Christoffel, Paul Bachmann, Joseph Brutkowski, Heinrich Eduard Heine, Rudolf Lipschitz, Leo Pochhammer, Friedrich Prym, Wilhelm Wagner, Hermann Waldaestel, Wilhelm Wernicke, Elena Gerz, Valentien Gerz, and Johanna Gerz. [alce::901__wikidata_simple__dev::p1]

Cited: alce::901__wikidata_simple__dev::p1

### `940__wikidata_simple__dev`
_Refused._

### `61__wikitables_composition__dev`
> **WUCL, WZKS, WMOX, WKZB, WOKK, WEXR, WYHL, WJXM, WMAW-FM**
> WUCL (FM 105.7), WZKS (FM 104.1), WMOX (AM 1010), WKZB (FM 97.9), WOKK (FM 97.1), WEXR (FM 106.9), WYHL (AM 1450), and WJXM (FM 95.1) are popular stations in the Meridian Arbitron Radio Market. [alce::61__wikitables_composition__dev::p0]
> WMAW-FM (FM 88.1) broadcasts Mississippi Public Broadcasting in the Meridian area. [alce::61__wikitables_composition__dev::p0]
> WOKK (97.1 FM) is a country music-formatted radio station broadcasting in the Meridian, Mississippi, Arbitron market. [alce::61__wikitables_composition__dev::p90]
> WJXM (95.1 FM) is an urban contemporary music formatted radio station broadcasting in the Meridian, Mississippi, Arbitron market. [alce::61__wikitables_composition__dev::p1]

Cited: alce::61__wikitables_composition__dev::p0, alce::61__wikitables_composition__dev::p1, alce::61__wikitables_composition__dev::p90

### `1360__wikidata_simple__dev`
> **North America**
> The Caribbean is a region of North America that consists of the Caribbean Sea, its islands (some surrounded by the Caribbean Sea and some bordering both the Caribbean Sea and the North Atlantic Ocean) and the surrounding coasts. [alce::1360__wikidata_simple__dev::p10]

Cited: alce::1360__wikidata_simple__dev::p10

### `814__wikidata_simple__dev`
> **Leonardo da Vinci**
> Andrea del Verrocchio was an Italian painter, sculptor, and goldsmith who was a master of an important workshop in Florence, and his pupils included Leonardo da Vinci, Pietro Perugino and Lorenzo di Credi. [alce::814__wikidata_simple__dev::p0]
> In 1466, at the age of 14, Leonardo was apprenticed to the artist Andrea di Cione, known as Verrocchio, whose workshop was one of the finest in Florence. [alce::814__wikidata_simple__dev::p5]

Cited: alce::814__wikidata_simple__dev::p0, alce::814__wikidata_simple__dev::p5

### `591__wikidata_simple__dev`
> **Swords Against Darkness**
> As an editor Offutt produced a series of five anthologies entitled 'Swords Against Darkness' [alce::591__wikidata_simple__dev::p6]

Cited: alce::591__wikidata_simple__dev::p6

### `159__wikidata_comp__dev`
> **Employees attended various schools including the University of Oregon and Yale Law School**
> One employee attended the University of Oregon in 1934 and then the School of Law at the University of Oregon, graduating with a J.D. in 1937, and later earned an advanced degree from Yale Law School. [alce::159__wikidata_comp__dev::p32]
> Another employee was appointed to a position at the University of Oregon School of Law in 1935 as a professor by Dean Wayne Morse. [alce::159__wikidata_comp__dev::p34]

Cited: alce::159__wikidata_comp__dev::p32, alce::159__wikidata_comp__dev::p34

### `531__wikitables_simple__dev`
> **Notable reefs include the Great Barrier Reef, Belize Barrier Reef, New Caledonian Barrier Reef, Lighthouse Reef, and the Florida reef system**
> Earth's largest and most famous reef is the Great Barrier Reef. [alce::531__wikitables_simple__dev::p13]
> Other major examples of barrier reefs are the Belize Barrier Reef and the New Caledonian Barrier Reef. [alce::531__wikitables_simple__dev::p1]
> Lighthouse Reef is known as a snorkelling and diving destination, considered as one of the best dive sites in Belize and the whole Caribbean. [alce::531__wikitables_simple__dev::p52]
> Notable individual reefs in the Florida reef system include reefs along the Florida coast north of the Florida Keys. [alce::531__wikitables_simple__dev::p0]

Cited: alce::531__wikitables_simple__dev::p0, alce::531__wikitables_simple__dev::p1, alce::531__wikitables_simple__dev::p13, alce::531__wikitables_simple__dev::p52

### `840__wikidata_simple__dev`
> **North American geosynchronous satellites**
> SES Americom was a major commercial satellite operator of North American geosynchronous satellites based in the United States. [alce::840__wikidata_simple__dev::p0]
> Before being merged into SES World Skies in 2009, SES Americom operated North American satellites in geosynchronous orbit. [alce::840__wikidata_simple__dev::p1]
> SES Americom took operational control of AMC-21, a communications satellite, in September 2008. [alce::840__wikidata_simple__dev::p11]

Cited: alce::840__wikidata_simple__dev::p0, alce::840__wikidata_simple__dev::p1, alce::840__wikidata_simple__dev::p11

### `872__wikidata_simple__dev`
> **Kofi Annan**
> The Donostia-San Sebastián International Peace Conference included six international personalities known for their work in the field of politics and pacification: Kofi Annan (former UN Secretary-General), Bertie Ahern (former Taoiseach of Ireland), Gro Harlem Brundtland (international leader in sustainable development and public health, former Prime Minister of Norway), Pierre Joxe (former Interior Minister of France), Gerry Adams (president of Sinn Féin, member of the Irish Parliament) and Jonathan Powell (British diplomat who served as the first Downing Street Chief of Staff). [alce::872__wikidata_simple__dev::p0, alce::872__wikidata_simple__dev::p9]

Cited: alce::872__wikidata_simple__dev::p0, alce::872__wikidata_simple__dev::p9

### `303__wikidata_comp__dev`
> **Multiple Fidelity Investments employees attended different schools**
> Edward Johnson III, who owns and runs Fidelity Investments, attended prep school at Milton Academy before transferring to Tabor Academy and graduating with a Bachelor's degree from Harvard College in 1954. [alce::303__wikidata_comp__dev::p14]
> Peter Lynch, hired as an intern with Fidelity Investments in 1966, graduated from Boston College where he studied history, psychology and philosophy, and earned a Master of Business Administration from the Wharton School of the University of Pennsylvania in 1968. [alce::303__wikidata_comp__dev::p0]
> Kathleen Murphy, President of Fidelity Personal Investing, graduated summa cum laude with a Bachelor of Arts degree in both Economics and Political Science from Fairfield University and holds a Juris Doctor degree with highest honors from the University of Connecticut School of Law. [alce::303__wikidata_comp__dev::p19]
> Anne Richards, chief executive officer of Fidelity International, was educated at the Royal High School, Edinburgh and graduated from the University of Edinburgh with a First Class Honours degree in Electronics and Electrical Engineering. [alce::303__wikidata_comp__dev::p38]

Cited: alce::303__wikidata_comp__dev::p0, alce::303__wikidata_comp__dev::p14, alce::303__wikidata_comp__dev::p19, alce::303__wikidata_comp__dev::p38

### `94__wikitables_composition__dev`
> **Jimmie Lee Jackson**
> Jimmie Lee Jackson was an African American civil rights activist who was shot by Alabama State Trooper James Bonard Fowler on February 18, 1965, and died eight days later on February 26, 1965. [alce::94__wikitables_composition__dev::p10, alce::94__wikitables_composition__dev::p37]
> Jackson was shot twice in the abdomen while participating in a peaceful voting rights march in Marion, Alabama. [alce::94__wikitables_composition__dev::p37]

Cited: alce::94__wikitables_composition__dev::p10, alce::94__wikitables_composition__dev::p37

### `3__wikitables_composition__dev`
_Refused._

### `270__wikidata_intersection__dev`
> **The Camp on Blood Island**
> The Camp on Blood Island is a 1958 British World War II film, directed by Val Guest for Hammer Film Productions. [alce::270__wikidata_intersection__dev::p50]
> Val Guest was an English film director and screenwriter who is best known for his work for Hammer, for whom he directed 14 films. [alce::270__wikidata_intersection__dev::p0]

Cited: alce::270__wikidata_intersection__dev::p0, alce::270__wikidata_intersection__dev::p50

### `433__wikidata_intersection__dev`
_Refused._

### `63__wikitables_composition__dev`
> **Pilgrim Hall Museum**
> The Pilgrim Hall Museum at 75 Court Street in Plymouth, Massachusetts is the oldest public museum in the United States in continuous operation, having opened in 1824. [alce::63__wikitables_composition__dev::p0]
> Plimoth Plantation is a living history museum in Plymouth, Massachusetts founded in 1947. [alce::63__wikitables_composition__dev::p2]
> The Plymouth Antiquarian House is an historic house museum at 126 Water Street in Plymouth, Massachusetts. [alce::63__wikitables_composition__dev::p89]

Cited: alce::63__wikitables_composition__dev::p0, alce::63__wikitables_composition__dev::p2, alce::63__wikitables_composition__dev::p89

### `530__wikitables_simple__dev`
> **Discovered and hypothesized physical particles include Standard Model particles, fundamental particles, quasiparticles, and proposed substructure particles**
> Discovered elementary particles include quarks, gluons, leptons, gravitons, neutrinos, and the Higgs boson. [alce::530__wikitables_simple__dev::p16]
> All the Standard Model particles were discovered below the energy scale of approximately 10 eV or 1 TeV. [alce::530__wikitables_simple__dev::p68]
> The graviton is a hypothetical elementary spin-2 particle proposed to mediate gravitation that remains undiscovered. [alce::530__wikitables_simple__dev::p67]
> Proposed fundamental particles or intermediate particles include prequarks, subquarks, maons, alphons, quinks, rishons, tweedles, helons, haplons, Y-particles, and primons, with 'preon' being the leading name in the physics community. [alce::530__wikitables_simple__dev::p48]
> Quasiparticles include excitons, magnons, phonons, plasmons, phasons, polarons, and rotons, which represent quanta of corresponding excitations. [alce::530__wikitables_simple__dev::p16]

Cited: alce::530__wikitables_simple__dev::p16, alce::530__wikitables_simple__dev::p48, alce::530__wikitables_simple__dev::p67, alce::530__wikitables_simple__dev::p68

### `676__wikidata_simple__dev`
> **Multiple works of literature, including novels by Jennifer Roberson, Hans Christian Andersen's "The Wild Swans", "The Frog Prince" by Brothers Grimm, George RR Martin's "The Ice Dragon", Bram Stoker's "Dracula", and Jodi Picoult's "Between the Lines"**
> Gilbert has provided the cover art for many of Jennifer Roberson's novels, including "Lady of the Forest" (1992) and its sequel "Lady of Sherwood" (1999), "Lady of the Glen" (1996), and the 2001 republications of her "Chronicles of the Cheysuli" fantasy series. [alce::676__wikidata_simple__dev::p5]
> Gilbert designed the art in "The Wild Swans" in 2005, featured in a republication of Hans Christian Andersen's story. [alce::676__wikidata_simple__dev::p5]
> She has also provided the illustrations for the Brothers Grimm work "The Frog Prince", retold by Kathy-Jo Wargin in 2007. [alce::676__wikidata_simple__dev::p1]
> In 2006, she redesigned the cover of George RR Martin's 1980 novel "The Ice Dragon". [alce::676__wikidata_simple__dev::p4]
> In 2010, she provided the illustrations seen in an abridged, young adult version of Bram Stoker's "Dracula", as told by author Nicky Raven. [alce::676__wikidata_simple__dev::p4]
> Gilbert produced the "traditional fairy tale type" illustrations for Jodi Picoult's first young adult novel "Between the Lines", published in 2012. [alce::676__wikidata_simple__dev::p4]

Cited: alce::676__wikidata_simple__dev::p1, alce::676__wikidata_simple__dev::p4, alce::676__wikidata_simple__dev::p5

### `932__wikidata_simple__dev`
_Refused._

### `342__wikidata_intersection__dev`
> **Wulfstan**
> Wulfstan (died 1023) was an English Bishop of London, Bishop of Worcester, and Archbishop of York. [alce::342__wikidata_intersection__dev::p26]
> In 1002 he was elected simultaneously to the diocese of Worcester and the archdiocese of York, holding both in plurality until 1016, when he relinquished Worcester; he remained archbishop of York until his death. [alce::342__wikidata_intersection__dev::p26]

Cited: alce::342__wikidata_intersection__dev::p26

### `823__wikidata_simple__dev`
> **Get a Job**
> Lionsgate Premiere is the specialty film division of entertainment company Lionsgate Films that specializes in direct-to-video and direct-to-VOD films. [alce::823__wikidata_simple__dev::p1]
> The division will also release select films by CBS Films as part of the distribution partnership with parent company Lionsgate, with the first release being "Get a Job". [alce::823__wikidata_simple__dev::p0]

Cited: alce::823__wikidata_simple__dev::p0, alce::823__wikidata_simple__dev::p1

### `543__wikitables_simple__dev`
> **Graham Gouldman, Eric Stewart, Kevin Godley, Lol Creme, and Rick Fenn**
> The band initially consisted of four musicians – Graham Gouldman, Eric Stewart, Kevin Godley, and Lol Creme – who had written and recorded together for some three years, before assuming the name '10cc' in 1972. [alce::543__wikitables_simple__dev::p1]
> Rick Fenn is best known for being a member of the band 10cc since 1976. [alce::543__wikitables_simple__dev::p3]
> After Godley and Creme left the band in 1976, Gouldman and Stewart were the main creative forces behind 10cc. [alce::543__wikitables_simple__dev::p0]

Cited: alce::543__wikitables_simple__dev::p0, alce::543__wikitables_simple__dev::p1, alce::543__wikitables_simple__dev::p3

### `838__wikidata_simple__dev`
> **Multiple entities were part of NATO, including Belgium, Canada, Denmark, France, Iceland, Italy, Luxembourg, the Netherlands, Norway, Portugal, the United Kingdom, and the United States as founding members, with additional members joining later such as Greece, Turkey, Albania, Croatia, and Montenegro.**
> Twelve countries were part of the founding of NATO: Belgium, Canada, Denmark, France, Iceland, Italy, Luxembourg, the Netherlands, Norway, Portugal, the United Kingdom, and the United States. [alce::838__wikidata_simple__dev::p8]
> Greece and Turkey joined NATO in 1952, with Greece later suspending its membership in 1974 before rejoining. [alce::838__wikidata_simple__dev::p8]
> Albania and Croatia joined NATO on 1 April 2009, and Montenegro joined on 5 June 2017. [alce::838__wikidata_simple__dev::p92]

Cited: alce::838__wikidata_simple__dev::p8, alce::838__wikidata_simple__dev::p92

### `1014__wikidata_comp__dev`
> **Royal Navy and Royal Australian Navy**
> The J, K and N class was a class of 24 destroyers of the Royal Navy launched in 1938. [alce::1014__wikidata_comp__dev::p0]
> HMAS 'Nepal' (G25/D14) was an N-class destroyer of the Royal Australian Navy (RAN). [alce::1014__wikidata_comp__dev::p89]

Cited: alce::1014__wikidata_comp__dev::p0, alce::1014__wikidata_comp__dev::p89

### `687__wikidata_simple__dev`
> **Meitei people are Manipuri citizens**
> The Meitei (also Meetei, Meithei, Manipuri) people are the majority ethnic group of Manipur, a northeastern state of India. [alce::687__wikidata_simple__dev::p10]
> Manipur is a state in Northeast India with a population of almost 3 million, including the Meitei, who are the majority group in the state. [alce::687__wikidata_simple__dev::p26]

Cited: alce::687__wikidata_simple__dev::p10, alce::687__wikidata_simple__dev::p26

### `87__wikitables_composition__dev`
_Refused._

### `910__wikidata_simple__dev`
> **Actuality Specials**
> Actuality Specials is an American television series consisting of a collection of documentaries produced by NBC News and broadcast during the 1960s. [alce::910__wikidata_simple__dev::p7]

Cited: alce::910__wikidata_simple__dev::p7

### `34__wikitables_composition__dev`
> **1939-1942 and 1946-1949**
> Eddie Anderson served as the head football coach at the University of Iowa from 1939–1942 and 1946–1949. [alce::34__wikitables_composition__dev::p8]
> The 1939 Iowa Hawkeyes football team was coached by Eddie Anderson. [alce::34__wikitables_composition__dev::p86]
> In 1948, Eddie Anderson was in his seventh and final season as Iowa's head coach. [alce::34__wikitables_composition__dev::p4]
> In 1946, Eddie Anderson returned as head coach for the Hawkeyes for his fifth season as Iowa's head coach. [alce::34__wikitables_composition__dev::p5]

Cited: alce::34__wikitables_composition__dev::p4, alce::34__wikitables_composition__dev::p5, alce::34__wikitables_composition__dev::p8, alce::34__wikitables_composition__dev::p86

### `842__wikidata_simple__dev`
> **Professor Garry W. Jenkins and Stras were part of the University of Minnesota Law School staff**
> The law school's 11th dean is Professor Garry W. Jenkins, formerly Associate Dean for Academic Affairs at The Ohio State University Moritz College of Law and chief operating officer and general counsel of the Goldman Sachs Foundation. [alce::842__wikidata_simple__dev::p3]
> While he was on the faculty of University of Minnesota Law School, he was also a counsel at Faegre & Bensen. [alce::842__wikidata_simple__dev::p30]

Cited: alce::842__wikidata_simple__dev::p3, alce::842__wikidata_simple__dev::p30

### `489__wikitables_simple__dev`
> **Professional wrestling streaming services include WWE Network, New Japan Pro-Wrestling World, Global Wrestling Network, and WWNLive/Club WWN**
> WWE Network is a subscription-based video streaming service owned by the WWE, using the infrastructure of BAMTech. [alce::489__wikitables_simple__dev::p8]
> New Japan Pro-Wrestling World is a subscription-based video streaming service owned by New Japan Pro-Wrestling. [alce::489__wikitables_simple__dev::p7]
> Global Wrestling Network (GWN) is a video streaming service and mobile app owned by Anthem Wrestling Exhibitions, a subsidiary of Anthem Sports & Entertainment and parent company of Impact Wrestling. [alce::489__wikitables_simple__dev::p60]
> The World Wrestling Network (WWN) is a professional wrestling governing body and internet streaming and video on demand service originating from the United States. [alce::489__wikitables_simple__dev::p14]
> WWNLive launched a replacement streaming service called Club WWN. [alce::489__wikitables_simple__dev::p14]

Cited: alce::489__wikitables_simple__dev::p14, alce::489__wikitables_simple__dev::p60, alce::489__wikitables_simple__dev::p7, alce::489__wikitables_simple__dev::p8

### `1361__wikidata_simple__dev`
> **Richard Sandomir**
> Richard Sandomir is an obituary writer for the New York Times. [alce::1361__wikidata_simple__dev::p86]

Cited: alce::1361__wikidata_simple__dev::p86

### `614__wikidata_simple__dev`
> **Uncle Henry's Nuclear Waste Dump**
> "Uncle Henry's Nuclear Waste Dump" (1986) has similarities to "Tetris", though it was published prior to "Tetris" reaching the US, and the author claims he hadn't seen it. [alce::614__wikidata_simple__dev::p3]

Cited: alce::614__wikidata_simple__dev::p3

### `54__wikitables_composition__dev`
_Refused._

### `142__wikidata_intersection__dev`
> **Back to the Future**
> Bob Gale famously co-wrote the science fiction comedy film "Back to the Future" with writing partner Robert Zemeckis, and the screenplays for the film's two sequels. [alce::142__wikidata_intersection__dev::p0]

Cited: alce::142__wikidata_intersection__dev::p0

### `209__wikidata_intersection__dev`
> **Devaraagam**
> Devaraagam is a 1996 Indian Malayalam-language film directed by Bharathan and starring Arvind Swamy and Sridevi in the lead roles. [alce::209__wikidata_intersection__dev::p4]

Cited: alce::209__wikidata_intersection__dev::p4

### `510__wikitables_simple__dev`
> **Crystal Bach and Crystal Mahler**
> River cruise ships of the Rhine class named 'Crystal Bach' and 'Crystal Mahler' were laid down at the Wismar shipyard. [alce::510__wikitables_simple__dev::p40]
> A river cruise is a voyage along inland waterways, often stopping at multiple ports along the way. [alce::510__wikitables_simple__dev::p0]

Cited: alce::510__wikitables_simple__dev::p0, alce::510__wikitables_simple__dev::p40

### `762__wikidata_simple__dev`
> **Sheikh Uways al-Barawi**
> Sheikh Uways al-Barawi of the Tuuni clan improved the application of the Arabic script to represent Somali in the 19th century, applying it to the Maay dialect of southern Somalia. [alce::762__wikidata_simple__dev::p7]
> Various Somali wadaads and scholars had used the Arabic script to write in Somali for centuries before al-Barawi's improvements. [alce::762__wikidata_simple__dev::p7]

Cited: alce::762__wikidata_simple__dev::p7

### `188__wikidata_intersection__dev`
> **Jeevan Prabhat**
> Jeevan Prabhat (Dawn Of Life) is a 1937 Hindi film social drama, produced by Bombay Talkies and directed by Franz Osten. [alce::188__wikidata_intersection__dev::p3]
> The music director was Saraswati Devi with lyrics and dialogues by J. S. Casshyap. [alce::188__wikidata_intersection__dev::p3]

Cited: alce::188__wikidata_intersection__dev::p3

### `906__wikidata_simple__dev`
> **Amaran (1992) and over 30 other films including Maman Magal, Luckyman, Asuran, Sevaalaperi Paandi, and Kovilpatti Veeralakshmi**
> Adithyan Aadithyan was an Indian film score and soundtrack composer who made his debut as composer with 'Amaran' (1992) with songs like 'Vethala Potta' and 'Chandirane Suriyane' becoming chartbusters. [alce::906__wikidata_simple__dev::p0]
> He went on to work in over 30 films including Maman Magal, Luckyman, Asuran, Sevaalaperi Paandi, Kovilpatti Veeralakshmi among others. [alce::906__wikidata_simple__dev::p0]
> He has predominantly scored music for Tamil films apart from working in Telugu and Malayalam films. [alce::906__wikidata_simple__dev::p1]

Cited: alce::906__wikidata_simple__dev::p0, alce::906__wikidata_simple__dev::p1

### `546__wikitables_simple__dev`
> **Notable landslides occurred in California, New Zealand (Napier, Wimbledon, Hawke's Bay region), and Germany (Öschingen, Farrenberg, Buchberg, Talheim)**
> Landslides are common in Southern California, the San Francisco Bay Area and other parts of Northern California, and the Sierra Nevada. [alce::546__wikitables_simple__dev::p0]
> In Napier, several tonnes of rock fell from Bluff Hill during the earthquake and smaller slips continually occurred for at least three days with each passing aftershock. Many landslides also occurred near Wimbledon, with the largest landslide being near the top of Sergeant's Hill, about a 40–50 meter wide slump gave way, taking down hundreds of trees with it. [alce::546__wikitables_simple__dev::p5]
> Other major landslides occurred, also after previous heavy rainfall, on 3 June 2013. The area of about one hectare was taken solely at the landslide in the Öschingen cottage settlement. More landslides occurred on the southwest side of the Farrenberg, on Buchberg, at the Talheim waterfalls and at the Talheim platforms. [alce::546__wikitables_simple__dev::p20]

Cited: alce::546__wikitables_simple__dev::p0, alce::546__wikitables_simple__dev::p20, alce::546__wikitables_simple__dev::p5

### `207__wikidata_comp__dev`
> **Sony Pictures**
> Jon Spaihts is an American screenwriter who wrote the screenplay for the 2016 film 'Passengers'. [alce::207__wikidata_comp__dev::p1, alce::207__wikidata_comp__dev::p3]
> The 2016 film 'Passengers' was made by Sony Pictures, produced by Original Film and Company. [alce::207__wikidata_comp__dev::p2]

Cited: alce::207__wikidata_comp__dev::p1, alce::207__wikidata_comp__dev::p2, alce::207__wikidata_comp__dev::p3

### `977__wikidata_comp__dev`
> **Hirokazu Tanaka (Chip Tanaka)**
> Hiromichi Tanaka was part of Square's original Planning and Development department, and the sources indicate he worked on projects including Final Fantasy XIV. [alce::977__wikidata_comp__dev::p43, alce::977__wikidata_comp__dev::p47]
> Hirokazu Tanaka, also known as Chip Tanaka, is a Japanese musician and composer who pioneered chiptune music and was one of Nintendo's in-house composers. [alce::977__wikidata_comp__dev::p0]
> Hirokazu 'Hip' Tanaka was the composer of the original 'Metroid'. [alce::977__wikidata_comp__dev::p18]

Cited: alce::977__wikidata_comp__dev::p0, alce::977__wikidata_comp__dev::p18, alce::977__wikidata_comp__dev::p43, alce::977__wikidata_comp__dev::p47

### `1009__wikidata_comp__dev`
> **Multiple winners of the Evian Championship including Chun In-gee (2016), Lydia Ko (2015), and Angela Stanford (2018)**
> Chun In-gee won her first Evian and second major championship at the 2016 Evian Championship, four strokes ahead of runners-up Ryu So-yeon and Park Sung-hyun. [alce::1009__wikidata_comp__dev::p0]
> Lydia Ko won her first major championship at the 2015 Evian Championship, becoming the youngest major winner at age 18. [alce::1009__wikidata_comp__dev::p1]
> At the age of 40, Angela Stanford won her first major championship at the 2018 Evian Championship on her 76th appearance in a major. [alce::1009__wikidata_comp__dev::p2]

Cited: alce::1009__wikidata_comp__dev::p0, alce::1009__wikidata_comp__dev::p1, alce::1009__wikidata_comp__dev::p2

### `276__wikidata_comp__dev`
> **Lone Scherfig**
> David Nicholls adapted his novel as a film script, and the film was directed by Lone Scherfig for Random House Films and Focus Features, with a theatrical release in August 2011. [alce::276__wikidata_comp__dev::p37]

Cited: alce::276__wikidata_comp__dev::p37

### `747__wikidata_simple__dev`
> **Multiple individuals worked for military branches of the Kingdom of Prussia, including King Frederick the Great, Field Marshal Helmuth von Moltke, and others employed by the Prussian Military Academy**
> King Frederick the Great, a formidable battle commander, led the disciplined Prussian troops to victory during the 18th-century Silesian Wars. [alce::747__wikidata_simple__dev::p1]
> The Prussian army was controlled by the General Staff, under Field Marshal Helmuth von Moltke. [alce::747__wikidata_simple__dev::p6]
> The Prussian Military Academy employed him, almost as a matter of course, in important instructional work (Clausewitz was one of his students). [alce::747__wikidata_simple__dev::p77]

Cited: alce::747__wikidata_simple__dev::p1, alce::747__wikidata_simple__dev::p6, alce::747__wikidata_simple__dev::p77

### `796__wikidata_simple__dev`
> **Zee Horror Show**
> Zee Horror Show is a TV series presented by Ramsay Brothers on Zee TV in the period 1993-1997. [alce::796__wikidata_simple__dev::p0]
> It was a very popular program in the 90s that featured short stories in the form of 4 to 5 episodes, each one based on suspense and horror. [alce::796__wikidata_simple__dev::p0]

Cited: alce::796__wikidata_simple__dev::p0

### `856__wikidata_simple__dev`
> **Porto Velho is the capital of the Brazilian state of Rondônia, located in the upper Amazon River basin on the eastern shore of the Madeira River**
> Porto Velho is the capital of the Brazilian state of Rondônia, in the upper Amazon River basin. [alce::856__wikidata_simple__dev::p1]
> It is located on the border of Rondônia and the state of Amazonas. [alce::856__wikidata_simple__dev::p1]
> It is on the eastern shore of the Madeira River, one of the main tributaries of the Amazon River. [alce::856__wikidata_simple__dev::p1]

Cited: alce::856__wikidata_simple__dev::p1

### `151__wikidata_intersection__dev`
> **Kaadhal Mannan**
> Saran's first film was 'Kaadhal Mannan', which featured music composer Bharathwaj making his debut. [alce::151__wikidata_intersection__dev::p2]
> The film saw music composer Bharathwaj debut, and the film's soundtrack gained rave review prior to release. [alce::151__wikidata_intersection__dev::p2]

Cited: alce::151__wikidata_intersection__dev::p2

### `392__wikidata_intersection__dev`
> **Goldfinger**
> Guy Hamilton directed Goldfinger, a film for which Harry Saltzman was responsible for production. [alce::392__wikidata_intersection__dev::p34, alce::392__wikidata_intersection__dev::p4]
> Broccoli and Saltzman turned to Guy Hamilton to direct Goldfinger. [alce::392__wikidata_intersection__dev::p34]
> Saltzman co-founded Danjaq, S.A. with Albert R. Broccoli in 1962, a holding company responsible for producing the James Bond films including Goldfinger. [alce::392__wikidata_intersection__dev::p4]

Cited: alce::392__wikidata_intersection__dev::p34, alce::392__wikidata_intersection__dev::p4

### `580__wikidata_simple__dev`
> **Multiple coaches including Steve King, Jude Macdonald, and James Dack**
> Steve King was re-appointed as manager on 13 September 2017 and departed at the end of the season to be replaced by Hawks successful U18 manager Jude Macdonald. [alce::580__wikidata_simple__dev::p3]
> James Dack is an English professional football coach and manager, most recently first team manager at National League South club Whitehawk. [alce::580__wikidata_simple__dev::p16]
> Asensio was appointed Assistant Manager at Whitehawk under Steve King on 10 February 2014, and took over as Caretaker Manager when King left his post in January 2016. [alce::580__wikidata_simple__dev::p12]

Cited: alce::580__wikidata_simple__dev::p12, alce::580__wikidata_simple__dev::p16, alce::580__wikidata_simple__dev::p3

### `701__wikidata_simple__dev`
> **King Crimson**
> Tony Levin is best known for his work with King Crimson and Peter Gabriel. [alce::701__wikidata_simple__dev::p0]
> He was also a member of Liquid Tension Experiment, Bruford Levin Upper Extremities, ProjeKct One, and ProjeKct Four. [alce::701__wikidata_simple__dev::p0]
> He has led his own band, Stick Men. [alce::701__wikidata_simple__dev::p0]

Cited: alce::701__wikidata_simple__dev::p0

### `168__wikidata_comp__dev`
> **Dan Gilroy**
> Dan Gilroy is best known for writing and directing "Nightcrawler" (2014). [alce::168__wikidata_comp__dev::p0]
> Once the script was finalized, Gilroy knew that he wanted to direct the film, referring to Nightcrawler. [alce::168__wikidata_comp__dev::p33]

Cited: alce::168__wikidata_comp__dev::p0, alce::168__wikidata_comp__dev::p33

### `785__wikidata_simple__dev`
> **Bodysong, Kelly + Victor, No Greater Love, Looking For Light, Institute Benjamenta, I Could Read The Sky, and Made In Heaven**
> Janine Marmot is a British film producer and founder of Hot Property Films, best known for the BAFTA-winning documentary Bodysong and the relationship drama Kelly + Victor, which won the Outstanding British Debut BAFTA award in 2014. [alce::785__wikidata_simple__dev::p1]
> Her feature credits as Producer include Simon Pummell's BAFTA and BIFA winning feature documentary Bodysong, scored by Jonny Greenwood of Radiohead and Shock Head Soul; Michael Whyte's No Greater Love and Looking For Light, Institute Benjamenta directed by The Brothers Quay; I Could Read The Sky directed by Nichola Bruce; and the multi directed film Made In Heaven. [alce::785__wikidata_simple__dev::p1]

Cited: alce::785__wikidata_simple__dev::p1

### `761__wikidata_simple__dev`
_Refused._

### `340__wikidata_comp__dev`
> **Bahman Maghsoudlou**
> Abbas Kiarostami: A Report is a 2013 documentary film about the Iranian filmmaker Abbas Kiarostami, produced and directed by Bahman Maghsoudlou. [alce::340__wikidata_comp__dev::p5]
> Abbas Kiarostami was an Iranian film director, screenwriter, poet, photographer and film producer who attained critical acclaim for directing numerous films. [alce::340__wikidata_comp__dev::p2]

Cited: alce::340__wikidata_comp__dev::p2, alce::340__wikidata_comp__dev::p5

### `792__wikidata_simple__dev`
> **Multiple marine vessels including Great Lakes freighters, destroyer escorts, landing craft, and yachts**
> In the early 1950s Defoe Shipbuilding constructed two large Great Lakes freighters, with one of the two vessels still in service on the Great Lakes as of April 2009, the M/V 'Ojibway'. [alce::792__wikidata_simple__dev::p4]
> From 1939 to 1945, the company built 154 ships, including four s, 13 destroyer escorts, 11 destroyer transports (converted destroyer escorts), patrol craft, and numerous landing craft of various types. [alce::792__wikidata_simple__dev::p2]
> From 1920 to 1939, the company built various types of government and commercial vessels and private yachts, including three Coast Guard Cutters. [alce::792__wikidata_simple__dev::p3]

Cited: alce::792__wikidata_simple__dev::p2, alce::792__wikidata_simple__dev::p3, alce::792__wikidata_simple__dev::p4

### `458__wikidata_intersection__dev`
> **1974 FA Cup Final and 1996 Premier League fixture**
> The 1974 FA Cup Final was an association football match between Liverpool and Newcastle United on Saturday, 4 May 1974 at Wembley Stadium, London. [alce::458__wikidata_intersection__dev::p15]
> On 3 April 1996, Liverpool faced Newcastle United in a Premier League fixture at Anfield, during the 1995–96 season. [alce::458__wikidata_intersection__dev::p3]

Cited: alce::458__wikidata_intersection__dev::p15, alce::458__wikidata_intersection__dev::p3

### `888__wikidata_simple__dev`
> **Brent Park**
> Brent Park is a small public park of 2.24 hectares in Hendon in the London Borough of Barnet, with the River Brent running along its western edge. [alce::888__wikidata_simple__dev::p96]
> The park is a narrow wooded strip of land west of the North Circular Road between Brent Street and Bell Lane, and there are three ponds next to the river. [alce::888__wikidata_simple__dev::p96]

Cited: alce::888__wikidata_simple__dev::p96

### `839__wikidata_simple__dev`
> **Anarky**
> Alan Grant is the creator of the characters Anarky, Victor Zsasz, and the Ventriloquist. [alce::839__wikidata_simple__dev::p0, alce::839__wikidata_simple__dev::p1]
> The creation of the supervillain Anarky was initially intended as a vehicle for exploring his political opinions through the comic medium. [alce::839__wikidata_simple__dev::p2]

Cited: alce::839__wikidata_simple__dev::p0, alce::839__wikidata_simple__dev::p1, alce::839__wikidata_simple__dev::p2

### `724__wikidata_simple__dev`
> **Naval Base San Diego is home port to approximately 54 ships, including 46 U.S. Navy ships, two Littoral Combat Ships, two U.S. Coast Guard cutters, and eight ships of the Military Sealift Command**
> Naval Base San Diego is home port to approximately 54 ships, including 46 U.S. Navy ships, two Littoral Combat Ships, two U.S. Coast Guard cutters, and eight ships of the Military Sealift Command. [alce::724__wikidata_simple__dev::p28]
> San Diego Bay also remains as a home port of major assets, including several aircraft carriers, of the United States Pacific Fleet. [alce::724__wikidata_simple__dev::p52]
> Several cruise lines home port in San Diego, such as Holland America, Celebrity Cruises, Disney Cruise Line, and Royal Caribbean. [alce::724__wikidata_simple__dev::p0]

Cited: alce::724__wikidata_simple__dev::p0, alce::724__wikidata_simple__dev::p28, alce::724__wikidata_simple__dev::p52

### `363__wikidata_comp__dev`
> **Berklee College of Music**
> Greg Hawkes, a keyboardist for the rock band The Cars, attended Berklee College of Music for two years, majoring in composition and flute. [alce::363__wikidata_comp__dev::p2]

Cited: alce::363__wikidata_comp__dev::p2

### `107__wikidata_intersection__dev`
> **2013, 2012, 2009, and 2007**
> Lewis Hamilton won the Hungarian Grand Prix four times: in 2013, 2012, 2009, and 2007. [alce::107__wikidata_intersection__dev::p1]
> The 2013 Hungarian Grand Prix was won by Lewis Hamilton after starting from pole position, marking his first win since joining Mercedes for 2013. [alce::107__wikidata_intersection__dev::p2]
> The 2009 Hungarian Grand Prix was won by Lewis Hamilton for McLaren-Mercedes, after starting from fourth place on the grid. [alce::107__wikidata_intersection__dev::p3]

Cited: alce::107__wikidata_intersection__dev::p1, alce::107__wikidata_intersection__dev::p2, alce::107__wikidata_intersection__dev::p3

### `574__wikidata_simple__dev`
> **Mogacho Anvddo**
> The first full length Konkani film was "Mogacho Anvddo", released on 24 April 1950, and was produced and directed by A. L.Jerry Braganza, a native of Mapusa. [alce::574__wikidata_simple__dev::p0]

Cited: alce::574__wikidata_simple__dev::p0

### `501__wikitables_simple__dev`
> **Yokozuna (Rodney Agatupu Anoai) and historical sumo wrestlers**
> Rodney Agatupu Anoai (October 2, 1966 – October 23, 2000) was an American professional wrestler who is best known for his time with the World Wrestling Federation (WWF) where he wrestled under the ring name Yokozuna. [alce::501__wikitables_simple__dev::p0]
> Akashi Shiganosuke (c. 1600 – c. 1649) is purported to be a sumo wrestler in antiquity who is formally recognized as the first yokozuna. [alce::501__wikitables_simple__dev::p10]
> Tanikaze was the first to receive a 'yokozuna' licence and perform the 'yokozuna' 'dohyo-iri' and so is often regarded as the first 'real' 'yokozuna'. [alce::501__wikitables_simple__dev::p10]
> Chiyonofuji reached the 'yokozuna' rank as a sumo wrestler from Fukushima, Hokkaidō. [alce::501__wikitables_simple__dev::p72]

Cited: alce::501__wikitables_simple__dev::p0, alce::501__wikitables_simple__dev::p10, alce::501__wikitables_simple__dev::p72

### `1300__wikidata_simple__dev`
> **Dr. James Hal Cone, Delores S. Williams, Dr. Gary Dorrien, and Dr. James A. Forbes**
> Dr. James Hal Cone is one of the founders of liberation theology and is active in the development of African-American theology at Union. [alce::1300__wikidata_simple__dev::p3]
> Union has been home to Womanist theologian Delores S. Williams. [alce::1300__wikidata_simple__dev::p3]
> Dr. Gary Dorrien is a social ethicist at Union. [alce::1300__wikidata_simple__dev::p3]
> Dr. James A. Forbes, the former senior pastor of the adjacent Riverside Church, is an adjunct professor at the seminary. [alce::1300__wikidata_simple__dev::p3]

Cited: alce::1300__wikidata_simple__dev::p3

### `390__wikidata_comp__dev`
> **Vetrimaaran**
> Vetrimaaran prepared a script for Dhanush, who was the lead hero of the film he worked on, and Dhanush immediately accepted the offer after hearing the story. [alce::390__wikidata_comp__dev::p19]
> The film titled was 'Desiya Nedunchalai 47' was initially launched with Yuvan Shankar Raja as the music director and Ekambaram as the cinematographer. [alce::390__wikidata_comp__dev::p19]

Cited: alce::390__wikidata_comp__dev::p19

### `887__wikidata_simple__dev`
> **Tesla produces the Model S, Model X, and Model 3**
> Tesla offers three car models: the Model S, Model X and Model 3. [alce::887__wikidata_simple__dev::p14]
> As of June 2018, Tesla sells the Model S, Model X and Model 3 vehicles. [alce::887__wikidata_simple__dev::p1]

Cited: alce::887__wikidata_simple__dev::p1, alce::887__wikidata_simple__dev::p14

### `878__wikidata_simple__dev`
_Refused._

### `752__wikidata_simple__dev`
> **Films credited to Ivan Goff as screenwriter include "White Heat" (1949), "Man of a Thousand Faces" (1957), "Charlie's Angels" pilot (1976), "The Captain from Köpenick" (1945), "Portrait in Black" (1960), "Captain Horatio Hornblower" (1951), and "Into the Night"**
> Ivan Goff was an Australian screenwriter, best known for his collaborations with Ben Roberts including "White Heat" (1949), "Man of a Thousand Faces" (1957) and the pilot for "Charlie's Angels" (1976). [alce::752__wikidata_simple__dev::p0]
> Goff was also credited on a comedy for PRC, "The Captain from Köpenick" (1945), which would be the last film he wrote without Roberts for the rest of his career. [alce::752__wikidata_simple__dev::p8]
> Ivan Goff and Ben Roberts had written a popular play, "Portrait in Black" (later made into a motion picture of the same name in 1960). [alce::752__wikidata_simple__dev::p15]
> Roberts and Goff contributed to the success of such varied projects as "White Heat" (1949), "Captain Horatio Hornblower" (1951), and other films. [alce::752__wikidata_simple__dev::p9]
> Warners hired Goff and Roberts to work on the crime story "Into the Night." [alce::752__wikidata_simple__dev::p15]

Cited: alce::752__wikidata_simple__dev::p0, alce::752__wikidata_simple__dev::p15, alce::752__wikidata_simple__dev::p8, alce::752__wikidata_simple__dev::p9

### `423__wikidata_comp__dev`
> **Multiple countries (Australia, Russia, and the United States)**
> Dante Exum is an Australian professional basketball player for the Utah Jazz who was selected by the Utah Jazz with the fifth overall pick in the 2014 draft. [alce::423__wikidata_comp__dev::p1]
> Andrei Kirilenko is a Russian-American retired professional basketball player who was drafted by the Utah Jazz twenty-fourth overall in 1999. [alce::423__wikidata_comp__dev::p86]
> Joe Ingles is an Australian professional basketball player for the Utah Jazz of the National Basketball Association (NBA). [alce::423__wikidata_comp__dev::p9]

Cited: alce::423__wikidata_comp__dev::p1, alce::423__wikidata_comp__dev::p86, alce::423__wikidata_comp__dev::p9

### `214__wikidata_comp__dev`
> **Rector, Dean, Faculty, Diocesan Superintendent of Schools, Assistant Principal, Assistant Rector, Pastor, Chief Academic Officer, Censor Librorum**
> After being ordained, Monsignor Bonner became an assistant rector of St. Bridget's Church in Philadelphia. Two years later, In April 1919, he became the assistant principal of Roman Catholic High School in which he had formerly been a student. In August 1926, he was appointed Diocesan Superintendent of Schools and held that position until he died of a heart attack on November 27, 1945. [alce::214__wikidata_comp__dev::p75]
> Dean, Theology Division, Saint Charles Borromeo Seminary 1999–2010 and Faculty, Saint Charles Borromeo Seminary, Theology Division 1999–2010, as well as Censor Librorum, Archdiocese of Philadelphia 1991–2010, and Pastor, Our Lady of Grace, Penndel PA 2010–2017. [alce::214__wikidata_comp__dev::p10]
> Reverend Monsignor Joseph G. Prior is the former rector of St. Charles Borromeo Seminary in Philadelphia, Pennsylvania, United States. Msgr. Prior is the current pastor at Our Lady of Grace, Penndel, (Langhorne) Pennsylvania, which is a part of the Archdiocese of Philadelphia. [alce::214__wikidata_comp__dev::p30]
> Chief Academic Officer, Saint Charles Borromeo Seminary 2000-2002. [alce::214__wikidata_comp__dev::p30]

Cited: alce::214__wikidata_comp__dev::p10, alce::214__wikidata_comp__dev::p30, alce::214__wikidata_comp__dev::p75

### `304__wikidata_comp__dev`
> **Shaji Kailas directed a Red Chillies Entertainment series**
> Red Chillies is a 2009 Indian Malayalam crime thriller film directed by Shaji Kailas. [alce::304__wikidata_comp__dev::p0]
> Red Chillies Entertainment (RCE) is an Indian motion picture production, distribution and a premier visual effects company based in the city of Mumbai. [alce::304__wikidata_comp__dev::p4]

Cited: alce::304__wikidata_comp__dev::p0, alce::304__wikidata_comp__dev::p4

### `411__wikidata_intersection__dev`
> **Dhand**
> Ranjith Bajpe also written directed "Dhand" (2015) which is the first Tulu language movie released in Israel Australia and UK. [alce::411__wikidata_intersection__dev::p45]

Cited: alce::411__wikidata_intersection__dev::p45

### `84__wikitables_composition__dev`
> **Multiple singles - "Tell Me (You're Coming Back)", "Little Red Rooster", "Brown Sugar" among others**
> "Tell Me (You're Coming Back)" was an A-side of a Rolling Stones single from their debut album, released as a single in the US only. [alce::84__wikitables_composition__dev::p7]
> "Little Red Rooster" was the Rolling Stones' fifth UK single, released in November 1964 and became their second No. 1 hit in the UK. [alce::84__wikitables_composition__dev::p6]
> "Brown Sugar" is a song by the Rolling Stones and the lead single from their album "Sticky Fingers" (1971). [alce::84__wikitables_composition__dev::p16]

Cited: alce::84__wikitables_composition__dev::p16, alce::84__wikitables_composition__dev::p6, alce::84__wikitables_composition__dev::p7

### `153__wikidata_intersection__dev`
> **Multiple Woody Allen films including "Zelig", "The Purple Rose of Cairo", "Broadway Danny Rose", "Stardust Memories", "Hannah and Her Sisters", "Radio Days", "Bullets Over Broadway", "Everyone Says I Love You", "Sweet and Lowdown", "The Curse of the Jade Scorpion", and "Melinda and Melinda"**
> Hyman has served as composer/arranger/conductor/pianist for the Woody Allen films "Zelig", "The Purple Rose of Cairo", "Broadway Danny Rose", "Stardust Memories", "Hannah and Her Sisters", "Radio Days", "Bullets Over Broadway", "Everyone Says I Love You", "Sweet and Lowdown", "The Curse of the Jade Scorpion" and "Melinda and Melinda". [alce::153__wikidata_intersection__dev::p0]

Cited: alce::153__wikidata_intersection__dev::p0

### `65__wikitables_composition__dev`
> **Skövde**
> Skövde Municipality is a municipality in Västra Götaland County in western Sweden, with its seat located in the city of Skövde. [alce::65__wikitables_composition__dev::p0]
> Skövde is a locality and urban centre in Skövde Municipality and Västra Götaland County. [alce::65__wikitables_composition__dev::p2]

Cited: alce::65__wikitables_composition__dev::p0, alce::65__wikitables_composition__dev::p2

### `265__wikidata_comp__dev`
> **The Great Lakes and other bodies of water near U.S. states**
> Ontario's border with the United States follows inland waterways including Lake of the Woods, the Rainy River, the Pigeon River, Lake Superior, the St. Marys River, Lake Huron, the St. Clair River, Lake St. Clair, the Detroit River, Lake Erie, the Niagara River, Lake Ontario and the St. Lawrence River, which border U.S. states of Minnesota, Michigan, Ohio, Pennsylvania, and New York. [alce::265__wikidata_comp__dev::p7]
> Kentucky is bordered by the Mississippi River to the west, the Ohio River to the north, and the Big Sandy River and Tug Fork to the east. [alce::265__wikidata_comp__dev::p74]
> The Southeast Region includes marine waters off U.S. states of North Carolina, South Carolina, Georgia, Florida, Alabama, Mississippi, Louisiana, and Texas. [alce::265__wikidata_comp__dev::p75]

Cited: alce::265__wikidata_comp__dev::p7, alce::265__wikidata_comp__dev::p74, alce::265__wikidata_comp__dev::p75

### `215__wikidata_intersection__dev`
> **Elmer Gantry**
> Richard Brooks was an American screenwriter, film director, novelist and film producer who was best known for several films including 'Elmer Gantry' (1960), for which he won the Academy Award for Best Adapted Screenplay. [alce::215__wikidata_intersection__dev::p1]
> As a screenwriter, film director, and producer, Brooks received multiple credits on his major works throughout his career. [alce::215__wikidata_intersection__dev::p1]

Cited: alce::215__wikidata_intersection__dev::p1

### `98__wikitables_composition__dev`
> **Meramec River U.S. 66 Bridge and Merchants Bridge**
> The Meramec River U.S. 66 Bridge (J421) was built in 1931 when US 66 was rerouted to pass through Times Beach. [alce::98__wikitables_composition__dev::p65]
> The Merchants Bridge is a railroad-only bridge built in 1889. [alce::98__wikitables_composition__dev::p5]

Cited: alce::98__wikitables_composition__dev::p5, alce::98__wikitables_composition__dev::p65

### `853__wikidata_simple__dev`
_Refused._

### `112__wikidata_comp__dev`
> **Will Gluck**
> In 2014, Aline Brosh McKenna wrote the musical comedy-drama 'Annie', directed by Will Gluck. [alce::112__wikidata_comp__dev::p6]

Cited: alce::112__wikidata_comp__dev::p6

### `357__wikidata_intersection__dev`
> **1964 VFL Grand Final**
> The 1964 VFL Grand Final was an Australian rules football game contested between the Collingwood Football Club and Melbourne Football Club, held at the Melbourne Cricket Ground in Melbourne on 19 September 1964. [alce::357__wikidata_intersection__dev::p70]
> The match was won by Melbourne by a margin of 4 points, marking that club's 12th premiership victory. [alce::357__wikidata_intersection__dev::p70]

Cited: alce::357__wikidata_intersection__dev::p70

### `877__wikidata_simple__dev`
> **Isuzu Erga and Hino Rainbow**
> The Isuzu Erga is a heavy-duty single-decker bus marketed by the Japanese manufacturer Isuzu and introduced in 2000, and it is built by J-Bus from Japan either as a step-entrance bus or a low-floor bus. [alce::877__wikidata_simple__dev::p86]
> The Hino Rainbow is a medium-duty single-decker bus marketed by the Japanese manufacturer Hino since 1980, and it is built by J-Bus. [alce::877__wikidata_simple__dev::p32]

Cited: alce::877__wikidata_simple__dev::p32, alce::877__wikidata_simple__dev::p86

### `709__wikidata_simple__dev`
> **Muzaffar Hassan, Karimullah, and Zafar Mahmood Abbasi served in the Navy of Pakistan**
> Vice-Admiral Muzzafar Hassan was a three-star rank admiral who served as the last Commander-in-Chief of Pakistan Navy from 1969 until 1972. [alce::709__wikidata_simple__dev::p52]
> Karimullah served in the Pakistan Navy, joining in October 1965 and later being promoted to Sub-Lieutenant. [alce::709__wikidata_simple__dev::p20]
> Admiral Zafar Mahmood Abbasi is a four-star rank admiral in the Pakistan Navy who has been serving as the Chief of the Naval Staff since 7 October 2017, having joined the Pakistan Navy in 1979. [alce::709__wikidata_simple__dev::p67]

Cited: alce::709__wikidata_simple__dev::p20, alce::709__wikidata_simple__dev::p52, alce::709__wikidata_simple__dev::p67

### `488__wikitables_simple__dev`
> **Sturmgewehr 44, M16A1, FN FAL, FN CAL, Heckler & Koch G3, SIG SG 543, SIG SG 542, Vz. 58, Winchester carbines, and Lee Enfield Cavalry Carbine**
> Carbines consisted of Sturmgewehr 44, M16A1, FN FAL (variants included the Israeli-produced 'lightened' ROMAT M1953), FN CAL, Heckler & Koch G3, SIG SG 543 carbines, SIG SG 542, Vz. 58, AK-47 and AKM assault rifles. [alce::488__wikitables_simple__dev::p13]
> Recognizable carbines were the lever-action Winchester carbines, with several versions available firing revolver cartridges. [alce::488__wikitables_simple__dev::p17]
> The Lee Enfield Cavalry Carbine (LEC) a shortened version of the standard British Army infantry rifle was introduced in 1896. [alce::488__wikitables_simple__dev::p17]

Cited: alce::488__wikitables_simple__dev::p13, alce::488__wikitables_simple__dev::p17

### `348__wikidata_comp__dev`
> **Anton Corbijn**
> Andrew Bovell wrote the thriller film "A Most Wanted Man", which was directed by Anton Corbijn. [alce::348__wikidata_comp__dev::p0]

Cited: alce::348__wikidata_comp__dev::p0

### `912__wikidata_simple__dev`
> **The Circle**
> In 2000 Panahi made "The Circle", produced by Jafar Panahi Film Productions and Mikado-Lumiere&Co. [alce::912__wikidata_simple__dev::p2]

Cited: alce::912__wikidata_simple__dev::p2

### `266__wikidata_intersection__dev`
> **Miami Vice (2006)**
> Michael Mann is an American film director, screenwriter, and producer of film and television who is best known for his distinctive brand of stylized crime drama. [alce::266__wikidata_intersection__dev::p2]
> After 'Collateral', Mann directed the film adaptation of 'Miami Vice' which he also executive produced. [alce::266__wikidata_intersection__dev::p1]

Cited: alce::266__wikidata_intersection__dev::p1, alce::266__wikidata_intersection__dev::p2

### `74__wikitables_composition__dev`
_Refused._

### `890__wikidata_simple__dev`
> **St Mary's Church in Twickenham**
> John James (c. 1673 – 15 May 1746) was a British architect particularly associated with Twickenham in west London, where he rebuilt St Mary's Church. [alce::890__wikidata_simple__dev::p0]

Cited: alce::890__wikidata_simple__dev::p0

### `1013__wikidata_comp__dev`
> **Dartmouth College and The Ohio State University Moritz College of Law**
> The law school's 11th dean is Professor Garry W. Jenkins, formerly Associate Dean for Academic Affairs at The Ohio State University Moritz College of Law and chief operating officer and general counsel of the Goldman Sachs Foundation. [alce::1013__wikidata_comp__dev::p5]
> He graduated from Minnetonka High School in Minnetonka, then attended Dartmouth College in Hanover, New Hampshire, earning a B.A. degree. [alce::1013__wikidata_comp__dev::p55]

Cited: alce::1013__wikidata_comp__dev::p5, alce::1013__wikidata_comp__dev::p55

### `581__wikidata_simple__dev`
> **Multiple buildings including St Mary the Virgin at Wanstead, St James Piccadilly, St Bartholomew-the-Less, St John's Church in St John's Wood, and St Mary in Marylebone Road**
> Thomas Hardwick designed the church of St Mary the Virgin at Wanstead, completed in 1790. [alce::581__wikidata_simple__dev::p29, alce::581__wikidata_simple__dev::p48]
> He restored Sir Christopher Wren's St James, Piccadilly and re-built George Dance the Younger's St Bartholomew-the-Less in West Smithfield (1823–25). [alce::581__wikidata_simple__dev::p29]
> He designed St John's Church in St John's Wood High Street (1813–14) and the church of St Mary in Marylebone Road (1813–17), arguably his most notable work. [alce::581__wikidata_simple__dev::p29]

Cited: alce::581__wikidata_simple__dev::p29, alce::581__wikidata_simple__dev::p48

### `345__wikidata_comp__dev`
_Refused._

### `294__wikidata_comp__dev`
> **Satyadev Dubey**
> Satyadev Dubey presented it in movie form in 1971 with Tendulkar's collaboration as the screenplay writer. [alce::294__wikidata_comp__dev::p26]

Cited: alce::294__wikidata_comp__dev::p26

### `1__wikitables_composition__dev`
> **Marko Arnautović**
> On 2 September 2013, Arnautović joined Premier League side Stoke City on a four-year contract for a fee of £2 million. [alce::1__wikitables_composition__dev::p15]

Cited: alce::1__wikitables_composition__dev::p15

### `337__wikidata_comp__dev`
_Refused._

### `571__wikidata_simple__dev`
> **Multiple officers held the position of Chief of the National Guard Bureau, including Earl T. Ricks, Donald W. McGowan, Wilson, and Joseph L. Lengyel**
> Earl T. Ricks was the first to hold the office of Deputy Chief of the National Guard Bureau, and in 1953 served as acting Chief of the National Guard Bureau, making him the first Air Guard officer to hold the chief's position. [alce::571__wikidata_simple__dev::p3, alce::571__wikidata_simple__dev::p6]
> Donald W. McGowan was appointed Chief of the National Guard Bureau after the retirement of Edgar C. Erickson. [alce::571__wikidata_simple__dev::p33]
> In 1963, Wilson was appointed chief of the National Guard Bureau, the first Air Force officer to be officially named to the position. [alce::571__wikidata_simple__dev::p33]
> Joseph L. Lengyel, a United States Air Force officer, has served as Chief of the National Guard Bureau since 2016. [alce::571__wikidata_simple__dev::p37]

Cited: alce::571__wikidata_simple__dev::p3, alce::571__wikidata_simple__dev::p33, alce::571__wikidata_simple__dev::p37, alce::571__wikidata_simple__dev::p6

### `942__wikidata_simple__dev`
> **Multiple TV series including "Hannibal", "Star Trek: Discovery", and others**
> Bryan Fuller is an American television writer and producer who has created a number of television series, including "Dead Like Me", "Wonderfalls", "Pushing Daisies", "Hannibal", and "American Gods". [alce::942__wikidata_simple__dev::p1]
> Bryan Fuller was expected to write the pilot episode and executive produce alongside Justin Falvey and Darryl Frank for a series created by Steven Spielberg. [alce::942__wikidata_simple__dev::p54]
> Bryan Fuller served as a writer-producer on NBC's "Heroes" and was brought in to write a pilot script for another series, which received a 13-episode first season order. [alce::942__wikidata_simple__dev::p10]
> In February 2016, Bryan Fuller was announced as the showrunner and co-creator of "Star Trek: Discovery" alongside Alex Kurtzman. [alce::942__wikidata_simple__dev::p26]

Cited: alce::942__wikidata_simple__dev::p1, alce::942__wikidata_simple__dev::p10, alce::942__wikidata_simple__dev::p26, alce::942__wikidata_simple__dev::p54

### `101__wikidata_intersection__dev`
> **Football League First Division fixture, FA Charity Shield, and FA Community Shield**
> On 20 October 1990, Manchester United Football Club faced Arsenal Football Club in a Football League First Division fixture at Old Trafford, during the 1990–91 season. [alce::101__wikidata_intersection__dev::p8]
> The 1999 edition of the FA Charity Shield was contested between Manchester United and Arsenal. [alce::101__wikidata_intersection__dev::p15]
> The 2003 edition of the FA Community Shield, an annual English football match, was contested between Manchester United and Arsenal at Cardiff's Millennium Stadium on 10 August. [alce::101__wikidata_intersection__dev::p97]

Cited: alce::101__wikidata_intersection__dev::p15, alce::101__wikidata_intersection__dev::p8, alce::101__wikidata_intersection__dev::p97

### `922__wikidata_simple__dev`
> **Takion**
> Kupperberg created the "Takion" series as well. [alce::922__wikidata_simple__dev::p6]

Cited: alce::922__wikidata_simple__dev::p6

### `585__wikidata_simple__dev`
> **Multiple books including Rosemary Sutcliff's historical novels, "Charley, Charlotte and the Golden Canary", "The Highwayman", "Wuthering Heights", "All Quiet on the Western Front", and "The God Beneath the Sea"**
> Charles Keeping first came to prominence with his illustrations of Rosemary Sutcliff's historical novels for children. [alce::585__wikidata_simple__dev::p0]
> He illustrated his own story 'Charley, Charlotte and the Golden Canary' (1967) and a new edition (1981) of Alfred Noyes's poem 'The Highwayman'. [alce::585__wikidata_simple__dev::p0]
> He illustrated the complete works of Charles Dickens for the Folio Society. [alce::585__wikidata_simple__dev::p0]
> In 1964 Keeping illustrated his first book for the Folio Society, an edition of Emily Brontë's 'Wuthering Heights'. [alce::585__wikidata_simple__dev::p2]
> He followed this with Erich Maria Remarque's 'All Quiet on the Western Front' (1966). [alce::585__wikidata_simple__dev::p2]
> Charles Keeping drew fifteen illustrations for 'The God Beneath the Sea'. [alce::585__wikidata_simple__dev::p11]

Cited: alce::585__wikidata_simple__dev::p0, alce::585__wikidata_simple__dev::p11, alce::585__wikidata_simple__dev::p2

### `807__wikidata_simple__dev`
> **Waterford County Museum Society**
> The Waterford County Museum Society is a non-profit organization that was founded explicitly to run the Waterford County Museum following a meeting convened in 1982 by the Dungarvan Irish Countrywomen's Association. [alce::807__wikidata_simple__dev::p37]
> The museum is located in the Old Town Hall in Dungarvan, which is in County Waterford. [alce::807__wikidata_simple__dev::p37]

Cited: alce::807__wikidata_simple__dev::p37

### `129__wikidata_intersection__dev`
> **1882, 1884, and 1885 FA Cup Finals**
> Blackburn Rovers competed in the 1882 FA Cup Final, where they lost 1–0 to Old Etonians. [alce::129__wikidata_intersection__dev::p74]
> Jimmy Douglas played in the 1884 FA Cup Final when Blackburn Rovers faced Queen's Park Glasgow and won 2–1. [alce::129__wikidata_intersection__dev::p74]
> Blackburn Rovers competed in the 1885 FA Cup Final on 4 April 1885 against Queen's Park Glasgow, winning 2–0. [alce::129__wikidata_intersection__dev::p74]
> Blackburn Rovers have won six FA Cups in total throughout their history. [alce::129__wikidata_intersection__dev::p84]

Cited: alce::129__wikidata_intersection__dev::p74, alce::129__wikidata_intersection__dev::p84

### `795__wikidata_simple__dev`
> **General M. A. G. Osmani**
> The military council was headed by General M. A. G. Osmani and eleven sector commanders. [alce::795__wikidata_simple__dev::p41]
> Osmani was reinstated from retirement to active duty into the Armed Forces of Bangladesh as its senior most official, with the rank of Colonel reactivated. [alce::795__wikidata_simple__dev::p32]
> Colonel Muhammad Ataul Gani Osmani (Appointed General 1972) served as BD Forces C-in-C. [alce::795__wikidata_simple__dev::p22]

Cited: alce::795__wikidata_simple__dev::p22, alce::795__wikidata_simple__dev::p32, alce::795__wikidata_simple__dev::p41

### `451__wikidata_intersection__dev`
> **Type VIIC/41**
> Type VIIC/41 was a slightly modified version of the VIIC and had the same armament and engines. [alce::451__wikidata_intersection__dev::p8]
> The Type VII was the most numerous German U-boat force, with 568 commissioned from 1940 to 1945, and Type VIIC/41 was one of the modifications of the Type VII design. [alce::451__wikidata_intersection__dev::p75, alce::451__wikidata_intersection__dev::p8]

Cited: alce::451__wikidata_intersection__dev::p75, alce::451__wikidata_intersection__dev::p8

### `329__wikidata_intersection__dev`
> **Super Bowls XVI, XIX, XXIII, XXIV, and XXIX**
> The 49ers have won five NFL championships – all Super Bowls. They were the first team to win five Super Bowls (Super Bowls XVI, XIX, XXIII, XXIV, and XXIX). [alce::329__wikidata_intersection__dev::p1]
> The 49ers also competed in Super Bowl XLVII, which was their first Super Bowl appearance since Super Bowl XXIX. [alce::329__wikidata_intersection__dev::p10, alce::329__wikidata_intersection__dev::p88]

Cited: alce::329__wikidata_intersection__dev::p1, alce::329__wikidata_intersection__dev::p10, alce::329__wikidata_intersection__dev::p88

### `43__wikitables_composition__dev`
> **Municipalities in Cameron County, Pennsylvania include Shippen Township, Lumber Township, Portage Township, Grove Township, Gibson Township, and the borough of Emporium**
> Under Pennsylvania law, there are four types of incorporated municipalities: cities, boroughs, townships, and, in at most two cases, towns. The following boroughs and townships are located in Cameron County: [alce::43__wikitables_composition__dev::p1]
> Shippen Township is a township in Cameron County, Pennsylvania, United States, with a population of 2,232 at the 2010 census. [alce::43__wikitables_composition__dev::p11]
> Lumber Township is a township in Cameron County, Pennsylvania, United States, with a population of 195 at the 2010 census. [alce::43__wikitables_composition__dev::p10]
> Lumber Township is bordered by Portage Township to the north and west, Grove Township to the east, Gibson Township to the south and Shippen Township to the west and north. [alce::43__wikitables_composition__dev::p10]
> The borough of Emporium, the county seat, lies enclaved within the eastern part of Shippen Township. [alce::43__wikitables_composition__dev::p11]

Cited: alce::43__wikitables_composition__dev::p1, alce::43__wikitables_composition__dev::p10, alce::43__wikitables_composition__dev::p11

### `370__wikidata_intersection__dev`
> **River-class frigate**
> She was laid down on 17 November 1943 by Canadian Vickers Ltd. at Montreal, Quebec and launched 28 March 1944. [alce::370__wikidata_intersection__dev::p17]
> The River-class frigate was designed by William Reed of Smith's Dock Company of South Bank-on-Tees. [alce::370__wikidata_intersection__dev::p17]

Cited: alce::370__wikidata_intersection__dev::p17

### `229__wikidata_intersection__dev`
> **Multiple VFL/AFL Grand Finals including the 1909 VFL Grand Final and 1981 VFL Grand Final**
> Carlton Football Club has been involved in 29 VFL/AFL Grand Finals from 1897-2006, winning 16 premiership titles. [alce::229__wikidata_intersection__dev::p2]
> The 1909 VFL Grand Final was an Australian rules football game contested between the Carlton Football Club and South Melbourne Football Club, held at the Melbourne Cricket Ground in Melbourne on 2 October 1909. [alce::229__wikidata_intersection__dev::p34]
> The 1981 VFL Grand Final was an Australian rules football game contested between the Carlton Football Club and Collingwood Football Club, held at the Melbourne Cricket Ground in Melbourne on 26 September 1981. [alce::229__wikidata_intersection__dev::p6]

Cited: alce::229__wikidata_intersection__dev::p2, alce::229__wikidata_intersection__dev::p34, alce::229__wikidata_intersection__dev::p6

### `673__wikidata_simple__dev`
> **Florida Reef**
> The Florida Keys National Marine Sanctuary includes the Florida Reef, the only barrier coral reef in North America and the third-largest coral barrier reef in the world. [alce::673__wikidata_simple__dev::p1]

Cited: alce::673__wikidata_simple__dev::p1

### `256__wikidata_comp__dev`
> **Multiple Baltimore Orioles draftees attended different schools**
> Baumann attended Mahtomedi High School in Mahtomedi, Minnesota, and the Baltimore Orioles selected him in the third round of the 2017 MLB draft. [alce::256__wikidata_comp__dev::p5]
> Dylan Bundy was drafted by the Orioles with the fourth overall pick in the 2011 Major League Baseball Draft and attended Owasso High School in Owasso, Oklahoma. [alce::256__wikidata_comp__dev::p86]
> Branden Becker was drafted by the Orioles in the 17th round of the 2015 Major League Baseball Draft and attended Cajon High School in San Bernardino, California. [alce::256__wikidata_comp__dev::p52]
> Cedric Mullins attended Brookwood High School in Snellville, Georgia and was drafted by the Baltimore Orioles in the 13th round of the 2015 Major League Baseball Draft. [alce::256__wikidata_comp__dev::p43]

Cited: alce::256__wikidata_comp__dev::p43, alce::256__wikidata_comp__dev::p5, alce::256__wikidata_comp__dev::p52, alce::256__wikidata_comp__dev::p86

### `1005__wikidata_comp__dev`
> **Detyens Shipyards, Inc.**
> Charleston Naval Shipyard ceased operations as a U.S. Navy facility in 1996 and was leased to Detyens Shipyards, Inc. [alce::1005__wikidata_comp__dev::p0, alce::1005__wikidata_comp__dev::p2]
> Detyens Shipyard, Inc. operates the facility with three dry docks, one floating dock, and six piers, and is the largest commercial facility on the East Coast, handling military, commercial, and cruise ship projects. [alce::1005__wikidata_comp__dev::p2]

Cited: alce::1005__wikidata_comp__dev::p0, alce::1005__wikidata_comp__dev::p2

### `605__wikidata_simple__dev`
> **The Adventures of Priscilla, Queen of the Desert**
> Lizzy Gardiner is best known for her American Express gold card dress which she wore to collect her Academy Award for Best Costume Designer at the 67th Academy Awards in 1995 for her work on "The Adventures of Priscilla, Queen of the Desert". [alce::605__wikidata_simple__dev::p0]
> Their costumes won the Academy Award for Best Costume Design at the 67th Academy Awards for "The Adventures of Priscilla, Queen of the Desert". [alce::605__wikidata_simple__dev::p1]

Cited: alce::605__wikidata_simple__dev::p0, alce::605__wikidata_simple__dev::p1

### `667__wikidata_simple__dev`
> **Betza's funny notation (also called "Betza notation")**
> Betza's funny notation, also referred to as "Betza notation", is a compact method to describe the way pieces move in chess-like board games. [alce::667__wikidata_simple__dev::p0]
> It was originally invented by the American chess master Ralph Betza. [alce::667__wikidata_simple__dev::p0]

Cited: alce::667__wikidata_simple__dev::p0

### `832__wikidata_simple__dev`
> **Hiwaga sa Bahay na Bato**
> By 1963, with the official launch of the first Philippine drama program, "Hiwaga sa Bahay na Bato", the ABS-CBN brand was officially used for the first time on the station in newspaper ads promoting the series. [alce::832__wikidata_simple__dev::p3]

Cited: alce::832__wikidata_simple__dev::p3

### `170__wikidata_comp__dev`
> **Christ Church, Oxford**
> Richard Charles Jackson is the current Bishop of Lewes in the Church of England and studied at Christ Church, Oxford, graduating with a Bachelor of Arts (BA) degree in 1983. [alce::170__wikidata_comp__dev::p34]

Cited: alce::170__wikidata_comp__dev::p34

### `66__wikitables_composition__dev`
> **Richmond Art Museum, Wayne County Historical Museum, and Joseph Moore Museum (at Earlham College)**
> The Richmond Art Museum was founded in 1898 as the Art Association of Richmond, Indiana. [alce::66__wikitables_composition__dev::p0]
> The Wayne County Historical Museum holds one of the mummies for which Richmond is known as the 'Mummy capital of Indiana'. [alce::66__wikitables_composition__dev::p7]
> The second mummy is held by Earlham College's Joseph Moore Museum. [alce::66__wikitables_composition__dev::p7]

Cited: alce::66__wikitables_composition__dev::p0, alce::66__wikitables_composition__dev::p7

### `523__wikitables_simple__dev`
> **President, Speaker, and Mr. President**
> The current President of the Legislative Council is Nelson MLC Jim Wilkinson. [alce::523__wikitables_simple__dev::p0]
> In the United States, the title 'Mr. President' is used in a number of formal instances as well: for example anyone presiding over the United States Senate is addressed as 'Mr. President.' Other uses of the title include presidents of state and local legislatures. [alce::523__wikitables_simple__dev::p33]
> In some countries the speaker of their unicameral legislatures, or of one or both houses of bicameral legislatures, the speakers have the title of president of 'the body', as in the case of Spain, where the Speaker of the Congress is the President of the Congress of Deputies and the Speaker of the Senate is the President of the Senate. [alce::523__wikitables_simple__dev::p85]

Cited: alce::523__wikitables_simple__dev::p0, alce::523__wikitables_simple__dev::p33, alce::523__wikitables_simple__dev::p85

### `271__wikidata_comp__dev`
> **Soundaryan**
> Soundaryan is an Indian music composer who composed music for 'Cheran Chozhan Pandian' (1998), a film directed by Senthamizhan. [alce::271__wikidata_comp__dev::p10, alce::271__wikidata_comp__dev::p4]
> The film 'Cheran Chozhan Pandian' (1998) had musical score by Soundaryan and was directed by Senthamizhan. [alce::271__wikidata_comp__dev::p4]

Cited: alce::271__wikidata_comp__dev::p10, alce::271__wikidata_comp__dev::p4

### `722__wikidata_simple__dev`
> **U-33 through U-36**
> Type VIIA U-boats were designed in 1933–34 as the first series of a new generation of attack U-boats, with examples including U-33 through U-36, which were built at Friedrich Krupp Germaniawerft, Kiel. [alce::722__wikidata_simple__dev::p37]

Cited: alce::722__wikidata_simple__dev::p37

### `227__wikidata_comp__dev`
> **Sony Pictures**
> The project was later made into the 2016 film "Passengers" by Sony Pictures, produced by Original Film and Company. [alce::227__wikidata_comp__dev::p2]

Cited: alce::227__wikidata_comp__dev::p2

### `727__wikidata_simple__dev`
> **Venkatachalam Ramaswamy**
> Venkatachalam Ramaswamy (V. "Ram" Ramaswamy) is the Director of the Geophysical Fluid Dynamics Laboratory of the National Oceanic and Atmospheric Administration (NOAA) Office of Oceanic and Atmospheric Research (OAR), studying climate modeling and climate change. [alce::727__wikidata_simple__dev::p46]

Cited: alce::727__wikidata_simple__dev::p46

### `92__wikitables_composition__dev`
> **Manistee Township**
> Manistee Township is a civil township of Manistee County in the U.S. state of Michigan. [alce::92__wikitables_composition__dev::p1]

Cited: alce::92__wikitables_composition__dev::p1

### `496__wikitables_simple__dev`
> **There are 41 active aircraft carriers in the world operated by thirteen navies**
> As of the present time, there are 41 active aircraft carriers in the world operated by thirteen navies. [alce::496__wikitables_simple__dev::p0]
> The United States Navy has 11 large nuclear-powered fleet carriers—carrying around 80 fighter jets each—the largest carriers in the world. [alce::496__wikitables_simple__dev::p0]
> Russia's only existing carrier is the Soviet era 'Admiral Kuznetsov' which will remain in service at least until 2030. [alce::496__wikitables_simple__dev::p8]

Cited: alce::496__wikitables_simple__dev::p0, alce::496__wikitables_simple__dev::p8

### `961__wikidata_comp__dev`
_Refused._

### `905__wikidata_simple__dev`
> **Amtrak maintains ticketing services, train operating crews, and passenger lists**
> Amtrak is responsible for providing ticketing services and train operating crews (engineers, assistant engineers, conductors, and assistant conductors). [alce::905__wikidata_simple__dev::p54]
> Following a recommendation to maintain a record of onboard passenger numbers, Amtrak now records passenger lists electronically. [alce::905__wikidata_simple__dev::p87]

Cited: alce::905__wikidata_simple__dev::p54, alce::905__wikidata_simple__dev::p87

### `204__wikidata_comp__dev`
> **College of Ripon and York St John**
> Mark Davies, the Bishop of Middleton since 2008, graduated from the College of Ripon and York St John in 1985 with a Bachelor of Arts (BA Hons) honours degree. [alce::204__wikidata_comp__dev::p16, alce::204__wikidata_comp__dev::p21]

Cited: alce::204__wikidata_comp__dev::p16, alce::204__wikidata_comp__dev::p21

### `1004__wikidata_comp__dev`
_Refused._

### `612__wikidata_simple__dev`
> **Multiple individuals, including Kotzwara (1791), Longhurst, and Hutchence**
> Kotzwara tied a ligature around the doorknob, the other end fastened around his neck, and proceeded to have sexual intercourse with Hill. After it was over, Kotzwara was dead. His is one of the first recorded deaths from erotic asphyxiation. [alce::612__wikidata_simple__dev::p0]
> According to Coutts's account in the witness box, he was masturbating whilst pulling the ligature around her neck, and when he reached orgasm he found that Longhurst was lying dead across him, with a quantity of blood produced. [alce::612__wikidata_simple__dev::p14]
> In a 1999 interview on '60 Minutes' (and in a documentary film on Channel 4), Yates claimed that Hutchence's death may have resulted from autoerotic asphyxiation. [alce::612__wikidata_simple__dev::p43]

Cited: alce::612__wikidata_simple__dev::p0, alce::612__wikidata_simple__dev::p14, alce::612__wikidata_simple__dev::p43

### `503__wikitables_simple__dev`
> **Dams with fill structure larger than 27.4 million cubic meters: The embankment project with approximately 152.8 million cubic meters, and Belle Fourche Dam with approximately 1.36 million cubic yards (approximately 1.04 million cubic meters)**
> The total volume of earth and rock used for the project is approximately 200 million cubic yards (152.8 million cu. meters) which makes it one of the largest man-made structures in the world. [alce::503__wikitables_simple__dev::p52]
> Belle Fourche Dam is described as 'a homogeneous earthfill structure containing about 1,783,000 cubic yards of material.' [alce::503__wikitables_simple__dev::p91]

Cited: alce::503__wikitables_simple__dev::p52, alce::503__wikitables_simple__dev::p91

### `18__wikitables_composition__dev`
> **Iceberg Skating Palace**
> The Iceberg Skating Palace is a 12,000-seat multi-purpose arena at Sochi Olympic Park in Sochi, Russia that hosted the figure skating and short track speed skating events at the 2014 Winter Olympics. [alce::18__wikitables_composition__dev::p21]

Cited: alce::18__wikitables_composition__dev::p21

### `533__wikitables_simple__dev`
> **Women's wrestling promotions include: World Women's Wrestling Association (WWWA), All Japan Women's Pro-Wrestling Federation, All Japan Women's Wrestling Club, Women of Wrestling (WOW), Shimmer Women Athletes, Shine Wrestling, Lucha Libre Femenil (LLF), Bellatrix Female Warriors, LCW Roses, WWE, TNA, Pro-Wrestling: EVE, and others**
> The World Women's Wrestling Association (WWWA) was a women's wrestling promotion. [alce::533__wikitables_simple__dev::p20]
> The All Japan Women's Pro-Wrestling Federation and the All Japan Women's Wrestling Club (started in 1948, which was the first women's wrestling promotion in Japan) were women's wrestling promotions. [alce::533__wikitables_simple__dev::p20]
> Women of Wrestling (WOW) is a women's professional wrestling promotion founded in 2000. [alce::533__wikitables_simple__dev::p17]
> Shimmer Women Athletes (est. 2005) in Illinois and Shine Wrestling (est. 2012) in Florida are women's wrestling promotions. [alce::533__wikitables_simple__dev::p3]
> WWE is a major women's professional wrestling promotion in the United States. [alce::533__wikitables_simple__dev::p3]
> Lucha Libre Femenil (LLF) is an all-woman promotion company started in Monterrey. [alce::533__wikitables_simple__dev::p0]
> Other independent women's wrestling promotions include Bellatrix Female Warriors and the LCW Roses. [alce::533__wikitables_simple__dev::p0]
> Pro-Wrestling: EVE is a British independent women's professional wrestling promotion founded in 2010. [alce::533__wikitables_simple__dev::p45]

Cited: alce::533__wikitables_simple__dev::p0, alce::533__wikitables_simple__dev::p17, alce::533__wikitables_simple__dev::p20, alce::533__wikitables_simple__dev::p3, alce::533__wikitables_simple__dev::p45

### `705__wikidata_simple__dev`
> **Ian Baird and others**
> Ian Baird was appointed head coach at Sutton United in October 2014. [alce::705__wikidata_simple__dev::p40]
> In May 2014, Beadle was appointed head coach at Sutton United by manager Paul Doswell. [alce::705__wikidata_simple__dev::p2]
> In July 1962 he was appointed manager of Athenian League side Sutton United. [alce::705__wikidata_simple__dev::p1]
> In 1956, Sutton United appointed a new manager who steered the club through one of its happiest periods. [alce::705__wikidata_simple__dev::p0]

Cited: alce::705__wikidata_simple__dev::p0, alce::705__wikidata_simple__dev::p1, alce::705__wikidata_simple__dev::p2, alce::705__wikidata_simple__dev::p40

### `726__wikidata_simple__dev`
> **The Adventures of Priscilla, Queen of the Desert**
> Lizzy Gardiner is best known for her American Express gold card dress which she wore to collect her Academy Award for Best Costume Designer at the 67th Academy Awards in 1995 for her work on "The Adventures of Priscilla, Queen of the Desert". [alce::726__wikidata_simple__dev::p0]
> Their costumes won the Academy Award for Best Costume Design at the 67th Academy Awards, Best Costume at the British Academy of Film and Television Arts (BAFTA), and Best Costume Design at the Australian Film Institute Awards. [alce::726__wikidata_simple__dev::p1]

Cited: alce::726__wikidata_simple__dev::p0, alce::726__wikidata_simple__dev::p1

### `302__wikidata_comp__dev`
> **Loyola University Chicago**
> Loyola University Chicago, the last remaining charter member from the Horizon League's founding in 1979, announced in April 2013 that it would leave the Horizon effective July 1 to join the Missouri Valley Conference. [alce::302__wikidata_comp__dev::p22]
> The Horizon League is a 10-school collegiate athletic conference in the National Collegiate Athletic Association (NCAA) Division I, whose members are located in and near the Midwestern United States. [alce::302__wikidata_comp__dev::p3]

Cited: alce::302__wikidata_comp__dev::p22, alce::302__wikidata_comp__dev::p3

### `400__wikidata_comp__dev`
> **Marc Forster**
> Michael Cristofer is an American playwright, filmmaker and actor who has written numerous screenplays for film. [alce::400__wikidata_comp__dev::p2]
> Michael Cristofer was hired to write the screenplay for a film adaptation, where he stuck close to the tone of the novel. [alce::400__wikidata_comp__dev::p8]
> Marc Forster is a German-born film director best known for directing films including 'Finding Neverland' and other major productions. [alce::400__wikidata_comp__dev::p95]

Cited: alce::400__wikidata_comp__dev::p2, alce::400__wikidata_comp__dev::p8, alce::400__wikidata_comp__dev::p95

### `381__wikidata_comp__dev`
> **Carl Gottlieb directed "Caveman" (1981)**
> Carl Gottlieb is an American screenwriter, actor, comedian and executive who is probably best known for co-writing the screenplay for "Jaws" and its first two sequels, as well as directing the 1981 film "Caveman". [alce::381__wikidata_comp__dev::p0]

Cited: alce::381__wikidata_comp__dev::p0

### `137__wikidata_comp__dev`
> **Allan Dwan**
> Allan Dwan directed 'Bound in Morocco', a 1918 film that Douglas Fairbanks produced and wrote. [alce::137__wikidata_comp__dev::p18]

Cited: alce::137__wikidata_comp__dev::p18

### `542__wikitables_simple__dev`
> **Multiple teams have goalkeepers that scored goals, including the Kansas City Blues, Columbus Crew, and Linfield**
> Michel Plasse, the goaltender for the Kansas City Blues, scored on an open net in a game against the Oklahoma City Blazers on February 21, 1971. [alce::542__wikitables_simple__dev::p1]
> Hesmer became the third goalkeeper in MLS history to score a goal in a 2–2 draw with Toronto FC at BMO Field on October 16, 2010, while playing for the Columbus Crew. [alce::542__wikitables_simple__dev::p9]
> A goalkeeper scored a goal for Linfield in a match against Omagh Town in 2003 when his long goal kick bounced over the opposing goalkeeper and into the net. [alce::542__wikitables_simple__dev::p91]

Cited: alce::542__wikitables_simple__dev::p1, alce::542__wikitables_simple__dev::p9, alce::542__wikitables_simple__dev::p91

### `176__wikidata_intersection__dev`
> **Bolton Wanderers F.C. competed in multiple FA Cup Finals: the 1922-23 FA Cup Final, the 1926 FA Cup Final, the 1953 FA Cup Final (Stanley Matthews Final), and the 1958 FA Cup Final**
> Bolton Wanderers won the competition, beating West Ham United 2–0 in the first final to be held at Wembley Stadium, London in the 1922–23 FA Cup. [alce::176__wikidata_intersection__dev::p63]
> The 1926 FA Cup Final was contested by Bolton Wanderers and Manchester City at Wembley, with Bolton winning by a single goal, scored by David Jack. [alce::176__wikidata_intersection__dev::p33]
> In 1953 Bolton played in one of the most famous FA Cup finals of all time – The Stanley Matthews Final of 1953, where Bolton lost the game to Blackpool 4–3 after gaining a 3–1 lead. [alce::176__wikidata_intersection__dev::p0]
> Bolton Wanderers won a major trophy in 1958, when two Lofthouse goals saw them overcome Manchester United in the FA Cup final. [alce::176__wikidata_intersection__dev::p0]

Cited: alce::176__wikidata_intersection__dev::p0, alce::176__wikidata_intersection__dev::p33, alce::176__wikidata_intersection__dev::p63

### `431__wikidata_intersection__dev`
> **Anandam**
> Anandam is a 2001 Telugu romance film, directed by Srinu Vaitla and starring Jai Akash and Rekha Vedavyas in the lead roles. [alce::431__wikidata_intersection__dev::p12]
> The music of the film was composed by Devi Sri Prasad. [alce::431__wikidata_intersection__dev::p12]

Cited: alce::431__wikidata_intersection__dev::p12

### `926__wikidata_simple__dev`
> **Multiple TV shows including The Avengers, The New Avengers, The Baron, Doctor Who, and Dramarama**
> Dennis Spooner was an English television writer and script editor, known primarily for his programmes about fictional spies and his work in children's television in the 1960s. [alce::926__wikidata_simple__dev::p0]
> He wrote for 'The Avengers' and 'The New Avengers', where he and Brian Clemens wrote the overwhelming majority of the scripts for the latter, making him the third-most prolific writer for 'The Avengers'. [alce::926__wikidata_simple__dev::p2]
> Spooner left 'Doctor Who' to help Terry Nation write the majority of the scripts for 'The Baron' in 1966. [alce::926__wikidata_simple__dev::p5]
> He was a contributor to both the Gerry Anderson and 'Doctor Who' universes in children's drama from 1964 to 1966. [alce::926__wikidata_simple__dev::p4]
> His final sale was the episode 'Flashback' for the children's supernatural anthology 'Dramarama'. [alce::926__wikidata_simple__dev::p4]

Cited: alce::926__wikidata_simple__dev::p0, alce::926__wikidata_simple__dev::p2, alce::926__wikidata_simple__dev::p4, alce::926__wikidata_simple__dev::p5

### `753__wikidata_simple__dev`
> **Henry Cow, Art Bears, Massacre, and Skeleton Crew**
> Fred Frith first came to attention as one of the founding members of the English avant-rock group Henry Cow. [alce::753__wikidata_simple__dev::p0]
> He was also a member of the groups Art Bears, Massacre, and Skeleton Crew. [alce::753__wikidata_simple__dev::p0]

Cited: alce::753__wikidata_simple__dev::p0

### `438__wikidata_intersection__dev`
_Refused._

### `146__wikidata_comp__dev`
> **Multiple victors in Argentine Grand Prix races**
> The 1955 Argentine Grand Prix was won by Juan Manuel Fangio for Mercedes. [alce::146__wikidata_comp__dev::p1]
> The 1960 Argentine Grand Prix was won by Bruce McLaren. [alce::146__wikidata_comp__dev::p8]
> The modernized Argentine Grand Prix returned with victory going to Damon Hill, who won the event again in his championship season, and Jacques Villeneuve won the race in his championship season. [alce::146__wikidata_comp__dev::p15]
> Michael Schumacher won the last running of the Argentine Grand Prix, his ninth win for Ferrari. [alce::146__wikidata_comp__dev::p15]
> Cal Crutchlow won the 2018 Argentine motorcycle Grand Prix. [alce::146__wikidata_comp__dev::p85]

Cited: alce::146__wikidata_comp__dev::p1, alce::146__wikidata_comp__dev::p15, alce::146__wikidata_comp__dev::p8, alce::146__wikidata_comp__dev::p85

### `579__wikidata_simple__dev`
> **A hill (referred to as "nose mountain")**
> Bathurst Inlet is a deep inlet located along the northern coast of the Canadian mainland, at the east end of Coronation Gulf, into which the Burnside and Western Rivers empty. [alce::579__wikidata_simple__dev::p0]
> The Inuit name for the community is 'Kingaun' (old orthography) or 'Qingaut' (new orthography), meaning 'nose mountain', which refers to a hill close to the community. [alce::579__wikidata_simple__dev::p97]

Cited: alce::579__wikidata_simple__dev::p0, alce::579__wikidata_simple__dev::p97

### `1362__wikidata_simple__dev`
> **Multiple individuals were involved in the wedding of Prince Harry and Meghan Markle, including Prince Harry, Meghan Markle, Queen Elizabeth II, Justin Welby, Thomas Markle Sr., and many others**
> The wedding of Prince Harry and Meghan Markle was held on 19 May 2018 in St George's Chapel at Windsor Castle in the United Kingdom, with Prince Harry as the groom and Meghan Markle as the bride. [alce::1362__wikidata_simple__dev::p0]
> Queen Elizabeth II conferred titles upon Prince Harry on the morning of the wedding, and Meghan Markle became Duchess of Sussex upon her marriage. [alce::1362__wikidata_simple__dev::p0]
> The Archbishop of Canterbury, Justin Welby, officiated at the wedding. [alce::1362__wikidata_simple__dev::p0]
> Meghan Markle's mother attended the wedding and accompanied her to the church, while her father, Thomas Markle Sr., did not attend due to his recent heart surgery. [alce::1362__wikidata_simple__dev::p4]
> Approximately 250 members of the British Armed Forces were involved in the wedding. [alce::1362__wikidata_simple__dev::p4]
> Notable guests included David and Victoria Beckham, Sir Elton John, James Blunt, Joss Stone, Jonny Wilkinson, James Haskell, Jessica Mulroney, Cressida Bonas, Chelsy Davy, Prince Seeiso of Lesotho, and Princess Mabereng. [alce::1362__wikidata_simple__dev::p5]
> Van Straubenzee served as an usher at the wedding. [alce::1362__wikidata_simple__dev::p54]

Cited: alce::1362__wikidata_simple__dev::p0, alce::1362__wikidata_simple__dev::p4, alce::1362__wikidata_simple__dev::p5, alce::1362__wikidata_simple__dev::p54

### `282__wikidata_intersection__dev`
> **The Great Northfield Minnesota Raid**
> In 1972, Kaufman wrote and directed 'The Great Northfield Minnesota Raid' starring Robert Duvall as Jesse James. [alce::282__wikidata_intersection__dev::p9]

Cited: alce::282__wikidata_intersection__dev::p9

### `678__wikidata_simple__dev`
> **Operas, motets, sacred works, chamber music, and instrumental compositions**
> Steffani composed six motets during his time studying in Rome. [alce::678__wikidata_simple__dev::p2]
> He published 'Psalmodia vespertina', a sacred work, as his first published composition in 1674. [alce::678__wikidata_simple__dev::p2]
> Steffani's opera overtures demonstrate his mastery of instrumental forms with a combination of Italian suavity and French influence. [alce::678__wikidata_simple__dev::p1]
> In 1709, Steffani produced two new operas: 'Enea' at Hanover and 'Tassilone' at Düsseldorf. [alce::678__wikidata_simple__dev::p33]

Cited: alce::678__wikidata_simple__dev::p1, alce::678__wikidata_simple__dev::p2, alce::678__wikidata_simple__dev::p33

### `609__wikidata_simple__dev`
> **The UN General Assembly passed several important resolutions and laws including Resolution 94 (1946), Resolution 174 (1947), the Arms Trade Treaty (2013), and resolutions on war crimes investigations and terrorism prevention**
> On December 11, 1946, The General Assembly passed Resolution 94, which called to establish a committee of legal experts to make recommendations to the UN Secretary-General on the ways the General Assembly could encourage the progressive development of international law and its codification. [alce::609__wikidata_simple__dev::p41]
> On November 21, 1947, the UN General Assembly passed Resolution 174, which provided for the creation of an 'International Law Commission' in order to promote these objectives. [alce::609__wikidata_simple__dev::p41]
> On 2 April 2013, Jeremić facilitated the General Assembly's adoption of the Arms Trade Treaty (ATT), which was aimed at regulating international conventional weapons commerce, and was passed by a vote of 154–3. [alce::609__wikidata_simple__dev::p10]
> The United Nations General Assembly endorsed a resolution calling for independent investigations to be conducted by Israel and Hamas on allegations of war crimes, which was passed by overwhelming numbers with 114 in favour and 18 against, and 44 abstentions. [alce::609__wikidata_simple__dev::p42]
> The General Assembly has passed resolutions aimed at achieving a world free of terrorism by 2045. [alce::609__wikidata_simple__dev::p5]

Cited: alce::609__wikidata_simple__dev::p10, alce::609__wikidata_simple__dev::p41, alce::609__wikidata_simple__dev::p42, alce::609__wikidata_simple__dev::p5

### `794__wikidata_simple__dev`
> **Pierre Harel, Johnny Gravel, Gerry Boulet, Michel Lamothe, and Denis Boulet**
> The band initially consisted of vocalist and lyricist Pierre Harel, guitarist Johnny Gravel, organist and singer Gerry Boulet, bassist Michel Lamothe (son of country singer Willie Lamothe) and drummer Denis Boulet (Gerry's brother). [alce::794__wikidata_simple__dev::p0]

Cited: alce::794__wikidata_simple__dev::p0

### `567__wikidata_simple__dev`
> **Members of Sentenced included Miika Tenkula, Sami Lopakka, Vesa Ranta, Lari Kylmänen, and Sami Kukkohovi**
> The original line-up consisted of Miika Tenkula (lead guitar and vocals), Sami Lopakka (guitar), Vesa Ranta (drums), and Lari Kylmänen (bass). [alce::567__wikidata_simple__dev::p0]
> Sami Kukkohovi joined the band in 1996, replacing Taneli Jarva, and stayed with Sentenced up until they disbanded in 2005. [alce::567__wikidata_simple__dev::p3]
> Miika Tenkula was the lead guitarist and the main songwriter for the band Sentenced until it disbanded, and was also the band's original vocalist from 1989 to late 1992. [alce::567__wikidata_simple__dev::p5]

Cited: alce::567__wikidata_simple__dev::p0, alce::567__wikidata_simple__dev::p3, alce::567__wikidata_simple__dev::p5

### `797__wikidata_simple__dev`
> **Coastal fortifications and towers including Wignacourt Tower, Mamo Tower, Għallis Tower, St. Mary's Battery, Dwejra Tower, St. Mark's Tower, St. Agatha's Tower, St. Mary's Tower, and Sopu Tower**
> Din l-Art Ħelwa is a non-governmental and non-profit, voluntary organisation founded in 1968, to safeguard Malta's cultural heritage and natural environment. [alce::797__wikidata_simple__dev::p0]
> Din l-Art Ħelwa has restored numerous cultural sites of historic and environmental importance, including Hospitaller coastal fortifications. [alce::797__wikidata_simple__dev::p0, alce::797__wikidata_simple__dev::p73]
> Towers and batteries restored and maintained by Din l-Art Ħelwa include Wignacourt Tower (1975–76 and 2003), Mamo Tower (1994–95), Għallis Tower (1995), St. Mary's Battery (1996–97 and 2003–04), Dwejra Tower (1997), St. Mark's Tower (1997–98), St. Agatha's Tower (1999–2001), St. Mary's Tower (2002 and 2005) and Sopu Tower (2004). [alce::797__wikidata_simple__dev::p73]
> Din l-Art Ħelwa is currently restoring St. Anthony's Battery and Xlendi Tower. [alce::797__wikidata_simple__dev::p73]

Cited: alce::797__wikidata_simple__dev::p0, alce::797__wikidata_simple__dev::p73

### `255__wikidata_intersection__dev`
> **Chelsea F.C. won multiple FA Cup Finals, including the 1970, 1997, 2000, 2007, and 2009 finals**
> Chelsea went into the match as four-time FA Cup winners, having previously won in 1970, 1997, 2000 and 2007. [alce::255__wikidata_intersection__dev::p0]
> The 1997 FA Cup Final took place on 17 May 1997 at Wembley Stadium and was won by Chelsea with a 2–0 victory over Middlesbrough. [alce::255__wikidata_intersection__dev::p13]
> Chelsea were also the last club to win the FA Cup at the old Wembley Stadium, when they beat Aston Villa in the 2000 Final. [alce::255__wikidata_intersection__dev::p15]
> Chelsea won 2–0 to win the FA Cup for the second time, the first having come in 1970. [alce::255__wikidata_intersection__dev::p1]
> Chelsea faced Liverpool in the FA Cup final and won their seventh FA Cup, largely thanks to heroics from goalkeeper Petr Čech. [alce::255__wikidata_intersection__dev::p82]

Cited: alce::255__wikidata_intersection__dev::p0, alce::255__wikidata_intersection__dev::p1, alce::255__wikidata_intersection__dev::p13, alce::255__wikidata_intersection__dev::p15, alce::255__wikidata_intersection__dev::p82

### `424__wikidata_comp__dev`
_Refused._

### `946__wikidata_simple__dev`
_Refused._

### `128__wikidata_comp__dev`
> **Evan Reilly directed episodes of TV shows whose scripts he wrote**
> Evan Reilly is an American television writer, producer and director who is best known as a long-time writer and producer on the FX series 'Rescue Me', which he worked on beginning with its second season and continuing through to its seventh and final season. [alce::128__wikidata_comp__dev::p1]
> During this time he wrote or co-wrote forty-three episodes and made his directorial-debut on the penultimate episode, 'Vows'. [alce::128__wikidata_comp__dev::p1]

Cited: alce::128__wikidata_comp__dev::p1

### `324__wikidata_intersection__dev`
> **Roger & Me**
> Roger & Me is a 1989 American film written, produced, directed by and starring Michael Moore. [alce::324__wikidata_intersection__dev::p4]
> The Big One is a 1997 documentary film written and directed by documentarian filmmaker and activist Michael Moore. [alce::324__wikidata_intersection__dev::p54]

Cited: alce::324__wikidata_intersection__dev::p4, alce::324__wikidata_intersection__dev::p54

### `51__wikitables_composition__dev`
> **Cerro Tipas**
> Cerro Tipas (also known as Cerro Cazadero or Cerro Walther Penck) is a massive complex volcano in the Andes, located in northwestern Argentina. [alce::51__wikitables_composition__dev::p52]

Cited: alce::51__wikitables_composition__dev::p52

### `625__wikidata_simple__dev`
> **Multiple films including "Housefull" (2010), "Baaghi" (2016), "Judwaa 2", "Highway", "2 States", "Heropanti", "Mujhse Shaadi Karogi", "Jeet", "Judwaa", "Har Dil Jo Pyaar Karega", "Tamasha", and "Dishoom"**
> He has produced films like "Judwaa 2", "Highway", "2 States", "Baaghi", "Heropanti", "Mujhse Shaadi Karogi", "Jeet", "Judwaa", "Har Dil Jo Pyaar Karega", "Tamasha", and "Dishoom". [alce::625__wikidata_simple__dev::p0]
> He has written and produced films including "Housefull" (2010) and "Baaghi" (2016). [alce::625__wikidata_simple__dev::p0]

Cited: alce::625__wikidata_simple__dev::p0

### `1258__wikitables_composition__dev`
> **WZCP, WLZT, and WQLX**
> WZCP is an American non-commercial FM radio station located in Chillicothe, Ohio, and operates on the assigned frequency of 89.3 MHz. [alce::1258__wikitables_composition__dev::p5]
> WLZT is a station in Chillicothe operating at 93.3 MHz with a Hot AC format. [alce::1258__wikitables_composition__dev::p3]
> WQLX (106.5 FM) is a radio station licensed to Chillicothe, Ohio, United States. [alce::1258__wikitables_composition__dev::p7]

Cited: alce::1258__wikitables_composition__dev::p3, alce::1258__wikitables_composition__dev::p5, alce::1258__wikitables_composition__dev::p7

### `203__wikidata_comp__dev`
> **Jack Brabham**
> The 1st Austrian Grand Prix was a motor race, run to Formula One rules, held on 1 September 1963 at the Zeltweg Airfield, and was won by Australian driver Jack Brabham in a Brabham BT3, finishing a massive five laps ahead of the next finisher. [alce::203__wikidata_comp__dev::p44]

Cited: alce::203__wikidata_comp__dev::p44

### `450__wikidata_intersection__dev`
> **The Eternal Derby of Bulgarian Football and the 1985 Bulgarian Cup Final**
> The Eternal Derby of Bulgarian Football is the name of the local derby football match between the two most popular and successful football clubs in Sofia and Bulgaria: PFC Levski Sofia and PFC CSKA Sofia. [alce::450__wikidata_intersection__dev::p56]
> The 1985 Bulgarian Cup Final was contested between CSKA Sofia and Levski Sofia on 19 June 1985 at Vasil Levski National Stadium in Sofia. [alce::450__wikidata_intersection__dev::p28]

Cited: alce::450__wikidata_intersection__dev::p28, alce::450__wikidata_intersection__dev::p56

### `967__wikidata_comp__dev`
_Refused._

### `180__wikidata_comp__dev`
> **Christopher Nolan and Jonathan Nolan (and others)**
> Christopher Nolan is an English film director, screenwriter, and producer who holds both British and American citizenship. [alce::180__wikidata_comp__dev::p11]
> For 'The Prestige' (2006), Nolan directed, co-wrote, and produced the film, with Jonathan Nolan helping write the script in collaboration with Christopher. [alce::180__wikidata_comp__dev::p0, alce::180__wikidata_comp__dev::p2]
> For 'Interstellar' (2014), Nolan directed, wrote, and produced the film, with the first drafts of the script written by Jonathan Nolan. [alce::180__wikidata_comp__dev::p5]
> For 'The Dark Knight' (2008), Jonathan and Christopher co-wrote the screenplay. [alce::180__wikidata_comp__dev::p2]

Cited: alce::180__wikidata_comp__dev::p0, alce::180__wikidata_comp__dev::p11, alce::180__wikidata_comp__dev::p2, alce::180__wikidata_comp__dev::p5

### `30__wikitables_composition__dev`
> **Turramurra**
> Reduplication is common in many Australian place names due to their Aboriginal origins. Some examples include Turramurra, Parramatta, Woolloomooloo. [alce::30__wikitables_composition__dev::p0]
> Western Australia is a state occupying the entire western third of Australia. [alce::30__wikitables_composition__dev::p11]

Cited: alce::30__wikitables_composition__dev::p0, alce::30__wikitables_composition__dev::p11

### `825__wikidata_simple__dev`
> **European Formula Two Championship (1977), Formula One races including the 1980 Brazilian Grand Prix and 1982 Italian Grand Prix**
> In 1977, Arnoux won the European Formula Two Championship. [alce::825__wikidata_simple__dev::p1]
> The race was won by French driver René Arnoux driving a Renault RE20. It was Arnoux's first World Championship victory. [alce::825__wikidata_simple__dev::p61]
> René Arnoux won the race. [alce::825__wikidata_simple__dev::p82]

Cited: alce::825__wikidata_simple__dev::p1, alce::825__wikidata_simple__dev::p61, alce::825__wikidata_simple__dev::p82

### `952__wikidata_comp__dev`
_Refused._

### `28__wikitables_composition__dev`
> **John Hufnagel and Wally Buono**
> John Hufnagel was hired as the head coach and general manager of the Calgary Stampeders in 2007, and in his first season, he led the Stampeders to the Grey Cup title with a 22–14 victory over the Montreal Alouettes on November 23, 2008. [alce::28__wikitables_composition__dev::p0]
> Wally Buono became the first head coach to win multiple Grey Cup championships for the Calgary Stampeders franchise. [alce::28__wikitables_composition__dev::p38]

Cited: alce::28__wikitables_composition__dev::p0, alce::28__wikitables_composition__dev::p38

### `978__wikidata_comp__dev`
> **Vishal Bhardwaj**
> Vishal Bhardwaj is an Indian film director, screenwriter, producer, music composer and playback singer. [alce::978__wikidata_comp__dev::p2]
> The film's music was composed by Vishal Bhardwaj, with lyrics by Gulzar, for the film Talvar. [alce::978__wikidata_comp__dev::p76]

Cited: alce::978__wikidata_comp__dev::p2, alce::978__wikidata_comp__dev::p76

### `677__wikidata_simple__dev`
> **The Mountaineer, The Blue Mountain Echo, The Blue Mountains Advertiser, and The Mountain Daily**
> The Mountaineer was a newspaper published in Katoomba, New South Wales which circulated throughout the Blue Mountains and Hartley districts between 1894 and 1908. [alce::677__wikidata_simple__dev::p17]
> The Blue Mountain Echo was a semi-weekly English language newspaper published in Katoomba, New South Wales, Australia, published from 1909-1939. [alce::677__wikidata_simple__dev::p2]
> The Blue Mountains Advertiser was a weekly English language newspaper published in Katoomba, New South Wales, Australia, published from 1939 to 1978. [alce::677__wikidata_simple__dev::p1]
> The Mountain Daily was an English language newspaper published in Katoomba, New South Wales, Australia between 1919 and 1920. [alce::677__wikidata_simple__dev::p8]

Cited: alce::677__wikidata_simple__dev::p1, alce::677__wikidata_simple__dev::p17, alce::677__wikidata_simple__dev::p2, alce::677__wikidata_simple__dev::p8

### `331__wikidata_comp__dev`
_Refused._

### `210__wikidata_intersection__dev`
> **Dharmatic**
> In November 2018, a new sector of the company was introduced, 'Dharmatic,' which would focus on producing digital content for online channels. [alce::210__wikidata_intersection__dev::p0]
> On 28 November 2018, Johar announced on Twitter that Dharma Productions had officially expanded into creating digital content for web channels via a new division, called 'Dharmatic'. [alce::210__wikidata_intersection__dev::p3]

Cited: alce::210__wikidata_intersection__dev::p0, alce::210__wikidata_intersection__dev::p3

### `165__wikidata_intersection__dev`
> **A.I. Artificial Intelligence**
> Following Kubrick's death in 1999, Spielberg took the various drafts and notes left by Kubrick and his writers and composed a new screenplay based on an earlier 90-page story treatment by Ian Watson written under Kubrick's supervision and according to Kubrick's specifications. In association with what remained of Kubrick's production unit, he directed the movie 'A.I. Artificial Intelligence' (2001) which was produced by Kubrick's longtime producer. [alce::165__wikidata_intersection__dev::p9]
> The film contains a posthumous production credit for Stanley Kubrick at the beginning and the brief dedication 'For Stanley Kubrick' at the end. [alce::165__wikidata_intersection__dev::p26]

Cited: alce::165__wikidata_intersection__dev::p26, alce::165__wikidata_intersection__dev::p9

### `117__wikidata_intersection__dev`
> **Rana**
> The film 'Rana' was to be directed by K. S. Ravikumar and would have featured music composed by A. R. Rahman. [alce::117__wikidata_intersection__dev::p73]

Cited: alce::117__wikidata_intersection__dev::p73

### `854__wikidata_simple__dev`
> **Military and civilian firearms, cartridges, gun mechanisms, shotguns, rifles, and pistols**
> John Moses Browning was an American firearms designer who developed many varieties of military and civilian firearms, cartridges, and gun mechanisms many of which are still in use around the world. [alce::854__wikidata_simple__dev::p0]
> Throughout his life, Browning designed a vast array of military and civilian small arms for his own company, as well as for Winchester, Colt, Remington, Savage, Stevens, and Fabrique Nationale de Herstal of Belgium. [alce::854__wikidata_simple__dev::p9]
> The company offers a wide variety of firearms including shotguns, rifles, and pistols. [alce::854__wikidata_simple__dev::p10]

Cited: alce::854__wikidata_simple__dev::p0, alce::854__wikidata_simple__dev::p10, alce::854__wikidata_simple__dev::p9

### `602__wikidata_simple__dev`
> **Refracting telescopes and instruments for observatories**
> Paul-Pierre Henry and his brother Prosper-Mathieu Henry were French opticians and astronomers who made refracting telescopes and instruments for observatories. [alce::602__wikidata_simple__dev::p2]
> They were also involved in the origin of the 'Carte du Ciel' project and were jointly awarded the first Valz Prize in 1877 for their sky charts designed to facilitate the search for minor planets. [alce::602__wikidata_simple__dev::p1, alce::602__wikidata_simple__dev::p2]

Cited: alce::602__wikidata_simple__dev::p1, alce::602__wikidata_simple__dev::p2

### `446__wikidata_intersection__dev`
> **Lost**
> "Lost" was created by Jeffrey Lieber, J. J. Abrams and Damon Lindelof, and throughout the show's run, Lindelof and Carlton Cuse served as showrunners and head writers. [alce::446__wikidata_intersection__dev::p16]
> Cuse was an executive producer and joint showrunner on "Lost" with Damon Lindelof. [alce::446__wikidata_intersection__dev::p0]

Cited: alce::446__wikidata_intersection__dev::p0, alce::446__wikidata_intersection__dev::p16

### `666__wikidata_simple__dev`
_Refused._

### `732__wikidata_simple__dev`
> **Multiple films including "Jackie", "Anthropoid", "Risen", "The Grey", "Albert Nobbs", "Killer Joe", "Disconnect", "The Collection", "Black Rock", "Biutiful", "I Love You Phillip Morris", "Good Hair", "The Details", "The Haunting of Molly Hartley", and "The Collector"**
> LD Entertainment is an independent American film studio and sales company, founded in 2006 by Mickey Liddell, which finances, produces, acquires and distributes full-length theatrical motion pictures around the world. [alce::732__wikidata_simple__dev::p2]
> LD's most recent films include "Jackie", a biopic about Jackie Kennedy starring Natalie Portman and directed by Pablo Larraín, the World War II drama "Anthropoid" starring Jamie Dornan and Cilian Murphy and "Risen", a fictional account of the Resurrection with Joseph Fiennes. [alce::732__wikidata_simple__dev::p2]
> Other films produced under the LD banner are "The Grey" with Liam Neeson and "Albert Nobbs" with Glenn Close. [alce::732__wikidata_simple__dev::p0]
> Some of the films which LD Entertainment has distributed include "Killer Joe", a dark comedy by William Friedkin and starring Matthew McConaughey; Disconnect, starring Jason Bateman and Alexander Skarsgard; the horror film "The Collection" by "Saw" writers Marcus Dunstan and Patrick Melton; and "Black Rock" starring Kate Bosworth, Lake Bell and Katie Aselton. [alce::732__wikidata_simple__dev::p0]
> Amongst the films LD Entertainment has acquired or produced are the Academy Award nominated "Biutiful", starring Javier Bardem and directed by Alejandro González Iñárritu; "I Love You Phillip Morris" starring Jim Carrey and Ewan McGregor; "Good Hair" starring Chris Rock; "The Details" starring Tobey Maguire, Elizabeth Banks, Laura Linney and Ray Liotta; as well as the genre movies, "The Haunting of Molly Hartley" and "The Collector". [alce::732__wikidata_simple__dev::p0, alce::732__wikidata_simple__dev::p1]

Cited: alce::732__wikidata_simple__dev::p0, alce::732__wikidata_simple__dev::p1, alce::732__wikidata_simple__dev::p2

### `78__wikitables_composition__dev`
> **The tallest buildings in Zagreb are the Zagreb Cathedral (tallest building in Croatia), Zagrepčanka (94.6 meters, 1st by height among office buildings), and other high-rise buildings including Sky Office Tower, Almeria Tower, Eurotower, HOTO Tower, and Zagrebtower**
> The Zagreb Cathedral on Kaptol is a Roman Catholic institution and not only the tallest building in Croatia but also the most monumental sacral building in Gothic style southeast of the Alps. [alce::78__wikitables_composition__dev::p8]
> Zagrepčanka is ranked 1st by height in Croatia among office buildings, standing 94.6 meters (310 feet) tall with 27 levels, and with a radio mast on the roof that increases the height to 109 meters (363 feet). [alce::78__wikitables_composition__dev::p3]
> Recent high-rise buildings in Zagreb include the Almeria Tower, Eurotower, HOTO Tower, Zagrebtower and one of the tallest skyscrapers Sky Office Tower. [alce::78__wikitables_composition__dev::p0]

Cited: alce::78__wikitables_composition__dev::p0, alce::78__wikitables_composition__dev::p3, alce::78__wikitables_composition__dev::p8

### `968__wikidata_comp__dev`
> **Various institutions including Cardozo School of Law, Pace University School of Law, Siena College, Alfred University, Columbia Law School, Long Island University, and St. John's University School of Law**
> One New York Supreme Court justice attended the Cardozo School of Law from 1985 to 1986 and the Pace University School of Law in 1984. [alce::968__wikidata_comp__dev::p39]
> Another Supreme Court justice attended night classes at Siena College and graduated with a B.A. in 1946. [alce::968__wikidata_comp__dev::p72]
> Karla Moskowitz, an Associate Justice of the New York Appellate Division of the Supreme Court, is a 1963 graduate of Alfred University and a 1966 graduate of Columbia Law School. [alce::968__wikidata_comp__dev::p71]
> Janet DiFiore, who served as a justice of the New York Supreme Court from 2003 to 2005, graduated from Long Island University and St. John's University School of Law. [alce::968__wikidata_comp__dev::p59]

Cited: alce::968__wikidata_comp__dev::p39, alce::968__wikidata_comp__dev::p59, alce::968__wikidata_comp__dev::p71, alce::968__wikidata_comp__dev::p72

### `787__wikidata_simple__dev`
> **Toussaint Louverture and Jean-Jacques Dessalines**
> Toussaint Louverture was the best-known leader of the Haitian Revolution and a leader of the growing resistance whose military and political acumen saved the gains of the first Black insurrection in November 1791. [alce::787__wikidata_simple__dev::p5]
> Jean-Jacques Dessalines was a leader of the Haitian Revolution and the first ruler of an independent Haiti under the 1805 constitution, and is regarded as one of the founding fathers of Haiti. [alce::787__wikidata_simple__dev::p13]
> The Haitian Revolution was led by formerly enslaved people like Georges Biassou, Toussaint Louverture, and Jean-Jacques Dessalines. [alce::787__wikidata_simple__dev::p34]

Cited: alce::787__wikidata_simple__dev::p13, alce::787__wikidata_simple__dev::p34, alce::787__wikidata_simple__dev::p5

### `512__wikitables_simple__dev`
> **The major wire services agencies are Reuters, Associated Press (AP), Agence France Press (AFP), United Press International (UPI), TASS, and Xinhua**
> In the 20th century, global news coverage was dominated by a combination of the 'Big Four' news agencies—Reuters, Associated Press, Agence France Press, and United Press International—representing the Western bloc, and the Communist agencies: TASS from the Soviet Union, and Xinhua from China. [alce::512__wikitables_simple__dev::p4]
> Studies of major world events, and analyses of all international news coverage in various newspapers, consistently found that a large majority of news items originated from the four biggest wire services. [alce::512__wikitables_simple__dev::p4]
> In early 1933 the three major news-wire services, AP, UP, and INS, announced they would no longer allow radio stations to use their stories. [alce::512__wikitables_simple__dev::p8]

Cited: alce::512__wikitables_simple__dev::p4, alce::512__wikitables_simple__dev::p8

### `845__wikidata_simple__dev`
> **Multiple competitions including Copa Libertadores, Copa Intercontinental, Copa Sudamericana, Primera División, and other domestic and international tournaments**
> Club Atlético River Plate is a professional Argentine sports club based in the Nuñez neighborhood of Buenos Aires. The football team is one of the most successful of Argentina, having won the Primera División professional title a record 36 times. [alce::845__wikidata_simple__dev::p8]
> At international level, River Plate has won 16 international titles, with 11 titles recognised by FIFA and CONMEBOL, including the Copa Libertadores, Copa Intercontinental and Copa Sudamericana. [alce::845__wikidata_simple__dev::p8]
> River Plate has also won 8 National cups. [alce::845__wikidata_simple__dev::p8]

Cited: alce::845__wikidata_simple__dev::p8

### `652__wikidata_simple__dev`
_Refused._

### `131__wikidata_intersection__dev`
> **Football League Cup**
> The 1982 Football League Cup Final was a football match between Liverpool and Tottenham Hotspur on 13 March 1982 at Wembley Stadium. [alce::131__wikidata_intersection__dev::p6]
> It was the final match of the 1981–82 Football League Cup, a football competition for the 92 teams in The Football League. [alce::131__wikidata_intersection__dev::p6]

Cited: alce::131__wikidata_intersection__dev::p6

### `399__wikidata_intersection__dev`
> **Music for Tamil and Hindi films, as well as Telugu films**
> P. Adinarayana Rao was a Telugu music director, film producer, lyricist and play writer who composed and produced music for several Tamil and Hindi movies. [alce::399__wikidata_intersection__dev::p0, alce::399__wikidata_intersection__dev::p1]
> He established himself as a well-known and full-fledged music director in the Telugu film industry with the film 'Palletoori Pilla' in 1950. [alce::399__wikidata_intersection__dev::p2]

Cited: alce::399__wikidata_intersection__dev::p0, alce::399__wikidata_intersection__dev::p1, alce::399__wikidata_intersection__dev::p2

### `372__wikidata_intersection__dev`
> **Multiple World Series victories, including 1947, 1953, 1996, and 2000**
> The 1947 World Series matched the New York Yankees against the Brooklyn Dodgers. The Yankees won the Series in seven games for their first title since, and their eleventh World Series championship in team history. [alce::372__wikidata_intersection__dev::p54]
> In 1953, the Yankees won 4–2 for their fourth straight World Series victory, matching the record set in 1936–1939, also by the Yankees. [alce::372__wikidata_intersection__dev::p17]
> In the 1996 World Series the Yankees beat the National League champion Atlanta Braves four games to two, winning four consecutive games to overcome a two-games-to-none deficit. The Yankees earned their 23rd World Series title and their first since 1978. [alce::372__wikidata_intersection__dev::p52]
> In the 2000 World Series against the cross-town Mets, the Yankees gained their third successive title. As of 2017, the 2000 Yankees are the most recent MLB team to repeat as World Series champions and the Yankees of 1998–2000 are the last team to win three consecutive World Series. [alce::372__wikidata_intersection__dev::p7]

Cited: alce::372__wikidata_intersection__dev::p17, alce::372__wikidata_intersection__dev::p52, alce::372__wikidata_intersection__dev::p54, alce::372__wikidata_intersection__dev::p7

### `96__wikitables_composition__dev`
> **Harlequins**
> Harlequins is a club that plays in London and has London origins. [alce::96__wikitables_composition__dev::p1]
> Harlequins play at The Stoop in London. [alce::96__wikitables_composition__dev::p1]

Cited: alce::96__wikitables_composition__dev::p1

### `75__wikitables_composition__dev`
> **Monroe is a city in Michigan located on the western shore of Lake Erie and serves as the county seat of Monroe County**
> Monroe is a city in the U.S. state of Michigan located on the western shore of Lake Erie. [alce::75__wikitables_composition__dev::p2]
> It is the county seat and largest city of Monroe County. [alce::75__wikitables_composition__dev::p2]

Cited: alce::75__wikitables_composition__dev::p2

### `780__wikidata_simple__dev`
> **Multiple TV shows including "Peter Gunn", "Yancy Derringer", "The Adventures of Robin Hood", "Decoy", "H.G. Wells: The Invisible Man", "Mr. Lucky", "The Adventures of Sir Lancelot", "Four Star Playhouse", "The Buccaneers", "Colonel March of Scotland Yard", "The Stu Erwin Show", "My Little Margie", and "Biography"**
> Official became an early syndicator of theatrical cartoons for television, during the late 1950s and early 1960s. It also syndicated live action television series such as "Peter Gunn", "Yancy Derringer", "The Adventures of Robin Hood", "Decoy", "H.G. Wells: The Invisible Man", "Mr. Lucky", "The Adventures of Sir Lancelot, Four Star Playhouse, The Buccaneers, Colonel March of Scotland Yard," "The Stu Erwin Show", "My Little Margie" and the original "Biography" during this period. [alce::780__wikidata_simple__dev::p7]

Cited: alce::780__wikidata_simple__dev::p7

### `178__wikidata_intersection__dev`
> **El Norte**
> El Norte is a 1983 British-American independent drama film, directed by Gregory Nava. [alce::178__wikidata_intersection__dev::p37]
> The screenplay was written by Gregory Nava and Anna Thomas, based on Nava's story. [alce::178__wikidata_intersection__dev::p37]

Cited: alce::178__wikidata_intersection__dev::p37

### `90__wikitables_composition__dev`
> **Since the 1999 season**
> Kirk Ferentz is the head football coach at the University of Iowa, a position he has held since the 1999 season. [alce::90__wikitables_composition__dev::p4]
> On December 2, 1998, Ferentz was hired as Iowa's 26th head football coach to replace the retiring Hayden Fry. [alce::90__wikitables_composition__dev::p15]

Cited: alce::90__wikitables_composition__dev::p15, alce::90__wikitables_composition__dev::p4

### `115__wikidata_comp__dev`
_Refused._

### `837__wikidata_simple__dev`
> **A group of (mainly French) mathematicians**
> Nicolas Bourbaki was the collective pseudonym of a group of (mainly French) mathematicians. [alce::837__wikidata_simple__dev::p2]
> Their aim was to reformulate mathematics on an extremely abstract and formal but self-contained basis in a series of books beginning in 1935. [alce::837__wikidata_simple__dev::p2]
> A group of 20th-century French mathematicians published many works under the pseudonym Nicolas Bourbaki. [alce::837__wikidata_simple__dev::p6]

Cited: alce::837__wikidata_simple__dev::p2, alce::837__wikidata_simple__dev::p6

### `314__wikidata_comp__dev`
> **FIAT, Kiwi, and Alstom**
> Bertone has styled cars for Abarth, Alfa Romeo, Aston Martin, Citroën, Ferrari, FIAT, Iso, Lancia, Lamborghini, Mercedes Benz, Opel and Volvo, among others. [alce::314__wikidata_comp__dev::p0]
> In the late 1980s, Bertone styled the K20 motorcycle helmet for Swiss bicycle and motorcycle helmet manufacturer Kiwi. [alce::314__wikidata_comp__dev::p0]
> Its most recent projects are the Frecciarossa 1000 Trenitalia and the regional train 'Jazz' produced by Alstom; both will go into service in 2015. [alce::314__wikidata_comp__dev::p2]

Cited: alce::314__wikidata_comp__dev::p0, alce::314__wikidata_comp__dev::p2

### `296__wikidata_comp__dev`
> **University College, Oxford**
> Geoffrey Francis Allen was the third Bishop of Derby and was educated at Dulwich College and University College, Oxford. [alce::296__wikidata_comp__dev::p2, alce::296__wikidata_comp__dev::p70]

Cited: alce::296__wikidata_comp__dev::p2, alce::296__wikidata_comp__dev::p70

### `869__wikidata_simple__dev`
_Refused._

### `848__wikidata_simple__dev`
> **Jim Bentley**
> Jim Bentley James Graham Bentley (born 11 June 1976) is an English former professional footballer, currently manager of League Two club Morecambe. [alce::848__wikidata_simple__dev::p42]
> On 13 May 2011, Bentley was appointed the player-manager of Morecambe on a two-year contract, but since then he has concentrated on the managerial role and has not played a competitive match since taking on that post. [alce::848__wikidata_simple__dev::p42]

Cited: alce::848__wikidata_simple__dev::p42

### `441__wikidata_intersection__dev`
> **FA Community Shield, Full Members' Cup, Premier League Asia Trophy, and friendly matches**
> The 2018 FA Community Shield was contested by Manchester City and Chelsea at Wembley Stadium in London on 5 August 2018. [alce::441__wikidata_intersection__dev::p2]
> The two sides faced each other in the Community Shield once previously, in 2012, a match won 3–2 by Manchester City. [alce::441__wikidata_intersection__dev::p4]
> The 1986 Full Members' Cup final was a football match which took place at Wembley Stadium on 23 March 1986, featuring both Chelsea and Manchester City. [alce::441__wikidata_intersection__dev::p3]
> Chelsea and Manchester City are among the most regular participants in the Premier League Asia Trophy, having each contested the tournament on two occasions. [alce::441__wikidata_intersection__dev::p47]
> Chelsea met Manchester City in two friendly matches during a post-season trip to the United States, with matches at Busch Stadium in St. Louis and Yankee Stadium in New York City. [alce::441__wikidata_intersection__dev::p17]

Cited: alce::441__wikidata_intersection__dev::p17, alce::441__wikidata_intersection__dev::p2, alce::441__wikidata_intersection__dev::p3, alce::441__wikidata_intersection__dev::p4, alce::441__wikidata_intersection__dev::p47

### `937__wikidata_simple__dev`
> **Country houses and public buildings**
> William Adam was a Scottish architect who designed and built numerous country houses and public buildings. [alce::937__wikidata_simple__dev::p0]
> Among his best known works are Hopetoun House near Edinburgh, and Duff House in Banff. [alce::937__wikidata_simple__dev::p0]

Cited: alce::937__wikidata_simple__dev::p0

### `173__wikidata_comp__dev`
> **C. Ashwini Dutt**
> In 2005, the film "Balu ABCDEFG", directed by A. Karunakaran was released. This film was produced by C. Ashwini Dutt under Vyjayanthi Movies banner. [alce::173__wikidata_comp__dev::p56]

Cited: alce::173__wikidata_comp__dev::p56

### `680__wikidata_simple__dev`
> **North of Blue**
> North of Blue is a 2018 American animated feature film directed, produced and animated by Joanna Priestley with a score by Jamie Haggerty. [alce::680__wikidata_simple__dev::p3]

Cited: alce::680__wikidata_simple__dev::p3

### `836__wikidata_simple__dev`
_Refused._

### `509__wikitables_simple__dev`
> **Examples of existing restaurant chains include fast food chains like McDonald's and Burger King, sit-down restaurant chains like Olive Garden and Buffalo Wild Wings, barbecue chains like Sonny's Real Pit BBQ and Dickey's Barbecue Pit, and international chains operating in various countries.**
> A restaurant chain is a set of related restaurants in many different locations that are either under shared corporate ownership (e.g., McDonald's in the U.S.) or franchising agreements. [alce::509__wikitables_simple__dev::p0]
> Fast food restaurants are the most common, but sit-down restaurant chains (such as Timber Lodge Steakhouse, Buffalo Wild Wings, Outback Steakhouse, T.G.I. Friday's, Legal Sea Foods, Ruby Tuesday and Olive Garden) also exist. [alce::509__wikitables_simple__dev::p0]
> In the U.S., some restaurant chains exist, such as Sonny's Real Pit BBQ, which is a franchise that in 2010 was the largest barbecue restaurant chain in the U.S. with over 130 stores, Smokey Bones, with over 70 stores in 2010, and Rib Crib, with 41 stores in 2008. [alce::509__wikitables_simple__dev::p2]
> International foreign-owned restaurant chains currently operating include A&W, Burger King, Baskin Robbins, Cold Stone Creamery, Johnny Rocket's, and Kenny Rogers Roasters, among others. [alce::509__wikitables_simple__dev::p4]

Cited: alce::509__wikitables_simple__dev::p0, alce::509__wikitables_simple__dev::p2, alce::509__wikitables_simple__dev::p4

### `499__wikitables_simple__dev`
> **Notable discovered galaxy clusters include CL J1001+0220, SPT-CL J0546-5345, and SPT-CL J2106-5844**
> CL J1001+0220 is, as of 2016, the most distant known galaxy cluster, discovered in 2016 by the Chandra X-ray Observatory in conjunction with the ESO's UltraVISTA telescope and the Atacama Large Millimeter Array, with a redshift of z=2.506 and a distance of 11.1 billion light-years from Earth. [alce::499__wikitables_simple__dev::p9]
> Notable galaxy clusters in the distant, high-redshift Universe include SPT-CL J0546-5345 and SPT-CL J2106-5844, which are the most massive galaxy clusters found in the early Universe. [alce::499__wikitables_simple__dev::p2]

Cited: alce::499__wikitables_simple__dev::p2, alce::499__wikitables_simple__dev::p9

### `89__wikitables_composition__dev`
> **Multiple museums are located in Florence, Tuscany, including the National Archaeological Museum, Uffizi Gallery, Palatina Gallery, Bargello, San Marco Museum, Academy, Buonarroti's House, Bardini, Horne, Stibbert, Romano, Corsini, Gallery of Modern Art, Museo dell'Opera del Duomo, Museum of Silverware, and Museum of Precious Stones.**
> The National Archaeological Museum of Florence is an archaeological museum in Florence, Italy, located at 1 piazza Santissima Annunziata, in the Palazzo della Crocetta. [alce::89__wikitables_composition__dev::p1]
> The Uffizi Gallery is a prominent art museum located adjacent to the Piazza della Signoria in the Historic Centre of Florence in the region of Tuscany, Italy. [alce::89__wikitables_composition__dev::p6]
> Several museums are gathered in the town of Florence: the Uffizi Gallery, the Palatina gallery, the Bargello, the museum of San Marco, the Academy, Buonarroti's house, the Bardini, Horne, Stibbert, Romano, Corsini, The Gallery of Modern Art, the Museo dell'Opera del Duomo, the museum of Silverware and the museum of Precious Stones. [alce::89__wikitables_composition__dev::p0]

Cited: alce::89__wikitables_composition__dev::p0, alce::89__wikitables_composition__dev::p1, alce::89__wikitables_composition__dev::p6

### `528__wikitables_simple__dev`
> **Robert Treat Paine, Jr.**
> Robert Treat Paine, Jr. (October 28, 1835-August 11, 1910) was a Boston lawyer, philanthropist and social reformer and great grandson of the signer of the Declaration of Independence. [alce::528__wikitables_simple__dev::p74]
> He is most widely known for his work as chairman of the building committee of Boston's Trinity Church in Copley Square, for his leadership of 19th century Boston philanthropists, and for his experiments in building housing for low-and middle-income workers. [alce::528__wikitables_simple__dev::p74]

Cited: alce::528__wikitables_simple__dev::p74

### `754__wikidata_simple__dev`
> **UEFA club competitions (Champions League, UEFA Cup, Europa League, and Cup Winners' Cup), Eliteserien, Norwegian Cup, and Tippeligaen**
> Molde FK is a Norwegian professional football club that currently plays in the Eliteserien, the Norwegian top division. [alce::754__wikidata_simple__dev::p4]
> The team has participated in 15 seasons of Union of European Football Associations (UEFA) club competitions, including 4 seasons in the Champions League, 13 seasons in the UEFA Cup and Europa League, and one season in the Cup Winners' Cup. [alce::754__wikidata_simple__dev::p2]
> Molde are three-time league champions and four-time Norwegian Cup winners. [alce::754__wikidata_simple__dev::p4]
> In specific seasons, Molde competed in Tippeligaen, the Norwegian Cup, and the UEFA Cup. [alce::754__wikidata_simple__dev::p14, alce::754__wikidata_simple__dev::p3]

Cited: alce::754__wikidata_simple__dev::p14, alce::754__wikidata_simple__dev::p2, alce::754__wikidata_simple__dev::p3, alce::754__wikidata_simple__dev::p4

### `85__wikitables_composition__dev`
> **Atrauli and Barauli**
> Atrauli Assembly constituency is one of the 403 constituencies of the Uttar Pradesh Legislative Assembly, India. It is a part of the Aligarh district and one of the five assembly constituencies in the Aligarh (Lok Sabha constituency). [alce::85__wikitables_composition__dev::p0]
> Barauli Assembly constituency is one of the 403 constituencies of the Uttar Pradesh Legislative Assembly, India. It is a part of the Aligarh district and one of the five assembly constituencies in the Aligarh (Lok Sabha constituency). [alce::85__wikitables_composition__dev::p15]

Cited: alce::85__wikitables_composition__dev::p0, alce::85__wikitables_composition__dev::p15

### `355__wikidata_intersection__dev`
> **1962 VFL Grand Final**
> The 1962 VFL Grand Final was an Australian rules football game contested between the Essendon Football Club and Carlton Football Club, held at the Melbourne Cricket Ground in Melbourne on 29 September 1962. [alce::355__wikidata_intersection__dev::p8]
> It was the 66th annual Grand Final of the Victorian Football League, staged to determine the premiers for the 1962 VFL season. [alce::355__wikidata_intersection__dev::p8]

Cited: alce::355__wikidata_intersection__dev::p8

### `1101__wikidata_intersection__dev`
> **Super Bowl XXI, Super Bowl XLII, and Super Bowl XLVI**
> The Giants went on to play the Denver Broncos in Super Bowl XXI in front of 101,063 fans at the Rose Bowl. [alce::1101__wikidata_intersection__dev::p56]
> The New York Giants were headed to Super Bowl XLII to face the 2007 AFC Champions New England Patriots who were undefeated at 18–0. [alce::1101__wikidata_intersection__dev::p8]
> The Giants would return to the Super Bowl in 2007 and again in 2011 defeating the New England Patriots on both occasions. [alce::1101__wikidata_intersection__dev::p2]

Cited: alce::1101__wikidata_intersection__dev::p2, alce::1101__wikidata_intersection__dev::p56, alce::1101__wikidata_intersection__dev::p8

### `706__wikidata_simple__dev`
> **Buildings designed by George Oakley Totten, Jr. include mansions on Dupont, Sheridan, and Kalorama circles and along 16th Street, N.W., near Meridian Hill, as well as a stone row house built in 1907 on the north side of R Street between Sheridan Circle and 22nd Street.**
> The mansions he designed were located primarily on or near Dupont, Sheridan (including Embassy Row), and Kalorama circles and along 16th Street, N.W., near Meridian Hill. [alce::706__wikidata_simple__dev::p0]
> A stone row house was built in 1907 to a design by George Oakley Totten, Jr., located on the north side of R Street, between Sheridan Circle and 22nd Street. [alce::706__wikidata_simple__dev::p69]
> Most of these buildings now serve as embassies, chanceries, or offices for national or international organizations. [alce::706__wikidata_simple__dev::p0]

Cited: alce::706__wikidata_simple__dev::p0, alce::706__wikidata_simple__dev::p69

### `241__wikidata_comp__dev`
> **Geelong Church of England Grammar School, Trinity College at the University of Melbourne, University of Durham**
> Reginald Stephen was the Bishop of Newcastle (New South Wales) from 1919 until his retirement in 1928 and was educated at Geelong Church of England Grammar School and entered Trinity College, at the University of Melbourne in 1878. [alce::241__wikidata_comp__dev::p50]
> Geoff Miller, who served as Dean of Newcastle (a related position in the Newcastle Cathedral), studied at the University of Durham, graduating with a Bachelor of Education. [alce::241__wikidata_comp__dev::p39]

Cited: alce::241__wikidata_comp__dev::p39, alce::241__wikidata_comp__dev::p50

### `1363__wikidata_simple__dev`
> **Cananéia-Iguape-Peruíbe Environmental Protection Area**
> Cananéia is the southernmost city in the state of São Paulo, Brazil, near to where the Tordesilhas Line passed. [alce::1363__wikidata_simple__dev::p0]
> The Cananéia-Iguape-Peruíbe Environmental Protection Area (APA) is a protected area in the State of São Paulo, Brazil that covers parts of the municipalities of Cananéia and other nearby municipalities. [alce::1363__wikidata_simple__dev::p2]

Cited: alce::1363__wikidata_simple__dev::p0, alce::1363__wikidata_simple__dev::p2

### `371__wikidata_comp__dev`
> **School of the Museum of Fine Arts, Boston**
> Edmund C. Tarbell was a member of the Ten American Painters. [alce::371__wikidata_comp__dev::p30]
> In 1879, he entered the School of the Museum of Fine Arts, Boston, studying under Otto Grundmann. [alce::371__wikidata_comp__dev::p4]

Cited: alce::371__wikidata_comp__dev::p30, alce::371__wikidata_comp__dev::p4

### `969__wikidata_comp__dev`
> **Mayo College, Imperial College London, Yale University, and Princeton University**
> Mohan did his schooling from Mayo College, a boarding school in Rajasthan, followed by BSc from Imperial College London in 1969; BA in Economics, Yale University 1971, MA in Economics, 1974 and PhD 1977 from Princeton University. [alce::969__wikidata_comp__dev::p3]
> He will shortly be taking over as India's Executive Director at the International Monetary Fund, Washington DC, USA. [alce::969__wikidata_comp__dev::p3]

Cited: alce::969__wikidata_comp__dev::p3

### `858__wikidata_simple__dev`
> **Bikol languages (Coastal Bikol and Inland Bikol)**
> Languages spoken in Camarines Sur are the Coastal Bikol (especially Central Bikol) and Inland Bikol group of languages. [alce::858__wikidata_simple__dev::p1]
> The Inland Bikol group includes Albay Bikol group and Rinconada Bikol, while Coastal Bikol consists of dialects such as Coastal Bikol-Partido and Coastal Bikol-Central. [alce::858__wikidata_simple__dev::p1]

Cited: alce::858__wikidata_simple__dev::p1

### `1255__wikitables_composition__dev`
> **Constantine XI**
> Constantine XI died fighting at the gates of Constantinople during the Ottoman siege. [alce::1255__wikitables_composition__dev::p31]
> Emperor Constantine was killed during the capture of Constantinople in 1453, as recorded by George Sphrantzes who wrote: 'in this capture my late master and emperor, Lord Constantine, was killed.' [alce::1255__wikitables_composition__dev::p38]
> Constantine died the day the city fell, 29 May 1453, while leading the defence of the city and taking an active part in the fighting alongside his troops. [alce::1255__wikitables_composition__dev::p89]

Cited: alce::1255__wikitables_composition__dev::p31, alce::1255__wikitables_composition__dev::p38, alce::1255__wikitables_composition__dev::p89

### `681__wikidata_simple__dev`
> **Hopman Cup**
> On 6 January 2007, Tursunov won the Hopman Cup in Perth, Australia, while representing Russia alongside Nadia Petrova. [alce::681__wikidata_simple__dev::p14]

Cited: alce::681__wikidata_simple__dev::p14

### `32__wikitables_composition__dev`
> **Nightclub fires in the United States occurred in Boston, Massachusetts (Cocoanut Grove, 1942), West Warwick, Rhode Island (The Station, 2003), and Southgate, Kentucky (Beverly Hills Supper Club, 1977)**
> The Cocoanut Grove was a premier nightclub during the post-Prohibition 1930s and 1940s in Boston, Massachusetts. On November 28, 1942, it was the scene of the deadliest nightclub fire in history, killing 492 people. [alce::32__wikitables_composition__dev::p5]
> The 2003 Station nightclub fire occurred in West Warwick, Rhode Island, in the United States. [alce::32__wikitables_composition__dev::p43]
> The Beverly Hills Supper Club fire in Southgate, Kentucky, is the third deadliest nightclub fire in U.S. history. It occurred on the night of May 28, 1977. [alce::32__wikitables_composition__dev::p13]

Cited: alce::32__wikitables_composition__dev::p13, alce::32__wikitables_composition__dev::p43, alce::32__wikitables_composition__dev::p5

### `352__wikidata_intersection__dev`
> **Multiple motion pictures were scripted by Craig Pearce and Baz Luhrmann: "Strictly Ballroom" (1992), "Romeo + Juliet" (1996), "Moulin Rouge!" (2001), and "The Great Gatsby" (2013)**
> Pearce co-wrote the play "Strictly Ballroom" and the screenplay of the 1992 movie adaptation with Baz Luhrmann. [alce::352__wikidata_intersection__dev::p0]
> He co-wrote the screenplay for the 1996 film "Romeo + Juliet," the 2001 film "Moulin Rouge!", and the 2013 film "The Great Gatsby"; all with Luhrmann. [alce::352__wikidata_intersection__dev::p0]

Cited: alce::352__wikidata_intersection__dev::p0

### `786__wikidata_simple__dev`
> **Matt Olson**
> Matt Olson is an American professional baseball first baseman and right fielder for the Oakland Athletics of Major League Baseball (MLB). [alce::786__wikidata_simple__dev::p11]
> He was drafted by the Oakland Athletics in the first round of the 2012 Major League Baseball draft. [alce::786__wikidata_simple__dev::p11]

Cited: alce::786__wikidata_simple__dev::p11

### `47__wikitables_composition__dev`
> **Balıkesir**
> Balıkesir is a city and the capital city of Balıkesir Province. [alce::47__wikitables_composition__dev::p2]
> Balıkesir is in the Marmara region of Turkey and has a population of 331,788 inhabitants. [alce::47__wikitables_composition__dev::p2]

Cited: alce::47__wikitables_composition__dev::p2

### `817__wikidata_simple__dev`
> **HMS Defender (or other D-class destroyer names like HMS Decoy, HMS Desperate, etc.)**
> The D class as they were known from 1913 was a fairly homogeneous group of torpedo boat destroyers (TBDs) built for the Royal Navy in the mid-1890s. [alce::817__wikidata_simple__dev::p0]
> All ten D-class destroyers had been built by Thornycroft, but 'Ariel' was lost before their renaming as 'D' class, leaving nine surviving vessels that were retrospectively classified by the Admiralty as the 'D' class. [alce::817__wikidata_simple__dev::p0, alce::817__wikidata_simple__dev::p69]

Cited: alce::817__wikidata_simple__dev::p0, alce::817__wikidata_simple__dev::p69

### `646__wikidata_simple__dev`
> **Neiden Chapel (a church and cemetery in Neiden)**
> Architect Karl Norum was very keen on old Norwegian stave churches, and he created a dragestil building that would be an expression of Norwegian culture and national cohesion in a border area. [alce::646__wikidata_simple__dev::p7]
> Karl Norum was the designer of a church and a cemetery built in Neiden, with the chapel being consecrated on 13 July 1902. [alce::646__wikidata_simple__dev::p7]

Cited: alce::646__wikidata_simple__dev::p7

### `702__wikidata_simple__dev`
> **America's Cup**
> Luna Rossa Challenge is an Italian sailboat racing syndicate first created to compete for the 2000 America's Cup. [alce::702__wikidata_simple__dev::p0]
> The team has won the Louis Vuitton Cup once, in 2000, and therefore was the Challenger for the final America's Cup race against the defending champion team, losing to Team New Zealand. [alce::702__wikidata_simple__dev::p0]
> Luna Rossa participated in multiple competitions including the 2007 Louis Vuitton Cup, the 2013 Louis Vuitton Cup, and the 2017 Louis Vuitton Cup. [alce::702__wikidata_simple__dev::p2, alce::702__wikidata_simple__dev::p4, alce::702__wikidata_simple__dev::p5]

Cited: alce::702__wikidata_simple__dev::p0, alce::702__wikidata_simple__dev::p2, alce::702__wikidata_simple__dev::p4, alce::702__wikidata_simple__dev::p5

### `384__wikidata_intersection__dev`
_Refused._

### `158__wikidata_intersection__dev`
> **2016 FA Community Shield**
> The 2016 FA Community Shield was an annual English football match played between the winners of the previous season's Premier League and FA Cup, contested by 2015–16 FA Cup winners Manchester United and Leicester City, champions of the 2015–16 Premier League. [alce::158__wikidata_intersection__dev::p1]
> Manchester United won the match 2–1 with goals from Jesse Lingard and Zlatan Ibrahimović. [alce::158__wikidata_intersection__dev::p1]
> Additionally, the 1962–63 FA Cup final was a football match played on 25 May 1963 at Wembley between Manchester United and Leicester City, with United winning 3–1. [alce::158__wikidata_intersection__dev::p23]

Cited: alce::158__wikidata_intersection__dev::p1, alce::158__wikidata_intersection__dev::p23

### `453__wikidata_intersection__dev`
> **UEFA Europa League**
> Manchester United won the Europa League competition after defeating AFC Ajax 2–0 in the final, giving them their first win of the competition. [alce::453__wikidata_intersection__dev::p7]
> United started their European campaign for 2016–17 in the Europa League for the first time since 1995–96. [alce::453__wikidata_intersection__dev::p7]

Cited: alce::453__wikidata_intersection__dev::p7

### `455__wikidata_intersection__dev`
> **Assault on Precinct 13**
> John Carpenter wrote, directed, and scored 'Assault on Precinct 13', also editing the film using the pseudonym 'John T. Chance'. [alce::455__wikidata_intersection__dev::p78]
> Carpenter is notable for having composed or co-composed most of his films' music, with examples including 'Assault on Precinct 13', 'The Fog', and 'Halloween'. [alce::455__wikidata_intersection__dev::p0, alce::455__wikidata_intersection__dev::p88]

Cited: alce::455__wikidata_intersection__dev::p0, alce::455__wikidata_intersection__dev::p78, alce::455__wikidata_intersection__dev::p88

### `871__wikidata_simple__dev`
> **Multiple players were drafted by the Atlanta Thrashers, including Patrik Štefan (1st overall, 1999), Dany Heatley (2nd overall, 2000), Daultan Leveille (29th overall, 2008), Zach Bogosian (3rd overall), and Riley Holzapfel (43rd overall, 2006)**
> Patrik Štefan was drafted 1st overall by the Atlanta Thrashers in the 1999 NHL Entry Draft. [alce::871__wikidata_simple__dev::p4]
> Dany Heatley was drafted second overall by the Atlanta Thrashers in the 2000 NHL Entry Draft. [alce::871__wikidata_simple__dev::p45]
> Daultan Leveille was drafted by the Atlanta Thrashers in the first round, 29th overall, in the 2008 NHL Entry Draft. [alce::871__wikidata_simple__dev::p87]
> Zach Bogosian was drafted third overall by the Atlanta Thrashers. [alce::871__wikidata_simple__dev::p39]
> Riley Holzapfel was drafted by the Atlanta Thrashers at the 2006 NHL Entry Draft, chosen 43rd overall. [alce::871__wikidata_simple__dev::p85]

Cited: alce::871__wikidata_simple__dev::p39, alce::871__wikidata_simple__dev::p4, alce::871__wikidata_simple__dev::p45, alce::871__wikidata_simple__dev::p85, alce::871__wikidata_simple__dev::p87

### `297__wikidata_intersection__dev`
> **Drag Me to Hell**
> Drag Me to Hell is a 2009 American supernatural horror film co-written and directed by Sam Raimi. [alce::297__wikidata_intersection__dev::p1]

Cited: alce::297__wikidata_intersection__dev::p1

### `882__wikidata_simple__dev`
> **Toby Howarth and Nick Baines**
> Nick Baines was the last diocesan Bishop of Bradford, serving from 21 May 2011 until 20 April 2014. [alce::882__wikidata_simple__dev::p0]
> Toby Howarth was announced on 26 August 2014 to become the first area bishop of Bradford in the newly created suffragan see within the Diocese of Leeds. [alce::882__wikidata_simple__dev::p2, alce::882__wikidata_simple__dev::p38]

Cited: alce::882__wikidata_simple__dev::p0, alce::882__wikidata_simple__dev::p2, alce::882__wikidata_simple__dev::p38

### `406__wikidata_comp__dev`
_Refused._

### `507__wikitables_simple__dev`
> **Pharaoh was a monarch of ancient Egypt**
> Pharaoh is the common title of the monarchs of ancient Egypt from the First Dynasty (c. 3150 BCE) until the annexation of Egypt by the Roman Empire in 30 BCE. [alce::507__wikitables_simple__dev::p1]
> In Latter-day Saint theology, Pharaoh is the proper name of the first king of Egypt, as found in the Book of Abraham in the Pearl of Great Price. [alce::507__wikitables_simple__dev::p0]

Cited: alce::507__wikitables_simple__dev::p0, alce::507__wikitables_simple__dev::p1

### `669__wikidata_simple__dev`
> **George L. Little was the costume designer for multiple movies including "The Hurt Locker", "Zero Dark Thirty", "Behind Enemy Lines", "Flight of the Phoenix", "The Omen", "The Crazies", "Warm Bodies", "Transcendence", "The Fantastic Four", and many others.**
> He was best known for his work on Kathryn Bigelow's acclaimed war films, 'The Hurt Locker' and 'Zero Dark Thirty'. [alce::669__wikidata_simple__dev::p0]
> He was costume designer on 'The Prince and the Surfer', 'Things You Can Tell Just by Looking at Her', 'Behind Enemy Lines', 'Flight of the Phoenix' and 'The Omen'. [alce::669__wikidata_simple__dev::p1]
> Other films for which Little was costume designer include 'The Crazies', 'Warm Bodies', 'Transcendence' and 'The Fantastic Four'. [alce::669__wikidata_simple__dev::p3]

Cited: alce::669__wikidata_simple__dev::p0, alce::669__wikidata_simple__dev::p1, alce::669__wikidata_simple__dev::p3

### `844__wikidata_simple__dev`
> **Queens of the Stone Age**
> Josh Homme is the founder and only continuous member of the rock band Queens of the Stone Age, in which he sings, plays guitar, as well as occasionally playing piano, drums, and bass. [alce::844__wikidata_simple__dev::p0]
> He was formerly a guitarist and founder of the stoner rock band Kyuss and co-founded Eagles of Death Metal. [alce::844__wikidata_simple__dev::p0]

Cited: alce::844__wikidata_simple__dev::p0

### `50__wikitables_composition__dev`
> **Hickory Museum of Art and Hickory Aviation Museum**
> The Hickory Museum of Art (HMA) is an art museum in downtown Hickory, North Carolina that holds exhibitions, events, and public educational programs based on a permanent collection of 19th through 21st century American art. [alce::50__wikitables_composition__dev::p2]
> The Sabre Society of North Carolina/Hickory Aviation Museum is a volunteer aviation historical society located at Hickory Regional Airport in Hickory, North Carolina. [alce::50__wikitables_composition__dev::p24]

Cited: alce::50__wikitables_composition__dev::p2, alce::50__wikitables_composition__dev::p24

### `469__wikitables_simple__dev`
> **Gregory Minor, Richard Hubbard, Dale Bridenbaugh, George Galatis, Richard Levernier, and Rainer Moormann**
> In 1976 Gregory Minor, Richard Hubbard, and Dale Bridenbaugh "blew the whistle" on safety problems at nuclear power plants in the United States. [alce::469__wikitables_simple__dev::p0]
> George Galatis was a senior nuclear engineer who reported safety problems at the Millstone 1 Nuclear Power Plant, relating to reactor refueling procedures, in 1995. [alce::469__wikitables_simple__dev::p0]
> Richard Levernier is an American nuclear whistleblower who worked for 23 years as a nuclear security professional and identified security problems at U.S. nuclear facilities. [alce::469__wikitables_simple__dev::p6]
> Rainer Moormann is a German chemist and nuclear whistleblower who published a critical paper on the safety of pebble bed reactors in 2008. [alce::469__wikitables_simple__dev::p31]

Cited: alce::469__wikitables_simple__dev::p0, alce::469__wikitables_simple__dev::p31, alce::469__wikitables_simple__dev::p6

### `139__wikidata_comp__dev`
_Refused._

### `200__wikidata_comp__dev`
> **David Cronenberg**
> Charles Edward Pogue is best known for writing the screenplays of "The Hound of the Baskervilles" (1983), "Psycho III" (1986), "The Fly" (1986) and "Dragonheart" (1996). [alce::200__wikidata_comp__dev::p1]
> His most well-known work to date is probably the acclaimed 1986 remake of "The Fly"; he provided the initial drafts, though his work was heavily rewritten by David Cronenberg, the film's director. [alce::200__wikidata_comp__dev::p0]

Cited: alce::200__wikidata_comp__dev::p0, alce::200__wikidata_comp__dev::p1

### `478__wikitables_simple__dev`
_Refused._

### `943__wikidata_simple__dev`
> **Fubuki, Ayanami, and Uranami were ships of the Fubuki-class destroyer**
> The Fubuki-class destroyer were a class of twenty-four destroyers of the Imperial Japanese Navy. [alce::943__wikidata_simple__dev::p1]
> Japanese destroyer Fubuki (1927) was a Fubuki-class destroyer built at the Maizuru Naval Arsenal. [alce::943__wikidata_simple__dev::p2]
> Japanese destroyer Ayanami (1929) was a Fubuki-class destroyer, built at the Fujinagata Shipyards in Osaka. [alce::943__wikidata_simple__dev::p19]
> Japanese destroyer Uranami (1928) was a Fubuki-class destroyer, built at the Uraga Dock Company. [alce::943__wikidata_simple__dev::p29]

Cited: alce::943__wikidata_simple__dev::p1, alce::943__wikidata_simple__dev::p19, alce::943__wikidata_simple__dev::p2, alce::943__wikidata_simple__dev::p29

### `199__wikidata_comp__dev`
> **MLS All-Stars vs. International Clubs**
> The Major League Soccer All-Star Game is an annual soccer game held by Major League Soccer featuring select players from the league against an international club. [alce::199__wikidata_comp__dev::p13]
> MLS initially adopted a traditional all-star game format where the Eastern Conference squared off against the Western Conference, but this eventually evolved into the current system where the league annually invites a club from abroad to play against a league all-star team. [alce::199__wikidata_comp__dev::p13]
> Specific examples of international clubs that competed include Chelsea FC in 2012, Manchester United in 2010, Bayern Munich in 2014, and Roma in 2013. [alce::199__wikidata_comp__dev::p0, alce::199__wikidata_comp__dev::p4, alce::199__wikidata_comp__dev::p9]

Cited: alce::199__wikidata_comp__dev::p0, alce::199__wikidata_comp__dev::p13, alce::199__wikidata_comp__dev::p4, alce::199__wikidata_comp__dev::p9

### `812__wikidata_simple__dev`
> **Marion Zimmer Bradley edited multiple pieces of literature including Marion Zimmer Bradley's Fantasy Magazine, Marion Zimmer Bradley's Darkover anthology, and the Sword and Sorceress anthology series**
> Marion Zimmer Bradley's Fantasy Magazine was a quarterly fantasy magazine founded and initially edited by American writer Marion Zimmer Bradley. [alce::812__wikidata_simple__dev::p6]
> Marion Zimmer Bradley's Darkover is a collection of science fantasy short stories by American writer Marion Zimmer Bradley. [alce::812__wikidata_simple__dev::p10]
> Bradley was the editor of the long-running "Sword and Sorceress" anthology series, which encouraged submissions of fantasy stories featuring original and non-traditional heroines from young and upcoming authors. [alce::812__wikidata_simple__dev::p9]

Cited: alce::812__wikidata_simple__dev::p10, alce::812__wikidata_simple__dev::p6, alce::812__wikidata_simple__dev::p9

### `179__wikidata_intersection__dev`
> **Patala Bhairavi**
> B. Nagi Reddy produced several films including "Patala Bhairavi" (1951). [alce::179__wikidata_intersection__dev::p2]
> Ghantasala composed music for "Patala Bhairavi" among many popular Telugu movies. [alce::179__wikidata_intersection__dev::p7]

Cited: alce::179__wikidata_intersection__dev::p2, alce::179__wikidata_intersection__dev::p7

### `25__wikitables_composition__dev`
> **The museums in Cambridge, Cambridgeshire include the Museum of Cambridge, the Fitzwilliam Museum, the Cambridge Museum of Technology, and the University of Cambridge Museums (including the Museum of Archaeology and Anthropology, The Polar Museum, The Sedgwick Museum of Earth Sciences, Museum of Classical Archaeology, The Whipple Museum of the History of Science, and the University Museum of Zoology).**
> The Museum of Cambridge, formerly known as the Cambridge & County Folk Museum, is a museum located in Castle Street in central Cambridge, England. [alce::25__wikitables_composition__dev::p0]
> The Fitzwilliam Museum is the art and antiquities museum of the University of Cambridge, located on Trumpington Street opposite Fitzwilliam Street in central Cambridge, England. [alce::25__wikitables_composition__dev::p28]
> The Cambridge Museum of Technology is an industrial heritage museum situated in Cambridge, England. [alce::25__wikitables_composition__dev::p11]
> Other members of the University of Cambridge Museums are the Museum of Archaeology and Anthropology, The Polar Museum, The Sedgwick Museum of Earth Sciences, Museum of Classical Archaeology, The Whipple Museum of the History of Science, and the University Museum of Zoology. [alce::25__wikitables_composition__dev::p2]

Cited: alce::25__wikitables_composition__dev::p0, alce::25__wikitables_composition__dev::p11, alce::25__wikitables_composition__dev::p2, alce::25__wikitables_composition__dev::p28

### `409__wikidata_intersection__dev`
> **Maari**
> Anirudh scored music for "Maari", which was another project with Dhanush. [alce::409__wikidata_intersection__dev::p6]

Cited: alce::409__wikidata_intersection__dev::p6

### `497__wikitables_simple__dev`
> **Lighthouses with a height of at least 26 meters: Polish lighthouse (26 meters), Portuguese lighthouse in Barra (62 meters), and Griffith Island lighthouse (25.9 meters - does not meet threshold)**
> The lighthouse is 26 metres tall, with a range of its light glare of 29.6 kilometres. [alce::497__wikitables_simple__dev::p5]
> In Barra, one can find the tallest Portuguese lighthouse (62 metres from the ground but 66 metres above sea level). [alce::497__wikitables_simple__dev::p36]
> The lighthouse is one of the so-called imperial towers and is 25.9 meters (85 feet) in height. [alce::497__wikitables_simple__dev::p51]
> The Gibraltar North Mole Elbow Lighthouse is a grey, square, skeletal tower, with a height of 25 metres (82 feet). [alce::497__wikitables_simple__dev::p96]

Cited: alce::497__wikitables_simple__dev::p36, alce::497__wikitables_simple__dev::p5, alce::497__wikitables_simple__dev::p51, alce::497__wikitables_simple__dev::p96

### `376__wikidata_comp__dev`
> **Trinity College, Oxford**
> Eric Henry Knell was the Bishop of Reading from 1954 until 1972 and was educated at Trinity College, Oxford. [alce::376__wikidata_comp__dev::p47]

Cited: alce::376__wikidata_comp__dev::p47

### `385__wikidata_intersection__dev`
> **Everton FC competed in multiple FA Cup Finals including 1893, 1897, 1906, 1907, 1980s, 2009, and 2015-16**
> Everton reached four FA Cup finals before the First World War, losing 1–0 against Wolverhampton Wanderers at Fallowfield Stadium, Manchester on 26 March 1893 and 3–2 against Aston Villa at Crystal Palace on 10 April 1897 before winning at their third attempt on 20 April 1906 against Newcastle United again at Crystal Palace. [alce::385__wikidata_intersection__dev::p25]
> Everton then reached their second successive final on 20 April 1907, however, finished in a 2–1 defeat to Sheffield Wednesday. [alce::385__wikidata_intersection__dev::p25]
> West Ham United beat Everton 2–1 at Elland Road to reach the FA Cup final in 1980. [alce::385__wikidata_intersection__dev::p26]
> Everton did reach their First FA Cup final since 1995 after knocking out Manchester United on penalties in the semi final at Wembley, but were overcome by Chelsea and lost 2–1. [alce::385__wikidata_intersection__dev::p75]
> Although the club managed to reach the semi-finals in both the FA Cup and League Cup in the 2015–16 season, their overall performance did not meet expectations. [alce::385__wikidata_intersection__dev::p58]
> In the FA Cup, Everton reached their second successive FA Cup Final. [alce::385__wikidata_intersection__dev::p32]

Cited: alce::385__wikidata_intersection__dev::p25, alce::385__wikidata_intersection__dev::p26, alce::385__wikidata_intersection__dev::p32, alce::385__wikidata_intersection__dev::p58, alce::385__wikidata_intersection__dev::p75

### `626__wikidata_simple__dev`
> **Multiple players were selected by the Boston Celtics in NBA drafts, including Jared Sullinger, Fab Melo, Kris Joseph, Cedric Maxwell, Larry Bird, Tom Heinsohn, Bill Russell, Jaylen Brown, Guerschon Yabusele, Ante Žižić, Deyonta Davis, Rade Zagorac, Demetrius Jackson, Terry Rozier, R.J. Hunter, Jordan Mickey, and Marcus Thornton**
> The Celtics drafted three players, Jared Sullinger, Fab Melo and Kris Joseph with their 21st, 22nd and 51st picks respectively. [alce::626__wikidata_simple__dev::p0]
> The Celtics drafted a young forward from the UNC Charlotte named Cedric Maxwell. [alce::626__wikidata_simple__dev::p36]
> Auerbach took a risk and selected junior Larry Bird of Indiana State with the 6th pick. [alce::626__wikidata_simple__dev::p36]
> Tom Heinsohn from the College of the Holy Cross was selected before the draft as Boston Celtics' territorial pick. [alce::626__wikidata_simple__dev::p76]
> Bill Russell from the University of San Francisco was selected second overall by the St. Louis Hawks and immediately traded to the Boston Celtics. [alce::626__wikidata_simple__dev::p76]
> For the first round of the draft, the Celtics drafted Jaylen Brown from the University of California, Guerschon Yabusele from France, and Ante Žižić from Croatia. [alce::626__wikidata_simple__dev::p1]
> In the second round, Boston took Deyonta Davis from Michigan State University, Rade Zagorac from Serbia, and Demetrius Jackson from the University of Notre Dame. [alce::626__wikidata_simple__dev::p1]
> In the 2015 NBA draft Boston selected Terry Rozier, R.J. Hunter, Jordan Mickey, and Marcus Thornton with the 16th, 28th, 33rd, and 45th selections respectively. [alce::626__wikidata_simple__dev::p39]

Cited: alce::626__wikidata_simple__dev::p0, alce::626__wikidata_simple__dev::p1, alce::626__wikidata_simple__dev::p36, alce::626__wikidata_simple__dev::p39, alce::626__wikidata_simple__dev::p76

### `193__wikidata_intersection__dev`
> **Super Bowl VI, Super Bowl VII, Super Bowl VIII, Super Bowl XVII, and Super Bowl XIX**
> The team made its first Super Bowl appearance in Super Bowl VI, but lost to the Dallas Cowboys. [alce::193__wikidata_intersection__dev::p2]
> The following year, the Dolphins completed the NFL's only perfect season culminating in a Super Bowl win. [alce::193__wikidata_intersection__dev::p2]
> Miami also appeared in Super Bowl XVII and Super Bowl XIX, losing both games. [alce::193__wikidata_intersection__dev::p62]
> The Dolphins were the first team to appear in three consecutive Super Bowls. [alce::193__wikidata_intersection__dev::p10]
> The Dolphins entered their fifth Super Bowl in team history after posting a 14–2 regular season record. [alce::193__wikidata_intersection__dev::p17]

Cited: alce::193__wikidata_intersection__dev::p10, alce::193__wikidata_intersection__dev::p17, alce::193__wikidata_intersection__dev::p2, alce::193__wikidata_intersection__dev::p62

### `737__wikidata_simple__dev`
> **Bodysong and Kelly + Victor**
> Janine Marmot is a British film producer and founder of Hot Property Films. She is best known for the BAFTA-winning documentary Bodysong and the relationship drama Kelly + Victor, which won the Outstanding British Debut BAFTA award in 2014. [alce::737__wikidata_simple__dev::p0]
> Her feature credits as Producer include Simon Pummell's BAFTA and BIFA winning feature documentary Bodysong, scored by Jonny Greenwood of Radiohead and Shock Head Soul; Michael Whyte's No Greater Love and Looking For Light, Institute Benjamenta directed by The Brothers Quay; and I Could Read The Sky directed by Nichola Bruce. [alce::737__wikidata_simple__dev::p0]

Cited: alce::737__wikidata_simple__dev::p0

### `746__wikidata_simple__dev`
> **Miyeon, Minnie, Soojin, Soyeon, Yuqi, and Shuhua**
> (G)I-dle is a South Korean girl group formed by Cube Entertainment in 2018, consisting of six members: Miyeon, Minnie, Soojin, Soyeon, Yuqi, and Shuhua. [alce::746__wikidata_simple__dev::p0]

Cited: alce::746__wikidata_simple__dev::p0

### `412__wikidata_comp__dev`
> **Calvert Hall College High School**
> Calvert Hall College High School in Baltimore, Maryland is a school attended by an athlete drafted by the Milwaukee Brewers. [alce::412__wikidata_comp__dev::p0]

Cited: alce::412__wikidata_comp__dev::p0

### `873__wikidata_simple__dev`
> **Abinergaios II, Meredates, Artabazos I, and Orabazes II**
> Abinergaios II was a ruler of Characene, an ancient kingdom located at the head of the Persian Gulf in modern Iraq. [alce::873__wikidata_simple__dev::p12]
> Meredates was a Parthian prince who ruled the state of Characene, a vassal of the Parthian Empire and important trading port. [alce::873__wikidata_simple__dev::p72]
> Artabazos I of Characene was a king of Characene, a vassal state of the Parthians. [alce::873__wikidata_simple__dev::p47]
> Orabazes II was a King of Characene a kingdom located at the head of the Persian Gulf. [alce::873__wikidata_simple__dev::p19]

Cited: alce::873__wikidata_simple__dev::p12, alce::873__wikidata_simple__dev::p19, alce::873__wikidata_simple__dev::p47, alce::873__wikidata_simple__dev::p72

### `261__wikidata_intersection__dev`
> **Multiple movies: Billy Madison (1995), Happy Gilmore (1996), and The Ridiculous 6 (2015)**
> Happy Gilmore is a 1996 American sports comedy film directed by Dennis Dugan with music by Mark Mothersbaugh and produced by Robert Simonds. It stars Adam Sandler as the title character, an unsuccessful ice hockey player who discovers a newfound talent for golf. The screenplay was written by Sandler and Tim Herlihy. [alce::261__wikidata_intersection__dev::p2]
> Billy Madison is a 1995 American comedy film directed by Tamra Davis. It stars Adam Sandler, Bradley Whitford, Bridgette Wilson, Norm Macdonald, in his feature film debut and Darren McGavin. The film was written by Sandler and Tim Herlihy, and produced by Robert Simonds. [alce::261__wikidata_intersection__dev::p36]
> The Ridiculous 6 is a 2015 American Western action comedy film directed by Frank Coraci and written by Tim Herlihy and Adam Sandler. [alce::261__wikidata_intersection__dev::p44]

Cited: alce::261__wikidata_intersection__dev::p2, alce::261__wikidata_intersection__dev::p36, alce::261__wikidata_intersection__dev::p44

### `527__wikitables_simple__dev`
> **Commercially available software-defined radios include USRP (Universal Software Radio Peripheral) and GNU Radio**
> Universal Software Radio Peripheral (USRP) is a range of software-defined radios designed and sold by Ettus Research and its parent company, National Instruments. [alce::527__wikitables_simple__dev::p65]
> The USRP product family is intended to be a comparatively inexpensive hardware platform for software radio, and is commonly used by research labs, universities, and hobbyists. [alce::527__wikitables_simple__dev::p65]
> GNU Radio is a free software development toolkit that provides signal processing blocks to implement software-defined radios and signal-processing systems, and is widely used in hobbyist, academic, and commercial environments. [alce::527__wikitables_simple__dev::p25]

Cited: alce::527__wikitables_simple__dev::p25, alce::527__wikitables_simple__dev::p65

### `566__wikidata_simple__dev`
> **The Cherokee people natively speak Cherokee**
> Cherokee is an endangered Iroquoian language and the native language of the Cherokee people. [alce::566__wikidata_simple__dev::p7]
> The Cherokee are one of the indigenous people of the Southeastern Woodlands who historically inhabited the mountain and inland regions of the southeastern United States. [alce::566__wikidata_simple__dev::p11, alce::566__wikidata_simple__dev::p5]

Cited: alce::566__wikidata_simple__dev::p11, alce::566__wikidata_simple__dev::p5, alce::566__wikidata_simple__dev::p7

### `312__wikidata_comp__dev`
_Refused._

### `311__wikidata_intersection__dev`
> **Premier League, FA Cup, League Championship, UEFA Cup Winners Cup, Champions League, FA WSL 1, Premier League National Division, Premier League Cup, FA Women's Cup**
> Everton F.C. competes in the Premier League, the top flight of English football. [alce::311__wikidata_intersection__dev::p2]
> Everton have won the League Championship nine times, the FA Cup five times, and the UEFA Cup Winners Cup once. [alce::311__wikidata_intersection__dev::p2]
> Both Everton and Liverpool were able to compete in the Champions League. [alce::311__wikidata_intersection__dev::p4]
> Everton L.F.C. competes in the FA WSL 1, the first division of women's football in England. [alce::311__wikidata_intersection__dev::p21]
> Everton L.F.C. has won the Premier League National Division once, the Premier League Cup once, and the FA Women's Cup twice. [alce::311__wikidata_intersection__dev::p10]
> Liverpool have won the European Cup 5 times and have eighteen top-flight titles. [alce::311__wikidata_intersection__dev::p1]

Cited: alce::311__wikidata_intersection__dev::p1, alce::311__wikidata_intersection__dev::p10, alce::311__wikidata_intersection__dev::p2, alce::311__wikidata_intersection__dev::p21, alce::311__wikidata_intersection__dev::p4

### `295__wikidata_intersection__dev`
> **Madrasapattinam**
> His music in the film "Madrasapattinam", directed by A. L. Vijay was appreciated mainly for his song "Pookal Pookum Tharunam". [alce::295__wikidata_intersection__dev::p0]

Cited: alce::295__wikidata_intersection__dev::p0

### `954__wikidata_comp__dev`
_Refused._

### `427__wikidata_intersection__dev`
> **Cup Winners' Cup, European Cup/UEFA Champions League, FA Cup, Football League Cup, FA Premier League, English Premier League, EFL Cup, and International Champions Cup**
> Tottenham Hotspur won the Cup Winners' Cup in 1963. [alce::427__wikidata_intersection__dev::p15]
> Manchester United were the first English winners of the European Cup in 1968. [alce::427__wikidata_intersection__dev::p15]
> During the 2000–01 season, Tottenham Hotspur participated in the English Premier League, FA Cup, and Football League Cup. [alce::427__wikidata_intersection__dev::p51]
> During the 1995–96 season, Tottenham Hotspur participated in the FA Premier League. [alce::427__wikidata_intersection__dev::p26]
> During the 2018–19 season, Tottenham Hotspur competed in the FA Cup, EFL Cup, and the Champions League, and took part in the 2018 International Champions Cup. [alce::427__wikidata_intersection__dev::p66]
> Manchester United has competed in every UEFA-organised competition, with the exception of the now-defunct Intertoto Cup, and has won three European Cups. [alce::427__wikidata_intersection__dev::p39]

Cited: alce::427__wikidata_intersection__dev::p15, alce::427__wikidata_intersection__dev::p26, alce::427__wikidata_intersection__dev::p39, alce::427__wikidata_intersection__dev::p51, alce::427__wikidata_intersection__dev::p66

### `220__wikidata_intersection__dev`
> **Kadavul Mama**
> The last collaboration was "Kadavul Mama" (1974) before the demise of Panthulu, where Lingappa continued on working with Panthulu in many more Kannada films till the early 1970s. [alce::220__wikidata_intersection__dev::p28]
> B. R. Panthulu was an Indian film director, producer and actor who produced films in Kannada, Tamil, Telugu and Hindi. [alce::220__wikidata_intersection__dev::p9]

Cited: alce::220__wikidata_intersection__dev::p28, alce::220__wikidata_intersection__dev::p9

### `468__wikidata_intersection__dev`
> **Cup Winners' Cup**
> Rangers won the Cup Winners' Cup in 1972, and Aberdeen won it in 1983, with both clubs competing in this European competition. [alce::468__wikidata_intersection__dev::p8]
> The 1982–83 European Cup Winners' Cup was won by Aberdeen FC, and Rangers had previously won the same competition in 1972. [alce::468__wikidata_intersection__dev::p25, alce::468__wikidata_intersection__dev::p8]

Cited: alce::468__wikidata_intersection__dev::p25, alce::468__wikidata_intersection__dev::p8

### `841__wikidata_simple__dev`
> **Senior politicians, senior judges, and officials from Commonwealth realms**
> The Privy Council of the United Kingdom is a formal body of advisers to the Sovereign of the United Kingdom, with membership mainly comprising senior politicians who are current or former members of either the House of Commons or the House of Lords. [alce::841__wikidata_simple__dev::p0]
> The Judicial Committee of the Privy Council consists of senior judges appointed as Privy Counsellors, predominantly Justices of the Supreme Court of the United Kingdom and senior judges from the Commonwealth. [alce::841__wikidata_simple__dev::p13]
> Although the Privy Council is primarily a British institution, officials from other Commonwealth realms are also appointed to the body, including Prime Ministers of Commonwealth countries which retain the British monarch as their sovereign. [alce::841__wikidata_simple__dev::p32]

Cited: alce::841__wikidata_simple__dev::p0, alce::841__wikidata_simple__dev::p13, alce::841__wikidata_simple__dev::p32

### `921__wikidata_simple__dev`
> **Multiple groups served the Union, including African-American soldiers, white soldiers, and the USS Union ship**
> Nearly 100,000 white Southern men served in the Union army during the American Civil War, with nearly every Southern slaveholding state raising at least one Yankee regiment. [alce::921__wikidata_simple__dev::p98]
> About 700 African-American soldiers from the county served on the Union side during the war, including many men who escaped slavery and joined the Union cause, as well as free Black citizens. [alce::921__wikidata_simple__dev::p39]
> USS Union (AKA-106) was a ship of the United States Navy that served as a commissioned ship for 25 years and 1 month. [alce::921__wikidata_simple__dev::p52]

Cited: alce::921__wikidata_simple__dev::p39, alce::921__wikidata_simple__dev::p52, alce::921__wikidata_simple__dev::p98

### `803__wikidata_simple__dev`
> **AMC Eagle**
> The AMC Eagle was one of the company's best-known products and is considered one of the first 'crossover SUVs'. [alce::803__wikidata_simple__dev::p44]
> The 'Eagle' name was taken by Chrysler from the four-wheel drive AMC Eagle models that were introduced for the 1980 model year, which was the last of American Motors' wholly U.S.-designed vehicles and arguably the first modern mass-production crossover automobile. [alce::803__wikidata_simple__dev::p2]

Cited: alce::803__wikidata_simple__dev::p2, alce::803__wikidata_simple__dev::p44

### `218__wikidata_intersection__dev`
> **Neelakkuyil**
> In 1954, Bhaskaran along with Ramu Kariat directed the film 'Neelakkuyil'. [alce::218__wikidata_intersection__dev::p0]
> Raghavan set a new trend in Malayalam film music with the release of the 1954 movie 'Neelakuyil'. Renowned lyricist and Raghavan's friend P. Bhaskaran had penned the songs in Neelakkuyil. [alce::218__wikidata_intersection__dev::p13]

Cited: alce::218__wikidata_intersection__dev::p0, alce::218__wikidata_intersection__dev::p13

### `194__wikidata_intersection__dev`
> **For Your Eyes Only**
> Richard Maibaum was a screenwriter best known for his screenplay adaptations of Ian Fleming's James Bond novels. [alce::194__wikidata_intersection__dev::p0]
> Maibaum started writing James Bond screenplays in 1981 with 'For Your Eyes Only'. [alce::194__wikidata_intersection__dev::p54]
> Eon Productions is a British film production company that produces the James Bond film series. [alce::194__wikidata_intersection__dev::p56]

Cited: alce::194__wikidata_intersection__dev::p0, alce::194__wikidata_intersection__dev::p54, alce::194__wikidata_intersection__dev::p56

### `1350__wikidata_simple__dev`
> **2006 Casablanca ATP tournament**
> Bracciali won his only ATP singles title in April 2006, at Casablanca, on clay. [alce::1350__wikidata_simple__dev::p1]
> In the final he beat Nicolás Massú. [alce::1350__wikidata_simple__dev::p1]

Cited: alce::1350__wikidata_simple__dev::p1

### `76__wikitables_composition__dev`
_Refused._

### `236__wikidata_intersection__dev`
> **Alban Berg and Anton Webern were the principal pupils of Arnold Schoenberg who counted themselves among the Second Viennese School, along with other pupils including Ernst Krenek, Heinrich Jalowetz, Erwin Stein, Egon Wellesz, Eduard Steuermann, Hanns Eisler, Roberto Gerhard, Norbert von Hannenheim, Rudolf Kolisch, Paul A. Pisk, Karl Rankl, Josef Rufer, Nikos Skalkottas, Viktor Ullmann, and Winfried Zillig.**
> The principal members of the school, besides Schoenberg, were Alban Berg and Anton Webern, who were among his first composition pupils. [alce::236__wikidata_intersection__dev::p1]
> Other pupils of this generation included Ernst Krenek, Heinrich Jalowetz, Erwin Stein and Egon Wellesz, and somewhat later Eduard Steuermann, Hanns Eisler, Roberto Gerhard, Norbert von Hannenheim, Rudolf Kolisch, Paul A. Pisk, Karl Rankl, Josef Rufer, Nikos Skalkottas, Viktor Ullmann, and Winfried Zillig. [alce::236__wikidata_intersection__dev::p1, alce::236__wikidata_intersection__dev::p2]

Cited: alce::236__wikidata_intersection__dev::p1, alce::236__wikidata_intersection__dev::p2

### `598__wikidata_simple__dev`
> **Tolly Cobbold Classic**
> Tolly Cobbold sponsored the Tolly Cobbold Classic, a non-ranking snooker tournament staged between 1979 and 1984. [alce::598__wikidata_simple__dev::p1]
> After the 1984 event, Tolly Cobbold decided to sponsor the English Professional Championship instead. [alce::598__wikidata_simple__dev::p0]

Cited: alce::598__wikidata_simple__dev::p0, alce::598__wikidata_simple__dev::p1

### `185__wikidata_comp__dev`
> **Multiple winners across different years (Austin Dillon in 2018, Kurt Busch in 2017, Dale Earnhardt Jr. in 2014, Lee Petty in 1959, Michael Waltrip in another year)**
> Austin Dillon is the defending winner of the Daytona 500, having won it in 2018. [alce::185__wikidata_comp__dev::p10]
> The 2017 Daytona 500 was won by Kurt Busch. [alce::185__wikidata_comp__dev::p34]
> Dale Earnhardt, Jr., driving for Hendrick Motorsports, won the 2014 Daytona 500 race. [alce::185__wikidata_comp__dev::p5]
> Lee Petty won the 1959 Daytona 500 on February 22, 1959. [alce::185__wikidata_comp__dev::p73]
> Michael Waltrip was declared as the winner of a Daytona 500 race that was called off due to rain. [alce::185__wikidata_comp__dev::p39]

Cited: alce::185__wikidata_comp__dev::p10, alce::185__wikidata_comp__dev::p34, alce::185__wikidata_comp__dev::p39, alce::185__wikidata_comp__dev::p5, alce::185__wikidata_comp__dev::p73

### `53__wikitables_composition__dev`
> **Great Mosque of Makassar**
> The Great Mosque of Makassar is a mosque located in Makassar, Indonesia, and the main mosque of South Sulawesi Province. [alce::53__wikitables_composition__dev::p41]

Cited: alce::53__wikitables_composition__dev::p41

### `187__wikidata_intersection__dev`
_Refused._

### `915__wikidata_simple__dev`
_Refused._

### `42__wikitables_composition__dev`
> **Genesee Township**
> Genesee Township, also known as the Charter Township of Genesee, is a charter township of Genesee County in the U.S. state of Michigan. [alce::42__wikitables_composition__dev::p1]

Cited: alce::42__wikitables_composition__dev::p1

### `816__wikidata_simple__dev`
> **Ernest Rutherford**
> In April 1919, Rutherford became director of the Cavendish Laboratory at the University of Cambridge, and Chadwick joined him there a few months later. [alce::816__wikidata_simple__dev::p4]
> Chadwick was awarded a Clerk-Maxwell studentship in 1920, and enrolled as a Doctor of Philosophy (PhD) student at Gonville and Caius College, Cambridge. [alce::816__wikidata_simple__dev::p4]
> The first half of his thesis was his work with atomic numbers. In the second, he looked at the forces inside the nucleus. His degree was awarded in June 1921. [alce::816__wikidata_simple__dev::p4]

Cited: alce::816__wikidata_simple__dev::p4

### `1364__wikidata_simple__dev`
> **Mercer Island**
> Lake Washington is a large freshwater lake that encloses Mercer Island. [alce::1364__wikidata_simple__dev::p5]

Cited: alce::1364__wikidata_simple__dev::p5

### `763__wikidata_simple__dev`
> **Setsuna F. Seiei**
> Setsuna F. Seiei, whose real name is ("Suran Ibrahim"), is a fictional character introduced as the protagonist of Sunrise's anime series "Mobile Suit Gundam 00". [alce::763__wikidata_simple__dev::p20]
> Setsuna F. Seiei is the primary protagonist of "Mobile Suit Gundam 00". [alce::763__wikidata_simple__dev::p28]

Cited: alce::763__wikidata_simple__dev::p20, alce::763__wikidata_simple__dev::p28

### `339__wikidata_intersection__dev`
> **MLB umpires**
> Beginning with the 2000 season, every umpire would work in both leagues. [alce::339__wikidata_intersection__dev::p45]
> As a result of the 2000 collective bargaining agreement between Major League Baseball and the newly formed World Umpires Association, all umpires were placed on one roster and can work in either league. [alce::339__wikidata_intersection__dev::p6]

Cited: alce::339__wikidata_intersection__dev::p45, alce::339__wikidata_intersection__dev::p6

### `828__wikidata_simple__dev`
> **Kala Bazar, Kala Pani, and Hum Dono**
> Kala Bazar is a 1960 Hindi film produced by Dev Anand for Navketan Films. [alce::828__wikidata_simple__dev::p84]
> Kala Pani is a 1958 Hindi movie, produced by Dev Anand for Navketan Films. [alce::828__wikidata_simple__dev::p70]
> Hum Dono is a 1961 Hindi film produced by Dev Anand and Navketan films. [alce::828__wikidata_simple__dev::p15]

Cited: alce::828__wikidata_simple__dev::p15, alce::828__wikidata_simple__dev::p70, alce::828__wikidata_simple__dev::p84

### `774__wikidata_simple__dev`
_Refused._

### `396__wikidata_intersection__dev`
_Refused._

### `955__wikidata_comp__dev`
> **Westminster School and Christ Church, Oxford**
> John King, who was the Bishop of London from 1611 to 1621, received early education at Westminster School and then matriculated at Christ Church, Oxford, where he graduated with a B.A. in 1580 and M.A. in 1583. [alce::955__wikidata_comp__dev::p96]

Cited: alce::955__wikidata_comp__dev::p96

### `731__wikidata_simple__dev`
> **Albert Von Tilzer composed "Take Me Out to the Ball Game" and numerous other popular music compositions**
> Albert Von Tilzer wrote the music to many hit songs, including, most notably, 'Take Me Out to the Ball Game'. [alce::731__wikidata_simple__dev::p5]
> Albert Von Tilzer was a top Tin Pan Alley tune writer, producing numerous popular music compositions from 1900 continuing through the early fifties. [alce::731__wikidata_simple__dev::p0]

Cited: alce::731__wikidata_simple__dev::p0, alce::731__wikidata_simple__dev::p5

### `861__wikidata_simple__dev`
> **The relational model for database management and Codd's cellular automaton**
> Edgar Frank 'Ted' Codd was an English computer scientist who, while working for IBM, invented the relational model for database management, the theoretical basis for relational databases and relational database management systems. [alce::861__wikidata_simple__dev::p0]
> Codd's cellular automaton is a cellular automaton devised by the British computer scientist Edgar F. Codd in 1968, designed to recreate the computation- and construction-universality of von Neumann's CA but with fewer states. [alce::861__wikidata_simple__dev::p4]

Cited: alce::861__wikidata_simple__dev::p0, alce::861__wikidata_simple__dev::p4

### `532__wikitables_simple__dev`
> **Xi**
> Xi was the world's first console-based and virtual world-based alternate reality game. [alce::532__wikitables_simple__dev::p87]
> It was a one-time-only play, unfolding in real time, and only available on the PlayStation 3 through the social gaming network, PlayStation Home. [alce::532__wikitables_simple__dev::p87]

Cited: alce::532__wikitables_simple__dev::p87

### `553__wikitables_simple__dev`
_Refused._

### `635__wikidata_simple__dev`
> **Carlo Armellini, Giuseppe Mazzini, and Aurelio Saffi (19th century Roman Republic)**
> The Roman Republic was a short-lived state declared on 9 February 1849, when the government of the Papal States was temporarily replaced by a republican government due to Pope Pius IX's flight to Gaeta. [alce::635__wikidata_simple__dev::p0]
> The republic was led by Carlo Armellini, Giuseppe Mazzini, and Aurelio Saffi, who together formed a triumvirate. [alce::635__wikidata_simple__dev::p0]

Cited: alce::635__wikidata_simple__dev::p0

### `907__wikidata_simple__dev`
> **Modern Theatres produced multiple films including Sathi Ahalya (1937), Balan (1938), Arundathi (1944), Manthiri Kumari, and Sarvadhikari**
> The first film produced under the banner of Modern Theatres was 'Sathi Ahalya' in 1937. [alce::907__wikidata_simple__dev::p4]
> The next year, Sundaram produced the Malayalam film 'Balan' (1938). [alce::907__wikidata_simple__dev::p4]
> His 1944 film 'Arundathi' was a commercial success and completed 100 days at the theatres. [alce::907__wikidata_simple__dev::p4]
> Sundaram was instrumental in giving M. G. Ramachandran his first major solo box office hit in 'Manthiri Kumari'. [alce::907__wikidata_simple__dev::p4]

Cited: alce::907__wikidata_simple__dev::p4

### `511__wikitables_simple__dev`
> **Isa, Nestor, Rosie, Winnie, Bing, Oliwa, Ginger, Ivan, Joan, Keith, Paka, Georgia, Emma, Ruth, Opal, Amy, Karen, Neoguri, Rammasun, Halong, Genevieve, Vongfong, Nuri, and Hagupit**
> Eleven super typhoons occurred in the basin: Isa, Nestor, Rosie, Winnie, Bing, Oliwa (from Central Pacific), Ginger, Ivan, Joan, Keith, and Paka (from Central Pacific). [alce::511__wikitables_simple__dev::p14]
> Six super typhoons formed in 1962 which were Georgia, Emma, Ruth, Opal, Amy and Karen. [alce::511__wikitables_simple__dev::p3]
> The 2014 season was notable for producing a series of powerful super typhoons, with seven storms reaching Category 5 intensity: Neoguri, Rammasun, Halong, Genevieve, Vongfong, Nuri and Hagupit. [alce::511__wikitables_simple__dev::p22]

Cited: alce::511__wikitables_simple__dev::p14, alce::511__wikitables_simple__dev::p22, alce::511__wikitables_simple__dev::p3

### `467__wikidata_intersection__dev`
> **Manchester City won multiple FA Cups: 1903-04, 1934, and 1955-56**
> Manchester City won the 1903-04 FA Cup, beating Bolton Wanderers 1-0 in the final at Crystal Palace, through a goal scored by Billy Meredith. [alce::467__wikidata_intersection__dev::p0]
> Manchester City won the 1934 FA Cup Final in a 2-1 win over Portsmouth. [alce::467__wikidata_intersection__dev::p52]
> Manchester City won the 1955-56 FA Cup, beating Birmingham City 3-1 in the final at Wembley, London. [alce::467__wikidata_intersection__dev::p4]

Cited: alce::467__wikidata_intersection__dev::p0, alce::467__wikidata_intersection__dev::p4, alce::467__wikidata_intersection__dev::p52

### `789__wikidata_simple__dev`
> **Multiple television programs including "Phred on Your Head Show", "A Walk In Your Shoes", "Sponk!", "Bill Nye the Science Guy", "Tiny Planets", "Pinky Dinky Doo", and "The Upside Down Show"**
> Programs that aired on Noggin during this period of Noggin's history included (among others) "Phred on Your Head Show", "A Walk In Your Shoes", "Sponk!", and "Bill Nye the Science Guy". [alce::789__wikidata_simple__dev::p7]
> Noggin became the primary broadcaster of the Workshop's "Tiny Planets", "Pinky Dinky Doo", and "The Upside Down Show". [alce::789__wikidata_simple__dev::p21]

Cited: alce::789__wikidata_simple__dev::p21, alce::789__wikidata_simple__dev::p7

### `617__wikidata_simple__dev`
> **Multiple written works were produced in Katoomba, including "The Pure Land" by David Foster, "The Bogan Mondrian" and "love, ghosts and nose-hair" by Steven Herrick, and albums by Claude Hay**
> The Pure Land is a novel written by David Foster that was published in 1974, with Part One set in 1930s Katoomba, New South Wales. [alce::617__wikidata_simple__dev::p6]
> Poet and author Steven Herrick wrote a novel, 'The Bogan Mondrian' located in modern-day Katoomba, and his verse-novel, 'love, ghosts and nose-hair' is also set in the town. [alce::617__wikidata_simple__dev::p0]
> Both of Claude Hay's albums, 2007's 'Kiss the Sky' and 2010's 'Deep Fried Satisfied' were recorded in Katoomba. [alce::617__wikidata_simple__dev::p0]

Cited: alce::617__wikidata_simple__dev::p0, alce::617__wikidata_simple__dev::p6

### `365__wikidata_comp__dev`
> **Steven Soderbergh directed "Traffic" (screenplay by Stephen Gaghan); Stephen Gaghan directed "Syriana" (screenplay by Stephen Gaghan)**
> Stephen Gaghan is noted for writing the screenplay for Steven Soderbergh's film 'Traffic', based on a Channel 4 series, for which he won the Academy Award. [alce::365__wikidata_comp__dev::p0]
> Gaghan also wrote and directed 'Syriana', a 2005 American geopolitical thriller film. [alce::365__wikidata_comp__dev::p32]

Cited: alce::365__wikidata_comp__dev::p0, alce::365__wikidata_comp__dev::p32

### `821__wikidata_simple__dev`
> **Malcolm X, Muhammad Ali, Elijah Muhammad, and Clarence 13X belonged to the Nation of Islam faith**
> Two of the most famous people to join the NOI were Malcolm X, who became the face of the NOI in the media, and Muhammad Ali, who, while initially rejected, was accepted into the group shortly after his first world heavyweight championship victory. [alce::821__wikidata_simple__dev::p33]
> Many former Nation of Islam members have gone on to become major figures in the large African-American Muslim presence in North America, such as Malcolm X, Muhammad Ali and Nation of Islam founder Elijah Muhammad's own son, Warith Deen Mohammed. [alce::821__wikidata_simple__dev::p3]
> Clarence 13X, a former student of Malcolm X, left the Nation of Islam after a theological dispute with the Nation's leaders over the nature and identity of God. [alce::821__wikidata_simple__dev::p79]

Cited: alce::821__wikidata_simple__dev::p3, alce::821__wikidata_simple__dev::p33, alce::821__wikidata_simple__dev::p79

### `1365__wikidata_simple__dev`
> **An aircraft carrier is a warship that serves as a seagoing airbase**
> An aircraft carrier is a warship that serves as a seagoing airbase, equipped with a full-length flight deck and facilities for carrying, arming, deploying, and recovering aircraft. [alce::1365__wikidata_simple__dev::p0]
> Typically, it is the capital ship of a fleet, as it allows a naval force to project air power worldwide without depending on local bases for staging aircraft operations. [alce::1365__wikidata_simple__dev::p0]

Cited: alce::1365__wikidata_simple__dev::p0

### `7__wikitables_composition__dev`
> **New York City**
> New York City Ballet (NYCB) is a ballet company founded in 1948 by choreographer George Balanchine and Lincoln Kirstein. [alce::7__wikitables_composition__dev::p1]
> The David H. Koch Theater is a theater for ballet, modern and other forms of dance, part of the Lincoln Center for the Performing Arts located at the intersection of Columbus Avenue and 63rd Street in New York City, United States, and has been home to the New York City Ballet since its opening in 1964. [alce::7__wikitables_composition__dev::p14]

Cited: alce::7__wikitables_composition__dev::p1, alce::7__wikitables_composition__dev::p14

### `395__wikidata_comp__dev`
> **Oliver Stone**
> Halsted partnered with filmmaker Oliver Stone in 1995 to create Illusion Entertainment, a joint production company. Together, they produced films such as: 'Nixon', 'U Turn', 'The Art of War', 'The Corruptor', 'Beyond Borders', 'Freeway', 'Any Given Sunday', and the documentary 'The Last Days of Kennedy and King' for TBS. [alce::395__wikidata_comp__dev::p1, alce::395__wikidata_comp__dev::p5]

Cited: alce::395__wikidata_comp__dev::p1, alce::395__wikidata_comp__dev::p5

### `383__wikidata_intersection__dev`
> **Multiple films including "49th Parallel" (1941), "The Life and Death of Colonel Blimp" (1943), "A Matter of Life and Death" (1946), "Black Narcissus" (1947), "The Red Shoes" (1948), and "The Tales of Hoffmann" (1951)**
> Through their production company 'The Archers', they together wrote, produced and directed a series of classic British films, notably '49th Parallel' (1941), 'The Life and Death of Colonel Blimp' (1943), 'A Matter of Life and Death' (1946, also called 'Stairway to Heaven'), 'Black Narcissus' (1947), 'The Red Shoes' (1948), and 'The Tales of Hoffmann' (1951). [alce::383__wikidata_intersection__dev::p22]
> Working together as co-producers, writers and directors in a partnership they dubbed 'The Archers', they made 19 feature films, many of which received critical and commercial success. [alce::383__wikidata_intersection__dev::p2]

Cited: alce::383__wikidata_intersection__dev::p2, alce::383__wikidata_intersection__dev::p22

### `201__wikidata_comp__dev`
> **Ranjan (for one film) and Harikrishnan (for another film)**
> It was Antony Perumbavoor who called Ranjan to script the film. [alce::201__wikidata_comp__dev::p1]
> Harikrishnan wrote 'Odiyan' devoid of myth, and Antony Perumbavoor suggested a major change in the first draft of the screenplay. [alce::201__wikidata_comp__dev::p86]

Cited: alce::201__wikidata_comp__dev::p1, alce::201__wikidata_comp__dev::p86

### `192__wikidata_comp__dev`
> **Gustav Holst**
> Gustav Holst was a choral symphony composer who wrote The Choral Symphony for soprano soloist, chorus, and orchestra in a setting of verses by John Keats. [alce::192__wikidata_comp__dev::p3]
> Other notable choral symphony composers include Hector Berlioz, Ludwig van Beethoven, and George Dyson. [alce::192__wikidata_comp__dev::p0, alce::192__wikidata_comp__dev::p11]

Cited: alce::192__wikidata_comp__dev::p0, alce::192__wikidata_comp__dev::p11, alce::192__wikidata_comp__dev::p3

### `243__wikidata_comp__dev`
> **Bill Condon**
> Bill Condon wrote the screenplay for "Chicago" (2002), and the film was directed by someone else, but Condon himself was a director on other films where he served as screenwriter. [alce::243__wikidata_comp__dev::p4]
> In films where Bill Condon was screenwriter, Bill Condon himself was also a director on several of his works, including "Gods and Monsters" (1998), "Kinsey" (2004), and "Dreamgirls" (2006), where he both wrote and directed. [alce::243__wikidata_comp__dev::p4]

Cited: alce::243__wikidata_comp__dev::p4

### `167__wikidata_comp__dev`
> **Multiple teams have competed in a Super Bowl, including the Green Bay Packers, New York Giants, Dallas Cowboys, Pittsburgh Steelers, New England Patriots, Denver Broncos, and many others**
> The Green Bay Packers and New York Giants have four Super Bowl championships, and fourteen other NFL franchises have won at least one Super Bowl. [alce::167__wikidata_comp__dev::p0]
> Eight teams have appeared in Super Bowl games without a win, including the Minnesota Vikings, Buffalo Bills, and others. [alce::167__wikidata_comp__dev::p0]
> The Patriots, Dallas Cowboys, and Pittsburgh Steelers are among four teams that have made eight appearances in the Super Bowl. [alce::167__wikidata_comp__dev::p71]
> The New England Patriots advanced to their ninth Super Bowl appearance in Super Bowl LI. [alce::167__wikidata_comp__dev::p71]

Cited: alce::167__wikidata_comp__dev::p0, alce::167__wikidata_comp__dev::p71

### `748__wikidata_simple__dev`
> **The Thin Blue Line**
> Errol Morris is an American film director primarily of documentaries, and he is perhaps best known for his 1988 documentary 'The Thin Blue Line', commonly cited among the best and most influential documentaries ever made. [alce::748__wikidata_simple__dev::p0]
> Other notable films created by Errol Morris include 'Gates of Heaven' (1978), 'Vernon, Florida' (1981), 'The Fog of War: Eleven Lessons from the Life of Robert S. McNamara' (2003), and 'Tabloid' (2010). [alce::748__wikidata_simple__dev::p20, alce::748__wikidata_simple__dev::p32, alce::748__wikidata_simple__dev::p36]

Cited: alce::748__wikidata_simple__dev::p0, alce::748__wikidata_simple__dev::p20, alce::748__wikidata_simple__dev::p32, alce::748__wikidata_simple__dev::p36

### `810__wikidata_simple__dev`
> **Multiple characters made their first appearance in The Incredible Hulk, including Betty Ross, Rebecca Banner, and Jim Wilson**
> Betty Ross made her first appearance in 'Incredible Hulk' #1 (1962) as a romantic interest of the Hulk (Dr. Bruce Banner). [alce::810__wikidata_simple__dev::p1]
> Rebecca Banner made her first appearance in 'Incredible Hulk' #267 (January 1982). [alce::810__wikidata_simple__dev::p43]
> Jim Wilson made his first appearance in 'The Incredible Hulk' (vol. 2) #131 as an angry young man who befriends the Hulk. [alce::810__wikidata_simple__dev::p62]

Cited: alce::810__wikidata_simple__dev::p1, alce::810__wikidata_simple__dev::p43, alce::810__wikidata_simple__dev::p62

### `91__wikitables_composition__dev`
_Refused._

### `938__wikidata_simple__dev`
> **Orson Scott Card's InterGalactic Medicine Show**
> Orson Scott Card's InterGalactic Medicine Show (2008) is an anthology edited by Edmund R. Schubert and Orson Scott Card. [alce::938__wikidata_simple__dev::p21]

Cited: alce::938__wikidata_simple__dev::p21

### `831__wikidata_simple__dev`
> **Mirian III and Artaxias I came from the Kingdom of Iberia**
> Mirian III was a king of Iberia or Kartli (Georgia), contemporaneous to the Roman emperor Constantine the Great (r. 306–337). [alce::831__wikidata_simple__dev::p95]
> Artaxias I, of the Artaxiad dynasty, was a king of Iberia (modern-day Georgia) from 90 to 78 BC. [alce::831__wikidata_simple__dev::p45]
> The Kingdom of Iberia was an exonym (foreign name) for the Georgian kingdom of Kartli, which during Classical Antiquity and the Early Middle Ages was a significant monarchy in the Caucasus. [alce::831__wikidata_simple__dev::p2]

Cited: alce::831__wikidata_simple__dev::p2, alce::831__wikidata_simple__dev::p45, alce::831__wikidata_simple__dev::p95

### `463__wikidata_intersection__dev`
> **Boxeo Telemundo**
> The network also produces "Boxeo Telemundo", a weekly late-night boxing series that airs on most Friday nights (except during the summer) showcasing fights from up-and-coming boxing talents. [alce::463__wikidata_intersection__dev::p50]

Cited: alce::463__wikidata_intersection__dev::p50

### `913__wikidata_simple__dev`
> **Multiple players including Kyrie Irving, Tristan Thompson, LeBron James, Anthony Bennett, Ron Harper, and Mark Price**
> The Cavaliers selected guard Kyrie Irving with the first pick and Texas Longhorns power forward Tristan Thompson with the 4th pick. [alce::913__wikidata_simple__dev::p0]
> The Cavaliers selected high school phenom LeBron James from St. Vincent-St. Mary High School in nearby Akron. [alce::913__wikidata_simple__dev::p20]
> The Cavaliers drafted forward Anthony Bennett of UNLV as the number one pick, making Bennett the first Canadian born player in history to be the number one pick. [alce::913__wikidata_simple__dev::p3]
> The Cavaliers drafted Ron Harper with the eighth pick in the 1986 draft and obtained the rights to Mark Price (in a trade with the Dallas Mavericks) the 25th pick (second round). [alce::913__wikidata_simple__dev::p79]

Cited: alce::913__wikidata_simple__dev::p0, alce::913__wikidata_simple__dev::p20, alce::913__wikidata_simple__dev::p3, alce::913__wikidata_simple__dev::p79

### `246__wikidata_comp__dev`
> **Multiple Associate Justices attended various schools including Brown University, University of Chicago Law School, Princeton University, Harvard Law School, Georgetown University, and Oxford University**
> Katherine Leatherman Adams, an Associate Justice of the Supreme Court of the United States, earned a Bachelor's degree in Comparative Literature from Brown University in 1986 and a Juris Doctoral degree from the University of Chicago Law School in 1990. [alce::246__wikidata_comp__dev::p37]
> Elena Kagan, an Associate Justice of the Supreme Court of the United States, attended Princeton University, Worcester College Oxford, and Harvard Law School. [alce::246__wikidata_comp__dev::p72]
> Antonin Scalia, an Associate Justice of the Supreme Court of the United States, attended Xavier High School in Manhattan, Georgetown University, and Harvard Law School. [alce::246__wikidata_comp__dev::p49]
> David Souter, a retired Associate Justice of the Supreme Court of the United States, attended Harvard College, Oxford University, and Harvard Law School. [alce::246__wikidata_comp__dev::p13]

Cited: alce::246__wikidata_comp__dev::p13, alce::246__wikidata_comp__dev::p37, alce::246__wikidata_comp__dev::p49, alce::246__wikidata_comp__dev::p72

### `149__wikidata_comp__dev`
> **Stanley Tucci**
> Joe Gould's Secret is a 2000 American drama film directed by Stanley Tucci. The screenplay by Howard A. Rodman is based on the magazine article "Professor Sea Gull" and the book "Joe Gould's Secret" by Joseph Mitchell. [alce::149__wikidata_comp__dev::p58]

Cited: alce::149__wikidata_comp__dev::p58

### `346__wikidata_comp__dev`
> **MI6**
> John Cairncross, another of the Cambridge Five, was posted from MI6 to work at Bletchley Park. [alce::346__wikidata_comp__dev::p13]
> Kim Philby, another member of the Cambridge Five, was assigned to Washington, serving as Britain's CIA-FBI-NSA liaison. [alce::346__wikidata_comp__dev::p68]
> In common with the other members of the Cambridge Five, his entry to British intelligence was achieved without vetting; his social position and personal recommendation were considered sufficient. [alce::346__wikidata_comp__dev::p43]

Cited: alce::346__wikidata_comp__dev::p13, alce::346__wikidata_comp__dev::p43, alce::346__wikidata_comp__dev::p68

### `38__wikitables_composition__dev`
> **Titanic (1997)**
> In 1997, James Cameron produced, wrote and directed a version of the epic story, 'Titanic'. [alce::38__wikitables_composition__dev::p76]
> The film combined romance with intricate special effects and was a huge success, becoming the highest-grossing film with over $2.1 billion worldwide, and winning 11 Academy Awards including Best Picture and Best Director. [alce::38__wikitables_composition__dev::p76]

Cited: alce::38__wikitables_composition__dev::p76

### `190__wikidata_intersection__dev`
> **Matula**
> "Matula" was a film directed by Tan Tjoei Hock and produced by The Teng Chun for Action Film, a subsidiary of his company New Java Industrial Film. [alce::190__wikidata_intersection__dev::p83]

Cited: alce::190__wikidata_intersection__dev::p83

### `275__wikidata_intersection__dev`
> **Katy Perry and Max Martin created "I Kissed a Girl" and "Hot n Cold"**
> Together with Max Martin they wrote and cut "I Kissed a Girl" and "Hot n Cold". [alce::275__wikidata_intersection__dev::p18]
> Max Martin has written or co-written 22 "Billboard" Hot 100 number-one hits, most of which he has also produced or co-produced, including Katy Perry's "I Kissed a Girl" (2008). [alce::275__wikidata_intersection__dev::p1]

Cited: alce::275__wikidata_intersection__dev::p1, alce::275__wikidata_intersection__dev::p18

### `802__wikidata_simple__dev`
> **Multiple competitions including the Championship, FA Premier League, FA Cup, European Cup, and UEFA Europa League**
> The club currently competes in the Championship, the second tier of the English football league system. [alce::802__wikidata_simple__dev::p12]
> Aston Villa were one of the founder members of the Football League in 1888 and of the Premier League in 1992. [alce::802__wikidata_simple__dev::p12]
> Aston Villa are one of only five English clubs to have won the European Cup, in 1981–82. [alce::802__wikidata_simple__dev::p12]
> During the 2006–07 English football season, Aston Villa F.C. competed in the FA Premier League. [alce::802__wikidata_simple__dev::p99]
> Villa also reached the FA Cup final for the first time in 43 years during the 1999–2000 season. [alce::802__wikidata_simple__dev::p31]
> Aston Villa once again competed in the UEFA Europa League, marking their 2nd consecutive season in the tournament. [alce::802__wikidata_simple__dev::p19]

Cited: alce::802__wikidata_simple__dev::p12, alce::802__wikidata_simple__dev::p19, alce::802__wikidata_simple__dev::p31, alce::802__wikidata_simple__dev::p99

### `102__wikidata_intersection__dev`
> **Multiple competitions: 1997 French Open Women's Doubles, 1997 Wimbledon Championships Women's Doubles, and 1994 Lipton Championships Women's Doubles**
> Gigi Fernández and Natasha Zvereva won the title at the 1997 French Open Women's Doubles, defeating Fernández and Raymond 6–2, 6–3 in the final. [alce::102__wikidata_intersection__dev::p1]
> Gigi Fernández and Natasha Zvereva defeated Arendt and Bollegraf in the final, 7–6, 6–4 to win the Ladies' Doubles tennis title at the 1997 Wimbledon Championships. [alce::102__wikidata_intersection__dev::p3]
> Gigi Fernández and Natasha Zvereva won the 1994 Lipton Championships Women's Doubles in the final 6–3, 6–1 against Fendick and McGrath. [alce::102__wikidata_intersection__dev::p4]

Cited: alce::102__wikidata_intersection__dev::p1, alce::102__wikidata_intersection__dev::p3, alce::102__wikidata_intersection__dev::p4

### `264__wikidata_intersection__dev`
> **Jnanasundari**
> K. S. Sethumadhavan debuted as an independent film director with "Veeravijaya", a Singhalese film in 1960, and his first Malayalam film was "Jnanasundari", produced by T. E. [alce::264__wikidata_intersection__dev::p1]
> G. Devarajan was a Malayalam music composer who scored music for more than three hundred Malayalam films. [alce::264__wikidata_intersection__dev::p14]

Cited: alce::264__wikidata_intersection__dev::p1, alce::264__wikidata_intersection__dev::p14

### `382__wikidata_comp__dev`
> **Multiple JASON members attended various schools including Elisabeth Morrow School, Dwight-Englewood School, Hotchkiss School, Tenafly High School, Westlake High School, Moorpark College, Salisbury High School, Fleetwood Area High School, Hampshire College, Amherst College, and Chorlton High School**
> Growing up, Jason attended a number of private schools, including the Elisabeth Morrow School, the Dwight-Englewood School, the Hotchkiss School, and Tenafly High School. [alce::382__wikidata_comp__dev::p5]
> Jason attended Westlake High School in Westlake Village, California and graduated in 1998. [alce::382__wikidata_comp__dev::p1]
> Jason attended Moorpark College, a two-year junior college, in Moorpark, California. [alce::382__wikidata_comp__dev::p1]
> Jason attended Salisbury High School, in Allentown, Pennsylvania, and Fleetwood Area High School, in Fleetwood, PA. [alce::382__wikidata_comp__dev::p14]
> In 1997, Jason joined his older brother in the United States, attending first Hampshire College and then neighboring Amherst College in Massachusetts. [alce::382__wikidata_comp__dev::p6]
> He attended Chorlton High School when it was known as Oakwood High School. [alce::382__wikidata_comp__dev::p20]

Cited: alce::382__wikidata_comp__dev::p1, alce::382__wikidata_comp__dev::p14, alce::382__wikidata_comp__dev::p20, alce::382__wikidata_comp__dev::p5, alce::382__wikidata_comp__dev::p6

### `221__wikidata_intersection__dev`
> **Multiple films were directed by Shaji Kailas and screenwritten by Renji Panicker, including "Thalastaanam" (1992), "Sthalathe Pradhana Payyans" (1993), "Ekalavyan" (1993), "Mafia" (1993), "Commissioner" (1994), and "The King" (1995)**
> With Renji Panicker, Shaji made popular political thrillers such as "Thalastaanam" (1992), "Sthalathe Pradhana Payyans" (1993), "Ekalavyan" (1993), "Mafia" (1993), "Commissioner" (1994), and "The King" (1995). [alce::221__wikidata_intersection__dev::p1]
> Renji scripted several commercially successful films for Shaji Kailas, including "Dr. Pasupathy" (1990), "Thalastaanam" (1992), "Sthalathe Pradhana Payyans" (1993), "Ekalavyan" (1993), "Mafia" (1993), "Commissioner"(1994), and "The King" (1995). [alce::221__wikidata_intersection__dev::p0]

Cited: alce::221__wikidata_intersection__dev::p0, alce::221__wikidata_intersection__dev::p1

### `69__wikitables_composition__dev`
_Refused._

### `326__wikidata_comp__dev`
_Refused._

### `959__wikidata_comp__dev`
> **University of Cambridge**
> John Henry Lawrence Phillips, the Anglican Bishop of Portsmouth from 1960 until 1975, graduated from the University of Cambridge in 1932. [alce::959__wikidata_comp__dev::p14]

Cited: alce::959__wikidata_comp__dev::p14

### `650__wikidata_simple__dev`
> **The Tale of Peter Rabbit**
> Beatrix Potter was an English writer, illustrator, natural scientist, and conservationist best known for her children's books featuring animals, such as those in "The Tale of Peter Rabbit". [alce::650__wikidata_simple__dev::p0]
> The Tale of Peter Rabbit is a British children's book written and illustrated by Beatrix Potter that follows mischievous and disobedient young Peter Rabbit as he is chased about the garden of Mr. McGregor. [alce::650__wikidata_simple__dev::p34]
> Other children's books illustrated by Beatrix Potter include The Tale of Mrs. Tiggy-Winkle, The Tale of Jemima Puddle-Duck, and The Tale of Two Bad Mice. [alce::650__wikidata_simple__dev::p24, alce::650__wikidata_simple__dev::p25, alce::650__wikidata_simple__dev::p53]

Cited: alce::650__wikidata_simple__dev::p0, alce::650__wikidata_simple__dev::p24, alce::650__wikidata_simple__dev::p25, alce::650__wikidata_simple__dev::p34, alce::650__wikidata_simple__dev::p53

### `545__wikitables_simple__dev`
> **Examples of island countries include the United Kingdom, Republic of Ireland, Haiti, Dominican Republic, Indonesia, Japan, New Zealand, Cuba, Bahrain, Singapore, Iceland, Malta, Taiwan, Trinidad and Tobago, the Philippines, The Bahamas, Seychelles, and the Maldives**
> Some island countries are centred on one or two major islands, such as the United Kingdom, Trinidad and Tobago, New Zealand, Cuba, Bahrain, Singapore, Iceland, Malta, and Taiwan. [alce::545__wikitables_simple__dev::p0]
> Others are spread out over hundreds or thousands of smaller islands, such as Indonesia, the Philippines, The Bahamas, Seychelles, and the Maldives. [alce::545__wikitables_simple__dev::p0]
> Some island countries share one or more of their islands with other countries, such as the United Kingdom and the Republic of Ireland; Haiti and the Dominican Republic; and Indonesia, which shares islands with Papua New Guinea, Brunei, East Timor, and Malaysia. [alce::545__wikitables_simple__dev::p1]

Cited: alce::545__wikitables_simple__dev::p0, alce::545__wikitables_simple__dev::p1

### `471__wikitables_simple__dev`
> **Notable search engines include Google, Bing, Yahoo, Baidu, DuckDuckGo, Yandex, and others**
> Notable engines include Lycos (1994), Alta Vista (1995), Magellan (1995), Google (1998), Yahoo! Search (2004), MSN Search (2005), and Bing (2009). [alce::471__wikitables_simple__dev::p13]
> A few of the most popular search engines are Google, Yahoo, Bing, and Baidu, but many other search engines that are focused on privacy have cropped up recently. [alce::471__wikitables_simple__dev::p8]
> Competitors of Google include Baidu and Soso.com in China; Naver.com and Daum.net in South Korea; Yandex in Russia; Seznam.cz in the Czech Republic; Yahoo in Japan, Taiwan and the US, as well as Bing and DuckDuckGo. [alce::471__wikitables_simple__dev::p81]
> Other search engines that appeared include Magellan, Excite, Infoseek, Inktomi, Northern Light, and AltaVista. [alce::471__wikitables_simple__dev::p1]

Cited: alce::471__wikitables_simple__dev::p1, alce::471__wikitables_simple__dev::p13, alce::471__wikitables_simple__dev::p8, alce::471__wikitables_simple__dev::p81

### `258__wikidata_intersection__dev`
> **2007 UEFA Champions League Final**
> The 2007 UEFA Champions League Final was an association football match between A.C. Milan of Italy and Liverpool F.C. of England on 23 May 2007 at the Olympic Stadium, Athens, Greece. [alce::258__wikidata_intersection__dev::p10]
> The showpiece event was the final match of the 2006–07 season of Europe's premier cup competition, the UEFA Champions League. [alce::258__wikidata_intersection__dev::p10]

Cited: alce::258__wikidata_intersection__dev::p10

### `68__wikitables_composition__dev`
> **The Odisha Legislative Assembly constituencies located in Jajpur district include Jajpur and at least 6 other constituencies, for a total of 7 Vidhan Sabha constituencies**
> Jajpur (Sl. No.: 52) is a Vidhan Sabha constituency of Jajpur district, Odisha. [alce::68__wikitables_composition__dev::p0]
> The following is the 7 Vidhan sabha constituencies of Jajpur district and the elected members of that area. [alce::68__wikitables_composition__dev::p72]

Cited: alce::68__wikitables_composition__dev::p0, alce::68__wikitables_composition__dev::p72

### `262__wikidata_comp__dev`
> **Des Moines, Iowa, USA**
> Meredith Corporation is an American media conglomerate based in Des Moines, Iowa, USA. [alce::262__wikidata_comp__dev::p1]
> The Meredith Corporation, a leading publishing and marketing company, is also based in Des Moines. [alce::262__wikidata_comp__dev::p22]

Cited: alce::262__wikidata_comp__dev::p1, alce::262__wikidata_comp__dev::p22

### `268__wikidata_intersection__dev`
> **North London Derby**
> Arsenal then faced Tottenham Hotspur in the season's first North London Derby, staged at White Hart Lane. [alce::268__wikidata_intersection__dev::p12]
> On 30 April 2017, Tottenham beat Arsenal 2-0 in the final North London Derby at White Hart Lane. [alce::268__wikidata_intersection__dev::p48]
> Tottenham Hotspur set up clash with Arsenal after defeating Sunderland 2–1 at the Stadium of Light on 13 May, with the two teams meeting in the 2008–09 Premier Academy League Play-off Final. [alce::268__wikidata_intersection__dev::p29]

Cited: alce::268__wikidata_intersection__dev::p12, alce::268__wikidata_intersection__dev::p29, alce::268__wikidata_intersection__dev::p48

### `518__wikitables_simple__dev`
> **Notable nightclub fires include the 2001 Canecão Mineiro fire in Belo Horizonte, the 2003 Station nightclub fire in West Warwick Rhode Island, the 2004 República Cromañón fire in Buenos Aires, the 2008 Wuwang Club fire in Shenzhen, the 2009 Santika Club fire in Bangkok, the 2009 Lame Horse fire in Perm Russia, the 2013 Kiss nightclub fire in Santa Maria Brazil, and the 2015 Colectiv nightclub fire in Bucharest Romania**
> Notable nightclub fires include the 2001 Canecão Mineiro nightclub fire in Belo Horizonte, Brazil; the 2003 Station nightclub fire in West Warwick, Rhode Island, in the United States; the 2004 República Cromañón nightclub fire in Buenos Aires, Argentina; the 2008 Wuwang Club fire in Shenzhen, China; the 2009 Santika Club fire in Watthana, Bangkok, Thailand; the 2009 Lame Horse fire in Perm, Russia; and the 2013 Kiss nightclub fire in Santa Maria, Brazil. [alce::518__wikitables_simple__dev::p2]
> The 2013 Kiss nightclub fire in Santa Maria, Rio Grande do Sul, Brazil killed 242 people and injured at least 630 others, making it the third-deadliest nightclub fire in history. [alce::518__wikitables_simple__dev::p3]
> The Cocoanut Grove Fire on November 28, 1942 in Boston, Massachusetts was the deadliest nightclub fire in history, killing 492 people. [alce::518__wikitables_simple__dev::p11]
> The 2015 Colectiv nightclub fire in Bucharest, Romania is also noted as a significant nightclub fire disaster. [alce::518__wikitables_simple__dev::p2]

Cited: alce::518__wikitables_simple__dev::p11, alce::518__wikitables_simple__dev::p2, alce::518__wikitables_simple__dev::p3

### `2__wikitables_composition__dev`
> **Villages in Okinawa include Onna Village and Tarama Village**
> Onna Village is located in the central part of Okinawa Island, occupying a long, narrow stretch of the western coast of the island. [alce::2__wikitables_composition__dev::p62]
> The village of Tarama is located in Okinawa Prefecture and is part of the Okinawa 4th electoral district. [alce::2__wikitables_composition__dev::p18]

Cited: alce::2__wikitables_composition__dev::p18, alce::2__wikitables_composition__dev::p62

### `31__wikitables_composition__dev`
> **South Sumter and East Sumter**
> South Sumter is a census-designated place (CDP) in Sumter County, South Carolina, United States. [alce::31__wikitables_composition__dev::p2]
> East Sumter is a census-designated place (CDP) in Sumter County, South Carolina, United States. [alce::31__wikitables_composition__dev::p7]

Cited: alce::31__wikitables_composition__dev::p2, alce::31__wikitables_composition__dev::p7

### `808__wikidata_simple__dev`
> **Multiple individuals served with the Singapore Armed Forces, including military officers and conscripts**
> One individual served in the Singapore Army from 1987 to 2011, holding positions including Commanding Officer of the 2nd Battalion, Singapore Infantry Regiment (1998-2000), Army Attaché in Jakarta (2001–03), and Commander of the 10th Singapore Infantry Brigade (2003–04). [alce::808__wikidata_simple__dev::p48]
> Another officer enlisted in the Singapore Military Forces in December 1959 and was commissioned as a Second Lieutenant in December 1961, serving as a platoon commander in the 1st Battalion Singapore Infantry Regiment and being deployed to Sebatik Island, Borneo between 1963 and 1964 during the Konfrontasi. [alce::808__wikidata_simple__dev::p92]
> A third individual enlisted in the Singapore Armed Forces in December 1982, was commissioned as a signals officer in December 1986, and served in active duty with the United Nations Iraq–Kuwait Observation Mission (UNIKOM) in Kuwait in 1991, eventually retiring in 2009 as Chief of Staff, Joint Staff. [alce::808__wikidata_simple__dev::p61]
> Another officer served in the Singapore Armed Forces and was the Chief of Army from 1992–1995, holding the rank of Major-General before retiring in 1995. [alce::808__wikidata_simple__dev::p69]
> Conscripts also serve in the Singapore Armed Forces as part of mandatory national service to defend and protect the country. [alce::808__wikidata_simple__dev::p90]

Cited: alce::808__wikidata_simple__dev::p48, alce::808__wikidata_simple__dev::p61, alce::808__wikidata_simple__dev::p69, alce::808__wikidata_simple__dev::p90, alce::808__wikidata_simple__dev::p92

### `827__wikidata_simple__dev`
_Refused._

### `547__wikitables_simple__dev`
> **Warszawa Radio Mast and a concrete building**
> The Warszawa Radio Mast at Konstantynów, Poland was 646.38 metres (2,120.67 ft) tall at the time of its collapse in 1991. [alce::547__wikitables_simple__dev::p10]
> The largest structure is a single-storey, concrete building with dimensions of 680 m and 2,300 m. [alce::547__wikitables_simple__dev::p63]

Cited: alce::547__wikitables_simple__dev::p10, alce::547__wikitables_simple__dev::p63

### `445__wikidata_intersection__dev`
> **West Ham vs Manchester United (13 May 2007)**
> On 13 May, in their last match of the season, West Ham played Manchester United at Old Trafford needing at least a draw to survive in the Premiership, and West Ham were victorious. [alce::445__wikidata_intersection__dev::p10]

Cited: alce::445__wikidata_intersection__dev::p10

### `619__wikidata_simple__dev`
> **Blaze of Glory**
> Blaze of Glory is Jon Bon Jovi's debut solo studio album, released in 1990. [alce::619__wikidata_simple__dev::p11]
> The album includes songs from and inspired by the movie Young Guns II, which Jon Bon Jovi composed after being asked to contribute to the film. [alce::619__wikidata_simple__dev::p11]
> Jon Bon Jovi is credited with composing the music for all of the album's tracks. [alce::619__wikidata_simple__dev::p4]

Cited: alce::619__wikidata_simple__dev::p11, alce::619__wikidata_simple__dev::p4

### `239__wikidata_comp__dev`
_Refused._

### `373__wikidata_comp__dev`
> **French citizenship (originally), then Swiss citizenship**
> Godard originally held only French citizenship, then in 1953, he became a citizen of Gland, canton of Vaud, Switzerland, possibly through simplified naturalisation through his Swiss father. [alce::373__wikidata_comp__dev::p8]

Cited: alce::373__wikidata_comp__dev::p8

### `443__wikidata_intersection__dev`
> **The Seven Minutes**
> The Seven Minutes is a 1971 American drama film directed and produced by Russ Meyer. [alce::443__wikidata_intersection__dev::p1]
> The film was based on a novel by Irving Wallace, and Russ Meyer was involved in writing the screenplay as indicated by the discussion of his contributions to the story and script. [alce::443__wikidata_intersection__dev::p1]

Cited: alce::443__wikidata_intersection__dev::p1

### `263__wikidata_comp__dev`
> **Huck Botko and Andrew Gurland**
> Newman produced "The Other Woman" (2011), another film written by Huck Botko and Andrew Gurland, the writers of "The Last Exorcism". [alce::263__wikidata_comp__dev::p7]
> Newman produced "The Last Exorcism" and "The Man with the Iron Fists" with Eli Roth. [alce::263__wikidata_comp__dev::p7]

Cited: alce::263__wikidata_comp__dev::p7

### `1366__wikidata_simple__dev`
> **The Life of Emile Zola**
> Norman Reilly Raine was an American screenwriter, creator of "Tugboat Annie" and winner of an Oscar for the screenplay of "The Life of Emile Zola" (1937). [alce::1366__wikidata_simple__dev::p2]
> He also wrote screenplays for many other films including "The Perfect Specimen", "God's Country and the Woman", The Adventures of Robin Hood, "Each Dawn I Die", "The Private Lives of Elizabeth and Essex", "Mountain Justice", The Fighting 69th", "Men Are Such Fools", "Eagle Squadron", "Ladies Courageous", "We've Never Been Licked", "Nob Hill", "A Bell for Adano", "Captain Kidd" and "Captains of the Clouds". [alce::1366__wikidata_simple__dev::p0]
> In 1933 he wrote the screenplay for the Tugboat Annie film, in which Marie Dressler played Annie and Wallace Beery portrayed Terry, her hard-drinking husband. [alce::1366__wikidata_simple__dev::p8]

Cited: alce::1366__wikidata_simple__dev::p0, alce::1366__wikidata_simple__dev::p2, alce::1366__wikidata_simple__dev::p8

### `738__wikidata_simple__dev`
> **Multiple players were drafted by the Minnesota Timberwolves, including Pooh Richardson, Kevin Garnett, Ray Allen, O.J. Mayo, Doug West, Ricky Rubio, Josh Okogie, and Karl-Anthony Towns**
> The Timberwolves drafted Pooh Richardson with their first ever draft pick, tenth overall, in the 1989 NBA draft. [alce::738__wikidata_simple__dev::p0]
> In 1995, the Timberwolves picked Kevin Garnett fifth overall, who went on to be a 13-time All-Star. [alce::738__wikidata_simple__dev::p0]
> In 1996, the Timberwolves drafted Ray Allen fifth overall but was traded to the Milwaukee Bucks. [alce::738__wikidata_simple__dev::p0]
> In the 2008 NBA draft, the Timberwolves drafted O. J. Mayo third overall but was traded to the Memphis Grizzlies. [alce::738__wikidata_simple__dev::p0]
> Doug West was selected by the Minnesota Timberwolves in the second round of the 1989 NBA Draft. [alce::738__wikidata_simple__dev::p86]
> Spanish teenager Ricky Rubio was drafted 5th by the Minnesota Timberwolves. [alce::738__wikidata_simple__dev::p33]
> Josh Okogie was drafted by the Minnesota Timberwolves with the 20th overall pick in the 2018 NBA draft. [alce::738__wikidata_simple__dev::p21]
> Karl-Anthony Towns was selected No. 1 by Minnesota in the draft. [alce::738__wikidata_simple__dev::p69]

Cited: alce::738__wikidata_simple__dev::p0, alce::738__wikidata_simple__dev::p21, alce::738__wikidata_simple__dev::p33, alce::738__wikidata_simple__dev::p69, alce::738__wikidata_simple__dev::p86

### `640__wikidata_simple__dev`
> **Ganga Maiyya Tohe Piyari Chadhaibo**
> The first Bhojpuri talkie film, "Ganga Maiyya Tohe Piyari Chadhaibo", was released in 1963 by Vishwanath Shahabadi. [alce::640__wikidata_simple__dev::p0]
> "Nadiya Ke Paar" is one of the best-known Bhojpuri-language movies. [alce::640__wikidata_simple__dev::p5]

Cited: alce::640__wikidata_simple__dev::p0, alce::640__wikidata_simple__dev::p5

### `466__wikidata_intersection__dev`
> **Attakathi**
> He made his debut as an independent music director in the 2012 Tamil film "Attakathi" directed by Pa. Ranjith. [alce::466__wikidata_intersection__dev::p70]
> He got the opportunity through its producer C. V. Kumar who saw him working in his studio. [alce::466__wikidata_intersection__dev::p70]

Cited: alce::466__wikidata_intersection__dev::p70

### `368__wikidata_comp__dev`
> **American**
> Meyers Patrick Leonard is an American professional basketball player for the Portland Trail Blazers who was selected by the Trail Blazers with the 11th overall pick in the 2012 NBA draft. [alce::368__wikidata_comp__dev::p20]

Cited: alce::368__wikidata_comp__dev::p20

### `349__wikidata_intersection__dev`
> **Battle for the Planet of the Apes**
> "Battle for the Planet of the Apes" was the second-to-last film produced by Arthur P. Jacobs. [alce::349__wikidata_intersection__dev::p11]
> The film was directed by J. Lee Thompson, who was unhappy with both the script and the scope of the production. [alce::349__wikidata_intersection__dev::p11]

Cited: alce::349__wikidata_intersection__dev::p11

### `863__wikidata_simple__dev`
> **Owned and managed the Nagoya Expressway network**
> The Nagoya Expressway is a network of urban expressways in Japan serving the greater Nagoya area. It is owned and managed by Nagoya Expressway Public Corporation. [alce::863__wikidata_simple__dev::p0]
> The Ring Route, which is part of the Nagoya Expressway network, is owned and operated by Nagoya Expressway Public Corporation. [alce::863__wikidata_simple__dev::p8]

Cited: alce::863__wikidata_simple__dev::p0, alce::863__wikidata_simple__dev::p8

### `883__wikidata_simple__dev`
> **David Boaz and Doug Bandow are employed by the Cato Institute**
> David Boaz is the executive vice president of the Cato Institute, an American libertarian think tank. [alce::883__wikidata_simple__dev::p14]
> Doug Bandow is an American political writer, currently working as a Senior Fellow at the Cato Institute. [alce::883__wikidata_simple__dev::p84]

Cited: alce::883__wikidata_simple__dev::p14, alce::883__wikidata_simple__dev::p84

### `520__wikitables_simple__dev`
> **Katyusha, T34 Calliope, bazooka, RPG, Type 4 20 cm rocket launcher, Type 4 40 cm rocket launcher, BM-27 Uragan, M270 Multiple Launch Rocket System**
> Soviet 'Katyusha' was a self-propelled system, being mounted on trucks, tanks and even trains, and the United States Army deployed the tank mounted T34 Calliope system late in the war. [alce::520__wikitables_simple__dev::p0]
> The rocket launchers category includes shoulder-fired weapons such as bazooka and RPG, which are specific types of rocket launchers. [alce::520__wikitables_simple__dev::p0]
> The Type 4 20 cm rocket launcher was a 203 mm rocket mortar used by the Imperial Japanese Army in the final stages of World War II. [alce::520__wikitables_simple__dev::p56]
> The Type 4 40 cm rocket launcher was a rocket used by the Imperial Japanese Army in the final stages of World War II. [alce::520__wikitables_simple__dev::p78]
> Examples of modern surface-to-surface rocket systems include the BM-27 Uragan and M270 Multiple Launch Rocket System. [alce::520__wikitables_simple__dev::p23]

Cited: alce::520__wikitables_simple__dev::p0, alce::520__wikitables_simple__dev::p23, alce::520__wikitables_simple__dev::p56, alce::520__wikitables_simple__dev::p78

### `833__wikidata_simple__dev`
> **Atari 7800**
> Atari Corporation was an American manufacturer of computers and video game consoles from 1984 to 1996, with chief products including the Atari ST, Atari 7800, Atari Lynx, and Atari Jaguar. [alce::833__wikidata_simple__dev::p6]

Cited: alce::833__wikidata_simple__dev::p6

### `454__wikidata_intersection__dev`
> **Premier League and European competitions (Champions League, UEFA Cup/Europa League, Cup Winners' Cup)**
> Manchester City has participated in the Premier League, European Cup (now the Champions League), UEFA Cup (now the Europa League), and Cup Winners' Cup. [alce::454__wikidata_intersection__dev::p0, alce::454__wikidata_intersection__dev::p78]
> Newcastle United F.C. participated in the FA Premier League during the 2002-03 season and has also competed in European competitions including the Champions League, Cup Winners' Cup, and Inter-Cities Fairs Cup. [alce::454__wikidata_intersection__dev::p10, alce::454__wikidata_intersection__dev::p2]
> Both clubs have competed in the Premier League and European competitions. [alce::454__wikidata_intersection__dev::p10, alce::454__wikidata_intersection__dev::p78]

Cited: alce::454__wikidata_intersection__dev::p0, alce::454__wikidata_intersection__dev::p10, alce::454__wikidata_intersection__dev::p2, alce::454__wikidata_intersection__dev::p78

### `847__wikidata_simple__dev`
> **Tricasses**
> The inhabitants of the region of Aube were the Tricasses and Lingones with a substantial human settlement around the year 400 BC. [alce::847__wikidata_simple__dev::p18]

Cited: alce::847__wikidata_simple__dev::p18

### `160__wikidata_comp__dev`
_Refused._

### `525__wikitables_simple__dev`
> **Motorcycle-related clubs include brand-specific clubs, riding-type clubs, women's clubs, charity organizations, and special interest groups**
> The Harley Owners Group is a brand club, and there are also large national independent motorcycle clubs such as the BMW Motorcycle Owners of America. [alce::525__wikitables_simple__dev::p0]
> Specific clubs exist for women, such as Women's International Motorcycle Association, and clubs for lesbians and gays, such as Dykes on Bikes. [alce::525__wikitables_simple__dev::p0]
> Clubs catering for vintage machines include the Vintage Motor Cycle Club, and clubs catering for riders' rights include the Motorcycle Action Group. [alce::525__wikitables_simple__dev::p0]
> Charities like The Royal British Legion Riders Branch are also popular motorcycle-related organizations. [alce::525__wikitables_simple__dev::p0]
> Example motorcycle clubs include American Motorcyclist Association, Harley Owners Group, and BMW MOA, with some organizations like Bikers Against Child Abuse existing primarily as social benefit organizations. [alce::525__wikitables_simple__dev::p2]
> Religiously oriented clubs include the Christian Motorcyclists Association, and law enforcement-specific clubs include the Blue Knights Law Enforcement Motorcycle Club. [alce::525__wikitables_simple__dev::p3]
> Organizations like the Patriot Guard Riders provide funeral escorts for military veterans, and Rolling Thunder advocates for troops missing in action and prisoners of war. [alce::525__wikitables_simple__dev::p6]

Cited: alce::525__wikitables_simple__dev::p0, alce::525__wikitables_simple__dev::p2, alce::525__wikitables_simple__dev::p3, alce::525__wikitables_simple__dev::p6

### `521__wikitables_simple__dev`
> **An archivist is an information professional who assesses, collects, organizes, preserves, maintains control over, and provides access to records and archives**
> An archivist is an information professional who assesses, collects, organizes, preserves, maintains control over, and provides access to records and archives determined to have long-term value. [alce::521__wikitables_simple__dev::p0]
> The records maintained by an archivist can consist of a variety of forms, including letters, diaries, logs, other personal documents, government documents, sound and/or picture recordings, digital files, or other physical objects. [alce::521__wikitables_simple__dev::p0]

Cited: alce::521__wikitables_simple__dev::p0

### `909__wikidata_simple__dev`
> **The Pittsburgh Pirates won the World Series in 1960, 1971, and 1979**
> The Pittsburgh Pirates won the 1960 World Series, defeating the New York Yankees 4-3, with the series-winning home run hit by Mazeroski. [alce::909__wikidata_simple__dev::p34, alce::909__wikidata_simple__dev::p49]
> The Pittsburgh Pirates won the 1971 World Series over the Baltimore Orioles 4-3. [alce::909__wikidata_simple__dev::p18]
> The Pittsburgh Pirates won the 1979 World Series over the Baltimore Orioles 4-3, after falling behind three games to one. [alce::909__wikidata_simple__dev::p3, alce::909__wikidata_simple__dev::p88]

Cited: alce::909__wikidata_simple__dev::p18, alce::909__wikidata_simple__dev::p3, alce::909__wikidata_simple__dev::p34, alce::909__wikidata_simple__dev::p49, alce::909__wikidata_simple__dev::p88

### `1102__wikidata_intersection__dev`
_Refused._

### `783__wikidata_simple__dev`
> **Cinergi Pictures produced multiple films including Tombstone, Die Hard with a Vengeance, Evita, Medicine Man, Renaissance Man, Color of Night, Judge Dredd, The Scarlet Letter, and Nixon**
> The company had a number of major hit films, most notably "Tombstone", "Die Hard with a Vengeance" and "Evita". [alce::783__wikidata_simple__dev::p0]
> Cinergi's first production, "Medicine Man" starring Oscar-winner Sean Connery, was followed by other releases including "Renaissance Man", "Color of Night", "Judge Dredd", "The Scarlet Letter", and "Nixon". [alce::783__wikidata_simple__dev::p6, alce::783__wikidata_simple__dev::p8]

Cited: alce::783__wikidata_simple__dev::p0, alce::783__wikidata_simple__dev::p6, alce::783__wikidata_simple__dev::p8

### `850__wikidata_simple__dev`
> **Myanmar Economic Corporation and Myanmar Airways International**
> The Myanmar Economic Corporation is one of the two major conglomerates and holding companies operated by the Burmese military, with its headquarters located on Ahlon Road in Yangon's Ahlon Township. [alce::850__wikidata_simple__dev::p17]
> Myanmar Airways International is a privately owned airline headquartered in Yangon, Myanmar. [alce::850__wikidata_simple__dev::p22]

Cited: alce::850__wikidata_simple__dev::p17, alce::850__wikidata_simple__dev::p22

### `1001__wikidata_comp__dev`
> **A.C. Milan, Liverpool F.C., Barcelona, Arsenal, Real Madrid, Valencia, Manchester United, Chelsea**
> A.C. Milan and Liverpool F.C. were finalists in the 2007 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p3]
> Barcelona and Arsenal were finalists in the 2006 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p41]
> Real Madrid and Valencia were finalists in the 1999-2000 UEFA Champions League Final. [alce::1001__wikidata_comp__dev::p27]
> Barcelona won the 2009 UEFA Champions League Final against Manchester United. [alce::1001__wikidata_comp__dev::p28]

Cited: alce::1001__wikidata_comp__dev::p27, alce::1001__wikidata_comp__dev::p28, alce::1001__wikidata_comp__dev::p3, alce::1001__wikidata_comp__dev::p41

### `956__wikidata_comp__dev`
> **Fort Leavenworth, Kansas and Carlisle Barracks, Pennsylvania**
> A US Army Chief of Staff attended the Army Command and General Staff School at Fort Leavenworth, Kansas, in 1935 and the Army War College at Carlisle Barracks, Pennsylvania, in 1937. [alce::956__wikidata_comp__dev::p89]

Cited: alce::956__wikidata_comp__dev::p89

### `975__wikidata_comp__dev`
> **Shashi Kapoor directed "Ajooba" (1991)**
> In 1991, he produced and directed a fantasy film titled 'Ajooba' [alce::975__wikidata_comp__dev::p12]

Cited: alce::975__wikidata_comp__dev::p12

### `596__wikidata_simple__dev`
_Refused._

### `436__wikidata_intersection__dev`
> **The Prestige and Interstellar**
> Nolan directed, co-wrote, and produced "The Prestige" (2006), an adaptation of the Christopher Priest novel about two rival 19th-century magicians. [alce::436__wikidata_intersection__dev::p0]
> Nolan also directed, wrote, and produced the science-fiction film "Interstellar" (2014). [alce::436__wikidata_intersection__dev::p6]

Cited: alce::436__wikidata_intersection__dev::p0, alce::436__wikidata_intersection__dev::p6

### `57__wikitables_composition__dev`
_Refused._

### `389__wikidata_comp__dev`
> **McG**
> Stephanie Savage moved to Los Angeles and in 1995 was offered a position at Drew Barrymore's production company Flower Films, where she handled production rewrites for 'Charlie's Angels' and met the film's director McG. [alce::389__wikidata_comp__dev::p1]
> Stephanie Savage and McG later formed production company Wonderland Sound and Vision in 2001. [alce::389__wikidata_comp__dev::p1]

Cited: alce::389__wikidata_comp__dev::p1

### `186__wikidata_intersection__dev`
> **European Cup Winners' Cup (1969-70)**
> Manchester City are one of twelve English football clubs to have won a European title, in City's case the 1969–70 Cup Winners Cup. [alce::186__wikidata_intersection__dev::p2]
> By winning the competition, Manchester City earned the right to compete in the 1969–70 European Cup Winners' Cup. [alce::186__wikidata_intersection__dev::p52]
> The club has won five league titles, five FA Cups, five League Cups, five FA Community Shields, and one European Cup Winners' Cup. [alce::186__wikidata_intersection__dev::p20]

Cited: alce::186__wikidata_intersection__dev::p2, alce::186__wikidata_intersection__dev::p20, alce::186__wikidata_intersection__dev::p52

### `745__wikidata_simple__dev`
> **Scottish people/Scots**
> Scots remained the vernacular of many rural communities and the growing number of urban working-class Scots. [alce::745__wikidata_simple__dev::p10]
> The Scottish people (Scots: "Scots Fowk"; Scottish Gaelic: "Albannaich") or Scots, are a nation and ethnic group native to Scotland. [alce::745__wikidata_simple__dev::p5]

Cited: alce::745__wikidata_simple__dev::p10, alce::745__wikidata_simple__dev::p5

### `822__wikidata_simple__dev`
> **Rohana Weerasinghe composed "Ekasitha dethanaka", "Hiruta Horen", and "Punchi Sithe Punchi Sina", among over 4000 songs for films, teledramas, and stage plays**
> He composed T. M. Jayaratne's "Ekasitha dethanaka", "Hiruta Horen" and Neela Wickramasinghe's "Punchi Sithe Punchi Sina" which became popular songs in Sri Lanka. [alce::822__wikidata_simple__dev::p0]
> So far he has created melodies for over 4000 songs, which includes films, teledramas, stage plays. [alce::822__wikidata_simple__dev::p0]

Cited: alce::822__wikidata_simple__dev::p0

### `485__wikitables_simple__dev`
> **Adolf Meyer**
> Adolf Meyer was a psychiatrist who rose to prominence as the first psychiatrist-in-chief of the Johns Hopkins Hospital (1910-1941). [alce::485__wikitables_simple__dev::p43]
> He was president of the American Psychiatric Association in 1927–28 and was one of the most influential figures in psychiatry in the first half of the twentieth century. [alce::485__wikitables_simple__dev::p43]

Cited: alce::485__wikitables_simple__dev::p43

### `401__wikidata_comp__dev`
> **coins**
> Charles Edward Barber was the sixth Chief Engraver of the United States Mint from 1879 until his death in 1917, and he designed most of the coins produced at the mint during his time as Chief Engraver. [alce::401__wikidata_comp__dev::p0]
> The Barber coinage were named after him, and he designed a number of commemorative coins. [alce::401__wikidata_comp__dev::p0]
> The Barber dime is named for its designer, Charles E. Barber, who was Chief Engraver of the U.S. Mint from 1879 to 1917. [alce::401__wikidata_comp__dev::p13]

Cited: alce::401__wikidata_comp__dev::p0, alce::401__wikidata_comp__dev::p13

### `717__wikidata_simple__dev`
> **Franco Donatoni, Aldo Clementi, Cornelius Cardew, Ennio Morricone, Karl Korte, Boris Porena, Norma Beecroft, Mario Bertoncini, Ernesto Rubin de Cervin, Eric Salzman, Kenneth Leighton, Peter Maxwell Davies, Michael Dellaira, Armando Santiago, and Richard Teitelbaum**
> Petrassi had many famous students, including Franco Donatoni, Aldo Clementi, Cornelius Cardew, Ennio Morricone, Karl Korte, Boris Porena, Norma Beecroft, Mario Bertoncini, Ernesto Rubin de Cervin, Eric Salzman, Kenneth Leighton, Peter Maxwell Davies, Michael Dellaira, Armando Santiago, and Richard Teitelbaum. [alce::717__wikidata_simple__dev::p1]

Cited: alce::717__wikidata_simple__dev::p1

### `141__wikidata_intersection__dev`
> **Multiple Super Bowls including Super Bowl XL, Super Bowl XLIII, and Super Bowl XLV**
> The Pittsburgh Steelers have won 6 Super Bowl titles and competed in multiple Super Bowls throughout their history. [alce::141__wikidata_intersection__dev::p40]
> The Steelers won Super Bowl XL and Super Bowl XLIII, and lost Super Bowl XLV. [alce::141__wikidata_intersection__dev::p8]
> The Steelers competed in a Super Bowl against the Dallas Cowboys in Miami, winning 21-17. [alce::141__wikidata_intersection__dev::p28]
> Super Bowl XLIII was played on February 1, 2009, where the Pittsburgh Steelers defeated the Arizona Cardinals 27-23, becoming the first team to win six Super Bowl championships. [alce::141__wikidata_intersection__dev::p7]

Cited: alce::141__wikidata_intersection__dev::p28, alce::141__wikidata_intersection__dev::p40, alce::141__wikidata_intersection__dev::p7, alce::141__wikidata_intersection__dev::p8

### `590__wikidata_simple__dev`
> **Prentis House, The Salt Box, and Montgomery Saltbox Houses**
> The Prentis House, built in 1773 in Hadley, Massachusetts by the Dickinson family, is typical of the indigenous style of Saltbox architecture that developed in New England during the Colonial period. [alce::590__wikidata_simple__dev::p9]
> The Salt Box was a house built in the 1880s in the Bunker Hill section of Los Angeles, California, designed in the saltbox style that was popularized in New England. [alce::590__wikidata_simple__dev::p0]
> The Montgomery Saltbox Houses are a pair of historic saltbox houses in Montgomery, Ohio, United States, built in 1800. [alce::590__wikidata_simple__dev::p3]

Cited: alce::590__wikidata_simple__dev::p0, alce::590__wikidata_simple__dev::p3, alce::590__wikidata_simple__dev::p9

### `953__wikidata_comp__dev`
> **Nashville, Tennessee**
> SouthComm Communications was a media company that owned a number of alternative newspapers and other news sources in the United States such as the 'Nashville Scene' and 'Washington City Paper'. It was based in Nashville, Tennessee. [alce::953__wikidata_comp__dev::p31]

Cited: alce::953__wikidata_comp__dev::p31

### `918__wikidata_simple__dev`
_Refused._

### `694__wikidata_simple__dev`
> **Multiple officials and military leaders worked for the Western Roman Empire, including Olympius, Stilicho, Constantius, Aëtius, Ricimer, Orestes, Julius Nepos, and Theoderic**
> Olympius was a minister of the Western Roman Empire, in the court of the emperor Honorius. [alce::694__wikidata_simple__dev::p84]
> Military strongmen who took the title of 'magister militum', 'patrician' or both ruled the Western Roman Empire, including Stilicho from 395 to 408, Constantius from about 411 to 421, Aëtius from 433 to 454 and Ricimer from about 457 to 472. [alce::694__wikidata_simple__dev::p17]
> From 468 CE, the Province was ruled by Julius Nepos, who was appointed Western Emperor in 473 CE by Leo I of the Eastern Court. [alce::694__wikidata_simple__dev::p16]
> Theoderic acted as a subordinate in domestic affairs of the Western Roman Empire, with administrative positions staffed by Romans and the army exclusively staffed by Goths. [alce::694__wikidata_simple__dev::p30]

Cited: alce::694__wikidata_simple__dev::p16, alce::694__wikidata_simple__dev::p17, alce::694__wikidata_simple__dev::p30, alce::694__wikidata_simple__dev::p84

### `601__wikidata_simple__dev`
> **HMCS Halifax, HMCS Goose Bay, and HMCS Glace Bay**
> HMCS Halifax (FFH 330) is assigned to Maritime Forces Atlantic (MARLANT) and is homeported at CFB Halifax in Halifax, Nova Scotia. [alce::601__wikidata_simple__dev::p7]
> HMCS Goose Bay is a coastal defence vessel assigned to Maritime Forces Atlantic (MARLANT) and is homeported at CFB Halifax. [alce::601__wikidata_simple__dev::p60]
> HMCS Glace Bay is assigned to Maritime Forces Atlantic (MARLANT) and is homeported at CFB Halifax. [alce::601__wikidata_simple__dev::p79]

Cited: alce::601__wikidata_simple__dev::p60, alce::601__wikidata_simple__dev::p7, alce::601__wikidata_simple__dev::p79

### `691__wikidata_simple__dev`
> **Sukhoi Su-57**
> The Sukhoi Su-57 is a stealth, single-seat, twin-engine multirole fifth-generation jet fighter being developed for air superiority and attack operations. [alce::691__wikidata_simple__dev::p59]
> Sukhoi also produces military aircraft models including the Su-27, Su-30 and Su-35, and on the civilian segment, the company's most important project is the Superjet 100. [alce::691__wikidata_simple__dev::p5]

Cited: alce::691__wikidata_simple__dev::p5, alce::691__wikidata_simple__dev::p59

### `860__wikidata_simple__dev`
> **19 PhD students including Alex Bateman, Steven E. Brenner, Mark Bender Gerstein, Julian Gough, Sarah Teichmann, Bissan Al-Lazikani, Goga Apic, Samantha Barré Matthew Bashton, Dan Bolser, Michael Bremang, Bernard de Bono, Emma Ganley, Martin Madera, Siarhei Maslau, Susan Miller, Jong Park, Rajkumar Sasidharan, and Christine Vogel**
> During his career, Chothia supervised 19 successful PhD students to completion including Alex Bateman, Steven E. Brenner, Mark Bender Gerstein, Julian Gough, Sarah Teichmann, Bissan Al-Lazikani, Goga Apic, Samantha Barré Matthew Bashton, Dan Bolser, Michael Bremang, Bernard de Bono, Emma Ganley (née Hill), Martin Madera, Siarhei Maslau, Susan Miller, Jong Park (aka Jong Bhak), Rajkumar Sasidharan, and Christine Vogel. [alce::860__wikidata_simple__dev::p2]

Cited: alce::860__wikidata_simple__dev::p2

### `490__wikitables_simple__dev`
> **Sex worker organizations include COYOTE, North American Task Force on Prostitution, Scarlet Alliance, International Committee for Prostitutes' Rights, SWAI, BAYSWAN, International Union of Sex Workers (IUSW), SISTERS, M Plus, and APNSW**
> In the United States of America, one such group is COYOTE (an abbreviation for "Call Off Your Old Tired Ethics") and another is the North American Task Force on Prostitution. [alce::490__wikitables_simple__dev::p13]
> In Australia the lead sex worker rights organisation is Scarlet Alliance. [alce::490__wikitables_simple__dev::p13]
> International prostitutes' rights organizations include the International Committee for Prostitutes' Rights and the Network of [alce::490__wikitables_simple__dev::p13]
> The "Sex Workers Alliance Ireland" (SWAI) was established in 2009. [alce::490__wikitables_simple__dev::p3]
> BAYSWAN is a non-profit organization for sex workers in the San Francisco Bay Area. [alce::490__wikitables_simple__dev::p3]
> One of the largest is the International Union of Sex Workers, headquartered in the United Kingdom. [alce::490__wikitables_simple__dev::p12]
> The newly formed organisation SISTERS works with transgender sex workers in Bangkok and Pattaya. [alce::490__wikitables_simple__dev::p26]
> M Plus is an organization for male sex workers in Chiang Mai, including men who identify as gay, straight or transgender. [alce::490__wikitables_simple__dev::p26]
> The Asia Pacific Network of Sex Workers (APNSW) is a regional organization, headquartered in Thailand, of sex worker led organizations. [alce::490__wikitables_simple__dev::p26]

Cited: alce::490__wikitables_simple__dev::p12, alce::490__wikitables_simple__dev::p13, alce::490__wikitables_simple__dev::p26, alce::490__wikitables_simple__dev::p3

### `250__wikidata_comp__dev`
_Refused._

### `776__wikidata_simple__dev`
> **Howard Friedman**
> Howard Steven Friedman is a prominent American statistician, health economist, writer and artist currently employed at the United Nations Population Fund (UNFPA) and as an adjunct Associate Professor at Columbia University. [alce::776__wikidata_simple__dev::p40]

Cited: alce::776__wikidata_simple__dev::p40

### `316__wikidata_comp__dev`
> **Geoff Barrow and Salisbury**
> Together with Geoff Barrow, he scored the feature film 'Ex Machina', Alex Garland's directorial debut, released in the UK in January 2015. [alce::316__wikidata_comp__dev::p2]
> Salisbury and Barrow won the 2016 Ivor Novello award for Best Original Score for 'Ex Machina'. [alce::316__wikidata_comp__dev::p2]

Cited: alce::316__wikidata_comp__dev::p2

### `608__wikidata_simple__dev`
> **Paintings with Victorine Meurent include "The Luncheon on the Grass," "Olympia," "Gare Saint-Lazare," and works by Edgar Degas and Alfred Stevens**
> Victorine Meurent became a painter herself after posing for several works, including two of the most infamous: "Manet's Olympia" and "Le déjeuner sur l'herbe". [alce::608__wikidata_simple__dev::p34]
> Her name remains forever associated with Manet's masterpieces of 1863, "The Luncheon on the Grass" and "Olympia", which include nude portrayals of her. [alce::608__wikidata_simple__dev::p3]
> At that time she also modeled for Edgar Degas and the Belgian painter Alfred Stevens, both close friends of Manet. [alce::608__wikidata_simple__dev::p3]
> The last Manet painting in which Meurent appears is "Gare Saint-Lazare". [alce::608__wikidata_simple__dev::p3]

Cited: alce::608__wikidata_simple__dev::p3, alce::608__wikidata_simple__dev::p34

### `733__wikidata_simple__dev`
> **New Police Story**
> New Police Story is a 2004 Hong Kong action film produced and directed by Benny Chan. [alce::733__wikidata_simple__dev::p19]
> Who Am I? is a 1998 Hong Kong action comedy film directed by Benny Chan and Jackie Chan. [alce::733__wikidata_simple__dev::p83]

Cited: alce::733__wikidata_simple__dev::p19, alce::733__wikidata_simple__dev::p83

### `970__wikidata_comp__dev`
> **University of Oxford**
> Ian Chubb was the Chief Scientist of Australia from 23 May 2011 to 22 January 2016 and has a DPhil from the University of Oxford. [alce::970__wikidata_comp__dev::p24]

Cited: alce::970__wikidata_comp__dev::p24

### `163__wikidata_intersection__dev`
> **Pattanapravesham**
> Pattanapravesham is a 1988 Malayalam screwball comedy film directed by Sathyan Anthikkad and written by Sreenivasan. [alce::163__wikidata_intersection__dev::p56]

Cited: alce::163__wikidata_intersection__dev::p56

### `415__wikidata_comp__dev`
_Refused._

### `442__wikidata_intersection__dev`
> **Taça de Portugal**
> S.L. Benfica and Sporting CP participated in the Taça de Portugal, where they faced each other in the sixth round. [alce::442__wikidata_intersection__dev::p1]
> In a highly entertaining 3–3 game, the tie went to penalties which saw Benfica defeat Sporting CP 7–6 on penalties. [alce::442__wikidata_intersection__dev::p1]

Cited: alce::442__wikidata_intersection__dev::p1

### `710__wikidata_simple__dev`
> **The Nimrod**
> Fantagraphics has additionally published a range of shorter pieces by Trondheim in the comic 'The Nimrod'. [alce::710__wikidata_simple__dev::p0]

Cited: alce::710__wikidata_simple__dev::p0

### `765__wikidata_simple__dev`
> **Isaac Asimov edited approximately 147 books across various genres including science fiction anthologies**
> Isaac Asimov was a prolific writer who wrote or edited more than 500 books and an estimated 90,000 letters and postcards. [alce::765__wikidata_simple__dev::p20]
> In a writing career spanning 53 years (1939–1992), science fiction and popular science author Isaac Asimov wrote and published 40 novels, 382 short stories, over 280 non-fiction books, and edited about 147 others. [alce::765__wikidata_simple__dev::p16]
> Asimov edited works including 'Isaac Asimov's Aliens & Outworlders' (1983), 'Isaac Asimov's Space of Her Own' (1984) and 'Isaac Asimov's Fantasy!' (1985). [alce::765__wikidata_simple__dev::p13]

Cited: alce::765__wikidata_simple__dev::p13, alce::765__wikidata_simple__dev::p16, alce::765__wikidata_simple__dev::p20

### `361__wikidata_intersection__dev`
_Refused._

### `536__wikitables_simple__dev`
> **Captain Sir John Franklin**
> Franklin's lost expedition was a British voyage of Arctic exploration led by Captain Sir John Franklin that departed England in 1845 aboard two ships. [alce::536__wikitables_simple__dev::p5]
> A Royal Navy officer and experienced explorer, Franklin had served on three previous Arctic expeditions, the latter two as commanding officer. [alce::536__wikitables_simple__dev::p5]

Cited: alce::536__wikitables_simple__dev::p5

### `138__wikidata_intersection__dev`
> **Wonder Woman**
> Queen Hippolyta is a fictional DC Comics superhero, based on the Amazon queen Hippolyta from Greek mythology. She is the queen of the Amazons of Themyscira, and the mother of Wonder Woman. [alce::138__wikidata_intersection__dev::p13]
> The Amazons of DC Comics are a race of warrior women who exist as part of Greek mythology and live on Paradise Island (also known as Themyscira), an isolated location in the middle of the ocean. [alce::138__wikidata_intersection__dev::p1]

Cited: alce::138__wikidata_intersection__dev::p1, alce::138__wikidata_intersection__dev::p13

### `641__wikidata_simple__dev`
_Refused._

### `219__wikidata_comp__dev`
> **William Pine and William C. Thomas**
> Pine-Thomas Productions was a prolific B-picture unit of Paramount Pictures from 1940–1957, producing 81 films, co-produced by William H. Pine and William C. Thomas. [alce::219__wikidata_comp__dev::p1]
> William Pine directed 'Aerial Gunner' - it was his first feature, although he had directed several wartime propaganda shorts. [alce::219__wikidata_comp__dev::p7]
> Pine and Thomas were both directing films by this stage. [alce::219__wikidata_comp__dev::p0]

Cited: alce::219__wikidata_comp__dev::p0, alce::219__wikidata_comp__dev::p1, alce::219__wikidata_comp__dev::p7

### `556__wikidata_simple__dev`
> **Multiple films including "Keep Fit", "The Captain's Paradise", "Smiley", "Mine Own Executioner", "Bonnie Prince Charlie", "Mr. Denning Drives North", and "The Amorous Prawn"**
> His first directorial assignment was "Keep Fit". [alce::556__wikidata_simple__dev::p0]
> After the war he produced an eclectic mix of films, such as the psychological thriller "Mine Own Executioner" (1947), "Bonnie Prince Charlie" (1948) and "Mr. Denning Drives North" (1951). [alce::556__wikidata_simple__dev::p2]
> In the 1950s Kimmin's work included the Sir Alec Guinness comedy "The Captain's Paradise" and the children's "Smiley" series of films. [alce::556__wikidata_simple__dev::p2]
> His final film harked back to his early days – it was "The Amorous Prawn" (1962). [alce::556__wikidata_simple__dev::p2]

Cited: alce::556__wikidata_simple__dev::p0, alce::556__wikidata_simple__dev::p2

### `126__wikidata_intersection__dev`
> **2007 Canadian Grand Prix and 2010 Canadian Grand Prix**
> The 2007 Canadian Grand Prix was a Formula One motor race held on 10 June 2007 at Circuit Gilles Villeneuve in Montreal, Quebec, Canada. The race was won by Lewis Hamilton, starting from pole position, in his first season in the top formula. [alce::126__wikidata_intersection__dev::p0]
> The 2010 Canadian Grand Prix was held in Montreal, Quebec, Canada at the Circuit Gilles Villeneuve on 13 June 2010. The race was won by McLaren driver Lewis Hamilton, his second Canadian Grand Prix victory. [alce::126__wikidata_intersection__dev::p4]

Cited: alce::126__wikidata_intersection__dev::p0, alce::126__wikidata_intersection__dev::p4

### `155__wikidata_comp__dev`
> **T. Rajender (who shot the whole film, though E. M. Ibrahim was officially credited as director)**
> The film's producer E. M. Ibrahim agreed to produce this film on the basis of one condition that Ibrahim himself will be credited as director while Rajender would be credited as the film's screenwriter and music composer. [alce::155__wikidata_comp__dev::p0]
> During the shoot, since Ibrahim had no prior experience of film direction, Rajender shot the whole film. [alce::155__wikidata_comp__dev::p0]
> The music was composed by T. Rajendar and the background score is worked upon by A. A. Raj. [alce::155__wikidata_comp__dev::p0]

Cited: alce::155__wikidata_comp__dev::p0

### `686__wikidata_simple__dev`
> **Canada, Great Britain and Northern Ireland, and the United States**
> Canada competed at the 2017 World Championships in Athletics in London, United Kingdom, 4–13 August 2017. [alce::686__wikidata_simple__dev::p2]
> Great Britain and Northern Ireland competed at the 2017 IAAF World Championships in London, from 4–13 August 2017. [alce::686__wikidata_simple__dev::p18]
> The United States has competed at every edition of the IAAF World Championships in Athletics since its inception in 1983, and by the end of the 2017 World Championships in Athletics its athletes had won a total of 352 medals. [alce::686__wikidata_simple__dev::p5]

Cited: alce::686__wikidata_simple__dev::p18, alce::686__wikidata_simple__dev::p2, alce::686__wikidata_simple__dev::p5

### `886__wikidata_simple__dev`
> **Major League Baseball games and competitions**
> The Chicago Cubs are an American professional baseball team based in Chicago, Illinois that compete in Major League Baseball (MLB) as a member club of the National League (NL) Central division. [alce::886__wikidata_simple__dev::p0]
> The Cubs have played against the Los Angeles Dodgers in the NLCS (National League Championship Series) in 7 games. [alce::886__wikidata_simple__dev::p66]
> The Brewers and Cubs have been playing each other in spring training Cactus League games as part of the Brewers–Cubs rivalry, a Major League Baseball rivalry between the Milwaukee Brewers and Chicago Cubs. [alce::886__wikidata_simple__dev::p66]

Cited: alce::886__wikidata_simple__dev::p0, alce::886__wikidata_simple__dev::p66

### `472__wikitables_simple__dev`
> **Barrett M107, Zastava M93 Black Arrow, McMillan Tac-50, Gepard GM6 Lynx, AMSD OM 50 Nemesis, Accuracy International AS50, Mechem NTW-20, Gepárd M1, IST-14.5, WKW Wilk, CheyTac Intervention M-200, Denel NTW-20**
> The Barrett M107 is a popular anti-materiel rifle used for both military and civilian purposes, featuring a .50 BMG caliber bullet. [alce::472__wikitables_simple__dev::p4]
> Other popular anti-materiel rifles include the Zastava M93 Black Arrow, McMillan Tac-50, Gepard GM6 Lynx, AMSD OM 50 Nemesis, Accuracy International AS50, Mechem NTW-20, and IST-14.5. [alce::472__wikitables_simple__dev::p1, alce::472__wikitables_simple__dev::p4]
> The Gepárd anti-materiel rifles are a family of Hungarian weapons designed to destroy unarmored and lightly armored targets. [alce::472__wikitables_simple__dev::p9]
> The WKW Wilk and CheyTac Intervention M-200 are also classified as anti-materiel rifles. [alce::472__wikitables_simple__dev::p1]
> The Denel NTW-20 is a South African anti-materiel rifle developed by Denel Mechem in the 1990s. [alce::472__wikitables_simple__dev::p40]

Cited: alce::472__wikitables_simple__dev::p1, alce::472__wikitables_simple__dev::p4, alce::472__wikitables_simple__dev::p40, alce::472__wikitables_simple__dev::p9

### `106__wikidata_intersection__dev`
> **Premier League Asia Trophy**
> The Premier League Asia Trophy tournament has featured teams solely from the Premier League, with Manchester City winning in 2013 and Arsenal winning in 2015. [alce::106__wikidata_intersection__dev::p69]
> Both Manchester City and Arsenal are among the most regular participants in the Premier League Asia Trophy, having each contested the tournament on multiple occasions. [alce::106__wikidata_intersection__dev::p69]

Cited: alce::106__wikidata_intersection__dev::p69

### `299__wikidata_intersection__dev`
> **1971 European Cup Winners' Cup Final**
> The 1971 European Cup Winners' Cup Final was a football match contested by Chelsea F.C. of England and Real Madrid of Spain. [alce::299__wikidata_intersection__dev::p85]
> Chelsea scored two goals with Peter Osgood and John Dempsey in the first half. Real's Sebastián Fleitas scored 15 minutes before the end of the game but Chelsea hung on to win 2–1 and become the third London club to win the trophy. [alce::299__wikidata_intersection__dev::p85]

Cited: alce::299__wikidata_intersection__dev::p85

### `175__wikidata_intersection__dev`
> **A match between SL Benfica and SC Braga**
> On 19 November, Benfica played Braga, with Benfica scoring first through Anderson but Braga coming back with goals from Césinha and Julio Bevacqua, and Bevacqua giving the win to Braga three minutes after Benfica's Nuno Gomes equalized in the 92nd minute. [alce::175__wikidata_intersection__dev::p84]
> On 25 March, Benfica hosted Braga, with Benfica scoring through Nuno Gomes and retaining their lead until the end. [alce::175__wikidata_intersection__dev::p8]

Cited: alce::175__wikidata_intersection__dev::p8, alce::175__wikidata_intersection__dev::p84

### `152__wikidata_intersection__dev`
> **The film produced by D. Madhusudhana Rao and directed by Adurthi Subba Rao (based on Sharat Chandra Chatterjee's "Nishkruti")**
> The film was produced by Madhusudhana Rao under his own banner Annapurna Pictures and was directed by Adurthi Subba Rao, who also did the editing. [alce::152__wikidata_intersection__dev::p15]
> The story was based on Sharat Chandra Chatterjee's Bengali novel 'Nishkruti'. [alce::152__wikidata_intersection__dev::p15]

Cited: alce::152__wikidata_intersection__dev::p15

### `0__wikitables_composition__dev`
> **Museums in Victoria, British Columbia include the Royal British Columbia Museum, Maritime Museum of British Columbia, British Columbia Aviation Museum, McNamara House, the Nave, Children's Discovery Museum, and Victoria Art Gallery**
> The Royal British Columbia Museum (sometimes referred to as Royal BC Museum) consists of The Province of British Columbia's natural and human history museum as well as the British Columbia Provincial Archives and is located in Victoria, British Columbia, Canada. [alce::0__wikitables_composition__dev::p2]
> Notable museums just outside of Victoria include the Maritime Museum of British Columbia, and the British Columbia Aviation Museum on the north edge of the Victoria International Airport. [alce::0__wikitables_composition__dev::p1]
> Several museums are located in Victoria including the McNamara House (a social history museum), the Nave (art), and the Children's Discovery Museum. [alce::0__wikitables_composition__dev::p8]
> Victoria Art Gallery is located in Victoria, BC. [alce::0__wikitables_composition__dev::p73]

Cited: alce::0__wikitables_composition__dev::p1, alce::0__wikitables_composition__dev::p2, alce::0__wikitables_composition__dev::p73, alce::0__wikitables_composition__dev::p8

### `884__wikidata_simple__dev`
> **Pranayam**
> Blessy is an Indian film director and screenwriter who has made several critically acclaimed Malayalam films. [alce::884__wikidata_simple__dev::p1]
> Blessy scripted the 2011 film 'Pranayam' which includes Mohanlal, Anupam Kher, and Jaya Prada. [alce::884__wikidata_simple__dev::p0, alce::884__wikidata_simple__dev::p3]

Cited: alce::884__wikidata_simple__dev::p0, alce::884__wikidata_simple__dev::p1, alce::884__wikidata_simple__dev::p3

### `908__wikidata_simple__dev`
> **Shrabani Deodhar directed the 1993 feature film "Lapandav" and "Stat Lota"**
> Shrabani Deodhar is a Marathi film director and screenwriter who won the Indian National Film Award for her very first project, the 1993 feature film "Lapandav". [alce::908__wikidata_simple__dev::p0]
> She directed "Stat Lota", a film that was delayed for four years due to personal issues surrounding her husband's death in 2010. [alce::908__wikidata_simple__dev::p1]

Cited: alce::908__wikidata_simple__dev::p0, alce::908__wikidata_simple__dev::p1

### `64__wikitables_composition__dev`
> **Peter Lilley**
> In 2001, Lilley provoked some controversy in his party and Britain more widely by calling for cannabis to be legalised in a Social Market Foundation pamphlet. [alce::64__wikitables_composition__dev::p2]

Cited: alce::64__wikitables_composition__dev::p2

### `624__wikidata_simple__dev`
> **Eitan Ezra and Harrison Hurt**
> Eitan Ezra and Harrison Hurt are alumni of Poly Prep Country Day School, as they were listed as representatives from the school in 2016. [alce::624__wikidata_simple__dev::p42]

Cited: alce::624__wikidata_simple__dev::p42

### `708__wikidata_simple__dev`
> **Nordwind Airlines**
> Nordwind Airlines has its head office within Sheremetyevo International Airport in Molzhaninovsky District. [alce::708__wikidata_simple__dev::p10]

Cited: alce::708__wikidata_simple__dev::p10

### `143__wikidata_comp__dev`
_Refused._

### `474__wikitables_simple__dev`
_Refused._

### `870__wikidata_simple__dev`
> **Othello**
> In 1948, Orson Welles began work on a self-financed film of "Othello", which was not completed until 1952. [alce::870__wikidata_simple__dev::p4]
> Orson Welles was responsible for production as part of the Mercury Theatre, where all offerings bore the credit line 'Production by Orson Welles'. [alce::870__wikidata_simple__dev::p30]

Cited: alce::870__wikidata_simple__dev::p30, alce::870__wikidata_simple__dev::p4

### `45__wikitables_composition__dev`
_Refused._

### `298__wikidata_comp__dev`
_Refused._

### `197__wikidata_intersection__dev`
> **First Reformed**
> First Reformed is a 2017 American drama film written and directed by Paul Schrader. [alce::197__wikidata_intersection__dev::p32]
> The Walker is a 2007 American-British drama film written and directed by Paul Schrader. [alce::197__wikidata_intersection__dev::p35]
> Hardcore is a crime drama written and directed by Paul Schrader. [alce::197__wikidata_intersection__dev::p1]

Cited: alce::197__wikidata_intersection__dev::p1, alce::197__wikidata_intersection__dev::p32, alce::197__wikidata_intersection__dev::p35

### `417__wikidata_comp__dev`
> **Lava Hot Springs High School and Albion State Normal School**
> Terrel Howard Bell was the Secretary of Education in the Cabinet of President Ronald Reagan. [alce::417__wikidata_comp__dev::p19]
> Bell graduated from Lava Hot Springs High School and the Albion State Normal School in 1946. [alce::417__wikidata_comp__dev::p19]

Cited: alce::417__wikidata_comp__dev::p19

### `603__wikidata_simple__dev`
> **Shallow tunnels**
> Cut-and-cover is a simple method of construction for shallow tunnels where a trench is excavated and roofed over with an overhead support system strong enough to carry the load of what is to be built above the tunnel. [alce::603__wikidata_simple__dev::p2]
> The Circle, District, Hammersmith & City, and Metropolitan lines are services that run on the sub-surface network that has railway tunnels just below the surface and built mostly using the 'cut-and-cover' method. [alce::603__wikidata_simple__dev::p3]

Cited: alce::603__wikidata_simple__dev::p2, alce::603__wikidata_simple__dev::p3

### `306__wikidata_intersection__dev`
> **Victorian Football League (VFL) and Australian Football League (AFL)**
> In 1897, Collingwood, along with fellow VFA clubs Fitzroy, Melbourne, St Kilda, Carlton, Essendon, South Melbourne and Geelong split from the VFA and formed the Victorian Football League (VFL). [alce::306__wikidata_intersection__dev::p1]
> Richmond Football Club became the 10th team two weeks later, joining the VFL. [alce::306__wikidata_intersection__dev::p22]
> The Collingwood Football Club is a professional Australian rules football club playing in the Australian Football League (AFL). [alce::306__wikidata_intersection__dev::p71]
> Richmond and Collingwood played against each other in five grand finals between 1919 and 1929, demonstrating their participation in the same competition. [alce::306__wikidata_intersection__dev::p5]

Cited: alce::306__wikidata_intersection__dev::p1, alce::306__wikidata_intersection__dev::p22, alce::306__wikidata_intersection__dev::p5, alce::306__wikidata_intersection__dev::p71

### `35__wikitables_composition__dev`
> **George Town has multiple localities: Tasmania (Australia), Chennai (India), and Exuma (Bahamas)**
> George Town, Tasmania is a large town in north-east Tasmania, on the eastern bank of the mouth of the Tamar River. [alce::35__wikitables_composition__dev::p4]
> George Town, Chennai is a neighbourhood in Chennai city (formerly Madras), Tamil Nadu, India. [alce::35__wikitables_composition__dev::p2]
> George Town is a town in the Bahamas, located on Exuma island. [alce::35__wikitables_composition__dev::p69]

Cited: alce::35__wikitables_composition__dev::p2, alce::35__wikitables_composition__dev::p4, alce::35__wikitables_composition__dev::p69

### `1367__wikidata_simple__dev`
> **Thomas Cocheé worked as a deputy sheriff in the LA County Sheriff's Department**
> After high school, he landed a job with the Los Angeles County Sheriff's Department as a deputy sheriff. [alce::1367__wikidata_simple__dev::p98]
> During the 1965 Watts riot, Cocheé was a sergeant in the Los Angeles County Sheriff's Department. [alce::1367__wikidata_simple__dev::p98]

Cited: alce::1367__wikidata_simple__dev::p98

### `225__wikidata_comp__dev`
> **Andrew Overtoom**
> Andrew Overtoom directed the feature film "My Life with Morrissey", which he also wrote. [alce::225__wikidata_comp__dev::p0, alce::225__wikidata_comp__dev::p16]
> Andrew Overtoom is an American animation director, writer and photographer/cinematographer best known for his work on the Disney animated television series Billy Dilley where he was a writer and animation supervisor. [alce::225__wikidata_comp__dev::p0]

Cited: alce::225__wikidata_comp__dev::p0, alce::225__wikidata_comp__dev::p16

### `682__wikidata_simple__dev`
> **Karuppu Roja**
> Ayngaran International's first production was 'Karuppu Roja' (1996), a horror film directed by Aabavanan. [alce::682__wikidata_simple__dev::p0]
> Ayngaran introduced the six-track DTS sound system to the Indian Cinema Industry through its inaugural production feature Karuppu Roja in 1996. [alce::682__wikidata_simple__dev::p1]

Cited: alce::682__wikidata_simple__dev::p0, alce::682__wikidata_simple__dev::p1

### `267__wikidata_comp__dev`
> **Robert Florey**
> Buckner's first film at Universal was 'Rogues' Regiment' (1948), which he wrote and produced, from a story by Buckner and director Robert Florey. [alce::267__wikidata_comp__dev::p0]

Cited: alce::267__wikidata_comp__dev::p0

### `876__wikidata_simple__dev`
> **Television stations and Mission Broadcasting**
> Nexstar Media Group owns 171 television stations across the U.S., most of whom are affiliates with the four major U.S. television networks located in small to medium-sized markets. [alce::876__wikidata_simple__dev::p0]
> The company also operates all of the stations owned by an affiliated company, Mission Broadcasting, under local marketing agreements. [alce::876__wikidata_simple__dev::p0]

Cited: alce::876__wikidata_simple__dev::p0

### `444__wikidata_intersection__dev`
> **Kattradhu Thamizh**
> In late 2007, the film 'Kattradhu Thamizh' and its soundtrack got released, with the music composed by Yuvan Shankar Raja. [alce::444__wikidata_intersection__dev::p3]
> Venkat Prabhu directed 'Kattradhu Thamizh', which featured music by Yuvan Shankar Raja that was called a 'musical sensation' and noted as proof of Yuvan Shankar Raja's composing skills. [alce::444__wikidata_intersection__dev::p3]

Cited: alce::444__wikidata_intersection__dev::p3

### `728__wikidata_simple__dev`
> **Highland Avenue and the Angeles Forest Highway**
> The segment from the US 101 Freeway south to Santa Monica Boulevard used to be designated as part of California State Route 170. California's legislature has since relinquished state control of that segment, and thus that portion is now maintained by the City of Los Angeles. [alce::728__wikidata_simple__dev::p7]
> Highland Avenue is a north/south road in Los Angeles that runs from Cahuenga Boulevard and the US 101 Freeway in Hollywood from the north end to Olympic Boulevard in Mid-City Los Angeles on the south end. [alce::728__wikidata_simple__dev::p7]
> The Angeles Forest Highway is maintained by the Los Angeles County Department of Public Works. [alce::728__wikidata_simple__dev::p59]

Cited: alce::728__wikidata_simple__dev::p59, alce::728__wikidata_simple__dev::p7

### `432__wikidata_intersection__dev`
> **Hard Times**
> Hill made a deal to write and direct for scale and in turn got a shot at directing. The result was Hill's 1975 breakthrough film, 'Hard Times', made on location in New Orleans for just $2.7 million in 38 days. [alce::432__wikidata_intersection__dev::p22]
> Hill wrote 'Hard Times', 'The Driver', 'The Warriors', and an uncredited rewrite of 'Alien' in this style. [alce::432__wikidata_intersection__dev::p77]

Cited: alce::432__wikidata_intersection__dev::p22, alce::432__wikidata_intersection__dev::p77

### `570__wikidata_simple__dev`
> **Over 1,000 sites covering over 22,500 hectares**
> The Woodland Trust maintains ownership of over 1,000 sites covering over 22,500 hectares. [alce::570__wikidata_simple__dev::p0]

Cited: alce::570__wikidata_simple__dev::p0

### `259__wikidata_intersection__dev`
> **Multiple films: "Where Danger Lives" (1950), "The Story of Mankind" (1957), "The Big Circus" (1959), "The Lost World" (1960), "Voyage to the Bottom of the Sea" (1961), and "Five Weeks in a Balloon" (1962)**
> Allen's first film as producer was "Where Danger Lives" (1950) at RKO with Robert Mitchum, directed by John Farrow and written by Charles Bennett. [alce::259__wikidata_intersection__dev::p1]
> Bennett was reunited with Allen on "The Story of Mankind" (1957), and then did a series of films for Allen: "The Big Circus" (1959), "The Lost World" (1960), "Voyage to the Bottom of the Sea" (1961), and "Five Weeks in a Balloon" (1962). [alce::259__wikidata_intersection__dev::p4]

Cited: alce::259__wikidata_intersection__dev::p1, alce::259__wikidata_intersection__dev::p4

### `974__wikidata_comp__dev`
> **Don Boyd**
> Don Boyd is a Scottish film director, producer, screenwriter and novelist. [alce::974__wikidata_comp__dev::p1]
> Boyd produced and co-directed the film documentary 'Jimi Hendrix' (1973). [alce::974__wikidata_comp__dev::p77]
> 'Intimate Reflections' is a 1975 British independent drama film directed by Don Boyd. [alce::974__wikidata_comp__dev::p18]
> After producing Derek Jarman's War Requiem for the BBC in 1988, Boyd returned to his directorial career and directed various feature films. [alce::974__wikidata_comp__dev::p3]

Cited: alce::974__wikidata_comp__dev::p1, alce::974__wikidata_comp__dev::p18, alce::974__wikidata_comp__dev::p3, alce::974__wikidata_comp__dev::p77

### `435__wikidata_intersection__dev`
> **FA Cup, League Cup, and First Division play-off**
> The 1914 FA Cup Final was a football match between Burnley and Liverpool on 25 April 1914 at Crystal Palace, London. [alce::435__wikidata_intersection__dev::p14]
> Burnley faced Liverpool again after the League Cup meeting to hold the Reds to a goalless draw at Turf Moor, forcing yet another replay against lower league opposition. [alce::435__wikidata_intersection__dev::p45]
> Liverpool entered the competition in the second round, where they drawn against First Division team Burnley. The tie was played over two legs, with the first leg held at Liverpool's home ground Anfield. Goals from defender John Scales and striker Robbie Fowler secured a 2–0 victory for Liverpool. The second leg was held at Burnley's home ground Turf Moor, which Liverpool won 4–1 to progress to the third round courtesy of a 6–1 aggregate victory. [alce::435__wikidata_intersection__dev::p6]

Cited: alce::435__wikidata_intersection__dev::p14, alce::435__wikidata_intersection__dev::p45, alce::435__wikidata_intersection__dev::p6

### `305__wikidata_comp__dev`
_Refused._

### `320__wikidata_intersection__dev`
_Refused._

### `649__wikidata_simple__dev`
> **The Somali National Armed Forces (SNAF) are composed of the Army, Navy, Air Force, and Police Force, headed by the President as Commander in Chief**
> The Somali National Armed Forces (SNAF) are the military forces of Somalia, officially known as the 'Federal Republic of Somalia'. [alce::649__wikidata_simple__dev::p2]
> Headed by the President as Commander in Chief, they are constitutionally mandated to ensure the nation's sovereignty, independence and territorial integrity. [alce::649__wikidata_simple__dev::p2]
> The SAF was initially made up of the Army, Navy, Air Force and Police Force. [alce::649__wikidata_simple__dev::p2]

Cited: alce::649__wikidata_simple__dev::p2

### `286__wikidata_comp__dev`
> **Ray and Guy Green, Mann, and Henry Hathaway**
> Ray and Guy Green directed "55 Days at Peking" (1963), which was authored by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]
> Mann directed "The Fall of the Roman Empire" (1964), which was written by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]
> Henry Hathaway directed "Circus World" (1964), which was mostly written by Bernard Gordon. [alce::286__wikidata_comp__dev::p3]

Cited: alce::286__wikidata_comp__dev::p3

### `171__wikidata_intersection__dev`
_Refused._

### `563__wikidata_simple__dev`
> **Prime Press published science fiction books, including works by L. Sprague de Camp**
> Prime Press, Inc. was a science fiction and fantasy small press specialty publishing house founded in 1947. It published a number of interesting science fiction books in its brief four-year lifespan. [alce::563__wikidata_simple__dev::p0]
> Their next book was to have been "Lost Continents", by L. Sprague de Camp. [alce::563__wikidata_simple__dev::p1]

Cited: alce::563__wikidata_simple__dev::p0, alce::563__wikidata_simple__dev::p1

### `245__wikidata_intersection__dev`
> **Vettaiyaadu Vilaiyaadu**
> Harris crafted a necessary classiness into Gautham Menon's blockbuster crime thriller "Vettaiyaadu Vilaiyaadu" starring Kamal Haasan. [alce::245__wikidata_intersection__dev::p47]

Cited: alce::245__wikidata_intersection__dev::p47

### `534__wikitables_simple__dev`
> **Professional wrestling memorial shows since 1980 include the Mike Marino Memorial Shield (1981), Terry Gordy Memorial Show, Mark Curtis Memorial Weekend of Champions (2003), and Fred Ward Memorial Show (2004-2009)**
> The Mike Marino Memorial Shield was a British professional wrestling single-elimination tournament produced by Dale Martin Promotions, which took place on 29 September 1981 at Fairfield Halls in Croydon, England. [alce::534__wikitables_simple__dev::p12]
> The Terry Gordy Memorial Show was a professional wrestling memorial event produced by the Legends of Pro Wrestling (LPW) promotion. [alce::534__wikitables_simple__dev::p7]
> Fourth Annual Mark Curtis Memorial Weekend of Champions was a two-day professional wrestling memorial show produced by Southern States Wrestling (SSW), which took place from May 9–10, 2003, at the Civic Auditorium in Kingsport, Tennessee. [alce::534__wikitables_simple__dev::p89]
> The Fred Ward Memorial Show was an annual professional wrestling memorial event produced by the Georgia Championship Wrestling (GCW) promotion, which was held from 2004 to 2009. [alce::534__wikitables_simple__dev::p18]

Cited: alce::534__wikitables_simple__dev::p12, alce::534__wikitables_simple__dev::p18, alce::534__wikitables_simple__dev::p7, alce::534__wikitables_simple__dev::p89

### `26__wikitables_composition__dev`
> **The Lady Vanishes**
> The Lady Vanishes is a 1938 British thriller film directed by Alfred Hitchcock. [alce::26__wikitables_composition__dev::p0, alce::26__wikitables_composition__dev::p2]

Cited: alce::26__wikitables_composition__dev::p0, alce::26__wikitables_composition__dev::p2

### `169__wikidata_comp__dev`
> **Sweden**
> He was subsequently selected with the 39th overall pick by the Detroit Pistons, becoming the second Swedish national player to be selected in the NBA, after the Swedish-born American Miles Simon. [alce::169__wikidata_comp__dev::p1]

Cited: alce::169__wikidata_comp__dev::p1

### `674__wikidata_simple__dev`
> **Azusa Pacific University**
> The Free Methodist Church is one of several denominations supporting Azusa Pacific University (Azusa, CA). [alce::674__wikidata_simple__dev::p0]
> The following educational institutions are a part of the Association of Free Methodist Educational Institutions. [alce::674__wikidata_simple__dev::p0]

Cited: alce::674__wikidata_simple__dev::p0

### `725__wikidata_simple__dev`
> **10 asteroids (minor planets)**
> Vladimir Albitsky was a Soviet/Russian astronomer and discoverer of minor planets. [alce::725__wikidata_simple__dev::p0]
> The Minor Planet Center credits him with the discovery of 10 asteroids during 1923–1925. [alce::725__wikidata_simple__dev::p1]

Cited: alce::725__wikidata_simple__dev::p0, alce::725__wikidata_simple__dev::p1

### `730__wikidata_simple__dev`
> **Rabbi Schneur Zalman of Liadi**
> Chabad was founded in 1775 by Rabbi Schneur Zalman of Liadi. [alce::730__wikidata_simple__dev::p1]
> Shneur Zalman of Liadi was an Orthodox rabbi and the founder and first Rebbe of Chabad, a branch of Hasidic Judaism. [alce::730__wikidata_simple__dev::p58]

Cited: alce::730__wikidata_simple__dev::p1, alce::730__wikidata_simple__dev::p58

### `430__wikidata_intersection__dev`
> **Multiple French Grand Prix races: 1994, 1998, 2001, and 2004**
> The 1994 French Grand Prix was a Formula One motor race held on 3 July 1994 at the Circuit de Nevers Magny-Cours, and the 72-lap race was won by Michael Schumacher, driving a Benetton-Ford. [alce::430__wikidata_intersection__dev::p4]
> The 1998 French Grand Prix was a Formula One motor race held at Magny-Cours on 28 June 1998, and the 71-lap race was won by German driver Michael Schumacher, driving a Ferrari. [alce::430__wikidata_intersection__dev::p0]
> The 2001 French Grand Prix was a Formula One motor race held at the Circuit de Nevers Magny-Cours on 1 July 2001, and the 72-lap race was won by Michael Schumacher, driving a Ferrari. [alce::430__wikidata_intersection__dev::p2]
> Michael Schumacher was able to win the 2004 French Grand Prix using an unprecedented four-stop strategy. [alce::430__wikidata_intersection__dev::p44]

Cited: alce::430__wikidata_intersection__dev::p0, alce::430__wikidata_intersection__dev::p2, alce::430__wikidata_intersection__dev::p4, alce::430__wikidata_intersection__dev::p44

### `172__wikidata_comp__dev`
> **Multiple winners across different years: Sebastian Vettel (2018), Jenson Button (2011), Robert Kubica (2008), Lewis Hamilton (2007), and Daniel Ricciardo (2014)**
> The 2018 Canadian Grand Prix was won by Sebastian Vettel of Ferrari. [alce::172__wikidata_comp__dev::p12]
> The 2011 Canadian Grand Prix was won by McLaren driver Jenson Button after starting from seventh position. [alce::172__wikidata_comp__dev::p5]
> The 2008 Canadian Grand Prix was won by Robert Kubica for the BMW Sauber team after starting from second position. [alce::172__wikidata_comp__dev::p16]
> The 2007 Canadian Grand Prix was won by Lewis Hamilton, starting from pole position, in his first season in the top formula. [alce::172__wikidata_comp__dev::p10]
> The 2014 Canadian Grand Prix was won by Daniel Ricciardo. [alce::172__wikidata_comp__dev::p1]

Cited: alce::172__wikidata_comp__dev::p1, alce::172__wikidata_comp__dev::p10, alce::172__wikidata_comp__dev::p12, alce::172__wikidata_comp__dev::p16, alce::172__wikidata_comp__dev::p5

### `606__wikidata_simple__dev`
> **Brooke Niles, Marloes Wesselink, and Patricia Labee are professional beach volleyball players**
> Brooke Niles (born March 11, 1981) is a professional beach volleyball player from the United States who plays on the FIVB World Tour and Top US Pro Tour. [alce::606__wikidata_simple__dev::p55]
> Marloes Wesselink (born April 14, 1987) is a Dutch professional beach volleyball player born in Doetinchem. [alce::606__wikidata_simple__dev::p94]
> Patricia Labee (born 4 April 1977) is a Dutch female professional beach volleyball and indoor volleyball player. [alce::606__wikidata_simple__dev::p99]

Cited: alce::606__wikidata_simple__dev::p55, alce::606__wikidata_simple__dev::p94, alce::606__wikidata_simple__dev::p99

### `700__wikidata_simple__dev`
> **Suddha**
> Suddha, also called "The Cleansing Rites", is an Indian film, the first ever Tulu language film shot on the digital format. [alce::700__wikidata_simple__dev::p18]
> The 105 minute film was shot in 2004 in a village called Marnad near Mangalore, Karnataka and was released in 2005. [alce::700__wikidata_simple__dev::p43]

Cited: alce::700__wikidata_simple__dev::p18, alce::700__wikidata_simple__dev::p43

### `452__wikidata_intersection__dev`
> **The Swarm (1978)**
> For theatrical release, he produced and directed "The Swarm" (1978) and "Beyond the Poseidon Adventure" (1979), and produced "When Time Ran Out" (1980). [alce::452__wikidata_intersection__dev::p1]

Cited: alce::452__wikidata_intersection__dev::p1

### `213__wikidata_intersection__dev`
> **Thomas H. Collins, Karl L. Schultz, Patrick M. Stillman, Robert S. Lucas, and John B. Hayes**
> Thomas Hansen Collins graduated from the U.S. Coast Guard Academy in 1968 and served as the 22nd Commandant of the U.S. Coast Guard. [alce::213__wikidata_intersection__dev::p13]
> Karl Leo Schultz graduated from the U.S. Coast Guard Academy in 1983 and is the 26th Commandant of the U.S. Coast Guard. [alce::213__wikidata_intersection__dev::p12]
> Patrick M. Stillman graduated from the Coast Guard Academy in 1972 and is a retired Rear Admiral of the United States Coast Guard. [alce::213__wikidata_intersection__dev::p96]
> Robert S. Lucas graduated from the United States Coast Guard Academy in 1952 and is a former rear admiral in the United States Coast Guard. [alce::213__wikidata_intersection__dev::p46]
> John Briggs Hayes graduated from the United States Coast Guard Academy in 1946 and served as the 16th Commandant of the U.S. Coast Guard. [alce::213__wikidata_intersection__dev::p91]

Cited: alce::213__wikidata_intersection__dev::p12, alce::213__wikidata_intersection__dev::p13, alce::213__wikidata_intersection__dev::p46, alce::213__wikidata_intersection__dev::p91, alce::213__wikidata_intersection__dev::p96

### `410__wikidata_intersection__dev`
_Refused._

### `514__wikitables_simple__dev`
> **Sheffield Doc/Fest, Full Frame Documentary Film Festival, Al Jazeera International Documentary Film Festival, DOC LA (Los Angeles Documentary Film Festival), and Dokufest**
> Sheffield Doc/Fest is described as one of the most significant documentary festivals in Britain and has been voted one of the Top Five Coolest Documentary Film Festivals in the World. [alce::514__wikitables_simple__dev::p12]
> The Full Frame Documentary Film Festival is an annual international event dedicated to the theatrical exhibition of non-fiction cinema. [alce::514__wikitables_simple__dev::p27]
> Al Jazeera International Documentary Film Festival is an international film festival showcasing documentaries and it is organized by Al Jazeera. [alce::514__wikitables_simple__dev::p9]
> DOC LA — Los Angeles Documentary Film Festival — is an international documentary film festival in Hollywood, California. [alce::514__wikitables_simple__dev::p10]
> Dokufest is an International Documentary and Short Film Festival held in the Kosovo town of Prizren. [alce::514__wikitables_simple__dev::p2]

Cited: alce::514__wikitables_simple__dev::p10, alce::514__wikitables_simple__dev::p12, alce::514__wikitables_simple__dev::p2, alce::514__wikitables_simple__dev::p27, alce::514__wikitables_simple__dev::p9

### `81__wikitables_composition__dev`
> **Jeremain Lens, Fabio Borini, Yann M'Vila, DeAndre Yedlin, and Ola Toivonen**
> During the summer transfer window, the club made two major signings in winger Jeremain Lens, who previously played under Advocaat at PSV, and striker Fabio Borini, who played for Sunderland on loan during the 2013–14 season. [alce::81__wikitables_composition__dev::p7]
> The club also signed several defenders and secured the loan signings of Yann M'Vila, DeAndre Yedlin and Ola Toivonen. [alce::81__wikitables_composition__dev::p7]
> On 6 August 2015, M'Vila joined English Premier League side Sunderland on a season-long loan with a view to being made a permanent deal. [alce::81__wikitables_composition__dev::p85]
> On 28 August 2015, Toivonen joined Premier League side Sunderland on a season-long loan, linking up with his former manager at PSV Dick Advocaat. [alce::81__wikitables_composition__dev::p6]

Cited: alce::81__wikitables_composition__dev::p6, alce::81__wikitables_composition__dev::p7, alce::81__wikitables_composition__dev::p85

### `475__wikitables_simple__dev`
> **Reefs are located in multiple locations worldwide including the Pacific, western Atlantic, Persian Gulf, Madagascar, Philippines, Hawaiian Islands, Southeast Asia, Tasman Sea, Great Barrier Reef, and other tropical and temperate regions between 30°N and 30°S from the equator**
> There are coral reefs in the Persian Gulf, Madagascar, the Philippines, Hawaiian Islands and off Southeast Asia. [alce::475__wikitables_simple__dev::p92]
> Coral reefs are found in the Pacific and western Atlantic regions. [alce::475__wikitables_simple__dev::p92]
> Shallow-water reefs are only found in areas 30° N to 30° S from the equator. [alce::475__wikitables_simple__dev::p42]
> Coral reefs are rare along the west coasts of the Americas and Africa, due primarily to upwelling and strong cold coastal currents. [alce::475__wikitables_simple__dev::p5]
> Reefs are located in the northern Tasman Sea, around 95 km north from Lord Howe Island and 555 km off the New South Wales coast. [alce::475__wikitables_simple__dev::p6]
> Fringing reefs are distributed widely in the Great Barrier Reef, most common towards the southern part, attached to high islands like the Whitsunday Islands. [alce::475__wikitables_simple__dev::p8]

Cited: alce::475__wikitables_simple__dev::p42, alce::475__wikitables_simple__dev::p5, alce::475__wikitables_simple__dev::p6, alce::475__wikitables_simple__dev::p8, alce::475__wikitables_simple__dev::p92

### `99__wikitables_composition__dev`
> **Dalby**
> Dalby is a locality situated in Lund Municipality, Skåne County, Sweden. [alce::99__wikitables_composition__dev::p26]
> There are nine urban areas (or localities) in Lund Municipality. [alce::99__wikitables_composition__dev::p0]

Cited: alce::99__wikitables_composition__dev::p0, alce::99__wikitables_composition__dev::p26

### `688__wikidata_simple__dev`
> **Fox Business Morning**
> Fox Business Morning was the first show to be aired on the Fox Business Network when it launched October 15, 2007. [alce::688__wikidata_simple__dev::p4]

Cited: alce::688__wikidata_simple__dev::p4

### `1368__wikidata_simple__dev`
> **Area conferences (21 area conferences)**
> All congregations in the denomination belong to an area conference, and it is the area conference that is the component part of Mennonite Church USA. [alce::1368__wikidata_simple__dev::p11]
> There are currently 21 area conferences with many of them overlapping geographically due to conference structures prior to the merger. [alce::1368__wikidata_simple__dev::p11]

Cited: alce::1368__wikidata_simple__dev::p11

### `206__wikidata_intersection__dev`
> **Attarintiki Daredi**
> Attarintiki Daredi is the feature film soundtrack of the 2013 film of the same name starring Pawan Kalyan, Samantha Ruth Prabhu and Pranitha Subhash. Directed by Trivikram Srinivas, the film's music and background score were composed by Devi Sri Prasad. [alce::206__wikidata_intersection__dev::p8]

Cited: alce::206__wikidata_intersection__dev::p8

### `661__wikidata_simple__dev`
> **Victor W. Marek was the doctoral advisor to 16 doctoral candidates in mathematics and computer science, including Małgorzata Dubiel-Lachlan, Roman Kossak, Adam Krawczyk, Tadeusz Kreid, Roman Murawski, Andrzej Pelc, Zygmunt Ratajczyk, Marian Srebrny, Zygmunt Vetulani, V. K. Cody Bumgardner, Waldemar W. Koczkodaj, Witold Lipski Jr., Joseph Oldham, Inna Pivkina, Michał Sobolewski, and Paweł Traczyk.**
> He was an advisor of 16 doctoral candidates both in mathematics and computer science. [alce::661__wikidata_simple__dev::p2]
> In particular, he advised dissertations in mathematics by Małgorzata Dubiel-Lachlan, Roman Kossak, Adam Krawczyk, Tadeusz Kreid, Roman Murawski, Andrzej Pelc, Zygmunt Ratajczyk, Marian Srebrny, and Zygmunt Vetulani. [alce::661__wikidata_simple__dev::p2]
> In computer science his students were V. K. Cody Bumgardner, Waldemar W. Koczkodaj, Witold Lipski Jr., Joseph Oldham, Inna Pivkina, Michał Sobolewski, Paweł Traczyk, and Zygmunt Vetulani. [alce::661__wikidata_simple__dev::p2]

Cited: alce::661__wikidata_simple__dev::p2

### `540__wikitables_simple__dev`
> **Common chord progressions include the V–I authentic cadence, the 12 bar blues progression, and the ⅱ–Ⅴ–I progression**
> The most conclusive and resolving cadences return to the tonic or I chord; following the circle of fifths, the most suitable chord to precede the I chord is a V chord. This particular cadence, V–I, is known as an authentic cadence. [alce::540__wikitables_simple__dev::p39]
> One example of a widely used chord progression in Western traditional music and blues is the 12 bar blues progression. [alce::540__wikitables_simple__dev::p9]
> The ⅱ–Ⅴ–I progression is a common cadential chord progression used in a wide variety of music genres, including jazz harmony. [alce::540__wikitables_simple__dev::p64]

Cited: alce::540__wikitables_simple__dev::p39, alce::540__wikitables_simple__dev::p64, alce::540__wikitables_simple__dev::p9

### `517__wikitables_simple__dev`
> **Mk 19, M203, HK69A1, Type 91, CIS 40 GL**
> Larger crew-served automatic grenade launchers such as the Mk 19 are mounted on vehicles. [alce::517__wikitables_simple__dev::p1]
> The American M203 grenade launcher is a type of grenade launcher. [alce::517__wikitables_simple__dev::p26]
> The HK69A1 is a 40 mm grenade launcher developed and produced by the German arms manufacturer Heckler & Koch. [alce::517__wikitables_simple__dev::p26]
> The Type 91 Grenade Launcher is a Chinese grenade launcher used to launch 35mm non-lethal grenades. [alce::517__wikitables_simple__dev::p2]
> The Singaporean CIS 40 GL is a type of grenade launcher. [alce::517__wikitables_simple__dev::p26]

Cited: alce::517__wikitables_simple__dev::p1, alce::517__wikitables_simple__dev::p2, alce::517__wikitables_simple__dev::p26

### `962__wikidata_comp__dev`
> **Various institutions including Truro College, the Leys School, Gonville and Caius College Cambridge, Dartford Grammar School, University of York, University of Southampton, and others**
> Joseph Wellington Hunkin, the eighth Bishop of Truro, was educated at Truro College, the Leys School and Gonville and Caius College, Cambridge. [alce::962__wikidata_comp__dev::p75]
> Chris Goldsmith, Bishop of St Germans and Acting Bishop of Truro since 2017, was educated at Dartford Grammar School and studied biochemistry at the University of York. [alce::962__wikidata_comp__dev::p48]
> Tim Thornton, who was diocesan Bishop of Truro from 2009–2017, was educated at Devonport High School for Boys and studied theology at the University of Southampton. [alce::962__wikidata_comp__dev::p8]

Cited: alce::962__wikidata_comp__dev::p48, alce::962__wikidata_comp__dev::p75, alce::962__wikidata_comp__dev::p8

### `473__wikitables_simple__dev`
> **Connie Kalitta was a bounty hunter**
> Connie Kalitta (born February 24, 1938) is an American businessman and former drag racing driver, nicknamed 'The Bounty Hunter'. [alce::473__wikitables_simple__dev::p76]
> A bounty hunter is a person who captures fugitives for a bounty. [alce::473__wikitables_simple__dev::p3]

Cited: alce::473__wikitables_simple__dev::p3, alce::473__wikitables_simple__dev::p76

### `697__wikidata_simple__dev`
> **Lesley Thomson**
> Lesley Thomson was the Solicitor General for Scotland from 2011 to 2016, one of the two law officers of the Scottish Government. [alce::697__wikidata_simple__dev::p20]

Cited: alce::697__wikidata_simple__dev::p20

### `388__wikidata_comp__dev`
_Refused._

### `133__wikidata_comp__dev`
> **Peter Weir, Joe Dante, Frank Oz, Michael Ritchie, and others**
> Tom Schulman wrote the screenplay for 'Dead Poets Society,' which was directed by Peter Weir. [alce::133__wikidata_comp__dev::p0]
> Schulman was hired to rewrite 'Honey, I Shrunk the Kids,' a film that was directed by Joe Dante. [alce::133__wikidata_comp__dev::p0]
> Schulman wrote or co-wrote comedies including 'What About Bob?' (directed by Frank Oz), 'Welcome to Mooseport,' 'Second Sight,' and 'Holy Man' (starring Eddie Murphy). [alce::133__wikidata_comp__dev::p6]
> Schulman wrote 'Medicine Man,' a Sean Connery drama that proved a critical failure. [alce::133__wikidata_comp__dev::p6]

Cited: alce::133__wikidata_comp__dev::p0, alce::133__wikidata_comp__dev::p6

### `86__wikitables_composition__dev`
> **1900 to 1921**
> Henry L. Williams served as the head football coach at the University of Minnesota from 1900 to 1921. [alce::86__wikitables_composition__dev::p1]
> In 1900, his first year as head coach, the Golden Gophers compiled a 10–0–2 record. [alce::86__wikitables_composition__dev::p2]

Cited: alce::86__wikitables_composition__dev::p1, alce::86__wikitables_composition__dev::p2

### `322__wikidata_comp__dev`
_Refused._

### `27__wikitables_composition__dev`
> **Saints canonized by Pope Francis after 17 December 2013 include: Angela of Foligno, Peter Faber, Martyrs of Otranto, José de Anchieta, Marie of the Incarnation, John XXIII, John Paul II, and six additional saints on 23 November 2014, Joseph Vaz, four saints on 17 May 2015, Junípero Serra, four saints on 18 October 2015, Maria Elisabeth Hesselblad, and Stanislaus Papczyński**
> Francis approved the equipollent canonization of Angela of Foligno the following 9 October and then the Jesuit Peter Faber the following 17 December. [alce::27__wikitables_composition__dev::p3]
> Francis canonised Martyrs of Otranto – 813 inhabitants of Otranto who had been executed by the Ottomans in 1480. [alce::27__wikitables_composition__dev::p3]
> The pope approved further equipollent canonizations on 3 April 2014 for the Jesuit José de Anchieta as well as the Ursuline nun Marie of the Incarnation. [alce::27__wikitables_composition__dev::p3]
> Francis canonized his two predecessors John XXIII and John Paul II on 27 April 2014 and canonized six additional saints the following 23 November. [alce::27__wikitables_composition__dev::p0]
> The pope canonized Joseph Vaz on his visit to Sri Lanka on 14 January 2015 and canonized a further four saints on the following 17 May; he canonized Junípero Serra on 23 September while visiting the United States and then canonized four saints on 18 October including the first married couple to be named as saints. [alce::27__wikitables_composition__dev::p0]
> Francis canonized Maria Elisabeth Hesselblad and Stanislaus Papczyński on 5 June 2016. [alce::27__wikitables_composition__dev::p0]

Cited: alce::27__wikitables_composition__dev::p0, alce::27__wikitables_composition__dev::p3

### `791__wikidata_simple__dev`
> **Gornergrat railway station**
> The Gornergrat Railway is a mountain rack railway located in the Swiss canton of Valais that links the resort village of Zermatt to the summit of the Gornergrat. [alce::791__wikidata_simple__dev::p2]
> The Gornergrat railway station is situated at an altitude that makes the Gornergrat Railway the second highest railway in Europe after the Jungfrau, and the highest open-air railway of the continent. [alce::791__wikidata_simple__dev::p2]

Cited: alce::791__wikidata_simple__dev::p2

### `88__wikitables_composition__dev`
> **Multiple Canadian organizations endorsed the BDS movement, including: the United Church of Canada, Québec solidaire, Centrale des syndicats du Québec, Fédération des femmes du Québec, the Green Party of Canada, CUPE Ontario, and the Confédération des syndicats nationaux.**
> The United Church of Canada voted to boycott products from Israeli settlements. [alce::88__wikitables_composition__dev::p0]
> In Québec the political party Québec solidaire, the second largest public sector union Centrale des syndicats du Québec and the feminist organization Fédération des femmes du Québec have all supported the BDS campaign. [alce::88__wikitables_composition__dev::p0]
> Members of the Green Party of Canada voted to endorse BDS in August 2016. [alce::88__wikitables_composition__dev::p3]
> The Ontario wing of the Canadian Union of Public Employees (CUPE) has supported the Boycott, Divestment and Sanctions (BDS) campaign against Israel since 2006. [alce::88__wikitables_composition__dev::p17]
> Confédération des syndicats nationaux, Quebec, Canada, representing 325,000 in nearly 2,000 unions, voted to join the campaign for BDS and support a military embargo against Israel. [alce::88__wikitables_composition__dev::p6]

Cited: alce::88__wikitables_composition__dev::p0, alce::88__wikitables_composition__dev::p17, alce::88__wikitables_composition__dev::p3, alce::88__wikitables_composition__dev::p6

### `899__wikidata_simple__dev`
> **Mam language (predominant), with multiple other Maya languages including Q'anjob'al, Chuj, Jakaltek, Tektik, Awakatek, Chalchitek, Akatek, and K'iche'**
> While the Mam are predominant in the department, other Maya groups are the Q'anjob'al, Chuj, Jakaltek, Tektik, Awakatek, Chalchitek, Akatek and K'iche'. Each of these nine Maya ethnic groups speaks its own language. [alce::899__wikidata_simple__dev::p1]
> Huehuetenango has the greatest number of Mam Maya in Guatemala, although there are also Mam speakers in the departments of Quetzaltenango and San Marcos, and in the Mexican state of Chiapas. [alce::899__wikidata_simple__dev::p0]

Cited: alce::899__wikidata_simple__dev::p0, alce::899__wikidata_simple__dev::p1

### `108__wikidata_intersection__dev`
> **Multiple Hammer Film Productions movies including "Paranoiac" (1963), "Nightmare" (1964), "Hysteria" (1965), "The Evil of Frankenstein" (1964), and "Dracula Has Risen from the Grave" (1968)**
> Beginning with "Paranoiac" (1963), Francis made numerous films for Hammer throughout the 1960s and 1970s. [alce::108__wikidata_intersection__dev::p27]
> These films included thrillers like "Nightmare" (1964) and "Hysteria" (1965), as well as monster films such as "The Evil of Frankenstein" (1964) and "Dracula Has Risen from the Grave" (1968). [alce::108__wikidata_intersection__dev::p27, alce::108__wikidata_intersection__dev::p3]

Cited: alce::108__wikidata_intersection__dev::p27, alce::108__wikidata_intersection__dev::p3

### `892__wikidata_simple__dev`
> **North Dakota Wing**
> The North Dakota Wing of the Civil Air Patrol (CAP) is the highest echelon of Civil Air Patrol in the state of North Dakota. [alce::892__wikidata_simple__dev::p97]
> Civil Air Patrol (CAP) is the civilian auxiliary of the United States Air Force (USAF). [alce::892__wikidata_simple__dev::p1]

Cited: alce::892__wikidata_simple__dev::p1, alce::892__wikidata_simple__dev::p97

### `500__wikitables_simple__dev`
> **The New York Times, CBS News, and ABC News provide daily news podcasts**
> The Daily is a daily news podcast and radio show by the American newspaper The New York Times, hosted by Times political journalist Michael Barbaro. [alce::500__wikitables_simple__dev::p2]
> The CBS News iCast was a daily news audio podcast, created and first hosted by CBS News' New York-based Correspondent and Anchor Chris Mavridis. [alce::500__wikitables_simple__dev::p3]
> On March 28, 2018, ABC News began its first daily podcast, 'Start Here'. [alce::500__wikitables_simple__dev::p9]

Cited: alce::500__wikitables_simple__dev::p2, alce::500__wikitables_simple__dev::p3, alce::500__wikitables_simple__dev::p9

### `529__wikitables_simple__dev`
> **Environmental film festivals include the Environmental Film Festival Australia, Environmental Film Festival in the Nation's Capital, San Francisco Green Film Festival, and G2 Green Earth Film Festival**
> The Environmental Film Festival Australia is a film festival which screens domestically and internationally produced environmental films around Australia, launched in 2010 and held annually since. [alce::529__wikitables_simple__dev::p1]
> The Environmental Film Festival in the Nation's Capital hosts the largest environmental film festival in the United States each March in Washington, DC, presenting more than 100 films to an audience of over 30,000. [alce::529__wikitables_simple__dev::p2]
> San Francisco Green Film Festival is an environmental film festival which was first held in March 2011 with a mission to educate and connect communities through forward-thinking programs of environmental films, dialogues, and action opportunities. [alce::529__wikitables_simple__dev::p7]
> The G2 Green Earth Film Festival is an annual environmental film festival that takes place at The G2 Gallery in Venice, California, beginning in 2013 and screening eco-centered documentaries and narrative films. [alce::529__wikitables_simple__dev::p10]

Cited: alce::529__wikitables_simple__dev::p1, alce::529__wikitables_simple__dev::p10, alce::529__wikitables_simple__dev::p2, alce::529__wikitables_simple__dev::p7

### `551__wikitables_simple__dev`
> **AIPC Magazine, Carnivorous Plant Newsletter, Planta Carnivora, and Bulletin of the Australian Carnivorous Plant Society**
> AIPC Magazine is a quarterly Italian-language periodical and the official publication of Associazione Italiana Piante Carnivore (AIPC), a carnivorous plant society based in Italy. [alce::551__wikitables_simple__dev::p36]
> The Carnivorous Plant Newsletter is the official publication of the International Carnivorous Plant Society (ICPS), the largest such organization in the world. [alce::551__wikitables_simple__dev::p1]
> Planta Carnivora is a biannual periodical and the official publication of The Carnivorous Plant Society of the United Kingdom. [alce::551__wikitables_simple__dev::p2]
> The Bulletin of the Australian Carnivorous Plant Society was a quarterly periodical and the official publication of the Australian Carnivorous Plant Society. [alce::551__wikitables_simple__dev::p4]

Cited: alce::551__wikitables_simple__dev::p1, alce::551__wikitables_simple__dev::p2, alce::551__wikitables_simple__dev::p36, alce::551__wikitables_simple__dev::p4

### `578__wikidata_simple__dev`
> **Multiple models including Legend, Integra, TL, RL, RLX, and ILX**
> Acura is the luxury vehicle marque of Japanese automaker Honda. [alce::578__wikidata_simple__dev::p2]
> Its initial offering consisted of two models: the executive class Legend and the compact class Integra, available as a five-door and three-door hatchback. [alce::578__wikidata_simple__dev::p51]
> The first vehicle offered as a Type-S variant was the 2002 Acura TL, and the first vehicle offered as an A-Spec variant was the 2003 Acura TL. [alce::578__wikidata_simple__dev::p18]
> The Acura RL is a mid-sized / executive luxury car that was manufactured by the Acura division of Honda for the 1996–2012 model years over two generations, and was replaced in 2013 by the Acura RLX. [alce::578__wikidata_simple__dev::p58]
> In 2013, two Acura ILXs were unofficially entered in the 25 Hours of Thunderhill by Honda R&D Americas designers and engineers. [alce::578__wikidata_simple__dev::p11]

Cited: alce::578__wikidata_simple__dev::p11, alce::578__wikidata_simple__dev::p18, alce::578__wikidata_simple__dev::p2, alce::578__wikidata_simple__dev::p51, alce::578__wikidata_simple__dev::p58

### `448__wikidata_intersection__dev`
> **FA Charity Shield**
> The Liverpool F.C.–Manchester United F.C. rivalry, also known as the North West Derby, is a high-profile inter-city rivalry between English professional association football clubs Liverpool and Manchester United. [alce::448__wikidata_intersection__dev::p50]
> Liverpool and United had previously contested the Shield four times, with United winning in 1983 and the Shield being shared on the other three occasions in 1965, 1977 and 1990. [alce::448__wikidata_intersection__dev::p97]
> Following a 0–0 draw with Manchester United in the 1977 FA Charity Shield, a disappointing start to the 1977–78 season saw Liverpool out of the title race early on. [alce::448__wikidata_intersection__dev::p25]

Cited: alce::448__wikidata_intersection__dev::p25, alce::448__wikidata_intersection__dev::p50, alce::448__wikidata_intersection__dev::p97

### `154__wikidata_comp__dev`
> **Jack Nicklaus (most Masters victories with 6 wins)**
> The player with the most Masters victories is Jack Nicklaus, who won six times between 1963 and 1986. [alce::154__wikidata_comp__dev::p2]
> Other notable Masters Tournament winners include Horton Smith (first winner in 1934), Arnold Palmer and Tiger Woods (four wins each), and Jimmy Demaret, Gary Player, Sam Snead, Nick Faldo, and Phil Mickelson (three titles each). [alce::154__wikidata_comp__dev::p2]

Cited: alce::154__wikidata_comp__dev::p2

### `582__wikidata_simple__dev`
> **Jerome Robbins choreographed dances in multiple works including stage productions and ballets**
> Jerome Robbins was an American choreographer, director, dancer, and theater producer who worked in classical ballet, on Broadway, and in films and television. [alce::582__wikidata_simple__dev::p3]
> Among his numerous stage productions he worked on were 'On the Town', 'Peter Pan', 'High Button Shoes', 'The King and I', 'The Pajama Game', 'Bells Are Ringing', 'West Side Story', 'Gypsy', and 'Fiddler on the Roof'. [alce::582__wikidata_simple__dev::p3]
> Jerome Robbins' Broadway is an anthology comprising musical numbers from shows that were either directed or choreographed by Jerome Robbins, including 'The King and I'. [alce::582__wikidata_simple__dev::p12]
> Jerome Robbins choreographed ballets including 'The Goldberg Variations', 'Glass Pieces', 'Eight Lines', 'The Four Seasons', 'Fanfare', 'Piccolo Balletto', 'Verdi Variations', and 'Dances at a Gathering'. [alce::582__wikidata_simple__dev::p50]
> Les Noces is a ballet choreographed by Jerome Robbins. [alce::582__wikidata_simple__dev::p8]

Cited: alce::582__wikidata_simple__dev::p12, alce::582__wikidata_simple__dev::p3, alce::582__wikidata_simple__dev::p50, alce::582__wikidata_simple__dev::p8

### `156__wikidata_intersection__dev`
> **2010 WTA Tour Championships and 2011 Australian Open**
> Partnering Flavia Pennetta, Dulko won the 2010 WTA Tour Championships and the 2011 Australian Open in doubles. [alce::156__wikidata_intersection__dev::p0]
> Dulko teamed with Pennetta to win their first Grand Slam event title by winning the 2011 Australian Open, defeating Victoria Azarenka and Maria Kirilenko, 2–6, 7–5, 6–1, in the final. [alce::156__wikidata_intersection__dev::p6]

Cited: alce::156__wikidata_intersection__dev::p0, alce::156__wikidata_intersection__dev::p6

### `121__wikidata_comp__dev`
> **Ernest Dickerson and Charles S. Dutton**
> For 'The Corner' miniseries, director Charles S. Dutton won the Emmy for Outstanding Directing for a Miniseries, Movie or Dramatic Special. [alce::121__wikidata_comp__dev::p13]
> Ernest Dickerson directed multiple episodes of 'The Wire' and 'Treme', both TV programs that David Simon worked on as a writer and producer. [alce::121__wikidata_comp__dev::p4, alce::121__wikidata_comp__dev::p7]

Cited: alce::121__wikidata_comp__dev::p13, alce::121__wikidata_comp__dev::p4, alce::121__wikidata_comp__dev::p7

### `140__wikidata_comp__dev`
> **Arthur Hiller**
> Arthur Hiller directed 'The Hospital' (1971), a film for which Paddy Chayefsky was the screenwriter and received the Academy Award for Best Original Screenplay. [alce::140__wikidata_comp__dev::p91]

Cited: alce::140__wikidata_comp__dev::p91

### `328__wikidata_intersection__dev`
_Refused._
