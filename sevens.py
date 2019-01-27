import constants as c
import deck
import player
import suitstack

class Sevens:
    def __init__(self):
        self.reset()

    def reset(self):
        # create the play area
        self.board = [suitstack.SuitStack(suit) for suit in c.suits]
        # create and shuffle the card deck
        self.deck = deck.Deck()
        self.deck.shuffle()
        # create the players
        self.player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
        self.players = [player.Player(name) for name in self.player_names]
        # deal out the hands
        self.deal_hands()

    def deal_hands(self):
        while self.deck.size() > 0:
            self.players[self.deck.size() % 4].add_to_hand(self.deck.draw())

    def print_game(self):
        for stack in self.board:
            stack.print_stack()
        for player in self.players:
            player.print_hand()