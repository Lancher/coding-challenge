"""
1. Create a max heap, Pop heap one by one, Push to the end

2. The time complexity is O(nlogn)

3. Example:


         0[ 23 ]
         /     \
        /       \
    1[ 8 ]    2[ 6 ]
       /
      /
   3[ 2 ]               <= swap (23) with (2) and then sink (2),
                           and so on...

--END--
"""


class HeapSort:

    def _make_heap(self, nums):
        for i in range(int(len(nums) / 2), -1, -1):
            self._sink(nums, len(nums), i)

    def _sink(self, nums, n, i):
        j = i * 2 + 1
        while j < n:
            if j + 1 < n and nums[j+1] > nums[j]:
                j += 1
            if nums[i] > nums[j]:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i, j = j, j * 2 + 1

    def sort(self, nums):
        self._make_heap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._sink(nums, i, 0)
