# LEETCODE@ 713. Subarray Product Less Than K
#
# --END--


def numSubarrayProductLessThanK(self, nums, k):
    res = 0
    i = 0
    mul = 1
    for j in range(len(nums)):
        mul *= nums[j]

        while i <= j and mul >= k:
            mul /= nums[i]
            i += 1
        res += j - i + 1

    return res
