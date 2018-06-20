# LEETCODE@ 27. Remove Element
#
# --END--


def remove_element(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return j


# LEETCODE@ 26. Remove Duplicates from Sorted Array
#
# --END--


def removeDuplicates(self, nums):
    if not nums:
        return 0

    i = 1
    for j in range(1, len(nums)):
        if nums[j - 1] != nums[j]:
            nums[i] = nums[j]
            i += 1
    return i


# LEETCODE@ 80. Remove Duplicates from Sorted Array II
#
# --END--


def removeDuplicates(self, nums):
    j = 0
    pre_num = None
    cnt = 0
    for i in range(len(nums)):
        if nums[i] == pre_num:
            if cnt < 2:
                nums[j] = nums[i]
                j += 1
                cnt += 1
        else:
            pre_num = nums[i]
            nums[j] = nums[i]
            j += 1
            cnt = 1
    return j