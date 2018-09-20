# LEETCODE@ 629. K Inverse Pairs Array
#
# 1. https://leetcode.com/problems/k-inverse-pairs-array/discuss/104825/Shared-my-C++-O(n-*-k)-solution-with-explanation
#
# --END--


def kInversePairs(self, n, k):
    mod = 10 ** 9 + 7
    # n = 3, k = 1
    # [1, 2, 3] => [1, 3, 2]
    #           => [2, 1, 3]

    # n = 3, k = 2
    # [1, 2, 3] => [3, 1, 2] one swap
    #           => [2, 3, 1] two swap

    # n = 4, k = 2
    # [1, 2, 3, 4] => [3, 1, 2, 4] one swap
    #              => [2, 3, 1, 4] two swap
    #              => [1, 4, 3, 2] one swap
    #              => [1, 2, 4, 3] one swap + 2 possible swaps

    # ----> k (0 ~ k)
    # |
    # |
    # v
    # n (1 ~ n)
    dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
    dp[0][0] = 1

    # dp[i][j] //represent the number of permutations of (1...n) with k inverse pairs.
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j-2] + ..... +dp[i-1][j - i + 1]
    for i in range(1, n + 1):
        for j in range(0, k + 1):
            for m in range(0, i):
                if 0 <= j - m <= k:
                    dp[i][j] += dp[i - 1][j - m]
                    dp[i][j] %= mod

    return dp[n][k]