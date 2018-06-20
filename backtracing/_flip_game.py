# LEETCODE@ 293. Flip Game
#
# 1. Do not need Backtracing.
#
# --END--


def generatePossibleNextMoves(self, s):
    res = []
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] == '+':
            res.append(s[:i] + '--' + s[i + 2:])
    return res


# LEETCODE@ 294. Flip Game II
#
# 1. There are a lot of possibility, and if one of combination can win , then win.
#
# --END


def canWin(self, s):
    l = list(s)
    return self.backtracing(l)


def backtracing(self, l):
    for i in range(len(l) - 1):
        if l[i] == '+' and l[i + 1] == '+':
            l[i] = l[i + 1] = '-'
            win = not self.backtracing(l)
            l[i] = l[i + 1] = '+'
            if win:
                return True
    return False
