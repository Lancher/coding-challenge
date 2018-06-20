# NOT LEETCODE@
#
# 1) Explanation: https://www.youtube.com/watch?v=NnD96abizww
#
# 2) Solution is DP.
#
# --END--


# time complexity O(n^2)
def longest_common_subseq(s1, s2):
    m, n = len(s1), len(s2)

    # dp[] the number of common subsequence so far & empty string "" is all zero
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    return dp[m][n]


#
print(longest_common_subseq('abcdaf', 'acbcf'))  # GTAB
