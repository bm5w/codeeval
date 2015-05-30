"""Code eval Fizz Buzz"""
import sys


def main(filename):
    """Open file and perform fizz_buzz on each line."""
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            fizz_buzz(line)


def divisible(num, denom):
    """Return true if num is divisible by denom, false otherwise."""
    if num % denom == 0:
        return True
    else:
        return False


def fizz_buzz(line):
    """Print correct fizz buzz output given input line."""
    inp = line.split(' ')
    x, y, num = int(inp[0]), int(inp[1]), int(inp[2])
    output = []
    for num in xrange(1, num+1):
        out = ''
        if divisible(num, x):
            out = 'F'
        if divisible(num, y):
            out = '{}B'.format(out)
        if not out:
            output.append(str(num))
        else:
            output.append(out)
    print ' '.join(output)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
