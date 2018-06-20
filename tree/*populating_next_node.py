

# LEETCODE@ 116. Populating Next Right Pointers in Each Node
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next
# pointer should be set to NULL.


# time complexity O(n)
def connect_perfect_bt(root):
    while root:
        pre, cur = None, root
        while cur:
            if pre and pre.right and cur.left:
                pre.right.next = cur.left
            if cur.left and cur.right:
                cur.left.next = cur.right
            pre, cur = cur, cur.next
        root = root.left


# LEETCODE@ 117. Populating Next Right Pointers in Each Node
# time complexity O(n)
# Remember the next root (first item in row) and the last child
#
#         0
#       /   \
#     1       2
#    /         \
#   3           4


def connect_bt(root):
    cur = root
    while cur:
        pre_child = None
        nxt = None
        while cur:
            if cur.left:
                if nxt is None:
                    nxt = cur.left
                if pre_child:
                    pre_child.next = cur.left
                pre_child = cur.left
            if cur.right:
                if nxt is None:
                    nxt = cur.right
                if pre_child:
                    pre_child.next = cur.right
                pre_child = cur.right
            cur = cur.next
        cur = nxt
