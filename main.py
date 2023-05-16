import random 

#Random number generator 
n = random.randrange(1,10) 
#User is prompted to guess # between 1-10
guess = int(input("Enter any number between 1-10: "))

while n !=guess: #if guess is too low, message below
		if guess < n: 
			print("Number is too low")
			guess = int(input("Try another number: "))
		else: #if guess is too high, message below
			print("Number is too high")
			guess = int(input("Enter a number again: "))
#User has guessed correctly
print("You guessed it right!")
