import Constants

class Deck():
    def __init__(self):
        self.cards = [0 for value in range(1,14) for suit in Constants.suits]

    # Returns the number of cards in the deck
    def size(self):
        return len(self.cards)