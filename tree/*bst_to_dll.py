# LEETCODE 426. Convert Binary Search Tree to Sorted Doubly Linked List
#
# 1. inorder traverse will solve the problem.
#
# --END--


def treeToDoublyList(self, root):
    if root is None:
        return None

    # dummy node
    dummy = Node(-1, None, None)

    # previous node, first node, last node
    mem_nodes = [dummy, None, None]

    # inorder traverse
    self.dfs(root, mem_nodes)

    # connect the first node with the last node
    mem_nodes[1].left = mem_nodes[2]
    mem_nodes[2].right = mem_nodes[1]
    return dummy.right


def dfs(self, node, mem_nodes):
    if not node:
        return
    self.dfs(node.left, mem_nodes)

    # update the first node & last node
    if mem_nodes[1] is None:
        mem_nodes[1] = node
    mem_nodes[2] = node

    # connect the previous node with the last node
    mem_nodes[0].right = node
    node.left = mem_nodes[0]
    mem_nodes[0] = node
    self.dfs(node.right, mem_nodes)