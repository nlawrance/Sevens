import card
import deck

class Player():
    def __init__(self):
        self.hand = []

    # Adds the given card to the player's hand
    def add_to_hand(self, card):
        self.hand.append(card)

    # Returns the number of cards in the player's hand
    def hand_size(self):
        return len(self.hand)