import pytest
import random
import string
from ankioku.Deck import Deck
from ankioku.Card import Card


@pytest.fixture
def deck() -> Deck:
    return Deck('Test Deck')


@pytest.fixture
def card() -> Card:
    return Card()


def test_deck_attributes(deck: Deck) -> None:
    assert deck.name == "Test Deck"
    assert repr(deck) == "Test Deck"

    attributes = ['id', 'name']
    for attribute in attributes:
        assert hasattr(deck, attribute)


def test_deck_tags(deck: Deck) -> None:
    assert deck.tags == set()
    with pytest.raises(ValueError):
        tag_too_long = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(141)
        )
        deck.tags = tag_too_long

    assert deck.tags == set()
    deck.tags = 'test'
    deck.tags = 'test'
    deck.tags = 'another'
    assert deck.tags == {'test', 'another'}
    assert isinstance(deck.tags, set)
    deck.tags.remove('test')
    assert deck.tags == {'another'}


def test_card_attributes(card: Card) -> None:
    assert card.question == ""
    assert repr(card) == ""
    attributes = ['id']
    for attribute in attributes:
        assert hasattr(card, attribute)


def test_card_tags(card: Card) -> None:
    assert card.tags == set()
    with pytest.raises(ValueError):
        tag_too_long = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(141)
        )
        card.tags = tag_too_long

    assert card.tags == set()
    card.tags = 'test'
    card.tags = 'test'
    card.tags = 'another'
    assert card.tags == {'test', 'another'}
    assert isinstance(card.tags, set)
    card.tags.remove('test')
    assert card.tags == {'another'}


def test_card_questions(card: Card) -> None:
    valid_question = "What color is the sky?"
    card.question = valid_question
    assert card.question == valid_question

    # Question should be < 140 characters
    with pytest.raises(ValueError):
        question_too_long = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(141)
        )

        card.question = question_too_long

    assert card.question == valid_question
