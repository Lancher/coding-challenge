# LEETCODE@ 655. Print Binary Tree
#
# --END--


def printTree(self, root):
    # find the maximum height
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        return 1 + max(left, right)

    m = height(root)

    # count the width
    n = 1
    for i in range(m - 1):
        n = n * 2 + 1

    # build the board
    res = [['' for j in range(n)] for i in range(m)]

    # dfs
    def dfs(node, i, j, ln):
        if node is None:
            return
        res[i][j] = str(node.val)
        dfs(node.left, i + 1, j - int(ln / 2) - 1, int(ln / 2))
        dfs(node.right, i + 1, j + int(ln / 2) + 1, int(ln / 2))

    dfs(root, 0, int(n / 2), int(n / 2))
    return res
