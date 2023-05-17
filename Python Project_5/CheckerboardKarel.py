"""
File: CheckerboardKarel.py
Name: Ryan Chung
----------------------------
When I finish writing it, CheckerboardKarel should draw
a checkerboard using beepers.
I will make sure that my program works for all of the
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    CheckerboardKarel will draw a checkerboard using beepers.
    """
    put_beeper()
    if left_is_clear():
        if not front_is_clear():
            fill_one_line_north()
    while left_is_clear():
        fill_one_line_east()
        fill_one_line_west()
    fill_one_line_east()


def fill_one_line_north():
    turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def fill_one_line_east():
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()
    if front_is_clear():
        if not on_beeper():
            move()
            turn_left()
            put_beeper()
        else:
            move()
            turn_left()
            move()
            put_beeper()


def fill_one_line_west():
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_right()
    if front_is_clear():
        if not on_beeper():
            move()
            turn_right()
            put_beeper()
        else:
            move()
            turn_right()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
