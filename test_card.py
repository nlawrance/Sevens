import card
import constants as c
import unittest

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = card.Card(c.spades, 1)

    def test_invalid_suit(self):
        self.assertRaises(ValueError, card.Card, "royals", 1)

    def test_invalid_value(self):
        self.assertRaises(ValueError, card.Card, c.clubs, 0)
        self.assertRaises(ValueError, card.Card, c.clubs, 14)

    def test_card_equal_to_itself(self):
        self.assertEqual(self.card, self.card, "A card should be equal to itself.")

    def test_card_equal_to_other_card(self):
        other_card = card.Card(c.spades, 1)
        self.assertEqual(self.card, other_card, "The two cards should be equal.")

    def test_card_not_equal_to_other_card(self):
        ace_hearts = card.Card(c.hearts, 1)
        two_spades = card.Card(c.spades, 2)
        self.assertNotEqual(self.card, ace_hearts, "Cards of different suits should not be equal.")
        self.assertNotEqual(self.card, two_spades, "Cards with different values should not be equal.")

if __name__ == '__main__':
    unittest.main()