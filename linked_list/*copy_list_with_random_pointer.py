# LEECODE@ 138. Copy List with Random Pointer
#
# 1) It is the same as LEETCODE 133. Clone Graph
#
# --END--


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copyRandomList(self, head):
    # 1) None must be in the dictionary
    d = {None: None}

    cur = head
    while cur:
        if cur not in d:
            d[cur] = RandomListNode(cur.label)
        if cur.next not in d:
            d[cur.next] = RandomListNode(cur.next.label)
        if cur.random not in d:
            d[cur.random] = RandomListNode(cur.random.label)
        d[cur].next = d[cur.next]
        d[cur].random = d[cur.random]
        cur = cur.next
    return d[head]
