import unittest
import deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = deck.Deck()

    def test_number_of_cards_in_deck(self):
        self.assertEqual(self.deck.size(), 52, "The deck should start with 52 cards.")

    def test_get_index_out_of_bounds(self):
        self.assertRaises(IndexError, self.deck.getIndex, -1)
        self.assertRaises(IndexError, self.deck.getIndex, 100)

    def test_deck_equals_itself(self):
        self.assertEqual(self.deck, self.deck, "The deck should be equal to itself.")

    def test_deck_equals_other_deck(self):
        otherDeck = deck.Deck()
        self.assertEqual(self.deck, otherDeck, "The two decks should have been equal.")

    def test_shuffling_deck(self):
        self.deck.shuffle()
        otherDeck = deck.Deck()
        self.assertEqual(self.deck, otherDeck, "The deck should have been reordered.")

    def test_draw_card_from_deck(self):
        card = self.deck.getIndex(0)
        self.assertEqual(self.deck.draw(), card, "Did not draw the top card of the deck.")
        self.assertEqual(self.deck.size(), 51, "Did not remove the card from the deck.")

if __name__ == '__main__':
    unittest.main()