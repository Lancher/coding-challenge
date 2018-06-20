# LEETCODE@ 159. Longest Substring with At Most Two Distinct Characters
#
# 1) Two pointer
#
#  i,j
#   e  c   e   b   a
#
#   i  j
#   e  c   e   b   a
#
#   i      j
#   e  c   e   b   a
#
#   i          j
#   e  c   e   b   a  => there are 3 distinct characters, so we have to move i
#
#          i   j
#   e  c   e   b   a  => once there are only 2 distinct characters, we cam move j forward
#
# --END--


def lengthOfLongestSubstringTwoDistinct(self, s):
    if not s:
        return 0

    n = len(s)
    chars = [0] * 256
    dis_cnt = 0
    i, j = 0, 0

    res = 1
    while j < n:
        c = s[j]
        if dis_cnt < 2:
            if chars[ord(c)] == 0:
                chars[ord(c)] += 1
                dis_cnt += 1
            else:
                chars[ord(c)] += 1
            # update the max length
            res = max(res, j - i + 1)
            j += 1
        elif dis_cnt == 2:
            if chars[ord(c)] == 0:
                chars[ord(c)] += 1
                dis_cnt += 1
            else:
                chars[ord(c)] += 1
                res = max(res, j - i + 1)
            j += 1
        else:
            while i < j:
                chars[ord(s[i])] -= 1
                if chars[ord(s[i])] == 0:
                    dis_cnt -= 1
                    i += 1
                    break
                i += 1
    return res
