# LEETCODE@ 54. Spiral Matrix
#
# --END--


def print_spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []

    i_s, i_e = 0, len(matrix)
    j_s, j_e = 0, len(matrix[0])

    res = []
    while i_s < i_e and j_s < j_e:
        for j in range(j_s, j_e):
            res.append(matrix[i_s][j])
        i_s += 1

        for i in range(i_s, i_e):
            res.append(matrix[i][j_e - 1])
        j_e -= 1

        # make sure i_s < i_e
        if i_s < i_e:
            for j in range(j_e - 1, j_s - 1, -1):
                res.append(matrix[i_e - 1][j])
            i_e -= 1

        # make sure j_s < j_e
        if j_s < j_e:
            for i in range(i_e - 1, i_s - 1, -1):
                res.append(matrix[i][j_s])
            j_s += 1
    return res


# LEETCODE@ 59. Spiral Matrix II
#
# --END--


def generateMatrix(self, n):
    res = [[0 for j in range(n)] for i in range(n)]

    i, j, di, dj = 0, 0, 0, 1
    for k in range(n * n):
        res[i][j] = k + 1
        if res[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i, j = i + di, j + dj
    return res
