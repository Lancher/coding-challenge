# LEETCODE@ 246. Strobogrammatic Number
#
# --END--


def isStrobogrammatic(self, num):
    i, j = 0, len(num) - 1
    while i <= j:
        if num[i] in ['0', '1', '8']:
            if num[j] != num[i]:
                return False
        elif num[i] == '6':
            if num[j] != '9':
                return False
        elif num[i] == '9':
            if num[j] != '6':
                return False
        else:
            return False
        i, j = i + 1, j - 1
    return True


# LEETCODE@ 247. Strobogrammatic Number II
#
# --END--


def findStrobogrammatic(self, n):
    result = []
    l = [''] * n
    pairs = [['0', '0'], ['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]
    singles = ['0', '1', '8']

    self.backtracing(result, l, pairs, singles, 0, n - 1)
    return result


def backtracing(self, result, l, pairs, singles, s, e):
    if s > e:
        result.append(''.join(l))
    else:
        if s == e:
            for single in singles:
                l[s] = single
                self.backtracing(result, l, pairs, singles, s + 1, e - 1)
        else:
            if s == 0:
                for pair in pairs[1:]:
                    l[s], l[e] = pair[0], pair[1]
                    self.backtracing(result, l, pairs, singles, s + 1, e - 1)
            else:
                for pair in pairs:
                    l[s], l[e] = pair[0], pair[1]
                    self.backtracing(result, l, pairs, singles, s + 1, e - 1)


# iterative method
def findStrobogrammatic(self, n):
    res = ['']
    if n % 2 == 1:
        res = ['0', '1', '8']
        n -= 1
    while n:
        tmp = []
        if n != 2:
            for s in res:
                tmp.append('0' + s + '0')
        for s in res:
            tmp.append('1' + s + '1')
        for s in res:
            tmp.append('8' + s + '8')
        for s in res:
            tmp.append('6' + s + '9')
        for s in res:
            tmp.append('9' + s + '6')
        n -= 2
        res = tmp
    return res


# LEETCODE@ 248. Strobogrammatic Number III
#
# --END--


def strobogrammaticInRange(self, low, high):
    # 1) find all the possibilities
    nums = []
    for i in range(len(low), len(high) + 1):
        nums += self.helper(i)
    res = 0
    # 2) count the
    for num in nums:
        if int(low) <= int(num) <= int(high):
            res += 1
    return res


def helper(self, n):
    res = ['']
    if n % 2 == 1:
        res = ['0', '1', '8']
        n -= 1
    while n:
        tmp = []
        if n != 2:
            for s in res:
                tmp.append('0' + s + '0')
        for s in res:
            tmp.append('1' + s + '1')
        for s in res:
            tmp.append('8' + s + '8')
        for s in res:
            tmp.append('6' + s + '9')
        for s in res:
            tmp.append('9' + s + '6')
        n -= 2
        res = tmp
    return res
