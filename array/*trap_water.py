# LEETCODE@ 42. Trapping Rain Water
#
# Solution 1: find the max. let left approach the max. let right approach max.
#
#
# Solution 2: two pointer
#
# --END


def trap(self, height):
    n = len(height)
    res = 0

    # find the max
    k = 0
    for i in range(1, n):
        if height[k] < height[i]:
            k = i

    # left index approach max
    mx = 0
    for i in range(k):
        mx = max(mx, height[i])
        res += mx - height[i]

    # right index approach max
    mx = 0
    for i in range(n - 1, k, -1):
        mx = max(mx, height[i])
        res += mx - height[i]

    return res


def trap(height):
    res = 0

    l, r = 0, len(height) - 1
    l_max, r_max = 0, 0

    while l < r:
        if height[l] < height[r]:
            l_max = max(l_max, height[l])
            res += l_max - height[l]
            l += 1
        else:
            r_max = max(r_max, height[r])
            res += r_max - height[r]
            r -= 1
    return res
