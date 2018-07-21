import unittest
import Deck

class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck.Deck()

    def test_number_of_cards_in_deck(self):
        self.assertEqual(self.deck.size(), 52, "The deck should start with 52 cards.")
