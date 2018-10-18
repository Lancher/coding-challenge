

def max_subarr_with_k(nums, k):
    if len(nums) < k:
        return -1

    # init
    n = len(nums)
    sm = sum(nums[:k])
    res = sm

    # slide the window
    for i in range(k, n):
        sm += nums[i] - nums[i-k]
        res = max(res, sm)

    return res


print(max_subarr_with_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))


def max_subarr_with_at_least_k(nums, k):
    # init
    n = len(nums)
    max_so_far = [0] * n
    max_so_far[0] = nums[0]
    max_so_far_i = [i for i in range(n)]

    # find max subarray
    cur_max = nums[0]
    cur_max_i = 0
    for i in range(1, n):
        if nums[i] < nums[i] + cur_max:
            cur_max = nums[i] + cur_max
            max_so_far_i[i] = cur_max_i
        else:
            cur_max = nums[i]
            cur_max_i = i
            max_so_far_i[i] = cur_max_i
        max_so_far[i] = cur_max

    # slide the window
    sm = sum(nums[:k])
    res = sm
    st, ed = 0, k - 1
    for i in range(k, n):
        sm += nums[i] - nums[i-k]
        if res < sm:
            res = sm
            st, ed = i - k + 1, i
        if res < sm + max_so_far[i-k]:
            res = sm + max_so_far[i-k]
            st, ed = max_so_far_i[i-k], i

    # return answer
    print(nums[st:ed+1])
    return res


print(max_subarr_with_at_least_k([1, 4, 2, 10, 23, 3, -10], 4))


