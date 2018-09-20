// LEETCODE@ 854. K-Similar Strings
//
// --END--


package bfs_dfs


func kSimilarity(A string, B string) int {
	// init
	n := len(A)
	q := make([]string, 0)
	vst := make(map[string]bool)

	// run bfs
	q = append(q, A)
	swaps := 0

	for 0 < len(q) {
		sz := len(q)
		for i := 0; i < sz; i++ {
			// pop left element
			str := q[0]
			vst[str] = true
			q = q[1:]

			// if we find the target, we return the swaps
			if str == B { return swaps }

			// find first not match
			j := 0
			for j < n {
				if str[j] != B[j] { break }
				j += 1
			}
			// try to swap str[j] bewteen str[j+1] ~ str[n-1]
			for k := j + 1; k < n; k++ {
				if str[k] != B[k] && str[k] == B[j] {
					// ***A****B***
					nxtStr := str[:j] + str[k:k+1] + str[j+1:k] + str[j:j+1] + str[k+1:]
					if _, ok := vst[nxtStr]; !ok {
						q = append(q, nxtStr)
					}
				}
			}
		}
		swaps += 1

	}

	return swaps
}