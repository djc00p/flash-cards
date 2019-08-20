import unittest

from .context import Card
from .context import Deck

class TestTurn(unittest.TestCase):

    def setUp(self):
        pass

    def test_deck_has_a_cards(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", 'STEM')
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        cards = [card1, card2, card3]
        deck = Deck(cards)

        self.assertEqual(deck.cards, [card1, card2, card3])

    def test_deck_has_a_card_count(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", 'STEM')
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        cards = [card1, card2, card3]
        deck = Deck(cards)

        self.assertEqual(deck.count(), 3)

    def test_deck_returns_cards_in_STEM_category(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        cards = [card1, card2, card3]
        deck = Deck(cards)
        # import pdb; pdb.set_trace()
        self.assertEqual(deck.cards_in_category("STEM"), [card2, card3])

    def test_deck_returns_cards_in_Geography_category(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        cards = [card1, card2, card3]
        deck = Deck(cards)
        # import pdb; pdb.set_trace()
        self.assertEqual(deck.cards_in_category("Geography"), [card1])
        
    def test_deck_returns_no_cards_in_PopCulture_category(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        cards = [card1, card2, card3]
        deck = Deck(cards)
        # import pdb; pdb.set_trace()
        self.assertEqual(deck.cards_in_category("Pop Culture"), [])
