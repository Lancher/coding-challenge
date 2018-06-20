# LEETCODE@ 172. Factorial Trailing Zeroes
#
# --END--


def trailingZeroes(self, n):
    # 1) 125 --> 25 --> 5 --> 1
    #        25  +   5  +  1 = 31
    res = 0
    while n:
        res += int(n / 5)
        n = int(n / 5)
    return res
