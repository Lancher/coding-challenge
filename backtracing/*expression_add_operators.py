# LEETCODE@ 282. Expression Add Operators
#
# Given a string that contains only digits 0-9 and a target value
def addOperators(self, num, target):
    result = []
    self.helper(num, target, result, 0, '', 0, 0)
    return result


def helper(self, num, target, result, i, s, val, mul):
    if i >= len(num):
        if val == target:
            result.append(s)
    else:
        for j in range(i + 1, len(num) + 1):
            cur = num[i:j]
            if len(cur) != 1 and cur.startswith('0'):
                continue
            cur_val = int(cur)
            # `5*2+1`, the first val does not have pre operator.
            if i == 0:
                self.helper(num, target, result, j, s + cur, cur_val, cur_val)
            else:
                self.helper(num, target, result, j, s + '+' + cur, val + cur_val, cur_val)
                self.helper(num, target, result, j, s + '-' + cur, val - cur_val, -cur_val)
                self.helper(num, target, result, j, s + '*' + cur, val - mul + mul * cur_val, mul * cur_val)


def addOperators(self, num, target):
    l, res = [], []
    self.backtracing(num, target, 0, 0, 0, l, res)
    return res


def backtracing(self, num, target, i, sm, pre_val, l, res):
    if len(num) <= i:
        if sm == target:
            res.append(''.join(l))
    else:
        for j in range(i, len(num)):
            if i < j and num[i] == '0':
                continue
            val = int(num[i:j + 1])

            if i == 0:
                l.append(str(val))
                self.backtracing(num, target, j + 1, sm + val, val, l, res)
                l.pop()
            else:
                l.append('+')
                l.append(str(val))
                self.backtracing(num, target, j + 1, sm + val, val, l, res)
                l.pop()
                l.pop()

                l.append('-')
                l.append(str(val))
                self.backtracing(num, target, j + 1, sm - val, -val, l, res)
                l.pop()
                l.pop()

                l.append('*')
                l.append(str(val))
                self.backtracing(num, target, j + 1, sm - pre_val + pre_val * val, pre_val * val, l, res)
                l.pop()
                l.pop()