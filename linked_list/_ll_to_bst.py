# LEETCODE@ 109. Convert Sorted List to Binary Search Tree
#
# --END--


def sortedListToBST(self, head):
    return self.bst(head, None)


def bst(self, head, tail):
    if head == tail:
        return None

    slow = fast = head
    while fast != tail and fast.next != tail:
        slow = slow.next
        fast = fast.next.next

    node = TreeNode(slow.val)
    node.left = self.bst(head, slow)
    node.right = self.bst(slow.next, tail)
    return node
