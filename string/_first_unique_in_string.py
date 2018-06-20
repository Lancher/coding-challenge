# LEETCODE@ 387. First Unique Character in a String
#
# --END--


def first_uniq_char(s):
    chars = [0] * 256
    for c in s:
        chars[ord(c)] += 1
    for i in range(len(s)):
        if chars[ord(s[i])] == 1:
            return i
    return -1
