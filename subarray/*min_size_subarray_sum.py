# LEETCODE@ 209. Minimum Size Subarray Sum
#
# --END--


_MAX = float('inf')


def minSubArrayLen(self, s, nums):
    res = _MAX
    tmp_s, j = 0, 0

    for i in range(len(nums)):
        tmp_s += nums[i]
        while tmp_s >= s:
            res = min(res, i - j + 1)
            tmp_s -= nums[j]
            j += 1
    return 0 if res == _MAX else res
