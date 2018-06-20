# 1. Space-partitioning trees.
#
# 2. In even level, we use vertical line, in odd level we use horizontal line.
#
# 3. K-dimensional data, leve = i mode k.
#
# 4. Example:
#
#                   V
#                 /   \
#               H       H
#              / \     / \
#             V   V   V   V
#            / \ / \ / \ / \
#           H  HH  HH  HH   H
#
#
#
# --END--


class Node:
    def __init__(self, k, points):
        self.k = k
        self.points = points[:]
        self.left = self.right = None


class KDTree:
    def __init__(self, k):
        self.k = k
        self.root = None

    def put(self, points):
        self.root = self._put(self.root, 0, points)

    def _put(self, node, depth, points):
        if node is None:
            return Node(self.k, points)
        d = depth % self.k
        if points[d] < node.points[d]:
            node.left = self._put(node.left, depth + 1, points)
        else:
            node.right = self._put(node.right, depth + 1, points)
        return node

    def show(self):
        self._show(self.root)

    def _show(self, node):
        if node is None:
            return
        self._show(node.left)
        print(node.points)
        self._show(node.right)
