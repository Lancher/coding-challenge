# LEETCODE@ 243. Shortest Word Distance
#
# 1. use two indexes to keep updating minimum
#
# --END


def shortestDistance(self, words, word1, word2):
    res = float('inf')
    i1, i2 = -1, -1
    for i in range(len(words)):
        if words[i] == word1:
            i1 = i
        if words[i] == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            res = min(res, abs(i1 - i2))
    return res


# LEETCODE@ 244. Shortest Word Distance II
#
# 1. Use merge sort to find closest in two ascending array
#
# --END--


import collections


class WordDistance:
    def __init__(self, words):
        self.d = collections.defaultdict(list)
        for i in range(len(words)):
            self.d[words[i]].append(i)

    def shortest(self, word1, word2):
        # merge sort to find closest distance
        res = float('inf')
        i, j = 0, 0
        while i < len(self.d[word1]) and j < len(self.d[word2]):
            res = min(res, abs(self.d[word1][i] - self.d[word2][j]))
            if self.d[word1][i] < self.d[word2][j]:
                i += 1
            else:
                j += 1
        return res


# LEETCODE@ 245. Shortest Word Distance III
#
# --END--


def shortestWordDistance(self, words, word1, word2):
    d = collections.defaultdict(list)
    for i in range(len(words)):
        d[words[i]].append(i)

    res = float('inf')

    # if it is the same, we traverse the array
    if word1 == word2:
        for i in range(1, len(d[word1])):
            res = min(res, d[word1][i] - d[word1][i - 1])
    # merge sort to find closest distance
    else:
        i, j = 0, 0
        while i < len(d[word1]) and j < len(d[word2]):
            res = min(res, abs(d[word1][i] - d[word2][j]))
            if d[word1][i] < d[word2][j]:
                i += 1
            else:
                j += 1

    return res
