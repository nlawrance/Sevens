import card
import constants as c
import suitstack
import unittest

class TestSuitStack(unittest.TestCase):
    def setUp(self):
        self.suit_stack = suitstack.SuitStack(c.spades)

    def test_no_initial_lowest_value(self):
        self.assertEqual(self.suit_stack.get_lowest_value(), None, "There should be no initial lowest value.")

    def test_no_initial_highest_value(self):
        self.assertEqual(self.suit_stack.get_highest_value(), None, "There should be no initial highest value.")

    def test_can_add_seven_if_empty(self):
        seven_spades = card.Card(c.spades, 7)
        result = self.suit_stack.can_add_to_stack(seven_spades)
        self.assertTrue(result, "Seven should be able to be added to an empty stack.")

    def test_cannot_add_card_from_wrong_suit(self):
        seven_hearts = card.Card(c.hearts, 7)
        result = self.suit_stack.can_add_to_stack(seven_hearts)
        self.assertFalse(result, "Seven should not be able to add a card from the worng suit.")

if __name__ == '__main__':
    unittest.main()