# LEETCODE@ 374. Guess Number Higher or Lower
#
# --END--


def guessNumber(self, n):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) / 2
        if guess(mid) == 1:
            lo = mid + 1
        else:
            hi = mid
    return lo