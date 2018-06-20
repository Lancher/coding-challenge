

# LEETCODE@ 199. Binary Tree Right Side View
#
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can
# see ordered from top to bottom.
def right_side_view(self, root):
    res = []
    self.dfs(root, 0, res)
    return res


def dfs(self, node, level, res):
    if not node:
        return
    if level == len(res):
        res.append(node.val)
    self.dfs(node.right, level + 1, res)
    self.dfs(node.left, level + 1, res)
