# LEETCODE@ 793. Preimage Size of Factorial Zeroes Function
#
#   [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#   [1,  2,  3,  4,  6,  7,  8,  9, 10, 12]
#
#   k = 5
#
#   lo  mi  hi
#    0  12  25  => 2 0s
#   13  19  25  => 3 0s
#   20  22  25  => 4 0s
#   23  24  25  => 4 0s
#
#   lo = 25     => count 25 and there are 6 zeros, so k == 5 is impossible
# 
# --END--


def preimageSizeFZF(self, K):
    lo, hi = 0, K * 5

    while lo < hi:
        mi = int((lo + hi) / 2)

        # count how many 5s
        cnt = 0
        tmp = mi
        while tmp:
            cnt += int(tmp / 5)
            tmp = int(tmp / 5)

        # judge bst
        if cnt < K:
            lo = mi + 1
        else:
            hi = mi

    # count how many 5s
    cnt = 0
    while lo:
        cnt += int(lo / 5)
        lo = int(lo / 5)

    return 5 if cnt == K else 0
