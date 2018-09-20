# https://blog.csdn.net/dominating413421391/article/details/43447399
# http://iamayushanand.github.io/cp/dp/2016/05/20/Dynamic-Programming-13C-codeforces.html
import time
import random


def min_operations(nums):
    return min(min_operations_to_increase(nums), min_operations_to_increase(nums[::-1]))


def min_operations_to_increase(nums):
    n = len(nums)
    dp = [0] * n

    s_nums = sorted(nums)

    for i in range(n):
        for j in range(n):
            dp[j] += abs(nums[i] - s_nums[j])
            if j:
                dp[j] = min(dp[j], dp[j-1])
    return dp[n-1]


s = time.time()
nums = [0] * 1000
nums[10] = 1
print(min_operations(nums))
e = time.time()
print(e - s)

s = time.time()
nums = [1] * 501 + [0] * 499
print(min_operations(nums))
e = time.time()
print(e - s)
