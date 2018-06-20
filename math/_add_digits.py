# LEETCODE@ 258. Add Digits
#
# 1) Digit Root Problem: https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
#
# --END--


def add_digits(num):
    while num > 9:
        s = 0
        while num:
            s += num % 10
            num /= 10
        num = s
    return num
