# Count Smaller After Self
#
# 1) use binary indexed tree
#
# 2) use segment tree
#
# 3) merge sort
#
# --END--


class BIT:
    def __init__(self, nums):
        self.arr = [0] * (len(nums) + 1)

    def update(self, i, v):
        while i < len(self.arr):
            self.arr[i] += v
            i += i & -i

    def prefix_sum(self, i):
        re = 0
        while 0 < i:
            re += self.arr[i]
            i -= i & -i
        return re


class Solution:
    def countSmaller(self, nums):
        d = {}
        for i, v in enumerate(sorted(list(set(nums)))):
            d[v] = i + 1

        bit = BIT(nums)

        re = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            bit.update(d[nums[i]], 1)
            re[i] = bit.prefix_sum(d[nums[i]] - 1)
        return re
