# Eval Report: harry_potter_micro

- **Pipeline:** `gemini/gemma-4-31b-it | bge-small | hybrid(BM25+lance) | min_tokens=100 | top_k=15 | loose`
- **Run at:** 2026-05-11 00:02:20
- **Questions:** 15
- **Errors:** 1

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.319 |
| `citation_recall` | 0.405 |
| `citation_f1` | 0.290 |
| `coverage` | 0.818 |
| `localization_accuracy` | 0.214 |
| `abstention_precision` | 1.000 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 1.000 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 11 | 3 | 0.03 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 1 | 2 | 4 | 0.03 |
| `hp_three_headed_dog_name` | ✗ | ✗ | 1 | 3 | 5 | 0.03 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 1 | 1 | 3 | 0.03 |
| `hp_mirror_of_erised` | ✗ | ✗ | 1 | 9 | 3 | 0.03 |
| `hp_why_famous` | ✗ | ✗ | 0 | 4 | 4 | 0.03 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 5 | 2 | 0.03 |
| `hp_platform` | ✗ | ✗ | 2 | 5 | 4 | 0.03 |
| `hp_sorcerers_stone` | ✗ | ✗ | 3 | 7 | 3 | 0.03 |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 1 | 2 | 2 | 0.03 |
| `hp_potter_called_sorting` | ✗ | ✗ | 1 | 7 | 1 | 0.03 |
| `hp_lily_james` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_refuse_favorite_color` | ✓ | ✓ | 0 | 0 | 0 | 0.03 |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.03 |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport that is similar to soccer in the Muggle world . It is played in the air on broomsticks and involves four balls . Each side has seven players , three of whom are called Chasers . Chasers use a bright red ball called the Quaffle, which is about the size of a soccer ball , and try to score ten points by throwing it through one of the three golden poles with hoops on the end located at either end of the field . A game of Quidditch only ends when the Snitch is caught . Seekers, who are usually the smallest and fastest players , are always the ones who get clobbered by the other team . Additionally, there are seven hundred ways of committing a Quidditch foul .

Cited: sample-c7feccb8::s1600, sample-c7feccb8::s1601, sample-c7feccb8::s3354, sample-c7feccb8::s3366, sample-c7feccb8::s3368, sample-c7feccb8::s3369, sample-c7feccb8::s3370, sample-c7feccb8::s3371, sample-c7feccb8::s3412, sample-c7feccb8::s3634, sample-c7feccb8::s3703

### `hp_voldemort_killed_parents`
> Harry's parents were killed by You-Know-Who and Voldemort .

Cited: sample-c7feccb8::s1070, sample-c7feccb8::s5491

### `hp_three_headed_dog_name`
> The three-headed dog guarding the trapdoor is named Fluffy .

Cited: sample-c7feccb8::s3285, sample-c7feccb8::s3877, sample-c7feccb8::s5584

### `hp_hagrid_dragon_name`
> Hagrid decided to call his dragon Norbert.

Cited: sample-c7feccb8::s4771

### `hp_mirror_of_erised`
> The Mirror of Erised shows the deepest, most desperate desire of a person's heart . The happiest man on earth would see himself exactly as he is, using it like a normal mirror . Examples of what individuals see include:
* Harry sees his family and later sees his reflection pull out a blood-red stone .
* Ronald Weasley sees himself as head boy , older, as Quidditch captain, and holding the Quidditch cup and the house cup .
* Dumbledore sees himself holding a pair of thick, woolen socks .
* Quirrell sees himself presenting the Stone to his master .

Cited: sample-c7feccb8::s4261, sample-c7feccb8::s4311, sample-c7feccb8::s4312, sample-c7feccb8::s4318, sample-c7feccb8::s4324, sample-c7feccb8::s4325, sample-c7feccb8::s4338, sample-c7feccb8::s5945, sample-c7feccb8::s5997

### `hp_why_famous`
> Harry Potter is famous in the wizarding world, to the extent that every child in that world knows his name . He is famous for something that he will not remember . Additionally, he is known as a hero of two Quidditch matches .

Cited: sample-c7feccb8::s1016, sample-c7feccb8::s254, sample-c7feccb8::s256, sample-c7feccb8::s4940

### `hp_hagrid_reveals_wizard`
> When they first meet, Hagrid tells Harry that something about him "finished" and "stumped" someone . He tells Harry that his mother met "that Potter" at school, they married and had Harry, and then she "got herself blown up" . Hagrid also tells Harry that he knew Harry would be "just the same, just as strange, just as -- as -- abnormal" , that every kid in "our world" knows his name , and that he is famous .

Cited: sample-c7feccb8::s1011, sample-c7feccb8::s1016, sample-c7feccb8::s1116, sample-c7feccb8::s1117, sample-c7feccb8::s1404

### `hp_platform`
> Harry needs to find platform nine and three-quarters at King's Cross station.

Cited: sample-c7feccb8::s1814, sample-c7feccb8::s1817, sample-c7feccb8::s1844, sample-c7feccb8::s1861, sample-c7feccb8::s1898

### `hp_sorcerers_stone`
> The Sorcerer's Stone is a legendary substance with astonishing powers that is the focus of the ancient study of alchemy . It can transform any metal into pure gold and produces the Elixir of Life, which makes the drinker immortal . Nicolas Flamel is the only known maker of the stone and owned the only one currently in existence . The stone is blood-red in color and has been destroyed .

Cited: sample-c7feccb8::s4430, sample-c7feccb8::s4435, sample-c7feccb8::s4436, sample-c7feccb8::s4437, sample-c7feccb8::s4438, sample-c7feccb8::s5997, sample-c7feccb8::s6113

### `hp_sorting_hat_not_slytherin`
> The Sorting Hat does not place Harry in Slytherin because Harry thought, "Not Slytherin, not Slytherin" . Although the hat told Harry that he could be great and that Slytherin would help him on the way to greatness, it placed him in Gryffindor because Harry was sure he did not want to be in Slytherin .

Cited: sample-c7feccb8::s2491, sample-c7feccb8::s2493

### `hp_potter_called_sorting`
> Harry's name was called , and a whisper asked, "Potter, did she say?" . Professor McGonagall was the one conducting the ceremony .

Cited: sample-c7feccb8::s2366, sample-c7feccb8::s2368, sample-c7feccb8::s2374, sample-c7feccb8::s2382, sample-c7feccb8::s2478, sample-c7feccb8::s2480, sample-c7feccb8::s2515

### `hp_lily_james`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_refuse_favorite_color`
_Refused._

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
