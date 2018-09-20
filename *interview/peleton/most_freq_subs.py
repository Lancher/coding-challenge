from collections import defaultdict


def feq(s, mn, mx, mx_u):
    cnt = defaultdict(int)
    n = len(s)

    for i in range(n):

        dist_cnt = set()
        for j in range(i, n):
            if j - i < mn:
                dist_cnt.add([s[j]])
                j += 1
            elif mn <= j - i <= mx and len(dist_cnt) <= mx_u:



