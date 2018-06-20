# LEETCODE@ 97. Interleaving String
#
# --END--


def isInterleave(self, s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    m, n = len(s1), len(s2)

    # 1) dp initialization
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dp[0][0] = 1

    # 2) row --> go down
    for i in range(m):
        if s1[i] == s3[i]:
            dp[i + 1][0] = dp[i][0]

    # 3) col --> go right
    for j in range(n):
        if s2[j] == s3[j]:
            dp[0][j + 1] = dp[0][j]

    # 4) dp
    for i in range(m):
        for j in range(n):
            k = i + j + 1
            if s1[i] == s3[k] and s2[j] != s3[k]:
                dp[i + 1][j + 1] = dp[i][j + 1]
            if s2[j] == s3[k] and s1[i] != s3[k]:
                dp[i + 1][j + 1] = dp[i + 1][j]
            if s1[i] == s3[k] and s2[j] == s3[k]:
                dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]
    return dp[m][n] == 1
