# LEETCODE@ 679. 24 Game
#
# --END--


def judgePoint24(self, nums):
    res = [False]
    self.backtracing(nums, len(nums), 0.0001, res)
    return res[0]


def backtracing(self, nums, ln, eps, res):
    if res[0]:
        return
    if ln == 1:
        if abs(nums[-1] - 24) < eps:
            res[0] = True
        return
    for i in range(len(nums)):
        if nums[i] is None:
            continue
        for j in range(i):
            if nums[j] is None:
                continue
            # pick two elements and perform one of the operations +, -, * /
            v1, v2 = nums[i], nums[j]
            nxt = [v1 + v2, v1 - v2, v2 - v1, v1 * v2]
            if v2 > eps:  # TODO: why?
                nxt.append(v1 / v2)
            if v1 > eps:
                nxt.append(v2 / v1)

            nums[i] = nums[j] = None
            for v in nxt:
                nums.append(v)
                self.backtracing(nums, ln - 2 + 1, eps, res)
                nums.pop()
            nums[i], nums[j] = v1, v2
