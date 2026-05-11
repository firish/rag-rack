"""Harry Potter book 1 mini-benchmark — 15 hand-curated questions.

Source: tests/parsers/fixtures/sample.pdf (Harry Potter and the Sorcerer's Stone).
Sentence IDs were located by keyword search against the parsed Document
(see examples/_lookup_sentences.py).

Gold sets are inclusive — any of the listed sentence_ids is an acceptable
citation. The Tier 1 metric (set overlap) gives credit for any intersection.

Question mix:
  * 9 easy / direct factual
  * 3 multi-source synthesis (may struggle without contextual retrieval)
  * 3 refusal cases (information not in book 1)
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
    # -------- Refusal cases (info not in book 1) ---------------------------
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
