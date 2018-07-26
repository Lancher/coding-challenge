# LEETCODE@ 201. Bitwise AND of Numbers Range
#
# 1) Example:
#
#   4: 0100
#   5: 0101
#   6: 0110
#   7: 0111
#
# --END--


def rangeBitwiseAnd(self, m, n):
    if m == 0:
        return 0
    move = 0
    while m != n:
        m >>= 1
        n >>= 1
        move += 1
    return m << move
