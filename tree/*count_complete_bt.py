# 222. Count Complete Tree Nodes
#
# --END--


# Recursive Solution
def height_recursive(node):
    return 1 + height_recursive(node.left) if node else 0


def count_nodes_recursive(node):
    if not node:
        return 0
    else:
        h = height_recursive(node)
        if height_recursive(node.right) == h - 1:
            return (1 << h - 1) + count_nodes_recursive(node.right)
        else:
            return (1 << h - 2) + count_nodes_recursive(node.left)


# Iterative Solution
def height_iterative(node):
    h = 0
    while node:
        node = node.left
        h += 1
    return h


def count_nodes_iterative(node):
    res = 0
    h = height_iterative(node)

    while node:
        if height_iterative(node.right) == h - 1:
            res += 1 << (h - 1)
            node = node.right
        else:
            res += 1 << (h - 2)
            node = node.left
        h -= 1
    return res
