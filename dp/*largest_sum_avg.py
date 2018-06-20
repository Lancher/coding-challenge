# LEETCODE@ 813. Largest Sum of Averages
#
# 1) Example
#
#        9      1       2      3       9    => accumulation  9, 10, 12, 15, 24
#
#    0  9/1    10/2   12/3    15/4    24/5
#
#    1   x  dp[1][1] dp[1][2]
#
#    2
#
#
#   dp[1][1] = 9/1 + (10-9)/(1-0)
#   dp[1][2] = 10/2 + (12-10)/(2-1) or 9/1 + (12-9)/(2-0)
#   ...
#   ...
#
# 2) Time complexity is O(K*n*n)
#
# --END--


_MIN = float('-inf')


def largestSumOfAverages(self, A, K):
    m, n = K, len(A)
    # 1) dp array
    sm = A[:]
    dp = [[_MIN for j in range(n)] for i in range(m)]
    # 2) build slices with 0
    for j in range(n):
        if j > 0:
            sm[j] += sm[j - 1]
        dp[0][j] = sm[j] / (j + 1)

    for i in range(1, m):
        for j in range(i, n):
            # 3) A[jj:j+1] is current new group
            jj = j
            while jj >= i:
                dp[i][j] = max(dp[i][j], dp[i - 1][jj - 1] + (sm[j] - sm[jj - 1]) / (j - jj + 1))
                jj -= 1
    return dp[m - 1][n - 1]
