# LEETCODE@ 83. Remove Duplicates from Sorted List
#
# --END--

def deleteDuplicates(self, head):
    cur = head
    while cur:
        if cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


# LEETCODE@ 82. Remove Duplicates from Sorted List II
#
# --END--

def deleteDuplicates(self, head):
    dummy = ListNode(None)
    dummy.next = head
    pre, cur = dummy, head

    while cur:
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        # 1) very clever thought, memorize it!!!!!!
        if pre.next == cur:
            pre = cur
            cur = cur.next
        else:
            pre.next = cur.next
            cur = cur.next
    return dummy.next