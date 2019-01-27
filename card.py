import constants as c

class Card():
    # suit must be one of the four defined suits
    # value must be an integer from 1 to 13
    def __init__(self, suit, value):
        if suit not in c.suits:
            raise ValueError("'{0}' is not a suit.".format(suit))
        if value < 1 or value > 13:
            raise ValueError("'{0}' does not correspond to a card value".format(value))
        self.suit = suit
        self.value = value

    # Returns True if the other card has the same suit and value
    def __eq__(self, other):
        if isinstance(other, Card):
            if self.suit == other.suit and self.value == other.value:
                return True
        return False

    def __str__(self):
        value_string = ''
        if self.value == 1:
            value_string = 'A'
        elif self.value == 11:
            value_string = 'J'
        elif self.value == 12:
            value_string = 'Q'
        elif self.value == 13:
            value_string = 'K'
        else:
            value_string = str(self.value)
        return self.suit + value_string