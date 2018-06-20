# LEETCODE@ 204. Count Primes
#
# --END


def countPrimes(self, n):
    if n < 3:
        return 0

    dp = [1] * n
    # 1) 1 is not prime number
    dp[0] = dp[1] = 0

    for i in range(2, n):
        if dp[i]:
            for j in range(2, n):
                if i * j >= n:
                    break
                dp[i * j] = 0
    return sum(dp)
