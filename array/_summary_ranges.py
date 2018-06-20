# LEETCODE@ 228. Summary Ranges
#
# 1. When there is input, we must consider 1) empty, 2) length is one 3) any length
#
# --END--


def summary_ranges(nums):
    # empty nums
    if not nums:
        return []

    result = []
    s = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if s == i - 1:
                result.append(str(nums[s]))
            else:
                result.append(str(nums[s]) + "->" + str(nums[i - 1]))
            s = i

    #  be careful the last part range
    if s == len(nums) - 1:
        result.append(str(nums[s]))
    else:
        result.append(str(nums[s]) + "->" + str(nums[len(nums) - 1]))
    return result
