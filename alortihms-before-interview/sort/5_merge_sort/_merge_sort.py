"""
1. Implement _merge(), _sort() and sort()

2. Get the middle element:

    lo            mi                  hi
  [ 10 ] [ 12 ] [ 7 ] [ 11 ] [ 19 ] [ 32 ]

    lo            mi           hi
  [ 10 ] [ 12 ] [ 7 ] [ 11 ] [ 19 ]

3. The index of mi & hi should be excluded.

--END--
"""


class MergeSort:
    def _merge(self, nums, aux, lo, mi, hi):
        # copy to the aux array
        aux[lo:hi] = nums[lo:hi]

        i, j = lo, mi

        # merge the two array
        for k in range(lo, hi):
            # i is reaching the end
            if i >= mi:
                nums[k] = aux[j]
                j += 1
            # j is reaching the end
            elif j >= hi:
                nums[j] = aux[i]
                i += 1
            # i < j
            elif aux[i] < aux[j]:
                nums[k] = aux[i]
                i += 1
            # j < i
            else:
                nums[k] = aux[j]
                j += 1

    def _sort(self, nums, aux, lo, hi):
        # make sure we can not work on only 1 element
        if lo < hi - 1:
            mi = (lo + hi) / 2
            self._sort(nums, aux, lo, mi)
            self._sort(nums, aux, mi, hi)
            self._merge(nums, aux, lo, mi, hi)

    def sort(self, nums):
        aux = nums[:]
        self._sort(nums, aux, 0, len(nums))
