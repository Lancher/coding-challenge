# TODO Morris Traversel https://www.youtube.com/watch?v=wGXB9OWhPTg


# LEETCODE@ 144. Binary Tree Preorder Traversal
#
# --END--


def preorder_recursive(root):
    res = []

    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res


def preorder_iterative(root):
    res = []
    stack = []
    cur = root
    while stack or cur:
        if cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            cur = cur.right
    return res


# LEETCODE@ 94. Binary Tree Inorder Traversal
#
# --END--


def inorder_recursive(root):
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res


def inorder_iterative(root):
    res = []
    stack = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


# LEETCODE@ 145. Binary Tree Postorder Traversal
#
# Given a binary tree, return the postorder traversal of its nodes' values.
def postorder_recursive(root):
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    return res


def postorder_iterative(root):
    res = []
    stack = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            res.insert(0, cur.val)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
    return res


# 102. LEETCODE@ Binary Tree Level Order Traversal
#
# --END--


def levelorder_recursive(root):
    res = []

    def dfs(node, i):
        if not node:
            return
        if i == len(res):
            res.append([])
        res[i].append(node.val)
        dfs(node.left, i + 1)
        dfs(node.right, i + 1)
    dfs(root, 0)
    return res


import Queue


def levelorder_iterative(root):
    if not root:
        return []
    res = []
    q = Queue.Queue()
    q.put(root)

    while not q.empty():
        sz = q.qsize()
        res.append([])
        for _ in range(sz):
            node = q.get()
            res[-1].append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
    return res


# LEETCODE@ 107. Binary Tree Level Order Traversal II
#
# --END--


def levelOrderBottom(self, root):
    res, q = [], []
    if root:
        q.append(root)

    while q:
        next_q = []
        res.append([])
        for node in q:
            res[-1].append(node.val)
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
        q = next_q
    return res[::-1]


# LEETCODE@ 103. Binary Tree Zigzag Level Order Traversal
#
# --END--


def zigzagLevelOrder(self, root):
    level = 1
    res, q = [], []
    if root:
        q.append(root)

    while q:
        next_q = []
        res.append([])
        for node in q:
            res[-1].append(node.val)
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
        if level % 2 == 0:
            res[-1] = res[-1][::-1]
        q = next_q
        level += 1
    return res
