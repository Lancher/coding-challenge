"""
1. Quick sort, average time complexity is O(nlogn)

3. `hi` include value

2. Partition:

  i,j               hi      i  j            hi
  [19, 3, 2, 37, 5, 8] => [19, 3, 2, 37, 5, 8]

         i,j           hi        i   j         hi
  => [3, 19, 2, 37, 5, 8] => [3, 19, 2, 37, 5, 8]

           ***here we swap i and j and increment i***

--END--
"""
from random import randint


class QuickSort:

    def _suffle(self, nums):
        for i in range(len(nums)):
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]

    def _sort(self, nums, lo, hi):
        if lo < hi:

            # partition, select index `hi` as pivot point
            i = lo
            for j in range(lo, hi):
                if nums[j] < nums[hi]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]

            # sort
            self._sort(nums, lo, i - 1)
            self._sort(nums, i + 1, hi)

    def sort(self, nums):
        self._suffle(nums)
        self._sort(nums, 0, len(nums) - 1)


# 1. Quick sort, average time complexity is O(nlogn)
#
# 3. `hi` include value
#
# 2. Partition:
#
#    lt                gt
#     i
#   [10, 3, 17, 10, 5, 11]
#
#
#    lt                gt
#        i
#   [10, 3, 17, 10, 5, 11]      if 3 < lt,swap and i++ & lt++
#
#
#       lt             gt
#           i
#   [3, 10, 17, 10, 5, 11]      if 17 > lt, swap and gt--
#
#
#       lt          gt
#           i
#   [3, 10, 11, 10, 5, 17]      if 11 > lt, swap and gt--
#
#
#       lt     gt
#           i
#   [3, 10, 5, 10, 11, 17]      if 5 < 10, swap and i++ & lt++
#
#
#          lt  gt
#               i
#   [3, 5, 10, 10, 11, 17]  check gt, we end the loop
#
#
# --END--
class QuickSortWithDup:

    def _shuffle(self, nums):
        for i in range(len(nums)):
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]

    def _sort(self, nums, lo, hi):
        if lo < hi:

            # partition
            lt, gt = lo, hi
            i = lo
            while i <= gt:
                if nums[i] < nums[lt]:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > nums[lt]:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # sort
            self._sort(nums, lo, lt - 1)
            self._sort(nums, gt + 1, hi)

    def sort(self, nums):
        self._shuffle(nums)
        self._sort(nums, 0, len(nums) - 1)
