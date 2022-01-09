"""
1. https://www.geeksforgeeks.org/counting-sort/

2. counter length should be `mx - mn + 1`.

  [1, 100] => [0, 1, .... 99] so it will be `100 - 99 + 1`

--END--
"""


def count_sort(nums):
    # find min & max
    mn, mx = min(nums), max(nums)
    counter = [0] * (mx - mn + 1)

    # count each elements
    for num in nums:
        counter[num-mn] += 1

    # build the new res array
    res = []
    for i in range(len(counter)):
        if counter[i]:
            res += [i+mn] * counter[i]

    return res


print(count_sort([100, 1, 100, 2, 33, 87]))
