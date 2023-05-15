import random 

#Random number generator 
n = random.randrange(1,10) 

guess = int(input("Enter any number between 1-10: "))

while n !=guess: 
		if guess < n: 
			print("Number is too low")
			guess = int(input("Try another number: "))
		else: 
			print("Number is too high")
			guess = int(input("Enter a number again: "))

print("You guessed it right!")