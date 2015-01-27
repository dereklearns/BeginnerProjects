import random

secretnum = random.randrange(1,11)

guess = None
attempts = 0
flag = True

while flag == True:
	guess = int(raw_input("Guess a number between 1-10...\t"))
	attempts += 1

	if guess > secretnum:
		print "Too high"
	elif guess < secretnum:
		print "Too low"
	else:
		print "You guessed the secret number in " + str(attempts) + " tries!"