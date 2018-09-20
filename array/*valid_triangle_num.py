# LEETCODE@ 611. Valid Triangle Number
#
# 1. Similar to n-num problems.
#
# --END--


def triangleNumber(self, nums):
    # sort it first
    nums.sort()
    n = len(nums)

    res = 0
    for i in range(n - 1, 1, -1):
        l, r = 0, i - 1
        while l < r:
            # if the sum of the smallest two value is greater than the largest, we can build triangle.
            if nums[l] + nums[r] > nums[i]:
                # if l + r is greater i, l+1 + r must be greater than i.
                # hence, we decrease r.
                res += r - l
                r -= 1
            else:
                l += 1
    return res
