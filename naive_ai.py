class NaiveAI:
    def __init__(self, name):
        self.name = name

    def play(self, hand, board):
        for card in hand:
            for stack in board:
                if stack.add_to_stack(card):
                    hand.remove(card)
                    return True
        return False

    def get_name(self):
        return self.name