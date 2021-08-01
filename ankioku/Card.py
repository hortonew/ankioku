from typing import Set
# get
# get_image -> s3
# save
# save_image -> s3
# ask
# reveal
# share
# tag
# attr
# # time_to_forget
# # relates_to
# rate (save metric)


class Card:
    def __init__(self):
        self.id = "test"
        self._tags: Set[str] = set()
        self._question: str = ""

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
    def tags(self) -> Set[str]:
        return self._tags

    @tags.setter
    def tags(self, tag: str) -> None:
        if len(tag) > 140:
            raise ValueError('Length of tag too long.')
        self._tags.add(tag)
