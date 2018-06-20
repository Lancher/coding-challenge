# Kruskals Algorithm
# Steps:
# 1) Sorted the edge(priority queue) and use Union-Find to avoid cycles.
# TODO the application, check princeton algorithm


class EdgeGraph:
    def __init__(self):
        self.vers = {}
        self.edges = []

    def add_edge(self, v, w, weight):
        e = (v, w, weight)
        if v not in self.vers:
            self.vers[v] = []
        self.vers[v].append(e)
        if w not in self.vers:
            self.vers[w] = []
        self.vers[w].append(e)
        self.edges.append(e)


import heapq


class Kruskal:
    def __init__(self, g):
        self.g = g
        self.res = []

    def run(self):
        # min queue to get min weight
        h = []
        for e in self.g.edges:
            heapq.heappush(h, (e[2], e))

        # union to avoid cycle
        u = Union(len(self.g.vers))

        while h:
            weight, e = heapq.heappop(h)
            if not u.connected(e[0], e[1]):
                u.union(e[0], e[1])
                self.res.append(e)


g = EdgeGraph()
g.add_edge(0, 7, 0.16)
g.add_edge(2, 3, 0.17)
g.add_edge(1, 7, 0.19)
g.add_edge(0, 2, 0.26)
g.add_edge(5, 7, 0.28)
g.add_edge(1, 3, 0.29)
g.add_edge(2, 7, 0.34)
g.add_edge(4, 5, 0.35)
g.add_edge(1, 2, 0.36)
g.add_edge(4, 7, 0.37)
g.add_edge(0, 4, 0.38)
g.add_edge(6, 2, 0.40)
g.add_edge(3, 6, 0.52)
g.add_edge(6, 0, 0.58)
g.add_edge(6, 4, 0.93)

k = Kruskal(g)
k.run()
print(k.res)
