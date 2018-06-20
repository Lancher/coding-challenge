# LEETCODE@ 132. Palindrome Partitioning II
#
# 1) The idea is the same as `516. Longest Palindromic Subsequence`.
#
# --END--


def minCut(self, s):
    n = len(s)
    # 1) dp[] for remembering [i:j] if palindrome
    dp = [[0 for j in range(n)] for i in range(n)]
    # 2) cut[] for remembering number of cuts from index i to n -1
    cut = [n - 1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # 3) Example: j from i and go to right
            #        i,j-> j ->j
            #        [ ] [ ] [ ]
            #            [ ] [ ]
            #                [ ]
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = 1
                if j == n - 1:
                    cut[i] = 0
                else:
                    if cut[j + 1] + 1 < cut[i]:
                        cut[i] = cut[j + 1] + 1

    return cut[0]


