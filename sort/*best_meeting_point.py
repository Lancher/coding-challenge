# LEETCODE@ 296. Best Meeting Point
#
# 1) https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations
#
# --END--


def minTotalDistance(self, grid):
    if not grid or not grid[0]:
        return 0

    i_s, j_s = [], []
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                i_s.append(i)
                j_s.append(j)

    # 1) the median will be the shortests distance
    i_s.sort()
    j_s.sort()
    med_i = i_s[int(len(i_s) / 2)]
    med_j = j_s[int(len(j_s) / 2)]

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                res += abs(i - med_i) + abs(j - med_j)
    return res