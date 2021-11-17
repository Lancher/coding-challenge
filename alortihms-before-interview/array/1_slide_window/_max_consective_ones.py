# Slide Window
#
# Q. Max Consecutive Ones II
#    Given a binary array nums, return the maximum number of consecutive 1's
#    in the array if you can flip at most one 0.
#
#    nums = [1,0,1,1,0], flip = 1
#
#    Keep the lo, hi indexes, number of flips and zeros we currently have.
#
# --END--

def solution(nums, flip):
    # init
    n = len(nums)

    lo = 0
    zero = 0
    res = 0

    for hi in range(n):
        if nums[hi] == 0:
            zero += 1

        # move the lo index forward
        while flip < zero:
            if nums[lo] == 0:
                zero -= 1
            lo += 1

        # calc our max length
        res = max(res, hi - lo + 1)

    assert res == 4


solution([1,0,1,1,0], 1)
