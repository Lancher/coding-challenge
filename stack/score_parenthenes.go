// LEETCODE@ 856. Score of Parentheses
//
// --END--


package stack


func scoreOfParentheses(S string) int {
	stack := make([]int, 0)

	for i := 0; i < len(S); i++ {
		if S[i] == '(' {
			// delimeter is important in stack, we can know where to stop
			stack = append(stack, -1)
		} else {
			cur := 0

			for 0 < len(stack) && stack[len(stack)-1] != -1 {
				cur += stack[len(stack)-1]
				stack = stack[:len(stack)-1]
			}
			stack = stack[:len(stack)-1]

			if cur == 0 {
				stack = append(stack, 1)
			} else {
				stack = append(stack, cur * 2)
			}
		}
	}

	res := 0
	for i := 0; i < len(stack); i++ {
		res += stack[i]
	}
	return res
}