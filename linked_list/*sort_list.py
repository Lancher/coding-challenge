# LEETCODE@ 147. Insertion Sort List
#
# --END--


def insertionSortList(self, head):
    dummy = ListNode(float('-inf'))
    dummy.next = head

    pre, cur = dummy, head
    while cur:
        ins = dummy
        while ins.next != cur:
            if ins.val <= cur.val < ins.next.val:
                pre.next = cur.next
                cur.next = ins.next
                ins.next = cur
                # 1) cur is move to the front
                pre, cur = pre, pre.next
                break
            ins = ins.next
        else:
            # 2) cur is still here, forward the two nodes
            pre, cur = pre.next, cur.next
    return dummy.next


# LEETCODE@ 148. Sort List
#
# --END--


def sortList(self, head):
    return self.sort(head)


def sort(self, node):
    if node is None or node.next is None:
        return node
    # 1) find the midddle point
    dummy = ListNode(None)
    dummy.next = node
    slow = fast = dummy
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2) cut the list into two list
    l1 = dummy.next
    l2 = slow.next
    slow.next = None

    # 3) sort each list
    l1 = self.sort(l1)
    l2 = self.sort(l2)

    # 4) merge two list, return head
    return self.merge(l1, l2)


def merge(self, l1, l2):
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
