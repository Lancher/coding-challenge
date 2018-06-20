# LEETCODE@ 217. Contains Duplicate
#
# --END--


def containsDuplicate(self, nums):
    st = set()
    for num in nums:
        if num in st:
            return True
        st.add(num)
    return False


# LEETCODE@ 219. Contains Duplicate II
#
# --END--
def containsNearbyDuplicate(self, nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            if i - d[nums[i]] <= k:
                return True
        d[nums[i]] = i
    return False
