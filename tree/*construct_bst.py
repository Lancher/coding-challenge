# LEETCODE@ 108. Convert Sorted Array to Binary Search Tree
#
# --END--


def build_bst_from_sorted_array(nums):
    return build_sorted_array(nums, 0, len(nums) - 1)


def build_sorted_array(nums, lo, hi):
    if lo > hi:
        return None
    mi = (lo + hi) / 2
    node = Node(nums[mi])
    node.left = build_sorted_array(nums, lo, mi - 1)
    node.right = build_sorted_array(nums. mi + 1, hi)
    return node


# LEETCODE@ 105. Construct Binary Tree from Preorder and Inorder Traversal
#
# 1. Can we construct the tree from pre-order & post-order?
#
#   https://www.quora.com/What-is-the-method-to-construct-a-binary-tree-when-postorder-and-preorder-is-given
#
# --END--


def construct_from_preorder_inorder(preorder, inorder):
    return build_pre_in(preorder, inorder, 0, len(inorder) - 1)


def build_pre_in(preorder, inorder, inorder_lo, inorder_hi):
    if inorder_lo <= inorder_hi:
        val = preorder.pop(0)

        inorder_i = inorder.index(val)
        node = Node(val)

        node.left = build_pre_in(preorder, inorder, inorder_lo, inorder_i - 1)
        node.right = build_pre_in(preorder, inorder, inorder_i + 1, inorder_hi)
        return node


# LEETCODE@ 106. Construct Binary Tree from Inorder and Postorder Traversal
#
# --END--


def construct_from_inorder_postorder(inorder, postorder):
    return build_pre_in(postorder, inorder, 0, len(inorder) - 1)


def build_in_post(postorder, inorder, inorder_lo, inorder_hi):
    if inorder_lo <= inorder_hi:
        val = postorder.pop()

        inorder_i = inorder.index(val)
        node = Node(val)

        node.left = build_in_post(postorder, inorder, inorder_lo, inorder_i - 1)
        node.right = build_in_post(postorder, inorder, inorder_i + 1, inorder_hi)
        return node

