# LEETCODE@ 781. Rabbits in Forest
#
# 1. There a trap in here.
#
#   [1, 1, 1, 2] => [1, 1] [1] [2] the total is 7.
#
# --END--


def numRabbits(self, answers):
    n = 1000
    counter = [0] * n

    for ans in answers:
        counter[ans] += 1

    res = counter[0]
    for i in range(1, n):
        while counter[i] > 0:
            counter[i] -= i + 1
            res += i + 1
    return res
