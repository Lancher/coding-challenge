# LEETCODE@ 38. Count and Say
#
# 1) Example:
#
#   1
#   11
#   21
#   1211
#   111221
#
# --END--


def count_and_say(n):
    res = '1'

    for i in range(1, n):
        tmp = ''
        count = 1
        for j in range(1, len(res)):
            if res[j] == res[j - 1]:
                count += 1
            else:
                tmp += str(count) + str(res[j - 1])
                count = 1
        tmp += str(count) + str(res[-1])
        res = tmp
    return res
