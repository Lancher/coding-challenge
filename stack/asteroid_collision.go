
func Abs(a int) int {
	if a < 0 {return -a}
	return a
}

func asteroidCollision(asteroids []int) []int {
	stack := make([]int, 0)

	n := len(asteroids)
	i := 0

	for i < n {
		a := asteroids[i]
		// skip 0
		if a == 0 { continue }

		// no element in the stack, we just append
		if len(stack) == 0 {
			stack = append(stack, a)
			i += 1
		} else {
			if a < 0 {
				if stack[len(stack)-1] > 0 {
					if Abs(stack[len(stack)-1]) == Abs(a) {
						stack = stack[:len(stack)-1]
						i += 1
					} else if Abs(stack[len(stack)-1]) < Abs(a) {
						stack = stack[:len(stack)-1]
					} else {
						i += 1
					}
				} else {
					i += 1
					stack = append(stack, a)
				}
			} else {
				i += 1
				stack = append(stack, a)
			}
		}
	}
	return stack
}
