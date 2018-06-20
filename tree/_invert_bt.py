# LEETCODE@ 226. Invert Binary Tree
#
# --END--


import Queue


def invert_recursive(node):
    if node:
        node.left, node.right = invert_recursive(node.right), invert_recursive(node.left)
    return node


def invert_bfs(root):
    if not root:
        return root

    q = Queue.Queue()
    q.put(root)

    while not q.empty():
        for _ in range(q.qsize()):
            node = q.get()
            node.left, node.right = node.right, node.left
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
    return root


def invert_dfs(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += [node.left, node.right]
    return root
