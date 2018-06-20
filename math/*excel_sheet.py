# LEETCODE@ 171. Excel Sheet Column Number
#
# --END--


def title_to_number(s):
    res = 0
    mul = 1
    for i in range(len(s) - 1, -1, -1):
        res += (ord(s[i]) - ord('A') + 1) * mul
        mul *= 26
    return res


# LEETCODE@ 168. Excel Sheet Column Title
#
# --END--


def convert_to_title(n):
    res = ''
    while n:
        n -= 1
        n, i = int(n / 26), n % 26
        res = chr(ord('A') + i) + res
    return res

