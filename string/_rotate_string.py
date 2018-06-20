# LEETCODE@ 796. Rotate String
#
# --END--


import collections


def rotateString(self, A, B):
    if collections.Counter(A) != collections.Counter(B):
        return False

    n = len(A)
    for i in range(1, n):
        s = A[i:] + A[:i]
        if s == B:
            return True
    return False
