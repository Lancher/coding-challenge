# LEETCODE@ 98. Validate Binary Search Tree
#
# --END--


def isValidBST(self, root):
    return self.dfs(root, float('-inf'), float('inf'))


def dfs(self, node, lo, hi):
    if node is None:
        return True
    if not lo < node.val < hi:
        return False
    return self.dfs(node.left, lo, node.val) and self.dfs(node.right, node.val, hi)
