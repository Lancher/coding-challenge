# LEETCODE@ 561. Array Partition I
#
# [4, 2, 3, 1]
#
# (1, 2) (3, 4)
#  1  +   3
# --END--


def array_pair_sum(nums):
    return sum(sorted(nums)[::2])
