# LEETCODE@ 776. Split BST
#
# 1. How to slice, use the return node to check if the slice happen?
#
# 2. Return from left & right node:
#
#            100
#          /
#         /
#      10
#         \          ==> If we slice at 50, there two situations.
#          \
#           90           When 50 return, we check if the slice happen 50 <= slice < 90
#          /
#         /              When 90 return, we check if the slice happen 10 <= slice < 90
#        50
#
# --END--


def splitBST(self, root, V):
    return self.dfs(root, V)


def dfs(self, node, V):
    if node is None:
        return [None, None]

    n1, n2 = None, None
    l_sm, l_bg = self.dfs(node.left, V)
    r_sm, r_bg = self.dfs(node.right, V)

    # 1) if the cut is on the right, we can guarantee the pair from left node will
    # not contain bigger node.
    if node.val <= V:
        node.left = l_sm
        node.right = r_sm
        n1 = node
        n2 = r_bg
    # 2) if the cut is on the left, we can guarantee the pair from right will not
    #    contain the smaller one.
    else:
        node.left = l_bg
        node.right = r_bg
        n1 = l_sm
        n2 = node

    return [n1, n2]
