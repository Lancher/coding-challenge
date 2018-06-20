# LEETCODE@ 114. Flatten Binary Tree to Linked List
#
# --END--


class Solution:
    def bt_to_ll_recursive_sol1(self, root):
        self.pre = None

        def dfs(node):
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = self.pre
            node.left = None
            self.pre = node
        dfs(root)

    def b_to_ll_recursive_sol2(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        self.b_to_ll_recursive_sol2(root.left)
        self.b_to_ll_recursive_sol2(right)

        # append left to right, and then right append to new right
        root.left = None
        root.right = left
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = right

    def b_to_ll_iterative_morris_traversal(self, root):
        if not root:
            return

        node = root
        while node:
            # find predecessor
            if node.left:
                pre = node.left
                while pre.right:
                    pre = pre.right
                pre.right = node.right
                node.right = node.left
                node.left = None
            node = node.right


# time complexity O(n)
def bt_to_ll_iterative(node):
    pass
