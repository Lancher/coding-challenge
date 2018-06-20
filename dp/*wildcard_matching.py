# LEETCODE@ 44. Wildcard Matching
#
# --END--


def isMatch(self, s, p):
    dp = [[0 for j in range(len(p) + 1)] for i in range(len(s) + 1)]
    dp[0][0] = 1

    for j in range(len(p)):
        if p[j] == '*':
            dp[0][j + 1] = dp[0][j]

    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == '?' or s[i] == p[j]:
                dp[i + 1][j + 1] = dp[i][j]
            if p[j] == '*':
                dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j] or dp[i][j + 1]

    return bool(dp[len(s)][len(p)])
