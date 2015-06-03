"""
Solution to code eval string permutations:
https://www.codeeval.com/open_challenges/14/
Write a program which prints all the permutations of a string in alphabetical
order. We consider that digits < upper case letters < lower case letters. The
sorting should be performed in ascending order.
"""
import sys
from itertools import permutations


def main(filename):
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            _permutations(line)


def _permutations(line):
    """Given input line, return all permutations in alphabetical order."""
    perm = permutations(line.rstrip())
    # itertools.permutations returns a generator, convert to list.
    perm = list(perm)
    output = []
    for x in perm:
        output.append(''.join(x))
    output.sort()
    print ','.join(output)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
