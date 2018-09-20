import time


def gen_all_subseq(s, nxt_i, tmp, res):
    subseq = ''.join(tmp)
    if subseq:
        res.add(subseq)

    for i in range(nxt_i, len(s)):
        tmp.append(s[i])
        gen_all_subseq(s, i + 1, tmp, res)
        tmp.pop()


# testing
s = time.time()
res = set()
gen_all_subseq('aaaaaaaaaaaaaaaa', 0, [], res)
e = time.time()
print(e - s)

print(list(res))
