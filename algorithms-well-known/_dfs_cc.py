# 1. Check if v connected to w in connected on O(1) constant time.
#
# 2. Union Find can not find in constant time.
#
# 3. Use DFS and assign IDs.
#
#   0 --- 1           7 --- 8
#   |
#   --- 2
#   |
#   --- 5 --- 4 --- 3             <= we got two group in this graph
#   |        /
#   --- 6 --/
#
#
# --END--


def cc(g):
    cc_id = [-1] * len(g)
    parent = [-1] * len(g)
    visited = [0] * len(g)

    def _dfs(u, i):
        if not visited[u]:
            # update state here
            visited[u] = 1
            cc_id[u] = i
            for v in g[u]:
                # parent is specially so set here
                parent[v] = u
                _dfs(v, i)

    # id can be the same as u
    for u in range(len(g)):
        _dfs(u, u)


# this is undirected graph
g = {
    0: [1, 2, 5, 6],
    1: [0],
    2: [0],
    3: [4],
    4: [3, 5, 6],
    5: [0, 4],
    6: [0, 4],
    7: [8],
    8: [7]
}
cc(g)
