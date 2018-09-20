# LEETCODE@ 647. Palindromic Substrings
#
# --END--


def countSubstrings(self, s):
    if not s:
        return 0
    n = len(s)

    # dp
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1

    # At least, we already n palindromic strings
    res = n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n, 1):
            if j - i == 1:
                if s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1
            else:
                if dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1
    return res