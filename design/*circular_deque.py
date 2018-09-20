# LEETCODE@ 641. Design Circular Deque
#
# --END--


class MyCircularDeque:
    def __init__(self, k):
        self.n = 0
        self.head = 0
        self.k = k
        self.arr = [None] * k

    def insertFront(self, value):
        if self.n != self.k:
            self.head = (self.head - 1) % self.k
            self.arr[self.head] = value
            self.n += 1
            return True
        else:
            return False

    def insertLast(self, value):
        if self.n != self.k:
            self.arr[(self.head + self.n) % self.k] = value
            self.n += 1
            return True
        else:
            return False

    def deleteFront(self):
        if self.n != 0:
            self.head = (self.head + 1) % self.k
            self.n -= 1
            return True
        else:
            return False

    def deleteLast(self):
        if self.n != 0:
            self.n -= 1
            return True
        else:
            return False

    def getFront(self):
        # Return -1 when empty
        if self.n == 0:
            return -1
        return self.arr[self.head]

    def getRear(self):
        # Return -1 when empty
        if self.n == 0:
            return -1
        return self.arr[(self.head + self.n - 1) % self.k]

    def isEmpty(self):
        return self.n == 0

    def isFull(self):
        return self.n == self.k
