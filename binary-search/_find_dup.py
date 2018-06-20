# LEETCODE@ 287. Find the Duplicate Number
#
# 1) 1. TODO: Very Good Explanation https://goo.gl/wyHLNw
#
# 2) trial and error
#
# --END--


def find_dup(nums):
    # possible range
    lo, hi = 1, len(nums) - 1

    # binary search
    while lo < hi:
        mi = int((lo + hi) / 2)
        cnt = 0
        for num in nums:
            if num <= mi:
                cnt += 1

        if cnt <= mi:
            lo = mi + 1
        else:
            hi = mi

    return lo
