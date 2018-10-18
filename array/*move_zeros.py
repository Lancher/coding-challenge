# LEETCODE@ 283. Move Zeroes
#
# 1. For the followUp, each array block will be assigned only once.
#
# --END


def move_zeros(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] !=0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


def move_zeros_with_less_operations(nums):
    n = len(nums)
    zeros = 0

    for i in range(n):
        if nums[i] == 0:
            zeros += 1
        else:
            if zeros:
                nums[i - zeros] = nums[i]

    # sometimes, the index is confusing, you need to only care how many iterations you have to do.
    for i in range(n - 1, n - zeros - 1, -1):
        nums[i] = 0
