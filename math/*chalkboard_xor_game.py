# LEETCODE@ 810. Chalkboard XOR Game
#
# 1) If xor == 0, Alice win directly.
#
# 2) If xor != 0 and length of numbers is even, Alice will win.
#
# --END--


def xorGame(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res == 0 or len(nums) % 2 == 0
