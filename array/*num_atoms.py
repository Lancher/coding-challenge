# LEETCODE@ 726. Number of Atoms
#
# --END--


def countOfAtoms(self, formula):
    n = len(formula)
    cur = 1
    num = ''
    element = ''
    stack = []
    counter = {}

    for i in range(n - 1, -1, -1):
        # lower
        if 0 <= ord(formula[i]) - ord('a') < 26:
            element = formula[i] + element
        # upper
        elif 0 <= ord(formula[i]) - ord('A') < 26:
            mul = int(num) if num else 1
            num = ''
            element = formula[i] + element
            if element in counter:
                counter[element] += cur * mul
            else:
                counter[element] = cur * mul
            element = ''
        # number
        elif 0 <= ord(formula[i]) - ord('0') < 10:
            num = formula[i] + num
        # open bracket
        elif formula[i] == '(':
            div = stack.pop()
            cur = int(cur / div)
            # close bracket
        elif formula[i] == ')':
            stack.append(int(num))
            cur *= int(num)
            num = ''
        else:
            print('not gonna happened')

    res = ''
    for element in sorted(counter.keys()):
        res += element
        res += str(counter[element]) if counter[element] > 1 else ''
    return res