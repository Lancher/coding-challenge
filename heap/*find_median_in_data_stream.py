# LEETCODE@ 295. Find Median from Data Stream
#
# --END--


import heapq


class MedianFinder(object):
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        # 1) the small maintain a MaxHeap & the large maintain a MinHeap
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        # 2) make sure the large one is always greater or equal
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self):
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0
