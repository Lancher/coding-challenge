# 87. Scramble String
#
# --END--


def isScramble(self, s1, s2):
    if s1 == s2:
        return True
    # prune the recursive call
    count = [0] * 256
    for c in s1:
        count[ord(c)] += 1
    for c in s2:
        count[ord(c)] -= 1
    for i in count:
        if i != 0:
            return False
    #
    for i in range(1, len(s1)):
        if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
            return True
        if self.isScramble(s1[:i], s2[len(s1) - i:]) and self.isScramble(s1[i:], s2[:len(s1) - i]):
            return True
    return False
