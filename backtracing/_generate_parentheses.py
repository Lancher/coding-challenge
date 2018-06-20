# LEETCODE@ 22. Generate Parentheses
#
# --END--


def generateParenthesis(self, n):
    res = []
    self.helper(n, n, '', res)
    return res


def helper(self, left, right, s, res):
    if left == 0 and right == 0:
        res.append(s)
    else:
        if left:
            self.helper(left - 1, right, s + '(', res)
        if right and left < right:
            self.helper(left, right - 1, s + ')', res)