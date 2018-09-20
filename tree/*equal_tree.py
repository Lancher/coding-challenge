# LEETCODE@ 663. Equal Tree Partition
#
# --END-


def checkEqualTree(self, root):
    if not root:
        return False

    # remember subtrees sum
    s = set()

    # find sum of tree
    def tree_sum(node):
        if node.left:
            l_sum = tree_sum(node.left)
            s.add(l_sum)
        else:
            l_sum = 0
        if node.right:
            r_sum = tree_sum(node.right)
            s.add(r_sum)
        else:
            r_sum = 0
        return node.val + l_sum + r_sum

    sm = tree_sum(root)
    if sm % 2 == 1:
        return False

    return int(sm / 2) in s
