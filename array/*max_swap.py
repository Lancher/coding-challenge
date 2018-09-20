# LEETCODE@ 670. Maximum Swap
#
# --END--


def maximumSwap(self, num):
    s = str(num)
    n = len(s)

    max_idx, max_digit = -1, '-1'
    left_idx, right_idx = -1, -1

    # find smaller elements relative to max_digit.
    for i in range(n - 1, -1, -1):
        if s[i] > max_digit:
            max_digit = s[i]
            max_idx = i
        if s[i] < max_digit:
            left_idx = i
            right_idx = max_idx

    l = list(s)
    l[left_idx], l[right_idx] = l[right_idx], l[left_idx]
    return int(''.join(l))
