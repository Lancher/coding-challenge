

# LEETCODE@ 224. Basic Calculator
#
# Implement a basic calculator to evaluate a simple expression string.
def calculate(self, s):
    result = 0
    num = 0
    sign = 1
    stack = []

    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'):
            num = ord(s[i]) - ord('0') + num * 10
        elif s[i] == '-':
            result += sign * num
            num = 0
            sign = -1
        elif s[i] == '+':
            result += sign * num
            num = 0
            sign = 1
        elif s[i] == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            num = 0
            sign = 1
        elif s[i] == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
            sign = 1
    if num:
        result += sign * num
    return result


# LEETCODE 227. Basic Calculator II
#
# Implement a basic calculator to evaluate a simple expression string.
def calculate(self, s):
    stack = []
    num = 0
    sign = '+'

    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'):
            num = num * 10 + int(s[i])
        if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            else:
                pre_num = stack.pop()
                if pre_num < 0:
                    stack.append(-(abs(pre_num) / num))
                else:
                    stack.append(pre_num / num)
            sign = s[i]
            num = 0

    if len(stack):
        return sum(stack)
    else:
        return 0


# LEETCODE@ 772. Basic Calculator III


# LEETCODE@ 770. Basic Calculator IV


