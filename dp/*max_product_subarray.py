# LEETCODE@ 152. Maximum Product Subarray
#
# --END--


def max_product_sub_array(nums):
    min_here = max_here = max_so_far = nums[0]

    for num in nums[1:]:
        min_here, max_here = min(min_here * num, max_here * num, num), max(min_here * num, max_here * num, num)
        max_so_far = max(max_so_far, max_here)

    return max_so_far

