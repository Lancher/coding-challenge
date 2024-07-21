# LEETCODE@ 347. Top K Frequent Elements
#
# 1) bucket sort concept
#
# --END--
import collections


def topKFrequent(self, nums, k):
    n = len(nums)
    bucket = [[] for _ in range(n + 1)]

    # 1) count each element and put it into bucket
    counter = collections.Counter(nums)
    for num in counter:
        bucket[counter[num]].append(num)

    res = []
    # 2) pop from the end
    i = n
    for _ in range(k):
        while not bucket[i]:
            i -= 1
        res.append(bucket[i].pop())

    return res
