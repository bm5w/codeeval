"""
Solution to code eval interrupted bubble sort:
https://www.codeeval.com/open_challenges/158/
"""


def main(filename):
    """Open file and perform bubble_sort on each line."""
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            interrupted_bs(line)


def interrupted_bs(line):
    """Parse input line and preform bubble sort X times.
    X is defined as the integer after '|' on line."""
    temp = line.split('|')
    num = int(temp[1])
    temp[0] = temp[0].rstrip()
    inputL = [int(x) for x in temp[0].split(' ')]
    for x in xrange(num):
        inputL = bubble_sort(inputL)
    # convert back to string
    print ' '.join(map(str, inputL))


def bubble_sort(inputL):
    """One iteration of bubble sort.
    Return None if already sorted."""
    changed = False
    for num in xrange(len(inputL)-1):
        if inputL[num+1] < inputL[num]:
            inputL[num+1], inputL[num] = inputL[num], inputL[num+1]
            changed = True
    if not changed:
        return None
    return inputL


if __name__ == '__main__':
    main('input.txt')
