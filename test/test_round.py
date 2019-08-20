import unittest

from .context import Card
from .context import Turn
from .context import Deck
from .context import Round

class TestTurn(unittest.TestCase):

    def setUp(self):
        pass

    def test_round_has_a_deck(self):
        card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", 'STEM')
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        deck = Deck([card1, card2, card3])

        round = Round(deck)

        self.assertEqual(round.deck, deck)
