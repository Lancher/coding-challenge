# LEETCODE@ 823. Binary Trees With Factors
#
# --END--


def numFactoredBinaryTrees(self, A):
    n = len(A)
    A.sort()

    dp = {}
    for i in range(n):
        cnt = 1
        for j in range(i):
            # 1) avoid time limit by j * j <= i
            if A[j] * A[j] <= A[i] and A[i] % A[j] == 0 and int(A[i] / A[j]) in dp:
                a, b = dp[A[j]], dp[int(A[i] / A[j])]
                cnt += a * b
                cnt += a * b if A[j] != int(A[i] / A[j]) else 0
        dp[A[i]] = cnt

    res = sum(dp.values())
    res = int(res % (1e9 + 7))
    return res
