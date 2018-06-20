# LEETCODE@ 290. Word Pattern
#
# 1. When encounter pattern problem, using index is always the way out.
#
# --END--


def wordPattern(self, p, s):
    d1, d2 = {}, {}
    p, s = list(p), s.split(' ')
    if len(p) != len(s):
        return False

    # use two index to keep update indexes
    for i in range(len(p)):
        if d1.get(p[i]) == d2.get(s[i]):
            d1[p[i]] = d2[s[i]] = i
        else:
            return False

    return True


# LEETCODE@ 291. Word Pattern II
#
# Use the same concept in leetcode 290
#
# --END--


def wordPatternMatch(self, pattern, str):
    pat_d, s_d = {}, {}
    result = [False]
    self.backtracing(pat_d, pattern, 0, s_d, str, 0, result)
    return result[0]


def backtracing(self, pat_d, pat, pat_i, s_d, s, s_i, result):
    if result[0]:
        return
    if pat_i == len(pat) and s_i == len(s):
        result[0] = True
    elif pat_i == len(pat) or s_i == len(s):
        pass
    else:
        for j in range(s_i + 1, len(s) + 1):
            if pat[pat_i] in pat_d and s[s_i:j] in s_d:
                if pat_d[pat[pat_i]] == s_d[s[s_i:j]]:
                    self.backtracing(pat_d, pat, pat_i + 1, s_d, s, j, result)
            elif pat[pat_i] not in pat_d and s[s_i:j] not in s_d:
                pat_d[pat[pat_i]] = pat_i
                s_d[s[s_i:j]] = pat_i
                self.backtracing(pat_d, pat, pat_i + 1, s_d, s, j, result)
                pat_d.pop(pat[pat_i])
                s_d.pop(s[s_i:j])
