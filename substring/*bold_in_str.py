# LEETCODE@ 616. Add Bold Tag in String
#
# 1. Use KMP to find all occurrences.
#
# 2.
#
# --END--


def kmp(pattern, string):
    # build array which prefix is also suffix.
    # prefix is the length of characters prefix matches suffix
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j

    # indexes of occurrence
    res = []
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = prefix[j - 1]
        if string[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i - len(pattern) + 1)
            j = prefix[j - 1]
    return res


def addBoldTag(self, s, tags):
    # initialization
    n = len(s)
    bold = [0] * (n + 1)

    # use kmp to find all occurrences for each sub strings
    for sub_s in tags:
        occurs = kmp(sub_s, s)
        for idx in occurs:
            if idx + len(sub_s) < n + 1:
                bold[idx] += 1
                bold[idx + len(sub_s)] -= 1

    # walk through the bold array
    pairs = []
    pre_cnt = cnt = 0
    for i in range(n + 1):
        pre_cnt = cnt
        cnt += bold[i]
        if pre_cnt == 0 and cnt == 0:
            continue
        elif 0 < pre_cnt and 0 < cnt:
            continue
        elif pre_cnt == 0 and 0 < cnt:
            pairs.append([i, None])
        else:
            pairs[-1][1] = i

    # build the string
    pairs = [[0, 0]] + pairs
    res = ''
    for i in range(1, len(pairs)):
        res += s[pairs[i - 1][1]:pairs[i][0]]
        print(s[pairs[i][0]:pairs[i][1]])
        res += '<b>' + s[pairs[i][0]:pairs[i][1]] + '</b>'
    res += s[pairs[-1][1]:n + 1]
    return res
