# LEETCODE@ 128. Longest Consecutive Sequence
#
# --END--


def longest_consecutive_seq(nums):
    if not nums:
        return 0

    res = 1
    d = {}
    for num in nums:
        # 1) we skip the duplicate items
        if num in d:
            continue
        # 2) find the length of left & right
        left = d[num - 1] if num - 1 in d else 0
        right = d[num + 1] if num + 1 in d else 0
        length = left + 1 + right

        # 3) try to join the left & right together
        d[num - left] = length
        d[num] = length
        d[num + right] = length
        res = max(res, length)
    return res
