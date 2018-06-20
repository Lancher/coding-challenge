# LEETCODE@ 775. Global and Local Inversions
#
# 1. The local inversion can be more than one.
#
# --END--


def isIdealPermutation(self, A):
    for i in range(len(A)):
        if abs(A[i] - i) > 1:
            return False
    return True
