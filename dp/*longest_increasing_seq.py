# LEECODE@ 300. Longest Increasing Subsequence
#
# 1) when dealing with DP problems, make sure you have empty array.
#
# 2) Solution 1 is DP n^2.
#
# 3) Solution 2 is Binary Search
#
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
#
# --END--


def lengthOfLIS(self, nums):
    # 1) remember the empty one
    if not nums:
        return 0
    # 2) dp for remembering the largest length of sebseq at
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(nums)


def lengthOfLIS(self, nums):
    # 1) set the array to `inf` to ensure
    n = len(nums)
    dp = [float('inf')] * (n + 1)
    res = 0

    for num in nums:
        # 2) like finding next insertion position
        lo, hi = 1, n
        while lo < hi:
            mi = int((lo + hi) / 2)
            if dp[mi] < num:
                lo = mi + 1
            else:
                hi = mi
        dp[lo] = num
        res = max(res, lo)
    return res
