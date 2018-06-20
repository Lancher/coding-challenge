# LEETCODE@ 238. Product of Array Except Self
#
# --END--


def productExceptSelf(self, nums):
    n = len(nums)
    res = [1] * n

    p = 1
    for i in range(n):
        res[i] *= p
        p *= nums[i]

    p = 1
    for i in range(n - 1, -1, -1):
        res[i] *= p
        p *= nums[i]

    return res
