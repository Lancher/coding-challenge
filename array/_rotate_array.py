# LEETCODE@ 189. Rotate Array
#
# 1. Reverse n - k, Reverse k, Reverse all.
#
# --END--


def rotate(self, nums, k):
    k %= len(nums)
    k = len(nums) - k
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, len(nums) - 1)
    self.reverse(nums, 0, len(nums) - 1)


def reverse(self, nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1
