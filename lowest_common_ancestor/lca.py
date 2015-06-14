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


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Bst():
    def __init__(self):
        self.start = None
        self.nodes = set()

    def _insert(self, node, curr):
        if node.value < curr.value:
            if curr.left:
                self._insert(node, curr.left)
            else:
                curr.left = node
        else:
            if curr.right:
                self._insert(node, curr.right)
            else:
                curr.right = node

    def insert(self, val):
        if self.contains(val):
            print "Value already in tree."
            return None
        new = Node(val)
        if self.start is None:
            self.start = new
        else:
            self._insert(new, self.start)

    def contains(self, val):
        for node in self.nodes:
            if val == node.value:
                return True
        return False


def find_path_to(node, tree):
    """Given node return path to as list of nodes."""
    out = []
    if tree.contains(node):
        return None
    current = tree.start
    while True:
        out.append(current.value)
        if node == current.value:
            break
        if node < current.value:
            current = current.left
        else:
            current = current.right
    return out


def lca(node1, node2, tree):
    """Compare paths to nodes and return lowest common ancestor."""
    path1 = find_path_to(node1, tree)
    path2 = find_path_to(node2, tree)
    last = None
    for x, y in map(None, path1, path2):
        if x == y:
            last = x
        else:
            break
    return last


def main(input_file):
    tree = Bst()
    list_of_nodes = [30, 8, 52, 3, 20, 10, 29]
    for x in list_of_nodes:
        tree.insert(x)
    with open(input_file) as f:
        for line in f:
            values = [int(value.strip()) for value in line.split(' ')]
            print lca(values[0], values[1], tree)


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
