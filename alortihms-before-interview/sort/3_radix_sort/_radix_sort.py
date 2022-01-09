"""
1. use `counting_sort()` to implement radix sort.

2. Example:

  [100, 200, 300, 1000, 2000, 2, 3, 1]

  0: 100, 200, 300, 1000, 2000 => 5
  1: 1                         => 6
  2: 2                         => 7
  3: 3                         => 8

                            <---------

  [100, 200, 300, 1000, 2000, 1, 2, 3]

--END--
"""


def counting_sort(nums, div):
    # count by digits
    counter = [0] * len(nums)
    for i in range(len(nums)):
        idx = int(nums[i] / div) % 10
        counter[idx] += 1

    # accumulate the counter
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]

    tmp = [0] * len(nums)
    # from the tail to the head, since counter decrement
    for i in range(len(nums) - 1, -1, -1):
        idx = int(nums[i] / div) % 10
        tmp[counter[idx]-1] = nums[i]
        counter[idx] -= 1
    nums[:] = tmp[:]


def radix_sort(nums):
    mx = max(nums)
    div = 1
    while int(mx / div):
        counting_sort(nums, div)
        print(nums)
        div *= 10


nums = [100, 200, 300, 1000, 2000, 2, 3, 1]
radix_sort(nums)
print(nums)
