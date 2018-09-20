# LEETCODE@ 701. Insert into a Binary Search Tree
#
# --END--


def insertIntoBST(self, root, val):
    if root is None:
        return TreeNode(val)

    pre, cur = None, root
    new_node = TreeNode(val)
    while cur:
        if val < cur.val:
            pre, cur = cur, cur.left
        else:
            pre, cur = cur, cur.right

    if val < pre.val:
        pre.left = new_node
    else:
        pre.right = new_node
    return root
