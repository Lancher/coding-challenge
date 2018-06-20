# LEETCODE@ 270. Closest Binary Search Tree Value
#
# --END--


def closestValue(self, root, target):
    res = [root.val]
    self.dfs(root, target, res)
    return res[0]


def dfs(self, node, target, res):
    if node is None:
        return
    if abs(node.val - target) < abs(res[0] - target):
        res[0] = node.val
    # we walk as binary search, we want to close the value as much as possible
    if target < node.val:
        self.dfs(node.left, target, res)
    if node.val < target:
        self.dfs(node.right, target, res)


# LEETCODE@ 272. Closest Binary Search Tree Value II
#
# --END--


def closestKValues(self, root, target, k):
    result = []
    pre_stack, suc_stack = [], []
    self.pre_inorder(root, target, pre_stack)
    self.suc_inorder(root, target, suc_stack)

    while k:
        if not pre_stack:
            result.append(suc_stack.pop())
        elif not suc_stack:
            result.append(pre_stack.pop())
        elif abs(suc_stack[-1] - target) < abs(pre_stack[-1] - target):
            result.append(suc_stack.pop())
        else:
            result.append(pre_stack.pop())
        k -= 1
    return result


def pre_inorder(self, root, target, stack):
    if not root:
        return
    self.pre_inorder(root.left, target, stack)
    if (root.val > target):
        return
    stack.append(root.val)
    self.pre_inorder(root.right, target, stack)


def suc_inorder(self, root, target, stack):
    if not root:
        return
    self.suc_inorder(root.right, target, stack)
    if (root.val <= target):
        return
    stack.append(root.val)
    self.suc_inorder(root.left, target, stack)
