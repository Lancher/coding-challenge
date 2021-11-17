# 1. import queue.Queue
#
#
# --END--


import queue


def bfs(g):
    parent = [-1] * len(g)
    visited = [0] * len(g)

    q = queue.Queue()

    # add Node 0 as source
    q.put(0)
    visited[0] = -1

    # consume until all node visited
    while not q.empty():
        sz = q.qsize()
        for _ in range(sz):
            u = q.get()
            for v in g[u]:
                if not visited[v]:
                    # visited set 1, set the parent, put to queue
                    visited[v] = 1
                    parent[v] = u
                    q.put(v)


g = {0: [1, 2, 3, 6], 1: [], 2: [], 3: [4], 4: [5], 5: [], 6: [4], 7: []}
bfs(g)
