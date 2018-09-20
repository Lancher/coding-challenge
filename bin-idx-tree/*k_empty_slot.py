# LEETCODE@ 683. K Empty Slots
#
# --END--


class BIT:

    def __init__(self, nums):
        # n + 1 for the dummy node 0
        self.bits = [0] * (len(nums) + 1)

    def update(self, i, val):
        while i < len(self.bits):
            self.bits[i] += val
            # find next element
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.bits[i]
            # find parent element
            i -= i & -i
        return s


class Solution:
    def kEmptySlots(self, flowers, k):
        bit = BIT(flowers)

        days = set()
        n = len(flowers)
        for i in range(n):
            bit.update(flowers[i], 1)
            days.add(flowers[i])
            # check the difference between v & v - k - 1
            if flowers[i] - k - 1 in days:
                if bit.prefix_sum(flowers[i]) - bit.prefix_sum(flowers[i] - k - 1) == 1:
                    return i + 1

            # check the difference between v & v + k + 1
            if flowers[i] + k + 1 in days:
                if bit.prefix_sum(flowers[i] + k + 1) - bit.prefix_sum(flowers[i]) == 1:
                    return i + 1
        return -1
