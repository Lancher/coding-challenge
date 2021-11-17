# Questions related to linked list usually need to build dummy node
# in the begining.
#
# --END--


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    # validate
    if not head:
        return None

    # init dummy node
    dummy = ListNode(-1)
    dummy.next = head
    pre, cur, nxt = dummy, head, head.next

    # move the nxt to head
    while nxt:
        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt
        nxt = cur.next

    return dummy.next


# test
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
new_head = reverse(n1)
