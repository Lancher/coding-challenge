# LEETCODE@ 266. Palindrome Permutation
#
# --END--


import collections


def canPermutePalindrome(self, s):
    counter = collections.Counter(s)

    one_seen = 0
    for c in counter:
        if counter[c] % 2 == 1:
            if one_seen:
                return False
            one_seen = 1
    return True


# LEETCODE@ 267. Palindrome Permutation II
#
# 1. In backtracing, to avoid duplicate we only run each character once on each layer.
#
# --END


def generatePalindromes(self, s):
    counter = collections.Counter(s)

    # allow only single odd
    odd = ''
    for c in counter:
        if counter[c] % 2 == 1:
            if odd:
                return []
            odd = c
            counter[c] -= 1

    # res
    res = []
    self.backtracing(odd, counter, len(odd), len(s), res)
    return res


def backtracing(self, s, counter, i, n, res):
    if i == n:
        res.append(s)
    else:
        # to avoid duplicate, we only run each character once on each layer
        for c in counter:
            if 0 < counter[c]:
                counter[c] -= 2
                self.backtracing(c + s + c, counter, i + 2, n, res)
                counter[c] += 2