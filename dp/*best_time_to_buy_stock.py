# LEETCODE@ 121. Best Time to Buy and Sell Stock
#
# --END--


def maxProfit(self, prices):
    if not prices:
        return 0

    re = 0
    mn = prices[0]

    for i in range(1, len(prices)):
        # 1) update minimum
        if prices[i] < mn:
            mn = prices[i]
        # 2) encounter increase means we are rising
        elif mn < prices[i]:
            re = max(re, prices[i] - mn)
    return re


# LEETCODE@ 122. Best Time to Buy and Sell Stock II
#
# --END--


def maxProfit(self, prices):
    re = 0
    for i in range(1, len(prices)):
        re += max(prices[i] - prices[i - 1], 0)
    return re


# LEETCODE@ 123. Best Time to Buy and Sell Stock III
#
# https://www.youtube.com/watch?v=oDhu5uGq_ic
#
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
def maxProfit(self, prices):
    if not prices:
        return 0

    m, n = 2, len(prices)
    dp = [[0 for j in range(n + 1)] for j in range(m + 1)]

    for i in range(m):
        max_diff = dp[i][1] - prices[0]
        for j in range(1, n):
            dp[i + 1][j + 1] = max(dp[i + 1][j], max_diff + prices[j])
            max_diff = max(max_diff, dp[i][j + 1] - prices[j])

    return dp[m][n]


# LEETCODE@ 188. Best Time to Buy and Sell Stock IV
#
# --END--


def maxProfit(self, k, prices):
    if not prices:
        return 0
    if k >= len(prices) / 2:
        return self.max_profit(k, prices)

    dp = [[0 for j in range(len(prices))] for i in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = dp[i - 1][0] - prices[0]
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j - 1], max_diff + prices[j])
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    return dp[k][len(prices) - 1]


def max_profit(self, k, prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

