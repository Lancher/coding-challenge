# 1. Select from 1 to end, try to swap wit the previous one
#
# 2. time complexity is O(n^2)
#
#
# --END--


def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
