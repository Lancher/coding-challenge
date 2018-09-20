# LEETCODE@ 600. Non-negative Integers without Consecutive Ones
#
# 1. https://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
#
# --END--


def findIntegers(self, num):
    # convert to binary
    bi = bin(num)[2:]
    n = len(bi)

    # i-th bit with 0 or 1
    ones = [0] * n
    zeros = [0] * n
    ones[0] = zeros[0] = 1
    for i in range(1, n):
        zeros[i] = zeros[i - 1] + ones[i - 1]
        ones[i] = zeros[i - 1]
    res = zeros[n - 1] + ones[n - 1]

    # subtract the numbers with the same lenght and greater than num
    #         MSB ----- LSB
    # Index:   0  ------ n
    # String:      1000    == 8
    #
    # we need to subtract 1010 & 1001
    #
    # The answer will be 6.
    for i in range(1, len(bi)):
        if bi[i] == '0' and bi[i - 1] == '0':
            # if bi[i] = 1, then the number is greater than the num, so we have to subtract 01 end with 1
            res -= ones[len(bi) - i - 1]
        elif bi[i] == '1' and bi[i - 1] == '1':
            # if there are two consecutive 1, we can gurantee there is no more answer about it.
            break
        elif bi[0] == '0' and bi[i - 1] == '1':
            # bi[i] can not be '1' because it will have two consecutive 1.
            continue
        else:
            # bi[i+1] can not be '1' because it will have two consecutive 1.
            continue
    return res
