# LEETCODE@ 151. Reverse Words in a String
#
# --END--


def reverse_words_1(s):
    return " ".join(s.strip().split()[::-1])


# LEETCODE@ 186. Reverse Words in a String II
#
# --END--


def reverse_words_2(str):
    s = str
    s.reverse()
    i = 0
    for j in range(len(s)):
        if s[j] == " ":
            s[i:j] = s[i:j][::-1]
            i = j + 1
    s[i:len(s)] = s[i:len(s)][::-1]


# LEETCODE@ 557. Reverse Words in a String III
#
# --END--


def reverse_words_3(s):
    s = list(s)
    i = 0
    for j in range(len(s)):
        if s[j] == ' ':
            s[i:j] = s[i:j][::-1]
            i = j + 1
    s[i:len(s)] = s[i:len(s)][::-1]
    return ''.join(s)
