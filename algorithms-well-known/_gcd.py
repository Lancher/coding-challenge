# Compute gcd
#
# 1. How to compute GCD?
#
# --END--


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
