# LEETCODE@ 202. Happy Number
#
# --END--


def is_happy(n):
    s = set()
    while n not in s:
        if n == 1:
            return True
        s.add(n)

        tmp = 0
        while n != 0:
            tmp += (n % 10) * (n % 10)
            n /= 10
        n = tmp
    return False
