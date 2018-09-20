# @LEETCODE 623. Add One Row to Tree
#
# 1. We also have to add `None` nodes to the queue.
#
#       2     v=7 & d = 2        2
#     /   \  ==========>       /   \
#    1                        7     7
#                            /
#                           1
#
# --END--


def addOneRow(self, root, v, d):
    # the depth is 1
    if d == 1:
        node = TreeNode(v)
        node.left = root
        return node

    # the depth is greater than 1 and root is not None
    q = []
    cur_d = 2

    # we also have to add `None` nodes to the queue.
    q.append([root.left, root, 'L'])
    q.append([root.right, root, 'R'])

    # bfs
    while q:
        if cur_d == d:
            for node, parent, l_r in q:
                new_node = TreeNode(v)
                if l_r == 'L':
                    new_node.left = node
                    parent.left = new_node
                else:
                    new_node.right = node
                    parent.right = new_node
            next_q = []
        else:
            next_q = []
            for node, parent, l_r in q:
                # we also have to add `None` nodes to the queue.
                if node:
                    next_q.append([node.left, node, 'L'])
                    next_q.append([node.right, node, 'R'])
        # update q & depth
        q = next_q
        cur_d += 1
    return root
