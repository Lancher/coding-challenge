
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def get(self, key):
        cur = self.root
        while cur:
            if cur.key == key:
                return cur.val
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, node, key, val):
        if node is None:
            return Node(key, val)
        if node.key == key:
            node.val = val
        elif key < node.key:
            node.left = self._put(node.left, key, val)
        else:
            node.right = self._put(node.right, key, val)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key == node.key:
            # find successor and delete
            if node.right is None:
                return node.left
            suc = node.right
            while suc.left is not None:
                suc = suc.left
            node.key, node.val = suc.key, suc.val
            # after swapping, we delete it again
            node.right = self._delete(node.right, suc.key)
        elif key < node.key:
            node.left = self._delete(node.left, key)
        else:
            node.right = self._delete(node.right, key)
        return node

