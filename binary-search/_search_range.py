

# LEETCODE@ 34. Search for a Range
#
# --END--


def searchRange(self, nums, target):
    res = [-1, -1]

    # 1) [lo, hi] is the range of target starting index.
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] == target:
            hi = mi
        elif nums[mi] < target:
            lo = mi + 1
        else:
            hi = mi
    if lo < len(nums) and nums[lo] == target:
        res[0] = lo
    else:
        return res

    # We have to make sure loop will not happen
    # 2) [lo, hi] is the range of target ending index + 1.
    lo, hi = res[0] + 1, len(nums)
    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] == target:
            lo = mi + 1
        elif nums[mi] > target:
            hi = mi

    res[1] = lo - 1
    return res
