# LEETCODE@ 99. Recover Binary Search Tree
#
# --END--


def recoverTree(self, root):
    pre = [None]
    elements = [None, None]
    self.inorder(root, pre, elements)
    elements[0].val, elements[1].val = elements[1].val, elements[0].val


def inorder(self, node, pre, elements):
    if node is None:
        return
    self.inorder(node.left, pre, elements)
    if pre[0] is not None and pre[0].val > node.val:
        if elements[0] is None:
            elements[0] = pre[0]
        if elements[0] is not None:
            elements[1] = node
    pre[0] = node
    self.inorder(node.right, pre, elements)
