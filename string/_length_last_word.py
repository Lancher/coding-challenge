# LEETCODE@ 58. Length of Last Word
#
# --END--


def lengthOfLastWord(self, s):
    res = 0
    word_seen = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            if word_seen:
                return res
        else:
            word_seen = True
            res += 1
    return res
