# LEETCODE@ 808
#
# --END--


import math


def soupServings(self, N):
    if N >= 4800:
        return 1
    dp = {}

    def f(a, b):
        if (a, b) in dp:
            return dp[(a, b)]
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        dp[(a, b)] = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
        return dp[(a, b)]
    n = math.ceil(N / 25)
    return f(n, n)
