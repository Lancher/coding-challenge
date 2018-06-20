# LEETCODE@ 89. Gray Code
#
# --END--


def grayCode(n):
    res = [0]

    for i in range(n):
        incr = 1 << i
        res += [v + incr for v in res[::-1]]

    return res

