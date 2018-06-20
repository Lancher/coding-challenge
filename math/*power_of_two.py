# LEETCODE@ 231. Power of Two
#
# 1) Power of 2 means only one bit of n is '1', so use the trick n&(n-1)==0
#    to judge whether that is the case.
#
# --END--


def is_power_of_two(n):
    if n <= 0:
        return False
    return not (n & (n - 1))


# LEETCODE@ 326. Power of Three
#
# --END--


def isPowerOfThree(self, n):
    # 1162261467 is 3^19,  3^20 is bigger than int
    return n > 0 and 1162261467 % n == 0
