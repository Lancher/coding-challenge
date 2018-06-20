# The distTo[v] will not change because the topological order make sure that no edge pointing to v. The distTo[w]
# will decrease because the relax function.
# No cycle allowed because of Topological sort!!
# Use the vertices order in Topological Sort and relax each vertex w adjacent to v.


class TopologicalSortSP:

    def __init__(self, g):
        self.g = g
        self.dst = {}

    def topological_sort(self):
        res = []
        visited = set()
        for v in range(self.g.n):
            if v not in visited:
                self._dfs(v, visited, res)
        res = res[::-1]
        return res

    def _dfs(self, v, visited, res):
        visited.add(v)
        if v in self.g.vers:
            for e in self.g.vers[v]:
                if e[1] not in visited:
                    self._dfs(e[1], visited, res)
        res.append(v)

    def run(self):
        self.dst[0] = 0.0

        order = self.topological_sort()
        for v in order:
            if v in self.g.vers:
                for e in self.g.vers[v]:
                    if e[1] in self.dst:
                        if self.dst[v] + e[2] < self.dst[e[1]]:
                            self.dst[e[1]] = self.dst[v] + e[2]
                    else:
                        self.dst[e[1]] = self.dst[v] + e[2]
