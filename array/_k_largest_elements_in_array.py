# LEETCODE@ 215.Kth Largest Element in an Array
#
# 1. Use Quick Select
#
# --END--

from random import randint


def findKthLargest(self, nums, k):
    self.shuffle(nums)

    k = len(nums) - k
    lo, hi = 0, len(nums) - 1
    while True:
        p = self.partition(nums, lo, hi)
        if p == k:
            return nums[p]
        elif p < k:
            lo = p + 1
        else:
            hi = p - 1


def partition(self, nums, lo, hi):
    i = j = lo
    while j < hi:
        if nums[j] <= nums[hi]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums[i], nums[hi] = nums[hi], nums[i]
    return i


def shuffle(self, nums):
    for i in range(len(nums)):
        j = randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]
