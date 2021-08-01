from ankioku.Deck import Deck
from ankioku.Card import Card


def test_deck_attributes() -> None:
    d = Deck()
    attributes = ['id']
    for attribute in attributes:
        assert hasattr(d, attribute)


def test_card_attributes() -> None:
    c = Card()
    attributes = ['id']
    for attribute in attributes:
        assert hasattr(c, attribute)
