# LEETCODE@ 141. Linked List Cycle
#
# --END--


def hasCycle(self, head):
    slow = fast = head
    # 1) check `fast` and `fast.next` is indeed important
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# LEETCODE@ 142. Linked List Cycle II
#
# --END--


def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    else:
        return None

    while head != slow:
        slow = slow.next
        head = head.next
    return slow
