# LEECODE@ 133. Clone Graph
#
# --END--


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def cloneGraph(self, node):
    if node is None:
        return node
    # 1) `g` can be used for checking the node already be visited
    g = {}
    g[node] = UndirectedGraphNode(node.label)
    self.dfs(node, g)
    return g[node]


def dfs(self, node, g):
    # 2) `node` is already in the `g`
    for neigh in node.neighbors:
        if neigh in g:
            g[node].neighbors.append(g[neigh])
        else:
            g[neigh] = UndirectedGraphNode(neigh.label)
            g[node].neighbors.append(g[neigh])
            self.dfs(neigh, g)
