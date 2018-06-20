# LEETCODE@ 28. Implement strStr()
#
# 1) KMP search https://www.youtube.com/watch?v=GTJr8OvyEVQ
#
# --END--


def strStr(self, haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


def strStr(self, haystack, needle):
    if not needle:
        return 0
    # 1) i & j are both on the needle, build the array where prefix is also suffix
    prefix = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        while j > 0 and needle[i] != needle[j]:
            j = prefix[j - 1]
        if needle[i] == needle[j]:
            j += 1
        prefix[i] = j

    # 2) j is on the needle, i is on the haystack
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1
    return -1
