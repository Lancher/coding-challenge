# LEETCODE@ 50. Pow(x, n)
#
# --END--


def my_pow(x, n):
    if n < 0:
        x = 1 / x
    n = abs(n)

    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 1:
        tmp = my_pow(x, n/ 2)
        return tmp * tmp * x
    else:
        tmp = my_pow(x, n / 2)
        return tmp * tmp
