from random import randint

#Rules from https://codereview.stackexchange.com/questions/14441/oop-in-rock-paper-scissors-program

CHOICES = ['rock','paper','scissors']

RULES = {
    'rock': {'scissors': 'blunts' },
    'paper': {'rock': 'covers' },
    'scissors': {'paper': 'cuts' },
        }

computer_wins=0
user_wins=0


while  True:
	computer = CHOICES[randint(0,2)]

	user=None
	while user not in CHOICES:
		user= input("Select - rock, paper or scissors: ")

	computer_won=False
	user_won=False

	if computer in RULES[user]:
		user_won=True
		user_wins+=1
		print(user.capitalize()+" "+RULES[user][computer]+" "+computer+". You won!")		
	elif user in RULES[computer]:
		computer_won=True
		computer_wins+=1
		print(computer.capitalize()+" "+RULES[computer][user]+" "+user+". Computer won!")		
	elif computer_won==user_won:
		print(computer+" and "+user+" is a draw.")


	print("Computer wins="+str(computer_wins)+" | User wins="+str(user_wins))

	if input("Would you like to play again (y/n) ") == 'n':
		break

	print()
