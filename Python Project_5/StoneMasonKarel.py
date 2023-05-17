"""
File: StoneMasonKarel.py
Name: Ryan Chung
--------------------------------
At present, the StoneMasonKarel file does nothing.
My job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will build a column (a vertical structure that is 5 beepers tall) in
    each avenue that is either on the right or left side of the arch, and then
    Karel will end on the last avenue, 1st Street, facing east.
    """
    while front_is_clear():
        repair()
        for i in range(4):
            move()
    repair()


def turn_around():
    turn_left()
    turn_left()


def move_back():
    turn_around()
    for i in range(4):
        move()
    turn_left()


def repair():
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    move_back()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
