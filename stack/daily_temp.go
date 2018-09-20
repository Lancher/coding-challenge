// LEETCODE@ 739. Daily Temperatures
//
// --END--


package stack


func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	res := make([]int, n, n)
	temp_stack := make([]int, 0)
	idx_stack := make([]int, 0)

	for i, tmp := range(temperatures) {
		// keep decreasing order in the stack
		for len(temp_stack) != 0 && temp_stack[len(temp_stack)-1] < tmp {
			stk_n := len(idx_stack)
			stk_i := idx_stack[stk_n-1]
			res[stk_i] = i - stk_i
			temp_stack = temp_stack[:stk_n-1]
			idx_stack = idx_stack[:stk_n-1]
		}

		temp_stack = append(temp_stack, tmp)
		idx_stack = append(idx_stack, i)
	}

	return res

}