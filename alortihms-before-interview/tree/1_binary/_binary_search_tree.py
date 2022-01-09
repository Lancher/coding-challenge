"""
1. build tree is O(nlogn), get & put & delete is O(logn)

2. Get:

  Use Node `cur` to do iterative traversal.

3. Put:

  Use `put()` and `_put()` to do recursive traversal.

4. Delete:

  Use `delete()` and `_delete()` to do recursive traversal.

   Find the successor:

        [ cur ]      <---- If the right is None, the left node
       /       \           is our successor.
      /         \
   [ ? ]       [ None ]


        [ cur ]      <---- If the right is not None, we have to find
       /       \           the leftest node in cur.right and it is "X".
      /         \
   [ ? ]       [ ? ]
                 /
                /
             [ X ]

5. Rank:

  Number of nodes less than keys.
  Use `rank()` and `_rank()` to do recursive traversal.

--END--
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
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

        # count is the total number of nodes include itself
        node.count = 1 + self._size(node.left) + self._size(node.right)

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
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        # number of keys less than key.
        if node is None:
            return 0
        if key == node.key:
            return self._size(node.left)
        elif key < node.key:
            return self._rank(node.left, key)
        else:
            return 1 + self._size(node.left) + self._rank(node.right, key)

    def _size(self, node):
        if node is None:
            return 0
        return node.count

    def show(self):
        self._show(self.root)

    def _show(self, node):
        if node is None:
            return
        self._show(node.left)
        print(node.key)
        self._show(node.right)
