# LEETCODE@ 160. Intersection of Two Linked Lists
#
# 1) we need to walk the same length
#
#   A:          a1 → a2
#                      ↘
#                       c1 → c2 → c3
#                     ↗
#   B:     b1 → b2 → b3
#
# --END--


def getIntersectionNode(self, headA, headB):
    n1, n2 = headA, headB

    while n1 != n2:
        n1 = headB if n1 is None else n1.next
        n2 = headA if n2 is None else n2.next
    # 1) [1, 2, 3] []
    #    n1 will be None
    return n1
