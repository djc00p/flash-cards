import unittest

from .context import Card
from .context import Turn

class TestTurn(unittest.TestCase):

    def setUp(self):
        pass

    def test_turn_has_a_card(self):
        card = Card("What is the capital of Alaska?", "Juneau", 'Geography')
        turn = Turn("Juneau", card)

        self.assertEqual(turn.card, card)
