# LEETCODE@ 766. Toeplitz Matrix
#
# 1. Example:
#
#   1 2 3 4 5 6
#    \ \ \ \ \
#   1 2 3 4 5 6
#
# --END--


def isToeplitzMatrix(self, matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m - 1):
        for j in range(n - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True
