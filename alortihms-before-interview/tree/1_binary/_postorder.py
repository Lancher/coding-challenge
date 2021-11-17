# post-order traversal
# --END--


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def recursive(root, res):
    if root:
        recursive(root.left, res)
        recursive(root.right, res)
        res.append(root.val)


def iterative(root):
    # init
    res = []
    cur = root
    stack = []

    while stack or cur:
        if cur:
            stack.append(cur)
            res.insert(0, cur.val)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
    return res


# test
#          3
#       2     5
#    1      4   6
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n3.left = n2
n3.right = n5
n2.left = n1
n5.left = n4
n5.right = n6

res1 = []
recursive(n3, res1)

res2 = iterative(n3)

assert res1 == res2
