# LEETCODE@ 124. Binary Tree Maximum Path Sum
#
#   1) there are 4 situations
#      - self is the biggest
#      - left + self is the biggest
#      - right + self is the biggest
#      -  self + left + right is the biigest
#
# --END--


_MIN = float('-inf')
_MAX = float('inf')


class Solution(object):
    def maxPathSum(self, root):
        self.val = _MIN
        self.dfs(root)
        return self.val

    def dfs(self, node):
        if node is None:
            return _MIN
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.val = max(self.val, node.val, left + node.val, right + node.val,
                       node.val + left + right)
        return max(node.val, max(left, right) + node.val)


# LEETCODE@ 112. Path Sum
#
# --END--


# Solution1
def path_sum_root_to_leaf(root, s):
    if not root:
        return []
    l = [root.val]
    res = []
    backtracing(res, l, s - root.val, root)
    return res


def backtracing(res, l, s, node):
    if not node.left and not node.right:
        if s == 0:
            res.append(l[:])
    else:
        if node.left:
            l.append(node.left.val)
            backtracing(res, l, s - node.left.val, node.left)
            l.pop()
        if node.right:
            l.append(node.right.val)
            backtracing(res, l, s - node.right.vak, node.right)
            l.pop()


# Solution2
def hasPathSum(self, root, sum):
    return self.dfs(root, 0, sum)


def dfs(self, node, s, sum):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return s + node.val == sum
    return self.dfs(node.left, s + node.val, sum) or self.dfs(node.right, s + node.val, sum)


# LEETCODE@ 113. Path Sum II
#
# --END--


def pathSum(self, root, sum):
    res = []
    arr = []
    self.dfs(root, sum, 0, arr, res)
    return res


def dfs(self, node, sum, acc, arr, res):
    if node is None:
        return
    else:
        if node.left:
            arr.append(node.val)
            self.dfs(node.left, sum, acc + node.val, arr, res)
            arr.pop()
        if node.right:
            arr.append(node.val)
            self.dfs(node.right, sum, acc + node.val, arr, res)
            arr.pop()
        if node.left is None and node.right is None:
            arr.append(node.val)
            if acc + node.val == sum:
                res.append(arr[:])
            arr.pop()


# LEETCODE@ 666. Path Sum IV
#
# --END--


def pathSum(self, nums):
    # use 2d matrix to build a tree
    tree = [[[0, 0] for j in range(8)] for i in range(4)]

    for num in nums:
        num = str(num)
        i, j, v = int(num[0]) - 1, int(num[1]) - 1, int(num[2])
        tree[i][j][0] = v
        tree[i][j][1] = 1

    for i in range(2, -1, -1):
        for j in range(0, 2 ** i):
            c1, c2 = j * 2, j * 2 + 1
            if tree[i + 1][c1][1] + tree[i + 1][c2][1] > 0:
                tree[i][j][1] = tree[i + 1][c1][1] + tree[i + 1][c2][1]

    res = 0
    for i in range(4):
        for j in range(8):
            res += tree[i][j][0] * tree[i][j][1]
    return res