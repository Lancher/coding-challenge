# How to build minimum spanning tree with Prim's Algorithm
#
# 1) Pick any node as a starting point.
#
# 2) Use heapq ot pick smallest edge
#
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
import collections
import heapq


class Node:
    def __init__(self, p, w):
        self.p = p
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


def mst(n, edges):
    # init
    cost = 0
    hq = []

    # build a graph
    g = collections.defaultdict(dict)
    for p1, p2, w in edges:
        g[p1][p2] = w
        g[p2][p1] = w

    # pick random node 0 into heapq
    heapq.heappush(hq, Node(0, 0))
    vst = set()

    # pick smallest edge at a time
    while hq:
        node = heapq.heappop(hq)

        # node is already visited
        if node.p in vst:
            continue

        cost += node.w
        vst.add(node.p)

        if len(vst) == n:
            break

        for nxt_node, nxt_w in g[node.p].items():
            heapq.heappush(hq, Node(nxt_node, nxt_w))


    # minimum cost is 7
    assert cost == 7


edges = [[0, 1, 1], [1, 2, 2], [2, 3, 5], [3, 0, 4], [0, 2, 3]]
mst(4, edges)
