import unittest

from .context import Card
from .context import Turn
from .context import Deck
from .context import Round

class TestTurn(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        self.card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", 'STEM')
        self.card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "STEM")

        self.deck = Deck([self.card1, self.card2, self.card3])

        self.round = Round(self.deck)

    def test_round_has_a_deck(self):
        self.assertEqual(self.round.deck, self.deck)

    def test_round_has_an_empty_array_for_turns(self):
        self.assertEqual(self.round.turns, [])

    def test_round_has_a_current_card(self):
        self.assertEqual(self.round.current_card, self.card1)

    def test_round_take_turn(self):
        new_turn = self.round.take_turn('Juneau')
        self.assertIsInstance(new_turn, Turn)
        self.assertTrue(new_turn.correct)
