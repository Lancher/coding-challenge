# 1. princeton algorithm
#
# 2. https://www.youtube.com/watch?v=GTJr8OvyEVQ
#
# 3. Example:
#
#
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
            j = prefix[j-1]
        if string[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i)
            j = prefix[j - 1]
    return res


print(kmp('a', 'aaaaaaaa'))  # [0, 1, 2, 3, 4, 5, 6, 7]
