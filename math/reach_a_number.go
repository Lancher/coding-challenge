// LEETCODE@ 754. Reach a Number
//
// e.g. for target == 4, take 3 steps 1, 2, 3 arriving at 6. since 6 - 4 = 2,
// if you reverse the 2/2 == 1st step you arrive at 4.
//
// another example target == 5, take 5 steps, 1,2,3,4,5 arriving at 15, difference is 10.
// you reverse the 10/2 = 5th step -> 1+2+3+4-5 = 5.
//
// the greedy approach is actually just a few lines of code which feels like an easy. The
// hard part is seeing there's an greedy solution.
//
// --END--



package math

import "fmt"

func reachNumber(target int) int {
	if target == 0 { return 0 }
	if target < 0 { target = -target }

	num := 0
	step := 1

	// exceed the target
	for num < target {
		num += step
		step += 1
	}
	fmt.Println(step)

	// check if can be reverse
	for (num - target) % 2 == 1 {
		num += step
		step += 1
	}

	return step - 1
}