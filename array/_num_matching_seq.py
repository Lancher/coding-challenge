# LEETCODE@ 792. Number of Matching Subsequences
#
# 1. Very Brilliant !!!!!
#
#   S = "abcde"
#   words = ["a", "bb", "acd", "ace"]
#
#   'a':  ["(a)", "(a)cd", "(a)ce"]
#   'b':  ["(b)b"]
#
#   'b':  ["(b)b"]
#   'c':  ["a(c)d", "a(c)e"]
#   None: ["a"]
#
#   'b':  ["b(b)"]
#   'c':  ["a(c)d", "a(c)e"]
#   None: ["a"]
#
# --END--
import collections


def numMatchingSubseq(self, S, words):
    d = collections.defaultdict(list)

    # add first verified character
    for word in words:
        d[word[0]].append([word, 1])

    res = 0
    for c in S:

        buf = []
        while d[c]:
            buf.append(d[c].pop())

        # append the next character to another bucket
        for word, i in buf:
            if i == len(word):
                res += 1
            else:
                d[word[i]].append([word, i + 1])

    return res
