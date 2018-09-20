# LEETCODE@ 691. Stickers to Spell Word
#
# --END--


_MAX = float('inf')


def minStickers(self, stickers, target):
    n = len(stickers)
    stick_chs = [[0] * 26 for i in range(n)]
    for i in range(n):
        for j in range(len(stickers[i])):
            stick_chs[i][ord(stickers[i][j]) - ord('a')] += 1

    # dp[s] is the minimum stickers required for string s (-1 if impossible).
    dp = {}
    dp[""] = 0

    def helper(dp, stick_chs, target):
        if target in dp:
            return dp[target]

        n = len(stick_chs)

        # count characters in target
        tar_chs = [0] * 26
        for c in target:
            tar_chs[ord(c) - ord('a')] += 1

            # number minimum stickers
        res = _MAX
        for i in range(n):
            if stick_chs[i][ord(target[0]) - ord('a')] == 0:
                continue

            # build a temp deducted string for this sticker
            s = ''
            for j in range(26):
                if tar_chs[j] > stick_chs[i][j]:
                    s += chr(ord('a') + j) * (tar_chs[j] - stick_chs[i][j])
            stick_num = helper(dp, stick_chs, s)
            res = min(res, 1 + stick_num)

            # update current string's
        dp[target] = res
        return dp[target]

    res = helper(dp, stick_chs, target)
    return -1 if res == _MAX else res
