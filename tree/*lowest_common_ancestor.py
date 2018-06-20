# LEETCODE@ 235. Lowest Common Ancestor of a Binary Search Tree
#
# --EMD--


def lca_bst_recursive(root, p, q):
    if not root:
        return root
    if q.val < p.val:
        p, q = q, p
    if p.val <= root.val <= q.val:
        return root
    if root.val > q.val:
        return lca_bst_recursive(root.left, p, q)
    if root.val < p.val:
        return lca_bst_recursive(root.right, p, q)


def lca_bst_iterative(root, p, q):
    if q.val < p.val:
        p, q = q, p
    while root:
        if root.val > q.val:
            root = root.left
        elif root.val < p.val:
            root = root.right
        else:
            break
    return root


# LEETCODE@ 236. Lowest Common Ancestor of a Binary Tree
#
# --END--


# time complexity O(n)
def lca_bt(root, p, q):
    if not root:
        return root
    if root == p or root == q:
        return root
    left = lca_bt(root.left, p, q)
    right = lca_bt(root.right, p, q)
    if left and right:
        return root
    # // return one of valid node
    return left if left else right


# time complexity O(logn)
def lca_bt_parent(p, q):
    s = set()

    while p or q:
        # check p
        if p in s:
            return p
        else:
            s.add(p)
            p = p.parent

        # check q
        if q in s:
            return q
        else:
            s.add(q)
            q = q.parent




