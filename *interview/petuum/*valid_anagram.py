# LEETCODE@ 242. Valid Anagram
#
# 1. The freq of two strings should be equal.
#
# --END--
import collections


def isAnagram(self, s, t):
    c1 = collections.Counter(s)
    c2 = collections.Counter(t)
    return c1 == c2
