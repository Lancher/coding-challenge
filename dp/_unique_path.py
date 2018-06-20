# LEETCODE@ 62. Unique Paths
#
# --END--


def uniquePaths(self, m, n):
    if m < n:
        m, n = n, m
    row = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[n - 1]


# LEETCODE@ 63. Unique Paths II
#
# --END--


def uniquePathsWithObstacles(self, obstacleGrid):
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[i])):
            obstacleGrid[i][j] ^= 1

    for i in range(1, len(obstacleGrid)):
        if obstacleGrid[i][0]:
            obstacleGrid[i][0] = obstacleGrid[i - 1][0]
    for j in range(1, len(obstacleGrid[0])):
        if obstacleGrid[0][j]:
            obstacleGrid[0][j] = obstacleGrid[0][j - 1]

    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[i][j]:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
    return obstacleGrid[-1][-1]
