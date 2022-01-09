"""
1. select minimum and swap with 0 and so on

2. time complexity is O(n^2), swapping is O(n)

--END --
"""


def selection_sort(nums):
    for i in range(len(nums)):
        min_i = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_i]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]
