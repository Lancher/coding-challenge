

# LEETCODE@ 777. Swap Adjacent in LR String
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL".
def canTransform(self, start, end):
    if len(start) != len(end):
        return False

    i, j = 0, 0

    s = []
    for i in range(len(start)):
        if start[i] != 'X':
            s.append(start[i])
    e = []
    for i in range(len(end)):
        if end[i] != 'X':
            e.append(end[i])
    if s != e:
        return False

    r_cnt = 0
    for i in range(len(start) - 1, -1, -1):
        if end[i] == 'R':
            r_cnt += 1
        if start[i] == 'R':
            if r_cnt == 0:
                return False
            else:
                r_cnt -= 1
    l_cnt = 0
    for i in range(len(start)):
        if end[i] == 'L':
            l_cnt += 1
        if start[i] == 'L':
            if l_cnt == 0:
                return False
            else:
                l_cnt -= 1
    return True
