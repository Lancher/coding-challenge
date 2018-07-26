# LEETCODE@ 460	LFU Cache
#
# --END--


from collections import defaultdict
from collections import OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.length = 0
        self.capacity = capacity
        self.min_cnt = 0
        self.cnt = {}
        self.val = {}
        self.lists = defaultdict(OrderedDict)

    def get(self, key):
        if key not in self.val:
            return -1

        # update the key counter
        self.lists[self.cnt[key]].pop(key)
        self.cnt[key] += 1
        self.lists[self.cnt[key]][key] = None

        # update minimum count
        if self.min_cnt == self.cnt[key] - 1 and len(self.lists[self.cnt[key] - 1]) == 0:
            self.min_cnt += 1

        return self.val[key]

    def put(self, key, value):
        if key in self.val:
            self.val[key] = value
            self.get(key)
        else:
            if self.capacity == 0:
                return

            # find the least used and remove it
            if self.length + 1 > self.capacity:
                first = self.lists[self.min_cnt].popitem(last=False)
                self.val.pop(first[0])
                self.cnt.pop(first[0])
            else:
                self.length += 1

            self.val[key] = value
            self.cnt[key] = 1
            self.min_cnt = 1
            self.lists[1][key] = None
