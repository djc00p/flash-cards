import unittest

from .context import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_card_has_a_question(self):
        card = Card("What is the capital of Alaska?")
        q = card.question
        self.assertEqual(q,"What is the capital of Alaska?")
