# LEETCODE@ Minimum Window Subsequence
#
# --END--


def minWindow(self, S, T):
    m, n = len(T), len(S)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for j in range(0, n + 1):
        dp[0][j] = j + 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if T[i - 1] == S[j - 1]:
                dp[i][j] = dp[i - 1][j - 1];
            else:
                dp[i][j] = dp[i][j - 1];
    _MAX = float('inf')
    start, ln = 0, _MAX
    for j in range(1, n + 1):
        if dp[m][j] != 0:
            if j - dp[m][j] + 1 < ln:
                start = dp[m][j] - 1
                ln = j - dp[m][j] + 1

    return '' if ln == _MAX else S[start:start + ln]
