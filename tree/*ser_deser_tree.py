
# LEETCODE@ 297. Serialize and Deserialize Binary Tree


# 1. use preorder to build data and tree.
#       1
#     /   \
#    2     #
#   / \
#  #   3
#     / \
#    #   #
#
#  the data is [1, 2, #, 3, #, #, #]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        def dfs(node, data):
            if node:
                data.append(node.val)
                dfs(node.left, data)
                dfs(node.right, data)
            else:
                data.append('#')

        data = []
        dfs(root, data)
        return data

    def deserialize(self, data):
        def build(data):
            val = data.pop(0)
            if val == '#':
                return None
            else:
                node = TreeNode(val)
                node.left = build(data)
                node.right = build(data)
                return node
        return build(data)
