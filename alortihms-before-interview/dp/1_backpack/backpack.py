"""
LINTCODE@ 92. Backpack

1) Backpack Problem 1 (Weight, Single Item)

2) There are 4 items each weight is [2, 3, 5, 7], and we have a bag weight capacity is 12.
   How full you can fill this backpack?

   Each item can only be picked up once!

      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
   0  0  0  0  0  0  0  0  0  0  0   0   0   0
   2  0  0  2  2  2  2  2  2  2  2   2   2   2
   3  0  0  2  3  3  5  5  5  5  5   5   5   5
   5  0  0  2  3  3  5  5  7  8  8  10  10  10
   7  0  0  2  3  3  5  5  7  8  9  10  10  12

2) use 2D array

3) https://zhengyang2015.gitbooks.io/lintcode/backpack_i_92.html

--END--
"""


def backPack(self, m, A):
    # write your code here
    m, n = len(A), m
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = dp[i][j + 1] # Don't Select
            if j + 1 - A[i] >= 0:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1 - A[i]] + A[i]) # Select

    return dp[m][n]

"""
LINTCODE@ 125. Backpack II

1) Backpack Problem 2 (Weight, Value, Single Item)

1) Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and
   a backpack with size 10. The maximum value is 9.
   What's the maximum value can you put into the backpack?

   Each item can only be picked up once!

      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
   0  0  0  0  0  0  0  0  0  0  0   0   0   0
   2  0  0  1  1  1  1  1  1  1  1   1   1   1
   3  0  0  1  5  5  5
   7  T

--END--
"""
def backPackII(self, m, A, V):
    m, n = len(A), m
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j + 1])
            if 0 <= j + 1 - A[i]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1 - A[i]] + V[i])

    return dp[m][n]

"""
LintCode 440: Backpack III

1) Backpack Problem 3 (Weight, Value, Infinite Items)

    Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and
    a backpack with size 10. The maximum value is 15.
    What's the maximum value can you put into the backpack?

    Each item can only be picked up multiple times!

          0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
       0  0  0  0  0  0  0  0  0  0  0   0   0   0
       2  0  0  1  1  2  1  3  1  4  1   5   1   6
       3  0  0  1  5  5  6
       7  T

2) Since we dont care about the number of `A` we use, we can ignore i directions.

--END--
"""

def backPackIII(self, m, A, V):
    """ Use 2D array or 1D array below!
    m, n = len(A), m
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = dp[i][j+1]
            if 0 <= j + 1 - A[i]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j+1-A[i]] + V[i])

    return dp[m][n]
    """
    m, n = len(A), m

    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            if 0 <= j + 1 - A[i]:
                dp[j+1] = max(dp[j+1], dp[j+1-A[i]] + V[i])
    return dp[n]


"""
LINTCODE@ 562. Backpack IV

1) Backpack Problem 4 (Weight, Infinite Items, How many times)

2) Given nums = [1, 2, 4], target = 4
   Output number fo ways to reach target 4.
   Each item may be chosen unlimited number of times.

      The possible combination ways are:
      [1, 1, 1, 1]
      [1, 1, 2]
      [2, 2]
      [4]

        0, 1, 2, 3, 4,
     0  1  0  0  0  0
     1  1  1  1  1  1
     2  1  1  2  2  3
     4  1  1  2  2  4

     From top to bottom, we add top or maybe left if amount < current number

--END--
"""


def backPackIV(nums, target):
    """ Corner case [0, 0, 0, 1], 1
    m, n = len(nums), target
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dp[0][0] = 1
    for i in range(m):
        dp[i+1][0] = dp[i][0]
        if 0 <= 0 - nums[i]:
                dp[i+1][0] += dp[i+1][0-nums[i]]

    for j in range(n):
        for i in range(m):
            dp[i+1][j+1] = dp[i][j+1]
            if 0 <= j + 1 - nums[i]:
                dp[i+1][j+1] += dp[i+1][j+1-nums[i]]

    return dp[m][n]
    """
    m, n = len(nums), target
    dp = [0] * (n + 1)

    # 0 item has 1 combination
    dp[0] = 1
    for i in range(m):
        for j in range(n):
            if 0 <= j + 1 - nums[i]:
                dp[j+1] += dp[j+1-nums[i]]
    return dp[n]


"""
LINTCODE@ 563. Backpack V

1) Backpack Problem 5 (Weight, Single Item, How many times)

2) Given nums = [1, 2, 4], target = 4

  Each item may only be used once.

  The possible combination ways are:
  [4]

        0, 1, 2, 3, 4,
     0  1  0  0  0  0
     1  1  1  0  0  0
     2  1  1  1  1  0
     4  1  1  1  1  0

--END--
"""
def backPackV(nums, target):
    nums.sort()
    m, n = len(nums), target
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dp[0][0] = 1

    # corner cases [0, 0, 0, 1], 1 => output 8
    for i in range(m):
        dp[i+1][0] = dp[i][0]
        if 0 <= 0 - nums[i]:
            dp[i+1][0] += dp[i][0]

    for i in range(m):
        for j in range(n):
            # we can not select A[i]
            dp[i+1][j+1] = dp[i][j+1]
            # we can select A[i]
            if 0 <= j + 1 - nums[i]:
                dp[i+1][j+1] += dp[i][j+1-nums[i]]

    return dp[m][n]


"""
LINTCODE@ 564. Backpack VI

1) Backpack Problem 6 (Weight, Infinite Items, How many times)

2) Given nums = [1, 2, 4], target = 4

  The possible combination ways are 6:
      [1, 1, 1, 1]
      [1, 1, 2]
      [1, 2, 1]
      [2, 1, 1]
      [2, 2]
      [4]

--END--
"""

def backPackVI(nums, target):
    m, n = len(nums), target
    dp = [0] * (n + 1)

    # different direction from Backpack Problem 4
    dp[0] = 1
    for i in range(n):
        for j in range(m):
            if 0 <= i + 1 - nums[j]:
                dp[i + 1] += dp[i + 1 - nums[j]]
    return dp[n]
