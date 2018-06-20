# LEETCODE@ 276. Paint Fence
#
# 1) The idea:
#
#   Case1:
#
#   0     1
#   Red   Red     (k)
#   Red   Blue    (k)(k-1)   ----------------
#                                           |
#   0     1     2                           |
#   Red   Red   Blue (k)(k-1)               |
#                                           |
#   Red   Blue  Blue (k)(k-1)  <------------|
#   Red   Blue  Red  (k)(k-1)(k-1)
#
# --END--


def numWays(self, n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    same = k * 1
    diff = k * (k - 1)
    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff
