
# It may become quite difficult to use sliding window, as the elements of the array are not all positives, so, making
# end increase doesn't mean the sum increase, and making start doesn't mean the sum decrease.


def sub_sum_eq_k(nums, k):
    # init
    n = len(nums)

    # iterate the array
    res = 0
    st = 0
    sm = 0
    for ed in range(n):
        sm += nums[ed]

        while k < sm:
            sm -= nums[st]
            st += 1

        if sm == k:
            res += 1

    return res


print(sub_sum_eq_k([1, 1, 1, 1, 1, 1], 3))
