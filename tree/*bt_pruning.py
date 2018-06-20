# LEETCODE@ 814. Binary Tree Pruning
#
# --END--


def pruneTree(self, root):
    if self.dfs(root) == 0:
        return None
    else:
        return root


def dfs(self, node):
    if node is None:
        return 0
    l_val = self.dfs(node.left)
    r_val = self.dfs(node.right)

    if l_val == 0:
        node.left = None
    if r_val == 0:
        node.right = None

    return l_val | r_val | node.val