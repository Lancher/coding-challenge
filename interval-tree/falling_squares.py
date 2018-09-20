# LEETCODE@ 699. Falling Squares
#
# --END--


class Node:
    def __init__(self, lo, hi, val):
        self.lo = lo
        self.hi = hi
        self.max = hi
        self.left = None
        self.right = None

        self.val = val

    def __repr__(self):
        return '[{}, {}]'.format(self.lo, self.hi)


class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, lo, hi, val):
        self.root = self._insert(self.root, lo, hi, val)

    def _insert(self, node, lo, hi, val):
        # when doing insertion, we use `lo` as key to do the insertions.
        if node is None:
            return Node(lo, hi, val)

        # go to left when less equal
        if lo <= node.lo:
            node.left = self._insert(node.left, lo, hi, val)
        else:
            node.right = self._insert(node.right, lo, hi, val)

        # update `max`
        node.max = max(node.max, hi)

        return node

    def search(self, lo, hi):
        """
        Find all possible intersections.
        """
        res = [0]
        self._search(self.root, lo, hi, res)
        return res[0]

    def _search(self, node, lo, hi, res):
        # intersection is impossible
        if node is None or node.max < lo:
            return

        # check current node
        if self._intersect(node, Node(lo, hi, -1)):
            res[0] = max(res[0], node.val)

        # check if right tree is possible
        if node.lo < hi:
            self._search(node.right, lo, hi, res)

        self._search(node.left, lo, hi, res)

    def _intersect(self, n1, n2):
        return n1.lo < n2.hi and n2.lo < n1.hi


class Solution:
    def fallingSquares(self, positions):
        n = len(positions)

        # build interval search tree
        tree = IntervalTree()

        mx = 0
        res = []
        for i in range(n):
            lo, hi = positions[i][0], positions[i][0] + positions[i][1]

            # find the highest in the interval
            h = tree.search(lo, hi)

            # update current max
            mx = max(mx, h + hi - lo)
            res.append(mx)
            tree.insert(lo, hi, h + hi - lo)
        return res
