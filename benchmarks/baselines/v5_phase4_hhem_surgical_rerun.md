# Eval Report: harry_potter_micro

- **Pipeline:** `gemini/gemma-4-31b-it | bge-small | hybrid(BM25+lance) | min_tokens=100 | bge-rerank-v2-m3 | retrieve=80/rerank=8 | hhem-2.1-open | balanced`
- **Run at:** 2026-05-12 21:07:10
- **Questions:** 29
- **Errors:** 1

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.466 |
| `citation_recall` | 0.449 |
| `citation_f1` | 0.328 |
| `coverage` | 0.640 |
| `localization_accuracy` | 0.214 |
| `abstention_precision` | 0.600 |
| `abstention_recall` | 0.600 |
| `abstention_f1` | 0.600 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 9 | 3 | 0.83 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 1 | 3 | 4 | 0.26 |
| `hp_three_headed_dog_name` | ✗ | ✗ | 0 | 0 | 5 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 1 | 1 | 3 | 0.84 |
| `hp_mirror_of_erised` | ✗ | ✗ | 1 | 10 | 3 | 0.69 |
| `hp_why_famous` | ✗ | ✗ | 2 | 3 | 4 | 0.61 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 1 | 2 | 0.90 |
| `hp_platform` | ✗ | ✗ | 1 | 2 | 4 | 0.95 |
| `hp_sorcerers_stone` | ✗ | ✗ | 3 | 5 | 3 | 0.74 |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 0 | 1 | 2 | 0.27 |
| `hp_potter_called_sorting` | ✗ | ✗ | 1 | 3 | 1 | 0.33 |
| `hp_lily_james` | ✓ | ✗ | 0 | 0 | 2 | 0.00 |
| `hp_hogwarts_headmaster` | ✗ | ✗ | 1 | 2 | 4 | 0.40 |
| `hp_ollivander_wand_connection` | ✗ | ✗ | 1 | 1 | 1 | 0.14 |
| `hp_hagrid_first_name` | ✓ | ✗ | 0 | 0 | 2 | 0.23 |
| `hp_dudley_school` | ✗ | ✗ | 1 | 1 | 3 | 0.84 |
| `hp_four_houses` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `hp_ron_older_brothers` | ✗ | ✗ | 1 | 4 | 1 | 0.47 |
| `hp_learn_about_flamel` | ✗ | ✗ | 2 | 8 | 5 | 0.57 |
| `hp_scar_voldemort_connection` | ✗ | ✗ | 0 | 2 | 4 | 0.23 |
| `hp_quote_welcome` | ✗ | ✗ | 1 | 1 | 1 | 0.93 |
| `hp_quote_dwell_on_dreams` | ✗ | ✗ | 1 | 1 | 4 | 0.86 |
| `hp_refuse_dumbledore_plan` | ✗ | ✓ | 0 | 2 | 0 | 0.45 |
| `hp_refuse_petunia_lily_feelings` | ✗ | ✓ | 0 | 2 | 0 | 0.29 |
| `hp_steals_stone` | ✗ | ✗ | 0 | 6 | 3 | 0.66 |
| `hp_cursed_broomstick` | ✗ | ✗ | 0 | 1 | 2 | 0.48 |
| `hp_refuse_favorite_color` | ✓ | ✓ | 0 | 0 | 0 | 0.20 |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.01 |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport that is similar to soccer in the Muggle world . It is played in the air on broomsticks and involves four balls and seven players on each side . Three of the players are called Chasers , who throw a bright red ball called the Quaffle—which is about the size of a soccer ball—to each other . The Chasers attempt to score a goal by getting the Quaffle through one of the hoops , and ten points are awarded every time the Quaffle goes through a hoop . The field has three golden poles with hoops on the end at either end . Additionally, Seekers are typically the smallest and fastest players

Cited: sample-c7feccb8::s1600, sample-c7feccb8::s1601, sample-c7feccb8::s2210, sample-c7feccb8::s3354, sample-c7feccb8::s3368, sample-c7feccb8::s3369, sample-c7feccb8::s3370, sample-c7feccb8::s3371, sample-c7feccb8::s3634

### `hp_voldemort_killed_parents`
> Voldemort killed Harry's parents . Hagrid also stated that "You-Know-Who" killed them

Cited: sample-c7feccb8::s1070, sample-c7feccb8::s5491, sample-c7feccb8::s6054

### `hp_three_headed_dog_name`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_hagrid_dragon_name`
> Hagrid decided to call his dragon Norbert.

Cited: sample-c7feccb8::s4771

### `hp_mirror_of_erised`
> The Mirror of Erised shows the deepest, most desperate desire of a person's heart . However, the happiest man on earth would see himself exactly as he is, using it like a normal mirror . Examples of what individuals see include:
* Harry sees his family standing around him .
* Ronald Weasley sees himself as the best of his brothers , appearing older, as head boy, and as Quidditch captain holding the house cup and the Quidditch cup .
* Dumbledore sees himself holding a pair of thick, woolen socks .
* Quirrell sees the Stone and himself presenting it to his master

Cited: sample-c7feccb8::s4211, sample-c7feccb8::s4261, sample-c7feccb8::s4263, sample-c7feccb8::s4264, sample-c7feccb8::s4318, sample-c7feccb8::s4324, sample-c7feccb8::s4325, sample-c7feccb8::s4326, sample-c7feccb8::s4338, sample-c7feccb8::s5945

### `hp_why_famous`
> Harry Potter is famous because a powerful, evil curse that killed his parents and house did not work on him . He is the only person to have lived after "You-Know-Who" decided to kill them, despite being only a baby at the time . Consequently, he is known as "the boy who lived!"

Cited: sample-c7feccb8::s1076, sample-c7feccb8::s1077, sample-c7feccb8::s315

### `hp_hagrid_reveals_wizard`
> When they first met, Hagrid told Harry that he had always wanted a dragon.

Cited: sample-c7feccb8::s4643

### `hp_platform`
> Harry needs to find platform nine and three-quarters at King's Cross station.

Cited: sample-c7feccb8::s1814, sample-c7feccb8::s6350

### `hp_sorcerers_stone`
> The Sorcerer's Stone is a legendary substance with astonishing powers that is the focus of the ancient study of alchemy . It can transform any metal into pure gold and produces the Elixir of Life, which makes the drinker immortal . Nicolas Flamel is the only known maker of the stone , and the only stone currently in existence belongs to him

Cited: sample-c7feccb8::s4430, sample-c7feccb8::s4435, sample-c7feccb8::s4436, sample-c7feccb8::s4437, sample-c7feccb8::s4438

### `hp_sorting_hat_not_slytherin`
> . After the hat asked if he was sure, it decided "better be GRYFFINDOR!"

Cited: sample-c7feccb8::s2493

### `hp_potter_called_sorting`
> Professor McGonagall calls Harry's name during the sorting ceremony

Cited: sample-c7feccb8::s2435, sample-c7feccb8::s2436, sample-c7feccb8::s2478

### `hp_lily_james`
_Refused._

### `hp_hogwarts_headmaster`
> The headmaster of Hogwarts is Albus Dumbledore

Cited: sample-c7feccb8::s1145, sample-c7feccb8::s6203

### `hp_ollivander_wand_connection`
> . Mr. Ollivander notes that it is very curious that Harry is destined for this wand when its "brother" gave Harry his scar

Cited: sample-c7feccb8::s1743

### `hp_hagrid_first_name`
_Refused._

### `hp_dudley_school`
> Dudley was accepted at Smeltings, which was Uncle Vernon's old private school.

Cited: sample-c7feccb8::s566

### `hp_four_houses`
> The four houses are called Gryffindor, Hufflepuff, Ravenclaw, and Slytherin.

Cited: sample-c7feccb8::s2323

### `hp_ron_older_brothers`
> Ron Weasley's older brothers include Bill, Charlie, Percy, Fred, and George , and Bill and Charlie had already left

Cited: sample-c7feccb8::s2007, sample-c7feccb8::s2008, sample-c7feccb8::s2039, sample-c7feccb8::s2040

### `hp_learn_about_flamel`
> Harry, Ron, and Hermione initially searched through hundreds of library books but were unable to find information on Nicolas Flamel . Harry eventually discovers the name on a Famous Wizard card, which notes that Dumbledore worked on alchemy with his partner, Nicolas Flamel . Subsequently, Hermione uses an enormous old book she had borrowed from the library weeks earlier to find that Flamel is a noted alchemist and opera lover and the only known maker of the Sorcerer's Stone

Cited: sample-c7feccb8::s3955, sample-c7feccb8::s3958, sample-c7feccb8::s4410, sample-c7feccb8::s4418, sample-c7feccb8::s4422, sample-c7feccb8::s4424, sample-c7feccb8::s4430, sample-c7feccb8::s4438

### `hp_scar_voldemort_connection`
> . Dumbledore clarifies that the protection Harry received from his mother's love is not a scar or any other visible sign

Cited: sample-c7feccb8::s6157, sample-c7feccb8::s6158

### `hp_quote_welcome`
> Professor McGonagall says "Welcome to Hogwarts."

Cited: sample-c7feccb8::s2319

### `hp_quote_dwell_on_dreams`
> Dumbledore says, "It does not do to dwell on dreams and forget to live, remember that."

Cited: sample-c7feccb8::s4331

### `hp_refuse_dumbledore_plan`
> Dumbledore states that Voldemort cannot be killed because he is not truly alive . He suggests that if someone is prepared to fight what seems like a losing battle to delay Voldemort's return to power, and if he is delayed repeatedly, he may never return to power

Cited: sample-c7feccb8::s6137, sample-c7feccb8::s6139

### `hp_refuse_petunia_lily_feelings`
> Aunt Petunia considered her sister Lily to be "a freak" and believed she was the only one who saw her as such and recalled Lily returning from school during vacations turning teacups into rats and with pockets full of frog spawn

Cited: sample-c7feccb8::s1006, sample-c7feccb8::s1007

### `hp_steals_stone`
> Harry believes that Snape is trying to steal the Stone and is attempting to force Quirrell to help him get it . Harry also reports that Snape tried to get past the three-headed dog on Halloween, and he thinks Snape was trying to steal whatever the dog was guarding . However, Hagrid claims that Snape helped protect the Stone and is not going to steal it

Cited: sample-c7feccb8::s3875, sample-c7feccb8::s3883, sample-c7feccb8::s4444, sample-c7feccb8::s4585, sample-c7feccb8::s4682, sample-c7feccb8::s5310

### `hp_cursed_broomstick`
> Ron explained that Snape cursed Harry's broomstick, noting that he and Hermione saw Snape muttering and refusing to take his eyes off Harry

Cited: sample-c7feccb8::s3869

### `hp_refuse_favorite_color`
_Refused._

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
