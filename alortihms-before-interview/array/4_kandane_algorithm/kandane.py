"""
1. Kandane's Algorithm

2. Find maximum sub array.

   Use `max_here` and `max_so_far` to find
   the correct value.

-- END --
"""

def max_sub_array(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    max_here = nums[0]
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_here = max(max_here + nums[i], nums[i])
        max_so_far = max(max_so_far, max_here)
    return max_so_far


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))
