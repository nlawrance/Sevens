import constants as c
import card
from random import shuffle

class Deck():
    def __init__(self):
        self.cards = [card.Card(suit, value) for value in range(1,14) for suit in c.suits]

    # Returns the number of cards in the deck
    def size(self):
        return len(self.cards)

    # Returns the card at the given index
    # throws IndexError if the index is out of bounds
    def getIndex(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index {0} is out of bounds for deck.".format(index))
        return self.cards[self.size() - index - 1]

    # Override of the 'equals' operator
    # Returns True if the decks have the same number of cards in the same order
    def __eq__(self, other):
        if isinstance(other, Deck):
            if self.size() == other.size():
                for i in range(0, self.size()):
                    if self.getIndex(i) != other.getIndex(i):
                        return False
                return True
        return False

    # Randomises the order of the cards in the deck
    def shuffle(self):
        shuffle(self.cards)

    # Removes and returns the top card of the deck
    def draw(self):
        return self.cards.pop()