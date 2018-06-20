# 1. https://www.youtube.com/watch?v=hgA4xxlVvfQ
# 2. http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/


# time complexity O(2^n)
def optimal_bst_recursive(keys, freqs, i, j):
    if i > j:
        return 0
    s = sum(freqs[i:j+1])

    res = 1000000
    for k in range(i, j + 1):
        cost = s + optimal_bst_recursive(keys, freqs, i, k - 1) + optimal_bst_recursive(keys, freqs, k + 1, j)
        if cost < res:
            res = cost
    return res


keys = [10, 12, 20]
freqs = [34, 8, 50]
print(optimal_bst_recursive(keys, freqs, 0, len(freqs) - 1))


# time complexity O(n^3)
def optimal_bst_iterative(keys, freqs):

    n = len(freqs)
    dp = [[100000 for j in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = freqs[i]

    for l in range(2, n + 1):
        i, j = 0, l - 1
        s = sum(freqs[i:j+1])

        for k in range(i, j + 1):
            left_s = dp[i][k-1] if i <= k - 1 else 0
            right_s = dp[k+1][j] if k + 1 <= j else 0
            cost = left_s + s + right_s
            if cost < dp[i][j]:
                dp[i][j] = cost
    return dp[0][n-1]


keys = [10, 12, 20]
freqs = [34, 8, 50]
print(optimal_bst_iterative(keys, freqs))
