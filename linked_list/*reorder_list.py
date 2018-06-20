# LEETCODE@ 143. Reorder List
#
# 1) How to find middle point in linked list?
#
# s,f
#     [1, 2, 3, 4]
#
#      s  f
#     [1, 2, 3, 4]
#
#         s     f
#     [1, 2, 3, 4]
#
# s,f
#     [1, 2, 3, 4, 5]
#
#      s  f
#     [1, 2, 3, 4, 5]
#
#         s     f
#     [1, 2, 3, 4, 5]
#
# 2) How to find middle point in linked list?
#
#     s,f
#     [1, 2, 3, 4]
#
#         s     f
#     [1, 2, 3, 4]
#
#     s,f
#     [1, 2, 3, 4, 5]
#
#         s  f
#     [1, 2, 3, 4, 5]
#
#            s     f
#     [1, 2, 3, 4, 5]
#
# We can get a conclusion that if `f.next is None or f.next.next is None`, then break.
#
# 2)
#
# --END--


def reorderList(self, head):
    if not head:
        return head

    dummy = ListNode(None)
    dummy.next = head

    # 1) find the middle one
    slow = fast = dummy
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2) reverse the last half part
    pre, cur, move = slow, slow.next, None
    while cur.next:
        move = cur.next
        cur.next = move.next
        move.next = pre.next
        pre.next = move
        move = cur.next

    # 3) n1 & n1.next to make sure we still have elements to pair
    n1 = dummy.next
    while n1 and n1.next:
        n2 = slow.next
        slow.next = n2.next
        n2.next = n1.next
        n1.next = n2
        n1 = n2.next
