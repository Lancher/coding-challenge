# LEETCODE@ 783. Minimum Distance Between BST Nodes
#
# 1. Remember the previous element.
#
# --END--


_MAX = float('inf')


def minDiffInBST(self, root):
    pre = [None]
    res = [_MAX]

    def dfs(node, pre, res):
        if not node:
            return
        dfs(node.left, pre, res)
        if pre[0] is not None:
            res[0] = min(res[0], abs(pre[0] - node.val))
        pre[0] = node.val
        dfs(node.right, pre, res)

    dfs(root, pre, res)

    return res[0]
