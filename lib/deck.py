class Deck(object):
    """docstring for Deck."""

    def __init__(self, cards):
        self.cards = cards

    def count(self):
        return len(self.cards)
