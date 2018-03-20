from random import randint

while True:
	number=randint(1,10)
	guess=None
	while number != guess:
		guess=int(input("Guess a number between 1 and 10: "))
		if guess == number:
			print("You guessed right!")
		elif guess < number:
			print("Your guess is too low.")
		else:
			print("Your guess is too high.")
	if input("Would you like to play again (y/n)") == "n":
		break
	else:
		print()