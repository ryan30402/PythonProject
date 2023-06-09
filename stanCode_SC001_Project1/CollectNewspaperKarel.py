"""
File: CollectNewspaperKarel.py
Name: Ryan Chung
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
My job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will walk to the door of its house, pick up the newspaper, and then return to its
    initial position in the upper left corner of the house.
    """
    move()
    go_in()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    move()
    go_in()
    turn_right()
    put_beeper()


def turn_right():
    """
    This function turns Karel to the left 3 times
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    This function turns Karel to the left 2 times
    """
    turn_left()
    turn_left()


def go_in():
    move()
    turn_right()
    move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
