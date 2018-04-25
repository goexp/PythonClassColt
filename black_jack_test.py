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
		self.deck=Deck(Card)
	
	def tearDown(self):
		pass
	
	def test_init(self):
		"""Each instance should have a cards attribute with all 52 possible instances of Card"""
		all_cards=[Card(suit,value) for suit in Card.valid_suits for value in Card.valid_values]
		isEqual=True
		cards_from_deck = str(self.deck.deal_hand(52))
		for card in all_cards:
			if not str(card) in cards_from_deck:
				isEqual=False
		self.assertTrue(isEqual)

	def test_count(self):
		"""Should return how many cards remain in a deck"""
		self.assertEqual(self.deck.count(),52)
		self.deck.deal_card()
		self.assertEqual(self.deck.count(),51)

	def test_repr(self):
		"""Should return how many cards are left in a deck eg. 'Deck of 52 cards'"""
		self.assertEqual(str(self.deck),"Deck of 52 cards")
		self.deck.deal_card()
		self.assertEqual(str(self.deck),"Deck of 51 cards")
	
	def test_deal(self):
		"""Accepts a number and removes that many cards from a deck. If there are no cards left it returns a valueError 'All cards have been dealt'"""
		all_cards=self.deck._deal(52)
		self.assertEqual(self.deck.count(),0)
		raised_exception=False
		try:
			self.deck._deal(1)
		except ValueError:
			raised_exception=True
		self.assertTrue(raised_exception)		

	def test_shuffle(self):
		"""Should shuffle a full deck. If any are missing it should return a valueError 'Only full decks can be shuffled'"""
		pass
	def test_deal_card(self):
		"""Should deal one card from the deck"""
		pass
	def test_deal_hand(self):
		"""Accepts a number and deals that many cards from the deck in a list"""
		pass

if __name__ == '__main__':
	unittest.main()
		