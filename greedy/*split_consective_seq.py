# LEETCODE@ 659. Split Array into Consecutive Subsequences
#
# --END--


def isPossible(self, nums):
    nums.sort()
    d = collections.defaultdict(list)
    d[nums[0]].append(1)

    for i in range(1, len(nums)):
        # found where it needs to go
        if nums[i] - 1 in d:
            seq_len = d[nums[i] - 1].pop(0)
            if len(d[nums[i] - 1]) == 0:
                d.pop(nums[i] - 1)
            d[nums[i]].append(seq_len + 1)
            d[nums[i]].sort()
        else:
            # make a new entry
            d[nums[i]].append(1)
            d[nums[i]].sort()

    for k,v in d.items():
        for lenn in v:
            if lenn < 3 and lenn != 0:
                return False
    return True
