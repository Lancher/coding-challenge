# LEETCODE@ 55. Jump Game
#
# 1) DP with O(n^2).
#
# 2) linear time with remember the ending point.
#
# --END--


def canJump(self, nums):
    n = len(nums)

    # 1) dp initialization, dp means can we reach here?
    dp = [0] * n
    dp[0] = 1

    for i in range(len(nums)):
        if dp[i]:
            for j in range(nums[i]):
                if i + j + 1 < len(nums):
                    dp[i + j + 1] = 1
        else:
            return False
    return True


def canJump(self, nums):
    n = len(nums)
    i, end = 0, 1

    while i < end and i < n:
        end = max(end, i + nums[i] + 1)
        i += 1
        print(i, end)
    return n <= end
