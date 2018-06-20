# LEETCODE@ 65. Valid Number
#
# --END--


def isNumber(self, s):
    # 1) 10.3e9
    #    [10].[3]e[9]
    num1_seen = False
    num2_seen = False
    num3_seen = False
    dot_seen = False
    e_seen = False

    s = s.strip()

    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'):
            if not dot_seen and not e_seen:
                num1_seen = True
            if dot_seen and not e_seen:
                num2_seen = True
            if e_seen:
                num3_seen = True
        elif s[i] == '.':
            if dot_seen or e_seen:
                return False
            dot_seen = True
        elif s[i] == 'e':
            if e_seen:
                return False
            e_seen = True
        elif s[i] == '+' or s[i] == '-':
            if i > 0 and s[i-1] != ' ' and s[i-1] != 'e':
                return False
        else:
            return False
    # 2) e & num3 should exist at the same time
    return (num1_seen or num2_seen) and not (e_seen ^ num3_seen)
