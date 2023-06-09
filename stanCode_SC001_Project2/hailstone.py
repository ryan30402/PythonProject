"""
File: hailstone.py
Name: Ryan Chung
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print("This program computes Hailstone sequences.")
    print('')
    hailstone()


def hailstone():
    n = int(input('Enter a number: '))
    steps = 0
    while n != 1:
        if n % 2 == 0:
            print(n, 'is even, so I take half:', n // 2)
            n = n // 2
        else:
            print(n, 'is odd, so I make 3n+1:', 3 * n + 1)
            n = 3 * n + 1
        steps += 1

    print('It took', steps, 'steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
