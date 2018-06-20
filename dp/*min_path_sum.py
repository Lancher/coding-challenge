# 64. Minimum Path Sum
#
# --END--


def minPathSum(self, grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    # dp initialization
    dp = [[grid[i][j] for j in range(n)] for i in range(m)]
    for i in range(1, m):
        dp[i][0] += dp[i - 1][0]
    for j in range(1, n):
        dp[0][j] += dp[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
    return dp[m - 1][n - 1]
