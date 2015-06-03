"""Code eval Fizz Buzz"""
import sys


def main(filename):
    """Open file and perform fizz_buzz on each line."""
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            fizz_buzz(line)


def divisible(num, denom):
    """Return true if num is divisible by denom, false otherwise."""
    return bool(num % denom == 0)


def fizz_buzz(line):
    """Print correct fizz buzz output given input line."""
    inp = line.split(' ')
    x, y, num = int(inp[0]), int(inp[1]), int(inp[2])
    output = []
    for num in xrange(1, num+1):
        if divisible(num, x) and divisible(num, y):
            output.append('FB')
        elif divisible(num, x):
            output.append('F')
        elif divisible(num, y):
            output.append('B')
        else:
            output.append(str(num))
    print ' '.join(output)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
