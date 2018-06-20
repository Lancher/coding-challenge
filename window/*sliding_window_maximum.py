# LEETCODE@ 239. Sliding Window Maximum
#
# 1. from collections import deque
#    deque.push()
#    deque.pushleft()
#    deque.pop()
#    deque.popleft()
#
# 2. Example:
#
#   DeQueue: store index, let values from High -> Low
#
#             |------|
#   Array:   [1, 3, -1, -3, 5, 3, 8, 10]
#
#   i = 0, DeQueue: [0]
#
#   i = 1, DeQueue: [1]
#
#   i = 2, DeQueue: [1, 2]
#
#   i = 3, DeQueue: [1, 2, 3] => the first item is the largest
#
#   i = 4, DeQueue: [4] => `5` will erase the previous items and become the first
#
#   i = 5, DeQueue: [4, 5] => the first item is the largest
#
#   i = 6, DeQueue: [6] => `8` will erase the previous items and become the first
#
#   i = 7, DeQueue: [7] => `10` will erase the previous items and become the first
#
# --END--
from collections import deque


def maxSlidingWindow(self, nums, k):
    res = []
    dq = deque()
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
