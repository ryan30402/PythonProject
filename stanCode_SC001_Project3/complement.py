"""
File: complement.py
Name: Ryan Chung
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Determine the complement of each DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == '':
        return'DNA strand is missing.'

    # Build the complement of a given DNA sequence.
    complement = ""
    for sequence in dna:
        if sequence == 'A':
            complement += 'T'
        elif sequence == 'T':
            complement += 'A'
        elif sequence == 'C':
            complement += 'G'
        elif sequence == 'G':
            complement += 'C'

    return complement


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
