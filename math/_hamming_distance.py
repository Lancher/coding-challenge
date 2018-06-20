# LEETCODE@ 461. Hamming Distance
#
# --END--


def hammingDistance(x, y):
    z = x ^ y
    res = 0
    while z:
        # 1) Set the rightmost bit to 0
        # https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
        z &= z - 1
        res += 1
    return res
