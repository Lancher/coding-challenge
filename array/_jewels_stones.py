# LEETCODE@ 771. Jewels and Stones
#
# 1. Check whether the set contain my stones
#
# --END--


def numJewelsInStones(self, J, S):
    s = set(J)

    res = 0
    for c in S:
        if c in s:
            res += 1
    return res
