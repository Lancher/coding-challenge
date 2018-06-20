# LEETCODE@ 53. Maximum Subarray
#
# --END--


def max_sub_array(nums):
    if not nums:
        return 0

    max_here = nums[0]
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_here = max(max_here + nums[i], nums[i])
        max_so_far = max(max_so_far, max_here)
    return max_so_far
