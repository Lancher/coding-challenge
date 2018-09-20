# LEETCODE@ 718. Maximum Length of Repeated Subarray
#
# --END--


def findLength(self, A, B):
    # na, nb
    na, nb = len(A), len(B)
    dp = [[0 for j in range(nb + 1)] for i in range(na + 1)]

    # try to match each string
    res = 0
    for i in range(na):
        for j in range(nb):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                res = max(res, dp[i + 1][j + 1])
    return res


def findLength(self, A, B):
    na, nb = len(A), len(B)
    suffix_a, suffix_b = [], []
    for i in range(na):
        suffix_a.append([A[i:], 'a'])
    for i in range(nb):
        suffix_b.append([B[i:], 'b'])

    arrs = suffix_a + suffix_b
    arrs.sort(key=lambda o: o[0])

    res = 0

    for i in range(len(arrs) - 1):
        if arrs[i][1] == arrs[i + 1][1]:
            continue
        m = min(len(arrs[i][0]), len(arrs[i + 1][0]))
        j = 0
        while j < m and arrs[i][0][j] == arrs[i + 1][0][j]:
            j += 1

        res = max(res, j)
    return res