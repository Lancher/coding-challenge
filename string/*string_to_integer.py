# LEETCODE@ 8. String to Integer (atoi)
#
# --END--


def myAtoi(str):
    seq_seen = False
    seq = 0
    sign_seen = False
    sign = 1
    for i in range(len(str)):
        if ord('0') <= ord(str[i]) <= ord('9'):
            seq = seq * 10 + int(str[i])
            seq_seen = sign_seen = True
        elif str[i] == '+' or str[i] == '-':
            if sign_seen or seq_seen:
                return 0
            sign_seen = True
            sign = 1 if str[i] == '+' else -1
        # 1) +123 3 should be 123
        elif str[i] == ' ':
            if seq_seen:
                break
            if sign_seen and not seq_seen:
                return 0
        # 2) +123@ should be 123
        else:
            if seq_seen:
                break
            else:
                return 0
    if seq * sign > 0x7fffffff:
        return 0x7fffffff
    if seq * sign < -0x80000000:
        return -0x80000000
    return seq * sign
