# LEETCODE@ 667. Beautiful Arrangement II
#
# 1. Example: n = 5, k = 4
#
#   => [1]
#   => [1, 5]
#   => [1, 5, 2]
#   => [1, 5, 2, 4]
#   => [1, 5, 2, 4, 3]
#
#   Example: n = 5, k = 3
#
#   => [1, 2]
#   => [1, 2, 5]
#   => [1, 2, 5, 3]
#   => [1, 2, 5, 3, 4]
#
# --END--


def constructArray(self, n, k):
    res = []
    max_k = n - 1
    for i in range(max_k - k + 1):
        res.append(i + 1)

    turn = 0
    s, e = max_k - k + 2, n
    while s <= e:
        if turn % 2 == 0:
            res.append(e)
            e -= 1
        else:
            res.append(s)
            s += 1
        turn += 1
    return res
