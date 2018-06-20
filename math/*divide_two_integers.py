# LEETCODE@ 29. Divide Two Integers
#
# 1. Example:
#   dividend = 10, divisor = 3
#   10 / 3 = 3
#
# 2. Signed Integer so our range goes from -0x80000000 ~ 0x7FFFFFFF
#
# --END--


def divide(dividend, divisor):
    if divisor == 0 or dividend == -0x80000000 and divisor == -1:
        return 0x7FFFFFFF

    sign = 1
    if (dividend < 0) ^ (divisor < 0):
        sign = -1
    dividend, divisor = abs(dividend), abs(divisor)

    res = 0
    while dividend >= divisor:
        shift = 0
        while dividend >= divisor << shift:
            shift += 1
        shift -= 1
        dividend -= divisor << shift
        res += 1 << shift
    return res * sign
