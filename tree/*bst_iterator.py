# LEETCODE@ 173. Binary Search Tree Iterator
#
# --END--


class BSTIterator(object):
    def __init__(self, root):
        self.cur = root
        self.stack = []

    def hasNext(self):
        # put the current node to the stack
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        return bool(self.stack)

    def next(self):
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val
