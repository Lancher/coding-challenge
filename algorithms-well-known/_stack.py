# 1. linked list
#
# --END--


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class StackInLinkedList:

    def __init__(self):
        self.head = Node(None)

    def empty(self):
        return self.head.next is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head.next
        self.head.next = new_node

    def pop(self):
        item = self.head.next.item
        self.head.next = self.head.next.next
        return item


# 1. array
#
# --END--


class StackInArray:
    def __init__(self):
        self.n = 0
        self.capacity = 8
        self.array = [None] * self.capacity

    def empty(self):
        return self.n == 0

    def push(self, item):
        # double
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.n] = item
        self.n += 1

    def pop(self):
        self.n -= 1
        item = self.array[self.n]
        # one-quarter
        if 0 < self.capacity / 4 and self.n == self.capacity / 4:
            self.resize(self.capacity / 4)
        return item

    def resize(self, next_capacity):
        new_array = [None] * next_capacity
        new_array[:self.n] = self.array[:]
        self.array = new_array
        self.capacity = next_capacity
