# LEETCODE@ 634. Find the Derangement of An Array
#
# 1. Let D(N) be the required answer. The recursion for the number of derangements of N is:
#    D(N) = (N-1) * (D(N-1) + D(N-2)).
#
# --END--


def findDerangement(self, n):
    mod = 10 ** 9 + 7
    dp = [1, 0]
    for i in range(2, n + 1):
        dp[0], dp[1] = dp[1], (i - 1) * (dp[0] + dp[1]) % mod
    return dp[1]
