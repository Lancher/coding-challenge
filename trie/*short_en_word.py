# LEETCODE@ 820. Short Encoding of Words
#
# 1) Remove all the suffix in the words array.
#
# 2) Build a trie like and visit all the leaves
#
# --END--


def minimumLengthEncoding(self, words):
    st = set(words)

    for word in words:
        for i in range(1, len(word)):
            s = word[i:]
            if s in st:
                st.remove(s)

    res = sum([len(word) + 1 for word in st])
    return res


def minimumLengthEncoding(self, words):
    d = {}
    nodes = []
    st = set(words)
    # 1) build trie
    for word in st:
        cur = d
        for c in word[::-1]:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        # 2) append all possible leaves
        nodes.append([cur, len(word)])

    res = 0
    for node, cnt in nodes:
        if len(node) == 0:
            res += cnt + 1
    return res
