"""
1. princeton algorithm

2. https://www.youtube.com/watch?v=GTJr8OvyEVQ

3. Example:

      0 1 2 3 4 5 6 7
      a b c d a b c a

      j i -> are not the same, so we keep j stay 0 and i move to index 2
      0 0

      j   i -> are not the same, so we keep j stay 0 and i move to index 3
      0 0 0

      j     i -> are not the same, so we keep j stay 0 and i move to index 4
      0 0 0 0

      j       i -> are the same, so we move j to 1, i to 5.
      0 0 0 0 1

        j       i -> are the same, so we move j to 2, i to 6.
      0 0 0 0 1 2

          j       i -> are the same, so we move j to 3, i to 7.
      0 0 0 0 1 2 3

            j       i -> are not the same, so we need to find the longest prefix in string[0:j]
      0 0 0 0 1 2 3 ?    since these two segements are the same. j = prefix[j-1]
      -----
              -----

--END--
"""


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
