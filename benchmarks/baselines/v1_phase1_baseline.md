# Eval Report: harry_potter_micro

- **Pipeline:** `groq/llama-3.3-70b-versatile | bge-small | hybrid(BM25+lance) | top_k=15 | loose`
- **Run at:** 2026-05-07 23:43:03
- **Questions:** 15

## Aggregate metrics

| Metric | Value |
|---|---|
| `citation_precision` | 0.317 |
| `citation_recall` | 0.201 |
| `citation_f1` | 0.199 |
| `coverage` | 0.500 |
| `localization_accuracy` | 0.200 |
| `abstention_precision` | 0.750 |
| `abstention_recall` | 1.000 |
| `abstention_f1` | 0.857 |

## Per-question results

| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |
|---|---|---|---|---|---|---|
| `hp_quidditch_basics` | ✗ | ✗ | 1 | 2 | 3 | 0.03 |
| `hp_voldemort_killed_parents` | ✗ | ✗ | 2 | 5 | 4 | 0.02 |
| `hp_three_headed_dog_name` | ✗ | ✗ | 0 | 2 | 5 | 0.03 |
| `hp_hagrid_dragon_name` | ✗ | ✗ | 1 | 1 | 3 | 0.03 |
| `hp_mirror_of_erised` | ✗ | ✗ | 1 | 5 | 3 | 0.03 |
| `hp_why_famous` | ✗ | ✗ | 0 | 4 | 4 | 0.02 |
| `hp_hagrid_reveals_wizard` | ✗ | ✗ | 0 | 4 | 2 | 0.02 |
| `hp_platform` | ✗ | ✗ | 1 | 5 | 4 | 0.02 |
| `hp_sorcerers_stone` | ✗ | ✗ | 2 | 4 | 3 | 0.03 |
| `hp_sorting_hat_not_slytherin` | ✓ | ✗ | 0 | 0 | 2 | 0.03 |
| `hp_potter_called_sorting` | ✗ | ✗ | 0 | 6 | 1 | 0.02 |
| `hp_lily_james` | ✗ | ✗ | 0 | 4 | 2 | 0.02 |
| `hp_refuse_favorite_color` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_triwizard` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |
| `hp_refuse_horcrux` | ✓ | ✓ | 0 | 0 | 0 | 0.02 |

## Per-question answers

### `hp_quidditch_basics`
> Quidditch is a wizard sport played up in the air on broomsticks with four balls, and it is somewhat hard to explain the rules. It is similar to soccer in the Muggle world, and everyone follows Quidditch. There are seven players on each side, with three of them called Chasers, making Quidditch easy enough to understand, even if it's not too easy to play.

Cited: sample-c7feccb8::s1601, sample-c7feccb8::s3368

### `hp_voldemort_killed_parents`
> You-Know-Who, also known as Voldemort, killed Harry's parents. Voldemort tried to kill Harry as well, but he couldn't.

Cited: sample-c7feccb8::s1070, sample-c7feccb8::s1071, sample-c7feccb8::s1073, sample-c7feccb8::s5491, sample-c7feccb8::s6147

### `hp_three_headed_dog_name`
> The name of the three-headed dog guarding the trapdoor is Fluffy.

Cited: sample-c7feccb8::s5392, sample-c7feccb8::s5393

### `hp_hagrid_dragon_name`
> Hagrid names his pet dragon Norbert.

Cited: sample-c7feccb8::s4771

### `hp_mirror_of_erised`
> The Mirror of Erised shows the viewer the deepest, most desperate desire of their heart. For the happiest man on earth, the Mirror of Erised would work like a normal mirror, showing him exactly as he is. However, for others, it reflects their deepest desires, such as Harry seeing his family smiling at him, or Ron seeing himself as head boy.

Cited: sample-c7feccb8::s4295, sample-c7feccb8::s4311, sample-c7feccb8::s4312, sample-c7feccb8::s4318, sample-c7feccb8::s5974

### `hp_why_famous`
> Harry Potter is famous in the wizarding world because he is a hero of two Quidditch matches and his story started to spread after he lost points for his house. He is also famous because he was involved in an incident where someone tried to kill him, which makes him even more famous. Additionally, Professor McGonagall thinks that Harry will be a legend and every child in the wizarding world will know his name, which suggests that he will be famous for a long time.

Cited: sample-c7feccb8::s1103, sample-c7feccb8::s1104, sample-c7feccb8::s254, sample-c7feccb8::s4940

### `hp_hagrid_reveals_wizard`
> Hagrid tells Harry that he is the Keeper of Keys at Hogwarts. He also tells Harry to call him Hagrid, as everyone does. However, when Harry asks him about something, Hagrid says it is a secret and he cannot tell Harry, as it is Hogwarts business and Dumbledore has trusted him with it.

Cited: sample-c7feccb8::s1479, sample-c7feccb8::s1480, sample-c7feccb8::s917, sample-c7feccb8::s918

### `hp_platform`
> Harry needs to find Platform Nine and Three-Quarters at King's Cross station. The platform is not immediately visible, and Harry has to figure out how to access it.

Cited: sample-c7feccb8::s1816, sample-c7feccb8::s1833, sample-c7feccb8::s1844, sample-c7feccb8::s1885, sample-c7feccb8::s1898

### `hp_sorcerers_stone`
> The Sorcerer's Stone is a legendary substance with astonishing powers. It has the ability to transform any metal into pure gold. The Stone also produces the Elixir of Life, which will make the drinker immortal. The only Stone currently in existence belongs to Mr. Nicolas Flamel, the noted alchemist.

Cited: sample-c7feccb8::s4435, sample-c7feccb8::s4436, sample-c7feccb8::s4437, sample-c7feccb8::s4438

### `hp_sorting_hat_not_slytherin`
_Refused._

### `hp_potter_called_sorting`
> Professor McGonagall calls out the names of the students during the sorting ceremony, but it is not explicitly stated that she calls Harry's name. However, another sentence shows that someone calls Harry's name. It is Professor Flitwick who is also shown to call Harry's name during a roll call. Snape also pauses at Harry's name during a roll call.

Cited: sample-c7feccb8::s2320, sample-c7feccb8::s2514, sample-c7feccb8::s2515, sample-c7feccb8::s2733, sample-c7feccb8::s2781, sample-c7feccb8::s6209

### `hp_lily_james`
> Harry's parents were referred to as "the Potters". His mum and dad were also mentioned, but their first names are not provided in the sources. They were a witch and a wizard, and their son, Harry, is the main subject of the conversation.

Cited: sample-c7feccb8::s1058, sample-c7feccb8::s1597, sample-c7feccb8::s55, sample-c7feccb8::s56

### `hp_refuse_favorite_color`
_Refused._

### `hp_refuse_triwizard`
_Refused._

### `hp_refuse_horcrux`
_Refused._
