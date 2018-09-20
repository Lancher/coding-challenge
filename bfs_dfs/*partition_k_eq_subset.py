# LEETCODE@ 698. Partition to K Equal Sum Subsets
#
# --END--


def canPartitionKSubsets(self, nums, k):
    # this is np-hard problem.

    # init
    n = len(nums)
    avg = int(sum(nums) / k)
    vst = [0] * n
    res = [False]

    self.dfs(nums, k, vst, avg, 0, res)
    return res[0]


def dfs(self, nums, k, vst, avg, cur_sum, res):
    if res[0]:
        return
    if k == 0:
        res[0] = True
        return
    if cur_sum == avg:
        self.dfs(nums, k - 1, vst, avg, 0, res)
    elif cur_sum < avg:
        for i in range(len(nums)):
            if not vst[i]:
                vst[i] = 1
                self.dfs(nums, k, vst, avg, cur_sum + nums[i], res)
                vst[i] = 0
