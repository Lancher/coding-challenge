# LEETCODE@ 674. Longest Continuous Increasing Subsequence
#
# 1. Easy & straight forward.
#
# --END--


def findLengthOfLCIS(self, nums):
    if not nums:
        return 0

    # current maximum & real maximum
    cur, res = 1, 1

    # iterate the array nums
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            cur += 1
            res = max(res, cur)
        else:
            cur = 1
    return res
