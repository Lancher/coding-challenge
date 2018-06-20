# LEETCODE@ 101. Symmetric Tree
#
# --END--


def is_symmetric_recursive(self, root):
    if root is None:
        return True
    return self.helper(root.left, root.right)


def helper(self, left, right):
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return self.helper(left.left, right.right) and self.helper(left.right, right.left)


def is_symmetric_iterative(root):
    if root is None:
        return True
    q = [root.left, root.right]

    while q:
        left = q.pop()
        right = q.pop()

        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            continue
        else:
            if left.val != right.val:
                return False
        q += [left.left, right.right]
        q += [left.right, right.left]
    return True

