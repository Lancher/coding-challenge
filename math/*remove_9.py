# LEETCODE@ 660. Remove 9
#
# 1. Example:
#
#   In base 10, the series, after removing 9, will be:
#   1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19
#   output - 19 (correct)
#
#   If number is converted to base 9, the series will be:
#   1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,20
#   output - 20 (which is not correct)
#
# --END--


def newInteger(self, n):

    ans = ''
    while n:
        ans = str(n % 9) + ans
        n /= 9
    return int(ans)
