# LEETCODE@ 263. Ugly Number
#
# --END--


def is_ugly(num):
    # 1) 0 is an ugly number
    # 2) 1 is an ugly number
    if num <= 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1


# LEETCODE@ 264. Ugly Number II
#
# --END--


def nthUglyNumber(self, n):
    res = [1] * n
    i2, i3, i5 = 0, 0, 0

    for i in range(1, n):
        v2, v3, v5 = res[i2] * 2, res[i3] * 3, res[i5] * 5
        mn = min(v2, v3, v5)
        if mn == v2:
            i2 += 1
        if mn == v3:
            i3 += 1
        if mn == v5:
            i5 += 1
        res[i] = mn
    return res[n - 1]
