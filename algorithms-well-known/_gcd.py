# Compute gcd
#
# 1. How to compute GCD?
#
# --END--


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
