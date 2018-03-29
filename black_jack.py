from random import shuffle as rnd_shuffle
from pyfiglet import figlet_format
from termcolor import colored

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
	def get_black_jack_value(self):
		if self.value in ["J","K","Q"]:
			return 10
		if self.value in ["A"]:
			return 11
		return int(self.value)

class Deck:
	def __init__(self):
		self.cards = []
		for suit in Card.valid_suits:
			for value in Card.valid_values:
				self.cards.insert(0,Card(suit,value))
	def count(self):
		return len(self.cards)
	def __repr__(self):
		return f"Deck of {Deck.count(self)} cards"
	def _deal(self,num):
		if Deck.count(self)==0:
			raise ValueError("All cards have been dealt")
		if num > Deck.count(self):
			num = Deck.count(self)
		return [self.cards.pop() for x in range(num)]
	def shuffle(self):
		if Deck.count(self) != 52:
			raise ValueError("Only full decks can be shuffled")
		rnd_shuffle(self.cards)
		return self.cards
	def deal_card(self):
		return Deck._deal(self,1)
	def deal_hand(self,num):
		return Deck._deal(self,num)


computer_wins=0
user_wins=0

print(colored(figlet_format("Black Jack 1999"),color="white"))

while  True:
	computer_won=False
	user_won=False
	the_deck=Deck()
	the_deck.shuffle()
	computer = the_deck.deal_card()
	user=the_deck.deal_card()
	computer_value=sum([item.get_black_jack_value() for item in computer])
	user_value=sum([item.get_black_jack_value() for item in user])

	print(f"The computer has {computer} which has a value of {computer_value}")
	print(f"You have {user} which has a value of {user_value}")

	while computer_value < 13 and user_value < 13: 
		if input("Would you like to  draw (y/n) ") == 'y':
			user+=the_deck.deal_card()
			user_value=sum([item.get_black_jack_value() for item in user])
			print(f"You now have {user} your blackjack total is {user_value}")
		else:
			computer+=the_deck.deal_card()
			computer_value=sum([item.get_black_jack_value() for item in computer])
			print(f"He has {computer} his blackjack total is {computer_value}")

	if computer_value > 13 or (user_value <= 13 and user_value > computer_value):
		user_won=True
		user_wins+=1
		print("You won!")		
	elif user_value > 13 or (computer_value <= 13 and computer_value > user_value):
		computer_won=True
		computer_wins+=1
		print("Computer won!")		
	else:
		print("It is a draw.")

	print("Computer wins="+str(computer_wins)+" | User wins="+str(user_wins))

	if input("Would you like to play again (y/n) ") == 'n':
		break

	print()