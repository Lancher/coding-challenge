# Segment Tree
#
# 1) Segment Tree for Range Sum
#
#   [-1, 3, 4, 0, 2, 1]
#
#                           (9)[0, 5]          <= sum [start index, end index]
#                               |
#                         ------------
#                        /            \
#                       /              \
#                (6)[0, 2]             (3)[3, 5]
#                   |                      |
#                 -----                  -----
#                /     \                /     \
#               /       \              /       \
#          (2)[0, 1]   (4)[2, 2]   (2)[3, 4]  (1)[5, 5]
#             |                        |
#           -----                    ------
#           /    \                  /      \
#          /      \                /        \
#     (-1)[0, 0]  (3)[1, 1]    (0)[3, 3]   (2)[4, 4]
#
#
#
# 3) Examples:
#
#   Range Minimum Query: http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
#   Range Sum: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
#
# --END--


class Node:
    def __init__(self, s, e, val):
        self.s, self.e, self.val = s, e, val
        self.left, self.right = None, None


class ST:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, s, e):
        if s == e:
            return Node(s, e, self.nums[s])
        elif s < e:
            m = int((s + e) / 2)
            node = Node(s, e, 0)
            node.left = self.build(s, m - 1)
            node.right = self.build(m + 1, e)
            return node
        else:
            return None

    def update(self, node, i, val):
        if not node:
            return 0

        # 1) Not in the range
        if i < node.s or node.e < i:
            # RangeSum: return 0
            return 0

        # 2) We arrive the leaf
        # RangeSum: assign the value
        # MinQuery: assign the value
        if i == node.s == node.e:
            node.val = val
            return node.val

        # 3) Intermediate nodes
        # RangeSum: sum two node
        # MinQuery: min(update(node.left), update(node.right))
        node.val = self.update(node.left, i, val) + self.update(node.right, i, val)
        return node.val

    # RangeSum: sum()
    def sum(self, node, s, e):
        if not node:
            return 0

        # 1) not in the range
        if e < node.s or node.e < s:
            return 0

        # 2) total overlap
        if s <= node.s and node.e <= e:
            return node.val

        # 3) partial overlap
        return self.sum(node.left, s, e) + self.sum(node.right, s, e)

    # MinQuery: min()
    def min(self, node, s, e):
        if not node:
            return float('inf')

        # 1) not in the range
        if e < node.s or node.e < s:
            return float('inf')

        # 2) total overlap
        if s <= node.s and node.e <= e:
            return node.val

        # 3) partial overlap
        return min(self.min(node.left, s, e), self.min(node.right, s, e))
