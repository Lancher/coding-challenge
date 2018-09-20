package array


// 755. Pour Water
//
// --END--


func pourWater(heights []int, V int, K int) []int {
	// init
	n := len(heights)

	// put a unit of water V times
	for i := 0; i < V; i ++ {
		put_idx := K

		// go from K to left and find lower index
		for j := K - 1; j >= 0; j -- {
			if heights[j] == heights[put_idx] {
				continue
			} else if heights[j] < heights[put_idx] {
				put_idx = j
			} else {
				break
			}
		}
		// go from K to right and find lower index
		if put_idx == K {
			for j := K + 1; j < n; j++ {
				if heights[j] == heights[put_idx] {
					continue
				} else if heights[j] < heights[put_idx] {
					put_idx = j
				} else {
					break
				}
			}
		}

		// not index found keep in current position
		heights[put_idx] += 1
	}

	return heights
}