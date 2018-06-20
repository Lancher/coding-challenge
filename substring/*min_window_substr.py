# LEETCODE@ 76. Minimum Window Substring
#
# --END--


def minWindow(self, s, t):
    # 1) how many characters we still need
    missing = len(t)
    counter = [0] * 256

    # 2) < 0 means we still need this character
    for c in t:
        counter[ord(c)] -= 1

    m, n = -1, -1
    i, j = 0, 0
    while j < len(s):
        # 3) if we encounter < 0, it means we still need to fill the character
        if counter[ord(s[j])] < 0:
            missing -= 1
        counter[ord(s[j])] += 1

        # 4) if we counter > 0, it means it is a reduntant character, so we can remove it
        if missing == 0:
            while i < j and counter[ord(s[i])] > 0:
                counter[ord(s[i])] -= 1
                i += 1
            if m == -1 or j - i < n - m:
                m, n = i, j
        j += 1
    return s[m:n + 1]
