# LEETCODE@ 254. Factor Combinations
#
# --END--
import math


def getFactors(self, n):
    res = []
    self.helper(2, [n], res)
    return res


def helper(self, i_s, l, res):
    n = l.pop()
    for i in range(i_s, int(math.sqrt(n)) + 1):
        if n % i == 0 and i <= int(n / i):
            nxt_n = int(n / i)
            res.append(l + [i, nxt_n])
            self.helper(i, l + [i, nxt_n], res)