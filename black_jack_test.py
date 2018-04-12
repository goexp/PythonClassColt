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

#    def test_sample(self):
    	#eg.
        #self.assertEqual(1, 1)
        #self.asserRaises(ValueError)
        #---more options---
        #assertTrue(a, Message)
		#assertFalse(a, Message)
		#assertEqual(a, b, Message)
		#assertNotEqual(a, b, Message)
		#assertIs(a, b, Message)
		#assertIsNot(a, b, Message)
		#assertIsNone(a, Message)
		#assertIsNotNone(a, Message)
		#assertIsInstance(a,b,M)
		#assertIsNotInstance(a, b, Message)
		#assertGreater(a, b, Message)
		#assertLess(a, b, Message)
		#assertGreaterEqual(a, b, Message)
		#assertLessEqual(a, b, Message)
		#assertAlmostEqual(a, b, n, Message)
		#assertNotAlmostEqual(a, b, n, Message)
		#assertItemsEqual(a, b, Message)

if __name__ == '__main__':
	unittest.main()
		