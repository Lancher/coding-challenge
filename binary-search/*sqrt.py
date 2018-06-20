# LEETCODE@ 69. Sqrt(x)
#
# --END--


def sqrt(x):
    lo, hi = 0, x
    while True:
        mi = (lo + hi) / 2
        if mi * mi <= x:
            if (mi + 1) * (mi + 1) > x:
                return mi
            lo = mi + 1
        else:
            hi = mi - 1
