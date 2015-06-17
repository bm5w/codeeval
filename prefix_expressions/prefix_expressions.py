from sys import argv


class Node(object):
    """A Node Class representing a Node in a queue.
    Each node has a pointer to the next node and a value.
    """

    def __init__(self, value, back=None):
        """Create Node with value and optional pointer.
        If no pointer is specified, pointer is set to None.
        """
        self.point_previous = back
        self.value = value


class Queue(object):
    """Class defining a queue data structure."""

    def __init__(self):
        """Create a queue with a pointer to the front and back of an empty queue
        and set count to zero to keep track of size"""
        self.front = None
        self.back = None
        self.count = 0

    def enqueue(self, value):
        """Adds a node with the value to the back of the queue"""
        old_back = self.back
        self.back = Node(value)
        if self.size() > 0:  # if any Nodes: set back previous to current Node
            old_back.point_previous = self.back
        else:  # adding to an empty, than define front
            self.front = self.back
        self.count += 1

    def dequeue(self):
        """Returns a value of the front node and removes it from the queue
        If the qpopulated_queueueue is empty, return AttributeError."""
        try:
            val = self.front.value
            self.front = self.front.point_previous
        except AttributeError:
            raise AttributeError(u"Queue is empty")
        self.count -= 1
        return val

    def peek(self):
        """Returns a value of the front node"""
        try:
            return self.front.value
        except AttributeError:
            raise AttributeError(u"Queue is empty")

    def size(self):
        """Returns the size of the queue"""
        return self.count


def perform(operator, index, nums):
    left = nums.dequeue()
    for count in xrange(index):
        nums.enqueue(nums.dequeue())
    right = nums.dequeue()

    if operator == '*':
        new = left * right
    elif operator == '/':
        if right > 0:
            new = left / right
        else:
            new = 0
    else:
        new = left + right
    nums.enqueue(new)
    for remaining in xrange(nums.size()-1-index):
        nums.enqueue(nums.dequeue())
    return nums


def prefix(line):
    nums_and_operators = line.split(' ')
    index = len(nums_and_operators) // 2
    operators, nums_list = nums_and_operators[:index], nums_and_operators[index:]
    nums = Queue()
    for x in nums_list:
        nums.enqueue(int(x))
    # for x in nums_and_operators:
    #     if ord(x) >= 48 and ord(x) <= 57:
    #         nums.enqueue(int(x))
    #     else:
    #         operators.append(x)
    possible_operators = [u'*', u'/', u'+']

    for operator in possible_operators:
        try:
            index = operators.index(operator)
            if index >= 0:
                nums = perform(operator, index, nums)
                operators.remove(operator)
        except ValueError:
            pass

    return nums.peek()


def main(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            print prefix(line)


if __name__ == '__main__':
    main(argv[1])
