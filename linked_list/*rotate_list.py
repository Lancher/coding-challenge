# LEETCODE@ 61. Rotate List
#
# 1) Example: 1->2->3->4->5->NULL and k = 2
#    Result:  4->5->1->2->3->NULL.
#
# --END--


def rotateRight(self, head, k):
    if not head:
        return head

    n = 1
    # 1) build the circle
    cur = head
    while cur.next:
        cur = cur.next
        n += 1
    cur.next = head

    # 2) cut the circle
    k = n - k % n
    for i in range(k):
        cur = cur.next
    head = cur.next
    cur.next = None
    return head