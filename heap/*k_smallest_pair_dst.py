# LEETCODE@ 719. Find K-th Smallest Pair Distance
#
# --END--


def smallestDistancePair(self, nums, k):
    # trail & errors
    n = len(nums)

    nums.sort()

    lo, hi = 0, nums[n - 1] - nums[0]

    while lo < hi:
        mi = int((lo + hi) / 2)

        cnt = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] - nums[i] <= mi:
                j += 1
            cnt += j - i - 1

        if cnt < k:
            lo = mi + 1
        else:
            hi = mi

    return lo


import heapq


class Solution:
    def smallestDistancePair(self, nums, k):
        n = len(nums)
        print(n)

        # sort
        nums.sort()

        # visited
        vst = set()

        # push to heap
        h = []
        for i in range(n - 1):
            heapq.heappush(h, [abs(nums[i] - nums[i + 1]), i, i + 1])
            vst.add((i, i + 1))

        # pop k items
        res = 0
        for i in range(k):
            val, i, j = heapq.heappop(h)
            j += 1
            res = val
            if j < n:
                heapq.heappush(h, [abs(nums[i] - nums[j]), i, j])
        return res