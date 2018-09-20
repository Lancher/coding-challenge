# LEETCODE@ 689. Maximum Sum of 3 Non-Overlapping Subarrays
#
# --END--


def maxSumOfThreeSubarrays(self, nums, k):
    n = len(nums)

    # calculate sum ends at i
    sum_end = [0] * n
    sm = 0
    for i in range(n):
        sm += nums[i]
        if k <= i:
            sm -= nums[ i -k]
        if k - 1 <= i:
            sum_end[i] = sm

    # dp[i][j] represent the max sum till index j,
    dp = [[0 for j in range(n)] for i in range(3)]

    # select 1st array
    mx = float('-inf')
    for j in range(k - 1, n):
        mx = max(mx, sum_end[j])
        dp[0][j] = mx

    # select 2nd & 3rd array
    for i in range(1, 3):
        for j in range((i + 1) * k - 1, n):
            dp[i][j] = max(dp[i][ j -1], dp[ i -1][ j -k] + sum_end[j])

    # trace back to find the indexes
    res = []
    val = dp[2][n -1]
    i, j = 2, n - 1

    # keep moving to (0, 0)
    while len(res) != 3:
        while 0 <= j - 1 and dp[i][ j -1] == val:
            j -= 1
        res.append(j - k + 1)
        val -= sum_end[j]
        j -= k
        i -= 1
    return res[::-1]