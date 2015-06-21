"""Output a tree of stars like so:

    *
   ***
    *
   ***
  *****
    *
   ***
  *****
 *******

Input argument is the number of levels to the tree (3 in this example)
"""
from sys import argv


def main(levels):
    for level in xrange(levels):
        for sub_level in xrange(level+2):
            spaces = (levels+2-sub_level) * ' '
            stars = ((2 * sub_level) + 1) * '*'
            print '{spaces}{stars}'.format(spaces=spaces, stars=stars)


if __name__ == '__main__':
    main(int(argv[1]))
