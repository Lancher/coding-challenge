# LEETCODE@ 656. Coin Path
#
# 1. If there are two path to reach n, and they have the same optimal cost,
#    then the longer path is lexicographically smaller.
#
# --END--


def cheapestJump(self, A, B):
    _MAX = float('inf')

    n = len(A)
    cost = [_MAX] * n
    parent = [-1] * n
    length = [0] * n

    cost[0] = A[0]
    length[0] = 1
    for i in range(1, n):
        if A[i] == -1:
            continue
        for j in range(max(0, i - B), i, 1):
            alt = cost[j] + A[i]
            # If there are two path to reach n, and they have the same optimal cost,
            # then the longer path is lexicographically smaller.
            if alt < cost[i] or alt == cost[i] and length[i] < length[j] + 1:
                cost[i] = alt
                parent[i] = j
                length[i] = length[j] + 1

    # if we can not reach the end
    if cost[n - 1] == _MAX:
        return []

    # build the res from indexes
    res = []
    i = n - 1
    while i >= 0:
        res.append(i)
        i = parent[i]
    res = res[::-1]

    return [num + 1 for num in res]