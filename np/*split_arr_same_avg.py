# LEETCODE@ 805. Split Array With Same Average
#
# 1. TLE
#
# --END


def splitArraySameAverage(self, A):
    if len(A) == 1:
        return False
    n = len(A)
    for l in range(1, int(n / 2) + 1):
        if sum(A) * l % n == 0:
            res = [False]
            self.exist(A, 0, l, 0, int(sum(A) * l / n), res)
            if res[0]:
                return True
    return False


def exist(self, arr, i, cnt, sm, target, res):
    if res[0]:
        return
    if cnt == 0:
        if sm == target:
            res[0] = True
    else:
        for j in range(i, len(arr)):
            if sm + arr[j] <= target:
                self.exist(arr, j + 1, cnt - 1, sm + arr[j], target, res)