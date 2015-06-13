"""
Solution to Lowest common ancestor problem on codeeval:
https://www.codeeval.com/open_challenges/11/
Write a program to determine the lowest common ancestor of two nodes in a binary search tree. You may hardcode the following binary search tree in your program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29
INPUT SAMPLE:

The first argument is a path to a file that contains two values. These values represent two nodes within the tree, one per line. E.g.:

8 52
3 29
OUTPUT SAMPLE:

Print to stdout the lowest common ancestor, one per line. Lowest means the lowest depth in the tree, not the lowest value. E.g.:

30
8
"""
import sys


def find_path_to(node, tree=default):
    """Given node return path to as list of nodes."""
    pass


def lca(node1, node2):
    """Compare paths to nodes and return lowest common ancestor."""
    path1 = find_path_to(node1)
    path2 = find_path_to(node2)
    last = None
    for x, y in map(None, path1, path2):
        if x == y:
            last = x
        else:
            break
    return last


def main(input_file):
    with open(input_file) as f:
        line = f.readline()
        values = line.split(' ')
        lca(values[0], values[1])


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)