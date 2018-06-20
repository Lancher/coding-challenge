# LEETCODE@ 345. Reverse Vowels of a String
#
# 1) Two pointers
#
# --END--


def reverseVowels(s):
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and s[i] not in 'aeiouAEIOU':
            i += 1
        while i < j and s[j] not in 'aeiouAEIOU':
            j -= 1
        if i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return ''.join(s)