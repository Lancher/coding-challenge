# 75. Sort Colors
#
# 1) Quick Sort
#
# --END--


def sortColors(nums):
    i, j, k = 0, 0, len(nums) - 1

    while i <= k:
        if nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[k] = nums[k], nums[i]
            k -= 1
