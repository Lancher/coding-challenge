# LEETCODE@ 9. Palindrome Number
#
# --END--


def is_palindrome(x):
    if x < 0 or x != 0 and x % 10 == 0:
        return False
    y = 0
    while x > y:
        y = y * 10 + x % 10
        x /= 10
    return x == y or x == y / 10
