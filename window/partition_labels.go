// LEETCODE@ 763. Partition Labels
//
// --END--


package window


func partitionLabels(S string) []int {
	// init
	n := len(S)

	// rightmost index
	idx := make([]int, 26)
	for i, ch := range(S) {
		idx[int(ch)-int('a')] = i
	}

	// int array
	res := make([]int, 0)

	// i, j = start, end
	i, j := 0, 0
	for j < n {
		// go to right as much as possible
		max_j := idx[int(S[j])-int('a')] + 1
		j += 1
		for j < max_j {
			next_j := idx[int(S[j])-int('a')] + 1
			j += 1
			if max_j < next_j { max_j = next_j }
		}

		// append length
		res = append(res, j - i)

		// update i
		i = j
	}

	return res
}