"""
1. If there is a repeated pattern in the string.

2. Concatenate
  s = "abcabc"
  ss = "abcabc" + "abcabc"

3. Find the s in s[1:-1].

4. Check the explaination on Good Notes Q.459

--END--
"""


def find_repeated_pattern(s):
    ss = s + s
    sub_end = ss[1:-1].find(s)

    return sub_end + 1


s1 = 'abcabc'
end = find_repeated_pattern(s1)
print(s1[:end])

s2 = 'abcabcab'
end = find_repeated_pattern(s2)
print(s2[:end])
