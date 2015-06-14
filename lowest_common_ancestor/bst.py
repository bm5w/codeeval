"""
Binary Search Tree implementation using nodes.
"""


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
