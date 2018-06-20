# LEETCODE@ 669. Trim a Binary Search Tree
#
# --END--


# time complexity is O(n)
def trimBST(self, root, L, R):
    return self.dfs(root, L, R)


def dfs(self, node, l, r):
    if node is None:
        return node
    node.left = self.dfs(node.left, l, r)
    node.right = self.dfs(node.right, l, r)

    if l <= node.val <= r:
        return node
    # if there is a cut, one of the side will be abandon
    else:
        return node.left or node.right
