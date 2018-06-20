# LEETCODE@ 801. Minimum Swaps To Make Sequences Increasing
#
# 1) Conditional DP
#
# 2) Can we swap or not.
#
# --END--


def minSwap(self, A, B):
    # 1) Example:
    # [1,3,5,4]
    # [1,2,3,7]
    n = len(A)
    swap, noswap = 1, 0

    for i in range(1, n):
        # 2) We have to determine whether we can swap.
        nochange_ok = A[i - 1] < A[i] and B[i - 1] < B[i]
        change_ok = A[i - 1] < B[i] and B[i - 1] < A[i]

        if nochange_ok and change_ok:
            n_swap = min(swap, noswap) + 1
            n_noswap = min(swap, noswap)
            swap, noswap = n_swap, n_noswap
        elif nochange_ok:
            swap += 1
        elif change_ok:
            n_swap = noswap + 1
            n_noswap = swap
            swap, noswap = n_swap, n_noswap

    return min(swap, noswap)
