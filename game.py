import constants as c
import deck
import player
import suitstack

class Game:
    def __init__(self, ai_list):
        self.ai_list = ai_list
        self.reset()

    def reset(self):
        # create the play area
        self.board = [suitstack.SuitStack(suit) for suit in c.suits]
        # create and shuffle the card deck
        self.deck = deck.Deck()
        self.deck.shuffle()
        # create the players
        self.players = [player.Player(ai) for ai in self.ai_list]
        # deal out the hands
        self.deal_hands()

    def deal_hands(self):
        while self.deck.size() > 0:
            self.players[self.deck.size() % 4].add_to_hand(self.deck.draw())

    def print_game(self, player = -1):
        for stack in self.board:
            stack.print_stack()
        if player != -1:
            self.players[player].print_hand()
        else:
            for player in self.players:
                player.print_hand()

    def is_game_over(self):
        for player in self.players:
            if player.hand_size() == 0:
                return True
        return False

    def get_winner(self):
        for player in self.players:
            if player.hand_size() == 0:
                return player.get_name()
        return ''

    def play_game(self):
        #self.print_game()
        turn = 0
        while not self.is_game_over():
            self.players[turn % 4].play(self.board)
            #self.print_game(turn % 4)
            turn += 1
        return self.get_winner()