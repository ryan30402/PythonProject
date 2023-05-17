"""
File: MidpointKarel.py
Name: Ryan Chung
----------------------------
When I finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but is allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    if front_is_clear():
        fill_one_line()
        remove_beeper()
    else:
        put_beeper()
    if not front_is_clear():
        turn_around()
        while not on_beeper():
            move()
    if not on_beeper():
        move()


def remove_beeper():
    turn_around()
    pick_beeper()
    while front_is_clear():
        while front_is_clear():
            move()
        turn_around()
        while not on_beeper():
            move()
        move()
        if on_beeper():
            turn_around()
            move()
            pick_beeper()
            turn_around()
        else:
            if not front_is_clear():
                turn_around()
                while not on_beeper():
                    move()
            if not on_beeper():
                move()


def fill_one_line():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
