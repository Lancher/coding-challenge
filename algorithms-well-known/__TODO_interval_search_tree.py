# Steps:
# 1) Store pair(low, high), and use low as key.
# 2) Use high_max to record the max high in self and subtree.
# 3) If left.max < node.low go left else go right.
#
# rectangle: https://www.youtube.com/watch?v=LQ-vRetWnu4&list=PLxc4gS-_A5VDXUIOPkJkwQKYiT2T1t0I8&index=51
#
# --END--


class Node:
    def __init__(self, interval):
        self.interval = interval[:]
        self.interval_max = interval[1]
        self.left = self.right = None


class IntervalTree:

    def __init__(self):
        self.root = None

    def put(self, interval):
        self.root = self._put(self.root, interval)

    def _put(self, node, interval):
        if node is None:
            return Node(interval)
        elif interval[0] < node.interval[0]:
            node.left = self._put(node.left, interval)
        else:
            node.right = self._put(node.right, interval)
        node.interval_max = max(node.interval[1], interval[1])
        return node

    def search_overlap_interval(self, interval):
        return self._search_overlap_interval(self.root, interval)

    def _search_overlap_interval(self, node, interval):
        if node is None:
            return None
        if self._is_overlap(node.interval, interval):
            return node.interval
        if node.left and interval[0] < node.left.interval_max:
            return self._search_overlap_interval(node.left, interval)
        else:
            return self._search_overlap_interval(node.right, interval)

    def _is_overlap(self, interval1, interval2):
        return interval1[0] < interval2[1] and interval2[0] < interval1[1]


t = IntervalTree()
t.put([17, 19])
t.put([5, 8])
t.put([21, 24])
t.put([4, 8])
t.put([15, 18])
t.put([7, 10])
print(t.search_overlap_interval([23, 25]))
print(t.search_overlap_interval([12, 14]))
