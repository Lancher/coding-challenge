# LEETCODE@ 74. Search a 2D Matrix
#
# --END--


def search_1(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])

    # 1) our ranges
    lo, hi = 0, m * n - 1
    while lo < hi:
        mi = int((lo + hi) / 2)
        i, j = int(mi / n), int(mi % n)
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            lo = mi + 1
        else:
            hi = mi
    return True if matrix[int(lo / n)][int(lo % n)] == target else False


# LEETCODE@ 240. Search a 2D Matrix II
#
# 1) Examples
#
#   [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
#   ]
#
# --END--


def search_2(matrix, target):
    i, j = len(matrix) - 1, 0

    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1
    return False
