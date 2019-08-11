class Turn(object):
    """docstring for Turn."""

    def __init__(self, guess, card):
        self.guess = guess
        self.card = card

    def correct(self):
        self.guess == self.card.answer

    def feedback(self):
        if correct == true:
            print("Correct!!")
        else:
            print("Incorrect!!")
