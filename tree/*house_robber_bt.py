# 1. recursive
# 2. recursive + dp
# 3. recursive + map


def rob_recursive(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    val = 0
    if root.left:
        val += self.rob(root.left.left) + self.rob(root.left.right)
    if root.right:
        val += self.rob(root.right.left) + self.rob(root.right.right)

    return max(val + root.val, self.rob(root.left) + self.rob(root.right))


# TODO rob_recursive_dp()


# TODO rob_recursive_map()
