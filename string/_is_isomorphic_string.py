# LEETCODE@ 205. Isomorphic Strings
#
# --END--


def isIsomorphic(s, t):
    d1, d2 = [-1] * 256, [-1] * 256
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i
        d2[ord(t[i])] = i
    return True
