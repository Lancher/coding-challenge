# LEETCODE@ 650. 2 Keys Keyboard
#
# 1. TODO: O(n) solution
#
# --END


def minSteps(self, n):
    dp = [0] * (1 + n)

    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                dp[i] = dp[j] + int(i / j)
                break
    return dp[n]
