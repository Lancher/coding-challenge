# LEETCODE@ 2. Add Two Numbers
#
# --END--


def addTwoNumbers(self, l1, l2):
    l3 = ListNode(None)
    n1, n2, n3 = l1, l2, l3
    carry = 0

    # 1) [0] + [0] should be [0]
    while n1 or n2:
        if n1 is None:
            carry += n2.val
            n2 = n2.next
        elif n2 is None:
            carry += n1.val
            n1 = n1.next
        else:
            carry += n1.val + n2.val
            n1, n2 = n1.next, n2.next
        n3.next = ListNode(carry % 10)
        carry = int(carry / 10)
        n3 = n3.next

    if carry:
        n3.next = ListNode(carry)
    return l3.next
