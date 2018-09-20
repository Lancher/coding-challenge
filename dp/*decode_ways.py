# LEETCODE@ 91. Decode Ways
#
# 1) Build dp array.
#
# 2) What is each dp[] entry meaning.
#
# 3) Find the formulation of last item.
#
# 4) Set the dp[0].
#
# --END--


def numDecodings(self, s):
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        # one digit
        if 1 <= int(s[i]) <= 9:
            dp[i + 1] += dp[i]

        # two digits
        if 1 <= i and s[i - 1] != '0' and 1 <= int(s[i - 1:i + 1]) <= 26:
            dp[i + 1] += dp[i - 1]

    return dp[n]


# LEETCODE@ 639. Decode Ways II
#
# --END--


def numDecodings(self, s):
    # decode string start from '0' should return 0
    if s[0] == '0':
        return 0

    mod = 10 ** 9 + 7
    n = len(s)

    #    -1, 0, 1
    pre_pre = 1
    pre = 9 if s[0] == '*' else 1

    for i in range(1, n):
        cur = 0
        if s[i - 1] == '*' and s[i] == '*':
            # two chars as a whole
            cur += pre_pre * 15
            # two chars are seperate
            cur += pre * 9
        elif s[i - 1] == '*' and s[i] != '*':
            # two chars as a whole
            if int(s[i]) <= 6:
                cur += pre_pre * 2  # 1X, 2X
            else:
                cur += pre_pre
                # two chars are seperate
            if s[i] == '0':
                pass
            else:
                cur += pre
        elif s[i - 1] != '*' and s[i] == '*':
            # two chars as a whole (1X, 2X)
            if s[i - 1] == '1':
                cur += pre_pre * 9  # 11 ~ 19
            elif s[i - 1] == '2':
                cur += pre_pre * 6  # 21 ~ 16
            else:
                pass
            # two chars are seperate
            cur += pre * 9
        else:
            # two chars as a whole
            if s[i - 1] == '0':
                pass
            elif 10 <= int(s[i - 1:i + 1]) <= 26:
                cur += pre_pre
            else:
                pass
            # two chars are seperate
            if s[i] == '0':
                pass
            else:
                cur += pre
        pre_pre, pre = pre % mod, cur % mod

    return pre
