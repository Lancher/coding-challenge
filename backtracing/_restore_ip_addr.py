# LEETCODE@ 93. Restore IP Addresses
#
# 1. Since there are some constraints in each part, we just make sure we can get to the length
#
# --END--


def restoreIpAddresses(self, s):
    res = []

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                for l in range(1, 4):
                    if i + j + k + l == len(s):
                        a, b, c, d = int(s[:i]), int(s[i:i + j]), int(s[i + j:i + j + k]), int(s[i + j + k:len(s)])
                        if a <= 255 and b <= 255 and c <= 255 and d <= 255:
                            ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
                            if len(ip) == len(s) + 3:
                                res.append(ip)
    return res
