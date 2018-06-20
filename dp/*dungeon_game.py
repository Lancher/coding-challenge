# LEETCODE@ 174. Dungeon Game
#
# --END--


def calculateMinimumHP(self, dungeon):
    m, n = len(dungeon), len(dungeon[0])
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)

    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
    for j in range(n - 2, -1, -1):
        dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            # 1) dp[ ] + dun[ ] = dp[ ]right
            #    dp[ ] = dp[ ]right - dun[ ]
            #
            # make sure, dp[ ] > 0
            #
            # --END--
            right = max(dp[i][j + 1] - dungeon[i][j], 1)
            down = max(dp[i + 1][j] - dungeon[i][j], 1)
            dp[i][j] = min(right, down)
    return dp[0][0]
