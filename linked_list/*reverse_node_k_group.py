# LEETCODE@ 25. Reverse Nodes in k-Group
#
# --END--


def reverseKGroup(self, head, k):
    if k < 2:
        return head
    # 1) when dealing with reverse, use `pre`, `cur`, `move`to setup the nodes
    dummy = ListNode(None)
    dummy.next = head

    # 2) init prev to dummy
    pre, cur, move = dummy, None, None
    while pre.next:
        cur, move = pre.next, pre.next.next
        for i in range(k - 1):
            # 3) reverse the unfilled part
            if move is None:
                cur, move = pre.next, pre.next.next
                while move:
                    cur.next = move.next
                    move.next = pre.next
                    pre.next = move
                    move = cur.next
                return dummy.next
            # 4) remember the steps of reversing
            cur.next = move.next
            move.next = pre.next
            pre.next = move
            move = cur.next
        pre = cur
    return dummy.next
