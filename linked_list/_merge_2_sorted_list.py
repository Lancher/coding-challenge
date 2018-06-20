# LEETCODE@ 21. Merge Two Sorted Lists
#
# --END--


def mergeTwoLists(l1, l2):
    l3 = ListNode(None)
    n1, n2, n3 = l1, l2, l3
    while n1 or n2:
        if n1 is None:
            n3.next = n2
            n2, n3 = n2.next, n3.next
        elif n2 is None:
            n3.next = n1
            n1, n3 = n1.next, n3.next
        elif n1.val < n2.val:
            n3.next = n1
            n1, n3 = n1.next, n3.next
        else:
            n3.next = n2
            n2, n3 = n2.next, n3.next
    return l3.next
