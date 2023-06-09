"""
File: fire.py
Name: Ryan Chung
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: greenland-fire.png
    :return: image with highlighted red spots on fire
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.green+pixel.blue)//3   # Calculate the average of RGB pixel
        if pixel.red > avg * HURDLE_FACTOR:           # If the red pixel exceed the assigned value (avg*HURDLE_FACTOR)
            pixel.red = 255                           # Highlight fire pixel
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg                           # Else, switch to gray pixel
            pixel.green = avg
            pixel.blue = avg

    return img


def main():
    """
    Detects the pixels that are recognized as fire
    and highlights them for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
