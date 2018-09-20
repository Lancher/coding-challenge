# https://www.youtube.com/watch?v=3kpmHEJXrsA
#
# --END--


class Node:

    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.max = hi
        self.left = None
        self.right = None

    def __repr__(self):
        return '[{}, {}]'.format(self.lo, self.hi)


class IntervalTree:

    def __init__(self):
        self.root = None

    def insert(self, lo, hi):
        self.root = self._insert(self.root, lo, hi)

    def _insert(self, node, lo, hi):
        # when doing insertion, we use `lo` as key to do the insertions.
        if node is None:
            return Node(lo, hi)

        # go to left when less equal
        if lo <= node.lo:
            node.left = self._insert(node.left, lo, hi)
        else:
            node.right = self._insert(node.right, lo, hi)

        # update `max`
        node.max = max(node.max, hi)

        return node

    def search(self, lo, hi):
        """
        Find all possible intersections.
        """
        res = []
        self._search(self.root, lo, hi, res)
        return res

    def _search(self, node, lo, hi, res):
        # intersection is impossible
        if node is None or node.max < lo:
            return []

        # check current node
        if self._intersect(node, Node(lo, hi)):
            res.append(node)

        # check if right tree is possible
        if node.lo < hi:
            self._search(node.right, lo, hi, res)

        self._search(node.left, lo, hi, res)

    def _intersect(self, n1, n2):
        return n1.lo < n2.hi and n2.lo < n1.hi


# Example:
#
#                 [17, 19]
#               /          \
#              /            \
#        [5, 8]              [21, 24]
#       /     \
#      /       \
# [4, 8]       [15, 18]
#              /      \
#             /        \
#        [7, 10]       [16, 22]
#
#
# Search [21, 23]




tree = IntervalTree()
tree.insert(17, 19)
tree.insert(5, 8)
tree.insert(4, 8)
tree.insert(15, 18)
tree.insert(7, 10)
tree.insert(16, 22)
tree.insert(21, 24)
print(tree.search(21, 23))
