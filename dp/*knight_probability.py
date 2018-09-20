# LEETCODE@ 688. Knight Probability in Chessboard
#
# --END--


def knightProbability(self, N, K, r, c):
    dp = [[[0 for j in range(N)] for i in range(N)] for k in range(K + 1)]

    dirs = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

    dp[0][r][c] = 1
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                # count the probability where it from
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < N and 0 <= y < N:
                        dp[k][i][j] += dp[k - 1][x][y] * 0.125

    # the probability of staying on the board
    res = 0
    for i in range(N):
        for j in range(N):
            res += dp[K][i][j]
    return res
