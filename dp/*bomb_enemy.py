# 361. Bomb Enemy
#
# --END--


def maxKilledEnemies(self, grid):
    if not grid or not grid[0]:
        return 0

    res = 0
    m, n = len(grid), len(grid[0])
    row, cols = 0, [0] * n
    for i in range(m):
        for j in range(n):
            # count row
            if j == 0 or grid[i][j - 1] == 'W':
                row = 0
                for k in range(n - j):
                    if grid[i][j + k] == 'W':
                        break
                    if grid[i][j + k] == 'E':
                        row += 1
            # count cols
            if i == 0 or grid[i - 1][j] == 'W':
                cols[j] = 0
                for k in range(m - i):
                    if grid[i + k][j] == 'W':
                        break
                    if grid[i + k][j] == 'E':
                        cols[j] += 1
            # put bomb
            if grid[i][j] == '0':
                res = max(res, row + cols[j])
    return res
