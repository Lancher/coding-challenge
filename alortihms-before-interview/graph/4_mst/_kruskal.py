# How to build minimum spanning tree with Kruskal Algorithms?
#
# 1) Create a Union Find class.
#
# 2) Put all edges into heapq
#
# 3. Pick one at a time to make sure two vertexes are not connected.
#
#  p0     1    p1
#     *------*
#     |\     |
#     | \ 3  | 2
#     |  \   |
#   4 |   \  |
#     |    \ |
#     |     \|
#     *------*
#  p3    5     p2
#
#     minimum is 7 (4 + 1 + 2)
#
# --END--
import heapq
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.groups = n

    def root(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p, root_q = self.root(p), self.root(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
                self.size[root_q] += root_p
            else:
                self.parent[root_q] = root_p
                self.size[root_p] += root_q
            self.groups -= 1

class Node:
    def __init__(self, p1, p2, w):
        self.p1 = p1
        self.p2 = p2
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


def mst(n, edges):
    # init
    cost = 0
    hq = []
    un = UnionFind(n)

    # put all edges into heap
    for p1, p2, w in edges:
        hq.append(Node(p1, p2, w))
    heapq.heapify(hq)

    # pick smallest edge at a time
    while hq:
        node = heapq.heappop(hq)
        if not un.connected(node.p1, node.p2):
            un.union(node.p1, node.p2)
            cost += node.w
            if un.groups == 1:
                break

    # minimum cost is 7
    assert cost == 7


edges = [[0, 1, 1], [1, 2, 2], [2, 3, 5], [3, 0, 4], [0, 2, 3]]
mst(4, edges)
