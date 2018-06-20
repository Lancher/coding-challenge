# 1. Python heap is min heap
#
#   import heapq
#   h = []
#   heapq.heappush(h, n)
#   heapq.heappop(h)
#
# 2. Push to end, swim up.
#
#          0[ 6 ]
#          /     \
#         /       \
#     1[ 8 ]   2[ 23 ]   <= parent is (i - 1) / 2
#        /
#       /
#    3[ 2 ]              <= current is i, new append value 2 should swim up
#
# 3. Pop from head, sink down.
#
#          0[ 2 ]                      0[ 8 ]        <= 8 have to sink down
#          /     \                     /     \
#         /       \                   /       \
#     1[ 6 ]   2[ 23 ]   ==>      1[ 6 ]   2[ 23 ]   <= children is (i * 2 + 1) & (i * 2 + 2)
#        /                          /
#       /                          /
#    3[ 8 ]                    3[ X ]
#
#
# --END--


class MinHeap:

    def __init__(self):
        self.n = 0
        self.capacity = 16
        self.arr = [None] * self.capacity

    def empty(self):
        return self.n == 0

    def push(self, val):
        # resize array
        if self.n == self.capacity:
            self._resize(self.capacity * 2)
        self.arr[self.n] = val
        self._swim(self.n)
        self.n += 1

    def _swim(self, i):
        while i > 0 and self.arr[i] < self.arr[(i-1)/2]:
            self.arr[i], self.arr[(i-1)/2] = self.arr[(i-1)/2], self.arr[i]
            i = (i - 1) / 2

    def pop(self):
        val = self.arr[0]
        self.n -= 1
        self.arr[0], self.arr[self.n] = self.arr[self.n], self.arr[0]
        # resize array
        if self.n and self.n == self.capacity / 4:
            self._resize(self.capacity / 4)
        self._sink(0)
        return val

    def _sink(self, i):
        j = i * 2 + 1
        while j < self.n:
            if j + 1 < self.n and self.arr[j+1] < self.arr[j]:
                j += 1
            if self.arr[i] < self.arr[j]:
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i, j = j, j * 2 + 1

    def _resize(self, n_capacity):
        new_arr = [None] * n_capacity
        new_arr[:self.n] = self.arr[:]
        self.arr = new_arr
        self.capacity = n_capacity
