# LEETCODE@ 35. Search Insert Position
#
# --END--


def searchInsert(self, nums, target):
    lo, hi = 0, len(nums)

    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] == target:
            return mi
        elif nums[mi] < target:
            lo = mi + 1
        else:
            hi = mi
    return lo
