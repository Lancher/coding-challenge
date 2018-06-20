# LEETCODE@ 279. Perfect Squares
#
# 1) DP Solution
#
# 2) BFS Solution
#
# --END--


def numSquares(self, n):
    # 1) dp init
    dp = [float("inf")] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(n + 1):
        # 2) if j start 0, dp[i-j*j] = d[i-0] which is not counting yet.
        for j in range(1, i):
            diff = i - j * j
            if diff < 0:
                break
            elif diff == 0:
                dp[i] = 1
            else:
                dp[i] = min(dp[i], dp[diff] + 1)
    return dp[n]


def num_squares(n):
    depth = 1
    s = set()
    s.add(n)

    while s:
        tmp_s = set()
        for num in s:
            i = 1
            while i * i <= num:
                if num - i * i == 0:
                    return depth
                else:
                    tmp_s.add(num - i * i)
                i += 1
        s = tmp_s
        depth += 1
