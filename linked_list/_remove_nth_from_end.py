# LEETCODE@ 19. Remove Nth Node From End of List
#
# --END--


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(self, head, n):
    dummy = ListNode(None)
    dummy.next = head

    # 1) slow & fast node
    slow = fast = dummy
    for i in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next
