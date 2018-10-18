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




def topKFrequent(self, nums, k):
    # init
    n = len(nums)

    # count the freq for each character
    counter = collections.Counter(nums)

    # sort the pair by freq
    pairs = [[counter[num], num] for num in counter]
    pairs.sort()

    # get top k freq elements into result list
    res = []
    for i in range(len(pairs) - 1, len(pairs) - k - 1, -1):
        res.append(pairs[i][1])

    return res
