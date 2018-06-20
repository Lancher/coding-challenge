# LEETCODE@ 225. Implement Stack using Queues
#
# 1. push(): just push it.
#
# 2. pop(): just pop & push n - 1 items
#
# 3. top(): the idea is the same as push()
#
# --END--


import queue


class MyStack(object):
    def __init__(self):
        self.q = queue.Queue()

    def push(self, x):
        self.q.put(x)

    def pop(self):
        sz = self.q.qsize()
        for _ in range(sz - 1):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self):
        sz = self.q.qsize()
        for _ in range(sz - 1):
            self.q.put(self.q.get())
        val = self.q.get()
        self.q.put(val)
        return val

    def empty(self):
        return self.q.empty()


# LEETCODE@ 232. Implement Queue using Stacks
#
# Use two stacks s1 & s2, s2 for the buffer array.
#
# 1. push(): just push it.
#
# 2. pop(): just pop & push n - 1 items
#
# 3. top(): the idea is the same as push()
#
# --END


class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2

