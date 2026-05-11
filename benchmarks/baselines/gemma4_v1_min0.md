# Eval Report: harry_potter_micro

- **Pipeline:** `gemini/gemma-4-31b-it | bge-small | hybrid(BM25+lance) | min_tokens=0 | top_k=15 | loose`
- **Run at:** 2026-05-10 23:28:21
- **Questions:** 15

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.447 |
| `citation_recall` | 0.250 |
| `citation_f1` | 0.241 |
| `coverage` | 0.500 |
| `localization_accuracy` | 0.200 |
| `abstention_precision` | 0.600 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.750 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 3 | 3 | 0.03 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 2 | 3 | 4 | 0.02 |
| `hp_three_headed_dog_name` | ✗ | ✗ | 0 | 1 | 5 | 0.03 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 1 | 1 | 3 | 0.03 |
| `hp_mirror_of_erised` | ✗ | ✗ | 1 | 5 | 3 | 0.03 |
| `hp_why_famous` | ✗ | ✗ | 0 | 3 | 4 | 0.02 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 3 | 2 | 0.02 |
| `hp_platform` | ✗ | ✗ | 2 | 3 | 4 | 0.02 |
| `hp_sorcerers_stone` | ✗ | ✗ | 3 | 6 | 3 | 0.03 |
| `hp_sorting_hat_not_slytherin` | ✓ | ✗ | 0 | 0 | 2 | 0.03 |
| `hp_potter_called_sorting` | ✓ | ✗ | 0 | 0 | 1 | 0.02 |
| `hp_lily_james` | ✗ | ✗ | 0 | 2 | 2 | 0.02 |
| `hp_refuse_favorite_color` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport . It is played in the air on broomsticks with four balls and is compared to soccer in the Muggle world . Although it is not too easy to play, it is easy enough to understand . Each side has seven players, three of whom are called Chasers .

Cited: sample-c7feccb8::s1600, sample-c7feccb8::s1601, sample-c7feccb8::s3368

### `hp_voldemort_killed_parents`
> You-Know-Who killed Harry's parents . Harry also states that Voldemort killed his parents . Voldemort said he killed Harry's mother because she tried to stop him from killing Harry .

Cited: sample-c7feccb8::s1070, sample-c7feccb8::s5491, sample-c7feccb8::s6147

### `hp_three_headed_dog_name`
> The name of the three-headed dog is Fluffy .

Cited: sample-c7feccb8::s5393

### `hp_hagrid_dragon_name`
> Hagrid decided to name his dragon Norbert.

Cited: sample-c7feccb8::s4771

### `hp_mirror_of_erised`
> The Mirror of Erised shows the happiest man on earth himself exactly as he is . It showed Harry his family , specifically his mother, father, and one of his grandfathers . It also showed Ron as head boy . Additionally, Harry believed that looking in the mirror would show him finding the Stone .

Cited: sample-c7feccb8::s4295, sample-c7feccb8::s4311, sample-c7feccb8::s4312, sample-c7feccb8::s4318, sample-c7feccb8::s5974

### `hp_why_famous`
> Harry Potter is famous because someone tried to kill him . He is also known as a hero of two Quidditch matches .

Cited: sample-c7feccb8::s1103, sample-c7feccb8::s1104, sample-c7feccb8::s4940

### `hp_hagrid_reveals_wizard`
> When they first meet, Hagrid tells Harry to call him Hagrid, as everyone does . He also tells Harry that he is the Keeper of Keys at Hogwarts . Additionally, Harry mentions that Hagrid told him the first time they met that he had always wanted a dragon .

Cited: sample-c7feccb8::s4643, sample-c7feccb8::s917, sample-c7feccb8::s918

### `hp_platform`
> Harry needs to find Platform Nine and Three-Quarters at King's Cross station .

Cited: sample-c7feccb8::s1844, sample-c7feccb8::s1898, sample-c7feccb8::s2131

### `hp_sorcerers_stone`
> The Sorcerer's Stone is a legendary substance with astonishing powers that is the focus of the ancient study of alchemy . It is a blood-red stone that can transform any metal into pure gold . It also produces the Elixir of Life, which makes the drinker immortal . Nicolas Flamel is the only known maker of the Sorcerer's Stone , and the only one currently in existence belongs to him .

Cited: sample-c7feccb8::s4430, sample-c7feccb8::s4435, sample-c7feccb8::s4436, sample-c7feccb8::s4437, sample-c7feccb8::s4438, sample-c7feccb8::s5997

### `hp_sorting_hat_not_slytherin`
_Refused._

### `hp_potter_called_sorting`
_Refused._

### `hp_lily_james`
> Harry's parents are referred to as the Potters .

Cited: sample-c7feccb8::s55, sample-c7feccb8::s56

### `hp_refuse_favorite_color`
_Refused._

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
