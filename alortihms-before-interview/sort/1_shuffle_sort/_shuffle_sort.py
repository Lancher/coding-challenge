"""
1. import random.randint

--END--
"""


import random


def shuffle_sort(nums):
    for i in range(len(nums)):
        # random a value and then swap
        j = random.randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]
