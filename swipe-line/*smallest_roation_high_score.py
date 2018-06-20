# LEETCODE@ 798. Smallest Rotation with Highest Score
#
# Find the rotation ranges!!!!!
#
# --END--


def bestRotation(self, A):
    n = len(A)
    bucket = [0] * (n + 1)
    intervals = []

    for i in range(n):
        # index: 0 1 2 3 4
        #            2
        # It will be two ranges [0, 1] [3, 5]
        if A[i] == i:
            intervals.append([0, 1])
            intervals.append([i + 1, n])
        # index: 0 1 2 3 4
        #            1
        # It will be two ranges [0, 2] [3, 5]
        elif A[i] < i:
            intervals.append([0, i - A[i] + 1])
            intervals.append([i + 1, n])
        # index: 0 1 2 3 4
        #            3
        # It will be two ranges [3, 5]
        else:
            intervals.append([i + 1, n - (A[i] - i) + 1])

    for i, j in intervals:
        bucket[i] += 1
        bucket[j] -= 1

    for i in range(1, n + 1):
        bucket[i] += bucket[i-1]

    res, mx = 0, 0
    for i in range(n):
        if mx < bucket[i]:
            res, mx = i, bucket[i]

    return res
