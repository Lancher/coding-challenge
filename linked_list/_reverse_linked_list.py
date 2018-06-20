# LEETCODE@ 206. Reverse Linked List
#
# --END--


def reverseList(self, head):
    if head is None:
        return head

    # 1) build dummy head
    dummy = ListNode(None)
    dummy.next = head

    # 2) for reversing the linked list, use `pre`, `cur` and `move`
    pre, cur, move = dummy, dummy.next, dummy.next.next
    while move:
        cur.next = move.next
        move.next = pre.next
        pre.next = move
        move = cur.next
    return dummy.next
