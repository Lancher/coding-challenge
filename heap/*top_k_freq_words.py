import collections
import heapq


class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution(object):
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)

        h = []
        for word, count in counts.items():
            heapq.heappush(h, (Element(count, word), word))
            if len(h) > k:
                heapq.heappop(h)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res[::-1]
