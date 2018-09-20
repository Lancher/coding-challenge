import random
import time


def intel_substring1(chars, s, k):
    # initialization
    n = len(s)
    i, j = 0, 0
    cnt_k = 0

    # max length
    res = 0

    for i in range(n):
        # j goes to right as much as possible
        while j < n:
            if chars[ord(s[j])-ord('a')] == 0:
                if cnt_k < k:
                    cnt_k += 1
                    j += 1
                elif cnt_k == k:
                    break
            else:
                j += 1

        # update max length
        res = max(res, j - i)

        # decrease cnt_k if possible
        if chars[ord(s[i]) - ord('a')] == 0:
            cnt_k -= 1

    return res


chars = [1] * 26
chars[1] = 0
chars[3] = 0

s = 'abcde'
s = ''.join([chr(ord('a') + random.randint(0, 25)) for _ in range(100000)])
print(s)

print(intel_substring1(chars, 'abcde', 1))
print(intel_substring1(chars, 'abcde', 0))

st = time.time()
print(intel_substring1(chars, s, 30))
end = time.time()
print(end - st)

