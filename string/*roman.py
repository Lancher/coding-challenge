# LEETCODE@ 13. Roman to Integer
#
# 1) "XXVII" We start from right to left.
#
# --END--


def roman_to_int( s):
    if not s:
        return 0
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = d[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        if d[s[i]] < d[s[i + 1]]:
            res -= d[s[i]]
        else:
            res += d[s[i]]
    return res


# LEETCODE@ 12. Integer to Roman
#
# 1) from int to Roman, we build the full table to handle the number.
#
# ---END--

def int_to_roman(num):
    m = ['', 'M', 'MM', 'MMM']
    c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    return m[num/1000] + c[num%1000/100] + x[num%100/10] + i[num%10]
