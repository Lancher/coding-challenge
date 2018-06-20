# LEETCODE@ 50. Pow(x, n)
#
# --END--


def myPow(self, x, n):
    if n < 0:
        x = 1 / x
        n = - n

    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        tmp = myPow(x, int(n / 2))
        return tmp * tmp
    else:
        tmp = myPow(x, int(n / 2))
        return tmp * tmp * x
