# LEETCODE@ 662. Maximum Width of Binary Tree
#
# --END--


def widthOfBinaryTree(self, root):
    lrs = []

    def dfs(node, depth, i):
        if node is None:
            return
        if depth >= len(lrs):
            lrs.append([float('inf'), float('-inf')])
        lrs[depth][0] = min(lrs[depth][0], i)
        lrs[depth][1] = max(lrs[depth][1], i)
        dfs(node.left, depth + 1, i * 2 + 1)
        dfs(node.right, depth + 1, i * 2 + 2)

    dfs(root, 0, 0)

    res = 0
    for l, r in lrs:
        res = max(res, r - l + 1)
    return res
