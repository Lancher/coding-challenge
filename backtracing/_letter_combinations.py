# LEETCODE@ 17. Letter Combinations of a Phone Number
#
# --END--


def letterCombinations(self, digits):
    if not digits:
        return []
    table = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    res = ['']
    for i in range(len(digits)):
        tmp = list(table[digits[i]])
        res = [x + y for y in tmp for x in res]
    return res
