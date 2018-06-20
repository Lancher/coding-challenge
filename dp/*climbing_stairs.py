# LEETCODE@ 70. Climbing Stairs
#
# --END--


def climbStairs(self, n):
    if n < 2:
        return 1

    pp, p = 1, 1
    cur = 0
    for i in range(2, n + 1):
        cur = pp + p
        pp, p = p, cur

    return cur
