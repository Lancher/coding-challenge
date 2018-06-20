# 1. Root is black, No two adjacent red nodes, Every path has the same black nodes.
# 2. Insert new node is always red node.
# 3. Check the parent & uncle node.
# 4. Parent node == uncle and node == red => recolor
# 5. Parent node == RED, uncle node == BLACK => rotation & recolor


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.color = 'r'
        self.parent = self.left = self.right = None


class RBTree:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        new_node = [None]
        self.root = self._put(self.root, key, val, new_node)
        self._fix_put_violation(new_node[0])

    def _put(self, node, key, val, new_node):
        if node is None:
            new_node[0] = Node(key, val)
            return new_node[0]
        if key < node.key:
            node.left = self._put(node.left, key, val, new_node)
            node.left.parent = node
        elif key > node.key:
            node.right = self._put(node.right, key, val, new_node)
            node.right.parent = node
        else:
            node.val = val
            new_node[0] = node
        return node

    def _fix_put_violation(self, node):
        while node.color == 'r' and node.parent and node.parent == 'r':
            parent = node.parent
            grand = node.parent.parent

            if parent == grand.left:
                uncle = grand.right
                if uncle and uncle.color == 'r':
                    grand.color = 'r'
                    parent.color = 'b'
                    uncle.color = 'b'
                    node = grand
                else:
                    if node == parent.right:
                        self._left_rotation(parent)
                        node = parent
                        parent = node.parent
                    self._right_rotation(grand)
                    parent.color, grand.color = grand.color, parent.color
                    node = parent
            else:
                uncle = grand.right
                if uncle and uncle.color == 'r':
                    grand.color = 'r'
                    parent.color = 'b'
                    uncle.color = 'b'
                    node = grand
                else:
                    if node == parent.left:
                        self._right_rotation(parent)
                        node = parent
                        parent = node.parent
                    self._left_rotation(grand)
                    parent.color, grand.color = grand.color, parent.color
                    node = parent
        if self.root:
            self.root.color = 'b'

    def _left_rotation(self, root_left):
        root = root_left.right
        # prompt root
        if root_left.parent is None:
            self.root = root
        elif root_left.parent.left == root_left:
            root_left.parent.left = root
        else:
            root_left.parent.right = root
        root.parent = root_left.parent
        # move child
        root_left.right = root.left
        if root_left.right:
            root_left.right.parent = root_left
        # sink root_left
        root.left = root_left
        root_left.parent = root
        return root

    def _right_rotation(self, root_right):
        root = root_right.left
        # prompt root
        if root_right.parent is None:
            self.root = root
        elif root_right.parent.left == root_right:
            root_right.parent.left = root
        else:
            root_right.parent.right = root
        # move child
        root_right.left = root.right
        if root_right.left:
            root_right.left.parent = root_right
        # sink root_right
        root.right = root_right
        root_right.parent = root

    def show(self):
        self._show(self.root)

    def _show(self, node):
        if node is None:
            return
        self._show(node.left)
        print(node.key)
        self._show(node.right)


