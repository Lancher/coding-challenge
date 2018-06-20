# LEETCODE@ 500. Keyboard Row
#
# --END--


def find_words(words):
    strings = ['QWERTYUIOPqwertyuiop', 'ASDFGHJKLasdfghjkl', 'ZXCVBNMzxcvbnm']
    d = {}
    for i in range(len(strings)):
        for c in strings[i]:
            d[c] = i

    res = []
    for word in words:
        for i in range(len(word)):
            if d[word[0]] != d[word[i]]:
                break
        else:
            res.append(word)
    return res
