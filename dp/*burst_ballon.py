# LEETCODE@ 312. Burst Balloons
#
# https://www.youtube.com/watch?v=IFNibRVgFBo
#
#
#
# --END--


def maxCoins(self, nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [[0 for j in range(n)] for i in range(n)]

    for l in range(1, n + 1):
        # 1) i, j are inclusive
        i, j = 0, l - 1

        # 2) j < n
        while j < n:
            for k in range(i, j + 1):
                # the `k` is the last index to burst.
                # the `i,j` is the inclusive length.
                #
                # [3, 1, 5, 8] & length == 2
                #
                #   [1, 5] & k is at element 1
                #    i  j
                #
                #   if 1 is the last index to burst, left == 0 & right == dp[1][1]
                #   left_num == 3 & right_num == 8.
                #
                # --END--
                left = 0 if k - 1 < i else dp[i][k - 1]
                right = 0 if j < k + 1 else dp[k + 1][j]

                num = nums[k]
                left_num = 1 if i - 1 < 0 else nums[i - 1]
                right_num = 1 if n - 1 < j + 1 else nums[j + 1]
                dp[i][j] = max(dp[i][j], left + left_num * num * right_num + right)
            i, j = i + 1, j + 1
    return dp[0][n - 1]

