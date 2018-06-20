# LEETCODE@ 110. Balanced Binary Tree
#
# --END--


def balanced(node):
    return dfs(node) != -1


def dfs(node):
    if not node:
        return 0
    l_h = dfs(node.left)
    r_h = dfs(node.right)
    if l_h == -1 or r_h == -1:
        return -1
    if abs(l_h - r_h) > 1:
        return -1
    return max(l_h, r_h) + 1
