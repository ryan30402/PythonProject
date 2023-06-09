"""
File: caesar.py
Name: Ryan Chung
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: Input a number to produce shifted ALPHABET as the cipher table.
    """
    sec_num = int(input('Secret number:'))
    new_alphabet = ALPHABET[26-sec_num:]+ALPHABET[:26-sec_num]  # Generate shifted alphabet based on secret number
    ciphered_str = input('What\'s the ciphered string?')    # Prompt the user to enter the ciphered string
    ciphered_str = ciphered_str.upper()  # Convert the ciphered string to uppercase for case-insensitive comparison
    ans = ""    # Store the deciphered string

    # Iterate through each character in the ciphered string
    for i in range(len(ciphered_str)):
        for j in range(26):
            if ciphered_str[i].isalpha():
                if ciphered_str[i] == new_alphabet[j]:
                    ans += ALPHABET[j]
                elif ciphered_str[i] == "":
                    ans += ""
            else:
                ans += ciphered_str[i]
                break
    print('The deciphered string is: ' + ans)

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
