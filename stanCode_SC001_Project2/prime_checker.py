"""
File: prime_checker.py
Name: Ryan Chung
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
# This number controls when to stop the program
EXIT = -100


def main():
	"""
	The main function checks if a number is prime.
	"""
	print("Welcome to the prime checker!")
	while True:
		n = int(input('n:'))
		if n == EXIT:
			print('Have a good one!')
			break
		elif n == 1:
			print(n, "is not a prime number")
		elif n > 1:  # If given number is greater than 1
			for i in range(2, n):
				if (n % i) == 0:
					print(n, "is not a prime number")
					break
			else:
				print(n, "is a prime number")
		else:
			print(n, "is not a prime number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
