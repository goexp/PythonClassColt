class Card:
	valid_suits=("Hearts","Diamonds","Clubs","Spades")
	valid_values=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
	def __init__(self,suit,value):
		Card._setSuit(self,suit)
		Card._setValue(self,value)
	def __repr__(self):
		return f"{self.value} of {self.suit}"
	def _setSuit(self,suit):
		if not (suit in Card.valid_suits):
			raise ValueError("Must be one of "+", ".join(Card.valid_suits)+".")
		self.suit=suit
	def _setValue(self,value):
		if not (value in Card.valid_values):
			raise ValueError("Must be one of "+", ".join(Card.valid_values)+".")
		self.value=value