# LEETCODE@ 658. Find K Closest Elements
#
# --END--


def findClosestElements(self, arr, k, x):
    # empty array
    if not arr or k == 0:
        return []

    # binary search
    n = len(arr)
    lo, hi = 0, n - 1
    while lo < hi:
        mi = int((lo + hi) / 2)
        if arr[mi] < x:
            lo = mi + 1
        else:
            hi = mi

    # [3, 7] find 4, but 3 is closer, so we need to check this
    if lo - 1 >= 0 and x - arr[lo - 1] < arr[lo] - x:
        lo -= 1

    # extend to left adn right
    cnt = 1
    l, r = lo - 1, lo + 1
    while cnt < k:
        if 0 <= l and r <= n - 1:
            if x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        elif 0 <= l:
            l -= 1
        else:
            r += 1
        cnt += 1
    return arr[l + 1:r]