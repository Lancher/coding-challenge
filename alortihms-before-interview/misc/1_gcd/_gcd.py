# Compute gcd
#
# 1. How to compute GCD?
#
# --END--
#
#   a    b
#   2    4
#   4    2
#   2    0

#   a    b
#   5    7
#   7    5
#   5    2
#   2,   1
#   1,   0


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
