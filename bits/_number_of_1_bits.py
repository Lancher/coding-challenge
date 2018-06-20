# LEETCODE@ 191. Number of 1 Bits
#
# 1) flip the right most bit.
#
#   n = n & (n - 1)
#
# --END--


def hammingWeight(self, n):
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res
