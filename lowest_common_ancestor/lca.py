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


class bst():
    def __init__(self):
        '''Initialize a bst with a start value and dictionary of nodes.'''
        self.start = None
        self.nodes = {}

    def _insert(self, node, val):
        '''Recursive helper method for insert.'''
        if node < val:
            if self.nodes[node].get('right') is None:
                self.nodes[node]['right'] = val
                self.nodes[val] = {'parent': node}

            else:
                self._insert(self.nodes[node]['right'], val)
        else:
            if self.nodes[node].get('left') is None:
                self.nodes[node]['left'] = val
                self.nodes[val] = {'parent': node}
            else:
                self._insert(self.nodes[node]['left'], val)

    def insert(self, val):
        '''Insert a value into the bst unless already present.'''
        if self.contains(val):
            return None
        if self.start is None:
            self.start = val
            self.nodes[val] = {}
        else:
            self._insert(self.start, val)

    def contains(self, val):
        '''Will return True if the value is in the bst.'''
        return val in self.nodes

    def left(self, node):
        return self.nodes[node].get('left')

    def right(self, node):
        return self.nodes[node].get('right')


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)