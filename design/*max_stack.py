


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.max_stack.append(x)
        else:
            if x <= self.max_stack[-1]:
                self.max_stack.append(self.max_stack[-1])
            else:
                self.max_stack.append(x)
            self.stack.append(x)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1]

    def popMax(self):
        # use tmp stack to store tmps
        tmp_stack = []
        while self.stack[-1] != self.max_stack[-1]:
            tmp_stack.append(self.stack[-1])
            self.stack.pop()
            self.max_stack.pop()

        # pop the target
        self.stack.pop()
        res = self.max_stack.pop()

        # push tmp
        while tmp_stack:
            val = tmp_stack.pop()
            self.push(val)

        return res
