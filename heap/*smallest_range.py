# LEETCODE@ 632. Smallest Range
#
# --END--
import heapq


def smallestRange(self, nums):
    # push to the heap
    h = []
    for i in range(len(nums)):
        heapq.heappush(h, (nums[i][0], i, 0))

    res = [float('-inf'), float('inf')]

    # From left to right will contain all the rows at once!!!!!!
    right = max(row[0] for row in nums)
    while h:
        left, i, j = heapq.heappop(h)
        if right - left < res[1] - res[0]:
            res = [left, right]
        if j + 1 == len(nums[i]):
            return res
        v = nums[i][j + 1]
        # Update right to make sure all the rows stay between left & right
        right = max(right, v)
        heapq.heappush(h, (v, i, j + 1))