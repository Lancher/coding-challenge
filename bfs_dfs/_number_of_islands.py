# LEETCODE@ 200. Number of Islands
#
# --END--


def numIslands(self, grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                res += 1
    return res


def dfs(self, grid, i, j):
    grid[i][j] = '0'
    x, y = 1, 0

    for _ in range(4):
        x, y = y, -x
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] == '1':
            self.dfs(grid, i + x, j + y)
