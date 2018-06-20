# LEETCODE@ 278. First Bad Version
#
# --END--


def firstBadVersion(self, n):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) / 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
