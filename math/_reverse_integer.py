# LEETCODE@ 7. Reverse Integer
#
# --END--


def reverse(x):
    sign = 1 if x >= 0 else -1
    x = abs(x)
    res = 0
    while x:
        res = res * 10 + x % 10
        x /= 10
    if res > 0x7FFFFFFF:
        return 0
    return res * sign
