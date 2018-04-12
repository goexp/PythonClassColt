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

if __name__ == '__main__':
	unittest.main()
		