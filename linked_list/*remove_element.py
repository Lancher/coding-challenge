# LEETCODE@ 203. Remove Linked List Elements
#
# --END--


def removeElements(self, head, val):
    pre_head = ListNode(-1)
    pre_head.next = head

    pre_n, n = pre_head, head
    while n:
        if n.val == val:
            pre_n.next = n.next
            n = n.next
        else:
            pre_n = pre_n.next
            n = n.next
    return pre_head.next
