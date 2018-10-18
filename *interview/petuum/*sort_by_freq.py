# LEETCODE@ 451


import collections


class Solution(object):
    def frequencySort(self, s):
        # init length & bucket
        n = len(s)
        buckets = [[] for i in range(n + 1)]

        # coun the freq of the string
        counter = collections.Counter(s)

        # put the character into freq buckets
        for ch in counter:
            buckets[counter[ch]].append(ch)

        # build the result string from the ending of buckets
        res = ''
        for i in range(n, 0, -1):
            while buckets[i]:
                res += buckets[i].pop() * i
        return res