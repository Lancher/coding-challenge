# LEETCODE@ 10. Regular Expression Matching
#
# --END--


def isMatch(s, p):
    # 1) dp init
    dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
    dp[0][0] = True

    # 2)  s = "aab", p = "c*a*b" will be true
    for j in range(len(p)):
        if p[j] == '*':
            dp[0][j+1] = dp[0][j-1]

    # 3)    "" a *
    #    "" 1  0 0
    #     a 0  1 1
    #     a 0  0
    #     a
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == '.' or s[i] == p[j]:
                dp[i+1][j+1] = dp[i][j]
            if p[j] == '*':
                if p[j-1] != '.' and s[i] != p[j-1]:
                    dp[i+1][j+1] = dp[i+1][j-1]
                else:
                    dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
    return dp[len(s)][len(p)]
