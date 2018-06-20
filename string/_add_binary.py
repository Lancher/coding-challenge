# LEETCODE@ 67. Add Binary
#
# --END--


def add_binary(a, b):
    res = ''

    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i > -1 or j > -1 or carry:
        carry += int(a[i]) if i > -1 else 0
        carry += int(b[j]) if j > -1 else 0
        res = str(carry % 2) + res
        carry /= 2
        i, j = i - 1, j - 1
    return res
