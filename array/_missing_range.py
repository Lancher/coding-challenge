# LEETCODE@ 163. Missing Ranges
#
# --END--


def findMissingRanges(self, nums, lower, upper):
    nums = [lower - 1] + nums
    nums.append(upper + 1)

    result = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 2:
            result.append(str(nums[i] - 1))
        elif nums[i] - nums[i - 1] > 2:
            result.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
    return result
