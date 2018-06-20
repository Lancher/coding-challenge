import Queue


# LEETCODE@ 104. Maximum Depth of Binary Tree
#
# --END--


def max_dep_dfs(node):
    return 0 if not node else max(max_dep_dfs(node.left), max_dep_dfs(node.right)) + 1


def max_dep_bfs(root):
    if not root:
        return 0

    q = Queue.Queue()
    q.put(root)
    res = 0

    while not q.empty():
        res += 1
        sz = q.qsize()
        for _ in range(sz):
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
    return res


# LEETCODE@ 111. Minimum Depth of Binary Tree
#
# --END--


def min_dep_dfs(node):
    if not node:
        return 0
    left_h = min_dep_dfs(node.left)
    right_h = min_dep_dfs(node.right)

    return left_h + right_h + 1 if right_h == 0 or right_h == 0 else min(left_h, right_h) + 1


def min_dep_bfs(node):
    if not node:
        return 0
    q = Queue.Queue()
    q.put(node)
    res = 0
    while not q.empty():
        res += 1
        sz = q.qsize()

        for _ in range(sz):
            node = q.get()
            if not node.left and not node.right:
                return res
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
