from .turn import Turn

class Round(object):
    """docstring for Round."""

    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.current_card = deck.cards[0]

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card)
        return turn
