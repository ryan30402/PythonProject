"""
File: find_max.py
Name: Ryan Chung
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = 100   # Sentinel value


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('This program finds the max!')
    data = int(input('Data: '))
    if data == EXIT:
        print('No data')
    else:
        maximum = data
        while True:
            data = int(input('Data: '))
            if data == EXIT:
                break
            if maximum < data:
                maximum = data

        print('The max: '+str(maximum))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
