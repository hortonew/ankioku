from typing import Dict, Set
from dataclasses import dataclass
from datetime import date  # , timedelta, datetime


@dataclass
class AccessHistory:
    last_acceseed: date
    correctness_history: Dict[date, bool]


class Card:
    def __init__(self):
        self.id = "test"
        self._tags: Set[str] = set()
        self._question: str = ""
        self._answer: str = ""
        self.access_history: AccessHistory = {}

    def __repr__(self) -> str:
        return self._question

    @property
    def question(self) -> str:
        return self._question

    @question.setter
    def question(self, question: str):
        if len(question) > 140:
            raise ValueError('Length of question > maximum.')
        self._question = question

    @property
    def answer(self) -> str:
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        if len(answer) > 140:
            raise ValueError('Length of answer > maximum.')
        self._answer = answer

    @property
    def tags(self) -> Set[str]:
        return self._tags

    @tags.setter
    def tags(self, tag: str) -> None:
        if len(tag) > 140:
            raise ValueError('Length of tag too long.')
        self._tags.add(tag)
