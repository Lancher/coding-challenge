# LEETCODE@ 370. Range Addition
#
# When facing intervals with continuous range, we can swipe the interval from left to right.
#
# --END--


def getModifiedArray(self, length, updates):
    res = [0] * (length + 1)

    for i, j, v in updates:
        res[i] += v
        res[j+1] += -v

    for i in range(1, len(res)):
        res[i] += res[i-1]

    res.pop()
    return res
