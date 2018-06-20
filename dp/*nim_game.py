# LEETCODE@ 292. Nim Game
#
# 1) https://drive.google.com/drive/folders/0B2NGRuIMPIZGMVNlNm0tWFcxWVE
#
# 2) The last one remove all the stones is the winner.
#
# 3) The diagram
#
#                    W[6]
#                /     |    \
#               /      |     \
#            W[5]    L[4]    W[3]
#           / |      / | \     \
#          /  |     /  |  \     \
#       L[4] W[3] W[3] W[2] W[1]
#
# --END--


def canWinNim(self, n):
    if n == 0:
        return False
    elif n < 4:
        return True
    dp = [False] * (n + 1)
    dp[0] = False
    dp[1] = dp[2] = dp[3] = True

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] == False or dp[i - 2] == False or dp[i - 3] == False
    return dp[n]
