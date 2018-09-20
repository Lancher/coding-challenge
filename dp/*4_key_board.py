# LEETCODE@ 651. 4 Keys Keyboard
#
# --END--


def maxA(self, n):
    dp = [i for i in range(n + 1)]
    for i in range(4, n + 1):
        for j in range(1, i - 2):
            # Example: AAAA
            #      i
            #   AAAA
            #   j
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
    return dp[n]
