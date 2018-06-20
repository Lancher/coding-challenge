# LEETCODE@ 277. Find the Celebrity
#
# 1. A celebrity does not know anyone and everybody know him.
#
# --END


def findCelebrity(self, n):
    a = 0

    # if a knows i, `i` might be candidate.
    for i in range(n):
        if knows(a, i):
            a = i

    # check if this is the candidate
    for i in range(n):
        if i != a and (knows(a, i) or not knows(i, a)):
            return -1
    return a
