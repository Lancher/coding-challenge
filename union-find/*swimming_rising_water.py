# LEETCODE@ 778. Swim in Rising Water
#
# Solution: Union Find
#
# --END--


class UnionFind:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.size = [1] * n

    def root(self, i):
        while i != self.arr[i]:
            self.arr[i] = self.arr[self.arr[i]]
            i = self.arr[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p, q = self.root(p), self.root(q)
        if p != q:
            if self.size[p] < self.size[q]:
                self.arr[p] = q
                self.size[q] += self.size[p]
            else:
                self.arr[q] = p
                self.size[p] += self.size[q]


def swimInWater(self, grid):
    m, n = len(grid), len(grid[0])

    # index mapping
    index = [0] * (m * n)
    for i in range(m):
        for j in range(n):
            index[grid[i][j]] = i * n + j

    # union find
    u = UnionFind(m * n)

    for t in range(m * n):
        i, j = index[t] / m, index[t] % m
        # try to union four direction
        x, y = 0, 1
        for _ in range(4):
            if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] < t:
                u.union(grid[i][j], grid[i + x][j + y])
            x, y = y, -x

        # check if start and end connected
        if u.connected(grid[0][0], grid[m - 1][n - 1]):
            return t


# Solution: Heap
#
# --END--
import heapq


def swimInWater(self, grid):
    n = len(grid)
    res = 0
    h = [(grid[0][0], 0, 0)]
    seen = set()

    while True:
        # always find smallest node around
        t, i, j = heapq.heappop(h)
        res = max(res, t)
        seen.add((i, j))
        if i == n - 1 and j == n - 1:
            return res

        # 4 directions
        x, y = 1, 0
        for _ in range(4):
            x, y = -y, x
            n_i, n_j = i + x, j + y
            if 0 <= n_i < n and 0 <= n_j < n and (n_i, n_j) not in seen:
                heapq.heappush(h, (grid[n_i][n_j], n_i, n_j))
