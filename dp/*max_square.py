# LEETCODE@ 221. Maximal Square
#
# --END--


def maximalSquare(self, matrix):
    if not matrix:
        return 0

    result = 0
    # 1) maximum size square sub-matrix with all 1s
    dp = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                # 2) if [x] [x] all x are one, we can expand the square
                #       [x] [ ]
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                result = max(result, dp[i + 1][j + 1])
    return result * result
