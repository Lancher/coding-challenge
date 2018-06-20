# LEETCODE@ 237. Delete Node in a Linked List
#
# --END--


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
