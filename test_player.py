import card
import constants as c
import player
import unittest

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.player = player.Player()

    def test_start_with_empty_hand(self):
        self.assertEqual(self.player.hand_size(), 0, "The player should start with an empty hand.")

    def test_add_card_to_hand(self):
        ace_spades = card.Card(c.spades, 1)
        self.player.add_to_hand(ace_spades)
        self.assertEqual(self.player.hand_size(), 1, "The player should have one card in their hand.")

if __name__ == '__main__':
    unittest.main()