# LEETCODE@ 3. Longest Substring Without Repeating Characters
#
# --END--


def lengthOfLongestSubstring(s):
    n = len(s)
    d = {}
    i = 0
    res = 0
    for j in range(n):
        if s[j] in d:
            # 1) i should always move forward i.e: "abba"
            i = max(i, d[s[j]] + 1)
        res = max(res, j - i + 1)
        d[s[j]] = j
    return res

