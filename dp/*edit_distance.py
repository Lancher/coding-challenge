# LEETCODE@ 72. Edit Distance
#
# --END--


def minDistance(self, word1, word2):
    if word1 == word2:
        return 0
    m, n = len(word1), len(word2)

    # dp initialization
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                # 1) dp[i][j] is for replacing
                # 2) dp[i+1][j] is for inserting
                # 3) dp[i][j+1] is for deleting
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
    return dp[m][n]


# LEETCODE@ 161. One Edit Distance
#
# --END--


def isOneEditDistance(self, s, t):
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            if len(s) == len(t):
                return s[i + 1:] == t[i + 1:]
            elif len(s) < len(t):
                return s[i:] == t[i + 1:]
            else:
                return s[i + 1:] == t[i:]
    return abs(len(s) - len(t)) == 1
