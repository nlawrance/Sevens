import unittest
import Deck

class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck.Deck()

    def test_number_of_cards_in_deck(self):
        self.assertEqual(self.deck.size(), 52, "The deck should start with 52 cards.")

    def test_get_index_out_of_bounds(self):
        self.assertRaises(IndexError, self.deck.getIndex, -1)
        self.assertRaises(IndexError, self.deck.getIndex, 100)