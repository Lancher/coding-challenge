# LINTCODE@ 92. Backpack
#
# 1) Example [2, 3, 5, 7] weight is 12
#
#       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
#    0  T  F  F  F  F  F  F  F  F  F  F   F   F
#    2  T
#    3  T
#    7  T
#
# 2) use two array
#
# 3) http://novoland.github.io/%E7%AE%97%E6%B3%95/2014/07/26/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98.html
# 
# --END--


def backPack(self, m, A):
    m, n = len(A), m
    # 1) use two array to do the rotation
    dp = [[0] * (n + 1), [0] * (n + 1)]

    # 2) dp logic
    dp[0][0] = dp[1][0] = 1
    for i in range(m):
        row = (i + 1) % 2
        pre_row = i % 2
        for j in range(n):
            if dp[pre_row][j + 1] or 0 <= j + 1 - A[i] and dp[pre_row][j + 1 - A[i]]:
                dp[row][j + 1] = 1
            else:
                dp[row][j + 1] = 0

    # 3) find the largest one
    row = m % 2
    for j in range(n, -1, -1):
        if dp[row][j]:
            return j


# LINTCODE@ 125. Backpack II
#
# 1) Example weight [2, 3, 5, 7], value [1, 5, 2, 4] weight is 12
#
#       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
#    0  0  0  0  0  0  0  0  0  0  0   0   0   0
#    2  0  0  1  1  1  1  1  1  1  1   1   1   1
#    3  0  0  1  5  5  5
#    7  T
#
# --END--
def backPackII(self, m, A, V):
    m, n = len(A), m
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j + 1])
            if 0 <= j + 1 - A[i]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1 - A[i]] + V[i])

    return dp[m][n]


# LintCode 440: Backpack III
#
# 1) Backpack II with n repeat items.
#
# 2) Since we dont care about the number of `A` we use, we can ignore i directions.
#
# --END--


def backPackIII(self, m, A, V):
    m, n = len(A), m

    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            if 0 <= j + 1 - A[i]:
                dp[j+1] = max(dp[j+1], dp[j+1-A[i]] + V[i])
    return dp[n]


# LINTCODE@ 563. Backpack V
#
# 1) Question:
#
# Given n items with size nums[i] which an integer array and all positive numbers. An integer target
# denotes the size of a backpack. Find the number of possible fill the backpack.
#
# --END--


def backPackV(self, A, target):
    m, n = len(A), target
    dp = [[0] for j in range(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(m):
        for j in range(n):
            # we can not select A[i]
            dp[i+1][j+1] = dp[i][j+1]
            # we can select A[i]
            if 0 <= j + 1 - A[i]:
                dp[i+1][j+1] += dp[i][j+1-A[i]]

    return dp[m][n]


# LINTCODE@ 564. Backpack VI
#
# Backpack V with repeat items.
#
# Given an integer array nums with all positive numbers and no duplicates, find the number of possible
# combinations that add up to a positive integer target.
#
# --END--


def backPackVI(self, nums, target):
    m, n = len(nums), target
    dp = [0] * (n + 1)

    # 1) 0 have one match
    for i in range(m):
        for j in range(n):
            if 0 <= j + 1 - nums[i]:
                dp[j+1] += dp[j+1-nums[i]]
    return dp[n]
