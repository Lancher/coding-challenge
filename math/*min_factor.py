# LEETCODE@ 625. Minimum Factorization


def smallestFactorization(a):
    # If the number is less than 10, we just return the value.
    if a < 10:
        return a

    # We divide the number from 9 to 2.
    digits = []
    for i in range(9, 1, -1):
        while a % i == 0:
            digits.append(i)
            a = int(a / i)

    # The a must be 1.
    if not digits or a != 1:
        return 0

    # Return answer.
    digits = digits[::-1]
    digits = [str(d) for d in digits]
    res = int(''.join(digits))
    return 0 if res > 0x7fffffff else res
