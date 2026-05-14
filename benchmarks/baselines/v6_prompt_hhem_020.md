# Eval Report: harry_potter_micro

- **Pipeline:** `gemini/gemma-4-31b-it | bge-small | hybrid(BM25+lance) | min_tokens=100 | bge-rerank-v2-m3 | retrieve=80/rerank=8 | hhem-2.1-open@0.2 | balanced`
- **Run at:** 2026-05-13 02:48:05
- **Questions:** 29
- **Errors:** 1

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.617 |
| `citation_recall` | 0.406 |
| `citation_f1` | 0.348 |
| `coverage` | 0.667 |
| `localization_accuracy` | 0.214 |
| `abstention_precision` | 0.500 |
| `abstention_recall` | 0.800 |
| `abstention_f1` | 0.615 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 5 | 3 | 0.88 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 1 | 1 | 4 | 0.31 |
| `hp_three_headed_dog_name` | ✓ | ✗ | 0 | 0 | 5 | 0.01 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 1 | 1 | 3 | 0.82 |
| `hp_mirror_of_erised` | ✗ | ✗ | 1 | 5 | 3 | 0.57 |
| `hp_why_famous` | ✗ | ✗ | 2 | 3 | 4 | 0.69 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 1 | 2 | 0.87 |
| `hp_platform` | ✗ | ✗ | 1 | 1 | 4 | 0.64 |
| `hp_sorcerers_stone` | ✗ | ✗ | 3 | 5 | 3 | 0.91 |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 2 | 3 | 2 | 0.61 |
| `hp_potter_called_sorting` | ✗ | ✗ | 1 | 1 | 1 | 0.17 |
| `hp_lily_james` | ✓ | ✗ | 0 | 0 | 2 | 0.00 |
| `hp_hogwarts_headmaster` | ✗ | ✗ | 1 | 1 | 4 | 0.89 |
| `hp_ollivander_wand_connection` | ✓ | ✗ | 0 | 0 | 1 | 0.10 |
| `hp_hagrid_first_name` | ✓ | ✗ | 0 | 0 | 2 | 0.09 |
| `hp_dudley_school` | ✗ | ✗ | 1 | 1 | 3 | 0.93 |
| `hp_four_houses` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_ron_older_brothers` | ✗ | ✗ | 1 | 4 | 1 | 0.68 |
| `hp_learn_about_flamel` | ✗ | ✗ | 2 | 6 | 5 | 0.65 |
| `hp_scar_voldemort_connection` | ✗ | ✗ | 2 | 5 | 4 | 0.70 |
| `hp_quote_welcome` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `hp_quote_dwell_on_dreams` | ✗ | ✗ | 1 | 2 | 4 | 0.97 |
| `hp_refuse_dumbledore_plan` | ✓ | ✓ | 0 | 0 | 0 | 0.10 |
| `hp_refuse_petunia_lily_feelings` | ✗ | ✓ | 0 | 2 | 0 | 0.16 |
| `hp_steals_stone` | ✗ | ✗ | 0 | 3 | 3 | 0.51 |
| `hp_cursed_broomstick` | ✗ | ✗ | 0 | 1 | 2 | 0.62 |
| `hp_refuse_favorite_color` | ✓ | ✓ | 0 | 0 | 0 | 0.20 |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.01 |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport. It's like soccer in the Muggle world. It is played up in the air on broomsticks and there's four balls. There are seven players on each side. Three of them are called Chasers. The Chasers throw the Quaffle to each other and try and get it through one of the hoops to score a goal. Ten points every time the Quaffle goes through one of the hoops. Seekers were usually the smallest and fastest players.

Cited: sample-c7feccb8::s1600, sample-c7feccb8::s1601, sample-c7feccb8::s3368, sample-c7feccb8::s3371, sample-c7feccb8::s3634

### `hp_voldemort_killed_parents`
> Voldemort killed Harry's parents.

Cited: sample-c7feccb8::s5491

### `hp_three_headed_dog_name`
_Refused._

### `hp_hagrid_dragon_name`
> Hagrid decided to call the dragon Norbert.

Cited: sample-c7feccb8::s4771

### `hp_mirror_of_erised`
> The Mirror of Erised shows nothing more or less than the deepest, most desperate desire of our hearts. The happiest man on earth would look into it and see himself exactly as he is. Ronald Weasley, who has always been overshadowed by his brothers, sees himself standing alone, the best of all of them. Dumbledore sees himself holding a pair of thick, woolen socks. Quirrell sees the Stone and presenting it to his master.

Cited: sample-c7feccb8::s4318, sample-c7feccb8::s4324, sample-c7feccb8::s4326, sample-c7feccb8::s4338, sample-c7feccb8::s5945

### `hp_why_famous`
> Harry is famous because a powerful, evil curse didn't work on him. No one ever lived after he decided ter kill 'em, no one except Harry, who was only a baby, and lived. He is known as "the boy who lived!"

Cited: sample-c7feccb8::s1076, sample-c7feccb8::s1077, sample-c7feccb8::s315

### `hp_hagrid_reveals_wizard`
> Hagrid told Harry the first time they met that he's always wanted a dragon.

Cited: sample-c7feccb8::s4643

### `hp_platform`
> Harry needs to take the train from platform nine and three-quarters.

Cited: sample-c7feccb8::s1814

### `hp_sorcerers_stone`
> The Sorcerer's Stone is a legendary substance with astonishing powers. The stone will transform any metal into pure gold. It also produces the Elixir of Life, which will make the drinker immortal. Nicolas Flamel is the only known maker of the Sorcerer's Stone. The only Stone currently in existence belongs to Mr. Nicolas Flamel.

Cited: sample-c7feccb8::s4430, sample-c7feccb8::s4435, sample-c7feccb8::s4436, sample-c7feccb8::s4437, sample-c7feccb8::s4438

### `hp_sorting_hat_not_slytherin`
> Harry thought, "Not Slytherin, not Slytherin." The Sorting Hat asked, "Not Slytherin, eh?" The Sorting Hat asked, "Are you sure?" The Sorting Hat said, "Well, if you're sure -- better be GRYFFINDOR!"

Cited: sample-c7feccb8::s2491, sample-c7feccb8::s2492, sample-c7feccb8::s2493

### `hp_potter_called_sorting`
> . Then, "Potter, Harry!" was called

Cited: sample-c7feccb8::s2478

### `hp_lily_james`
_Refused._

### `hp_hogwarts_headmaster`
> Albus Dumbledore is the headmaster of Hogwarts.

Cited: sample-c7feccb8::s1145

### `hp_ollivander_wand_connection`
_Refused._

### `hp_hagrid_first_name`
_Refused._

### `hp_dudley_school`
> Dudley had been accepted at Uncle Vernon's old private school, Smeltings.

Cited: sample-c7feccb8::s566

### `hp_four_houses`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_ron_older_brothers`
> Fred and George Weasley are Ron's brothers .
Bill and Charlie have already left .
Percy is a prefect

Cited: sample-c7feccb8::s2007, sample-c7feccb8::s2008, sample-c7feccb8::s2039, sample-c7feccb8::s2040

### `hp_learn_about_flamel`
> They had indeed been searching books for Flamel's name ever since Hagrid had let it slip . Harry looked at the Famous Wizard card . The card stated that Dumbledore was famous for "his work on alchemy with his partner, Nicolas Flamel" . Hermione was dashing back, an enormous old book in her arms . She whispered that "Nicolas Flamel... is the only known maker of the Sorcerer's Stone!" . The book stated that the only Stone currently in existence belongs to Mr. Nicolas Flamel, the noted alchemist and opera lover

Cited: sample-c7feccb8::s3958, sample-c7feccb8::s4410, sample-c7feccb8::s4418, sample-c7feccb8::s4422, sample-c7feccb8::s4430, sample-c7feccb8::s4438

### `hp_scar_voldemort_connection`
> A needle-sharp pain seared across Harry's scar when Harry felt Quirrell's hand close on his wrist. Harry's scar was almost blinding him with pain while Quirrell, who shares his soul with Voldemort, was howling in agony. A sharp, hot pain shot across the scar on Harry's forehead when a teacher looked past Quirrell's turban straight into Harry's eyes.

Cited: sample-c7feccb8::s2593, sample-c7feccb8::s6056, sample-c7feccb8::s6057, sample-c7feccb8::s6061, sample-c7feccb8::s6165

### `hp_quote_welcome`
> Professor McGonagall said, "Welcome to Hogwarts."

Cited: sample-c7feccb8::s2319

### `hp_quote_dwell_on_dreams`
> Dumbledore says, "It does not do to dwell on dreams and forget to live, remember that."

Cited: sample-c7feccb8::s4323, sample-c7feccb8::s4331

### `hp_refuse_dumbledore_plan`
_Refused._

### `hp_refuse_petunia_lily_feelings`
> . Aunt Petunia claimed she was the only one who saw Lily for what she was -- a freak . It seemed Aunt Petunia had been wanting to say all this for years

Cited: sample-c7feccb8::s1007, sample-c7feccb8::s1010

### `hp_steals_stone`
> Harry says, "Snape's trying to steal it" .
Harry states that "Snape's trying to force Quirrell to help him get" the Sorcerer's Stone .
Hagrid says that Snape "helped protect the Stone" and "he's not about ter steal it"

Cited: sample-c7feccb8::s3883, sample-c7feccb8::s4585, sample-c7feccb8::s4682

### `hp_cursed_broomstick`
> Ron explained that it was Snape who was cursing Harry's broomstick.

Cited: sample-c7feccb8::s3869

### `hp_refuse_favorite_color`
_Refused._

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
