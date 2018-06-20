# LEETCODE@ 23. Merge k Sorted Lists
#
#
# --END--


import heapq


def mergeKLists(self, lists):
    h = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, [lists[i].val, lists[i]])

    head = tail = ListNode(None)
    while h:
        _, node = heapq.heappop(h)
        tail.next = node
        tail = tail.next
        node = node.next
        if node:
            heapq.heappush(h, [node.val, node])
    return head.next
