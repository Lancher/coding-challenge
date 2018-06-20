# LEETCODE@ 255. Verify Preorder Sequence in Binary Search Tree
#
# 1. Use stack to maintain a decreasing array.
#
# 2.     5
#      /   \        Pre Order is [5, 2, 6].
#     /     \       the lower bound is 5 for 6.
#   2         6
#
# --END--


def verifyPreorder(self, preorder):
    low = float('-inf')
    stack = []
    for i in preorder:
        if i < low:
            return False
        while stack and i > stack[-1]:
            low = stack.pop()
        stack.append(i)
    return True
