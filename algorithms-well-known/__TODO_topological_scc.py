# Strongly-Connected Components is that ff the vertex v has a directed path to w and so does the vertex x.
# Steps:
# 1) Get Topological sort order, and then run dfs in reversed graph.


class DiaGraph:

    def __init__(self):
        self.e = 0
        self.vers = {}

    def add_edge(self, v, w):
        if v not in self.vers:
            self.vers[v] = []
        self.vers[v].append(w)
        self.e += 1

    def reverse(self):
        g = DiaGraph()
        for v in self.vers.keys():
            for w in self.vers[v]:
                g.add_edge(w, v)
        return g


class SCC:
    def __init__(self, g):
        self.g = g
        self.rev_g = g.reverse()
        self.visited = {}

    def _dfs(self, g, v, scc_id):
        if v in g.vers:
            for w in g.vers[v]:
                if w not in self.visited:
                    # set id
                    self.visited[w] = scc_id
                    self._dfs(g, w, scc_id)

    def dfs(self):
        s = TopologicalSort(self.g)
        s.dfs()

        scc_id = 0
        for v in s.res:
            if v not in self.visited:
                self.visited[v] = scc_id
                self._dfs(self.rev_g, v, scc_id)
                scc_id += 1


g = DiaGraph()
g.add_edge(4, 2)
g.add_edge(2, 3)
g.add_edge(3, 2)
g.add_edge(6, 0)
g.add_edge(0, 1)
g.add_edge(2, 0)
g.add_edge(11, 12)
g.add_edge(12, 9)
g.add_edge(9, 10)
g.add_edge(9, 11)
g.add_edge(7, 9)
g.add_edge(10, 12)
g.add_edge(11, 4)
g.add_edge(4, 3)
g.add_edge(3, 5)
g.add_edge(6, 8)
g.add_edge(8, 6)
g.add_edge(5, 4)
g.add_edge(0, 5)
g.add_edge(6, 4)
g.add_edge(6, 9)
g.add_edge(7, 6)


s = SCC(g)
s.dfs()
print(s.visited)
