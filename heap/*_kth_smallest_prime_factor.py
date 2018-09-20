# LEETCODE@ 786. K-th Smallest Prime Fraction
#
# 1. TODO: Very Good Explanation https://goo.gl/wyHLNw
#
# 2. Heap solution for [1, 2, 3, 5]
#
#    1: [1/5, 1/3, 1/2]
#
#    2: [2/5, 2/3]
#
#    3: [3/5]
#
#    5: []
#
#    Push the n to the heap and pop K - 1 times. The heap[0] is or answer
#
# 3. Trail & Error solution for [1, 2, 3, 5]
#
# --END--
import heapq


def kthSmallestPrimeFraction(self, A, K):
    # A = [1, 2, 3, 5], K = 3
    #
    # 0: [1/5, 1/3/, 1/2 ]
    # 1: [2/5, 2/3]
    # 2: [3/5]
    # 3: []

    # height of heap is equal to log(len(A))
    h = []
    for i in range(len(A) - 1):
        j = len(A) - 1
        heapq.heappush(h, [A[i] / A[j], i, j])

    # pop k - 1 times then We get our answer
    for _ in range(K - 1):
        val, i, j = heapq.heappop(h)
        j -= 1
        if i < j:
            heapq.heappush(h, [A[i] / A[j], i, j])

    return [A[h[0][1]], A[h[0][2]]]


def kthSmallestPrimeFraction(self, A, K):
    # A = [1, 2, 3, 5], K = 3
    #
    # 0: [1/5, 1/3, 1/2]
    # 1: [2/5, 2/3]
    # 2: [3/5]
    # 3: []

    # binary search
    lo, hi = 0, 1
    while lo < hi:
        mi = (lo + hi) / 2
        cnt = 0
        p, q = 0, 1

        # count the elements < mi
        for i in range(len(A)):
            for j in range(len(A) - 1, i, -1):
                if A[i] / A[j] <= mi:
                    cnt += 1

                    # update p, q
                    if p / q < A[i] / A[j]:
                        p, q = A[i], A[j]
                else:
                    break

        if cnt < K:
            lo = mi
        elif K < cnt:
            hi = mi
        else:
            return [p, q]
