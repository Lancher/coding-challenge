# LEETCODE@ 791. Custom Sort String
#
# 1. Nothing special, count the freq of each character.
#
# --END--


import collections


def customSortString(self, S, T):
    d = collections.defaultdict(int)
    for c in T:
        d[c] += 1

    res = ''
    for c in S:
        if d[c] > 0:
            res += c * d[c]
            d[c] = 0

    for c in d:
        res += c * d[c]

    return res
