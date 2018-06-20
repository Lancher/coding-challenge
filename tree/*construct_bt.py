# 654. Maximum Binary Tree
#
# 1. Keep an decreasing order array.
#
# 2. Example:
#
#   Input is [3,2,1,6,0,5]
#
#       [3, 2, 1]
#
#   ->  [6]
#
#   ->  [6, 0]
#
#   ->  [6, 5]
#
# --END--


def constructMaximumBinaryTree(self, nums):
    stack = []
    for i in range(len(nums)):
        node = TreeNode(nums[i])
        while stack and stack[-1].val < nums[i]:
            node.left = stack.pop()
        if stack:
            stack[-1].right = node
        stack.append(node)

    return stack[0] if stack else None
