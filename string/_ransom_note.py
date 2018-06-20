# LEETCODE@ 383. Ransom Note
#
# --END--


def canConstruct(ransomNote, magazine):
    chars = [0] * 256
    for c in magazine:
        chars[ord(c)] += 1
    for c in ransomNote:
        chars[ord(c)] -= 1
        if chars[ord(c)] < 0:
            return False
    return True
