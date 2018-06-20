# LEETCODE@ 684. Redundant Connection
#
# 1) Union Find is a perfect technique to slove all kinds of problems.
#
# 2) N node with N edges, if there is a cycle, there must be only one edge to be deleted.
#
# --END--


class Union:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.size = [1] * n

    def root(self, p):
        while p != self.arr[p]:
            self.arr[p] = self.arr[self.arr[p]]
            p = self.arr[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p = self.root(p)
        q = self.root(q)
        if p != q:
            if self.size[p] < self.size[q]:
                self.arr[p] = q
                self.size[q] += self.size[p]
            else:
                self.arr[q] = p
                self.size[p] += self.size[q]


class Solution:
    def findRedundantConnection(self, edges):
        un = Union(len(edges) + 1)
        for e in edges:
            if un.connected(e[0], e[1]):
                return e
            else:
                un.union(e[0], e[1])