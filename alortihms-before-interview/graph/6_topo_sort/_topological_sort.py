# 1. DFS so the cycles is not allowed, but we can find the circle by
#    coloring the nodes.
#
# 2. length of graph is the number of nodes
#
# 3. Example:
#
#   0 --> 2 --> 3 --> 4
#         ^
#   1 --- |
#
#   Node 4 and his children will be done and append to array
#   Node 3 and his children will be done and append to array
#   Node 2 and his children will be done and append to array
#   Node 0 and his children will be done and append to array
#   Node 1 and his children will be done and append to array
#   [4, 3, 2, 0, 1] reverse [1, 0, 2, 3, 4]
#
# 4. TODO: another way to do the topological sort is LeetCode 444.
#
# --END--


def topological_sort_dfs(g):
    visited = [0] * len(g)
    res = []

    # inner function can only reference the mutable outer variables
    def dfs(u):
        if not visited[u]:
            visited[u] = 1
            for v in g[u]:
                dfs(v)

            # when all children are done, we append current node
            res.append(u)

    # run DFS
    for u in range(len(g)):
        dfs(u)

    # return reverse order
    return res[::-1]


g = {0: [2], 1: [2], 2: [3], 3: [4], 4: []}
print(topological_sort_dfs(g))

# 1. BFS
#
# 2. length of graph is the number of nodes
#
# 3. Example:
#
#   0 --> 2 --> 3 --> 4
#         ^
#   1 --- |
#
#   Node 0 and 1 will be added into the queue which is defined as non-parent
#   nodes queue.
#
# --END--

def topological_sort_bfs(g):
    # init
    visited = [0] * len(g)
    res = []

    # build parent
    parent = {i: set() for i in range(len(g))}
    for p in g:
        for c in g[p]:
            parent[c].add(p)

    # queue with
    q = [c for c in parent if len(parent[c] == 0)]
    for node in q:
        visited[node] = 1

    # Run BFS until no elements in the queue
    while q:
        nxt_q = []
        for node in q:
            res.append(node)
            for nxt_node in q[node]:
                # skip visited nodes
                if visited[nxt_node]:
                    continue
                # add node to queue
                parent[nxt_node].remove(node)
                if len(parent[nxt_node]) == 0:
                    nxt_q.append(nxt_node)
                    visited[nxt_node] = 1
    return res

g = {0: set([2]), 1: set([2]), 2: set([3]), 3: set([4]), 4: set()}
print(topological_sort_bfs(g))
