"""
File: quadratic_solver.py
Name: Ryan Chung
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0

"""

import math


def main():
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b * b - 4 * a * c
	sqrt = math.sqrt(abs(discriminant))
	if a != 0:
		if discriminant > 0:
			print('Two roots: ', end='')
			print((-b + sqrt)/(2 * a), end=' , ')
			print((-b - sqrt)/(2 * a))
		elif discriminant == 0:
			print('One root: ', end='')
			print(-b / (2 * a))
		elif discriminant < 0:
			print('No real roots')
	else:
		print('The parameter "a" cannot be zero. Please start it over!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
