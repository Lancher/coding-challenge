# LEETCODE@ 6. ZigZag Conversion
# 
# ---END--


def zigzag(s, numRows):
    if numRows < 2:
        return s
    res = ''
    gap = (numRows - 1) * 2
    for i in range(numRows):
        if i == 0 or i == numRows - 1:
            j = i
            steps = gap
            while j < len(s):
                res += s[j]
                j += steps
        else:
            steps = gap - i * 2
            j = i
            while j < len(s):
                res += s[j]
                j += steps
                steps = gap - steps
    return res
