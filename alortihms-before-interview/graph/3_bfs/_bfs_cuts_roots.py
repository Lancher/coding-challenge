"""
We have second variation for BFS.

1. We need to have one additonal graph for tacking how many
   incoming nodes for each node.

--END--
"""

import queue


def bfs(g, rev_g):
    # init
    n = len(g)
    visited = set()

    q = queue.Queue()

    # add nodes with 0 incoming nodes
    for i in range(n):
        if len(rev_g[i]) == 0:
            q.put(i)
            visited.add(i)

    # consume until all node visited
    while not q.empty():
        sz = q.qsize()
        for _ in range(sz):
            u = q.get()
            for v in g[u]:
                if v not in visited:
                    # delete incoming node u in rev_g
                    rev_g[v].remove(u)
                    # seef if this become our next node
                    if len(rev_g[v]) == 0:
                        visited.add(v)
                        q.put(v)

    # if not equal, then there is cycle
    assert len(visited) == n

g = {0: [1, 2, 3, 6], 1: [], 2: [], 3: [4], 4: [5], 5: [], 6: [4], 7: []}
rev_g = {0: [], 1: [0], 2: [0], 3: [0], 4: [3, 6], 5: [4], 6: [0], 7: []}

bfs(g, rev_g)
