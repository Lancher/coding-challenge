

# LEETCODE@ 30. Substring with Concatenation of All Words
#
# You are given a string, s, and a list of words, words, that are all of the same length.
import collections
import copy


def findSubstring(self, s, words):
    res = []
    sz = len(words[0])
    n = len(words) * len(words[0])

    for i in range(len(s) - n + 1):
        # reset counters & cnt
        counter = collections.Counter(words)
        cnt = len(words)

        for j in range(i, i + n, sz):
            word = s[j:j + sz]
            if counter[word]:
                counter[word] -= 1
                cnt -= 1
            else:
                break
        if cnt == 0:
            res.append(i)

    return res

