# LEETCODE@ 100. Same Tree
#
# --END--


# Recursive Solution
def is_the_same(p, q):
    if p is None or q is None:
        return p == q
    if p.val == q.val:
        return is_the_same(p.left, q.left) and is_the_same(p.right, q.right)
    else:
        return False


# Iterative Solution
def isSameTree(self, p, q):
    queue = [p, q]
    while queue:
        p = queue.pop()
        q = queue.pop()

        if p is None and q is None:
            continue
        elif p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False

        queue += [p.left, q.left]
        queue += [p.right, q.right]
    return True
