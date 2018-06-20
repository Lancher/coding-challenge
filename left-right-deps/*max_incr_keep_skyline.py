# LEETCODE@ 807. Max Increase to Keep City Skyline
#
# --END--


def maxIncreaseKeepingSkyline(self, grid):
    if not grid or not grid[0]:
        return 0

    # 1) find the maximum to avoid affect skyline
    m, n = len(grid), len(grid[0])
    row, col = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            row[i] = max(row[i], grid[i][j])
            col[j] = max(col[j], grid[i][j])

    res = 0
    for i in range(m):
        for j in range(n):
            m = min(row[i], col[j])
            res += m - grid[i][j] if grid[i][j] < m else 0
    return res
