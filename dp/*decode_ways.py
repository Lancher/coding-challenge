# LEETCODE@ 91. Decode Ways
#
# 1) Build dp array.
#
# 2) What is each dp[] entry meaning.
#
# 3) Find the formulation of last item.
#
# 4) Set the dp[0].
#
# --END--


def numDecodings(self, s):
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        # one digit
        if 1 <= int(s[i]) <= 9:
            dp[i + 1] += dp[i]

        # two digits
        if 1 <= i and s[i - 1] != '0' and 1 <= int(s[i - 1:i + 1]) <= 26:
            dp[i + 1] += dp[i - 1]

    return dp[n]
