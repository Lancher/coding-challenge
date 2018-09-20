# LEETCODE@ 664. Strange Printer
#
# --END--


def strangePrinter(self, s):
    if not s:
        return 0

    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]

    # dp[i][j] stands for the minimal turns we need for string from index i to index j.
    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            dp[i][i + l - 1] = l
            for j in range(i, i + l - 1):
                tmp = dp[i][j] + dp[j + 1][i + l - 1]
                if s[j] == s[i + l - 1]:
                    tmp -= 1
                dp[i][i + l - 1] = min(dp[i][i + l - 1], tmp)

    return dp[0][n - 1]
