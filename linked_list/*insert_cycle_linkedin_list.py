# LEETCODE@ 708. Insert into a Cyclic Sorted List
#
# --END--


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def insert(self, head, insertVal):
    if head is None:
        node = Node(insertVal, None)
        return node

    cur, nxt = head, head.next
    node = Node(insertVal, None)
    stop = None

    while nxt != stop:
        if cur.val <= nxt.val:
            if cur.val <= insertVal <= nxt.val:
                node.next = nxt
                cur.next = node
                return head
        else:
            if insertVal < nxt.val:
                node.next = nxt
                cur.next = node
                return head
            if insertVal > cur.val:
                node.next = nxt
                cur.next = node
                return head
        if stop is None:
            stop = nxt
        cur, nxt = cur.next, nxt.next

    node = Node(insertVal, None)
    node.next = nxt
    cur.next = node
    return head