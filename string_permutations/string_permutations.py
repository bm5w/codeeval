"""
Solution to code eval string permutations:
https://www.codeeval.com/open_challenges/14/
Write a program which prints all the permutations of a string in alphabetical
order. We consider that digits < upper case letters < lower case letters. The
sorting should be performed in ascending order.
"""
import sys
from itertools import permutations


def _permutations(line):
    """Given input line, return all permutations in alphabetical order."""
    perm = permutations(line.rstrip())
    output = [''.join(x) for x in perm]
    output.sort()
    print ','.join(output)

with open(sys.argv[1], 'r') as file_handle:
    for line in file_handle:
        _permutations(line)
