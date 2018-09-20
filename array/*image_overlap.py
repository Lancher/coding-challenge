# LEETCODE@ 835. Image Overlap
#
# 1. https://leetcode.com/problems/image-overlap/discuss/130623/C++JavaPython-Straight-Forward
#
# TODO: Brilliant Solution
#
# --END--


def largestOverlap(self, A, B):
    N = len(A)
    LA = [i / N * 100 + i % N for i in xrange(N * N) if A[i / N][i % N]]
    LB = [i / N * 100 + i % N for i in xrange(N * N) if B[i / N][i % N]]

    # Count number of the same shifts
    c = collections.Counter(i - j for i in LA for j in LB)
    return max(c.values() or [0])
