# How to detect circle?
#
# 1) In directed graph, we use colors as flag to detect circle.
#
#   http://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/
#
# 2) In udirected graph, we can use DFS or Union-Find.
#
#   https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
#   https://www.geeksforgeeks.org/union-find/
#
# --END--


# directed graph
def detect_circle_dg(g):
    # 0 white
    # 1 grey
    # 2 black
    vst = [0] * len(g)

    def dfs(u):
        # unvisited
        if vst[u] == 0:
            vst[u] = 1
            for v in g[u]:
                if dfs(v):
                    return True
            vst[u] = 2
        # currently visiting
        elif vst[u] == 1:
            return True
        # already visited
        else:
            return False

    for u in g:
        if dfs(u):
            return True
    return False


#   0 --> 1 --> 3
#   | \
#   --> 2
g = {
    0: [1, 2],
    1: [3],
    2: [0],
    3: []  # node 3 should also be add to the graph
}
print(detect_circle_dg(g))


def detect_circle_udg(g):
    vst = [0] * len(g)

    def dfs(u, parent):
        vst[u] = 1
        for v in g[u]:
            if vst[v] == 0:
                if dfs(v, u):
                    return True
            # avoid go back
			#
            # v/parent  u
            #  0 ------ 1
            #
            # node 1 may go back to node 0
            elif v != parent:
                print(v, u, parent)
                return True

    # check if already visited first.
    for u in g:
        if vst[u] == 0:
            if dfs(u, -1):
                return True
    return False


#   0 ----- 1 ---- 3
#   |       \     /
#   |        \   /
#   |          4
#   --- 2
g = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1, 4],
    4: [1, 3]
}
print(detect_circle_udg(g))
