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


def findNumberOfLIS(self, nums):
    if not nums:
        return 0
    n = len(nums)

    # ln[i] the longest length sebseq endw at i
    # cnt[i] the number of longest length sebseq endw at i
    dp_ln = [1] * n
    dp_cnt = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                ln, cnt = dp_ln[j] + 1, dp_cnt[j]
                # we found the better length, we can abandon the shorter length since it wont affect our answer
                if ln > dp_ln[i]:
                    dp_ln[i] = ln
                    dp_cnt[i] = cnt
                # if we found the same length, that is also the solution ends at i.
                elif ln == dp_ln[i]:
                    dp_cnt[i] += cnt

    res = 0
    max_ln = max(dp_ln)
    for i in range(n):
        if dp_ln[i] == max_ln:
            res += dp_cnt[i]
    return res