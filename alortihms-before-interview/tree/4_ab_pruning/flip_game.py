"""
AB Pruning

Two players will try their best to win.

-- END --
"""


class Solution:
    def canWin(self, s: str) -> bool:
        cache = {}
        reward = self.first(s, cache)
        return reward == 1

    def first(self, s, cache):
        state = ('1', s)
        if state in cache:
            return cache[state]

        # Try player 1's best to win.
        for i in range(len(s) - 1):
            if s[i] == s[i+1] == '+':
                if self.second(s[:i] + '--' + s[i+2:], cache) == -1:
                    cache[state] = 1
                    return 1

        # means we can not flip anymore
        cache[state] = -1
        return -1


    def second(self, s, cache):
        state = ('2', s)
        if state in cache:
            return cache[state]

        # Try player 2's best to win.
        for i in range(len(s) - 1):
            if s[i] == s[i+1] == '+':
                if self.first(s[:i] + '--' + s[i+2:], cache) == -1:
                    cache[state] = 1
                    return 1

        # means we can not flip anymore
        cache[state] = -1
        return -1

print('Can player1 win?', Solution().canWin('++++'))
