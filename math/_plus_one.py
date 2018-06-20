# LEETCODE@ 66. Plus One
#
# --END--


def plusOne(self, digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        carry += digits[i]
        digits[i] = carry % 10
        carry /= 10
    if carry:
        digits = [carry] + digits
    return digits
