# LEETCODE@ 234. Palindrome Linked List
#
# --END--


def isPalindrome(self, head):
    if not head or not head.next:
        return True

    dummy = ListNode(None)
    dummy.next = head

    slow = fast = dummy
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    pre, cur, move = slow, slow.next, slow.next.next
    while move:
        cur.next = move.next
        move.next = pre.next
        pre.next = move
        move = cur.next

    n1, n2 = dummy.next, slow.next
    while n1 != slow.next:
        if n1.val != n2.val:
            return False
        n1 = n1.next
        n2 = n2.next
    return True

