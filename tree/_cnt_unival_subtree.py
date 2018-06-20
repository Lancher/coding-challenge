# LEETCODE@ 250. Count Univalue Subtrees
#
# --END--


def countUnivalSubtrees(self, root):
    res = [0]
    self.dfs(root, res)
    return res[0]


def dfs(self, node, res):
    if not node:
        return True
    left = self.dfs(node.left, res)
    right = self.dfs(node.right, res)

    if left and right:
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        res[0] += 1
        return True
    return False
