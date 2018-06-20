# 516. Longest Palindromic Subsequence
#
# 1) TLE happen for Python, but it is fine.
#
# --END--


def longestPalindromeSubseq(self, s):
    n = len(s)

    # 1) dp init, dp[] is the longest pal so far
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            # 2) if i == j, we know we only have to find substring [i+1:j-1]
            if s[i] == s[j]:
                if i + 1 == j:
                    dp[i][j] = 2
                else:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
