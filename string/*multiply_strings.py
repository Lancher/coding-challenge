# LEETCODE@ 43. Multiply Strings
#
# --END--


def multiply(self, num1, num2):
    ans = [0] * (len(num1) + len(num2))

    # 1) 99 x 99
    #
    #     01 <= index
    #
    #     99
    #  x  99
    # ------
    #   xxxx
    #
    #   0123 <= index

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            k = i + j + 1
            tmp = int(num1[i]) * int(num2[j]) + ans[k]
            ans[k] = tmp % 10
            ans[k - 1] += tmp / 10
    ans = ''.join([str(i) for i in ans])
    ans = ans.lstrip('0')
    if ans:
        return ans
    else:
        return '0'
