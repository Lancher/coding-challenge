# LEETCODE@ 261. Graph Valid Tree
#
# 1. DFS
#
# 2. Union Find
#
# --END--


import collections


def validTree(self, n, edges):
    # two seperate tree is not allowed
    if len(edges) != n - 1:
        return False

    g = collections.defaultdict(list)
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])

    vst = [0] * n
    for i in range(n):
        if not vst[i]:
            if self.is_cycle(n, g, vst, -1, i):
                print(i)
                return False
    return True


def is_cycle(self, n, g, vst, par, i):
    vst[i] = 1
    for j in g[i]:
        if not vst[j]:
            if self.is_cycle(n, g, vst, i, j):
                return True
        else:
            if j != par:
                return True
    return False
