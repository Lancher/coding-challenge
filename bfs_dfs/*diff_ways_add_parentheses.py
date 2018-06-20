# LEETCODE@ 241. Different Ways to Add Parentheses
#
# --END--


def diffWaysToCompute(self, input):
    result = []
    for i in range(len(input)):
        if input[i] in ['+', '-', '*']:
            left = self.diffWaysToCompute(input[:i])
            right = self.diffWaysToCompute(input[i + 1:])
            for l in left:
                for r in right:
                    if input[i] == '+':
                        result.append(l + r)
                    if input[i] == '-':
                        result.append(l - r)
                    if input[i] == '*':
                        result.append(l * r)
    if not result:
        result.append(int(input))
    return result
