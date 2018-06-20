# Prim’s Algorithm
# Steps:
# 1. Start with vertex 0 and find the min edge(priority queue) which is adjacent to T.
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


class Prim:
    def __init__(self, g):
        self.g = g
        self.res = []

    def run(self):
        # if the vertex visited
        visited = set()
        # record min weight edges adjacent to current MST
        h = []
        visited.add(0)
        for e in self.g.vers[0]:
            heapq.heappush(h, (e[2], e))

        def other(e, v):
            return e[1] if e[0] == v else e[0]

        while h:
            weight, edge = heapq.heappop(h)
            v, w, _ = edge
            if v not in visited or w not in visited:
                self.res.append(edge)
                if v not in visited:
                    visited.add(v)
                    for e in self.g.vers[v]:
                        if other(e, v) not in visited:
                            heapq.heappush(h, (e[2], e))
                if w not in visited:
                    visited.add(w)
                    for e in self.g.vers[w]:
                        if other(e, w) not in visited:
                            heapq.heappush(h, (e[2], e))


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

p = Prim(g)
p.run()
print(p.res)

