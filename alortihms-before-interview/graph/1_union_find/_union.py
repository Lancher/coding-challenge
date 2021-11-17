# 1. Implement root(), connected() and union()
#
# 2. Time Complexity:
#
#   Appending makes the depth of tree to log(n).
#   Path compression makes the running time to c(N+M log*n).
#
# --END--


class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def root(self, p):
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # smaller tree to bigger tree
        root_p, root_q = self.root(p), self.root(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.parent[root_q] = root_p
                self.size[root_p] += self.size[root_q]
