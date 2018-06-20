# LEETCODE@ 784. Letter Case Permutation
#
# --END--


def letterCasePermutation(self, S):
    res = []
    self.helper(S, 0, res)
    return res


def helper(self, S, i, res):
    res.append(S)
    for j in range(i, len(S)):
        if 0 <= ord(S[j]) - ord('a') < 26:
            self.helper(S[:j] + S[j].upper() + S[j + 1:], j + 1, res)
        if 0 <= ord(S[j]) - ord('A') < 26:
            self.helper(S[:j] + S[j].lower() + S[j + 1:], j + 1, res)
