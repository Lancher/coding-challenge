# Convert Binary Tree to Double linked list
#
# --END--


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def bt_to_dll(self, root):
        self.pre = None

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            if self.pre:
                self.pre.right = node
                node.left = self.pre
            self.pre = node
            dfs(node.right)
        dfs(root)


# Test
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node4.left = node2
node4.right = node6

node2.left = node1
node2.right = node3

node6.left = node5
node6.right = node7

s = Solution()
s.bt_to_dll(node4)

cur = node1
while cur:
    print(cur.val)
    cur = cur.right

cur = node7
while cur:
    print(cur.val)
    cur = cur.left



