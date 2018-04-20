import unittest
from black_jack import Card,Deck

class Card_test(unittest.TestCase):
	def setUp(self):
		self.card=Card("Diamonds","K")
	def tearDown(self):
		pass
	def test_init(self):
		"""cards should have a suit and value"""
		self.assertEqual(self.card.suit,"Diamonds")
		self.assertEqual(self.card.value,"K")
	def test_repr(self):
		"""repr should return a string VALUE of SUIT"""
		self.assertEqual(repr(self.card), "K of Diamonds")

class Deck_test(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_init(self):
		"""Each instance should have a cards attribute with all 52 possible instances of Card"""
	def test_count(self):
		"""Should return how many cards remain in a deck"""
	def test_repr(self):
		"""Should return how many cards are left in a deck eg. 'Deck of 52 cards'"""
	def test_deal(self):
		"""Accepts a number and removes that many cards from a deck. If there are no cards left it returns a valueError 'All cards have been dealt'"""
	def test_shuffle(self):
		"""Should shuffle a full deck. If any are missing it should return a valueError 'Only full decks can be shuffled'"""
	def test_deal_card(self):
		"""Should deal one card from the deck"""
	def test_deal_hand(self):
		"""Accepts a number and deals that many cards from the deck in a list"""

if __name__ == '__main__':
	unittest.main()
		