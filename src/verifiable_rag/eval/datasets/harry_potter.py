"""Harry Potter book 1 mini-benchmark — 29 hand-curated questions.

Source: tests/parsers/fixtures/sample.pdf (Harry Potter and the Sorcerer's Stone).
Sentence IDs were located by keyword search against the parsed Document
(see examples/_lookup_sentences.py).

Gold sets are inclusive — any of the listed sentence_ids is an acceptable
citation. The Tier 1 metric (set overlap) gives credit for any intersection.

Categories
==========

Each category targets a different retrieval / citation / abstention failure
mode. We aim for ≥2 questions per category so a single bad annotation or
lucky guess doesn't dominate the metric.

* **Definition lookup (3)** — "What is X?" where X has an explicit definition
  sentence somewhere in the book. Tests whether retrieval surfaces the
  defining passage.
* **Specific detail / proper noun (5)** — Asks for a named entity or
  identifier (e.g. "What is the name of the three-headed dog?"). Often the
  answer is one word; tests whether the system pinpoints the right span.
* **Causal / "Why?" synthesis (2)** — Requires combining a cause-and-effect
  chain across multiple sentences (e.g. "Why does the Sorting Hat NOT place
  Harry in Slytherin?"). Multi-source reasoning.
* **Factual w/ redundant context (2)** — The answer is repeated across many
  passages (e.g. "Who killed Harry's parents?"). Tests that the system picks
  *any* valid supporting sentence, not necessarily the best one.
* **Scene-specific event (2)** — Asks about something that happens in a
  single localized scene (e.g. "What does Hagrid tell Harry when they first
  meet?"). Tests scene-anchored retrieval.
* **Refusal — out-of-document (3)** — Information is not in the book at all
  (e.g. "Who wins the Triwizard Tournament?"). Tests architectural hard
  refusal — system must say "I cannot answer."

Categories added in the expanded set (covering retrieval failure modes that
the original 15-question set didn't exercise):

* **Long-tail / single-sentence gold (2)** — The supporting fact is stated
  exactly once in the entire book (e.g. "What is Hagrid's first name?",
  Rubeus — mentioned ~3 times total, scattered). A retriever can't get
  lucky here; it has to find the rare passage.
* **List / enumeration (2)** — Answer is a list (e.g. "What are the four
  houses of Hogwarts?"). Tests recall — the system must surface the one
  sentence that enumerates them, *or* surface multiple distant sentences
  that each mention one.
* **Cross-chapter synthesis (2)** — The answer requires combining passages
  spread across distant chapters (e.g. "How does the trio learn about
  Nicolas Flamel?" — references span chapters 5, 12, 13). Tests retrieval
  breadth across long documents.
* **Quote attribution (2)** — Given an exact quote, find the speaker.
  Reverse-lookup pattern: the question contains a string that appears
  literally in the source. Tests whether keyword retrieval (BM25) carries
  its weight in the hybrid stack.
* **Partial-information refusal (2)** — Topic is touched on in the book but
  the specific question isn't answered (e.g. "What is Dumbledore's plan to
  defeat Voldemort?"). Harder than out-of-document refusals — system must
  recognize "this topic exists but the answer doesn't." Tests abstention
  calibration on the *boundary*.
* **Misleading / distractor-rich (2)** — Multiple passages frame the wrong
  entity as the answer (e.g. "Who tries to steal the Sorcerer's Stone?" —
  the book frames Snape as the suspect for most of the plot; Quirrell is
  revealed only at the climax). Tests whether the system commits to the
  obvious-but-wrong answer when many supporting-looking passages exist.

Totals: 29 questions (15 original + 12 new gap-fillers + 2 thin-category
fillers). 5 are refusal cases (3 OOD + 2 partial-info), 24 are answerable.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from verifiable_rag.eval import EvalQuestion

_PDF = Path("tests/parsers/fixtures/sample.pdf")
_DOC_PREFIX = "sample-c7feccb8"  # doc_id of the cached Harry Potter parse


def _sid(n: int) -> str:
    return f"{_DOC_PREFIX}::s{n}"


_QUESTIONS: list[EvalQuestion] = [
    # -------- Easy / direct factual ----------------------------------------
    EvalQuestion(
        id="hp_quidditch_basics",
        question="What is Quidditch?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(1601), _sid(1599), _sid(1587)}),
        gold_answer_text=(
            "Quidditch is a wizard sport played in the air on broomsticks "
            "with four balls and seven players per team."
        ),
    ),
    EvalQuestion(
        id="hp_voldemort_killed_parents",
        question="Who killed Harry's parents?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(224),
                _sid(233),
                _sid(5491),
                _sid(6147),
            }
        ),
        gold_answer_text="Voldemort killed Lily and James Potter.",
    ),
    EvalQuestion(
        id="hp_three_headed_dog_name",
        question="What is the name of the three-headed dog guarding the trapdoor?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(3877),
                _sid(3878),
                _sid(4592),
                _sid(4658),
                _sid(4686),
            }
        ),
        gold_answer_text="The three-headed dog's name is Fluffy.",
    ),
    EvalQuestion(
        id="hp_hagrid_dragon_name",
        question="What does Hagrid name his pet dragon?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(4771),
                _sid(4773),
                _sid(4775),
            }
        ),
        gold_answer_text="Hagrid names the dragon Norbert.",
    ),
    EvalQuestion(
        id="hp_mirror_of_erised",
        question="What does the Mirror of Erised show people?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(4308),
                _sid(4315),
                _sid(4318),
            }
        ),
        gold_answer_text=(
            "The Mirror of Erised shows the deepest desire of one's heart; "
            "the happiest person would see only themselves as they are."
        ),
    ),
    EvalQuestion(
        id="hp_why_famous",
        question="Why is Harry Potter famous in the wizarding world?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(233),
                _sid(315),
                _sid(1071),
                _sid(1077),
            }
        ),
        gold_answer_text=(
            "Harry is famous because Voldemort tried to kill him as a baby "
            "but couldn't, and Voldemort's power was broken in the attempt."
        ),
    ),
    EvalQuestion(
        id="hp_hagrid_reveals_wizard",
        question="What does Hagrid tell Harry about himself when they first meet?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(969),
                _sid(1126),
            }
        ),
        gold_answer_text="Hagrid tells Harry that he is a wizard.",
    ),
    EvalQuestion(
        id="hp_platform",
        question="What platform does Harry need to find at King's Cross station?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(1814),
                _sid(1818),
                _sid(1898),
                _sid(2131),
            }
        ),
        gold_answer_text="Platform nine and three-quarters.",
    ),
    EvalQuestion(
        id="hp_sorcerers_stone",
        question="What is the Sorcerer's Stone?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(4430),
                _sid(4435),
                _sid(4438),
            }
        ),
        gold_answer_text=(
            "A legendary substance with astonishing powers, made via alchemy; "
            "Nicolas Flamel is its only known maker."
        ),
    ),
    # -------- Multi-source synthesis (harder for retrieval) ----------------
    EvalQuestion(
        id="hp_sorting_hat_not_slytherin",
        question="Why does the Sorting Hat NOT place Harry in Slytherin?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(2491),
                _sid(2492),
            }
        ),
        gold_answer_text=(
            "Harry mentally pleaded 'not Slytherin' while wearing the hat, "
            "and the hat respected his choice and put him in Gryffindor instead."
        ),
    ),
    EvalQuestion(
        id="hp_potter_called_sorting",
        question="Who calls Harry's name during the sorting ceremony?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(2478)}),
        gold_answer_text=("Professor McGonagall calls 'Potter, Harry!' during the sorting."),
    ),
    EvalQuestion(
        id="hp_lily_james",
        question="What were the names of Harry's parents?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(224), _sid(228)}),
        gold_answer_text="Lily and James Potter.",
    ),
    # -------- Factual with redundant context (extra) ----------------------
    # Same answer is supported by many passages — tests that we surface ANY
    # valid one, not necessarily the canonical sentence.
    EvalQuestion(
        id="hp_hogwarts_headmaster",
        question="Who is the headmaster of Hogwarts?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(159),  # "This man's name was Albus Dumbledore."
                _sid(1145),  # "the greatest headmaster Hogwarts ever had Albus Dumbledore"
                _sid(2503),  # "in a large gold chair, sat Albus Dumbledore"
                _sid(2519),  # "Albus Dumbledore had gotten to his feet"
            }
        ),
        gold_answer_text="Albus Dumbledore.",
    ),
    # -------- Scene-specific event (extra) -------------------------------
    # A single localized scene contains the answer — tests scene-anchored
    # retrieval.
    EvalQuestion(
        id="hp_ollivander_wand_connection",
        question=(
            "What does Mr. Ollivander tell Harry about the phoenix feather "
            "in his wand?"
        ),
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(1743)}),
        gold_answer_text=(
            "The phoenix whose tail feather is in Harry's wand gave one "
            "other feather — the one in the wand that gave Harry his scar "
            "(Voldemort's wand)."
        ),
    ),
    # -------- Long-tail / single-sentence gold ----------------------------
    # The answer appears once in the entire book (or scattered across very
    # few sentences). Retriever can't get lucky — must find the rare passage.
    EvalQuestion(
        id="hp_hagrid_first_name",
        question="What is Hagrid's first name?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(900), _sid(1683)}),
        gold_answer_text="Rubeus (Rubeus Hagrid).",
    ),
    EvalQuestion(
        id="hp_dudley_school",
        question="What is the name of Dudley's private school?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(566), _sid(575), _sid(580)}),
        gold_answer_text="Smeltings.",
    ),
    # -------- List / enumeration -----------------------------------------
    # Answer is a list. Either one sentence enumerates all items, OR the
    # system must surface multiple distant sentences each naming one item.
    EvalQuestion(
        id="hp_four_houses",
        question="What are the four houses of Hogwarts?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(2323)}),
        gold_answer_text="Gryffindor, Hufflepuff, Ravenclaw, and Slytherin.",
    ),
    EvalQuestion(
        id="hp_ron_older_brothers",
        question="Name some of Ron Weasley's older brothers.",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(2039)}),
        gold_answer_text="Bill, Charlie, Percy, Fred, George (any subset).",
    ),
    # -------- Cross-chapter synthesis ------------------------------------
    # Answer requires combining passages across distant chapters.
    EvalQuestion(
        id="hp_learn_about_flamel",
        question="How do Harry, Ron, and Hermione discover who Nicolas Flamel is?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(2105),  # initial Dumbledore card mention (chapter 6, train)
                _sid(3897),  # Hagrid lets the name slip (chapter 13)
                _sid(3898),
                _sid(4418),  # Hermione's library re-discovery (chapter 13)
                _sid(4430),  # final answer — only known maker of the Stone
            }
        ),
        gold_answer_text=(
            "Harry first sees the name on a Chocolate Frog card describing "
            "Dumbledore's work on alchemy with Flamel; Hagrid later lets the "
            "name slip when guarding the Stone; Hermione finally re-finds "
            "the reference in a library book and identifies Flamel as the "
            "only known maker of the Sorcerer's Stone."
        ),
    ),
    EvalQuestion(
        id="hp_scar_voldemort_connection",
        question="What is the connection between Harry's scar and Voldemort?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(281),  # the scar will be forever (chapter 1)
                _sid(353),  # description of the lightning-bolt scar
                _sid(6057),  # scar burns near Voldemort/Quirrell (climax)
                _sid(6061),
            }
        ),
        gold_answer_text=(
            "Harry's lightning-bolt scar is the mark left when Voldemort "
            "tried (and failed) to kill him as a baby; when Harry is near "
            "Voldemort (via Quirrell) at the climax, the scar burns."
        ),
    ),
    # -------- Quote attribution (reverse lookup) -------------------------
    # Given an exact string from the book, find the speaker. Tests BM25
    # contribution to the hybrid retriever (the exact words ARE in the doc).
    EvalQuestion(
        id="hp_quote_welcome",
        question="Who says 'Welcome to Hogwarts'?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(2319)}),
        gold_answer_text="Professor McGonagall.",
    ),
    EvalQuestion(
        id="hp_quote_dwell_on_dreams",
        question=(
            "Who says 'It does not do to dwell on dreams and forget to live'?"
        ),
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset({_sid(4329), _sid(4330), _sid(4331), _sid(4332)}),
        gold_answer_text=(
            "Dumbledore, after finding Harry at the Mirror of Erised."
        ),
    ),
    # -------- Partial-information refusal --------------------------------
    # The topic exists in the book, but the specific question isn't answered.
    # System must say "I cannot answer this from the sources" — harder than
    # out-of-document refusal because relevant-looking passages WILL retrieve.
    EvalQuestion(
        id="hp_refuse_dumbledore_plan",
        question="What is Dumbledore's plan to permanently defeat Voldemort?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(),
        should_refuse=True,
    ),
    EvalQuestion(
        id="hp_refuse_petunia_lily_feelings",
        question=(
            "What were Aunt Petunia's true feelings about her sister Lily?"
        ),
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(),
        should_refuse=True,
    ),
    # -------- Misleading / distractor-rich -------------------------------
    # Many passages frame an obvious-but-WRONG answer. Tests whether the
    # system commits to the false suspect when distractors are plentiful.
    EvalQuestion(
        id="hp_steals_stone",
        question="Who attempts to steal the Sorcerer's Stone?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(
            {
                _sid(5898),  # "It wasn't even Voldemort" (climax — re: Snape)
                _sid(5943),  # Quirrell confessing his role
                _sid(5959),  # Voldemort showed me how wrong I was
            }
        ),
        gold_answer_text=(
            "Quirrell — possessed/aided by Voldemort. Not Snape, despite "
            "many earlier passages framing Snape as the suspect."
        ),
    ),
    EvalQuestion(
        id="hp_cursed_broomstick",
        question=(
            "Who cursed Harry's broomstick during his first Quidditch match?"
        ),
        document_paths=(_PDF,),
        # Truth is revealed at the climax: Quirrell, not Snape.
        # Early passages (s3869) explicitly accuse Snape — those are the
        # *distractors*. Gold credits citations to the climax revelation.
        gold_sentence_ids=frozenset({_sid(5943), _sid(5959)}),
        gold_answer_text=(
            "Quirrell (revealed at the climax). The book repeatedly frames "
            "Snape as the suspect, but Snape was actually counter-cursing "
            "the broomstick to save Harry."
        ),
    ),
    # -------- Refusal cases — fully out-of-document ----------------------
    # Information isn't in book 1 at all (e.g. from later books).
    EvalQuestion(
        id="hp_refuse_favorite_color",
        question="What is Harry Potter's favorite color?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(),
        should_refuse=True,
    ),
    EvalQuestion(
        id="hp_refuse_triwizard",
        question="Who wins the Triwizard Tournament?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(),
        should_refuse=True,
    ),
    EvalQuestion(
        id="hp_refuse_horcrux",
        question="How many Horcruxes did Voldemort create?",
        document_paths=(_PDF,),
        gold_sentence_ids=frozenset(),
        should_refuse=True,
    ),
]


class HarryPotterMicroBench:
    """15-question Harry Potter book 1 mini-benchmark."""

    name: str = "harry_potter_micro"

    def questions(self) -> Iterator[EvalQuestion]:
        yield from _QUESTIONS


__all__ = ["HarryPotterMicroBench"]
