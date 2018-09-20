# LEETCODE@ 622. Design Circular Queue
#
# --END--


class MyCircularQueue:

    def __init__(self, k):
        self.arr = [None] * k
        self.k = k
        # use n to determine if we can enqueue or dequeue array.
        self.n = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        if self.n < self.k:
            nxt_rear = (self.rear + 1) % self.k
            self.arr[self.rear] = value
            self.rear = nxt_rear
            self.n += 1
            return True
        else:
            return False

    def deQueue(self):
        if self.n > 0:
            self.front = (self.front + 1) % self.k
            self.n -= 1
            return True
        else:
            return False

    def Front(self):
        return -1 if self.n == 0 else self.arr[self.front]

    def Rear(self):
        return -1 if self.n == 0 else self.arr[(self.rear - 1) % self.k]

    def isEmpty(self):
        return self.n == 0

    def isFull(self):
        return self.n == self.k