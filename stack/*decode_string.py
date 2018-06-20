# LEETCODE@ 394. Decode String
#
# 1) one type per stack, so use one
#
# --END--


def decodeString(self, s):
    count = ''
    res = ''
    count_stack = []
    res_stack = []

    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'):
            count += s[i]
        elif s[i] == '[':
            count_stack.append(int(count) if count else 0)
            res_stack.append(res)
            count = ''
            res = ''

        # 3[3[a]bb2[cc]]
        # when [cc] close, we merge the previous one which is already complete
        elif s[i] == ']':
            res = res_stack.pop() + res * count_stack.pop()
        else:
            res += s[i]
    return res
