# LEETCODE@ 328. Odd Even Linked List
#
# --END--


def oddEvenList(self, head):
    l1, l2 = ListNode(None), ListNode(None)
    n1, n2 = l1, l2

    i = 1
    cur = head
    while cur:
        if i % 2 == 1:
            n1.next = cur
            n1 = n1.next
        else:
            n2.next = cur
            n2 = n2.next
        i += 1
        cur = cur.next
    n1.next = l2.next
    n2.next = None
    return l1.next
