# LEETCODE@ 214. Shortest Palindrome
#
# 1) Solution 1
#
#   Start with string "abcd".
#
#   Reverse the string "dcba".
#
#   Is the original string "abcd" start with substring "dcba".
#
#   Is the original string "abcd" start with substring "cba".
#
#   Is the original string "abcd" start with substring "ba".
#
#   Is the original string "abcd" start with substring "a".
#
#   Then "dcb" + "abcd" is "dcbabcd"
#
# 2) Solution 2
#
#   Build the new string where "abcd" + "#" + "dcba"
#
#   Use KMP to find the largest value in prefix array.
#
# --END--


def shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s


def shortestPalindrome(self, s):
    # 1) Use KMP to buid prefix array
    com_s = s + '#' + s[::-1]
    n = len(com_s)
    prefix = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and com_s[j] != com_s[i]:
            j = prefix[j - 1]
        if com_s[j] == com_s[i]:
            j += 1
        prefix[i] = j
    # 2) we find the value in the last cell which mean the largest palindrome substring
    m = prefix[n - 1]
    return s[m:][::-1] + s
