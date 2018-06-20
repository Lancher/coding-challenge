# LEETCODE@ 14. Longest Common Prefix
#
# --END--


def longestCommonPrefix(strs):
    if not strs:
        return ''

    k = len(strs[0])
    for i in range(len(strs)):
        j = 0
        while j < k and j < len(strs[i]) and strs[0][j] == strs[i][j]:
            j += 1
        k = j
    return strs[0][:k]
