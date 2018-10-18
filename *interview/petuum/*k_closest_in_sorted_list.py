
def findClosestElements(self, arr, k, x):
    n = len(arr)
    lo, hi = 0, n - 1

    # find the element equal or greater than x
    while lo < hi:
        mi = (lo + hi) // 2
        if arr[mi] < x:
            lo = mi + 1
        else:
            hi = mi

    # it is possible that the element we find is not the best answer
    if 0 <= lo - 1 and abs(arr[lo-1] - x) < abs(arr[lo] - x):
        lo -= 1

    # try to find our left & right bound of array
    k -= 1
    l, r = lo - 1, lo + 1
    while k:
        if 0 <= l and r < n:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
        elif 0 <= l:
            l -= 1
        else:
            r += 1
        k -= 1
    return arr[l+1:r]