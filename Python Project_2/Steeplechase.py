"""
File: Steeplechase.py
Name: Ryan Chung
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the right
    """
    up()
    cross()
    down()


def down():
    """
    Pre-condition: Karel is at the upper right, facing South
    Post-condition: Karel is at the lower right, facing South
    """
    while front_is_clear():
        move()


def up():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is facing North, at the upper left
    Comment/Un-comment: Command+/
    """
    turn_left()
    # Karel is facing North
    while not right_is_clear():
        move()


def cross():
    """
    Pre-condition: Karel is facing North, at the upper left
    Post-condition: Karel is facing South, at the upper right
    """
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
