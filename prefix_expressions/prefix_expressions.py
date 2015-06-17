"""
Solution for code eval problem:
https://www.codeeval.com/open_challenges/7/

PREFIX EXPRESSIONS
CHALLENGE DESCRIPTION:

You are given a prefix expression. Write a program which evaluates it.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains one prefix expression per line.

For example:


1
* + 2 3 4
Your program should read this file and insert it into any data structure you like. Traverse this data structure and evaluate the prefix expression. Each token is delimited by a whitespace. You may assume that sum ‘+’, multiplication ‘*’ and division ‘/’ are the only valid operators appearing in the test data.

OUTPUT SAMPLE:

Print to stdout the output of the prefix expression, one per line.

For example:


1
20
CONSTRAINTS:

The evaluation result will always be an integer ≥ 0.
The number of the test cases is ≤ 40.
"""
from sys import argv



def prefix(line):
    pass



def main(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            print prefix(line)


if __name__ == '__main__':
    main(argv[1])