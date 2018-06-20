# LEETCODE@ 268. Missing Number
#
# 1. Use xor, a ^ b ^ a = b
#
# --END--


def missing_number(nums):
    val = 0
    for i in range(len(nums)):
        val ^= i
        val ^= nums[i]
    return val ^ len(nums)


# LEETCODE@ 41. First Missing Positive
#
# --END--


def first_missing_positive(self, nums):
    j = len(nums) - 1
    # Swap the numbers such as 0, -1, -2 to the right
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < 1:
            nums[i], nums[j] = nums[j], 0
            j -= 1
    for i in range(0, j + 1):
        k = abs(nums[i]) - 1
        if k < len(nums):
            nums[k] = -abs(nums[k])

    # We might go through the array and can not find any missing. In that case, the 'i+1'
    # is the missing one.
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            return i + 1
        i += 1
    return i + 1


# LEETCODE@ 448. Find All Numbers Disappeared in an Array
#
# --END--


def find_all_disappeared_numbers(nums):
    for i in xrange(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
