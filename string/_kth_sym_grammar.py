# LEETCODE@ 779. K-th Symbol in Grammar
#
# 1. Carefully observe the transformation of string
#
# 2. Example
#
#    0: 0
#    1: 01
#    2: 0110
#    3: 01101001
#
# --END--


def kthGrammar(self, N, K):
    n, k = N - 1, K - 1

    res = 0
    while n >= 0:
        l = pow(2, n)
        if l / 2 <= k:
            k -= l / 2
            res += 1
        n -= 1
    return res % 2

