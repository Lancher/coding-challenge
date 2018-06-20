# LEETCODE@ 136. Single Number
#
# 1) a ^ b ^ a = b
#
# --END


def single_number(nums):
    single = nums[0]
    for num in nums[1:]:
        single ^= num
    return single


# LEETCODE@ 137. Single Number II


# LEETCODE@ 260 Single Number III

