

# LEETCODE@ 230. Kth Smallest Element in a BST
#
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# TODO Follow-Up


# recursive
def bst_find_k_smallest_recursive(root, k):
    res = [None]
    count = [0]

    def dfs(node):
        if res[0] is not None:
            return
        if not node:
            return
        dfs(node.left)
        count[0] += 1
        if count[0] == k:
            res[0] = node.val
        dfs(node.right)

    dfs(root)
    return res[0]


# iterative
def bst_find_k_smallest_iterative(root, k):
    stack = []

    while root:
        stack.append(root)
        root = root.left

    c = 0
    while stack:
        node = stack.pop()
        c += 1
        if c == k:
            return node.val
        cur = node.right
        while cur:
            stack.append(cur)
            cur = cur.left

