# LEETCODE@ 118. Pascal's Triangle
#
# --END--


def generate(self, numRows):
    n = numRows

    res = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[-1][j - 1] + res[-1][j]
        res.append(row)
    return res


# LEETCODE@ 119. Pascal's Triangle II
#
# Given an index k, return the kth row of the Pascal's triangle.
def getRow(self, rowIndex):
    n = rowIndex + 1
    res = [1] * n
    for i in range(n):
        for j in range(i - 1, 0, -1):
            res[j] = res[j - 1] + res[j]
    return res
