from random import shuffle as rnd_shuffle
from pyfiglet import figlet_format
from termcolor import colored

BLACKJACK = 21

class Card:
	valid_suits=("Hearts","Diamonds","Clubs","Spades")
	valid_values=("A","2","3","4","5","6","7","8","9","10","J","Q","K")

	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	def __repr__(self):
		return f"{self.value} of {self.suit}"
	
	def get_black_jack_value(self,ace=11):
		if self.value in ["J","K","Q"]:
			return 10
		if self.value in ["A"]:
			return ace
		return int(self.value)
	
	@property
	def suit(self):
		return self._suit
	@suit.setter
	def suit(self,suit):
		if not (suit in Card.valid_suits):
			raise ValueError("Must be one of "+", ".join(Card.valid_suits)+".")
		self._suit=suit

	@property
	def value(self):
		return self._value
	@value.setter
	def value(self,value):
		if not (value in Card.valid_values):
			raise ValueError("Must be one of "+", ".join(Card.valid_values)+".")
		self._value=value


class Deck:
	def __init__(self):
		self.cards=[Card(suit,value) for suit in Card.valid_suits for value in Card.valid_values]
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

	print(f"You have {user} which has a value of {user_value}")
	print(f"The computer has {computer} which has a value of {computer_value}")

	while computer_value < BLACKJACK and user_value < BLACKJACK: 
		if input("Would you like to  draw (y/n) ") == 'y':
			user+=the_deck.deal_card()
			user_value=sum([item.get_black_jack_value() for item in user])
			user_value_ace_1=sum([item.get_black_jack_value(1) for item in user])
			if user_value > BLACKJACK:
				user_value=user_value_ace_1
			print(f"You now have {user} your blackjack total is {user_value}")
		
		if (computer_value < (BLACKJACK - 4) and user_value < (BLACKJACK+1)) or (computer_value < user_value and user_value <= BLACKJACK):
			computer+=the_deck.deal_card()
			computer_value=sum([item.get_black_jack_value() for item in computer])
			computer_value_ace_1=sum([item.get_black_jack_value(1) for item in computer])
			if computer_value > BLACKJACK:
				computer_value=computer_value_ace_1
			print(f"The computer has {computer} his blackjack total is {computer_value}")

	if computer_value > BLACKJACK or (user_value <= BLACKJACK and user_value > computer_value):
		user_won=True
		user_wins+=1
		print("You won!")		
	elif user_value > BLACKJACK or (computer_value <= BLACKJACK and computer_value > user_value):
		computer_won=True
		computer_wins+=1
		print("Computer won!")		
	else:
		print("It is a draw.")

	print("Computer wins="+str(computer_wins)+" | User wins="+str(user_wins))

	if input("Would you like to play again (y/n) ") == 'n':
		break

	print()