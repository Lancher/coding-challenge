// LEETCODE@ 740. Delete and Earn
//
// --END--


package dp


func deleteAndEarn(nums []int) int {
	// build sum array
	sum := make([]int, 10001)
	for _, num := range(nums) {
		sum[num] += num
	}

	// dp
	take, skip := 0, 0
	for i := 0; i < 10001; i++ {
		nxt_take, nxt_skip := skip + sum[i], 0
		if take > skip {
			nxt_skip = take
		} else {
			nxt_skip = skip
		}
		take, skip = nxt_take, nxt_skip
	}

	if take > skip {
		return take
	} else {
		return skip
	}
}