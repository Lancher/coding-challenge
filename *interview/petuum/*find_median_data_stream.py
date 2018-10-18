

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # add to max_heap
        heapq.heappush(self.max_heap, -num)
        # balance the heap
        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)

        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0] / 1.0
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0