

def num_of_distinct_subarray(nums, k):
    # initialization
    n = len(nums)
    cnt_k = 0
    i, j = 0, 0

    # number of distinct arrays
    res = 0

    # find all sub arrays start from ith
    jj = 0
    for i in range(n):
        jj = max(i, jj)
        j = max(i, j)

        # j goes to right as much as possible
        while j < n:
            if cnt_k < k:
                if nums[j] % 2 == 1:
                    cnt_k += 1
                    if cnt_k == k:
                        jj = j
                j += 1
            elif cnt_k == k:
                if nums[j] % 2 == 1:
                    break
                else:
                    j += 1

        # accumulate
        if cnt_k == k:
            res += j - jj

        # decrease cnt_k if possible
        if nums[i] % 2 == 1:
            cnt_k -= 1

    # return res
    return res


print(num_of_distinct_subarray([2, 4, 6], 0))
print(num_of_distinct_subarray([1, 2, 3, 4], 0))
print(num_of_distinct_subarray([1, 2, 3, 4], 1))
