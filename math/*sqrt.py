# LEETCODE@ 69. Sqrt(x)
#
# --END--


def my_sqrt(self, x):
    lo, hi = 0, x

    while lo <= hi:
        mi = int((lo + hi) / 2)
        if mi * mi == x:
            return mi
        elif mi * mi < x:
            if (mi + 1) * (mi + 1) > x:
                return mi
            lo = mi + 1
        else:
            hi = mi
