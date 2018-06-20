

def dfs(g):
    parent = [-1] * len(g)
    visited = [0] * len(g)

    def _dfs(u):
        # check if the node already visited
        if not visited[u]:
            # visited is set right after check if visited
            visited[u] = 1
            for v in g[u]:
                # set parent, run inner dfs
                parent[v] = u
                _dfs(v)

    # run all nodes
    for u in range(len(g)):
        _dfs(u)

    print(parent)


g = {0: [1, 2, 3, 6], 1: [], 2: [], 3: [4], 4: [5], 5: [], 6: [4], 7: []}
dfs(g)
