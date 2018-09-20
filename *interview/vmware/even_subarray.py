import os


def num_of_distinct_subarray(nums, k):
    # initialization
    n = len(nums)
    cnt_k = 0
    i, j = 0, 0

    # number of distinct arrays
    res = 0

    # find all sub arrays start from ith
    for i in range(n):

        # j goes to right as much as possible
        while j < n:
            if cnt_k < k:
                if nums[j] % 2 == 1:
                    cnt_k += 1
                j += 1
            elif cnt_k == k:
                if nums[j] % 2 == 1:
                    break
                else:
                    j += 1

        # accumulate
        res += j - i

        # decrease cnt_k if possible
        if nums[i] % 2 == 1:
            cnt_k -= 1

    # build suffix array
    suffix_array = []
    for i in range(n):
        suffix_array.append(nums[i:])
    suffix_array.sort()

    # find lcp and minus the duplicate items
    for i in range(n - 1):
        cnt_k = 0
        prefix_len = 0
        for j in range(min(len(suffix_array[i]), len(suffix_array[i+1]))):
            # the length of prefix_len = min(prefix_len, the length of longest string containing at most k)
            if suffix_array[i][j] == suffix_array[i+1][j]:
                if suffix_array[i][j] % 2 == 1:
                    if cnt_k < k:
                        cnt_k += 1
                    elif cnt_k == k:
                        break
                prefix_len += 1
            else:
                break
        res -= prefix_len

    # return res
    return res


import collections


def odd_subarray1(nums, k):

    dp = [0] * (len(nums)+1)
    dic = collections.defaultdict(list)
    ans = set()

    for i in range(1,len(nums)+1):
        # check if is odd
        if i == 0:
            dp[i] = nums[i-1] % 2
        else:
            dp[i] = dp[i-1] + nums[i-1] % 2
        dic[dp[i]].append(i)

        for j in range(max(0, dp[i]-k), dp[i]+1): # check for dp[i]-k ~ dp[i]
            if j in dic:
                for num in dic[j]:
                    if dp[i] - dp[max(0,num-1)] <= k:
                        temp = nums[num-1:i]
                        ans.add(tuple(temp))
    print(ans)
    return len(ans)


def odd_subarray2(nums, k):
    dp = [0] * len(nums)
    ans = set()

    for i in range(0,len(nums)):
        if i == 0:
            dp[i] =  nums[i] % 2
        else:
            dp[i] = dp[i-1] + nums[i] % 2

        for j in range(0, i+1):
            if j==0:
                num_odd = dp[i]
            else:
                num_odd = dp[i]- dp[j-1]
            if num_odd <= k :
                ans.add(tuple(nums[j:i+1]))
    return len(ans)


import random
import time

nums = [random.randint(0, 250) for i in range(1000)]
nums = [1, 1, 1, 1]

# solution 1
start = time.time()
print('Ans:', num_of_distinct_subarray(nums, 1))
done = time.time()
elapsed = done - start
print('Time', elapsed)
print()

# solution 2
start = time.time()
print('Ans:', odd_subarray1(nums, 1))
done = time.time()
elapsed = done - start
print('Time', elapsed)
