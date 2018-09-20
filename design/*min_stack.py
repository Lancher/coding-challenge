# LEETCODE@ 155. Min Stack
#
# 1. Solution 1: we push (current value, current minimum)
#
# 2. Solution 2: we push the subtraction of current value and min value.
#
#    [3, 1, 2, 4, 0]
#
#   1) Push 3
#
#   stack [0]
#   min: 3
#
#   2) Push 1, we encounter negative value (1 - 3), so we know minimum is changed.
#
#   stack [0, -2]
#   min: 1
#
#   cur - cur_min = -2
#   when -2 < 0, we know that cur = self.min
#
# --END--


class MinStack(object):
    def __init__(self):
        self.min = 0
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top < 0:
                self.min -= top

    def top(self):
        top = self.stack[-1]
        if top >= 0:
            return top + self.min
        else:
            return self.min

    def getMin(self):
        return self.min
