# LEETCODE@ 322. Coin Change
#
# 1) DFS
#
# 2) DP (Backpack Problem)
#
# --END--


_MAX = float('inf')


# DFS
def coinChange(self, coins, amount):
    res = self.dfs(coins, amount)
    return -1 if res == _MAX else res


def dfs(self, coins, amount):
    if amount == 0:
        return 0
    res = _MAX
    for i in range(len(coins)):
        if amount - coins[i] >= 0:
            res = min(res, self.dfs(coins, amount - coins[i]) + 1)
    return res


# DP
def coinChange(self, coins, amount):
    m, n = len(coins), amount
    dp = [0] + [_MAX] * amount

    for i in range(m):
        for j in range(n):
            # be careful with index out of range
            if 0 <= j + 1 - coins[i]:
                dp[j + 1] = min(dp[j + 1], dp[j + 1 - coins[i]] + 1)

    return -1 if dp[n] == _MAX else dp[n]

