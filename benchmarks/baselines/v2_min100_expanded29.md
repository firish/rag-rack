# Eval Report: harry_potter_micro

- **Pipeline:** `gemini/gemma-4-31b-it | bge-small | hybrid(BM25+lance) | min_tokens=100 | top_k=15 | loose`
- **Run at:** 2026-05-11 00:23:08
- **Questions:** 29
- **Errors:** 14

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.321 |
| `citation_recall` | 0.385 |
| `citation_f1` | 0.165 |
| `coverage` | 0.462 |
| `localization_accuracy` | 0.133 |
| `abstention_precision` | 0.500 |
| `abstention_recall` | 0.500 |
| `abstention_f1` | 0.500 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_three_headed_dog_name` | ✗ | ✗ | 1 | 3 | 5 | 0.03 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_mirror_of_erised` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_why_famous` | ✗ | ✗ | 0 | 4 | 4 | 0.03 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 0 | 2 | 0.00 ⚠️ ServiceUnavailableError: litellm.ServiceUnavailableError: GeminiException - {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
 |
| `hp_platform` | ✗ | ✗ | 0 | 0 | 4 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_sorcerers_stone` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_sorting_hat_not_slytherin` | ✗ | ✗ | 1 | 2 | 2 | 0.03 |
| `hp_potter_called_sorting` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_lily_james` | ✗ | ✗ | 0 | 1 | 2 | 0.03 |
| `hp_hogwarts_headmaster` | ✗ | ✗ | 1 | 3 | 4 | 0.03 |
| `hp_ollivander_wand_connection` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_hagrid_first_name` | ✓ | ✗ | 0 | 0 | 2 | 0.03 |
| `hp_dudley_school` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_four_houses` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_ron_older_brothers` | ✗ | ✗ | 1 | 5 | 1 | 0.03 |
| `hp_learn_about_flamel` | ✗ | ✗ | 4 | 13 | 5 | 0.03 |
| `hp_scar_voldemort_connection` | ✓ | ✗ | 0 | 0 | 4 | 0.03 |
| `hp_quote_welcome` | ✗ | ✗ | 0 | 0 | 1 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_quote_dwell_on_dreams` | ✗ | ✗ | 1 | 2 | 4 | 0.03 |
| `hp_refuse_dumbledore_plan` | ✗ | ✓ | 0 | 2 | 0 | 0.03 |
| `hp_refuse_petunia_lily_feelings` | ✗ | ✓ | 0 | 3 | 0 | 0.03 |
| `hp_steals_stone` | ✗ | ✗ | 0 | 0 | 3 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_cursed_broomstick` | ✗ | ✗ | 0 | 4 | 2 | 0.03 |
| `hp_refuse_favorite_color` | ✗ | ✓ | 0 | 0 | 0 | 0.00 ⚠️ InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
 |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.03 |

## Per-question answers

### `hp_quidditch_basics`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_voldemort_killed_parents`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_three_headed_dog_name`
> The three-headed dog guarding the trapdoor is named Fluffy .

Cited: sample-c7feccb8::s3285, sample-c7feccb8::s3877, sample-c7feccb8::s5584

### `hp_hagrid_dragon_name`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_mirror_of_erised`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_why_famous`
> Harry Potter is famous in the wizarding world, to the extent that every child in that world knows his name . He is famous for something that he will not remember . Additionally, he is known as a hero of two Quidditch matches .

Cited: sample-c7feccb8::s1016, sample-c7feccb8::s254, sample-c7feccb8::s256, sample-c7feccb8::s4940

### `hp_hagrid_reveals_wizard`
**Error:** ServiceUnavailableError: litellm.ServiceUnavailableError: GeminiException - {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}


### `hp_platform`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_sorcerers_stone`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_sorting_hat_not_slytherin`
> The Sorting Hat does not place Harry in Slytherin because Harry thought, "Not Slytherin, not Slytherin" . Although the hat told Harry that he could be great and that Slytherin would help him on the way to greatness, it placed him in Gryffindor because Harry was sure he did not want to be in Slytherin .

Cited: sample-c7feccb8::s2491, sample-c7feccb8::s2493

### `hp_potter_called_sorting`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_lily_james`
> Harry's parents are referred to as the Potters .

Cited: sample-c7feccb8::s4212

### `hp_hogwarts_headmaster`
> Albus Dumbledore is the headmaster of Hogwarts .

Cited: sample-c7feccb8::s1145, sample-c7feccb8::s1152, sample-c7feccb8::s1153

### `hp_ollivander_wand_connection`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_hagrid_first_name`
_Refused._

### `hp_dudley_school`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_four_houses`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_ron_older_brothers`
> Ron Weasley's older brothers include Bill, Charlie, Percy, Fred, and George . Ron is the sixth in his family to go to Hogwarts and notes that the others "did it first" .

Cited: sample-c7feccb8::s2038, sample-c7feccb8::s2039, sample-c7feccb8::s2040, sample-c7feccb8::s2041, sample-c7feccb8::s2042

### `hp_learn_about_flamel`
> After Hagrid mentions the name Nicolas Flamel, Harry, Ron, and Hermione search for him in library books for two weeks but find nothing . Harry eventually discovers Flamel's name on a Famous Wizard card from a Chocolate Frog, which notes that Flamel was Dumbledore's partner in alchemy . Subsequently, Hermione finds an old book she had borrowed from the library weeks prior that reveals Nicolas Flamel is the only known maker of the Sorcerer's Stone . This book describes Flamel as a noted alchemist and opera lover who lives in Devon with his wife, Perenelle .

Cited: sample-c7feccb8::s3897, sample-c7feccb8::s3898, sample-c7feccb8::s3958, sample-c7feccb8::s3978, sample-c7feccb8::s4402, sample-c7feccb8::s4415, sample-c7feccb8::s4416, sample-c7feccb8::s4418, sample-c7feccb8::s4422, sample-c7feccb8::s4424, sample-c7feccb8::s4430, sample-c7feccb8::s4438, sample-c7feccb8::s4439

### `hp_scar_voldemort_connection`
_Refused._

### `hp_quote_welcome`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_quote_dwell_on_dreams`
> Dumbledore says, "It does not do to dwell on dreams and forget to live, remember that."

Cited: sample-c7feccb8::s4323, sample-c7feccb8::s4331

### `hp_refuse_dumbledore_plan`
> Dumbledore states that Voldemort cannot be killed because he is not truly alive . He suggests that if someone prepared to fight a losing battle continues to delay Voldemort's return to power again and again, he may never return to power .

Cited: sample-c7feccb8::s6137, sample-c7feccb8::s6139

### `hp_refuse_petunia_lily_feelings`
> Aunt Petunia referred to Lily as her "dratted sister" . She believed she was the only person who saw Lily for what she truly was, which she described as "a freak" . She recalled Lily receiving a letter and attending a school, returning during vacations with pockets full of frog spawn and turning teacups into rats . Additionally, she noted that her parents were proud of having a witch in the family .

Cited: sample-c7feccb8::s1005, sample-c7feccb8::s1007, sample-c7feccb8::s1008

### `hp_steals_stone`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_cursed_broomstick`
> Quirrell was the one who tried to kill Harry and would have gotten him off his broom if not for Hermione knocking him over and Snape muttering a countercurse to save him .

Cited: sample-c7feccb8::s5914, sample-c7feccb8::s5915, sample-c7feccb8::s5917, sample-c7feccb8::s5918

### `hp_refuse_favorite_color`
**Error:** InternalServerError: litellm.InternalServerError: GeminiException InternalServerError - {
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}


### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
