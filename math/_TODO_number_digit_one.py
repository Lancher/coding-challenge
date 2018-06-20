# LEETCODE@ 233. Number of Digit One
#
# --END--


def count_digit_one(n):
    ones, m = 0, 1
    while m <= n:
        ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones
