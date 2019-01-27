import card as cd
import constants as c

class SuitStack:
    # set up stack
    def __init__(self, suit):
        if suit not in c.suits:
            raise ValueError("{} is not a valid suit for a SuitStack.".format(suit))
        self.lowest_value = None
        self.highest_value = None
        self.suit = suit

    # Returns the lowest value in the stack
    def get_lowest_value(self):
        return self.lowest_value
         
    # Returns the highest value in the stack
    def get_highest_value(self):
        return self.highest_value

    # Returns True is the given card can be added to the stack
    def can_add_to_stack(self, card):
        if not isinstance(card, cd.Card):
            raise ValueError("Only cards can be added to a stack.")
        if card.suit != self.suit:
            return False
        if card.value == 7:
            if self.get_highest_value() == None and self.get_lowest_value() == None:
                return True
        elif card.value < 7:
            if card.value == self.get_lowest_value() - 1:
                return True
        else:
            if card.value == self.get_highest_value() + 1:
                return True
        return False

    # Attempts to add a card to the stack
    # Returns True if successful
    def add_to_stack(self, card):
        if not isinstance(card, cd.Card):
            raise ValueError("Only cards can be added to a stack.")
        if not self.can_add_to_stack(card):
            raise False
        if card.value <= 7:
            self.lowest_value = card.value
        if card.value >= 7:
            self.highest_value = card.value
        return True