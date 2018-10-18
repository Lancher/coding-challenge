# 198. House Robber
#
# --END--


def rob(self, nums):
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)
    n = len(nums)

    # 1) dp initialization
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        # 2) rob
        dp[i] = max(dp[i], dp[i - 2] + nums[i])
        # 3) not rob
        dp[i] = max(dp[i], dp[i - 1])
    return dp[n - 1]


# 213. House Robber II
#
# --END--


def rob(self, nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    # we cut the circle to into two different types of lines
    # 1) from 1 to n
    # 2) from 0 to n - 1
    return max(self.rob2(nums, 1, len(nums)), self.rob2(nums, 0, len(nums) - 1))


def rob2(self, nums, s, e):
    pre_pre, pre = 0, nums[s]
    for i in range(s + 1, e):
        cur = max(pre_pre + nums[i], pre)
        pre_pre, pre = pre, cur
    return pre



# LEETCODE@ 337	House Robber III

def rob_helper(self, root):
    if root is None:
        return 0, 0
    # left = max value if you include the direct child
    # right = max value if you do not include the direct child
    a, b = self.rob_helper(root.left)
    c, d = self.rob_helper(root.right)
    return max(a + c, root.val + b + d), a + c


def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return max(self.rob_helper(root))

