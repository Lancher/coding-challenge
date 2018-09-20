# LEETCODE@ Find Duplicate Subtrees
#
# --END--


def findDuplicateSubtrees(self, root):
    vst = set()
    res_vst = set()
    res = []
    self.dfs(root, vst, res_vst, res)
    return res


def dfs(self, node, vst, res_vst, res):
    if not node:
        return []
    left = self.dfs(node.left, vst, res_vst, res)
    right = self.dfs(node.right, vst, res_vst, res)

    # We need add seperator otherwise the T1 and T2 order will be the same!!!
    #
    #   T1         T2
    #       0         0
    #     /             \
    #    0                0
    #
    # Original T1: 00, T2: 00
    # After:   T1: (0)0, 0(0)
    left = ['('] + [str(val) for val in left] + [')']
    right = ['('] + [str(val) for val in right] + [')']
    order = ['('] + left + [str(node.val)] + right + [')']
    key = '_'.join(order)
    if key in vst:
        # avoid dulpicate result
        if key not in res_vst:
            res_vst.add(key)
            res.append(node)
    else:
        vst.add(key)
    return left + right + [node.val]
