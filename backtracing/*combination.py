# LEETCODE@ 39. Combination Sum
#
# 1. Sort the candidates first.
#
# 2. We did not skip duplicate here is that `candidate` does not have duplicate items.
#
# --END--


def combinationSum(self, candidates, target):
    l, res = [], []
    candidates.sort()
    self.backtracing(candidates, 0, target, 0, res, l)
    return res


def backtracing(self, candidates, i, target, s, res, l):
    if s == target:
        res.append(l[:])
    else:
        for j in range(i, len(candidates)):
            # we did not skip duplicate here is that `candidate` does not have duplicate items
            if candidates[j] + s <= target:
                l.append(candidates[j])
                self.backtracing(candidates, j, target, candidates[j] + s, res, l)
                l.pop()


# LEETCODE@ 40. Combination Sum II
#
# 1. Sort the candidates first.
#
# 2. There might be duplicate elements in `candidates`, so we have to check whether to skip or not.
#
# --END--


def combinationSum2(self, candidates, target):
    res, l = [], []
    candidates.sort()
    self.backtracing(candidates, 0, target, 0, res, l)
    return res


def backtracing(self, candidates, i, target, s, res, l):
    if s == target:
        res.append(l[:])
    else:
        for j in range(i, len(candidates)):
            #
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            if candidates[j] + s <= target:
                l.append(candidates[j])
                self.backtracing(candidates, j + 1, target, s + candidates[j], res, l)
                l.pop()


# LEETCODE@ 216. Combination Sum III
#
# --END--


def combinationSum3(self, k, n):
    cands = [i for i in range(1, 10)]
    l, res = [], []
    self.backtracing(cands, k, n, 0, 0, l, res)
    return res


def backtracing(self, cands, k, n, i, s, l, res):
    if len(l) == k:
        if s == n:
            res.append(l[:])
    else:
        if len(l) < k:
            for j in range(i, len(cands)):
                if s + cands[j] <= n:
                    l.append(cands[j])
                    self.backtracing(cands, k, n, j + 1, s + cands[j], l, res)
                    l.pop()


# LEETCODE@ 77. Combinations
#
# --END--
def combine(self, n, k):
    l, res = [], []
    self.backtracing(n, k, 0, l, res)
    return res


def backtracing(self, n, k, s, l, res):
    if len(l) == k:
        res.append(l[:])
    else:
        if len(l) + n - s < k:
            return
        for i in range(s + 1, n + 1):
            l.append(i)
            self.backtracing(n, k, i, l, res)
            l.pop()


