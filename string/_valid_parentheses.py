# LEETCODE@ 20. Valid Parentheses
#
# --END--


def isValid(s):
    d = {')': '(', '}': '{', ']': '['}
    stack = []
    for i in range(len(s)):
        if s[i] in d:
            if not stack or stack[-1] != d[s[i]]:
                return False
            stack.pop()
        else:
            stack.append(s[i])
    return not bool(stack)
