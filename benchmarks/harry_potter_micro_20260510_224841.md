# Eval Report: harry_potter_micro

- **Pipeline:** `groq/llama-3.3-70b-versatile | bge-small | hybrid(BM25+lance) | min_tokens=150 | top_k=15 | loose`
- **Run at:** 2026-05-10 22:48:41
- **Questions:** 15
- **Errors:** 12

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.100 |
| `citation_recall` | 0.167 |
| `citation_f1` | 0.125 |
| `coverage` | 0.500 |
| `localization_accuracy` | 0.333 |
| `abstention_precision` | 1.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 1.000 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 5 | 3 | 0.03 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_three_headed_dog_name` | ✗ | ✗ | 0 | 0 | 5 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_mirror_of_erised` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_why_famous` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 22 | 2 | 0.03 |
| `hp_platform` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_sorcerers_stone` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_potter_called_sorting` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_lily_james` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_refuse_favorite_color` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_horcrux` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport played up in the air on broomsticks with four balls. It has seven players on each side, including three Chasers who throw the Quaffle to each other and try to get it through one of the hoops to score a goal. The game ends when the Snitch is caught.

Cited: sample-c7feccb8::s1600, sample-c7feccb8::s1601, sample-c7feccb8::s3368, sample-c7feccb8::s3371, sample-c7feccb8::s3412

### `hp_voldemort_killed_parents`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_three_headed_dog_name`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_hagrid_dragon_name`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_mirror_of_erised`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_why_famous`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_hagrid_reveals_wizard`
> Hagrid tells Harry that he is a wizard and that his parents, James and Lily Potter, were killed by the dark wizard Lord Voldemort, but he doesn't go into much detail about himself. Hagrid also mentions that he is the gamekeeper at Hogwarts. However, most of the information Hagrid shares with Harry is about Harry himself and his parents, rather than about Hagrid's own life or background.

Cited: sample-c7feccb8::s1011, sample-c7feccb8::s1012, sample-c7feccb8::s1013, sample-c7feccb8::s1014, sample-c7feccb8::s1015, sample-c7feccb8::s1016, sample-c7feccb8::s1017, sample-c7feccb8::s1018, sample-c7feccb8::s1019, sample-c7feccb8::s1020, sample-c7feccb8::s1021, sample-c7feccb8::s1022, sample-c7feccb8::s1023, sample-c7feccb8::s1024, sample-c7feccb8::s1025, sample-c7feccb8::s1026, sample-c7feccb8::s1027, sample-c7feccb8::s1116, sample-c7feccb8::s1117, sample-c7feccb8::s1118, sample-c7feccb8::s1119, sample-c7feccb8::s5386

### `hp_platform`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_sorcerers_stone`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_sorting_hat_not_slytherin`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_potter_called_sorting`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_lily_james`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_refuse_favorite_color`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'
