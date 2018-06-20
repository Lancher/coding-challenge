# LEETCODE@ 257. Binary Tree Paths
#
# 1) Solution 1: backtracing
#
# 2) Solution 2: bfs
#
# --END--


def get_paths_recursive(root):
    if not root:
        return []
    res, l = [], []
    dfs(res, l, root)
    return res


def dfs(res, l, node):
    if node.left is None and node.right is None:
        l.append(node.val)
        res.append('->'.join(str(i) for i in l))
        l.pop()
    else:
        if node.left:
            l.append(node.val)
            res.append(res, l, node.left)
            l.pop()
        if node.right:
            l.append(node.val)
            res.append(res, l, node.right)
            l.pop()


def get_paths_iterative(root):
    if not root:
        return []
    res = []
    q = [(root, '')]

    for node, s in q:
        next_q = []
        if node.left is None and node.right is None:
            res.append(s + str(node.val))
        if node.left:
            next_q.append((node.left, s + str(node.val) + '->'))
        if node.right:
            next_q.append((node.right, s + str(node.val) + '->'))
    return res
