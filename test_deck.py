import card
import constants as c
import deck
import unittest

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = deck.Deck()

    def test_number_of_cards_in_deck(self):
        self.assertEqual(self.deck.size(), 52, "The deck should start with 52 cards.")

    def test_get_index_out_of_bounds(self):
        self.assertRaises(IndexError, self.deck.getIndex, -1)
        self.assertRaises(IndexError, self.deck.getIndex, 52)

    def test_get_index_top_card_of_deck(self):
        top_card = self.deck.getIndex(0)
        king_diamonds = card.Card(c.suits[-1], 13)
        self.assertEqual(top_card, king_diamonds, 
            "An incorrect index was returned.\nWas '{0}' but should be '{1}'".format(top_card, king_diamonds))

    def test_deck_equals_itself(self):
        self.assertEqual(self.deck, self.deck, "The deck should be equal to itself.")

    def test_deck_equals_other_deck(self):
        otherDeck = deck.Deck()
        self.assertEqual(self.deck, otherDeck, "The two decks should have been equal.")

    def test_shuffling_deck(self):
        self.deck.shuffle()
        otherDeck = deck.Deck()
        self.assertNotEqual(self.deck, otherDeck, "The deck should have been reordered.")

    def test_draw_card_from_deck(self):
        card = self.deck.getIndex(0)
        drawn_card = self.deck.draw()
        self.assertEqual(drawn_card, card, "Did not draw the top card of the deck.")
        self.assertEqual(self.deck.size(), 51, "Did not remove the card from the deck.")

if __name__ == '__main__':
    unittest.main()