from typing import Set
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

    def __repr__(self) -> str:
        return self.name

    @property
    def tags(self) -> Set[str]:
        return self._tags

    @tags.setter
    def tags(self, tag: str) -> None:
        if len(tag) > 140:
            raise ValueError('Length of tag too long.')
        self._tags.add(tag)
