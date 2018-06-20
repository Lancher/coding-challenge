# 1. Remember a binary search to help you think.
#    http://www.geeksforgeeks.org/wp-content/uploads/2009/09/BST_LCA.gif


# LEETCODE@ 285. Inorder Successor in BST

# time complexity is O(logn)
def find_successor_parent(root, node):
    # find smallest in right node
    if node.right is not None:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur

    # find cur is parent's left child
    cur = node
    parent = cur.parent
    while parent:
        if cur == parent.left:
            return parent
        cur = parent
        parent = parent.parent

    # maybe there is no successor
    return None


# time complexity is O(logn)
def find_successor(root, node):
    # find smallest in right node
    if node.right is not None:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur

    # travel from root
    cur = root
    successor = None
    while cur:
        if node.val < cur.val:
            successor = cur
            cur = cur.left
        elif node.val > cur.val:
            cur = cur.right
        else:
            break
    return successor
