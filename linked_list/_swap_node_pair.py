# LEETCODE@ 24. Swap Nodes in Pairs
#
# --END--


def swapPairs(self, head):
    dummy = ListNode(None)
    dummy.next = head
    pre, cur, move = dummy, None, None

    while pre.next and pre.next.next:
        cur, move = pre.next, pre.next.next
        cur.next = move.next
        move.next = cur
        pre.next = move
        # 1) Remember to update here
        pre = cur
    return dummy.next
