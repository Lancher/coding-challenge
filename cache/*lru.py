# LEETCODE@ 146. LRU Cache
#
# 1) Double Linkedlist + hash
#
# --END--


class Node:
    def __init__(self, key, val, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt


class DoubleLinkedList:
    def __init__(self):
        # use real head & tail
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def add_head(self, node):
        # add to head
        nxt = self.head.nxt
        nxt.pre = node
        node.nxt = nxt
        node.pre = self.head
        self.head.nxt = node

    def move_head(self, node):
        # remove node
        nxt = node.nxt
        pre = node.pre
        nxt.pre = pre
        pre.nxt = nxt
        # add to head
        self.add_head(node)

    def pop_tail(self):
        # pop node
        node = self.tail.pre
        pre = node.pre
        self.tail.pre = pre
        pre.nxt = self.tail
        return node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.d = {}
        self.ll = DoubleLinkedList()

    def get(self, key):
        if key in self.d:
            self.ll.move_head(self.d[key])
            return self.d[key].val
        else:
            return -1

    def put(self, key, value):
        # add node
        if key in self.d:
            self.d[key].val = value
            self.ll.move_head(self.d[key])
        else:
            self.length += 1
            node = Node(key, value)
            self.d[key] = node
            self.ll.add_head(node)
        # remove exceed one
        if self.length > self.capacity:
            self.length -= 1
            node = self.ll.pop_tail()
            self.d.pop(node.key)
