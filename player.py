import card
import deck

class Player():
    def __init__(self, name):
        self.hand = []
        self.name = name

    # Adds the given card to the player's hand
    def add_to_hand(self, card):
        self.hand.append(card)

    # Returns the number of cards in the player's hand
    def hand_size(self):
        return len(self.hand)

    # Returns the name of the player
    def get_name(self):
        return self.name

    def print_hand(self):
        print(self.name, end=": ")
        for card in self.hand:
            print(card, end=" ")
        print()

    def play(self, board):
        for card in self.hand:
            for stack in board:
                if stack.add_to_stack(card):
                    self.hand.remove(card)
                    return True
        return False