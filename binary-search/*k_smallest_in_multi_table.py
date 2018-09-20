# LEETCODE@ 668. Kth Smallest Number in Multiplication Table
#
# 1. Similar to LEETCODE@ 786. K-th Smallest Prime Fraction.
#
# --END--


def findKthNumber(self, m, n, k):
    lo, hi = 1, m * n
    while lo < hi:
        mi = int((lo + hi) / 2)
        if self.count(mi, m, n) < k:
            lo = mi + 1
        else:
            hi = mi

    return lo


def count(self, val, m, n):
    res = 0
    for i in range(1, m + 1):
        res += min(int(val / i), n)
    return res
