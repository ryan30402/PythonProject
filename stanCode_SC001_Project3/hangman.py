"""
File: hangman.py
Name: Ryan Chung
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: Play a hangman game where the user has a limited number of guesses.
    """
    dashed = random_word()  # Get a random word to guess
    starting_word = '-' * len(dashed)   # Create a string with dashes to represent the hidden word
    print('The word looks like ' + starting_word)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    chances = N_TURNS   # Initialize the remaining number of guesses
    encrypted_letters = len(dashed)  # Track the number of letters yet to be guessed
    while True:
        input_ch = ""   # Store the guessed letters and the missing letters
        guess = input('Your guess: ')   # Prompt the user to enter a letter
        guess = guess.upper()   # Convert the guess to uppercase for case-insensitive comparison
        if len(guess) != 1:
            print('Illegal format.')
        elif not guess.isalpha():
            print('Illegal format.')
        elif starting_word.find(guess) != -1:   # Checks if the guessed letter is present in the word
            print('You are correct!')
        else:   # If the guessed letter is not in the word, the following steps are performed
            for i in range(len(dashed)):    # A loop iterates through each letter in the word.
                ch = dashed[i]
                # If the letter matches the guessed letter, the encrypted_letters variable is decreased by 1,
                # and the letter is added to the input_ch string.
                if ch == guess:
                    encrypted_letters -= 1
                    input_ch += ch
                # Otherwise, the corresponding character from starting_word is added to the input_ch string.
                else:
                    input_ch += starting_word[i]
            if input_ch == starting_word:
                chances -= 1
                print('There is no ' + guess + '\'s in the word.')
            else:
                starting_word = input_ch
                print('You are correct!')
        if chances == 0:
            print('You are completely hung : ( ')
            print('The word was: ' + dashed)
            return
        elif encrypted_letters == 0:
            print('You win!! ')
            print('The word was: ' + dashed)
            return
        print('The word looks like' + starting_word)
        print('You have ' + str(chances) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
