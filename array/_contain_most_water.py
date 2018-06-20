# LEETCODE@ 11. Container With Most Water
#
# 1. Use two pointer `i` and `j` to approach.
#
# --END--


def maxArea(self, height):
    res = 0
    n = len(height)
    i, j = 0, len(height) - 1

    while i < j:
        res = max(res, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res
