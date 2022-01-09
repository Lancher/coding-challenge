"""
1. unsorted array select index k element, time complexity average O(n)

2. Partition:

  i,j               hi      i  j            hi
  [19, 3, 2, 37, 5, 8] => [19, 3, 2, 37, 5, 8]

         i,j           hi        i   j         hi
  => [3, 19, 2, 37, 5, 8] => [3, 19, 2, 37, 5, 8]

           ***here we swap i and j and increment i***

--END--
"""


from random import randint


class QuickSelect:

    def _shuffle(self, nums):
        for i in range(len(nums)):
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]

    def _partition(self, nums, lo, hi):
        i = lo
        for j in range(lo, hi):
            if nums[j] < nums[hi]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i

    def select(self, nums, k):
        lo, hi = 0, len(nums) - 1
        while True:
            # P can be the same as lo and hi which will cause while loop
            p = self._partition(nums, lo, hi)
            if p == k:
                return nums[p]
            elif p < k:
                # P can be the same as lo and hi which will cause while loop
                lo = p + 1
            else:
                # P can be the same as lo and hi which will cause while loop
                hi = p - 1


qs = QuickSelect()
qs.select([1, 1, 1, 1], 2)
