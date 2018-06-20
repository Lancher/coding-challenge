# LEETCODE@ 795. Number of Subarrays with Bounded Maximum
#
# 1) Example: [2, 1, 4, 3]
#
# --END--


def numSubarrayBoundedMax(self, A, L, R):
    j = 0
    res = 0
    cnt = 0
    for i in range(len(A)):
        if L <= A[i] <= R:
            res += i - j + 1
            cnt = i - j + 1
        elif A[i] < L:
            res += cnt
        else:
            j = i + 1
            cnt = 0
    return res
