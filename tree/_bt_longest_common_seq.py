# LEETCODE@ 298. Binary Tree Longest Consecutive Sequence
#
# --END--


def longestConsecutive(self, root):
    res = [0]
    self.dfs(root, None, 0, res)
    return res[0]


def dfs(self, node, parent, cnt, res):
    if node is None:
        return
    if parent and parent.val + 1 == node.val:
        cnt += 1
    else:
        cnt = 1
    res[0] = max(res[0], cnt)
    left = self.dfs(node.left, node, cnt, res)
    right = self.dfs(node.right, node, cnt, res)
