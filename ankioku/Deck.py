from typing import List, Set
from .Card import Card
# __init__ -> create
# get
# share
# tag
# search
# schedule
# save


class Deck:
    def __init__(self, name: str):
        self.id = "test"
        self.name: str = name
        self._tags: Set[str] = set()
        self._cards: List[Card] = []

    def __repr__(self) -> str:
        return f'{self.name} - A deck of {len(self._cards)} cards.'

    @property
    def tags(self) -> Set[str]:
        return self._tags

    @tags.setter
    def tags(self, tag: str) -> None:
        if len(tag) > 140:
            raise ValueError('Length of tag too long.')
        self._tags.add(tag)

    @property
    def cards(self) -> List[Card]:
        return self._cards

    @cards.setter
    def cards(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError('Card is incorrect object type.')
        self._cards.append(card)
