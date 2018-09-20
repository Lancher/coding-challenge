# LEETCODE@ 644. Maximum Average Subarray II
#
# 1. Similar with the problem in heap section.
#
# --END--


def findMaxAverage(self, nums, k):
    lo, hi = min(nums), max(nums)

    while lo < hi - 1e-6:
        mi = (lo + hi) / 2
        if self.check(nums, mi, k):
            lo = mi
        else:
            hi = mi
    return lo


def check(self, nums, mean, k):
    n = len(nums)

    # let arr be the nums[i] - mean
    arr = [num - mean for num in nums]
    print(arr)

    # cur be the of window size more than k
    sum_so_far = 0
    for i in range(k):
        sum_so_far += arr[i]

    # it means we have the answer greater or equal to mean.
    if sum_so_far >= 0:
        return True

    possible_minus = 0
    for i in range(k, len(arr)):
        sum_so_far += arr[i]
        possible_minus += arr[i - k]

        # we shrink the size of window
        if possible_minus < 0:
            sum_so_far -= possible_minus
            possible_minus = 0

        if sum_so_far >= 0:
            return True