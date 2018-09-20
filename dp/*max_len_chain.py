# LEETCODE@ 646. Maximum Length of Pair Chain
#
# --END--


def findLongestChain(self, pairs):
    n = len(pairs)
    dp = [1] * n
    pairs.sort(key=lambda k: k[0])

    for i in range(n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[n - 1]


def findLongestChain(self, pairs):
    # TODO: greedy really smart!!!
    cur, res = float('-inf'), 0
    for p in sorted(pairs, key=lambda x: x[1]):
        if cur < p[0]:
            cur, res = p[1], res + 1
    return res
