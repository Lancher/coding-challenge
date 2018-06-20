# LEETCODE@ 162. Find Peak Element
#
# --END--


def findPeakElement(self, nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] < nums[mi + 1]:
            lo = mi + 1
        else:
            hi = mi
    return lo
