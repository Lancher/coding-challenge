# LEETCODE@ 821. Shortest Distance to a Character
#
# 1) Example:
#
#    ----> Right
#
#    x x x x C x x x x
#    n n n n 0 1 2 3 4
#
#    <---- Left
#
#    x x x x C x x x x
#    4 3 2 1 0 1 2 3 4
#
# --END--


def shortestToChar(self, S, C):
    n = len(S)
    pos = -(n - 1)
    res = [n - 1] * n

    for i in range(n):
        if S[i] == C:
            pos = i
        res[i] = min(res[i], abs(i - pos))

    pos = -(n - 1)
    for i in range(n - 1, -1, -1):
        if S[i] == C:
            pos = i
        res[i] = min(res[i], abs(i - pos))

    return res
