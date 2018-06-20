# LEETCODE@ 150. Evaluate Reverse Polish Notation
#
# --END


def evalRPN(self, tokens):
    stack = []
    for t in tokens:
        if t in ['+', '-', '*']:
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(str(eval(val1 + t + val2)))
        elif t == '/':
            val2 = float(stack.pop())
            val1 = int(stack.pop())
            stack.append(str(int(val1 / val2)))
        else:
            stack.append(t)
    return int(stack[0])
