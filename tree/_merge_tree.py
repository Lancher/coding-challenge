# LEETCODE@ 617. Merge Two Binary Trees
#
# --END--


def merge_tree(t1, t2):
    if t1 is None and t2 is None:
        return None
    node = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    node.left = merge_tree(t1.left if t1 else None, t2.left if t2 else None)
    node.right = merge_tree(t1.right if t1 else None, t2.right if t2 else None)
    return node
