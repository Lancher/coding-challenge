# LEETCODE@ 51. N-Queens
#
# 1. / : i + j
#    \ : n + i - j - 1
#
# 2. Remember the node and use the nodes to build map.
#
# --END--


def solveNQueens(self, n):
    used1, used2, used3 = [0] * n, [0] * (2*n-1), [0] * (2*n-1)
    qs, qs_list = [], []
    self.backtracing(n, 0, qs, qs_list, used1, used2, used3)

    res = []
    print(qs_list)
    for qs in qs_list:
        matrix = [['.' for j in range(n)] for i in range(n)]
        for q in qs:
            matrix[q[0]][q[1]] = 'Q'
        for i in range(n):
            matrix[i] = ''.join(matrix[i])
        res.append(matrix)
    return res


def backtracing(self, n, i, qs, qs_list, used1, used2, used3):
    if len(qs) == n:
        qs_list.append(qs[:])
    else:
        for j in range(n):
            if not used1[j] and not used2[i+j] and not used3[n-1+j-i]:
                used1[j] = used2[i+j] = used3[n-1+j-i] = 1
                qs.append((i, j))
                self.backtracing(n, i + 1, qs, qs_list, used1, used2, used3)
                used1[j] = used2[i+j] = used3[n-1+j-i] = 0
                qs.pop()


# LEETCODE@ 52. N-Queens II
#
# --END--


def totalNQueens(self, n):
    result = [0]
    flags_0, flags_45, flags_135 = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)
    self.backtracing(n, 0, flags_0, flags_45, flags_135, result)
    return result[0]


def backtracing(self, n, row, flags_0, flags_45, flags_135, result):
    if row == n:
        result[0] += 1
    else:
        for col in range(n):
            if flags_0[col] or flags_45[row + col] or flags_135[n - 1 + col - row]:
                continue
            flags_0[col] = flags_45[row + col] = flags_135[n - 1 + col - row] = 1
            self.backtracing(n, row + 1, flags_0, flags_45, flags_135, result)
            flags_0[col] = flags_45[row + col] = flags_135[n - 1 + col - row] = 0
