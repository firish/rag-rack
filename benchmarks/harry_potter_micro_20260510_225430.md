# Eval Report: harry_potter_micro

- **Pipeline:** `groq/llama-3.3-70b-versatile | bge-small | hybrid(BM25+lance) | min_tokens=150 | top_k=15 | loose`
- **Run at:** 2026-05-10 22:54:30
- **Questions:** 15
- **Errors:** 9

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.500 |
| `citation_recall` | 0.267 |
| `citation_f1` | 0.233 |
| `coverage` | 0.600 |
| `localization_accuracy` | 0.167 |
| `abstention_precision` | 0.500 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.667 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 6 | 3 | 0.03 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_three_headed_dog_name` | ✗ | ✗ | 0 | 0 | 5 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 1 | 1 | 3 | 0.03 |
| `hp_mirror_of_erised` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_why_famous` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 15 | 2 | 0.03 |
| `hp_platform` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_sorcerers_stone` | ✗ | ✗ | 2 | 6 | 3 | 0.03 |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_potter_called_sorting` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_lily_james` | ✓ | ✗ | 0 | 0 | 2 | 0.03 |
| `hp_refuse_favorite_color` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_refuse_triwizard` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity' |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.03 |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport played on broomsticks with four balls. It has seven players on each side, including three Chasers who throw the Quaffle to each other and try to get it through one of the hoops to score a goal. The game ends when the Snitch is caught. Quidditch is a popular sport in the wizarding world, with many people following it, similar to how Muggles follow soccer.

Cited: sample-c7feccb8::s1600, sample-c7feccb8::s1601, sample-c7feccb8::s3368, sample-c7feccb8::s3370, sample-c7feccb8::s3371, sample-c7feccb8::s3412

### `hp_voldemort_killed_parents`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_three_headed_dog_name`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_hagrid_dragon_name`
> Hagrid names his pet dragon Norbert.

Cited: sample-c7feccb8::s4771

### `hp_mirror_of_erised`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_why_famous`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_hagrid_reveals_wizard`
> Hagrid tells Harry that he is a wizard and that his parents, James and Lily Potter, were killed by the dark wizard Lord Voldemort, but he doesn't reveal much about himself. However, it is mentioned that Hagrid is the gamekeeper at Hogwarts and that he has a fondness for magical creatures, including dragons . Hagrid also mentions that he was the one who borrowed Fluffy, a three-headed dog, to guard the Sorcerer's Stone .

Cited: sample-c7feccb8::s1014, sample-c7feccb8::s1015, sample-c7feccb8::s1016, sample-c7feccb8::s1017, sample-c7feccb8::s1018, sample-c7feccb8::s1019, sample-c7feccb8::s1020, sample-c7feccb8::s1021, sample-c7feccb8::s1022, sample-c7feccb8::s1023, sample-c7feccb8::s3878, sample-c7feccb8::s3879, sample-c7feccb8::s4640, sample-c7feccb8::s5386, sample-c7feccb8::s5387

### `hp_platform`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_sorcerers_stone`
> The Sorcerer's Stone is a legendary substance with astonishing powers that can transform any metal into pure gold and produce the Elixir of Life, which will make the drinker immortal. It is also known that the Stone was created by Nicolas Flamel, who is the only known maker of the Sorcerer's Stone. The Stone was being kept at Hogwarts, and its safety was a concern as several people, including Snape and Quirrell, were trying to obtain it.

Cited: sample-c7feccb8::s4430, sample-c7feccb8::s4435, sample-c7feccb8::s4436, sample-c7feccb8::s4437, sample-c7feccb8::s4443, sample-c7feccb8::s4585

### `hp_sorting_hat_not_slytherin`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_potter_called_sorting`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_lily_james`
_Refused._

### `hp_refuse_favorite_color`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_refuse_triwizard`
**Error:** Exception: tenacity import failed please run `pip install tenacity`. ErrorNo module named 'tenacity'

### `hp_refuse_horcrux`
_Refused._
