# LEETCODE@ 702 Search in a Sorted Array of Unknown Size
#
# --END--


def search(self, reader, target):
    _MAX = 2147483647
    lo, hi = 0, 10000 - 1

    while lo < hi:
        mi = int((lo + hi) / 2)
        val = reader.get(mi)
        print(lo, mi, hi, val)

        if val == _MAX:
            hi = mi - 1
        elif val == target:
            return mi
        elif val < target:
            lo = mi + 1
        else:
            hi = mi

    # for example [0], we need to check the lo as well.
    if reader.get(lo) == target:
        return lo
    return -1
