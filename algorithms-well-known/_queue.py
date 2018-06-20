# 1. linked list
#
# --END--


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class QueueInLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def empty(self):
        return self.head.next is None

    def put(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        self.tail = new_node

    def get(self):
        item = self.head.next.item
        self.head.next = self.head.next.next
        if self.empty():
            self.tail = self.head
        return item


# 1. array
#
# --END--
class QueueInArray:

    def __init__(self):
        self.head = 0
        self.tail = 0
        self.capacity = 8
        self.array = [None] * self.capacity

    def empty(self):
        return self.head == self.tail

    def put(self, item):
        if self.tail == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.tail] = item
        self.tail += 1

    def get(self):
        item = self.array[self.head]
        self.head += 1
        # the minimum capacity is 1
        if self.tail > self.head and self.tail - self.head == self.capacity / 4:
            self.resize(self.capacity / 4)
        return item

    def resize(self, next_capacity):
        new_array = [None] * next_capacity
        new_array[:self.tail-self.head] = self.array[self.head:self.tail]
        self.array = new_array
        self.capacity = next_capacity
        self.head, self.tail = 0, self.tail - self.head
