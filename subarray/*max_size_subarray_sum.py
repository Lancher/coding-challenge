# LEETCODE@ 325. Maximum Size Subarray Sum Equals k
#
# --END--


def max_size_subarray_sum(k, nums):
    res, acc = 0, 0
    d = {0: -1}
    for i in range(len(nums)):
        acc += nums[i]
        if acc not in d:
            d[acc] = i
        if acc - k in d:
            res = max(res, i - d[acc - k])
    return res
