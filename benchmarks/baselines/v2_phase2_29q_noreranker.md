# Eval Report: harry_potter_micro

- **Pipeline:** `gemini/gemma-4-31b-it | bge-small | hybrid(BM25+lance) | min_tokens=100 | no-reranker | retrieve=40/rerank=15 | loose`
- **Run at:** 2026-05-11 22:05:11
- **Questions:** 29

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.368 |
| `citation_recall` | 0.484 |
| `citation_f1` | 0.310 |
| `coverage` | 0.692 |
| `localization_accuracy` | 0.172 |
| `abstention_precision` | 0.750 |
| `abstention_recall` | 0.600 |
| `abstention_f1` | 0.667 |

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
| `hp_lily_james` | ✗ | ✗ | 0 | 1 | 2 | 0.03 |
| `hp_hogwarts_headmaster` | ✗ | ✗ | 1 | 3 | 4 | 0.03 |
| `hp_ollivander_wand_connection` | ✗ | ✗ | 1 | 2 | 1 | 0.03 |
| `hp_hagrid_first_name` | ✓ | ✗ | 0 | 0 | 2 | 0.03 |
| `hp_dudley_school` | ✗ | ✗ | 1 | 1 | 3 | 0.03 |
| `hp_four_houses` | ✗ | ✗ | 1 | 1 | 1 | 0.03 |
| `hp_ron_older_brothers` | ✗ | ✗ | 1 | 5 | 1 | 0.03 |
| `hp_learn_about_flamel` | ✗ | ✗ | 4 | 14 | 5 | 0.03 |
| `hp_scar_voldemort_connection` | ✗ | ✗ | 2 | 8 | 4 | 0.03 |
| `hp_quote_welcome` | ✗ | ✗ | 1 | 1 | 1 | 0.03 |
| `hp_quote_dwell_on_dreams` | ✗ | ✗ | 1 | 2 | 4 | 0.03 |
| `hp_refuse_dumbledore_plan` | ✗ | ✓ | 0 | 2 | 0 | 0.03 |
| `hp_refuse_petunia_lily_feelings` | ✗ | ✓ | 0 | 3 | 0 | 0.03 |
| `hp_steals_stone` | ✗ | ✗ | 0 | 9 | 3 | 0.03 |
| `hp_cursed_broomstick` | ✗ | ✗ | 0 | 4 | 2 | 0.03 |
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
> Harry's parents are referred to as the Potters .

Cited: sample-c7feccb8::s4212

### `hp_hogwarts_headmaster`
> Albus Dumbledore is the headmaster of Hogwarts .

Cited: sample-c7feccb8::s1145, sample-c7feccb8::s1152, sample-c7feccb8::s1153

### `hp_ollivander_wand_connection`
> Mr. Ollivander tells Harry that his wand is an unusual combination of phoenix feather and holly . He explains that the phoenix that provided the tail feather for Harry's wand gave only one other feather . Mr. Ollivander notes that it is very curious that Harry is destined for this wand when its "brother" wand gave Harry his scar .

Cited: sample-c7feccb8::s1728, sample-c7feccb8::s1743

### `hp_hagrid_first_name`
_Refused._

### `hp_dudley_school`
> Dudley's private school is named Smeltings.

Cited: sample-c7feccb8::s566

### `hp_four_houses`
> The four houses are called Gryffindor, Hufflepuff, Ravenclaw, and Slytherin.

Cited: sample-c7feccb8::s2323

### `hp_ron_older_brothers`
> Ron Weasley's older brothers include Bill, Charlie, Percy, Fred, and George . Ron is the sixth in his family to go to Hogwarts and notes that the others "did it first" .

Cited: sample-c7feccb8::s2038, sample-c7feccb8::s2039, sample-c7feccb8::s2040, sample-c7feccb8::s2041, sample-c7feccb8::s2042

### `hp_learn_about_flamel`
> After Hagrid mentions that Nicolas Flamel is involved with what the dog is guarding, Harry, Ron, and Hermione attempt to find out who he is . They search through hundreds of books in the library for two weeks but are unable to find him . Harry eventually discovers Flamel's name on a Famous Wizard card from a Chocolate Frog, which notes that Flamel was Dumbledore's partner in alchemy . Subsequently, Hermione finds an old book she had borrowed from the library weeks prior that reveals Nicolas Flamel is the only known maker of the Sorcerer's Stone . This book describes him as a noted alchemist and opera lover who lives in Devon with his wife, Perenelle .

Cited: sample-c7feccb8::s3897, sample-c7feccb8::s3898, sample-c7feccb8::s3949, sample-c7feccb8::s3955, sample-c7feccb8::s3978, sample-c7feccb8::s4410, sample-c7feccb8::s4415, sample-c7feccb8::s4416, sample-c7feccb8::s4418, sample-c7feccb8::s4422, sample-c7feccb8::s4424, sample-c7feccb8::s4430, sample-c7feccb8::s4438, sample-c7feccb8::s4439

### `hp_scar_voldemort_connection`
> Harry's scar causes him pain in several instances involving Voldemort or those associated with him. When Quirrell, who shares his soul with Voldemort , grabbed Harry, Harry felt a "needle-sharp pain" and later "blinding" pain in his scar. Harry also felt pain as if his scar were "on fire" when a hooded figure looked at him , and he later noted that Voldemort was waiting in the forest . Additionally, a "sharp, hot pain" shot across the scar when a teacher looked past Quirrell's turban . Harry believes that when his scar hurts, it is a "warning" that "danger's coming" , and Ron associates the scar with "You-Know-Who" .

Cited: sample-c7feccb8::s2020, sample-c7feccb8::s2593, sample-c7feccb8::s5218, sample-c7feccb8::s5299, sample-c7feccb8::s5348, sample-c7feccb8::s6057, sample-c7feccb8::s6061, sample-c7feccb8::s6165

### `hp_quote_welcome`
> Professor McGonagall says "Welcome to Hogwarts."

Cited: sample-c7feccb8::s2319

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
> Professor Quirrell attempted to take the Stone from Harry and had previously failed to steal it from Gringotts . Additionally, Harry believed that Professor Snape was trying to steal the Stone .

Cited: sample-c7feccb8::s3883, sample-c7feccb8::s4444, sample-c7feccb8::s5310, sample-c7feccb8::s5437, sample-c7feccb8::s5483, sample-c7feccb8::s5964, sample-c7feccb8::s6106, sample-c7feccb8::s6109, sample-c7feccb8::s6112

### `hp_cursed_broomstick`
> Quirrell was the one who tried to kill Harry and would have gotten him off his broom if not for Hermione knocking him over and Snape muttering a countercurse to save him .

Cited: sample-c7feccb8::s5914, sample-c7feccb8::s5915, sample-c7feccb8::s5917, sample-c7feccb8::s5918

### `hp_refuse_favorite_color`
_Refused._

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
