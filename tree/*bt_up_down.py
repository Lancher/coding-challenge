# LEETCODE@ 156. Binary Tree Upside Down
#
# --END--


def upsideDownBinaryTree(self, root):
    if not root or not root.left:
        return root

    n_root = self.upsideDownBinaryTree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left, root.right = None, None

    return n_root
