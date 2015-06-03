"""Code eval Fizz Buzz"""
import sys


def main(filename):
    """Open file and perform fizz_buzz on each line."""
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            fizz_buzz(line)


def fizz_buzz(line):
    """Print correct fizz buzz output given input line."""
    inp = line.split(' ')
    x, y, num = int(inp[0]), int(inp[1]), int(inp[2])
    output = []
    for num in xrange(1, num+1):
        if bool(num % x == 0) and bool(num % y == 0):
            output.append('FB')
        elif bool(num % x == 0):
            output.append('F')
        elif bool(num % y == 0):
            output.append('B')
        else:
            output.append(str(num))
    print ' '.join(output)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
