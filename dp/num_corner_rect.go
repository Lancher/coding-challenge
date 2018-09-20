// 750. Number Of Corner Rectangles
//
// 1. Looks DP but not DP
//
// --END--


package dp


func countCornerRectangles(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	m, n := len(grid), len(grid[0])
	res := 0

	for i := 0; i < m; i ++ {
		for j := i + 1; j < m; j++ {
			cnt := 0
			for k := 0; k < n; k++ {
				if grid[i][k] == 1 && grid[j][k] == 1 {
					cnt += 1
				}
			}
			// Combination: x!/ (x-2)! / 2!
			res += cnt * (cnt - 1) / 2
		}
	}
	return res
}
