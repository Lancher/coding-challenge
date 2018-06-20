# LEETDCODE@ 474. Ones and Zeroes
#
# 1) Backpack problem
#
# 2) Because we encounter one more condition is that 0s & 1s, we have
#    to extend the 2-d dp to 3-d dp.
#
# --END--


def findMaxForm(self, strs, m, n):
    counter = []
    for s in strs:
        counter.append([0, 0])
        for c in s:
            if c == '0':
                counter[-1][0] += 1
            else:
                counter[-1][1] += 1
    l = len(strs)

    # 1) dp initialization
    dp = [[[0 for j in range(n + 1)] for i in range(m + 1)] for k in range(l + 1)]
    for k in range(1, l + 1):
        for i in range(m + 1):
            for j in range(n + 1):
                if i - counter[k - 1][0] >= 0 and j - counter[k - 1][1] >= 0:
                    dp[k][i][j] = max(dp[k][i][j], dp[k - 1][i - counter[k - 1][0]][j - counter[k - 1][1]] + 1)
                dp[k][i][j] = max(dp[k][i][j], dp[k - 1][i][j])
    return dp[l][m][n]
