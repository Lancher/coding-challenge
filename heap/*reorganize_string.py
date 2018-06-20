# LEETCODE@ 767. Reorganize String
#
#  1. When we want to find only one result as much as possible, it might be Greedy
#
#  1. import collections
#     counter = collections.Counter(S)
#
#     import heapq
#     heap.heappush
#
#  2. Example:
#
#     1) s = "aaab", res = ""
#
#           [-3, a]
#            /
#           /
#        [-1, b]
#
#
#     2) pop a, res += a
#
#           [-2, a]
#            /
#           /
#        [-1, b]
#
#
#     3) pop a and find that it is the same as previous character, and pop another character.
#
#           [-2, a]
#            /
#           /
#        [0, b]
#
# --END--

import collections
import heapq


def reorganizeString(self, S):
    counter = collections.Counter(S)
    h = []

    for i in range(ord('a'), ord('z') + 1):
        heapq.heappush(h, [-counter[chr(i)], chr(i)])

    res = ''

    # Greedy !!! Since the we only want one result, we put the character as much as possible
    for i in range(len(S)):
        cnt1, ch1 = heapq.heappop(h)
        cnt1 = abs(cnt1)
        if i == 0 or ch1 != res[i - 1]:
            res += ch1
            cnt1 -= 1
            heapq.heappush(h, [-cnt1, ch1])
        else:
            cnt2, ch2 = heapq.heappop(h)
            cnt2 = abs(cnt2)
            if cnt2 == 0:
                return ''
            res += ch2
            cnt2 -= 1
            heapq.heappush(h, [-cnt1, ch1])
            heapq.heappush(h, [-cnt2, ch2])
    return res
