# LEETCODE@ 799. Champagne Tower
#
# 1) The idea is extremely clever. We can put more than one in our dp array.
#
# --END--


def champagneTower(self, poured, query_row, query_glass):
    m, n = query_row + 1, query_row + 1

    # 1) dp initialization
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dp[0][0] = poured

    # 2) overflow
    for i in range(n):
        for j in range(i + 1):
            if dp[i][j] > 1:
                over_flow = dp[i][j] - 1
                dp[i][j] = 1
                dp[i + 1][j] += over_flow / 2
                dp[i + 1][j + 1] += over_flow / 2
    return dp[query_row][query_glass]
