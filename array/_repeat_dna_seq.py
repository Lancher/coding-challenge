# LEETCODE@ 187. Repeated DNA Sequences
#
# --END--


def findRepeatedDnaSequences(self, s):
    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # the answer did not contain duplicate
    res = set()
    st = set()
    sm = 0
    for i in range(len(s)):
        sm <<= 2
        sm += d[s[i]]
        sm &= 0x000fffff

        if 9 <= i:
            if sm in st:
                res.add(s[i - 9:i + 1])
            else:
                st.add(sm)
    return list(res)
