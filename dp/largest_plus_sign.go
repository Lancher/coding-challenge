package dp

import "sort"

func orderOfLargestPlusSign(N int, mines [][]int) int {
	// not valid map
	if N == 0 { return 0 }

	// init
	n := N

	// build map
	m := make([][]int, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ { m[i] = append(m[i], 1) }
	}

	// put mines
	for _, mine := range(mines) {
		m[mine[0]][mine[1]] = 0
	}

	// from left, right top, down
	left := make([][]int, n)
	right := make([][]int, n)
	top := make([][]int, n)
	down := make([][]int, n)
	for i := 0; i < n; i++ {
		left[i] = make([]int, n)
		right[i] = make([]int, n)
		top[i] = make([]int, n)
		down[i] = make([]int, n)
	}

	// build from left
	for i := 0; i < n; i++ {
		cnt := 0
		for j := 0; j < n; j++ {
			if m[i][j] == 1 {
				left[i][j] = cnt + 1
				cnt += 1
			} else {
				cnt = 0
			}
		}
	}
	// build from right
	for i := 0; i < n; i++ {
		cnt := 0
		for j := n - 1; j >= 0; j-- {
			if m[i][j] == 1 {
				right[i][j] = cnt + 1
				cnt += 1
			} else {
				cnt = 0
			}
		}
	}
	// build from top
	for j := 0; j < n; j++ {
		cnt := 0
		for i := 0; i < n; i++ {
			if m[i][j] == 1 {
				top[i][j] = cnt + 1
				cnt += 1
			} else {
				cnt = 0
			}
		}
	}
	// build from down
	for j := 0; j < n; j++ {
		cnt := 0
		for i := n - 1; i >= 0; i-- {
			if m[i][j] == 1 {
				down[i][j] = cnt + 1
				cnt += 1
			} else {
				cnt = 0
			}
		}
	}
	// find the max
	res := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			min := find_min(left[i][j], right[i][j], top[i][j], down[i][j])
			if res < min {  res = min }
		}
	}

	// for _, row := range(m) { fmt.Println(row) }
	// fmt.Println("")
	// for _, row := range(left) { fmt.Println(row) }
	// fmt.Println("")
	// for _, row := range(right) { fmt.Println(row) }
	// fmt.Println("")
	// for _, row := range(top) { fmt.Println(row) }
	// fmt.Println("")
	// for _, row := range(down) { fmt.Println(row) }

	return res
}

func find_min(a, b, c, d int) int {
	s := []int{a, b, c, d}
	sort.Slice(s[:], func (i, j int) bool {
		return s[i] < s[j]
	})
	return s[0]
}

