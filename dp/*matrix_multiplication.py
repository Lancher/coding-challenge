# matrix multiplication
#
# 1) Example
#
#  [2, 3] x [3, 6] x [6, 4] x [4, 5]
#
# 2) Time complexity O(n^3)
#
# 3) https://www.youtube.com/watch?v=vgLJZMUfnsU
#
# --END--


def matrix_mul(matrices):
    if len(matrices) < 2:
        return 0

    # 1) dp[i,j] minimum multiplication between i,j
    n = len(matrices)
    dp = [[float('inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for l in range(2, n + 1):
        lo, hi = 0, l - 1
        while hi < n:
            # 2) make slices after i
            for i in range(lo, hi):
                mul = dp[lo][i] + matrices[lo][0] * matrices[i+1][0] * matrices[hi][1] + dp[i+1][hi]
                if mul < dp[lo][hi]:
                    dp[lo][hi] = mul
            lo, hi = lo + 1, hi + 1
    return dp[0][n-1]


print(matrix_mul([(2, 3), (3, 6), (6, 4), (4, 5)]))
