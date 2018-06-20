# LEETCODE@ 131. Palindrome Partitioning
#
#
# --END--


def partition(self, s):
    l, result = [], []
    self.backtracing(s, 0, l, result)
    return result


def backtracing(self, s, i, l, result):
    if i == len(s):
        result.append(l[:])
    else:
        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                l.append(s[i: j+1])
                self.backtracing(s, j + 1, l, result)
                l.pop()


def is_palindrome(self, s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True
