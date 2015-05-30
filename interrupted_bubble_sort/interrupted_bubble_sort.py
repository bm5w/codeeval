"""
Solution to code eval interrupted bubble sort:
https://www.codeeval.com/open_challenges/158/
"""
import sys


def bubble_sort(inputL):
    """One iteration of bubble sort."""
    for num in xrange(len(inputL)-1):
        if inputL[num+1] < inputL[num]:
            inputL[num+1], inputL[num] = inputL[num], inputL[num+1]
    return inputL


def interrupted_bs(line):
    """Parse input line and preform bubble sort X times.
    X is defined as the integer after '|' on line."""
    temp = line.split('|')
    num = int(temp[1].rstrip())
    temp[0] = temp[0].rstrip()
    inputL = [int(x) for x in temp[0].split(' ')]
    for x in xrange(num):
        old = list(inputL)
        inputL = bubble_sort(inputL)
        # check if sorted
        if old == inputL:
            break
    # convert back to string
    print ' '.join(map(str, inputL))


def main(filename):
    """Open file and perform bubble_sort on each line."""
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            interrupted_bs(line)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
