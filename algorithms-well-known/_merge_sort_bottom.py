# 1. Implement _merge(), _sort() and sort()
#
# 2. Bottom Up Flow:
#
#    sz = 1
#   |-----|-----| |-----|-----| |-----|-----|
#   [ 10 ] [ 12 ] [ 70 ] [ 11 ] [ 19 ] [ 32 ]

#    sz = 2
#   |------------|------------| |------------|------------| <- this should not run because
#   [ 10 ] [ 12 ] [ 11 ] [ 70 ] [ 19 ] [ 32 ]                  only have two element, we need
#                                                              two part to merge
#    sz = 4
#   |--------------------------|--------------------------| <- take care the second part
#   [ 10 ] [ 12 ] [ 11 ] [ 70 ] [ 19 ] [ 32 ]
#
#    sz = 8 break
# 
# 3. The index of mi & hi should be excluded.
#
#
# --END--


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

    def sort(self, nums):
        aux = nums[:]
        sz = 1
        while sz < len(nums):
            for lo in range(0, len(nums), sz * 2):
                # make sure the first part exist, so we can do the merge.
                if lo + sz < len(nums):
                    self._merge(nums, aux, lo, lo + sz, min(lo + sz * 2, len(nums)))
            sz *= 2
