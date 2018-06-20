# LEETCODE@ 86. Partition List
#
# 1) Use two list to preserve two different value.
#
# --END--


def partition(self, head, x):
    l1, l2 = ListNode(None), ListNode(None)
    n1, n2 = l1, l2
    cur = head

    while cur:
        if cur.val < x:
            n1.next = cur
            n1 = n1.next
        else:
            n2.next = cur
            n2 = n2.next
        cur = cur.next
    n1.next = l2.next
    # 1) n2.next should be none to avoid the loop
    n2.next = None
    return l1.next
