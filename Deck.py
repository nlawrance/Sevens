import Constants
from random import shuffle

class Deck():
    def __init__(self):
        self.cards = [0 for value in range(1,14) for suit in Constants.suits]

    # Returns the number of cards in the deck
    def size(self):
        return len(self.cards)

    # Returns the card at the given index
    # throws IndexError if the index is out of bounds
    def getIndex(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index {0} is out of bounds for deck.".format(index))
        return self.cards[index]