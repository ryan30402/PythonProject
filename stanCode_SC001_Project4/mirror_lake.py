"""
File: mirror_lake.py
Name: Ryan Chung
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: mt-rainier.jpg
    :return: A reflected image that creates a mirror lake vibe.
    """
    img = SimpleImage(filename)

    # Create a new blank with double height
    reflect_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            reflect_img_pixel1 = reflect_img.get_pixel(x, y)
            reflect_img_pixel1.red = img_pixel.red
            reflect_img_pixel1.green = img_pixel.green
            reflect_img_pixel1.blue = img_pixel.blue

            # Mirror the upper half and paste it as the lower half
            reflect_img_pixel2 = reflect_img.get_pixel(x, img.height*2 - y - 1)
            reflect_img_pixel2.red = img_pixel.red
            reflect_img_pixel2.green = img_pixel.green
            reflect_img_pixel2.blue = img_pixel.blue
    return reflect_img


def main():
    """
    Create a new image that creates a mirror lake vibe by placing an inverse image of
    mt-rainier.jpg below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
