# LEETCODE@ 788. Rotated Digits
#
# --END--


def rotatedDigits(self, N):
    d = {
        '0': '0',
        '1': '1',
        '2': '5',
        '5': '2',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    res = 0
    for i in range(1, N + 1):
        s = str(i)
        tmp = ''
        for j in range(len(s)):
            if s[j] in d:
                tmp += d[s[j]]
            else:
                break
        if len(tmp) == len(s) and tmp != s:
            res += 1
    return res
