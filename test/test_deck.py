import unittest

from .context import Card
from .context import Deck

class TestTurn(unittest.TestCase):

    def setUp(self):
        pass

    def test_turn_has_a_card(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", 'STEM')
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        cards = [card1, card2, card3]
        deck = Deck(cards)

        self.assertEqual(deck.cards, [card1, card2, card3])
