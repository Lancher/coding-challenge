# LEETCODE@ 710. Random Pick with Blacklist
#
# --END--


import random


class Solution:
    def __init__(self, N, blacklist):
        self.d = {}
        self.n = N - len(blacklist)
        print(self.n)

        for num in blacklist:
            self.d[num] = -1

        N -= 1
        for num in blacklist:
            if num < self.n:
                while N in self.d:
                    N -= 1
                self.d[num] = N
                N -= 1
        print(self.d)

    def pick(self):
        i = random.randint(0, self.n - 1)
        return self.d[i] if i in self.d else i
