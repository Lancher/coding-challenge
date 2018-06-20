# LEETCODE@ 806. Number of Lines To Write String
#
# --END


def numberOfLines(self, widths, S):
    i, j = 0, 0
    for c in S:
        incr = widths[ord(c) - ord('a')]
        if j + incr < 100:
            j += incr
        elif j + incr == 100:
            i += 1
            j = 0
        else:
            i += 1
            j = incr
    return [i + 1, j]
