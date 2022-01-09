"""
Segment Tree

1) Segment Tree for Range Sum

  [-1, 3, 4, 0, 2, 1]

                          (9)[0, 5]          <= sum [start index, end index]
                              |
                        ------------
                       /            \
                      /              \
               (6)[0, 2]             (3)[3, 5]
                  |                      |
                -----                  -----
               /     \                /     \
              /       \              /       \
         (2)[0, 1]   (4)[2, 2]   (2)[3, 4]  (1)[5, 5]
            |                        |
          -----                    ------
          /    \                  /      \
         /      \                /        \
    (-1)[0, 0]  (3)[1, 1]    (0)[3, 3]   (2)[4, 4]



3) Examples:

  Range Minimum Query: http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
  Range Sum: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

--END--
"""


class Node:
    def __init__(self, s, e, val):
        self.s, self.e = s, e
        self.val = val
        self.left = self.right = None


class SegmentTree:
    def __init__(self, nums):
        self.root = self._build(0, len(nums) - 1, nums)

    def _build(self, s, e, nums):
        if s > e:
            return None
        elif s == e:
            return Node(s, e, nums[s])
        else:
            m = (s + e) // 2
            node = Node(s, e, 0)
            node.left = self._build(s, m, nums)
            node.right = self._build(m + 1, e, nums)
            node.val += 0 if node.left is None else node.left.val
            node.val += 0 if node.right is None else node.right.val
            return node

    def update(self, i, val):
        self._update(self.root, i, val)

    def _update(self, node, i, val):
        if node is None:
            return 0
        # 1) not in the range
        elif node.s > i or node.e < i:
            return node.val
        # 2) total overlap
        elif node.s == node.e == i:
            node.val = val
            return node.val
        # 3) partial overlap
        else:
            node.val = self._update(node.left, i, val) + self._update(node.right, i, val)
            return node.val

    def range_sum(self, s, e):
        return self._range_sum(self.root, s, e)

    def _range_sum(self, node, s, e):
        if node is None:
            return 0
        # 1) not in the range
        elif node.e < s or node.s > e:
            return 0
        # 2) total overlap
        elif s <= node.s and node.e <= e:
            return node.val
        # 3) partial overlap
        else:
            return self._range_sum(node.left, s, e) + self._range_sum(node.right, s, e)

nums = [2, 3, 4, 5, 2, 1]

st = SegmentTree(nums)
print(st.range_sum(0, 0))
