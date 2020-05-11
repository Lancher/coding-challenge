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
    def __init__(self, s, e, num, wgh):
        self.s, self.e = s, e
        self.num = num
        self.wgh = wgh
        self.left = self.right = None


class SegmentTree:
    def __init__(self, nums, wghs):
        self.root = self._build(0, len(nums) - 1, nums, wghs)

    def _build(self, s, e, nums, wghs):
        if s > e:
            return None
        elif s == e:
            return Node(s, e, nums[s], wghs[s])
        else:
            m = (s + e) // 2
            node = Node(s, e, None, 0)
            node.left = self._build(s, m, nums, wghs)
            node.right = self._build(m + 1, e, nums, wghs)
            node.wgh += 0 if node.left is None else node.left.wgh
            node.wgh += 0 if node.right is None else node.right.wgh
            return node

    def update(self, i, num, wgh):
        self._update(self.root, i, num, wgh)

    def _update(self, node, i, num, wgh):
        if node is None:
            return 0
        # 1) not in the range
        elif node.s > i or node.e < i:
            return node.wgh
        # 2) total overlap
        elif node.s == node.e == i:
            node.num = num
            node.wgh = wgh
            return node.wgh
        # 3) partial overlap
        else:
            node.wgh = self._update(node.left, i, num, wgh) + self._update(node.right, i, num, wgh)
            return node.wgh

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
            return node.wgh
        # 3) partial overlap
        else:
            return self._range_sum(node.left, s, e) + self._range_sum(node.right, s, e)

    def traverse(self, wgh):
        sm = 0
        pre, cur = None, self.root
        while cur:
            prefix = cur.left.wgh if cur.left else 0
            prefix += sm
            if prefix <= wgh:
                sm = prefix
                pre, cur = cur, cur.right
            else:
                pre, cur = cur, cur.left
        return pre


# We pick an element based on the weight, and we will not put elements
# back.
nums = [101, 48, -18, 120, 8, 11]
wghs = [2, 3, 4, 5, 2, 1]
n = len(nums)
st = SegmentTree(nums, wghs)
print('Sum:', st.range_sum(0, n - 1))

# If we have a random weight 15.1
print('Delete idx:', st.traverse(15.1).s)
delete = st.traverse(15.1)

# We swap with last element
if delete.s == n - 1:
    st.update(delete.s, None, 0)
else:
    swap = st.traverse(st.range_sum(0, n - 1))
    st.update(delete.s, swap.num, swap.wgh)
    st.update(n - 1, None, 0)
n -= 1
print('Sum:', st.range_sum(0, n - 1))
