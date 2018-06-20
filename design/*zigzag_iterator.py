# LEETCODE@ 281. Zigzag Iterator
#
#
# --END--


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.ll = [v1, v2]
        self.i = 0
        self.js = [0, 0]
        self.nxt = None

    def next(self):
        return self.nxt

    def hasNext(self):
        for _ in range(len(self.ll)):
            if self.js[self.i % 2] < len(self.ll[self.i % 2]):
                self.nxt = self.ll[self.i % 2][self.js[self.i % 2]]
                self.js[self.i % 2] += 1
                self.i += 1
                return True
            else:
                self.i += 1
        else:
            return False
