# LEETCODE@ 115. Distinct Subsequences
#
# 1) Transfer S to T
#
# 2) Example
#
#       ""  r  a  b  b  i  t
#   ""   1  0  0  0  0  0  0
#    r   1  2  0  0  0  0  0
#    a   1
#    b   1
#    b   1
#    b   1
#    i   1
#    t   1
#
# --END--


def numDistinct(self, s, t):
    m, n = len(s), len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # 1) initialization
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(m):
        for j in range(n):
            # 2) only s can be reduced
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
    return dp[m][n]
