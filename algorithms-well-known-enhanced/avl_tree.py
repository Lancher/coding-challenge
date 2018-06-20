# 1. AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and
# right subtrees cannot be more than 1.


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.height = 1
        self.left = self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, node, key, val):
        if node is None:
            return Node(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # check if node is balanced
        height_diff = self._height_diff(node)
        # R
        if height_diff > 1 and key < node.left.key:
            return self._right_rotation(node)
        # LR
        if height_diff > 1 and key > node.left.key:
            node.left = self._left_rotation(node.left)
            return self._right_rotation(node)
        # L
        if height_diff < -1 and key > node.right.key:
            return self._left_rotation(node)
        # RL
        if height_diff < -1 and key < node.right.key:
            node.right = self._right_rotation(node.right)
            return self._left_rotation(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            else:
                # find successor
                suc = node.right
                while suc.left:
                    suc = suc.left
                node.key, node.val = suc.key, suc.val
                node.right = self._delete(node.right, key)
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # check if node is balanced
        height_diff = self._height_diff(node)
        # R
        if height_diff > 1 and self._height_diff(node.left) >= 0:
            return self._right_rotation(node)
        # LR
        if height_diff > 1 and self._height_diff(node.left) < 0:
            node.left = self._left_rotation(node.left)
            return self._right_rotation(node)
        # L
        if height_diff < -1 and self._height_diff(node.right) <= 0:
            return self._left_rotation(node)
        # RL
        if height_diff < -1 and self._height_diff(node.right) > 0:
            node.right = self._right_rotation(node.right)
            return self._left_rotation(node)
        return node

    def _left_rotation(self, root_left):
        root = root_left.right
        root_left.right = root.left
        root.left = root_left
        root_left.height = 1 + max(self._height(root_left.left), self._height(root_left.right))
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        return root

    def _right_rotation(self, root_right):
        root = root_right.left
        root_right.left = root.right
        root.right = root_right
        root_right.height = 1 + max(self._height(root_right.left), self._height(root_right.right))
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        return root

    def _height_diff(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def show(self):
        self._show(self.root)

    def _show(self, node):
        if node is None:
            return
        self._show(node.left)
        print(node.key)
        self._show(node.right)


