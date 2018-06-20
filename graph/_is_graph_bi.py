# LEETCODE@ 785. Is Graph Bipartite?
#
# 1. Set the two color and 0 is for unvisited:
#
#   [1] --> [2] --> [1]
#      \            ^
#       \ --> [2]--/
#
# 2. If it happen isolated graph, we only have to check each graph is Bipartite.
#
# --END--


def isBipartite(self, graph):
    color = [0] * len(graph)

    #  check i and adjacent j
    def dfs(i):
        for j in graph[i]:
            if color[j] == 0:
                color[j] = 1 if color[i] == 2 else 2
                if not dfs(j):
                    return False
            else:
                if color[i] == color[j]:
                    return False
        return True

    # check the isolated graph
    for i in range(len(graph)):
        if color[i] == 0:
            color[i] = 1
            if not dfs(i):
                return False

    return True
